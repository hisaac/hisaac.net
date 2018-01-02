---
layout: post
title: "Solo Project Day Four: Too Big for my Britches"
tags: twitter, projects, crow, webdev
date: 2016-12-08T18:52:41-06:00
---

Today was a tough day actually. I started to get hung up on some bigger issues than I need to worry about at this stage. Contemplating user security is new to me, and something that I began to worry a lot about. When a user logs into my app using Firebase, my app gets sent that user's key and their secret. These are essentially their username and password, but they are specific to my app, and requre my apps key and secret as well to be used in any way. This means that even if someone were to steal a user's key and secret, they wouldn't be able to do anything with them unless they had also stolen my app's key and secret.

So this provides a good level of security, but my question was whether or not it's good practice to store the user's key and secret on my server. It *seems* like it would be secure *enough*, but secure enough doesn't really seem like good practice these days. For now, I'm going to not store the key and secret anywhere, and only hold while the user is currently using the app. I plan to do more research on it later.

### Things Done

- Implemented [dotenv][1] for environment specific variables.
- Tried out [unirest][2] for API requests.
- After fussing with Twitter's API for too long than I probably should have, I eventually ditched the manual API call route using unirest, and decided to use a library. I landed on [twit][3] as the best option.

### Today's Research

- [Understanding OAuth Request Signing - The Polyglot Developer][4]
- [Application Only AUthentication - Twitter API Docs][5] - Application only authentication is used to make reqeusts to Twitter using only an app's API credentials. Twitter restricts the types of information that can be accessed this way, but the rate limits are also raised. This allows an app to do more frequent calls for generic Twitter information without worrying about getting temporarily locked out from accessing Twitter's data.
- [Twitter for Node.js][6] - One of the server-side JavaScript Twitter libraries I looked at using for my app. I eventually decided not to use it, for no reason other than twit had more stars on GitHub.
- [twit][7] - The server-side JavaScript library I decided to use for making API calls to Twitter from my server. So far, I'm pleased with it. It's ***way*** easier than building the API calls manually.
- [POST statuses/update - Twitter API Docs][8] - Twitter's documentation on how to make an API call to post a new status to Twitter.
- [Application Tokens from dev.twitter.com - Twitter API Docs][9] - Twitter's documentation on what application access tokens are, how to obtain them, and how to use them.
- [Security Best Practices - Twitter API Docs][10] - Twitter's documentation on security best practices when using their API.
- [Authenticate Using Twitter in JavaScript - Firebase Docs][11] - Firebase's documentation on how to use their service to authenticate a user using their Twitter credentials, specific to JavaScript.


[1]:	https://github.com/motdotla/dotenv
[2]:	http://unirest.io
[3]:	https://github.com/ttezel/twit
[4]:	https://www.thepolyglotdeveloper.com/2014/11/understanding-request-signing-oauth-1-0a-providers/
[5]:	https://dev.twitter.com/oauth/application-only
[6]:	https://github.com/desmondmorris/node-twitter
[7]:	https://github.com/ttezel/twit
[8]:	https://dev.twitter.com/rest/reference/post/statuses/update
[9]:	https://dev.twitter.com/oauth/overview/application-owner-access-tokens
[10]:	https://dev.twitter.com/basics/security-best-practices
[11]:	https://firebase.google.com/docs/auth/web/twitter-login