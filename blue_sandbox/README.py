import os

from blue_objects import file, README

from blue_sandbox import NAME, VERSION, ICON, REPO_NAME


items = [
    "{}[`{}`]({}) [![image]({})]({}) {}".format(
        "🌐",
        "`@damage`",
        "https://github.com/kamangir/blue-sandbox/blob/microsoft-building-damage-assessment-2025-01-09-chRAIH/blue_sandbox/microsoft_building_damage_assessment/README.md",
        "https://github.com/microsoft/building-damage-assessment/raw/main/figures/damage.png",
        "Satellite imagery damage assessment workflow",
        "https://github.com/kamangir/blue-sandbox/blob/microsoft-building-damage-assessment-2025-01-09-chRAIH/blue_sandbox/microsoft_building_damage_assessment/README.md",
    )
] + 2 * [""]


def build():
    return README.build(
        items=items,
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    ) and README.build(
        path=os.path.join(file.path(__file__), "microsoft_building_damage_assessment"),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
