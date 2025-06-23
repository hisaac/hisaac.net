# Difficulties of Building Catalyst Apps on CI

I recently had my first experience trying to build a Mac Catalyst app in CI, and ran into more roadblocks than I expected. I also had a very hard time finding good information online on the topic, so I wanted to write some things I learned here in hopes that it helps someone else in the future (and let’s be honest, I’ll probably forget it all soon and be grateful for the reference down the road).

Catalyst apps exist in this weird space between being an iOS app and being a macOS app. When trying to spin up a macOS version of an existing iOS app, Catalyst can be an excellent option, but it presents some interesting and unexpected challenges when it comes to building and code signing the app. Apple’s code signing system is already complex as it is, so this just makes matters worse.

With a typical iOS app, in order to run the app on a physical device, you must sign the app with a certificate, and provide a provisioning profile

## macOS App

After many failed attempts, I eventually learned that it is not feasible to run unit tests of a Mac Catalyst app on a virtual machine that we don't have control of. This is due to some code signing particularities specific to Catalyst apps. Catalyst apps exist in this weird space in between iOS and macOS apps where some requirements of each platform are necessary.

For a standard iOS app, in order to run a debug build, the app needs to be code signed with a certificate, and have a provisioning profile that includes the specific device that the app is being run on. The Simulator gets around this by not requiring the provisioning profile to authorize the Simulator.

For a standard macOS app, code signing is not required to run a debug build, so you can just explicitly disable it to run unit tests.

Mac Catalyst apps on the other hand have the same code signing requirements as an iOS app — they need to be signed with a certificate and use a provisioning profile that includes the specific device the app is being run on. In this case though, the device it is running on is a Mac, and there is no Mac Simulator that would allow us to get around the provisioning profile requirement.

There are a few possible ways to get this to work:

1. Sign into an Apple ID within Xcode, and enable automatic code signing
2. Register the Mac device to the provisioning profile being used before running the tests

As far as I know, option 1 is not possible to do from a script. You'd need access to the machine/VM in order to click around and sign into the account within Xcode.

Option 2 could conceivably be done through a script, but it would require registering the virtual machine with our Apple developer account, adding the machine to the provisioning profile, downloading the newly updated provisioning profile, and installing it on the machine. While this is all technically possible — either with Fastlane, or a complex script of our own — it runs the risk of hitting the dev account's 100 device limit rather quickly, not to mention it adds quite a bit of complexity to the build.

So, for now, CI is *building* the macOS app — this is possible to do without the code signing shenanigans — but it's not running any tests.

We do plan to get the macOS unit tests running in CI at some point, but we're going to have to wait on it for the time being. The options we have are to run the tests on the 2 Mac minis we have hosted in a Tandem data center, or running them on a VM that we *do* control. The latter is preferred. We're going to investigate switching to running our builds on MacStadium, which would allow us to accomplish the latter option.

.mobileprovision for iOS and .provisionprofile for macOS

## Resources

[Continuous Integration with Github Actions for macOS and iOS projects](https://rhonabwy.com/2020/05/09/continuous-integration-with-github-actions-for-macos-and-ios-projects/)

[GitHub - heckj/MPCF-TestBench: Tooling for benchmarking Multipeerconnectivity framework on apple platforms](https://github.com/heckj/MPCF-TestBench)

[Catalyst Requires Code Signing? | Apple Developer Forums](https://developer.apple.com/forums/thread/699085)

[Supported capabilities (macOS) - Reference - Account - Help - Apple Developer](https://developer.apple.com/help/account/reference/supported-capabilities-macos)

[Supported capabilities (iOS) - Reference - Account - Help - Apple Developer](https://developer.apple.com/help/account/reference/supported-capabilities-ios)

[Resolving common notarization issues | Apple Developer Documentation](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution/resolving_common_notarization_issues#3087731)

![CleanShot 2023-05-16 at 15.00.12.png](Blog%20Drafts/old/Difficulties%20of%20Building%20Catalyst%20Apps%20on%20CI.assets/CleanShot%202023-05-16%20at%2015.00.12.png)

[TN3125: Inside Code Signing: Provisioning Profiles | Apple Developer Documentation](https://developer.apple.com/documentation/technotes/tn3125-inside-code-signing-provisioning-profiles)
