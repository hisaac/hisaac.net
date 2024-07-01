# config
.PHONY: *    # all targets phony
$(V).SILENT: # all targets silent

# variables
mkfile_path  := $(abspath $(lastword $(MAKEFILE_LIST)))
project_root := $(realpath $(dir $(mkfile_path)))
scripts_dir  := $(project_root)/scripts

# targets

up:
	"$(scripts_dir)/up.sh"

build:
	"$(scripts_dir)/generate-syntax.sh"
	"$(scripts_dir)/build.sh"

format:
	"$(scripts_dir)/format.sh"

lint:
	"$(scripts_dir)/lint.sh"

run:
	"$(scripts_dir)/run.sh"

clean:
	"$(scripts_dir)/clean.sh"

ci: up build format
reset: clean run
