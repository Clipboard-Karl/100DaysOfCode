#100DaysOfCode 027/100 - Fixing Errors
#
#
#  20200712 - 100DaysOfCode 027/100 -
#
################################################################################
#
#  Syntax errors
print(1)
#int 9  #  int needs brackets
int(9)
print(2)
#print 3   # again brackets missing
print (3)
#a =[1,2,3)
#  File "Day027Code_fixing_errors.py", line 15
#    a =[1,2,3)
#             ^
# The error ^ shows the problem
a = [1,2,3]
#
#  Runtime Errors - Exceptions
a = 1
b = "2"
#print(int(2.5)  #  this causes a syntax erro on the next line missing )
#  note:  Python checks for syntax errors first - taht is why this was used
print(int(2.5))
#print(a + b)   # adding a string to an intiger
print(a + float(b))
print(str(a) + b)
#
#
#print(a/0)
#  error ---- ZeroDivisionError: division by zero
# if you don't understand the error - copy and paste in google
#    stack overflow has a lot of answers  i
#
#  If you don't find and error - then ask the question
#    Ask good questions
#      Bad question - "I got an error - what do I do?"
#
#  long questions area better
#  state expected results
#  for stackoverflow - follow the format and rules
#
#
# Error handling
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:  #with no error name all errors will be allowed
        return ("Error - divide by zero")

print (divide(1,0))
