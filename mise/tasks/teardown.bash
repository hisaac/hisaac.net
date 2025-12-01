#!/usr/bin/env bash

# shellcheck source=mise/lib/base.bash
source "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")/lib/base.bash"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main() {
	if command -v mise &>/dev/null; then
		mise implode --yes
	fi
	if command -v brew &>/dev/null; then
		brew uninstall mise --force
	fi
}

main "$@"
