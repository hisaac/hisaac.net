---
title: "Update All the Things"
date: 2018-02-12
layout: post
tags: tech, bash, mac
---

The other day, I was wishing for an easy way to update all of the [CLI](https://en.wikipedia.org/wiki/Command-line_interface) package managers on my computer at once, rather than having to type each command separately. Then I realized, this would be a great job for a bash/zsh alias!

Here’s what I’ve come up with. I call it `update-all-the-things`:

```bash
alias update-all-the-things='
	echo "🍺 Updating Homebrew" ; brew upgrade ;
	echo "🚀 Updating Global Node Modules" ; npm update -g ;
	echo "💎 Updating RubyGems" ; gem update'
```

I think it would be fun to make this into an actual package itself someday. A super simple little [Homebrew](https://brew.sh) or [NPM](https://www.npmjs.com) package would be fun to make. Have any ideas on how to implement it as its own package? Any package managers I'm missing? Let me know!
