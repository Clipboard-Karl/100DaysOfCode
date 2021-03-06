#100DaysOfCode 030/100 - Sudoku Idea
#
#  20200718 - 100DaysOfCode 030/100 - Sudoku Idea
#             The idea is simple really.  Write code that will solve a sudoku puzzle
#
################################################################################
#
#  Needed to open the input file
import os
#  Used to process the input file
import pandas
#  To work with arrays
import numpy as np

#sudoku_array_1 = np.zeros(9)
#sudoku_array_2 = np.array([[0,0,0],[0,0,0],[0,0,0]])
sudoku_array_2 = np.array([["q","q","q"],["q","q","q"],["q","q","q"]])

print(sudoku_array_2)
print(sudoku_array_2.ndim)
print(sudoku_array_2.shape)
print("Print from array: ", sudoku_array_2[1,1])

#  Read the puzzle - 0 is missing number
if os.path.exists("Files/Sudoku/3x3.csv"):
    input_3x3_df = pandas.read_csv("Files/Sudoku/3x3.csv", header=None)
    print(input_3x3_df)
    print('-------')
else:
    print("file does not exist")

#  Iterate through the input_3x3_df
#     Note:  does not read the last value
present_3x3_list =[]
print("Before present_3x3_list = ",present_3x3_list)
for y in range(0, 3):
    for x in range(0, 3):
#        print("x=",x," y=",y,"  ",input_3x3_df[x][y])
        if input_3x3_df[x][y] == 0:
            sudoku_array_2[y,x]="x"
        else:
            present_3x3_list.append(input_3x3_df[x][y])
#            print(input_3x3_df[x][y]," is being added to the list")
#            print("present_3x3_list: ",present_3x3_list)
#   Fill the numpy array
            sudoku_array_2[y,x]=input_3x3_df[x][y]
present_3x3_list.sort()
print("After present_3x3_list = ",present_3x3_list)
length = len(present_3x3_list)
print(length)
#  Build missing list from present_3x3_list
#     This would be easier if I could have removed from the missing list
#     in earlier revieions of the 100DaysOfCode
missing_3x3_list = []
for missing in range(1, 10):
    if missing in present_3x3_list:
        print(missing," is on the list")
    else:
        missing_3x3_list.append(missing)

print("Missing List = ",missing_3x3_list)
print(sudoku_array_2)
