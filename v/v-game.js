let userInput, success, failure, clue, clueTitle;
let currentState = 1;

$(document).ready(function() {

  router(currentState);

  $('#clueTitle').html(clueTitle);
  $('#clue').html(clue);

  $('form').submit(function() {
    event.preventDefault();
    userInput = $('#userInput').val();
    inputChecker(currentState, userInput);
  });
});

function router(state) {
  switch (state) {
    case 1:
      keyboardSticker(currentState, userInput);
      break;
    case 2:
      beerSticker(currentState, userInput);
      break;
    case 3:
      printerSticker(currentState, userInput);
      break;
    case 1:
      finalClue(currentState, userInput);
      break;
  }
}

function inputChecker(state, input) {

  $('#correct, #incorrect').addClass('hidden');

  if (input == 'test') {
    $('#correct').removeClass();
  } else {
    $('#incorrect').removeClass();
  }
}

function keyboardSticker(state, input) {
  clueTitle = 'Clue 1';
  clue = 'I\'ve got way too many of these, but I just can\'t stop buying them. But it\'s what I used to write all of this, so I think they\'re worth investing in. <br> <br> The answer to this clue is the number of these that I\'ll need before I\'m satisfied.';
  let answer = '42';
}

function beerSticker(state, input) {
  // correct answer is '42'
  clueTitle = 'Clue 2';
  clue = 'I\'ve filled up on some Groundbreaker brews, but there ain\'t nothing like that Burning Brothers. Could you make sure to fill that growler for me before you get back?';
  let answer = 'cheers';
}

function printerSticker(state, input) {
  // correct answer is 'cheers'
  clueTitle = 'Clue 3';
  clue = 'Thanks for getting the beer! Now I hope you\'ll be printing off a sign for my return. As you know, an airport pickup just wouldn\'t be the same without a sign, baloons, candy, and stuffed animals. Only problem is, there\'s something wrong with the paper in the printer! You might need to pull out what\'s in there and replace it.';
  let answer = 'gimme dat paper';
}

function finalClue(state, input) {
  // correct answer is 'gimme dat paper'
  clueTitle = 'Final Clue!';
  clue = 'Thanks for printing off that sign. Now I\'ll know it\'s you when I get to the airport.';
}

