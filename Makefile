.EXPORT_ALL_VARIABLES:

BUNDLE_GEMFILE=./build/Gemfile
PIPENV_PIPFILE=./build/Pipfile

up:
	pip install pipenv
	pipenv install
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

download-content:
	pipenv run python ./build/get_posts_from_dropbox.py
.PHONY: download-content

ci: up download-content build
.PHONY: ci

dev: download-content run
.PHONY: dev

clean:
	rm -rf ./_site
	rm -rf ./src/.jekyll-cache
	rm -rf ./src/_posts
	rm -rf ./src/_drafts
	rm -rf ./src/pages
	rm -rf ./build/Gemfile.lock
	rm -rf ./build/Pipfile.lock
.PHONY: clean

reset: clean
.PHONY: reset
