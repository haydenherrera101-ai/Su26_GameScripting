# Author: Hayden Herrera
# Date: 2026-07-07
# Description: Take string user, print out capitalized version of the string
#print ("Hello from Capit!")

#Check if number
#return true if number
#return false if not a number
def CheckIfNumber(userInput):
    if userInput.isdigit():
        print("Please enter a string, not a number.")
    return userInput.isdigit()

#Check if spaces
#Return true if spaces
#Return false if not spaces
def CheckIfSpaces(userInput):
    if userInput.isspace():
        print("Please enter a string that is not spaced.")
    return userInput.isspace()

#Check if empty
#Return true if empty
#Return false if not empty
def CheckIfEmpty(userInput):
    if not userInput:
        print("Prompt is empty, please enter a string.")
        return True
    else:
        return False

#Check if capped
#Return true if all caps
#Return false if not all caps
def CheckIfCapped(userInput):
    if userInput == str.upper(userInput):
        print("Please enter a string that is not all capitalized.")
        return True
    else:
        return False

#Check all
def CheckAll(userInput):
    while CheckIfNumber(userInput) or CheckIfSpaces(userInput) or CheckIfEmpty(userInput) or CheckIfCapped(userInput):
        userInput = str(input("Please enter valid string: "))
    return userInput

strToUpper = str(input("Enter a string: "))
print(str.upper(CheckAll(strToUpper)))

#At most simple:
#print(str(input("Enter a string: ")).capitalize())