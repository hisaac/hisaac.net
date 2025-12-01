.PHONY: * # all targets phony
.SILENT:  # all targets silent

project_root = $(realpath $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

all: bootstrap

up: bootstrap
bootstrap:
	$(project_root)/mise/tasks/bootstrap.bash $(project_root)

down: teardown
teardown:
	$(project_root)/mise/tasks/teardown.bash
