#! /usr/bin/env bash

function test_blue_sandbox_palisades_train() {
    local options=$1

    local query_object_name=palisades-dataset-v1

    # test is empty; train causes the github worker to crash.
    abcli_eval ,$options \
        roofai_dataset_review download \
        $query_object_name \
        --index 0 \
        --subset test
    [[ $? -ne 0 ]] && return 1

    abcli_hr

    # next step
}
