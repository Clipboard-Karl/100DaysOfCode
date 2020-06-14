#-----------------------------------------------
#100DaysOfCode day 005  -
#   2020-06-14
#  User input, String Formatting
#
def Hot_Or_Cold(generic_value_to_be_checked):
    if generic_value_to_be_checked > 80:
        return "HOT"
    else:
        return "COLD"

# Commented out so it doesn't run when wokring on other assignments :)
#user_input = float(input("Enter Temperature (F): "))
#print(type(user_input), user_input)
#print("The temperature is:  ",Hot_Or_Cold(user_input))


user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
#the next line is for python 2 & 3
message = "Hello %s %s!" % (user_first_name, user_last_name)
print(message)
#the next line works in python 3.6 and above  ** note the f
message = f"Hello {user_first_name} {user_last_name} have a great day!"
print(message)

# Assignment 28
def say_hi(generic_name):
    return "Hi %s" %(generic_name)

print(say_hi(user_first_name))

# Assignment 29
def say_hi(generic_name):

    return "Hi %s" %(generic_name.capitalize())

print(say_hi(user_first_name))
