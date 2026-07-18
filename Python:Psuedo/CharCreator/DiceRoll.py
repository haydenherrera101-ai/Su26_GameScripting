# Author: Hayden Herrera
# Date: 2026-09-07
# Description: This is for determining dice roll

import random

def dice(sides):
    roll = random.randint(1, int(sides))
    return roll

def percDice():
    roll = random.randint(0, 10)
    return int(roll) * 10

def coinFlip():
    flip = random.randint(1, 100)
    if flip % 2 == 0:
        return "Heads"
    else:
        return "Tails"
