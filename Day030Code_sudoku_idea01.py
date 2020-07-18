#100DaysOfCode 030/100 - Sudoku Idea
#
#  20200718 - 100DaysOfCode 030/100 - Sudoku Idea
#             The idea is simple really.  Write code that will solve a sudoku puzzle
#
#
#
#
################################################################################
#
#  Needed to open the input file
import os
#  Used to process the input file
import pandas

#df what_is_missing_3x3(check_3x3):

if os.path.exists("Files/Sudoku/3x3.csv"):
    input_3x3_df = pandas.read_csv("Files/Sudoku/3x3.csv", header=None)
    print(input_3x3_df)
    print('-------')
#    this is how you index a dataframe
#    print(input_3x3_df[0][1])
else:
    print("file does not exist")

#  Iterate through the input_3x3_df
#     Note:  does not read the last value

#########   NOT WORKING!!!!!
#   it is not removing the items from the list as expected.
#
# with this input I need to change the 3 to a string to remove it
#6,x,x
#5,3,x
#2,x,x
#  I am givin up - I have no clue and spent way to much time.
#  trying new code in file 02
#
#
#missing_3x3_list = ["1","2","3","4","5","6","7","8","9"]
missing_3x3_list = [1,2,3,4,5,6,7,8,9]
print("Before missing_3x3_list = ",missing_3x3_list)
for y in range(0, 3):
    for x in range(0, 3):
        print("x=",x," y=",y,"  ",input_3x3_df[x][y])
        if str(input_3x3_df)[x][y] in missing_3x3_list:
            print("Removing: ",input_3x3_df[x][y])
            missing_3x3_list.remove(input_3x3_df[x][y])
        else:
            print(input_3x3_df[x][y]," is not in the list")
        print("Missing list: ",missing_3x3_list)

print("After missing_3x3_list = ",missing_3x3_list)
