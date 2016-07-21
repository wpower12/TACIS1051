# Loop to ask for grades
print("Hello!  Welcome to Grade Calculator.")

num_grades = int(raw_input('Number of Grades?: '))
grades_entered = 0

while grades_entered < num_grades:
	val = int(raw_input)