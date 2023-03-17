alias: 2016/12/11/solo-project-day-six-saturday.html
published_date: 2016-12-11
tags: twitter, projects, crow, webdev
title: Solo Project Day Six: Saturday
___

I didn't do too much today, as it's a weekend, but I did get a little work done. Namely, I used Twitter's API to look up the logged in user's Twitter username using the `user_id` I receive back from Firebase on login. I also started building functionality for the draft of a tweet to be saved to the database for later editing.

### Today's Research

- [HTTP Status Codes](http://www.restapitutorial.com/httpstatuscodes.html)
- [GET account/verify\_credentials (Twitter API Docs)](https://dev.twitter.com/rest/reference/get/account/verify_credentials) - I was frustrated that I didn't get a user's email address back from Firebase or Twitter when doing API calls, but I found out why. Twitter does allow for it, but I must provide links to my privacy policy and terms of service. I don't actually have a privacy policy or terms of service yet, but if I plan to make this into a real app (which I do), I'll need to write those at some point.
