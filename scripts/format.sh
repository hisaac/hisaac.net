#!/bin/bash

source "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/lib/base.sh"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	cd "${PUBLIC_DIR}" || exit
	mise_exec npx prettier --write . --config "${PROJECT_ROOT}/.prettierrc.yml"
}

main "$@"
