.PHONY: * # all targets phony
.SILENT:  # all targets silent

project_root = $(realpath $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

all: ci

up: bootstrap-ci
bootstrap-ci:
	$(project_root)/mise/tasks/bootstrap-ci.bash $(project_root)

down: teardown
teardown:
	$(project_root)/mise/tasks/teardown.bash

ci: bootstrap-ci
	mise run build
