.EXPORT_ALL_VARIABLES:

BUNDLE_GEMFILE=./build/Gemfile

up:
	bundle install
	npm --prefix ./build ci
.PHONY: up

build:
	bundle exec jekyll build --source ./src/
.PHONY: build

run:
	bundle exec jekyll serve --source ./src/
.PHONY: run

serve: run
.PHONY: serve

ci: up build
.PHONY: ci

dev: run
.PHONY: dev

clean:
	rm -rf ./_site
	rm -rf ./src/.jekyll-cache
	rm -rf ./build/Gemfile.lock
	rm -rf ./build/node_modules
.PHONY: clean

reset: clean
.PHONY: reset
