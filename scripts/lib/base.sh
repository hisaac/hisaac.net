#!/bin/bash

# To use this in your script, add
#
# 	source "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/lib/base.sh"
# 	trap 'exit_handler "$?" "${0##*/}"' EXIT
#
# at the top of your script

set -o errexit  # Exit on error
set -o nounset  # Exit on unset variable
set -o pipefail # Exit on pipe failure

source "$(dirname -- "$(readlink -f "${BASH_SOURCE[0]}")")/logging.sh"

# "public" functions - run by consumers

function mise_exec {
	mise exec -- "$@"
}

function exit_handler {
	declare -ri exit_code="$1"
	declare -r script_name="$2"
	if [[ "${exit_code}" -ne 0 ]]; then
		error "${script_name} exited with code ${exit_code}"
	elif [[ "${VERBOSE:-false}" == true ]]; then
		info "${script_name} exited with code ${exit_code}"
	fi
}

# "private" functions - run on script load

function _export_vars {
	declare -r project_root="$(dirname "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")")"
	export PROJECT_ROOT="${project_root}"
	export PUBLIC_DIR="${project_root}/public"
}
_export_vars

function _load_mise {
	declare -r mise_path="${HOME}/.local/bin/mise"
	if [[ -f "${mise_path}" ]]; then
		eval "$("${mise_path}" activate -C "$PROJECT_ROOT" bash --shims)"
	else
		warn "mise not found in expected location: ${mise_path}"
		warn "Please run 'make up' to install mise"
	fi
}
_load_mise
