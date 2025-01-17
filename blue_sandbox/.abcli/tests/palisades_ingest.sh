#! /usr/bin/env bash

function test_blue_sandbox_palisades_ingest_target() {
    local options=$1

    abcli_eval ,$options \
        blue_sandbox_palisades \
        ingest \
        ~upload \
        target=Palisades-Maxar \
        - \
        -
}

function test_blue_sandbox_palisades_ingest_query() {
    local options=$1

    abcli_eval ,$options \
        blue_sandbox_palisades \
        ingest \
        ~upload \
        $PALISADES_TEST_QUERY_OBJECT_NAME \
        - \
        -
}

function test_blue_sandbox_palisades_ingest_target_ingest_datacubes() {
    local options=$1

    abcli_eval ,$options \
        blue_sandbox_palisades \
        ingest \
        ~upload \
        target=Palisades-Maxar-test \
        ingest_datacubes,scope=rgb \
        -
}
