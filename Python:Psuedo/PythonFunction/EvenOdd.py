import random
#Author: Hayden Herrera
# Date: 2026-07-07
# Description: This will be going into loops to determine whether the validated integers
# are either even or odd.

counter = 0
zeroCount = 0
evenCount = 0
oddCount = 0
compNum = 0

while counter < 10:
    #get a random num
    compNum = random.randint(0, 100)
    print(compNum)
    if compNum == 0: #ZERO
        zeroCount = zeroCount + 1
    elif compNum % 2 == 1: #ODD
        oddCount = oddCount + 1
    else: #EVEN
        evenCount = evenCount + 1
    counter = counter + 1

print("Zeros: " + str(zeroCount))
print("Left Count: " + str(oddCount))
print("Right Count: " + str(evenCount))

