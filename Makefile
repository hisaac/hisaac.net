.EXPORT_ALL_VARIABLES:

BUNDLE_GEMFILE=./build/Gemfile

up:
	bundle install
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
.PHONY: clean

reset: clean
.PHONY: reset
