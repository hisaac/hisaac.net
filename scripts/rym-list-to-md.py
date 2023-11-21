#!/usr/bin/env python3

"""
This script will take a RYM list and convert it to a markdown file.
"""

import requests
from bs4 import BeautifulSoup
import pathlib


def main():
	project_root = pathlib.Path(__file__).parent.parent.resolve()

	# list_url = "https://rateyourmusic.com/list/hisaac/best-of-2023/"
	# list_html = get_list_html_from_url(list_url)
	list_path = f"{project_root}/scripts/list-full.html"
	list_html = get_list_html_from_file(list_path)
	list_content = process_list_html(list_html)

	for release in list_content:
		print(vars(release))


def get_list_html_from_url(list_url):
	headers = requests.utils.default_headers()
	headers.update({
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
	})

	list_html = requests.get(list_url, headers=headers).text
	return list_html


def get_list_html_from_file(list_path):
	with open(list_path, "r") as f:
		list_html = f.read()
	return list_html


def process_list_html(list_html):
	soup = BeautifulSoup(list_html, "html.parser")
	user_list = soup.find("table", {"id": "user_list"})
	release_list = []

	for table_row in user_list.find_all("tr"):
		if not table_row.has_attr("class"):
			continue
		if "show-for-small-table-row" in table_row["class"]:
			continue

		artist = table_row.find("a", {"class": "list_artist"}).text
		artist = artist.replace("\n", " ").replace("\t", "")
		artist_link = table_row.find("a", {"class": "list_artist"})["href"]

		title = table_row.find("a", {"class": "list_album"}).text
		album_link = table_row.find("a", {"class": "list_album"})["href"]

		rel_date = table_row.find("span", {"class": "rel_date"}).text
		release_date = rel_date[rel_date.find("(") + 1:rel_date.find(")")]

		artwork_url = None
		if table_row.find("img"):
			if table_row.find("img").has_attr("data-src"):
				artwork_url = table_row.find("img")["data-src"]
			elif table_row.find("img").has_attr("src"):
				artwork_url = table_row.find("img")["src"]

		release = Release(artist, artist_link, title, album_link, release_date, artwork_url)
		release_list.append(release)

	return release_list


class Release:
	def __init__(self, artist, artist_link, title, link, release_date, artwork_url):
		self.artist = artist
		self.artist_link = artist_link
		self.title = title
		self.link = link
		self.release_date = release_date
		self.artwork_url = artwork_url

	def __str__(self):
		return f"{self.artist} - {self.title} ({self.release_date})"


if __name__ == "__main__":
	main()
