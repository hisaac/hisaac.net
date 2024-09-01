---
title: "How to Speed Up Codecov Analysis for Xcode Projects, Revisited"
date: 2024-09-01
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

## 2. Gather Information

Next, we need to locate the Profile data generated during testing. This will be a file named `Coverage.profdata`, and will be located in a subdirectory of `DerivedData/Build/ProfileData`. You can use a `find` command to locate it like so:

```bash
find "./DerivedData/Build/ProfileData" -name "Coverage.profdata"

# example result:
# ./DerivedData/Build/ProfileData/00006000-000420CA0CA3801E/Coverage.profdata
```

Finally, we need to get a list of all the test bundles generated when running our tests. These will be files with a `.xctest` extension, and will be located in various locations within `./DerivedData/Build/Products`. We can use a `find` command to locate them like so:

```bash
find "./DerivedData/Build/Products" -name "*.xctest"

# example result:
# ./DerivedData/Build/Products/Debug-iphoneos/MyAppUITests-Runner.app/PlugIns/MyAppUITests.xctest
# ./DerivedData/Build/Products/Debug-iphoneos/MyApp.app/PlugIns/MyAppTests.xctest
# ./DerivedData/Build/Products/Debug-iphoneos/.XCInstall/MyApp.app/Wrapper/MyApp.app/PlugIns/MyAppTests.xctest
```

What `llvm-cov` expects is the path to the binary within these test bundles. They will be located at the root of each bundle, and be named the same as the bundle itself. You can use the `basename` function in bash to get the name like so:

```bash
basename "./DerivedData/Build/Products/Debug-iphoneos/MyAppUITests-Runner.app/PlugIns/MyAppUITests.xctest" .xctest

# example result:
# MyAppUITests
```

## 3. Convert!

Now that we've located that information, we can pass it to the `llvm-cov export` command. The command will need to be run separately for each test bundle you're handling, so we'll run it multiple times within a loop.

Here's a simple bash script that puts all the pieces together:

```bash
#!/bin/bash

set -o errexit  # Exit on error
set -o nounset  # Exit on unset variable
set -o pipefail # Exit on pipe failure

function main() {
	declare -r coverage_profdata_path="$(
		find "./DerivedData/Build/ProfileData" -name "Coverage.profdata"
	)"

	declare -r xctest_bundles="$(
		find "./DerivedData/Build/Products" -name "*.xctest"
	)"

	# Loop through each test bundle and convert the coverage data to lcov format
	while IFS= read -r test_bundle; do

		# Get the test bundle name
		test_bundle_name="$(basename "$test_bundle" .xctest)"

		# Get the test bundle binary path
		test_bundle_binary_path="${test_bundle}/${test_bundle_name}"

		# Define where the converted coverage data will be output
		output_path="./artifacts/${test_bundle_name}.coverage.info"

		# Convert the coverage data to lcov format
		xcrun llvm-cov export --format lcov \
			--instr-profile "${coverage_profdata_path}" \
			"${test_bundle_binary_path}" >"${output_path}"

	done <<<"${xctest_bundles}"
}

main "$@"
```

This script will produce a number of text files with the extension `.coverage.info` within a directory named `artifacts`. From there, you can upload these text files to Codecov and let it work its magic!

As I said before, this does run slightly faster than the `xcresultparser` method, but the biggest win is the fact that it removes a dependency on a tool, which is always welcome.