#!/bin/bash

source "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/lib/base.sh"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	mise_exec npx --prefix "${CONFIG_DIR}" \
		prettier --write . --ignore-path "${CONFIG_DIR}/.prettierignore"
}

main "$@"
