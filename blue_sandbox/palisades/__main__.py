import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_sandbox import NAME
from blue_sandbox.palisades.ingest import complete_ingest
from blue_sandbox.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="complete_ingest",
)
parser.add_argument(
    "--query_object_name",
    type=str,
)

args = parser.parse_args()

success = False
if args.task == "complete_ingest":
    success = complete_ingest(
        query_object_name=args.query_object_name,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
