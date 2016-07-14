import random
random.seed()
playing = True

while(playing):
	a = random.randint(0,9)
	b = random.randint(0,9)
	c = random.randint(0,9)
	print a, b, c
	guesses = 0
	guessing = True
	while(guessing):
		guesses += 1
		ga = int(raw_input("Guess a: "))
		gb = int(raw_input("Guess b: "))
		gc = int(raw_input("Guess c: "))

		#Game over
		if( ga == a and gb == b and gc == c ):
			print "You won!  It took you this many guesses:"
			print guesses
			guessing = False
			ans = raw_input("Would you like to keep playing? ")
			if( not (ans == "Y" or ans == "y") ):
				playing = False
		else:
		# Fermi
			if( ga == a ):
				print "fermi"
			if( gb == b ):
				print "fermi"
			if( gc == c ):
				print "fermi"
		# Pico
			if( ga == b or ga == c ):
				print "pico"
			if( gb == a or gb == c ):
				print "pico"
			if( gc == a or gc == b ):
				print "pico"		
		# Bagel
			if( ga != a and ga != b and ga != c and
				gb != a and gb != b and gb != c and
				gc != a and gc != b and gc != c ):
				print "bagel"
