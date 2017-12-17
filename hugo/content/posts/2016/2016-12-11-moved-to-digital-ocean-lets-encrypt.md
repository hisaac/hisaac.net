---
title: "Moved to Digital Ocean + Let's Encrypt"
tags: internet, tech, webdev
date: 2016-12-11T01:24:57-06:00
---

A quick update: I just moved both [hisaac.net](http://hisaac.net) and [hisaac.blog](http://hisaac.blog) to an Ubuntu VPS at [Digital Ocean](http://digitalocean.com). I'd previously been hosting through GitHub pages, but I wanted a little more control. This way, I can host both sites in one place, and get to learn more about servers, Linux, and Apache. The only issue now is git commits. I need to find a way to commit to GitHub *and* the VPS at the same time. Currently, I'm commiting from my local machine to GitHub, and then pulling the changes from GitHub to the VPS. It's not a very efficient routine.

I also enabled SSL on both domains using [Let's Encrypt](http://letsencrypt.com). I followed [this guide](https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04), and it was surprisingly easy.

One note if you decide to use that guide: It's slightly out of date. They mention near the beginning:

> Although the Let's Encrypt project has renamed their client to `certbot`, the client included in the Ubuntu 16.04 repositories is simply called `letsencrypt`. This version is completely adequate for our purposes.

For me, using `letsencrypt` didn't work, and I used `certbot` instead.
