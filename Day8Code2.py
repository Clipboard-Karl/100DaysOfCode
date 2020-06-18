#-----------------------------------------------
#100DaysOfCode 008.1/100 - List Comprehesions
#   2020-06-17
#
#  I had some extra time so I am getting more coding in
#

temps = [221, 234, 340, -9999, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)


# or do This
new_temps_2 = [temp / 10 for temp in temps]

print(new_temps_2)

# now with if conditional

new_temps_3 = [temp / 10 for temp in temps if temp != -9999]

print(new_temps_3)


# Print non strings or numbers only
karl_list = ([99, 'no data', 95, 94, 'no data'])

def george(lst):
    return [i for i in lst if not isinstance(i, str)]

print(george(karl_list))

# Print non strings or numbers only
karl_list_1 = ([-5, 3, -1, 101])

def george_1(lst):
    return [i for i in lst if i >= 0 ]

print(george_1(karl_list_1))

# replace with 0
karl_list_2 = ([99, 'no data', 95, 94, 'no data'])

def geroge_2(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]

print(geroge_2(karl_list_2))

#  Convert and Sum Up
karl_list_3 = (['1.2', '2.6', '3.3'])

def george_3(lst):
    return sum([float(i) for i in lst])

print(george_3(karl_list_3))
