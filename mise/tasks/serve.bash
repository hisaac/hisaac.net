#!/usr/bin/env bash

# shellcheck source=mise/lib/base.bash
source "$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")/lib/base.bash"
trap 'exit_handler "$?" "${0##*/}"' EXIT

function main {
	hugo --config "${MISE_PROJECT_ROOT}/hugo.yml" \
		server --buildDrafts --buildFuture --gc --disableFastRender
}

main "$@"
