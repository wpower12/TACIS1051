# Retirement - Chained Conditionals
# 
# Ask about age and work history, return gift type.
#
# Bill Power
# tug00038@temple.edu
# 
# 6/29/26

age   = input('enter age\n')
years = input('years worked\n')

if( age > 65 ):
	print "gold watch"
elif( years > 25 ):
	print "silver watch"
else:
	print "pen"