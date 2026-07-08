# Author: Hayden Herrera
# Date: 2026-07-07
# Description: Add many numbers and print the result

#If integer or float, return true
#If not integer or float, return false
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

#Keep asking for input until user enters a number
def AddNewNum(total):
    newNum = "a"
    newNum = input("Please add next number:")
    newNum = TryAgain(newNum)
    total = float(total) + float(newNum)
    return total

#Check if number
#return true if number
sum = 0
sum = AddNewNum(sum)
print(sum)
while CheckContinue():
    sum = AddNewNum(sum)
    print(sum)