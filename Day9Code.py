#-----------------------------------------------
#100DaysOfCode 009/100 - More on Functions
#   2020-06-18
#
#

# positional Arguments
def area(a, b):
    return a * b

print(area(4, 5))

#---------  Positional Arguments
def george_1(in_1, in_2):
        return in_1 + in_2

print(george_1("Hello ", "Karl"))

#-----------  Key Word Arguments
def george_2(in_1, in_2):
        return in_1 + in_2

print(george_2(in_2="Day", in_1="Good "))

#---- pass as many arguments as you want - arbutary number
#----   *args could be any name but *args is the standard
def average(*args):
    return sum(args) / len(args)

print(average(10, 20, 30, 40))

#------- convert to uppercase and sort
def george_3(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(george_3("snow", "glacier", "iceberg"))

# arbutary number of key word arguments **kwargs (convention is **kwargs)
def simple_print_test(**kwargs):
    return kwargs

print(simple_print_test(A=10, B=20, C=30, D=40))
