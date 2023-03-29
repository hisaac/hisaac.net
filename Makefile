.EXPORT_ALL_VARIABLES:

BUNDLE_GEMFILE=./build/Gemfile
PIPENV_PIPFILE=./build/Pipfile

up:
	pip install pipenv
	pipenv install
	bundle install

build:
	bundle exec jekyll build --source ./src/
.PHONY: build

run:
	bundle exec jekyll serve --source ./src/
serve: run

download-content:
	pipenv run python ./build/get_posts_from_dropbox.py

ci: up download-content build
dev: download-content run

clean:
	rm -rf ./_site
	rm -rf ./src/.jekyll-cache
	rm -rf ./src/_posts
	rm -rf ./src/_drafts
	rm -rf ./src/pages
reset: clean
