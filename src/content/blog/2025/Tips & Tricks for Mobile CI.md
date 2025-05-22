# Tips & Tricks for Mobile CI

## Tools

- yamllint
- shellcheck
- shfmt
- xcbeautify
- [xcresultparser](https://github.com/a7ex/xcresultparser)
- Tuist
- Bazel
- SwiftLint
- SwiftFormat
- jq
- xcodes
- yeetd
- xcodegen
- tart
- tartelet
- [Cirrus CI](https://cirrus-ci.org)
- GitHub Actions
- GitLab
- Xcode Cloud
- BuildKite
- MacStadium
- Danger

LOCK YOUR TOOL VERSIONS somehow

SPM > Carthage > Cocoapods

## Methods

### Use a Command Runner

Make is a great option for this, because it's built into the system, so there are no dependencies you have to manage. The downside is that the syntax is kind of specialized and antiquated.

There are a number of other options out there. I prefer [just](https://just.systems). Another good option is [rake](https://github.com/ruby/rake), but this one is somewhat Ruby-focused.

There are a number of advantages to using a command runner, rather than running your build scripts directly:

- It defines a consistent surface for interacting with your build scripts.
- Allows you to define dependent jobs (e.g. Every time you run anything build or test related, run the `xcode-setup` job and `download-dependencies` job first).
- You can make shortcuts that are useful to developers with predefined arguments.

If you do decide to use a build tool that is different than Make, make sure it's dead simple to set up that build tool first. Have a script at the root of the project that's easy to run (I'd suggest `up.sh`) or even a Makefile with just one target in it. Then devs have a simple command to get the bootstrapping process started. (If you have a simple Makefile with just one target, you can define your bootstrap target as the default, so new developers only have to run `make` to get their environment set up.)

### Use a `main.sh` script to route commands

You may wish to have a `main.sh` script as your entry point to most/all of your build scripts. This is a place you can parse the given arguments, and send information or arguments to other scripts as needed. Don't do too much work in this script, think of it as just a script router of sorts. "Oh, you want to run unit tests, then send the rest of your arguments to `test.sh`."

### CI Workflows

Do as little logic as possible within your CI workflow files. This is not what they are meant for. Think of your workflow files as the API between your build scripts and your CI system. Use it to trigger builds, and pass information to your scripts that are useful or necessary to perform builds (e.g. branch name, trigger type, trigger inputs, etc.).

Anything your workflow files do is trapped and difficult to test. If you write your build scripts in such a way that you can inject variables, you can easily simulate your CI environment, and test things locally without having to push them up to your code storage tool.

### Bash Scripting Tips

Bash is not nearly as bad and scary as you might think. It is very capable for many types of tasks, and is the best option for the job in many circumstances.

Here are some tips and tricks I've learned through my time writing bash:

- Use [Bash strict mode](http://redsymbol.net/articles/unofficial-bash-strict-mode/) everywhere.

- You should strive to make your build scripts functional. Rely on environment and script-level variables sparingly. As much as possible, pass anything required for a script to run into it via arguments.

- Use a base script for variables or functions that you _do_ need to have globally defined, and `source` it into your other scripts. A good example would be a project's build directory, something that may need to be referenced from multiple scripts. Keeping this consistent makes things easier.

```bash
source "$(dirname -- "$(dirname -- "$(readlink -f "${BASH_SOURCE[0]}")")")/base.sh"
```

- Within your base script, provide the ability to override things using a `.env` file, and nil-coalesce the actual value if not provided.

```bash
# Load environment variables from the .env file
if [[ -f "${PROJECT_ROOT}/.env" ]]; then
	set -o allexport
	source "${PROJECT_ROOT}/.env"
	set +o allexport
fi

# Absolute path to the directory containing the scripts
export SCRIPTS_DIR="${SCRIPTS_DIR:-${PROJECT_ROOT}/scripts}"
```

- Provide an easy way to enable debug logging.

```bash
# Output extra debug logging if `TRACE` is set to `true`
# or if `ACTIONS_STEP_DEBUG` is set to `true` (GitHub Actions)
if [[ "${TRACE:-false}" == true || "${ACTIONS_STEP_DEBUG:-false}" == true ]]; then
	set -o xtrace # Trace the execution of the script (debug)
fi
```

- Know when to move away from Bash. At some point, your build scripts may become complex and difficult to use. Moving to a new system could be beneficial.
	- If you'd like to stick with a scripting language, Python or Ruby are great options. (I personally prefer Python, but Ruby is great too. The biggest downside to both of these is that you now have to ensure a machine's Python or Ruby environment is configured correctly, which can be a pain.)
	- Alternately, consider other options like Go, Swift, or Rust. These tools have great, modern ecosystems around them.
	- You could consider something JavaScript or TypeScript-based, although I personally would stay away from that if possible. Having to manage JavaScript dependencies can be a real pain.
	- A couple ways to migrate to this system:
		- Top-down: Start with a wrapper around your existing build scripts (`main.py`, `main.rb`, etc.) that simply calls the existing build scripts. Then start working your way down the script stack, refactoring into your chosen tool/language as you go. (I'd personally recommend this option.)
		- Bottom-up: Start at the lower-level or most simple scripts, and rewrite those one at a time.
	- The key with this is that it's best to choose a new option, and stick just with that. Don't start using Python AND Ruby, just pick one and go. (I worked at a place that had a web of complex build scripts, written in Bash, Python, Ruby, Swift, and Perl. It was hell.)

- Consider building a general-purpose CLI tool focused toward your teams' needs.. This can get tricky, as every project is a special flower in its own way, so you need to provide consistency and rigidity when you can, but provide the option for flexibility when necessary. Perhaps some sort of config file at the root of a repo (YAML, TOML, etc.), which the CLI reads and changes its behavior depending on the settings there.

Whatever you choose, remember that your build scripts are software, and should be treated as such. Find ways to have unit tests and integration tests where you can. Run linters and formatters to ensure consistency. Add remote logging and reporting to be able to monitor how well your systems are running.

### Codesigning

Everyone's favorite topic, codesigning. Some notes:

- Use automatic code signing for developer debug builds on their development machines.
- Use manual code signing for _everything_ else.
- Consider hosting your code signing resources within the repo that requires them, or in one centralized repo.
	- Encrypt the certificates, and decrypt them on the fly when being used in CI using a decryption key set as a secure environment variable.
- If not hosted in the repo, you can convert them to base64 and store them as environment variables within your CI system. This is kind of a pain to be honest, but it does work.
- Interacting with the keychain from shell scripts can be error prone and can put a machine in a messy and difficult state if done incorrectly. I highly recommend testing your build scripts in an isolated environment before testing them locally. Get a second machine that you don't mind borking, or a VM that you can reset and reboot when borked.

### Build Machines

- Use frozen VM images if possible. Your life will be _SO_ much easier if you can rely on the state of your VMs being identical every time they start up.
- Cache commonly used tools or dependencies.
- Consider a tool for automatically setting up your build machines or VMs. Some options are Packer, Chef, Nix, or just custom scripts.
- If you have the option of using Linux VMs from your CI provider, consider using them for things that don't require macOS. Generally, macOS is harder to configure, and can be less reliable.

### Xcode Project Setup

- Swift Packages are great, except when they're not.
	- Limited in their abilities.
	- Project definition is static. More difficult to modify the project's build process depending on the environment or other outside variables.
		- This can be good in some instances, but can also be quite limiting. Consider that SPM only allows for Debug and Release configurations for Packages. If you have more configurations — Alpha, Beta, Release Candidate, etc. — you will not be able to utilize those within your package.
- Define your project settings in xcconfig files. Reduces pbxproj conflicts.
	- [BuildSettingExtractor](https://buildsettingextractor.com)
	- <https://nshipster.com/xcconfig/>
	- <https://pewpewthespells.com/blog/xcconfig_guide.html>
	- <https://indiestack.com/2023/10/conditional-xcode-build-settings/>
- Generate your xcodeproj — xcodegen is a great place to start, but Tuist is more powerful.

### What about Fastlane?

I've used Fastlane in the past. It is a powerful and great tool in a lot of ways, but I've found that I prefer to write my own build scripts. You get a better understanding of how they work, and crucially, how to debug, troubleshoot, and fix them when problems inevitably arise. I ran into too many instances of Fastlane breaking in some inscrutable way, and having lots of trouble sorting out the problem and getting support. There's also the frustration of managing a Ruby environment that has to be considered.

One thing to consider is that you can use Fastlane in bits and pieces. You could, for instance, use its code signing functionality specifically, and not use anything else. This might be a better approach than using everything it offers.

### Notarizing a Binary Tool

[https://github.com/a7ex/xcresultparser/blob/205604b04a684ef7c6026e01f02efffc8d9987db/notarize.sh](https://github.com/a7ex/xcresultparser/blob/205604b04a684ef7c6026e01f02efffc8d9987db/notarize.sh)

```bash
# First (if not already done) create a profile and store it in the keychain for later use with notary tool
#!/bin/sh

usage()
{
	echo ""
	echo "NAME: $0"
    echo ""
    echo "SYNOPSIS:"
    echo "$0 [-t <teamId>] [-n <productName>] [-p profileName]"
	echo ""
    echo "DESCRIPTION:"
	echo " -- Compile the app for M1 and Intel (fat) and notorize the resulting binary with Apple"
	echo ""
    echo "  The options are as follows:"
	echo "    -t | --teamId             Your Apple Developer Team Id (go to developer.apple.com, log in and scrol down.)"
    echo "    -n | --productName        The name of the product, so it can be found in the .build folder."
	echo "    -p | --profileName        The name of the credentials profile, which is stored in the keychain."
	echo "                              To create such a profile use: `xcrun notarytool store-credentials`"
    echo "    -h | --help               This help"
	echo ""
}

## Default values for this app, so I can invoke this script without parameters
productName="xcresultparser"

while [ "$1" != "" ]; do
    case $1 in
        -t | --teamId )     	shift
                            	teamId="$1"
                        		;;
        -n | --productName )	shift
                            	productName="$1"
                        		;;
        -p | --profileName ) 	shift
                            	productName="$1"
                        		;;
        -h | --help )       	usage
                        		exit
                            	;;
    esac
    shift
done

if [ -z "$teamId" ]
then
	echo "Please provide the TeamID of your Apple Developer Account"
	exit 1
fi

if [ -z "$profileName" ]
then
	echo "Please provide a profile name of the profile in your keychain, which was created using `notarytool store-credentials`"
	exit 1
fi

# build the project for M1 and Intel:
swift build -c release --arch arm64 --arch x86_64

# move the result from the .build folder to the product folder
cp ".build/apple/Products/Release/$productName" "product/$productName"

# Now codesign the app with hardening (-o)
codesign --sign "$teamId" -o runtime "product/$productName"

# Create zip archive
zip -r "product/${productName}.zip" "product/$productName"

# upload to notary
xcrun notarytool submit "product/${productName}.zip" -p "$keychainProfileName"

# ------------------------- Sample Output
# Conducting pre-submission checks for xcresultparser.zip and initiating connection to the Apple notary service...
# Submission ID received
#   id: 4a078fbf-6069-469f-8158-6de5c8e03315
# Upload progress: 100,00 % (1,39 MB of 1,39 MB)
# Successfully uploaded file
#   id: 4a078fbf-6069-469f-8158-6de5c8e03315
#   path: /Users/alex/Work/__OwnProjects/myGithub/xcresultparser/product/xcresultparser.zip
# -------------------------


#####################################################################################
################# Later call 'info' or 'log' to verify the result
# info:
# xcrun notarytool info <submission id from previous step> -p FarbflashAppleDevAccount

# ------------------------- Sample Output
# Successfully received submission info
#   createdDate: 2023-04-28T05:42:55.955Z
#   id: 4a078fbf-6069-469f-8158-6de5c8e03315
#   name: xcresultparser.zip
#   status: Accepted
# -------------------------

# log:
# xcrun notarytool log <submission id from previous step> -p FarbflashAppleDevAccount

# ------------------------- Sample Output
# {
#   "logFormatVersion": 1,
#   "jobId": "4a078fbf-6069-469f-8158-6de5c8e03315",
#   "status": "Accepted",
#   "statusSummary": "Ready for distribution",
#   "statusCode": 0,
#   "archiveFilename": "xcresultparser.zip",
#   "uploadDate": "2023-04-28T05:42:58.669Z",
#   "sha256": "b1d5cfe49f50c791c3f4b98a9c59862b18d6373f27388d6172ce4547e0b3402a",
#   "ticketContents": [
#     {
#       "path": "xcresultparser.zip/xcresultparser",
#       "digestAlgorithm": "SHA-256",
#       "cdhash": "53c2792da2debf2224eb22ee77da8a35ad9dac60",
#       "arch": "x86_64"
#     },
#     {
#       "path": "xcresultparser.zip/xcresultparser",
#       "digestAlgorithm": "SHA-256",
#       "cdhash": "ae0727572cac10aba7e38ff8a901f211a08f276d",
#       "arch": "arm64"
#     }
#   ],
#   "issues": null
# }
# -------------------------
```

## Misc

- <https://indiestack.com/2014/12/speeding-up-custom-script-phases/>
- <https://docs.tuist.io/building-at-scale/microfeatures/>
