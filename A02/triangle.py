import math

print "Please enter the lengths of the sides of a triangle: "
a = float(raw_input("a: "))
b = float(raw_input("b: "))
c = float(raw_input("c: "))

if( (a > (b+c)) or (b > (a+c)) or (c > (a+b)) ):
	print "not a triangle"
else:
	s = a+b+c
	area = math.sqrt( s*(s-a)*(s-b)*(s-c) )
	print "The area is: ", area

	if a == b == c:
		print "equilateral"
	elif a == b or b == c or a == c:
		print "isoceles"

	if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
		print "right"
	elif (a*a + b*b < c*c) or (a*a + c*c < b*b) or (c*c + b*b < a*a):
		print "obtuse"
	else:
		print "acute"