#-----------------------------------------------
#100DaysOfCode 008/100 - Starter Program
#   2020-06-17
#
#  Prompt user to input say something and hit enter.
#      loop until user enters \end
#  Output:
#     print the sentances with capitalization and punctuation.
#
# This is the re-worded program.  I am still thinking old school loops.
#   print("  ".join(results)) -- is much cleaner than looping
#

def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say something: ")
    if user_input == '\end':
        break
    else:
        results.append(sentence_maker(user_input))
        #        continue

print("  ".join(results))
