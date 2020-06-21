#-----------------------------------------------
#100DaysOfCode 011/100 - Continuing with File Processing
#   2020-06-21
#
#

# Read a file and create a new file with the first 90 characters
with open("files/bear.txt") as myfile:
    content = myfile.read()

with open("files/first.txt", "w") as myfile:
    myfile.write(content[:90])


# Append a file
#    (a) will append but not allow a read
#    (a+) will allow read/write
#    seek(0)  resets the curser to the zero positon
with open("files/vegitables.txt", "a+") as myfile:
    myfile.write("\nOkra")
    myfile.seek(0)
    content = myfile.read()

print(content)

#  Assignment - append text1 to test2
with open("files/animals_2.txt", "r") as myfile:
    content = myfile.read()

with open("files/vegitables.txt", "a+") as myfile:
    myfile.write(content)

# Assignment - read file and append the content to the end twice
with open("files/vegitables.txt", "r+") as myfile:
    content = myfile.read()
    myfile.write(content)
    myfile.write(content)
