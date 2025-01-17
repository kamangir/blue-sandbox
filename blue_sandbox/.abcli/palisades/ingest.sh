#! /usr/bin/env bash

function blue_sandbox_palisades_ingest() {
    local options=$1
    local target_options=$2
    local datacube_ingest_options=$3

    blue_geo_watch_targets_download

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload 0)

    local target=$(abcli_option "$target_options" target)
    local query_object_name
    if [[ -z "$target" ]]; then
        query_object_name=$target_options

        abcli_download - $query_object_name
    else
        query_object_name=palisades-$target-query-$(abcli_string_timestamp_short)

        blue_geo_watch_query \
            $target_options \
            $query_object_name
        [[ $? -ne 0 ]] && return 1
    fi

    local ingest_object_name=$(abcli_clarify_object $4 $query_object_name-ingest-$(abcli_string_timestamp))

    abcli_log "🪄"
}
