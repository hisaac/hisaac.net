#!/usr/bin/env python3

"""
This script converts markdown files from Jekyll format to Bear format.

More info:
- Jekyll: https://jekyllrb.com/docs/step-by-step/03-front-matter/
- Bear: https://docs.bearblog.dev/post/

Warning:
    This script is bespoke to my blog, and will probably break if you try to use it.
    That said, feel free to use it as a starting point for your own script.
"""

import os
from datetime import datetime
from textwrap import dedent, indent
import pathlib
import typing

import frontmatter


def main():
    project_root = pathlib.Path(__file__).parent.parent.resolve()

    posts_dir = os.path.join(project_root, 'posts')
    recurse_posts(posts_dir)

    pages_dir = os.path.join(project_root, 'pages')
    recurse_posts(pages_dir)


def recurse_posts(post_dir):
    """
    Recursively process all markdown files in a directory.
    :param post_dir: The directory to process.
    """
    for root, subdirectories, files in os.walk(post_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_file = os.path.join(root, file)
                process_file(markdown_file)


def process_file(file):
    """
    Process a markdown file.
    :param file: The file to process.
    """
    with open(file) as file_text:
        post = frontmatter.load(file_text)
        post = process_frontmatter(post, file)
        post_content = frontmatter.dumps(post)
        post_content = process_post_content(post_content)

    with open(file, 'w') as file_text:
        file_text.write(post_content)


def process_frontmatter(post, file) -> frontmatter.Post:
    """
    Process the frontmatter of a post, converting from Jekyll to Bear.
    :param post: The post to process.
    :param file: The file the post is in.
    :return: The processed post.
    """
    post = process_layout(post)
    post = process_date(post, file)
    post = set_alias(post, file)
    post = process_categories(post)
    post = process_tags(post)
    post = process_permalink(post)
    post = process_source_and_via(post)
    return post


def process_post_content(post_content) -> str:
    """
    Process the post's content, converting from Jekyll to Bear.
    :param post_content: The post's content.
    :return: The processed post's content.
    """

    # Bear's frontmatter is delimited differently to Jekyll's
    #
    # Jekyll:
    #   ---
    #   key: value
    #   ---
    #
    # Bear:
    #   key: value
    #   ___
    post_content = post_content.replace('---', '', 1)
    post_content = post_content.replace('---', '___', 1)

    # Bear doesn't need/support wrapping a post's 'title' in quotes,
    # but the `frontmatter` library adds them if the title has special characters,
    # so we need to remove them.
    post_lines = post_content.splitlines()
    for i, line in enumerate(post_lines):
        if line.startswith('title: \'') or line.startswith('title: "'):
            post_lines[i] = line\
                .replace('\'', '', 1)\
                .replace('"', '', 1)[:-1]
            break

    # Remove empty lines at the start of the post
    if post_lines[0] == "":
        post_lines.pop(0)

    post_content = '\n'.join(post_lines)

    # Ensure the post ends with a newline
    if post_content[-1] != '\n':
        post_content += '\n'

    return post_content


def process_layout(post) -> frontmatter.Post:
    """
    Process the 'layout' tag of a post's frontmatter.
    :param post: The post to process.
    :return: The processed post.

    Bear doesn't support the 'layout' tag, so we need to remove it,
    and set the 'is_page' tag if the layout is 'page'.
    """
    if 'layout' in post.metadata:
        if post.metadata['layout'] == 'page':
            post.metadata['is_page'] = True
        del post.metadata['layout']

    return post


def process_date(post, file) -> frontmatter.Post:
    """
    Process the 'date' tag of a post's frontmatter.
    :param post: The post to process.
    :param file: The file the post is in.
    :return: The processed post.

    We use the date from the filename as the source of truth,
    just in case the post's 'date' property is different from
    the filename's date.
    """

    # Bear's name for the 'date' tag is 'published_date',
    # and since we're going to be pulling the date from the filename,
    # we'll just delete the 'date' tag.
    if 'date' in post.metadata:
        del post.metadata['date']

    date_from_filename = get_date_from_filename(file)
    if date_from_filename:
        post.metadata['published_date'] = date_from_filename.date()

    return post


def get_date_from_filename(file) -> typing.Optional[datetime]:
    """
    Get the date from a post's filename.
    :param file: The file to get the date from.
    :return: The date from the filename, or None if the filename doesn't contain a date.
    """
    filename = os.path.basename(file)
    date_text = filename.split('-', 3)
    date_text.pop()
    date_text = '-'.join(date_text)

    try:
        return datetime.fromisoformat(date_text)
    except ValueError:
        return None


def set_alias(post, file) -> frontmatter.Post:
    """
    Set the 'alias' tag of a post's frontmatter.
    :param post: The post to process.
    :param file: The file the post is in.
    :return: The processed post.

    By default, Bear uses the slugified title of a post as its URL.
        e.g. 'My Post' -> 'site.com/my-post'

    On my old Jekyll site though, I used the date in the URL instead.
        e.g. '2020-01-01-my-post.md' -> 'site.com/2020/01/01/my-post.html'

    In order to not break the links to my old posts,
    we'll set the 'alias' tag to the old URL.
    """
    if 'published_date' in post.metadata:
        filename = os.path.basename(file)
        post.metadata['alias'] = filename.replace('-', '/', 3).replace('.md', '.html')

    return post


def process_categories(post) -> frontmatter.Post:
    """
    Process the 'categories' tag of a post's frontmatter.
    :param post: The post to process.
    :return: The processed post.

    Bear doesn't support the 'categories' tag,
    so we'll just add them to the 'tags' tag.
    """
    if 'categories' in post.metadata:
        if 'tags' not in post.metadata:
            post.metadata['tags'] = []

        post.metadata['tags'] += post.metadata['categories']
        del post.metadata['categories']

    return post


def process_tags(post) -> frontmatter.Post:
    """
    Process the 'tags' tag of a post's frontmatter.
    :param post: The post to process.
    :return: The processed post.

    Bear doesn't support yaml's list syntax for tags,
    so we'll convert the tags to a comma-separated string.
    """
    if 'tags' in post.metadata:
        tags = post.metadata['tags']
        tags = [tag.lower() for tag in tags]
        tags = ', '.join(tags)
        post.metadata['tags'] = tags
    return post


def process_permalink(post) -> frontmatter.Post:
    """
    Process the 'permalink' tag of a post's frontmatter.
    :param post: The post to process.
    :return: The processed post.

    Bear doesn't support the 'permalink' tag,
    so we'll just delete it.
    """
    if 'permalink' in post.metadata:
        del post.metadata['permalink']
    return post


def process_source_and_via(post) -> frontmatter.Post:
    """
    Process the 'source' and 'via' tags of a post's frontmatter.
    :param post: The post to process.
    :return: The processed post.

    Bear doesn't support the 'source' and 'via' tags
    (Jekyll doesn't technically either, they're custom tags I added),
    but I'd like to retain the information, so we'll add it to the bottom
    of the post's content as a definition list.
    """
    if 'source' in post.metadata or 'via' in post.metadata:
        post_meta_url_text = dedent(
            f"""

            ***

            <dl>
            """
        )

        if 'source' in post.metadata:
            source = post.metadata['source']
            del post.metadata['source']

            html = f"""\
                <dt>Source:</dt>
                <dd><a href="{source}">{source}</a></dd>
            """
            dedented_html = dedent(html)
            post_meta_url_text += indent(dedented_html, '\t')

        if 'via' in post.metadata:
            via = post.metadata['via']
            del post.metadata['via']

            html = f"""\
                <dt>Found via:</dt>
                <dd><a href="{via}">{via}</a></dd>
            """
            dedented_html = dedent(html)
            post_meta_url_text += indent(dedented_html, '\t')

        post_meta_url_text += "</dl>"
        post.content += post_meta_url_text

    return post


if __name__ == '__main__':
    main()
