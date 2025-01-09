import os

from blue_objects import file, README

from blue_sandbox import NAME, VERSION, ICON, REPO_NAME


items = [
    "{}[`{}`](#) [![image]({})](#) {}".format(
        "🌐",
        "`@damage`",
        "TBA",
        "Satellite imagery damage assessment workflow",
    )
    for index in range(1, 4)
]


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
