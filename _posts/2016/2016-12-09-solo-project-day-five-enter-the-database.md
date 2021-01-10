---
layout: post
title: "Solo Project Day Five: Enter the Database"
tags: [twitter, projects, crow, webdev]
date: 2016-12-09T23:13:30-06:00
---

Today's goal was simply to move the data I was receiving from Twitter via Firebase, into my database. While this seemed simple in concept, as someone new to programming, it was difficult in practice.

I'm using Angular for my project, and I have a controller that calls to Firebase for the user's authentication. The data is returned to the controller, and then put in a factory for temporary storage, and for use between controllers.

The same controller then makes an AJAX POST request to the server, which is then routed to the database using Mongoose. I also had to fuss a lot with my schema in Mongoose, which took up a good deal of my time.

Thankfully, a classmate of mine was able to offer some help. I'm also using Mongoose sub-documents in my project, and I could not for the life of me figure out how to import the sub-document modules into my main schema module.

Here is the correct way to do it:

```javascript
var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var User = require('../models/user.model');
var Draft = require('../models/draft.model').schema;
var Post = require('../models/post.model').schema;
```

My issue was the `.schema` at the end of the sub-document require statements. I wasn't using the `.schema` initially, so it wasn't working at all.

### Today's Research

- [Routing - Express Documentation](https://expressjs.com/en/guide/routing.html)
- [Difference Between `app.use()` and `router.use()` in Express - Stack Overflow](http://stackoverflow.com/questions/27227650/difference-between-app-use-and-router-use-in-express)
- [Sub-Documents - Mongoose Documentation](http://mongoosejs.com/docs/subdocs.html)
- [MongoDB: Updating Subdocument - Stack Overflow](http://stackoverflow.com/questions/5646798/mongodb-updating-subdocument) - Another handy piece of information that Alex showed me today, the use of the `$` positional operator when referring to Mongoose sub-documents.
- [GET users/lookup - Twitter Developer Documentation](https://dev.twitter.com/rest/reference/get/users/lookup)
