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

#df what_is_missing_3x3(check_3x3):

if os.path.exists("Files/Sudoku/3x3.csv"):
    input_3x3_df = pandas.read_csv("Files/Sudoku/3x3.csv", header=None)
    print(input_3x3_df)
    print('-------')
else:
    print("file does not exist")

#  Iterate through the input_3x3_df
#     Note:  does not read the last value
#missing_3x3_set = ["1","2","3","4","5","6","7","8","9"]
present_3x3_list = []
print("Before present_3x3_list = ",present_3x3_list)
for y in range(0, 3):
    for x in range(0, 3):
        print("x=",x," y=",y,"  ",input_3x3_df[x][y])
        if input_3x3_df[x][y] == "x":
            print("We need to solve for x!")
        else:
            hold_number = input_3x3_df[x][y]
            if type(hold_number) == str:
                print("Str found!!!!")
                number_as_int = int(hold_number)
                number_as_int + 0
                print(type(number_as_int))
            else:
                number_as_str = str(hold_number)

            print("hold_number is a: ",type(hold_number))

            present_3x3_list.append(hold_number)
            print(input_3x3_df[x][y]," is being added to the list")
            print("present_3x3_list: ",present_3x3_list)

print("After present_3x3_list = ",present_3x3_list)
