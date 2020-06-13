#-----------------------------------------------
#100DaysOfCode day 004
#  I am really overthinking this.  Python is much easiery than Cobol
#  I am trying to define everything and track it.  Mind Blown

#This is my code that worked:
def Warm_Or_Cold(generic_value_to_be_checked):
    if generic_value_to_be_checked > 7:
        answer_to_be_returned  = ("Warm")
    else:
        answer_to_be_returned = ("Cold")
    return answer_to_be_returned

Temp_Check = (6)
print("The temperature is:  ",Warm_Or_Cold(Temp_Check))
Temp_Check = (7)
print("The temperature is:  ",Warm_Or_Cold(Temp_Check))
Temp_Check = (8)
print("The temperature is:  ",Warm_Or_Cold(Temp_Check))


#This is the simplified answer
def Hot_Or_Cold(generic_value_to_be_checked):
    if generic_value_to_be_checked > 7:
        return "HOT"
    else:
        return "COLD"

Temp_Check = (6)
print("The temperature is:  ",Hot_Or_Cold(Temp_Check))
Temp_Check = (7)
print("The temperature is:  ",Hot_Or_Cold(Temp_Check))
Temp_Check = (8)
print("The temperature is:  ",Hot_Or_Cold(Temp_Check))
print("----------------------------------")

# Hot, Warm, Cold assignment

def hwc(generic_value_to_be_checked):
    if generic_value_to_be_checked > 25:
        return "Hot"
    elif generic_value_to_be_checked > 14:
        return "Warm"
    else:
        return "Cold"

Temp_In = (26)
print("The temperature is:  ",hwc(Temp_In))
Temp_In = (25)
print("The temperature is:  ",hwc(Temp_In))
Temp_In = (20)
print("The temperature is:  ",hwc(Temp_In))
Temp_In = (15)
print("The temperature is:  ",hwc(Temp_In))
Temp_In = (14)
print("The temperature is:  ",hwc(Temp_In))
Temp_In = (10)
print("The temperature is:  ",hwc(Temp_In))
