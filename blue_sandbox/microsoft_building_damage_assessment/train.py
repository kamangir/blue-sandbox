import os

from blueness import module
from blue_objects import mlflow, metadata, file, objects
from blue_objects.env import abcli_path_git

from blue_sandbox import NAME
from blue_sandbox.logger import logger


NAME = module.name(__file__, NAME)


# ... copy `configs/example_config.yml` and fill the first three sections.
def train(
    dataset_object_name: str,
    model_object_name: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.train: {dataset_object_name} -> {model_object_name}")

    config_filename = os.path.join(
        abcli_path_git,
        "building-damage-assessment/configs/example_config.yml",
    )
    success, config = file.load_yaml(config_filename)
    if not success:
        return False

    ...

    if not file.save_yaml(
        objects.path_of(
            filename="config.yml",
            object_name=model_object_name,
        ),
        config,
    ):
        return False

    return all(
        [
            mlflow.set_tags(
                model_object_name,
                {
                    "dataset": dataset_object_name,
                },
            ),
            metadata.post_to_object(
                model_object_name,
                "train",
                {
                    "dataset": dataset_object_name,
                },
            ),
        ]
    )
