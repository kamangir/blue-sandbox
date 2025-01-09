import os

from blue_objects import file, README

from blue_sandbox import NAME, VERSION, ICON, REPO_NAME


items = ["wip 🔥"] + 2 * [""]


def build():
    return README.build(
        items=items,
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
