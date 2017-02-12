var keyboard = {
  clueTitle: 'Clue 1',
  clue: "I may have too many of these, but I just can't stop buying them. It is what I used to write all of this, so perhaps that will convince you of their value? <br> <br> The answer to this clue is the number of these that I'll need before I'm satisfied.",
  correctAnswer: '42',
  success: "Nice work! You know me well. Do you think 42 keyboards is too much?",
  failure: "Having trouble? Here's a hint: My newest one of these holds the answer you seek."
};

var growler = {
  clueTitle: 'Clue 2',
  clue: "I've tried the gluten free brews of Portland, and now Seattle too, but there just ain't nothing like that Burning Brothers Pyro. Could you go fill up my growler for me? The answer will then become clear.",
  correctAnswer: 'cheers',
  success: "Thanks for getting the beer for me! All joking aside, Pyro is still my fav! (Although Olallie is a very close second)",
  failure: "Having trouble? Here's a hint: Grab that growler!"
};

var printer = {
  clueTitle: 'Clue 3',
  clue: "Now I hope you'll be printing off a sign for my return. As you know, an airport pickup just wouldn't be the same without a sign. Only problem is, there's a paper jam in the printer. You'd better check that out before you try to print something",
  correctAnswer: 'gimme dat paper',
  success: "Thanks for printing off that sign! That way, I'll know who's there to pick me up.",
  failure: "Having trouble? Here's a hint: I think the jam is in the paper tray."
};

var final = {
  clueTitle: 'Final Clue',
  clue: "You've made it to the <strong>FINAL CLUE</strong>! I'm very impressed.<br><br>I suppose it's time now for you to get your actual gift. I actually wanted to hide it in the apartment, but it's just too big! It barely fit in my truck bed! Hopefully you can find it before I get home…",
  correctAnswer: '',
  success: "I love you! I'm looking forward to seeing you and loving you in just a little bit. :)",
  failure: "Having trouble? Here's a hint: Check out how clean my truck is! The car wasj was able to wash everything except for the truck bed!"
};

var currentState;

$(document).ready(function() {
  init();

  // $('form').submit(function() {
  //   event.preventDefault();
  //   userInput = $('#userInput').val();
  //   checkAnswer(userInput);
  // });
});

function init() {
  if (!currentState) {
    currentState = keyboard;
  }

  $('#clueTitle').html(currentState.clueTitle);
  $('#clue').html(currentState.clue);

}

function checkAnswer(input) {
  let isCorrect = false;
  if (input == correctAnswer) {

  }
  init();
}

