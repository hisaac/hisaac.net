---
title: "Set an Xcode Project's DerivedData Location via Script"
date: 2023-06-02
layout: post
tags: [software, xcode, script]
---

# Set an Xcode Project's DerivedData Location via Script

Say the words "Derived Data" to any Apple platform developer, and they will immediately cringe, remembering painful times of deleting the directory just to get Xcode to behave properly.

I’m here to tell you, there is a better way! (Or at least a slight improvement.)

[(Skip ahead for the tl;dr)](#the-solution)

## Some Context

Lately, I've taken to setting my Xcode projects to keep their derived data folders alongside the project itself. Xcode calls this a "Project-relative Location", and it can be set in the UI by navigating to "File" > "Project Settings…" in the menu bar. You'll be presented with a window, where you can change the "Derived Data:" drop-down to "Project-relative Location".

Now whenever Xcode runs a build, it will place the derived data right next to your project. This has a number of advantages.

1. If you need to clear derived data, you can do it on a per-project basis, without effecting any other project.
2. Any Swift Package dependencies get placed in this directory (`DerivedData/<project_name>/SourcePackages/`).
3. Having a consistent location means you can more easily refer to or use any built artifacts (e.g. For launching development versions of a macOS app for testing outside of Xcode).

![The project settings window, with the "Project-relative Location" option set]({% asset_path per-user-project-settings-window.png %})
*The project settings window*

This setting is a "per-user" setting though, which ideally should be included in your `.gitignore` file, which means it will not get checked in and saved.

Previously, I would go manually set this setting on the projects that I worked on, but why use a mouse when you could use a script instead!

## <a name="the-solution">The Solution</a>

Here's the Bash script I came up with to perform the modifications needed on whichever project or workspace you pass to it:

```bash
#!/usr/bin/env bash

# This script sets the user-specific Derived Data location setting
# for the given Xcode project or workspace to be "project-relative"
# and next to the project or workspace.

set -o errexit  # Exit on error
set -o nounset  # Exit on unset variable
set -o pipefail # Exit on pipe failure

# Output extra debug logging if `TRACE` is set to `true`
if [[ "${TRACE:-false}" == true ]]; then
	set -o xtrace # Trace the execution of the script (debug)
fi

help() {
	echo "Usage: $0 <path/to/project[.xcodeproj | .xcworkspace]>"
}

main() {
	if [[ $# -ne 1 ]]; then
		help
		exit 1
	fi

	case "$1" in
	*.xcodeproj) ;;
	*.xcworkspace) ;;
	-h | --help)
		help
		exit 0
		;;
	*)
		help
		exit 1
		;;
	esac

	set_local_derived_data "$1"
}

set_local_derived_data() {
	# Absolute path to the `.xcodeproj` or `.xcworkspace` file
	local PROJECT_FILE=$1

	if [[ ! -d "$PROJECT_FILE" ]]; then
		echo "Error: $PROJECT_FILE does not exist or is not a directory"
		exit 1
	fi

	# Absolute path to the current user's `xcuserdatad` directory
	local XCUSERDATAD_DIR
	if [[ "$PROJECT_FILE" == *".xcodeproj" ]]; then
		XCUSERDATAD_DIR="${PROJECT_FILE}/project.xcworkspace/xcuserdata/$(whoami).xcuserdatad"
	elif [[ "$PROJECT_FILE" == *".xcworkspace" ]]; then
		XCUSERDATAD_DIR="${PROJECT_FILE}/xcuserdata/$(whoami).xcuserdatad"
	fi

	# Create the `xcuserdatad` directory if it doesn't exist
	mkdir -p "$XCUSERDATAD_DIR"

	WORKSPACE_SETTINGS_PLIST_PATH="${XCUSERDATAD_DIR}/WorkspaceSettings.xcsettings"

	# Create the `WorkspaceSettings.xcsettings` file if it doesn't exist
	if [[ ! -f "$WORKSPACE_SETTINGS_PLIST_PATH" ]]; then
		plutil -create xml1 "$WORKSPACE_SETTINGS_PLIST_PATH"
	fi

	# Set the Derived Data settings
	plutil -replace BuildLocationStyle -string UseAppPreferences "$WORKSPACE_SETTINGS_PLIST_PATH"
	plutil -replace CustomBuildLocationType -string RelativeToDerivedData "$WORKSPACE_SETTINGS_PLIST_PATH"
	plutil -replace DerivedDataCustomLocation -string DerivedData "$WORKSPACE_SETTINGS_PLIST_PATH"
	plutil -replace DerivedDataLocationStyle -string WorkspaceRelativePath "$WORKSPACE_SETTINGS_PLIST_PATH"

	# Validate the `WorkspaceSettings.xcsettings` file
	plutil -lint "$WORKSPACE_SETTINGS_PLIST_PATH"
}

main "$@"
```

Simply call the script and pass it the path to an `.xcodeproj` or `.xcworkspace`, and it will do the modifications for you.

```shell
./set-local-derived-data.sh <path/to/project.xcodeproj>
```

Enjoy your newly local DerivedData directory!
