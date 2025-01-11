from typing import List

from blue_options.terminal import show_usage, xtra


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("recreate_env,dryrun", mono=mono)

    return show_usage(
        [
            "@damages",
            "install",
            f"[{options}]",
        ],
        "install @damages.",
        mono=mono,
    )
