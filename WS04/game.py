import random
random.seed()

playing = True
while( playing ):
	first_number  = random.randint(1,10)
	second_number = random.randint(1,10)
	third_number  = random.randint(1,10)
	print first_number, second_number, third_number
	if( first_number  == second_number and
		second_number == third_number):
		print "jackpot! matched 3!"
	elif( first_number  == second_number or
		  first_number  == third_number  or
		  second_number == third_number ):
		print "you win! matched 2"
	else:
		print "you lose!"
	answer = raw_input('Play?\n')
	while( not (answer == "Y" or answer == "N") ):
		answer = raw_input('Play?\n')
	if answer == "N":
		playing = False
	