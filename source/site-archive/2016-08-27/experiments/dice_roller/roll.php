<!DOCTYPE html>
<html>
    <head>
		<title>dice roll</title>
        <meta name="viewport" content="width=device-width, initial-scale=0.6">
        <link type='text/css' rel='stylesheet' href='../v3/assets/css/normalize.css'/>
        <link type='text/css' rel='stylesheet' href='../v3/assets/css/main.css'/>
	</head>
	<body>
	
	<p>While learning PHP (with the help of the wonderful <a href="http://codecademy.com/">Codecademy</a>), I made this little dice roll app.</p>
	<p>It just rolls a die (generates a random number between 1 and six) until it rolls a six, and displays the values.</p>
	<p style="font-size: small;">hint: reload the page to rerun the app.</p>
	<hr>
    <?php
        $roll = 0;
        do {
            $roll = rand(1,6);
            echo "<p>You rolled a " . $roll . "</p>";
        } while ($roll != 6);
        
    ?>
    </body>
</html>