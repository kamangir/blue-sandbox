from typing import List

from blue_options.terminal import show_usage, xtra


def help_train(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,dryrun,~upload", mono=mono)

    return show_usage(
        [
            "@damages",
            "train",
            f"[{options}]",
            "[.|<dataset-object-name>]",
            "[-|<model-object-name>]",
        ],
        "train <dataset-object-name> -> <model-object-name>.",
        mono=mono,
    )
