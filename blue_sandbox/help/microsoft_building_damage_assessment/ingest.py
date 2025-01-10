from typing import List

from blue_options.terminal import show_usage, xtra

list_of_events = [
    "Maui-Hawaii-fires-Aug-23",
    "<event_name>",
]


def help_(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~download,dryrun,", mono=mono),
            "event=<event>",
            xtra(",~gdal,~rm,~upload", mono=mono),
        ]
    )

    args = [
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@damage",
            "ingest",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "ingest <event> -> <object-name>.",
        {
            "event: {}".format(" | ".join(list_of_events)): [],
        },
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "events"

    usage_1 = show_usage(
        [
            "@damage",
            "ingest",
            "list",
            f"[{options}]",
        ],
        "list events.",
        mono=mono,
    )

    options = "event=<event>"

    usage_2 = show_usage(
        [
            "@damage",
            "ingest",
            "list",
            f"[{options}]",
            "<suffix>",
        ],
        "list <event> acquisitions.",
        mono=mono,
    )

    return "\n".join(
        [
            usage_1,
            usage_2,
        ]
    )


help_functions = {
    "": help_,
    "list": help_list,
}
