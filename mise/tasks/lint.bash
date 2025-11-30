#!/usr/bin/env bash

# shellcheck source=mise/lib/base.bash
source "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")/lib/base.bash"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	npx prettier --check . --config "${MISE_PROJECT_ROOT}/.prettierrc.yml"
	mise fmt --check
}

main "$@"
