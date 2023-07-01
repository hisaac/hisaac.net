---
title: "Contextually Open GitHub via the Command Line"
date: 2023-03-29
layout: post
tags: [software]
---

# Contextually Open GitHub via the Command Line

Here's a little `fish` function I whipped up to open GitHub in the web browser depending on the current state of the repo:

```shell
function gv --description 'Opens the current repository in the browser, trying first to open a pull request, then a branch, then the repository itself'
    set -l current_branch (git symbolic-ref --short HEAD)
    set -l pr_url (gh pr list --head "$current_branch" --state OPEN --json url --jq '.[0].url')

    git rev-parse --abbrev-ref $current_branch@{upstream} >/dev/null 2>&1
    set -l remote_branch_exists $status # 0 if the branch exists, something else if it doesn't

    if test -n "$pr_url"
        echo "Opening pull request $pr_url"
        open $pr_url
    else if test "$remote_branch_exists" -eq 0
        and test "$current_branch" != main
        and test "$current_branch" != master
        echo "Opening branch '$current_branch'"
        gh browse --branch $current_branch
    else
        echo "Opening repository"
        gh browse
    end
end
```

In summary:

1. First, if there is an existing pull request for the current branch, open that.
2. Then, if there is a remote branch being tracked by the local branch, open that.
3. Finally, if none of the above match, just open the repo's main page.

---

I know `fish` isn't as popular as the venerable `bash`, so here's a version as a `bash` script:

(I haven't fully tested this version, so it may not work as expected.)

```shell
#!/bin/bash

CURRENT_BRANCH=$(git symbolic-ref --short HEAD)
PR_URL=$(gh pr list --head "${CURRENT_BRANCH}" --state OPEN --json url --jq '.[0].url')

git rev-parse --abbrev-ref "${CURRENT_BRANCH}@{upstream}" >/dev/null 2>&1
REMOTE_BRANCH_EXISTS=$? # 0 if the branch exists, something else if it doesn't

if [[ -n "${PR_URL}" ]]; then
	echo "Opening pull request ${PR_URL}"
	open "${PR_URL}"
elif [[ "$REMOTE_BRANCH_EXISTS" == 0 && "${CURRENT_BRANCH}" != main && "${CURRENT_BRANCH}" != master ]]; then
	echo "Opening branch '${CURRENT_BRANCH}'"
	gh browse --branch "${CURRENT_BRANCH}"
else
	echo "Opening repository"
	gh browse
fi
```
