
# Author: Hayden Herrera
# Date: 2026-10-07
# Description: This program creates a Text Adventure with min. 10 prompts for the user
# It will be a interactive adventure which uses text commands when given choices which will influence the outcome of the game or story. 
# This kind of interactive adventure would dive into two friends heading home and would attempt to
# take a shortcut into a mysterious forest which lies a unknown being.

import sys
from time import sleep

gameOver = False
playerName = ""

"""======================================================================================================================"""
"""====================================================FUNCTIONS========================================================="""
"""======================================================================================================================"""

#CHECKING CODES

#Checks for complex invalid answers
def checkYN(choice, y, n):
    choice = str.lower(choice)

    while choice != y and choice != n:
        print("Please enter", y, "or", n)
        choice = str.lower(input("> "))

    return choice


# Checks numbered choices
def checkChoice(choice, options):
    while choice not in options:
        print("Invalid choice. Please pick 1 or 2.")
        choice = input("> ")

    return choice


"""====================="""
"""     Story Chunks    """
"""====================="""

def introHome():

    global playerName

    print("What is your name?")
    playerName = input("> ")

    while len(playerName) < 1 or playerName.isspace() or not playerName.isalpha():
        print("Please enter your first name only.")
        playerName = input("> ")

    """On your way driving home with your friend Fred, Fred would take a shortcut within the forest."""

    print("\nAfter a thrilling party with your friend Fred, he offers to take you back home before midnight.")
    sleep(2)

    print("You notice as you both drive down an unfamilar passage towards the forest.")
    sleep(2)

    print(playerName + ": Where exactly are we going? Why aren't we taking the highway?")
    sleep(3.5)

    print("\nFred: Relax dude. I have this shortcut in mind that could take us home much faster.")
    sleep(5)

    print("Though you are ensured by Fred that he knows the way out of this trail, you can't feel but feel uncertain of this unknown forest. . .")
    sleep(4)

    forest()



def forest():

    """You drive into the forest trail"""

    print("As you drive, you notice that the trees become bigger and the trail getting darker. . .")
    sleep(2)

    print("You take a moment to think.")


    print("\nWhat do you say?:")
    print("1. I think we should turn back.")
    print("2. You sure this trail is safe?")


    choice1 = checkChoice(input("> "), ["1", "2"])


    if choice1 == "1":

        print("\n" + playerName + ": I think you should turn back, This forest is giving me the creeps.")
        sleep(3)

        print("Your friend looks at you with a scornful way")
        sleep(4)

        print("Fred: Hell nah, man. Don't be a suck up. This shortcut is the way to go.")

    else:

        print("\n" + playerName + ": So you're positive that taking this trail is safe?")
        sleep(3)

        print("\nFred: Of course it is. These are one of many trails used back in the 1600s.")


    sleep(4)

    print("Fred: Besides, this trail leads us to the interstate in about-")

    sleep(1.5)

    print("\nBefore he could finish, the car unknowingly collides with something and would cause it to shake aggressively.")

    sleep(3)

    print("Fred pushes the brakes immediately, his face turning slightly pale.")

    sleep(3)

    print("\nFred: What the hell was that?")

    sleep(2)

    investigate()




