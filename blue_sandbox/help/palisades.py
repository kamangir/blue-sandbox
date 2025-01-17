from typing import List

from blue_options.terminal import show_usage, xtra

from blue_geo.watch.targets.target_list import TargetList
from blue_geo.help.datacube import scope_details
from blue_geo.help.datacube import ingest_options as datacube_ingest_options


target_list = TargetList(catalog="maxar_open_data")


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~download,dryrun,", mono=mono),
            "upload",
        ]
    )

    target_options = "".join(
        [
            "target=<target>",
            xtra(" | <query-object-name>", mono),
        ]
    )

    ingest_options = "".join(
        [
            xtra("~ingest_datacubes | ", mono=mono),
            datacube_ingest_options(mono=mono),
        ]
    )

    return show_usage(
        [
            "palisades",
            "ingest",
            f"[{options}]",
            f"[{target_options}]",
            f"[{ingest_options}]",
        ],
        "ingest <target>.",
        {
            "target: {}".format(" | ".join(target_list.get_list())): [],
            **scope_details,
        },
        mono=mono,
    )


help_functions = {
    "ingest": help_ingest,
}
