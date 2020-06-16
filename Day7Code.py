#-----------------------------------------------
#100DaysOfCode 007/100 - Starter Program - partial solution
#   2020-06-16
#
#  Prompt user to input say something and hit enter.
#      loop until user enters \end
#  Output:
#     print the sentances with capitalization and punctuation.
#
#   ******* this is a partial solutoin - I ran out of time today
#

say_something = []

while True:
    say_input = input("Say something: ")
    if say_input == '\end':
        break
    else:
        say_something.append(say_input.capitalize())
        continue

print("----")
print("Output")
print("----")
for print_something_loop in say_something:
    print(print_something_loop)