def investigate():

    """With the front tire damaged, they have no choice but to fix the tire or investigate what they struck"""

    print("You both would exit the vehicle and notice that the right front tire has flattened.")

    sleep(3.4)

    print("\nWhat should you do first?")
    print("1. Check the damaged car.")
    print("2. Look around the road.")

    choice = checkChoice(input("> "), ["1", "2"])

    if choice == "1":
            print("\nYou inspect the vehicle and discover the front tire has completely blown out.")
            sleep(2)
    else:
            print("\nYou shine your phone around the road but only find blood across the track and seems to be leading into the woods.")
            sleep(2)
            print("\nFred: Hey, focus! We got to see if the car is alright.")
            sleep(2)
            print("As Fred inspects the car, he finally assesses the damages.")

            sleep(3)
    print("\nFred: Dammit! The tire is busted, I'm going to grab a spare tire on the back. Just stay right there.")

    sleep(2)

    print("You understand the situation and await for Fred to ask for help. . .")

    sleep(5)

    print("\nHowever. . .")

    sleep(3)

    print("\nYou hear a faint animalistic growl only a few feet away. You believe that's what they hit.")

    sleep(2)

    print(playerName + ": What was that?")

    print("\nShould you investigate:")
    print("1. Yes")
    print("2. No")


    choice2 = checkChoice(input("> "), ["1", "2"])


    if choice2 == "1":

        print("\nWhile you wait for Fred to fix up the tire, you decide to walk up to the creature.")

        sleep(3)

        print("As you approach the creature, you flash it with your phone light to get a better look.")

        sleep(4)

        print("The appearance of this unknown creature has a highly grotesque, asymmetric, and chaotic amalgamation. This was no animal. This was an abomination. . .")

        sleep(2)

        print("Its amalgamated body would begin to move slowly and would stare directly at you as it starts to utter words.")

        sleep(2)

        print("\nThe creature slowly stares at you.")

        sleep(2)

        print("\nWhat do you do?")
        print("1. Stand completely still.")
        print("2. Slowly back away.")

        choice = checkChoice(input("> "), ["1", "2"])

        if choice == "1":
            print("\nThe creature tilts its head but doesn't attack.")
        else:
            print("\nYou carefully step backwards while keeping your eyes on it.")

        sleep(4)

        print("\nEntity: Mors tibi imminet... Poenas dabis...")

        sleep(2)

        print("\n" + playerName + ": Oh my god. . . ")

        sleep(2)

        print("As it slowly regains its strength, you hastily run back towards the car to warn Fred.")

        sleep(4)

        print("Fred happens to see you, however, he is very upset that you left him there.")

        sleep(2)

        print("\nFred: I told you to stay here! where have you been?")

        sleep(2)

        print("Fred then stops after hearing a random sound that came from the forest and notice a creature slowly approaching from afar.")

        sleep(3)

        runOrhide()


    else:

            print("Though curiosity was running your mind. You would rather stay with Fred in order to get out of this forest.")

            sleep(3)

            print("\nFred: Hey, can you pass me the trolley jack, I got the tire out from the back.")

            sleep(2)

            print("\nAs you help Fred with repairing the car, ya'll would hear a faint growl from the distance.")

            sleep(3)

            print("You and Fred stop to see where that random sound came from and notice a creature slowly approaching from afar.")

            sleep(3)

            print("The appearance of this unknown creature has a highly grotesque, asymmetric, and chaotic amalgamation. This was no animal. This was an abomination. . .")

            sleep(5)

            runOrhide()

    

def runOrhide():
    """As the creature approaches, the vehicle has yet to be repaired and have no choice but to avoid the creatures wrath"""

    print("\nYou try thinking of a plan to Fred, but as you turn to him, he has already fled into the trees.")

    sleep(2)

    print("\n" + playerName + ": Fred, you bastard!")

    sleep(2)

    print("The creature begins to pick up speed as you go into the forest.")

    sleep(3.4)

    print("As you go further into the dark forest, you take a moment to catch your breath.")

    sleep(3)


    print("\nWhat shall you do:")

    print("1. Run back to the car")

    print("2. Hide within the trees")


    choice3 = checkChoice(input("> "), ["1", "2"])



    if choice3 == "1":

        print("\nWhile the creature is distracted trying to find one of you, you make a break for it towards the car.")

        sleep(4)

        print("As you approach the car, you see that the tire has yet to be repaired.")

        sleep(4)

        print("\n" + playerName + ": Dammit! The car isn't fixed yet!")

        print("In desperation to get out of here, Fred is nowhere to be seen and he had the keys.")

        sleep(3)

        leaveEarly()


    else:

        print("\nYou decide to hide within the trees, hoping the creature passes by.")

        sleep(4)

        print("You stay completely still as the creature walks closer.")

        sleep(4)

        print("The creature stops directly in front of you.")

        sleep(3)

        print("You hold your breath, hoping it does not notice you.")

        sleep(3)

        print("Suddenly, a loud noise echoes throughout the forest.")

        sleep(2)

        print("The creature turns away and disappears deeper into the forest.")

        sleep(4)

        print("You slowly leave your hiding spot and attempt to find Fred.")

        findFred()


def leaveEarly():
    """Another bad ending but you die"""

    print("Fred is the only one who can get you out of here, but fear clouds your mind.")

    sleep(2)

    print("With hesitation, you are put into another risky decision.")


    print("\nWhat should you do:")

    print("1. Run to any sign of road.")

    print("2. Find Fred.")


    choice5 = checkChoice(input("> "), ["1", "2"])

    if choice5 == "1":
        awfulEnding()

    else:

        findFred()






def findFred():

    """Searching for Fred after escaping the creature"""

    print("\nYou look around the forest, searching for any sign of Fred.")

    sleep(3)

    print("The darkness makes it difficult to see, but you notice footprints leading further into the trees.")

    sleep(3)


    print("\nWhat shall you do:")

    print("1. Leave him behind")

    print("2. Search for Fred")


    choice4 = checkChoice(input("> "), ["1", "2"])



    if choice4 == "1":
        badEnd()


    else:

        print("\nYou follow the footprints deeper into the forest.")

        sleep(4)

        print("The sounds of the forest become quieter as you move further away.")

        sleep(3)

        print("You finally find Fred hiding behind a large tree.")

        sleep(3)

        print("\nFred: Dude... where have you been? I thought you were gone.")

        sleep(3)

        print("You explain everything that happened while trying to convince Fred to leave.")

        sleep(4)

        print("Together, you both rush back towards the vehicle.")

        sleep(3)

        escapeForest()




