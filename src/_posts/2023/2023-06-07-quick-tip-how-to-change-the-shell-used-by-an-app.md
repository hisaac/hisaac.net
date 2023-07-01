---
title: "Quick Tip: How To Change the Shell Used by an App"
date: 2023-06-07
layout: post
tags: [software, macos]
via: https://eli.li/acme
---

# Quick Tip: How To Change the Shell Used by an App

If you need to force an application on your Mac (and probably Linux too?) to use a specific shell on your system, it can be accomplished by setting the `SHELL` environment variable.

This can be done either within a script:

```bash
#!/bin/bash
export SHELL=/bin/bash
open -a "/Applications/SuperCoolApp.app"
```

Or can be done right at the command line:

```shell
SHELL=/bin/bash open -a "/Applications/SuperCoolApp.app"
```

Bam! My thanks to my good friend [Eli](https://eli.li) for the tip on this.

## But… Why?

So why on earth would you want to do this? Let's say you've got an application that runs shell commands as a part of its operation. Ideally, the app would explicitly target a specific shell to ensure compatibility across systems, but it also might just default to whatever your system's login shell is. I ran into the latter case, and the commands being run by the application were failing because they were not compatible with my preferred shell, [`fish`](https://fishshell.com). So now I just open the application using the shell command above, and voilà! All works as it should.
