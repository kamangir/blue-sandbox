from typing import List

from blue_options.terminal import show_usage, xtra


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    return show_usage(
        [
            "@sam",
            "install",
        ],
        "install @sam.",
        mono=mono,
    )


help_functions = {
    "install": help_install,
}
