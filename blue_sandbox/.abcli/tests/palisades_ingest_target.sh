#! /usr/bin/env bash

function test_blue_sandbox_palisades_ingest_target() {
    local options=$1

    abcli_eval ,$options \
        blue_sandbox_palisades ingest ~upload \
        target=Palisades-Maxar --
}
