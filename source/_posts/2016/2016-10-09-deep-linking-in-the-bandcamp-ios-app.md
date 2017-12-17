---
title: Deep Linking in the Bandcamp iOS
date: 2016-10-09T15:31:40-05:00
layout: post
tags: technology, ios, music
---

*tl;dr: Bandcamp's iOS app does support deeplinking, but in a limited capacity.*

---

I love [Bandcamp](http://bandcamp.com). They are truly the premiere independent music platform. They treat their users and artists well, and still manage to stay afloat.

I also like their iOS app. It works well for previewing new music, or listening to music I've already purchased on the platform.

I do have one complaint about their app though: There's no way to open the app when viewing an album or artist's page in the web browser. Many apps have this functionality. To name a few:

- [Twitter](http://twitter.com/hisaac)
- [Wikipedia](https://en.wikipedia.org/wiki/Bandcamp)
- [Medium](https://medium.com/@fireland/my-dead-girlfriends-bot-9dc6a2f55ce3#.xysv1y5b9)
- [YouTube](https://youtu.be/blpe_sGnnP4)

(All of those links should open in their respective iOS apps if you have them installed)

So why not Bandcamp? I don’t know *why* they’ve avoided deep linking, but for a while now, I’ve just accepted it as a fact. Until recently.

The other day, I bought an album on Bandcamp — Vaporlane’s [*Hieretic Teen*](https://usonian.bandcamp.com/album/hieratic-teen) to be exact:

<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=531538254/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/artwork=small/transparent=true/" seamless><a href="http://usonian.bandcamp.com/album/hieratic-teen">Hieratic Teen by Vapor Lanes</a></iframe>

After the purchase, I received an email receipt as usual. For whatever reason, I opened that email on my iPhone, and noticed a link saying “listen now in the Bandcamp app”. I don’t know if this is new or not, but this is the first time I noticed it.

Intrigued, I tapped the link. It first opened a web page in Safari, and then opened the Bandcamp app directly to the album, and started playing it! I was surprised and immediately started digging further. I had thought the Bandcamp app didn’t support deep linking, but it was now obvious that it does indeed.

So first, let’s look at the link in that email (personal/purchase information replaced with `@@@`):

```
http://bandcamp.com/redirect_to_app?fallback_url=http%3A%2F%2Fbandcamp.com%2Fdownload%3Ffrom%3Dreceipt%26payment_id%3D@@@%26sig%3D@@@&url=x-bandcamp%3A%2F%2Fshow_tralbum%3Ftralbum_type%3Da%26tralbum_id%3D531538254%26play&sig=@@@
```

The URL is constructed in a way that it first tries to open the Bandcamp iOS app, but then falls back to the web page if it’s not successful.

So what are all those `%` symbols? This URL uses [Percent Encoding](https://en.wikipedia.org/wiki/Percent-encoding) to encode information not normally allowed in URLs/URIs. Here’s a list of the codes used, and their translations:

| Percent code | Translation |
| ------------ | ----------- |
| `%3A`        | `:`         |
| `%2F`        | `/`         |
| `%3F`        | `?`         |
| `%3D`        | `=`         |
| `%26`        | `&`         |

So, if we use this to fix the parts after the `fallback_url=` in the original URL[^1], we get:

```
http://bandcamp.com/download?from=receipt&payment_id=@@@&sig=@@@&url=x-bandcamp://show_tralbum?tralbum_type=a&tralbum_id=531538254&play&sig=@@@
```

The last bit of that URL is the key. Here it is isolated:

```
bandcamp://show_tralbum?tralbum_type=a&tralbum_id=531538254&play
```

iOS’s deep linking syntax uses URIs to open applications rather than web pages. This description from the [deep linking Wikipedia page](https://en.wikipedia.org/wiki/Mobile_deep_linking) is good:

> Unlike the Web, where the underlying technology of HTTP and URLs allow for deep linking by default, enabling deep linking on mobile apps requires these apps be configured to properly handle a uniform resource identifier (URI). Just like a URL is an address for a website, a URI is the address for an app on a mobile device.

`twitter://` and `YouTube://` are the iOS URIs used to launch their respective apps, so in this instance, it’s the `bandcamp://` part of the URL that tipped me off.

Looking at the URI, there is an `album_id=` field. I was hoping an album's ID was used in the actual URL for the album, but it's not the case. If we dig into the HTML source code though, we find the goods. Here are the last few lines of the source code for Hieretic Teen's Bandcamp page:

```html
</body>
</html>
<!-- bender01-6 Sun Oct 09 20:06:39 UTC 2016 -->
<!-- album id 531538254 -->
```

There it is! Buried at the bottom of the page is this album's ID. Each album's page has an album ID commented out at the very bottom of the page.

Next, I built a couple workflows using the excellent [Workflow](https://geo.itunes.apple.com/us/app/workflow-powerful-automation/id915249334?mt=8&uo=4&at=1001laDe) iOS app to test this out. Here they are:

- [Open current Bandcamp web page in Bandcamp iOS app](https://workflow.is/workflows/bd3284f7333e406b87a4500230016ba5)
- [Open current Bandcamp web page in Bandcamp iOS app, and start playing the album (using the `&play` modifier from the original URI)](https://workflow.is/workflows/162f55c816e84cd59624c68e3e95409a)

Here's where we hit a problem that I can't fix on my own. These workflows work beautifully and without error (in my testing), *but only* on albums that the user logged into the Bandcamp app already owns. If used on albums not already in the user's library, the Bandcamp app throws up an error saying:

> The album could not be loaded. You may need to add your payment email address or sign in as a different user.

So this is where my journey ends. It seems that Bandcamp and its developers want to keep the deep linking to themselves, and use it only for opening the app from purchase receipts. I'm definitely curious to know why, and I'd like to request that the app's behavior be changed. Preferably, I'd like it to act like the Twitter and YouTube apps: When any link to a Bandcamp web page is opened, open the Bandcamp app instead. The app's audio player is *much* preferable to the web player.

[^1]: I used [ascii.cl’s URL Decoding page](http://ascii.cl/url-decoding.htm) to convert this. It’s a handy resource.
