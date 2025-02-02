import os

from blue_objects import file, README
from blue_options.help.functions import get_help

from blue_sandbox import NAME, VERSION, ICON, REPO_NAME
from blue_sandbox.list import list_of_experiments

items = [
    "[`{}`]({}) {} [![image]({})]({}) {}".format(
        experiment_name,
        experiment["url"],
        experiment.get("status", "⏸️"),
        experiment.get(
            "marquee",
            "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true",
        ),
        experiment["url"],
        experiment["title"],
    )
    for experiment_name, experiment in list_of_experiments.items()
    if experiment_name != "template"
]


def build():
    return all(
        README.build(
            items=thing.get("items", []),
            cols=thing.get("cols", 3),
            path=os.path.join(file.path(__file__), thing["path"]),
            help_function=thing.get("help_function", None),
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
        )
        for thing in (
            [
                {
                    "items": items,
                    "path": "..",
                },
            ]
        )
    )
