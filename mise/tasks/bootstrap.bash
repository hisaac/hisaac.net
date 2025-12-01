#!/usr/bin/env bash

# shellcheck source=mise/lib/base.bash
source "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")/lib/base.bash"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	local -r project_root="${1:-$MISE_PROJECT_ROOT}"
	if ! command -v mise &>/dev/null; then
		install_mise
	else
		update_mise
	fi
	install_mise_plugins
}

function install_mise {
	info "Installing mise"
	if command -v brew &>/dev/null; then
		brew install mise
		local -r mise_path="$(brew --prefix mise)"
	else
		curl https://mise.run | sh
		local -r mise_path="${HOME}/.local/bin/mise"
	fi
	mise trust --yes
	eval "$("${mise_path}" activate -C "${project_root}" bash --shims)"
}

function update_mise {
	info "Updating mise"
	if command -v brew &>/dev/null; then
		brew upgrade mise
	else
		mise self-update --yes || true # Ignore errors if mise is already up-to-date
	fi
}

function install_mise_plugins {
	info "Installing mise plugins"
	mise plugins update
	mise install --yes
	mise upgrade --bump
	mise reshim
}

main "$@"
