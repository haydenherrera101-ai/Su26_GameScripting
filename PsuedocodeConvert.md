--Hayden Herrera
--06/30/2026
--These contain all psuedo code scripts that have been individually converted into fucntional programs.

AddManyNums.lua
-- This is a fundamental to add numbers from users until they say stop, then printing the result.
---------------
local function printUserSum()
--variables
local newNum = nil
local sum = 0
local mathDone = false
local choice

- while the math isn't done, keep asking for numbers
while not mathDone do

--Get new number from user
    while (newNum == nil or newNum == "" or not tonumber(newNum)) do
        print("Enter a number to add to the total: ")
        newNum = io.read()
    end
    
--Add to total
    sum = sum + newNum

--reset usernum variable for next loop
    newNum = nil

--Ask user if they want to add another number
    print("Do you want to add another number? (y/n): ")
    choice = io.read()
    if string.upper(choice) == "N" then
        mathDone = true
  --print total
        print ("The total sum of all numbers entered is: " .. sum)
        mathDone = true
        break
    end

end


end
printUserSum()

---------------------------------------------------------------------------------------

AddTwoNums.lua
--This is a fundamental of adding two numbers to get the sum, then printing the result.
--------------
  variables
  local num1 = nil
  local num2 = nil
  local sum

   -- Get first number from user
    while (num1 == nil or num1 == "" or tonumber(num1) == nil) do
        print("Enter the first number:")
        num1 = io.read()
    end


   -- Get second number from user
    while (num2 == nil or num2 == "" or tonumber(num2) == nil) do
        print("Enter the second number:")
        num2 = io.read()
    end

   --Add numbers together
    sum = num1 + num2
    --Print total
    print("The sum of " .. num1 .. " + " .. num2 .. " is: " .. sum)

---------------------------------------------------------------------------------------

ChangeToUpperCase.lua
--This is a fundamental to converting user-input into all caps, then printing the result.
---------------------

local function capitalizeIt()
    local userInput = ""

   -- while input is empty or numeric, ask again
    while (
        userInput == nil or userInput == "" or
        userInput == tonumber(userInput) or
        userInput == string.upper(userInput)
    ) do
        -- prompt user
        print("What phrase do you want to capitalize: ")
        -- get user input to capitalize
        userInput = io.read()
    end

   -- capitalize it
    return string.upper(userInput)
end

print(capitalizeIt())

---------------------------------------------------------------------------------------

CompRandom.lua
-- Gets user defined high, then have comp generate a random number between 0 and that high and printing the result.
-- **ALLOW to CONTINUE PLAY
---------------
local function printRandomNum()
    --variables
    local maxNum = nil
    local randomNum = nil
    local keepPlaying = true
    
  --Set up random number
    math.randomseed(os.time())
    math.random(); math.random(); math.random() -- "warm up" the random number generator
    
   --While Still Playing 
    while keepPlaying == true do
        --Ask user for max number
        while (maxNum == nil or maxNum == "" or not tonumber(maxNum)) do
            print("Give me a higher number: ")
            maxNum = io.read()
        end
        --Print random number
        print("The random number between 1 and " .. maxNum .. " is: " .. math.random(1, maxNum))

  --Ask user if they want to continue playing
    print ("Do you want to continue playing? (y/n): ")
    local choice = io.read()
    if string.upper(choice) == "N" then
        keepPlaying = false
        break
    end
        keepPlaying = true
        maxNum = nil

end
    print("Thanks for playing!")
end

printRandomNum()

---------------------------------------------------------------------------------------

EvenOdds.lua
--This focuses on even and odd numbers. It will show how many are
--even and how many are odd in a given range. It will also show the
--sum of the even numbers and the sum of the odd numbers.
------------
local zerocount = 0
local evencount = 0
local oddcount = 0
local counter = 0
local checkNum

--randoma number generator
math.randomseed(os.time())
math.random(); math.random(); math.random()

while counter < 10 do
    --get a random number between 0 and 100
    checkNum = math.random(0, 100)

  --check if 0
    if checkNum == 0 then
        zerocount = zerocount + 1
        print(checkNum.. " is zero.")

  --if not 0, check if even or odd
    else
        --check if odd
        if math.fmod(checkNum, 2) == 1 then
            oddcount = oddcount + 1
            print(checkNum.. " is odd.")
        --check if even
        else
            evencount = evencount + 1
            print(checkNum.. " is even.")
        end

  end
    counter = counter + 1
end

print("Zeroes: " .. zerocount)
print("Evens: " .. evencount)
print("Odds: " .. oddcount)
