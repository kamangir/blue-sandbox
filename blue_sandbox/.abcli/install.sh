#! /usr/bin/env bash

function abcli_install_blue_sandbox() {
    abcli_git_clone https://github.com/microsoft/building-damage-assessment.git
    [[ $? -ne 0 ]] && return 1

    # https://github.com/microsoft/building-damage-assessment?tab=readme-ov-file#setup
    conda env create \
        -f $abcli_path_git/building-damage-assessment/environment.yml
    [[ $? -ne 0 ]] && return 1

    [[ "$abcli_is_mac" == true ]] &&
        brew install wget

    return 0
}

abcli_install_module blue_sandbox 1.1.1
