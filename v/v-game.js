let userInput, success, failure;
let clue = 'I\'ve got way too many of these, but I just can\'t stop buying them. But it\'s what I used to write all of this, so I think they\'re worth investing in. <br> <br> The answer to this clue is the number of these that I\'ll need before I\'m satisfied.';
let currentState = 'beginning';

$(document).ready(function() {

  $('#clue').html(clue)

  $('form').submit(function() {
    event.preventDefault();
    userInput = $('#userInput').val();
    inputChecker(currentState, userInput);
  });
});

function inputChecker(state, input) {

	$('#correct, #incorrect').addClass('hidden');

  if (input == 'test') {
  	$('#correct').removeClass();
  } else {
  	$('#incorrect').removeClass();
  }
}

function keyboardSticker(state, input) {
  // correct answer is '42'
  clue = 'I\'ve filled up on some Groundbreaker brews, but there ain\'t nothing like that Burning Brothers. Could you make sure to fill that growler for me before you get back?';
}

function beerSticker(state, input) {
  // correct answer is 'cheers'
  clue = 'Thanks for getting the beer! Now I hope you\'ll be printing off a sign for my return. As you know, an airport pickup just wouldn\'t be the same without a sign, baloons, candy, and stuffed animals. Only problem is, there\'s something wrong with the paper in the printer! You might need to pull out what\'s in there and replace it.';
}

function printerSticker(state, input) {
  // correct answer is 'gimme dat paper'
  clue = 'Thanks for printing off that sign. Now I\'ll know it\'s you when I get to the airport.';
}