up:
	bundle install

build:
	bundle exec jekyll build --source ./src/

run:
	bundle exec jekyll serve --source ./src/

clean:
	rm -rf _site
	rm -rf .jekyll-cache
