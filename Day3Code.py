if 3 > 1:
    print("Greater")
else:
    print("Not Greater")

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

temperatures = [72, 75, 80]
grades = {"joe": 20,"tom": 30,"sue": 27}

# print(mean(temperatures))
print(mean(temperatures))
print("Grades:  ",mean(grades))

def pass_check(pass_word):
    if len(pass_word) >= 8:
        return True
    else:
        return False

pass_word_in = ("12345678")
