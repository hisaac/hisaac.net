---
layout: post
title: "Solo Project Day Seven: To The Database and Back Again"
tags: twitter, projects, crow, webdev
date: 2016-12-12T21:10:56-06:00
---

This is technically the eighth day since I began my solo project, but I didn't do any work on the project on Sunday (although I did do [some other web work]({% post_url /2016/2016-12-11-moved-to-digital-ocean-lets-encrypt %})).

Today was a very productive day for me. I got more done than I expected to, and I made it to MVP (Minimum Viable Product)! I didn't think I'd get to MVP this fast, but I'm glad I did. At Prime, we all get industry mentors to work with, and tomorrow we meet with them to show them our solo projects. I was really hoping I'd have a usable product to show them.

### Tasks Accomplished

- Sorted out asynchronous tasks on the login page so that writing data returned from Firebase to the database happened *after* the data was actually received.
- Figured out how to use `$location` to redirect to a new page after login: `$location.path('/drafts')`
- This one was a doozie. I figured out how to create a new blank Mongoose sub-document upon the press of the "new tweet" button. Here's the code (authFactory is where I'm storing the currently logged in user's data):

```javascript
// client side
$http.post('/db/draft/newBlank', self.authFactory)
  .then(function(res){
    // move info from newly created blank draft into draft factory
    self.draftFactory._id = res.data._id;
    self.draftFactory.text = res.data.text;
    self.draftFactory.dateCreated = res.data.dateCreated;
  });

// server side
router.post('/draft/newBlank', function(req, res){
  User.findOne({ uid: req.body.uid }, function(error, user){
    user.drafts.push(new Draft);
    if(error){
      res.sendStatus(500);
    } else {
      user.save();
      res.status(201).send(user.drafts[user.drafts.length-1]);
    }
  });
});
```

- I then figured out how to move the edited text of a draft into the database. This was also difficult, as I had to query the database for the specific draft that was being edited, and then update that one. Here's the code:

```javascript
// client side
self.saveDraft = function(){
  $http.post('/db/draft/saveDraft/' + self.draftFactory.text, self.draftFactory);
};

// server side
router.post('/draft/saveDraft/:tweetText', function(req, res){
  var query = { 'drafts._id': req.body._id };
  var update = { 'drafts.$.text': req.params.tweetText };
  var options = { upsert: true, new: true, setDefaultsOnInsert: true };

  User.findOneAndUpdate(query, update, options, function(error, result){
    if(error){
      res.sendStatus(500);
    } else {
      res.sendStatus(201);
    }
  });
});

```

- Lastly, I queried the database to display the current user's drafts on the Drafts page in a list.

Tomorrow's task will be mainly styling. I want the app to look nice for my mentors.

### Today's Research

- [getting the id of the newly pushed embedded object - Stack Overflow][1] - I needed to get this data when I created a new blank draft. Turns out, it's just basic JavaScript (`array.length - 1`). I shoulda known.
- [Factory not keeping data when used in controller - Stack Overflow][2] - This was frustrating. I initially was trying to assign objects directly to my factories, but I found that I had to assign specific values to them instead (see the first client side code example above). I still don't know *why* I need to do it this way, but I know that it does work.

[1]:	http://stackoverflow.com/questions/13195283/mongodb-getting-the-id-of-the-newly-pushed-embedded-object
[2]:	http://stackoverflow.com/questions/21006222/factory-not-keeping-data-when-used-in-controller
