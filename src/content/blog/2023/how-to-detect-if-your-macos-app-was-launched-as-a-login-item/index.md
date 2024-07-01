---
title: "How to Detect if Your macOS App Was Launched as a Login Item"
date: 2023-06-05
tags: [swift, macos, xcode, software]
source: https://stackoverflow.com/a/19890943/4118208
---

Have you ever wondered how to detect if a macOS app you're building was launched as a login item, as opposed to being launched manually by the user? Well, here's how to do it in Swift:

```swift
private var launchedAsLogInItem: Bool {
	guard let event = NSAppleEventManager.shared().currentAppleEvent else { return false }
	return
		event.eventID == kAEOpenApplication &&
		event.paramDescriptor(forKeyword: keyAEPropData)?.enumCodeValue == keyAELaunchedAsLogInItem
}
```

There are probably a number of reasons you'd want to check for this. In my case, I wanted to prevent the main app window of my app [CenterMouse](https://hisaac.net/centermouse/) from opening when the app was launched as a login item, but still open it if a user launches it manually.

You can see this code in context in CenterMouse's AppDelegate here: [AppDelegate.swift](https://github.com/hisaac/CenterMouse/blob/main/CenterMouse/Sources/AppDelegate.swift).
