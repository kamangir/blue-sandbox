from blue_sandbox.help.microsoft_building_damage_assessment.ingest import (
    help_functions as help_ingest,
)
from blue_sandbox.help.microsoft_building_damage_assessment.ingest import list_of_events
from blue_sandbox.help.microsoft_building_damage_assessment.install import help_install
from blue_sandbox.help.microsoft_building_damage_assessment.label import help_label
from blue_sandbox.help.microsoft_building_damage_assessment.train import help_train

help_functions = {
    "ingest": help_ingest,
    "install": help_install,
    "label": help_label,
    "train": help_train,
}
