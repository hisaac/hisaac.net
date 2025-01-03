#!/bin/bash

source "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/lib/base.sh"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	mise_exec npx prettier --check . --config "${PROJECT_ROOT}/.prettierrc.yml"
}

main "$@"
