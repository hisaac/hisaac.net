up:
	bundle install

build:
	bundle exec jekyll build

run:
	bundle exec jekyll serve

clean:
	rm -rf _site
	rm -rf .jekyll-cache
