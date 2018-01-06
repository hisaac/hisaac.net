---
layout: post
title: "Solo Project Day Two: Getting Something on the Page"
tags: twitter, projects, crow, webdev
date: 2016-12-06T17:15:35-06:00
---

My scope was approved at the end of yesterday, so today I got to begin actual coding. It feels really good to start wrapping my brain around the concept of this app, and to start visualizing the whole project.

I began the day by thinking through my database structure. I've decided to use MongoDB for the project, and have two schemas I'll be using. The main schema:

```javascript
var userSchema = new Schema({
    email: String,
    name: String,
    username: String,
    date_joined: { type: Date, default: Date.now },
    tweets: { [tweet] }
});
```

And a sub-document schema for the tweets themselves:

```javascript
var tweetSchema = new Schema({
    twitter_id: { type: String, default: "" },
    url: { type: String, default: "" },
    posted: { type: Boolean, default: false },
    date_posted: Date,
    date_created: { type: Date, default: Date.now },
    hashtags: { type: String, default: "" },
    mentions: { type: String, default: "" },
    hearts: { type: Number, default: 0 },
    retweets: { type: Number, default: 0 },
    tweet: { type: String, default: "" }
});
```

(Normally I would use single-quotes in my JavaScript, but I had some issues with single-quotes within the tweet text escaping the string definition. I decided to use double-quotes, as they are less likely to be used in a tweet.)

These schemas are based off of assumptions about what the Twitter API will likely return to me, but I haven't yet begun building that component of the application, so it will likely change. Until then, I've populated my database with some test data based off of these schemas, and will continue testing using that.

Next, I began building my Angular routes in my client-side JavaScript to be able to display different content based on what "page" the user is on. I also build static Login and Logout pages to be used in testing.

I also dug into some simple CSS styling using Skeleton, and copying some of Bootstrap's button styles into them.

Lastly, we had a brief lecture on JavaScript debuggers. I haven't looked into it much, but I definitely plan to use one soon.

### Today's Research

- [Angular $routeProvider][1] - specifically the `resolve` parameter. I need to be able to route the user to different pages based on if the user is logged into Twitter or not.
- [Firebase Web API reference documentation][2]
	- Specifically the [TwitterAuthProvider documentation][3]
- [Skeleton][4] - The main CSS framework I'm using during the development phase.
- [Bootstrap's buttons][5]
- [node-inspector][6] - The debugger that was shown during lecture today.

### Screenshots

<figure class="image half-width">
    [![Login Page](./login-page.png)](./login-page.png)
    <figcaption>Login Page</figcaption>
</figure>

<figure class="image half-width">
    [![Settings Page](./settings-page.png)](./settings-page.png)
    <figcaption>Settings Page</figcaption>
</figure>

<figure class="image half-width">
    [![Tweet Page](./tweet-page.png)](./tweet-page.png)
    <figcaption>Tweet Page</figcaption>
</figure>

[1]:	https://docs.angularjs.org/api/ngRoute/provider/$routeProvider
[2]:	https://firebase.google.com/docs/reference/js/
[3]:	https://firebase.google.com/docs/reference/js/firebase.auth.TwitterAuthProvider
[4]:	http://getskeleton.com
[5]:	http://getbootstrap.com/css/#buttons
[6]:	https://github.com/node-inspector/node-inspector
