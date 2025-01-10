from typing import List

from blue_options.terminal import show_usage, xtra


def help_label(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,dryrun,~upload", mono=mono)

    return show_usage(
        [
            "@damages",
            "label",
            f"[{options}]",
            "[.|<dataset-object-name>]",
        ],
        "label <dataset-object-name>.",
        mono=mono,
    )
