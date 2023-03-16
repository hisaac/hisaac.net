import frontmatter
import os
from datetime import datetime
from textwrap import dedent, indent


def recurse_posts(post_dir):
    for root, subdirectories, files in os.walk(post_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_file = os.path.join(root, file)
                process_file(markdown_file)


def process_file(file):
    with open(file) as f:
        post = frontmatter.load(f)
        post = convert_frontmatter_to_bear_format(post, file)
        frontmatter.dumps(post, f)


def convert_frontmatter_to_bear_format(post, file):
    post = process_layout(post)
    post = process_date(post, file)
    post = set_alias(post, file)
    post = process_categories(post)
    post = process_permalink(post)
    post = process_source_and_via(post)
    return post


def process_layout(post):
    if 'layout' in post.metadata:
        if post.metadata['layout'] == 'page':
            post.metadata['is_page'] = True
        del post.metadata['layout']

    return post


def process_date(post, file):
    if 'date' in post.metadata:
        del post.metadata['date']

    date_from_filename = get_date_from_filename(file)
    if date_from_filename:
        post.metadata['published_date'] = date_from_filename

    return post


def get_date_from_filename(file):
    filename = os.path.basename(file)
    date_text = filename.split('-', 3)
    date_text.pop()

    if len(date_text) <= 1:
        return None

    date_text = '-'.join(date_text)
    date = datetime.fromisoformat(date_text)
    return date


def set_alias(post, file):
    if 'published_date' in post.metadata:
        filename = os.path.basename(file)
        post.metadata['alias'] = filename.replace('-', '/', 3).replace('.md', '')

    return post


def process_categories(post):
    if 'categories' in post.metadata:
        if 'tags' not in post.metadata:
            post.metadata['tags'] = []

        post.metadata['tags'] += post.metadata['categories']
        del post.metadata['categories']

    return post


def process_permalink(post):
    if 'permalink' in post.metadata:
        del post.metadata['permalink']
    return post


def process_source_and_via(post):
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
    recurse_posts('posts')
