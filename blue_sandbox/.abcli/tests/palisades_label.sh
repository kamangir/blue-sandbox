#! /usr/bin/env bash

function test_blue_sandbox_palisades_label() {
    local options=$1

    local query_object_name=palisades-dataset-v1

    abcli_eval ,$options \
        blue_sandbox_palisades_label \
        download,offset=0 \
        ~QGIS \
        $query_object_name
    [[ $? -ne 0 ]] && return 1

    abcli_eval ,$options \
        roofai_dataset_review - \
        $query_object_name \
        --index 0 \
        --subset train
}
