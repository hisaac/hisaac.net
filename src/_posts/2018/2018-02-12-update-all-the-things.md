---
title: "Update All the Things"
date: 2018-02-12
layout: post
tags: [tech, bash, mac]
---

The other day, I was wishing for an easy way to update all of the [CLI](https://en.wikipedia.org/wiki/Command-line_interface) package managers on my computer at once, rather than having to type each command separately. Then I realized, this would be a great job for a bash/zsh alias!

Here’s what I’ve come up with. I call it `update-all-the-things`:

```shell
alias update-all-the-things='
	echo "🍺 Updating Homebrew" ; brew upgrade ;
	echo "\n🛢 Updating Casks" ; brew cask upgrade ;
	echo "\n🚀 Updating Global Node Modules" ; npm update -g ;
	echo "\n💎 Updating RubyGems" ; gem update ;
	echo "\n🐍 Updating pip" ;
		pip install --upgrade pip setuptools wheel ;
		pip freeze --local | grep -v "^-e" | cut -d = -f 1 | xargs pip install -U
	echo "\n🐉 Updating pip3" ;
		pip3 install --upgrade pip setuptools wheel ;
		pip3 freeze --local | grep -v "^-e" | cut -d = -f 1 | xargs pip3 install -U
'
```

I think it would be fun to make this into an actual package itself someday. A super simple little [Homebrew](https://brew.sh) or [NPM](https://www.npmjs.com) package would be fun to make. Have any ideas on how to implement it as its own package? Any package managers I'm missing? Let me know!
