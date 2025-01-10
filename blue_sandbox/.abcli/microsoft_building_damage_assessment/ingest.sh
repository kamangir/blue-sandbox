#! /usr/bin/env bash

function blue_sandbox_microsoft_building_damage_assessment_ingest() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))
    local event_name=$(abcli_option "$options" event default)

    local object_name=$(abcli_clarify_object $2 $event_name-ingest-$(abcli_string_timestamp_short))

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_sandbox.microsoft_building_damage_assessment \
        ingest \
        --event_name $event_name \
        --object_name $object_name \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return $status
}
