from typing import List
import segmentation_models_pytorch as smp
import numpy as np
from tqdm import tqdm
import torch
import cv2

from blueness import module
from blue_objects import objects, file
from blue_objects.metadata import post_to_object
from blue_objects.logger.matrix import log_matrix
from blue_options.elapsed_timer import ElapsedTimer
from roofai.semseg.model import SemSegModel
from roofai.semseg import Profile
from roofai.semseg.augmentation import get_validation_augmentation, get_preprocessing
from blue_geo.catalog import get_datacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope

from blue_sandbox import NAME
from blue_sandbox.palisades.geo.dataset import GeoDataset
from blue_sandbox.logger import logger


NAME = module.name(__file__, NAME)


def predict(
    model_object_name: str,
    datacube_id: str,
    prediction_object_name: str,
    device: str,
    profile: Profile = Profile.VALIDATION,
    in_notebook: bool = False,
    batch_size: int = 32,
) -> bool:
    model = SemSegModel(
        model_filename=objects.path_of(
            filename="model.pth",
            object_name=model_object_name,
        ),
        profile=profile,
        device=device,
    )

    datacube = get_datacube(datacube_id)
    list_of_files = datacube.list_of_files(scope=DatacubeScope("rgb"))
    if not list_of_files:
        logger.error("cannot find a reference file.")
        return False

    reference_filename = list_of_files[0]
    logger.info(f"reference: {reference_filename}")

    logger.info(
        "{}.predict: {}/{} -{}-batch-size:{}-> {}".format(
            NAME,
            datacube_id,
            reference_filename,
            device,
            batch_size,
            prediction_object_name,
        )
    )

    preprocessing_fn = smp.encoders.get_preprocessing_fn(
        model.encoder_name,
        model.encoder_weights,
    )

    dataset = GeoDataset(
        filename=objects.path_of(
            filename=reference_filename,
            object_name=datacube_id,
        ),
        augmentation=get_validation_augmentation(),
        preprocessing=get_preprocessing(preprocessing_fn),
        count=model.profile.data_count,
    )

    index_list = (
        [np.random.choice(len(dataset))]
        if model.profile == Profile.VALIDATION
        else range(len(dataset))
    )
    timer = ElapsedTimer()
    list_of_masks: List[np.ndarray] = []
    for i in tqdm(range(0, len(index_list), batch_size)):
        batch_indices = index_list[i : i + batch_size]
        images = [dataset[n][0] for n in batch_indices]

        x_tensor = torch.from_numpy(np.stack(images)).to(model.device)
        pr_masks = model.model.predict(x_tensor)
        pr_masks = pr_masks.cpu().numpy().round()
        list_of_masks += [pr_masks]
    timer.stop()
    logger.info(f"took {timer.elapsed_pretty()}")

    stack_of_masks = np.concatenate(list_of_masks, axis=0)

    logger.info(f"stitching {stack_of_masks.shape[0]:,} chips...")
    output_matrix = np.zeros(dataset.matrix.shape[:2], dtype=np.uint8)
    weight_matrix = np.zeros(dataset.matrix.shape[:2], dtype=np.uint8)
    chip_index: int = 0
    for y in range(
        0,
        dataset.matrix.shape[0] - dataset.chip_height,
        int(
            dataset.chip_overlap * dataset.chip_height,
        ),
    ):
        for x in range(
            0,
            dataset.matrix.shape[1] - dataset.chip_width,
            int(
                dataset.chip_overlap * dataset.chip_width,
            ),
        ):
            output_matrix[
                y : y + dataset.chip_height,
                x : x + dataset.chip_width,
            ] += (
                stack_of_masks[chip_index, 0] > 0.5
            ).astype(np.uint8)

            weight_matrix[
                y : y + dataset.chip_height,
                x : x + dataset.chip_width,
            ] += 1

            chip_index += 1
            if chip_index >= len(dataset):
                break
        if chip_index >= len(dataset):
            break

    output_matrix = output_matrix / weight_matrix
    if not log_matrix(
        matrix=output_matrix,
        header=[],
        footer=[],
        dynamic_range=[0, 1],
        filename=objects.path_of(
            filename=file.add_extension(
                file.add_suffix(
                    reference_filename,
                    suffix="prediction",
                ),
                "png",
            ),
            object_name=prediction_object_name,
        ),
        colormap=cv2.COLORMAP_JET,
    ):
        return False

    # TODO: generate whole image

    # TODO: generate geoimage

    # TODO: generate geojson

    return post_to_object(
        prediction_object_name,
        "predict",
        {
            "elapsed_time": timer.elapsed_time,
        },
    )
