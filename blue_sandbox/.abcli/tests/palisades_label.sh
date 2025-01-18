#! /usr/bin/env bash

function test_blue_sandbox_palisades_label() {
    local options=$1

    abcli_eval ,$options \
        blue_sandbox_palisades_label \
        download,offset=0 \
        ~QGIS \
        palisades-dataset-v1
}
