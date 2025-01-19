from blueness import module

from blue_objects.metadata import post_to_object

from blue_sandbox import NAME
from blue_sandbox.logger import logger

NAME = module.name(__file__, NAME)


def complete_ingest(
    query_object_name: str,
) -> bool:
    logger.info(f"{NAME}.complete_ingest: {query_object_name}")

    return all(
        post_to_object(
            query_object_name,
            keyword,
            value,
        )
        for keyword, value in {
            "kind": "distributed",
            "source": "catalog_query",
        }.items()
    )
