from typing import List

from blue_options.terminal import show_usage, xtra

from blue_geo.watch.targets.target_list import TargetList


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono=mono)

    target_options = "".join(
        [
            xtra("<query-object-name> | ", mono),
            "target=<target>",
        ]
    )

    target_list = TargetList()

    return show_usage(
        [
            "palisades",
            "ingest",
            f"[{options}]",
            "[.|<object-name>]",
            f"[{target_options}]",
        ],
        "ingest <target>.",
        {
            "target: {}".format(" | ".join(target_list.get_list())): [],
        },
        mono=mono,
    )


help_functions = {
    "ingest": help_ingest,
}
