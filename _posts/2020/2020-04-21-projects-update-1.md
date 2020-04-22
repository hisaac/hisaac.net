---
title: "Projects Update #1"
date: 2020-04-21
layout: post
tags: "projects update"
---

A semi-regular and overly verbose update on my personal projects.

## Completed

### [hisaac.net](https://hisaac.net) 3.0.0

Work on version 3.0.0 of this website is basically complete! There are a few odds and ends that still need to be wrapped up before it's "officially" launched, and I still need to write a wrap-up post about the new redesign, but it is basically ready to go. Please [reach out](mailto:new-site-feedback@hisaac.net) if you have any feedback on the new design. Seriously.

## In Progress

### Mac mini Server

I recently acquired a 2012 Mac mini to use as a home server, to replace a QNAP NAS. I've got multiple projects in flight related to the server.

#### Set up [Arq](https://www.arqbackup.com) to backup the computer.

The first step here is to decide on a backup destination. On my personal machine, I'm currently using Backblaze's [B2 Cloud Storage](https://www.backblaze.com/b2/cloud-storage.html). I've been happy with it in every way except the price. I've currently got 8.7 TB backed up there, and it costs me around $45/month. I could probably slim that down by thinning my backups, but I haven't explored that yet. Either way, that's way more than I'd like to pay.

I _very_ rarely access my backup data, so I plan to move to an "archive class" cloud storage solution. The cost is far cheaper, but you are charged to retrieve your data. I'm most likely going to use Amazon's [S3 Glacier](https://aws.amazon.com/glacier/) class storage. I already use AWS for my web hosting and related things, and am marginally familiar with the service, so using it for backups seems appropriate.

#### Migrate eBooks to [Calibre](https://calibre-ebook.com)

Calibre is the de facto standard for eBook library management. It's a gross app, but it's powerful and has tons of support online. I've got eBooks and comic books strewn about in files that I'd like to import and organize within Calibre.

### Moving from Evernote to Notion

I've wanted to move away from [Evernote](https://evernote.com) for a long time now, but until recently, hadn't actually started the process. The biggest issue I had was that I hadn't yet found a suitable replacement.

Enter [Notion](https://notion.so). Notion is something I'd heard about before — and even tried out briefly — but never gave any serious thought to it. I'd recently been hearing a lot about it in my online circles, so I decided to give it another look.

It meets most of the requirements that I had for a catchall notes replacement:

- Good apps for both iOS and macOS
	- It can also be accessed via the web, which wasn't a requirement, but is a nice-to-have
- Ability to host notes as web pages for easy public access
	- I plan to use Notion as a wiki, to replace what I've currently called "living documents"
- Ability to embed multimedia within notes
- Easy Evernote import
	- Notion actually has the ability to connect directly to Evernote's API. Every other service I've tested required you to export your notes from Evernote into their proprietary `.enex` file format, then import them into the app, often with middling results. Notion's Evernote import is _worlds_ better — both faster and more reliable.
- Easy export of notes
	- Notion has multiple export options, including Markdown! 🎉

There are also some cons to Notion:

- The macOS app is an [Electron](https://www.electronjs.org) app
	- I'd _much_ prefer a native app, but the Notion app is at least a decent Electron app. Not great[^1] by any means, but decent enough.
- The iOS app is not great
	- It does not work offline, and some of the functionality can be cumbersome. That said, it's passable, and it meets my needs.
- Notion has the concept of plain notes, but there are also "databases"
	- The database feature is confusing to me. I can't decide if it's confusing just because I don't yet understand it, or confusing because it's confusing. Only time will tell.

Overall, the pros outweigh the cons, so the migration has started. And the more I use the app and service, the more I like it. I'd say I'm about 60% of the way through. I'm also using the time to clean through a lot of the cruft that has built up in my Evernote database. Once this is completed, I'll have a fresh clean notes database to use for hopefully a very long time.

I just looked, and I've got an Evernote premium subscription until July 16<sup>th</sup> of this year. That day will come fast!

## Upcoming

### Research Dynamic DNS Options

I'd like to setup dynamic DNS on my Mac mini server so that I can actually host some things on it for personal access outside my home. I need to research the options to decide which service to go with, as well as the potential security/privacy implications.

### Buy New Sweatpants

My favorite sweatpants have started to get holes in them, so I need to buy a new pair. Have a favorite pair of your own to recommend? [Let me know what they are!](mailto:sweatpants@hisaac.net)

### Buy a New Wi-Fi Router

I'd like to get a new Wi-Fi router that supports Wi-Fi 6 (a.k.a. 802.11ax). Research has just started on this, so I haven't got much idea yet what to get.

### Buy a Bike Trailer

This will be my son's first full Summer, and my wife and I are eager to get outside with him on our bikes. I need to find a good bike trailer to put him in. Hopefully one that can also double as a stroller.

### Moving Research

We're planning to buy a house in the next year or two, and research and discussion is continuing on what type of housing we'd look for (leaning toward a town home right now), and where we'd like to live. A current favorite of mine is Ramsey, Minnesota's ["COR" neighborhood](https://www.ci.ramsey.mn.us/531/The-COR).

[^1]: I think the only Electron app I'd bestow the "great" adjective too would be [Visual Studio Code](https://code.visualstudio.com). It's amazing that that thing is built on web technologies.
