up:
	bundle install
	pipenv install

up-ci:
	bundle install --without development
	pipenv install

ci: up-ci download_content build
dev: up download_content build

build:
	bundle exec jekyll build --source ./src/

run:
	bundle exec jekyll serve --source ./src/

download_content:
	pipenv run python ./scripts/get_posts_from_dropbox.py

clean:
	rm -rf ./_site
	rm -rf ./src/.jekyll-cache
	rm -rf ./src/_posts
	rm -rf ./src/_drafts
	rm -rf ./src/pages
