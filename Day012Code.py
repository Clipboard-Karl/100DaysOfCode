#-----------------------------------------------
#100DaysOfCode 012/100 - Modules
#   2020-06-22
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

import time

while True:
    with open("files/vegitables_2.txt") as file:
        print(file.read())
        time.sleep(10)
