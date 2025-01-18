#! /usr/bin/env bash

function test_blue_sandbox_palisades_train() {
    local options=$1

    local query_object_name=palisades-dataset-v1

    abcli_eval ,$options \
        roofAI_dataset_review download \
        $query_object_name
    [[ $? -ne 0 ]] && return 1

    abcli_hr

    # next step
}
