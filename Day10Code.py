#-----------------------------------------------
#100DaysOfCode 010/100 - File Processing
#   2020-06-19
#
#

# Open a file then read and print
myfile = open("animal.txt")
print(myfile.read())

#this moves a curser through the file and leaves it at the end of the File
myfile = open("animal.txt")
content = myfile.read()
myfile.close()      # <-- it is a good practice to close when you are done
print(content)
print("And again")
print(content)

# There is a better way to handle files
#  The file will be closed when the block (intent) ends
with open("animal.txt") as myfile:
    content = myfile.read()

print(content)

#  Specify file path
with open("files/animals_2.txt") as myfile:
    content = myfile.read()

print(content)

# Create a file and write to it
#  **** warning existing files will be overwritten
with open("files/vegitables.txt", "w") as myfile:
    myfile.write("Evelyn")

#  To add to a files
with open("files/vegitables.txt", "w") as myfile:
    myfile.write("Evelyn3\nCucumber\nHunter")

# readn and print the first 90 characters
with open("files/bear.txt", "r") as myfile:
    content = myfile.read()
    print(content[:90])

# function to return a single string charater and a file path and returns
#  the number of occurances of the characters

def george_1(char_in, file_path):
    with open(file_path, "r") as myfile:
        content = myfile.read()
        char_count = 0
        for i in content:
            if i == char_in:
                char_count = char_count +1
    return char_count

print("the character count is: ",george_1("z", "files/bear.txt"))

# the instructors solution
def george_1(char_in, file_path):
    with open(file_path, "r") as myfile:
        content = myfile.read()
        return content.count(char_in)

print("the character count is: ",george_1("y", "files/bear.txt"))

#  create file "file.txt" and write "snail" in the file"
with open("file.txt", "w") as myfile:
    myfile.write("snail")
