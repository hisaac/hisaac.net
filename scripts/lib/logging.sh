#!/bin/bash

# If `TERM` is set to `dumb`, set it to `xterm`
# This is needed for the `tput` commands to work on GitHub Actions runners
if [[ "${TERM}" == dumb ]]; then
	export TERM=xterm
fi

# Only do this if `XCODE_VERSION_ACTUAL` is not set, because if it is set, we're running in
# Xcode, and Xcode can't use `tput` for pretty logging
if [[ -z "${XCODE_VERSION_ACTUAL:-}" ]]; then
	text_red=$(tput setaf 1)
	text_yellow=$(tput setaf 3)
	text_blue=$(tput setaf 4)
	text_bold=$(tput bold)
	text_reset=$(tput sgr0)
fi

function info() {
	echo -e "${text_blue:-}==>${text_bold:-} ${1:-}" "${text_reset:-}"
}

function warn() {
	echo -e "${text_yellow:-}==>${text_bold:-} ${1:-}" "${text_reset:-}"
}

function error() {
	echo -e "${text_red:-}ERROR:${text_bold:-} ${1:-}" "${text_reset:-}" >&2
}

# Output extra debug logging if `TRACE` is set to `true`
if [[ "${TRACE:-false}" == true ]]; then
	set -o xtrace # Trace the execution of the script (debug)
fi
