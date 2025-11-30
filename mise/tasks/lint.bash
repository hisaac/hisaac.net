#!/usr/bin/env bash

source "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")/lib/base.bash"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	mise_exec npx prettier --check . --config "${MISE_PROJECT_ROOT}/.prettierrc.yml"
	mise fmt --check
}

main "$@"
