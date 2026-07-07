# Author: Hayden Herrera
# Date: 2026-07-07
# Description: Add two numbers and print the result

#If integer or float, return true
#If not integer or float, return false
def CheckIfNum(userInput):
    return bool(userInput.isdigit() or isinstance(userInput, float))

#Keep asking for input until user enters a number
def TryAgain(userInput):
    while not CheckIfNum(userInput):
        userInput = input("Please enter a valid number: ")
    return userInput

num1 = input("Enter first number: ")
num1 = TryAgain(num1)
num2 = input("Enter second number: ")
num2 = TryAgain(num2)

print("The sum of " + num1 + " and " + num2 + " is: " + str(float(num1) + float(num2)))