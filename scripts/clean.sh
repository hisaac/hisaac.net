#!/bin/bash

source "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/lib/base.sh"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	rm -rf "${PROJECT_ROOT}/node_modules"
	rm -rf "${PROJECT_ROOT}/public"
	rm -rf "${PROJECT_ROOT}/resources"
	rm -f "${PROJECT_ROOT}/.hugo_build.lock"

}

main "$@"
