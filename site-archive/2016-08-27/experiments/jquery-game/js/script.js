$(document).ready(function(){
	$("#main").click(changeColors);
});

var colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

var changeColors = function(){
	var randomNum1 = Math.floor(Math.random() * colors.length);
	var randomNum2 = Math.floor(Math.random() * colors.length);

	var randomColor1 = colors[randomNum1];
	var randomColor2 = colors[randomNum2];

	$("h2").text(randomColor1);
	$("h2").css("color", randomColor2);
};