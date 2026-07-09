import random
#Author: Hayden Herrera
# Date: 2026-07-09
# Description: Ask user if they want a random number
#keep looping until user no longer wants more. User defined maximum


def CheckContinue():
    playAgain = "y"
    while playAgain != "y" or playAgain != "n":
        playAgain = str.lower(input("Would you like to add another number? (y/n): "))
        if playAgain == "y":
            return True
        elif playAgain == "n":
            return False
        else:
            print("Please enter 'y' or 'n'.")
    return True

#check if letter
def InputIsLetter(userInput):
    if userInput.isalpha():
        return True
    else:
        return False
    
#check if space
def InputIsSpace(userInput):
    if userInput.isspace():
        return True
    else:
        return False
    
#check if enter/empty
#length less than 1, true
#1 or more, false
def InputIsEnter(userInput):
    if len(userInput) < 1:
        return True
    else:
        return False

#Master error check
def TryAgain(userInput):
    while InputIsLetter(userInput) or InputIsSpace(userInput) or InputIsEnter(userInput):
        userInput = input("Please enter valid number: ")
    return userInput

userMax = "a"
compNum = "a"

while CheckContinue():
    userMax = input("Please enter the maxiumum integer: ")
    userMax = TryAgain(userMax)
    compNum = random.randint(0, int(userMax))
    print("Random Number:" + str(compNum))