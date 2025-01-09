from blueness import module

from blue_sandbox import NAME
from blue_sandbox.logger import logger


NAME = module.name(__file__, NAME)


def ingest(object_name: str) -> bool:
    logger.info(f"{NAME}.ingest -> {object_name}")

    return True
