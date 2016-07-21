def draw_line(len):
	res = ""
	for i in range(0, len):
		res += "*"
	print(res)

def draw_rect(len, width):
	for i in range(0, width):
		draw_line(len)

def draw_square(len):
	draw_rect(len, len)

drawing = True
while(drawing):
	 type = raw_input("Type? [S]quare [R]ectangle: ")

	 length = int(raw_input("Enter Length: "))
	 if type == "R":
	 	width = int(raw_input("Enter Width: "))
	 	draw_rect( width, length )
	 elif type == "S":
	 	draw_square( length )

	 drawing = (raw_input("Keep playing? (y/Y): ").upper() == "Y")

