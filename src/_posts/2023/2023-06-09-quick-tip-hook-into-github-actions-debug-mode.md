---
title: "Quick Tip: Hook Into GitHub Actions' Debug Mode"
date: 2023-06-09
layout: post
tags: [software, github]
---

# Quick Tip: Hook Into GitHub Actions' Debug Mode

Whenever re-running a job on GitHub Actions, there is a handy toggle for [debug logging](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/enabling-debug-logging).

![The "Re-run jobs" pop-up within GitHub Actions, showing the "Enable debug logging" check box at the bottom]({% asset_path debug-logging-toggle.png %})
*The "Re-run jobs" pop-up within GitHub Actions*

Checking this prints out some extra information on the next run of the job, but by default is limited to information about GitHub's execution of the script, not about what happens _during_ the actual run.

The way this toggle works is that it sets a secret named `ACTIONS_STEP_DEBUG` to `true`. GitHub's step execution process then reads this value, and prints out the extra information. Just like any secret in a GitHub Action though, we can also read this and use it to our liking.

Because this is a "secret" and not a "variable", we have to do a tiny bit of work in order for our builds to have access to the value. Like any other secret, this can be done by reassigning the value of the secret to a variable manually in an `env` block:

{% raw %} <!-- needed to escape the variable in the yaml below 🙄 -->
```yaml
env:
  ACTIONS_STEP_DEBUG: ${{ secrets.ACTIONS_STEP_DEBUG }}
```
{% endraw %}

Now any script or process run by the action can check the value of `ACTIONS_STEP_DEBUG`, and use it to print out extra logging information.

## How I Use This in Bash

I add the following to any Bash script that I use in my builds:

```bash
# Output extra debug logging if `TRACE` is set to `true`
# or if `ACTIONS_STEP_DEBUG` is set to `true` (GitHub Actions)
if [[ "${TRACE:-false}" == true || "${ACTIONS_STEP_DEBUG:-false}" == true ]]; then
	set -o xtrace # Trace the execution of the script (debug)
fi
```

This allows us to read the value of that secret to print debug information on CI, as well as do so locally by setting `TRACE=true`. Usually we just do this directly when we invoke the script.

```shell
TRACE=true ./scripts/do-stuff.sh
```

The above methods can be used in any language that supports reading of environment variables. For example, here's how you'd do it in Swift:

```swift
let environment = ProcessInfo.processInfo.environment
if environment["TRACE"] == "true" || environment["ACTIONS_STEP_DEBUG"] == "true" {
	logger.debugMode = true
}
```
