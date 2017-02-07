let userInput;

$(document).ready(function() {
  $('button').click(function() {
    userInput = $('#userInput').val();
    inputChecker(userInput);
  });
});

function inputChecker(input) {

	$('#correct, #incorrect').addClass('hidden');

  if (input == 'test') {
  	$('#correct').removeClass();
  } else {
  	$('#incorrect').removeClass();
  }
}

