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

# from enum import Enum

# Score categories.
# Change the values as you see fit.
# class yacht(Enum):
YACHT = 0   
ONES = 1 
TWOS = 2 
THREES = 3 
FOURS = 4
FIVES = 5 
SIXES = 6 
FULL_HOUSE = 7 
FOUR_OF_A_KIND = 8 
LITTLE_STRAIGHT = 9 
BIG_STRAIGHT = 10 
CHOICE = 11 


def score(dice, category):
    if category == YACHT:
        for die in dice:
            if die != dice[0]:
                return 0
        return 50
    elif category in range(1, 7):
        score = 0
        for die in dice:
            if die == category:
                score += die
        return score
    elif category == FULL_HOUSE:
        num1 = [dice[0]]
        num2 = []
        for die in dice[1:]:
            if die == dice[0]:
                num1.append(die)
            elif num2 == [] or die == num2[0]:
                num2.append(die)
        if (len(num1) == 2 and len(num2) == 3) or (len(num1) == 3 and len(num2) == 2):
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        num1 = [dice[0]]
        num2 = []
        for die in dice[1:]:
            if die == dice[0]:
                num1.append(die)
            elif num2 == [] or die == num2[0]:
                num2.append(die)
        if len(num1) >= 4:
            return sum(num1[0:4])
        elif len(num2) >= 4:
            return sum(num2[0:4])
        else:
            return 0
    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0
    elif category == CHOICE:
        return sum(dice)
