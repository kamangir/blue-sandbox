from blue_objects import objects
from roofai.semseg.model import SemSegModel
from roofai.semseg.train import SemSegModelTrainer
from roofai.semseg import Profile

from blue_sandbox.logger import logger


def predict(
    model_object_name: str,
    datacube_id: str,
    prediction_object_name: str,
    device: str,
    profile: Profile = Profile.VALIDATION,
    in_notebook: bool = False,
) -> bool:
    model = SemSegModel(
        model_filename=objects.path_of(
            filename="model.pth",
            object_name=model_object_name,
        ),
        profile=profile,
        device=device,
    )

    ...

    logger.info("🪄")

    return True
