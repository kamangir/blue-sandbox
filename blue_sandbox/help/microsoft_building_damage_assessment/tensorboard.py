from typing import List

from blue_options.terminal import show_usage, xtra


def help_tensorboard(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun,port=<8889>", mono=mono)

    return show_usage(
        [
            "@damages",
            "tensorboard",
            f"[{options}]",
            "[.|<model-object-name>]",
        ],
        "tensorboard the model.",
        mono=mono,
    )
