#-----------------------------------------------
#100DaysOfCode 014/100 - Interactive English Dictonry
#   2020-06-25
#
#  Open the json file that contains the dictionary data
#    Function Translate takes a word thenn returns the definitation
#    Add Error Handling
#
#   Note:  this does handle some error checking but a lot of improvements could
#          still happen
#
import json
from difflib import get_close_matches   #finds close matches in a list

data = json.load(open("Dictionary/data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s insead?  Enter Y/N" % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Word does not exist in dictionary."
        else:
            return "We didn't understand"
    else:
        return "The word doesn't exist.  Please double check it."

word = input("Enter word:  ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
