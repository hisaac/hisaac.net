---
title: "A More Personal Database"
date: 2025-01-27
tags: [database, software, airtable, obsidian]
---

Lately I've been on the hunt for a personal database application that I could use to store, manipulate, and explore data important to me. I think I'm at least now able to articulate what it is I want, but I haven't yet been able to find anything that perfectly matches the daydream.

## The Daydream

Put simply, I want a user-friendly GUI that wraps a real database, but that is meant to be run and used locally. Something like [Airtable](https://airtable.com/), but intended to be run locally instead of in a web browser. (And no, a self-hosted version doesn't count. I don't want or need to run this as a server application.)

The UI would intentionally obscure most of the databasey bits, just like Airtable does.

- Friendly data types over database primitives. Types like [Airtable's "text", "number", "rating", "image", etc.](https://support.airtable.com/docs/supported-field-types-in-airtable-overview). Sure these friendly data types are built upon basic database primitives like `BOOLEAN` and `varchar(255)`, I don't want to have to care about that.
- Similarly, I don't want to have to care about SQL queries (by default). Really there should be no mention of the term "SQL" anywhere, unless a user wants to dig into that.

A lot of this is inspired by Steph Ango's [File over App](https://stephango.com/file-over-app) ideology, and the way it's been applied to [[Obsidian]]. I want the app to be offline-first, and built upon durable, open file formats without lock-in. (Probably either [SQLite](https://www.sqlite.org/) or something NoSQL like [MongoDB](https://www.mongodb.com/) that can store its data as flat JSON files.)

## Current Options

[Beekeeper Studio](https://www.beekeeperstudio.io/) gets closest to what I'm envisioning. It's designed to be run on a PC, not in a web browser. It has a spreadsheet-like view for manipulating the database. It even has things called [Query Magics](https://docs.beekeeperstudio.io/user_guide/query-magics/) that are custom SQL queries you can run to apply some nicer UI to your database. But still, you have to know what a SQL query is. You still have to *think about* the fact that there's a database under there doing things.

I also like what [Simon Willison](https://simonwillison.net/) is doing with [Datasette](https://datasette.io/). It's a tool for viewing, exploring, and sharing data. I'd love for some of these ideas to be applied to Beekeeper somehow.

For now I'm going to give Beekeeper a try and see if it can fit enough of my needs to suffice. It is missing some things I'd like, but it's also open source and community-driven, so maybe I could contribute, or at least discuss my vision with the community.
