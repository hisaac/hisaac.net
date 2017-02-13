var clueIndex = 0;
var currentClue, userInput;

var clueArray = [
  keyboard = {
    clueTitle: 'Clue 1',
    clue: "I may have too many of these, but I just can't stop buying them! It is what I used to write all of this though, so perhaps that will convince you of their value?<br><br>The answer to this clue is the number of these that I'll need before I am satisfied.",
    correctAnswer: '42',
    success: "Nice work! You know me well.\n\n42 keyboards isn't too outrageous, is it?",
    failure: "Having trouble? Here's a hint:\n\nMy newest one of these holds the answer you seek."
  },
  growler = {
    clueTitle: 'Clue 2',
    clue: "I've tried the gluten free brews of Portland — and now Seattle too — but there just ain't nothing like that Burning Brothers Pyro.<br><br>Could you grab my growler from on top of the cupboard so I can refill it when I get home?",
    correctAnswer: 'cheers',
    success: "Thanks for getting that down for me!\n\nAll joking aside, Pyro is still my fav! (Although Olallie is a very close second)",
    failure: "Having trouble? Here's a hint:\n\nGrab the growler, not the grumbler!"
  },
  printer = {
    clueTitle: 'Clue 3',
    clue: "I really hope you'll be printing off a sign for my return. As you know, an airport pickup just wouldn't be the same without a sign.<br><br>Only problem is, there's a paper jam in the printer! You'd better check that out before you try to print anything.",
    correctAnswer: 'gimme dat paper',
    success: "Thanks for printing off that sign!\n\nNow I'll know for sure who is there to pick me up.",
    failure: "Having trouble? Here's a hint:\n\nI think the jam is in the paper tray."
  },
  final = {
    clueTitle: 'Final Clue',
    clue: "You've made it to the <strong>FINAL CLUE</strong>! I'm very impressed. It is time now for you to get your actual gift!<br><br>I wanted to hide it in the apartment, but it's just too big! It barely fit in my truck bed! Hopefully you can find it before I get home.",
    correctAnswer: '',
    success: "Text me when you've found it! I'm probably still on the plane, but you can leave me a message for when I land.\n\nI'd sure love a picture of you using your new gift. 😉",
    failure: "Having trouble? Here's a hint:\n\nIf it barely fit in my truck bed, and was too big to bring upstairs, where could it be?"
  }
];

$(document).ready(function() {
  init();

  $('form').submit(function() {
    event.preventDefault();
    userInput = $('#userInput').val().toLowerCase();
    $('#userInput').val('');
    checkAnswer(userInput);
  });

  $('#help').click(function() {
    alert(currentClue.failure);
  });

  $('#text').click(function() {
    alert(currentClue.success);
  });
});

function init() {
  currentClue = clueArray[clueIndex];
  if (clueIndex === 3) {
    $('form').addClass('hidden');
    $('#finalForm').removeClass('hidden');
  }
  $('#clueTitle').html(currentClue.clueTitle);
  $('#clue').html(currentClue.clue);
}

function checkAnswer(input) {
  if (input == currentClue.correctAnswer) {
    alert(currentClue.success);
    clueIndex++;
    init();
  } else {
    alert(currentClue.failure);
  }
}

