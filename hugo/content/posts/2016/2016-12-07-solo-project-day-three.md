---
title: "Solo Project Day Three: The Day I Tweeted"
tags: twitter, projects, crow, webdev
date: 2016-12-07T16:59:01-06:00
---

I tweeted using my app (sort of) for the first time today! I say sort of, because I didn't actually do it from my app, but I did use my my app's credentials and my [test user](http://twitter.com/hisaac0)'s credentials. I used a wonderful API testing app called [Paw](https://paw.cloud) to do my testing today. It's a really nice tool, and I plan to continue using it for this project.

I also implemented [FastClick](https://github.com/ftlabs/fastclick), a JavaScript library to remove the 300ms lag when tapping items on the screen on touch-screen devices. It was very easy to implement, just a short piece of code in my client-side JavaScript after importing the library itself in the `index.html`.

```javascript
// instantiates FastClick
if ('addEventListener' in document) {
  document.addEventListener('DOMContentLoaded', function() {
    FastClick.attach(document.body);
  }, false);
}
```

Lastly, I began building functionality for the client-side code to send a created tweet to the server for the server to then post to Twitter.

I've been hearing good things about JetBrain's [WebStorm](https://www.jetbrains.com/webstorm/) JavaScript IDE, so I'm going to try using that for development for a while. One of my instructors really likes it, so hopefully I'll be able to get support from him if I decide to do it.

### Today's Research

- Twitter's API Documentation:
	- [POST statuses/update](https://dev.twitter.com/rest/reference/post/statuses/update) - General information on how to POST statuses to Twitter. It turns out it's much easier than I'd expected. If the user is already logged in, you simply URL encode the text, and then send it to Twitter in the request URL.
	- [Counting Characters](https://dev.twitter.com/basics/counting-characters) - This article describes in depth how a character is counted by Twitter. It turns out, it's not quite as simple as you'd imagine. Certain types of characters take up different amounts of bytes, and are therefor couted differently. The article says that 'character normalization' is necessary, and it turns out JavaScript has a character normalization function built in.
	- [t.co links](https://dev.twitter.com/basics/tco) - Twitter's built in URL shortener — called `t.co` after the URLs it generates — works relatively automatically, with some caveats. When sending a tweet to Twitter, if it detects a URL in the text, it will automatically convert it to a `t.co` link, *unless* it is less than the current maximum `t.co` URL length. As time goes on, the length of shortened URLs grows as more and more unique links are used up. This means it's important to check with Twitter what the current maximum `t.co` link length is. This is done by periodically performing a GET request to Twitter's help/configureation URL.
	- [GET help/configuration](https://dev.twitter.com/rest/reference/get/help/configuration) - Information on how to get configuration data from Twitter's API.
- [JavaScript Character Normalization (MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize) - The Mozilla Developer Network's documentation on JavaScripts `.normalize()` method.
- [Angular $routeProvider](https://docs.angularjs.org/api/ngRoute/provider/$routeProvider) - Once again looking into how to route a user to different pages based on their logged in status using `$routeProvider`'s `resolve` functionality.
- [Unirest](http://unirest.io/nodejs.html) - NodeJS REST API library for doing API calls from the server.
