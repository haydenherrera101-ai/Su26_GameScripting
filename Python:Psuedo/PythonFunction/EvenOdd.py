#Author: Hayden Herrera
# Date: 2026-07-07
# Description: This will be going into loops to determine whether the validated integers
# are either even or odd.



def CheckNum(userInput):
    if userInput.isalpha():
        print("Please enter a number that is not a string.")
    return userInput.isalpha()


def CheckSpace(userInput):
    if userInput.isspace():
        print("Please enter a string that is not spaced.")
    return userInput.isspace()


def CheckEmpty(userInput):
    if len(userInput) < 1:
        print("Prompt is empty, please enter a number.")
        return True
    else:
        return False
    

def TryAgain(userInput):
    while CheckNum(userInput) or CheckSpace(userInput) or CheckEmpty(userInput):
        userInput = input("Please enter a valid number: ")
    return userInput


number = input("Enter a number: ")
number = TryAgain(number)

number = int(number)

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")