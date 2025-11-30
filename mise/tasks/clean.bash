#!/usr/bin/env bash

source "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")/lib/base.bash"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	rm -rf "${MISE_PROJECT_ROOT}/public"

	if [[ "${1:-}" == "nuke" ]]; then
		rm -rf "${MISE_PROJECT_ROOT}/node_modules"
		rm -rf "${MISE_PROJECT_ROOT}/resources"
		rm -f "${MISE_PROJECT_ROOT}/.hugo_build.lock"
	fi
}

main "$@"
