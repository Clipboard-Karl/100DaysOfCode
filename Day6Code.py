#-----------------------------------------------
#100DaysOfCode 006/100 - The Basics:  Loops
#   2020-06-15
#
monday_temp = [9.1, 8.3, 7.6]

print(round(monday_temp[0]))
print(round(monday_temp[1]))
print(round(monday_temp[2]))

# Now in a Loops
for name_of_the_variable_goes_here in monday_temp:
    print(round(name_of_the_variable_goes_here))

for letter in 'hello':
    print(letter)

colors = [11, 34, 98, 43, 45, 54, 54]

for color_loop in colors:
    if color_loop > 50:
        print(color_loop)

print("----------------")

#  print only the intigers greater than 50
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color_loop in colors:
    if isinstance(color_loop, int) and color_loop > 50:
        print(color_loop)

print("----------------")

# Loop a dictionary
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.items():
    print(grades)

for grades in student_grades.keys():
    print(grades)

for grades in student_grades.values():
    print(grades)

for key, value in student_grades.items():
    print("{} hase a grade of {}".format(key, value))

print("----------------")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{}: {}".format(key, value))

# for pre python 3.6
for key, value in phone_numbers.items():
    print("%s: %s" % (key,value))

for value in phone_numbers.values():
    print(value.replace("+", "00"))

print("----- while loops start here -------")

username = ''   #<-- empty string

while username != "karl":  #<-- while user name is different from "karl"
    print("the correct answer is karl")
    username = input("Enter username:")

while True:
    username = input("Enter username:")
    if username == 'smith':
        break
    else:
        print("the correct answer is smith")
        continue
