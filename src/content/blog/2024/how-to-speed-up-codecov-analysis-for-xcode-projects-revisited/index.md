---
title: "How to Speed Up Codecov Analysis for Xcode Projects, Revisited"
date: 2024-09-01
updated: 2026-04-17
tags: [xcode, software, programming, swift, apple]
---

In a [previous post]({{< ref "how-to-speed-up-codecov-analysis-for-xcode-projects" >}}), I outlined a method for converting Xcode's code coverage format to a format that [Codecov](https://codecov.io) can ingest. This method relied on an open source tool called [`xcresultparser`](https://github.com/a7ex/xcresultparser).

Since writing that post, I've found a new method that is slightly faster and — more importantly — removes the dependency on external tools, instead relying solely on tools included within Xcode's command line tools.

Codecov lists the code coverage formats it natively accepts in its documentation here: [Supported Coverage Report Formats](https://docs.codecov.com/docs/supported-report-formats). Among the accepted formats is `lcov`.

Xcode includes a tool called `llvm-cov`, which can be called from the command line using `xcrun`:

```shell
xcrun llvm-cov
```

`llvm-cov`'s has a number of subcommands, but the one we're interested in is `export`. This command does the conversion we need from Xcode's native format to the more interoperable `lcov` format.

## 1. Run the Tests

In order to use the `export` command, we'll need to gather a couple dependencies that need to be passed to it in order to do the conversion.

First, we need to know the location of the DerivedData directory. In order to isolate your test results to just the tests that you care about, I recommend using the `-derivedDataPath` flag to specify the location of DerivedData explicitly in whatever `xcodebuild` command you use to run your tests. (I usually just put it at the present working directory for easy future reference.)

```shell
xcrun xcodebuild test -derivedDataPath ./DerivedData ...
```

## 2. Convert the Coverage Data

You'll need to fill in the app name and test target name in the following commands, but the general process is as follows:

```shell
xcrun llvm-cov export \
	--format lcov \
	--ignore-filename-regex "DerivedData" \
	--instr-profile DerivedData/Build/ProfileData/*/Coverage.profdata \
	DerivedData/Build/Products/Debug-iphonesimulator/<app_name>.app/<app_name>.debug.dylib \
	> coverage.info
```

If needed, you can also post-process the `coverage.info` file to remove relative paths to the source files, which can be done with a simple `sed` command like so:

```shell
sed -i '' sed "s|SF:$(pwd)/|SF:|" coverage.info
```

## Conclusion

This method is slightly faster than the `xcresultparser` method, but the biggest win is the fact that it removes a dependency on a tool, which is always welcome.
