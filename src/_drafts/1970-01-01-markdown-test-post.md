---
title: Markdown Test Post
date: 1970-01-01
layout: post
---

This is a test post to use for demoing how the site renders different Markdown elements. It is based on GitHub's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) guide.

----

## Headers

# This is an <h1> tag
## This is an <h2> tag
### This is an <h3> tag
#### This is an <h4> tag
##### This is an <h5> tag
###### This is an <h6> tag

## Emphasis

_This text will be italic_

**This text will be bold**

_**This text will be bold and italic**_

## Lists

### Unordered

- Item 1
- Item 2
	- Item 2a
	- Item 2b

### Ordered

1. Item 1
1. Item 2
1. Item 3
	1. Item 3a
	1. Item 3b

### Images

![Markdown Logo](https://raw.githubusercontent.com/dcurtis/markdown-mark/master/png/208x128.png)

### Links

[This is a link to GitHub.com](https://github.com)

### Blockquotes

As Kanye West said:

> We're living the future so the present is our past.

### Inline Code

I think you should use an `<addr>` element here instead.

### Syntax Highlighting

```swift
import Foundation

var pid: pid_t?
var path: String?
var uid: uid_t?
var timestamp: Date?
var ppid: pid_t?

func printDescription() {
    let descriptionValues: [String: Any?] = [
        "pid": pid,
        "path": path,
        "uid": uid,
        "timestamp": timestamp,
        "ppid": ppid ?? -1
    ]

    let nonNullDescriptionValues = descriptionValues.compactMapValues { $0 }
    let stringRepresentation = nonNullDescriptionValues.map { "\($0.0) : \($0.1)" }.joined(separator: ", ")

    print(stringRepresentation)
}

pid = 10
path = "path/to/file"
timestamp = Date()

printDescription()
```

### Horizontal Rule

----

### Task Lists

- [x] this is a complete item
- [ ] this is an incomplete item

### Tables

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

### Strikethrough

I'm going to strikethrough ~~the rest of this sentence.~~

## Non-Markdown Elements

### Definition Lists

(Not natively supported in Markdown, but can be added using raw HTML)

<dl>
	<dt>Definition List</dt>
	<dd>Allows you to define terms</dd>
</dl>

### Aside

<aside>This is an aside</aside>

### Embeds

#### YouTube

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/iy49P-8wrEw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Bandcamp

<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=2573998004/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="http://aceyalone.bandcamp.com/album/a-book-of-human-language">A BOOK OF HUMAN LANGUAGE by ACEYALONE</a></iframe>
