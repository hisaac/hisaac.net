#!/usr/bin/env bash

# shellcheck source=mise/lib/base.bash
source "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")/lib/base.bash"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	if ! command -v mise &>/dev/null; then
		install_mise
	else
		update_mise
	fi
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
	eval "$("${mise_path}" activate -C "$MISE_PROJECT_ROOT" bash --shims)"
}

function update_mise {
	info "Updating mise"
	if command -v brew &>/dev/null; then
		brew upgrade mise
	else
		mise self-update --yes || true # Ignore errors if mise is already up-to-date
	fi
}

main "$@"
