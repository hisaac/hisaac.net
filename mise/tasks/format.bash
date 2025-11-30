#!/usr/bin/env bash

source "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")/lib/base.bash"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	cd "${PUBLIC_DIR}" || exit
	mise_exec npx prettier --write . --config "${MISE_PROJECT_ROOT}/.prettierrc.yml" "!css/vendors/**"
	mise fmt
}

main "$@"
