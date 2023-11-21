#!/usr/bin/env python3

"""
This script will take a RYM list and convert it to a markdown file.
"""
from pathlib import Path
from textbundle import TextBundle


def main():
	project_root = Path(__file__).parent.parent.resolve()
	content_dir = project_root.joinpath('content')
	posts_dir = content_dir.joinpath('posts')
	pages_dir = content_dir.joinpath('pages')
	static_dir = content_dir.joinpath('static')
	posts = gather_textbundles(posts_dir)
	print("posts:", posts)
	pages = gather_textbundles(pages_dir)
	print("pages:", pages)


def gather_textbundles(directory: Path) -> list[TextBundle]:
	"""
	Recursively find all textbundles in a directory.
	:param directory: The directory to process.
	"""
	textbundles: list[TextBundle] = []
	for root, subdirectories, files in directory.walk():
		for subdirectory in subdirectories:
			if subdirectory.endswith('.textbundle'):
				textbundle = TextBundle.from_path(Path(root, subdirectory))
				textbundles.append(textbundle)
	return textbundles


if __name__ == "__main__":
	main()
