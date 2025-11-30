#!/usr/bin/env bash

# shellcheck source=mise/lib/base.bash
source "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")/lib/base.bash"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	cd "${PUBLIC_DIR}" || exit
	npx prettier --write . --config "${MISE_PROJECT_ROOT}/.prettierrc.yml" "!css/vendors/**"
	mise fmt
}

main "$@"
