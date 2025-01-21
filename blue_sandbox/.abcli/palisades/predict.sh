#! /usr/bin/env bash

function blue_sandbox_palisades_predict() {
    local options=$1
    $abcli_gpu_status_cache && local device=cuda || local device=cpu
    local device=$(abcli_option "$options" device $device)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))
    local profile=$(abcli_option "$options" profile VALIDATION)

    local model_object_name=$(abcli_clarify_object $2 ..)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $model_object_name

    local datacube_id=$(abcli_clarify_object $3 .)

    local prediction_object_name=$(abcli_clarify_object $4 predict-$datacube_id-$(abcli_string_timestamp_short))

    abcli_log "semseg[$model_object_name].predict($datacube_id) -$device-@-$profile-> $prediction_object_name."

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_sandbox.palisades predict \
        --device $device \
        --model_object_name $model_object_name \
        --datacube_id $datacube_id \
        --prediction_object_name $prediction_object_name \
        --profile $profile \
        "${@:5}"
    local status="$?"

    abcli_mlflow_tags_set \
        $prediction_object_name \
        datacube_id=$datacube_id,model=$model_object_name,profile=$profile

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $prediction_object_name

    return $status
}
