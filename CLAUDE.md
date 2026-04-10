# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Isaac Halvorson's personal website and blog at [hisaac.net](https://hisaac.net), built with [Hugo](https://gohugo.io) (a Go-based static site generator). Content is written in Markdown. The site is deployed automatically to Netlify on push to `main`.

## Tooling

All tools are managed via [mise](https://mise.jdx.dev). Run `mise install` to get everything set up.

### Common commands

```sh
mise run build      # Build the site (outputs to public/)
mise run rebuild    # Clean then build
mise run check      # Run all linters (alias: chk, lint)
mise run fix        # Run all linters in fix mode (alias: format, fmt)
mise run bootstrap  # Run hugo mod tidy (also runs automatically post-install)
mise run upg        # Upgrade all tools and Hugo modules
```

There are no tests — this is a static site.

Linting is handled by [hk](https://github.com/jdx/hk), configured in `hk.pkl`. It runs golangci-lint, shellcheck, shfmt, yamlfmt, yamllint, and several generic fixers (smart quotes, line endings, trailing whitespace). It runs automatically as a pre-commit hook.

## Hugo version lock

**Hugo is pinned to `0.152` in `mise.toml`.** Do not upgrade it without testing carefully. Versions 0.153+ have two bugs that break this site's build:

1. WebP image encoding OOM crash — [gohugoio/hugo#14282](https://github.com/gohugoio/hugo/issues/14282)
2. Dart Sass WASM panic — `panic: call with ID 0 not found` in `warpc.go`, triggered by `hugo-admonitions` SCSS compilation (unreported as of 2026-04-10)

## Site architecture

### Directory layout

All source files live under `src/` — this is non-standard for Hugo and configured explicitly in `hugo.yml`:

```
src/
  assets/       # CSS files (reset.css, styles.css, syntax.css)
  content/      # Markdown content
  layouts/      # Hugo templates
  static/       # Static files (favicon, humans.txt)
  themes/       # (empty — theme is self-contained in layouts/)
```

Hugo is configured via `hugo.yml` (not the default `hugo.toml`/`hugo.yaml`). Always pass `--config hugo.yml` when running Hugo directly.

### Content structure

```
src/content/
  blog/         # Blog posts, organized by year/slug/index.md
  about/
  canon/
  projects/
  CenterMouse/  # macOS app page
  more.md
  artifacts.md
```

Blog posts live at `src/content/blog/YYYY/slug/index.md`. Images for a post go in an `assets/` subdirectory alongside its `index.md` and are referenced as `assets/filename.jpg` in Markdown.

### Hugo module

The site is itself a Hugo module (`module hisaac.net` in `go.mod`). It imports one external module: `github.com/KKKZOZ/hugo-admonitions`, which provides GitHub-style alert blockquotes (`> [!tip]`, `> [!note]`, etc.) with SCSS styling.

### Image processing

The custom render hook at `src/layouts/_default/_markup/render-image.html` intercepts all Markdown images and:
- Converts them to WebP and JPEG using Hugo's image processing pipeline
- Generates a tiny base64-encoded JPEG placeholder (3px wide) for lazy loading
- Wraps everything in a `<figure>` / `<picture>` element

This means images in posts **must be page resources** (i.e., placed in the post's `assets/` directory), not external URLs. The hook silently does nothing for images that aren't page resources.

### Templates

- `baseof.html` — shell with `<head>`, `<header>`, `<main>`, `<footer>`
- `home.html` — homepage: groups blog posts by year, shows tag list
- `list.html` — used for blog section and tag pages
- `single.html` — individual post pages, shows title, date, tags
- `rss.xml` — custom RSS template that only includes blog posts and outputs full content

### RSS feed

The RSS feed URL is `/feed.xml` (not the default `/index.xml`), configured via `outputFormats.rss.baseName: feed` in `hugo.yml`.

### Front matter

Blog posts use standard Hugo front matter:

```yaml
---
title: "Post title"
date: 2025-01-15
tags: [tag1, tag2]
---
```

Optional: `link` (renders as an external link in lists), `author`, `description`.