def escapeForest():

    """Final escape sequence"""

    print("\nAfter several tense moments, you finally reach the vehicle.")

    sleep(3)

    print("\nFred: HELP ME FIX THIS TIRE!")

    print("\nFred hands you the tire iron.")

    print("1. Help finish changing the tire.")
    print("2. Keep watch for the creature.")

    choice = checkChoice(input("> "), ["1", "2"])

    if choice == "1":
        print("\nYou urgently assist Fred and grab the tire iron.")
        sleep(2)
        print("Together you finish replacing the tire much faster.")
        sleep(2)
        print("\n" + playerName + ": OKAY, WE GOT IT!")
    else:
        print("\n" + playerName + ": Hey! You know cars better than me! I'll be on look out!")
        sleep(2)
        print("Fred: Fine! Just make sure it isn't near while I fix this!")
        print("\nYou scan the darkness while Fred struggles with the tire.")

    sleep(2)

    print("As you all quickly replace the tire")

    sleep(1)

    print("The creature aggressively hits the car trying to reach us.")

    sleep(3)

    print("\nEntity: RRRROOOAAAAAAAHHHHHHHRRRRRR")

    print("\nFred quickly starts the engine as the creature's sounds grow closer.")

    sleep(4)

    print("The tires spin against the dirt before the vehicle finally begins moving.")

    sleep(2)

    print("As the creature tries to hold on, it lets go from all the momentum.")

    sleep(4)

    print("You both drive through the forest trail without looking back.")

    theEnd()


def awfulEnding():

    """You make the fateful mistake that costs your life."""

    print("You attempt to find any sign of escape and you would hear a faint scream in the distance.")

    sleep(2)

    print("You can't help but believe you left Fred to die, but you are more focused on escaping it has left your mind.")

    sleep(4)

    print("As you go further, you see a faint light in the distance of the trees.")

    sleep(2)

    print("\n" + playerName + ": Yes. . . A way out. I'm free!")

    sleep(3)

    print("As you almost exit the horrors of the forest, a long elastic arm springs out from behind and grabs you.")

    sleep(2)

    print("\n" + playerName + ": AH! HOLY SHIT!!")

    sleep(2)

    print("You turn around to see the creature but you then realize its new features.")

    sleep(5)

    print("\nFred: hEeElPp MmeEe")

    sleep(2)

    print("You see that the amalgamated creature has fused with what's left of Fred and now slowly pulls you in.")

    sleep(2)

    print("As you are dragged away from safety, you would be slowly consumed by the creature.")

    sleep(1)

    print("\n" + playerName + ": OH GOD!!! NO! NO! NOOOOOOOOOO!!!!!!")

    sleep(2)

    print("As you sink into the creature, the last thing you see is the light from the road which then falls to darkness.")

    sleep(4)

    print("\nBecoming part of it's collection. . .\n")

    sleep(2)

    print("\n==============================")
    print("      AWFUL ENDING")
    print("      'Consumed'")
    print("==============================")

    playAgain()


def badEnd():

    """Bad Ending"""

    print("\nFear takes over.")
    sleep(2)

    print("You convince yourself that Fred is already gone.")
    sleep(3)

    print("You would hear a faint cry from both Fred and the creature as if they were screaming synchronously.")

    print("Without looking back, you sprint through the forest until you finally reach the road.")
    sleep(3)

    print("Hours later, a passing driver notices you and calls the police.")
    sleep(3)

    print("Despite a massive search effort, Fred is never found.")
    sleep(3)

    print("Weeks pass, but his disappearance remains an unsolved mystery.")
    sleep(3)

    print("Every night, you hear echoes of Fred calling your name in your dreams.")
    sleep(4)

    print("\nYou wonder...")
    sleep(2)

    print("\"Could I have saved him?\"")
    sleep(3)

    print("\n==============================")
    print("      BAD ENDING")
    print("      'Left Behind'")
    print("==============================")

    playAgain()


def theEnd():

    """Ending"""

    print("\nAfter several tense minutes, the forest becomes completely silent.")

    sleep(3)

    print("Neither of you says a word as you drive away from the forest.")

    sleep(3)

    print("\nWhen you finally reach the highway, you ask him one favor.")

    sleep(3)

    print("\n" + playerName + ": We are NOT taking that route again, man. . .")

    sleep(2)

    print("\n. . .\n")

    sleep(4)

    print("\n. . .\n")

    sleep(4)

    print("\nFred: Agreed. . .")


    print("\n========================")

    print("        THE END")

    print("========================")

    playAgain()


#Replay Function. Once prompt is entered "y", will send the game back to the beginning story chunks
#and follows up with the error checks. If "n", game will immediately end to prevent potential loops.
def playAgain():
    replay = checkYN(input("\n Would you like to play again (y/n): "), "y", "n")

    if replay == "y":
        introHome()
        forest()
        investigate()
        runOrhide()
    else:
        print("\nThanks for playing!")
        sys.exit()
