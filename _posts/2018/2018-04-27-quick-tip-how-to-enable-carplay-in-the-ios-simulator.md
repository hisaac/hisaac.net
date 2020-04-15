---
layout: post
title: "Quick Tip: How to Enable CarPlay in the iOS Simulator"
date: 2018-04-27
tags: software, ios, how-to, tip
link: https://stackoverflow.com/questions/32723237/switch-between-carplay-and-regular-window-in-ios-simulator
---

This little tip was surprisingly hard to find — only mentioned a couple times online — so I figured I'd do my part to spread the word.

To enable CarPlay in Xcode's iOS simulator, execute the following terminal command:

```shell
defaults write com.apple.iphonesimulator CarPlay -bool YES
```

Restart the simulator if it was currently running, and then in the menu bar, go to `Hardware > External Displays > CarPlay`.

![How to turn on CarPlay once you've enabled it in the simulator](carplay-simulator-demo.gif)
*How to turn on CarPlay once you've enabled it in the simulator*

Easy peasy.
