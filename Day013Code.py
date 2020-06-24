#-----------------------------------------------
#100DaysOfCode 013/100 - Modules - continued
#   2020-06-24
#
# Notes:
#  Run pyton on the terminal:  python3
#  Search methods:  dir(str)
#  to search builtin functions:  dir(__builtins__)
#  to import a builtin functions:  import FUNCTION_NAME
#  to get more details:  dir(FUNCTION_NAME)
#  to get help:  help(FUNCTION_NAME.module_name)
#         example:  import.FUNCTION_NAME
#                   dir(time)
#                   help(time.sleep)

# Read a file and waitn 10 seconds and read again - print results
#   Day13 - added error handling for file path not found
#
#
#  I installed pip from the command line and used pip to get a 3rd party module
#  pip - a library in pyton
#  on command line -->  pip3 install pandas
#    this will be a quick demo - more on pandas in future lessons.


import time
import os
import pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean())
        print(data.mean()["st1"])
    else:
        print("file does not exist")
    time.sleep(10)
