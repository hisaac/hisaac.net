#!/usr/bin/env bash

source "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")/lib/base.bash"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	if command -v mise &>/dev/null; then
		install_mise
	fi

	install_mise_plugins
	install_hugo_plugins
}

function brew_install_mise {
	brew install mise
	eval "$("${mise_path}" activate -C "$MISE_PROJECT_ROOT" bash --shims)"
}

function install_mise {
	info "Installing mise"
	if command -v brew &>/dev/null; then
		brew install mise
	else
		curl https://mise.run | sh
	fi
	eval "$("${mise_path}" activate -C "$MISE_PROJECT_ROOT" bash --shims)"
}

function update_mise {
	info "Updating mise"
	mise self-update --yes || true # Ignore errors if mise is already up-to-date
}

function install_mise_plugins {
	info "Installing mise plugins"
	mise install --yes
	mise upgrade --bump
	mise reshim
}

function install_hugo_plugins {
	info "Installing Hugo plugins"
	mise_exec hugo version
	mise_exec hugo mod get -u ./...
}

main "$@"
