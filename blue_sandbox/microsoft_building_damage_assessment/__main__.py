import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_sandbox import NAME
from blue_sandbox.microsoft_building_damage_assessment.ingest import ingest
from blue_sandbox.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="ingest",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--verbose",
    type=bool,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "ingest":
    success = ingest(args.arg)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
