import time
import Player
import Helpers

examined_room = False
saw_start_description = False

def start_description():
    global saw_start_description
    Helpers.stylized_print("You find yourself in .... a train conductor's booth?")
    print("\n")
    saw_start_description = True


def room_description():
    Helpers.stylized_print("Around you, a tight and cramped space mostly filled with a large switch board")
    Helpers.stylized_print("Lights blink and mechanical beeps fill the small room.")
    Helpers.stylized_print("On the board, you notice a singular, huge lever.")
    Helpers.stylized_print("One wall is just a window, overlooking a forked train track.")
    Helpers.stylized_print("In the distance you can see the lights of an oncoming train, heading for the fork.")
    Helpers.stylized_print("A small and visibly anxious man paces around the room.")
    print("\n")

def return_description():
    Helpers.stylized_print("You're standing in the trolley room.")
    print("\n")

# handles both the first visit (room not yet examined) and every visit after
def menu(show_return_description=True):
    global displaying_menu
    global examined_room

    Player.player_location = "trolley"

    if not examined_room:
        if not saw_start_description:
            start_description()
        else:
            return_description()
    elif show_return_description:
        return_description()

    Helpers.stylized_print("What do you do next?")
    if not examined_room:
        Helpers.stylized_print("\t1. Examine your surroundings")
        Helpers.stylized_print("\t2. Turn back to the alley")
    else:
        Helpers.stylized_print("\t1. Approach the man")
        Helpers.stylized_print("\t2. Examine your surroundings")
        Helpers.stylized_print("\t3. Turn back to the alley")
    player_choice = input("> ").strip()

    if not examined_room:
        if player_choice == "1":
            room_description()
            examined_room = True
            return menu(show_return_description=False)

        elif player_choice == "2":
            Helpers.stylized_print("You turn back to the alley.")
            print("\n")
            Player.player_location = "alley"
            displaying_menu = False

        else:
            print("Please choose a valid option.")
    else:
        if player_choice == "1":
            if not Player.flags["metTrolleyMan"]:
                dialogue_menu()
            elif "essence of hope" in Player.player_inventory:
                Helpers.stylized_print("The man looks calm")
                Helpers.stylized_print("and the kitten basks in the sunlight streaming in from the window.")
                return menu()
            else:
                Helpers.stylized_print("the man doesnt seem any calmer now that the lever fiasco is over. ")
                print("\n")

                if "cat box" in Player.player_inventory:
                    Helpers.stylized_print("\t1. Give him the cat box")
                    Helpers.stylized_print("\t2. Nevermind (leave)")
                    player_response = input("> ").strip()

                    if player_response == "1":
                        Helpers.stylized_print("The man stops pacing as you hand him the box")
                        Helpers.stylized_print("What's this...?")
                        Helpers.stylized_print("He gingerly puts the box on the ground and opens it.")
                        Helpers.stylized_print("Out pops a small orange kitten, mewing loudly.")
                        Helpers.stylized_print("All things considered, it looks perfectly healthy. ")
                        print("\n")
                        Helpers.stylized_print("The man opens his mouth in shock")
                        Helpers.stylized_print("and the kitten proceeds to curl up by his foot.")
                        Helpers.stylized_print("it's purring. ")
                        print("\n")
                        Helpers.stylized_print("He bends down to pet it, and for once he doesn't look so anxious.")
                        print("\n")
                        Helpers.stylized_print("I .... I am always worried about potentially doing the wrong thing one day,")
                        Helpers.stylized_print("constantly running all these future scenarios in my head, all these hypotheticals...")
                        Helpers.stylized_print("the man trails off.")
                        print("\n")
                        Helpers.stylized_print("the kitten continues to purr.")
                        print("\n")
                        Helpers.stylized_print("I think I'd forgotten that I can't account for the future.")
                        Helpers.stylized_print("Only right now.")
                        Helpers.stylized_print("And right now - ")
                        Helpers.stylized_print("He picks the kitten up and places it on his shoulder - ")
                        Helpers.stylized_print("I'm going to take care of this little guy.")
                        Helpers.stylized_print("The man smiles.")
                        print("\n")
                        Helpers.stylized_print("I think this is for you, my friend.")
                        print("\n")
                        Helpers.stylized_print("you aquire the ESSENCE OF HOPE!")
                        Helpers.stylized_print("this warm, glowing orb glimmers in your hand.")

                        Player.player_inventory.append("essence of hope")
                        Player.player_inventory.remove("cat box")
                        return menu()

                    elif player_response != "2":
                        print("Please choose a valid option.")

                return menu()

        elif player_choice == "2":
            room_description()
            return menu(show_return_description=False)

        elif player_choice == "3":
            Helpers.stylized_print("You turn back to the alley.")
            print("\n")
            Player.player_location = "alley"
            displaying_menu = False

        else:
            print("Please choose a valid option.")

