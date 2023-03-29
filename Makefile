up:
	bundle install
	pipenv install

build:
	bundle exec jekyll build --source ./src/

run:
	bundle exec jekyll serve --source ./src/
serve: run
dev: run

download-content:
	pipenv run python ./scripts/get_posts_from_dropbox.py

ci: up download-content build

clean:
	rm -rf ./_site
	rm -rf ./src/.jekyll-cache
	rm -rf ./src/_posts
	rm -rf ./src/_drafts
	rm -rf ./src/pages
reset: clean
