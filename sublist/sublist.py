"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 2 
SUPERLIST = 3 
EQUAL = 1 
UNEQUAL = 4 

def contains(list_one, list_two):  
    if list_one == []:
        return True
    i = 0
    while i + len(list_one) < len(list_two) + 1:
        if list_one == list_two[i:i + len(list_one)]:
            return True
        i += 1
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif contains(list_one, list_two):
        return SUBLIST
    elif contains(list_two, list_one):
        return SUPERLIST
    return UNEQUAL

sublist([1, 3], [1, 2, 3])
sublist(list(range(1000)) * 1000 + list(range(1000, 1100)), list(range(900, 1050)))