def dialogue_menu():
    dialogue_looping = True
    Player.flags["metTrolleyMan"] = True

    Helpers.stylized_print("As you approach the man he stops pacing and looks intently at you.")
    Helpers.stylized_print("Oh, THANK GOD you're here!")
    Helpers.stylized_print("We're almost out of time - quick - it's over there!")
    Helpers.stylized_print("He points at the oversized lever on the switch board.")
    Helpers.stylized_print("He covers his eyes. Just.... do it! I cant watch!!")

    while dialogue_looping:
        print("\n")
        Helpers.stylized_print("\t1. What is happening??")
        Helpers.stylized_print("\t2. What do you want me to do??")
        print("\n")
        player_response = input("> ").strip()


        if player_response == "1" or player_response == "2":
            Helpers.stylized_print("You mean you don't know???")
            Helpers.stylized_print("I thought the higher ups sent a professional!!")
            Helpers.stylized_print("He exhales quickly. You have to choose!")
            Helpers.stylized_print("Do nothing and 5 people get hit by the train!")
            Helpers.stylized_print("Pull the lever, switch the track, and doom one person to get hit by the train!")
            Helpers.stylized_print("While he's yelling, you look out the window. No one is standing on the tracks.")
            print("\n")

            Helpers.stylized_print("\t1. Um, buddy, no ones in danger. I don't see anyone on the tracks.")
            Helpers.stylized_print("\t2. Ok, here I go - (approach the lever)")
            player_response = input("> ").strip()

            # No ones in danger
            if player_response == "1":
                Helpers.stylized_print("I know that!")
                Helpers.stylized_print("But what IF??")
                Helpers.stylized_print("The potential moral dilemma is just too much for me to bear!!")
                print("\n")
                lever_choice()
                return

            elif player_response == "2":
                lever_choice()
                return

            else:
                print("Please choose a valid option.")

        else:
            print("Please choose a valid option.")

def lever_choice():
    global player_response
    Helpers.stylized_print("You approach the lever")
    print("\n")
    Helpers.stylized_print("What do you do next?")
    Helpers.stylized_print("\t1. Pull the lever")
    Helpers.stylized_print("\t2. Do nothing")
    player_response = input("> ").strip()

    if player_response == "1":
        # level pulling dialogue
        Helpers.stylized_print("you pull the lever, and watch through the window, ")
        Helpers.stylized_print("as the tracks shift at the fork.")
        Helpers.stylized_print("moments later the train rushes by.")
        Helpers.stylized_print("if there -had- been someone there, they surely would have been a goner.")
        print("\n")
        Helpers.stylized_print("the anxious man peers through his fingers at you")
        Helpers.stylized_print("is it over??")
        print("\n")
        Helpers.stylized_print("he straightens himself out.")
        Helpers.stylized_print("I see you chose to pull the lever.")
        Helpers.stylized_print("I couldn't have made that choice. Or, erm. Maybe I should have?")
        Helpers.stylized_print("One person IS less than five, after all. Less suffering..")
        Helpers.stylized_print("But your actions doomed the one person.....")
        print("\n")
        Helpers.stylized_print("The man seems to be overcome with anxiety")
        Helpers.stylized_print("as he reckons with the potential of making a difficult moral choice.")
        Helpers.stylized_print("He begins to pace again, muttering to himself.")
        Helpers.stylized_print("What -would- I do? he asks to himself repeatedly.")

        Player.flags["pulledLever"] = True
        Helpers.stylized_print("")
        mirror_shard_menu()

    elif player_response == "2":
        # do nothing dialouge
        Helpers.stylized_print("You watch through the window ")
        Helpers.stylized_print("as the train rushes by, the lever remaining untouched.")
        Helpers.stylized_print("if there -had- been 5 people there, they surely would have been goners.")
        Helpers.stylized_print("the anxious man peers through his fingers at you")
        Helpers.stylized_print("is it over??")
        Helpers.stylized_print("he straightens himself out.")
        Helpers.stylized_print("I see you chose to not pull the lever.")
        Helpers.stylized_print("I couldn't have made that choice. Or, erm. Maybe I should have?")
        Helpers.stylized_print("It'd make sense to save 5 people over one...")
        Helpers.stylized_print("But then you'd be directly causing the suffering")
        Helpers.stylized_print("instead of merely witnessing it...")
        Helpers.stylized_print("The man seems to be overcome with anxiety")
        Helpers.stylized_print("as he reckons with the potential of making a difficult moral choice.")
        Helpers.stylized_print("He begins to pace again, muttering to himself.")
        Helpers.stylized_print("What -would- I do? he asks to himself repeatedly.")

        Player.flags["pulledLever"] = False
        Helpers.stylized_print("")
        mirror_shard_menu()

    else:
        print("Please choose a valid option.")
        return lever_choice()

def mirror_shard_menu():
    Helpers.stylized_print("")
    Helpers.stylized_print("As you turn to leave the booth you notice a small glint on the ground, and reach to pick up...")
    Helpers.stylized_print("MIRROR SHARD. It's once jagged edges seem to have been worn smooth by time. ")
    Player.player_inventory.append("mirror shard")
    print("\n")
    Helpers.stylized_print("What do you see when you look in the mirror?")
    Helpers.stylized_print("\t1. Nothing, I choose not to look.")
    Helpers.stylized_print("\t2. Someone who's lived a good life. Smile lines frame your mouth.")
    Helpers.stylized_print("\t3. Someone who's seen hard times. You look tired and worn down.")
    player_response = input("> ").strip()

    while player_response not in ("1", "2", "3"):
        print("Please choose a valid option.")
        player_response = input("> ").strip()

    if player_response == "1":
        Helpers.stylized_print("")
        Player.flags["mirrorShardDescription"] = "didntLook"
        Helpers.stylized_print("Whether due to indifference or fear of what you might see, you dont look.")
        Helpers.stylized_print("You place the mirror in your pocket without a glance. ")
        print("\n")
    elif player_response == "2":
        Helpers.stylized_print("")
        Player.flags["mirrorShardDescription"] = "goodLife"
        Helpers.stylized_print("With a lightness in your heart,")
        Helpers.stylized_print("you put the mirror shard in your pocket.")
        print("\n")
    elif player_response == "3":
        Helpers.stylized_print("")
        Player.flags["mirrorShardDescription"] = "hardLife"
        Helpers.stylized_print("With a heaviness of heart,")
        Helpers.stylized_print("you put the mirror shard in your pocket.")
        print("\n")
    Player.player_location = "alley"
