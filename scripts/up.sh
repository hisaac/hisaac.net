#!/bin/bash

source "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/lib/base.sh"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	declare -r mise_path="${HOME}/.local/bin/mise"
	if [[ ! -f "${mise_path}" ]]; then
		install_mise
	else
		update_mise
	fi

	install_plugins
}

function install_mise {
	info "Installing mise"
	curl https://mise.run | sh
	eval "$("${mise_path}" activate -C "$SRCROOT" bash --shims)"
}

function update_mise {
	info "Updating mise"
	mise self-update --yes || true # Ignore errors if mise is already up-to-date
}

function install_plugins {
	info "Installing mise plugins"
	mise install --yes
}

main "$@"
