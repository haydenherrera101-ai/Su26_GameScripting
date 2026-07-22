import time
import Player
import Helpers


displaying_menu = True


# handles both the one-time shadow question and every visit after
def menu():
    global displaying_menu
    Player.player_location = "tunnel"

    if Player.flags["playerShadow"] == None:
        Helpers.stylized_print("A single lantern swings high above you,")
        Helpers.stylized_print("casting shifting shadows across the tunnel walls as you walk.")
        print("\n")

        Helpers.stylized_print("What do you see in the shadows?")
        Helpers.stylized_print("\t1. Wild animals, running fast and free across the walls.")
        Helpers.stylized_print("\t2. Horrible monsters, stalking and chasing you in the darkness.")
        Helpers.stylized_print("\t3. Calm waters, lapping at your feet and relaxing you.")
        Helpers.stylized_print("\t4. Nothing, they're just shadows.")
        player_choice = input("> ").strip()

        if player_choice == "1":
            Helpers.stylized_print("As the shadow animals dash around you,")
            Helpers.stylized_print("you imagine what it's like to feel that free.")

            Helpers.stylized_print("You are filled with a sense of wonder.")
            Player.flags["playerShadow"] = "animals"
            print("\n")
            return menu()

        elif player_choice == "2":
            Helpers.stylized_print("Monsters lurk around every corner, just out of sight...")
            Helpers.stylized_print("...and you know they're watching you.")

            Helpers.stylized_print("You are filled with a sense of anxiety.")
            Player.flags["playerShadow"] = "monsters"
            print("\n")
            return menu()

        elif player_choice == "3":
            Helpers.stylized_print("The calm waters flow gently in and out, ")
            Helpers.stylized_print("and you imagine yourself far off on a beach somewhere.")

            Helpers.stylized_print("You are filled with a sense of peace.")
            Player.flags["playerShadow"] = "waters"
            print("\n")
            return menu()

        elif player_choice == "4":
            Helpers.stylized_print("You continue along the shadowy tunnel,")
            Helpers.stylized_print("Noticing nothing in particular except that it's dark.")

            Helpers.stylized_print("You are filled with a sense of")
            time.sleep(1)
            Helpers.stylized_print("....not a whole lot, really.")
            print("\n")
            Player.flags["playerShadow"] = "nothing"
            return menu()

        else:
            print("Please choose a valid option.")
            return

    displaying_menu = True

    while Player.player_location == "tunnel" and displaying_menu:

        Helpers.stylized_print("What do you do next?")
        Helpers.stylized_print("\t1. Examine your surroundings")
        Helpers.stylized_print("\t2. Continue right")
        Helpers.stylized_print("\t3. Turn back to the cave")
        player_choice = input("> ").strip()

        if player_choice == "1":
            Helpers.stylized_print("The shadows continue to move around you. ")
            Helpers.stylized_print("The air is cool and still, and you can hear the faint sound of dripping water echoing through the tunnel.")
            Helpers.stylized_print("To the right, the tunnel seems to open up and dim light filters in.")
            Helpers.stylized_print("To the left, the cave with the door.")
            print("\n")

        elif player_choice == "2":
            Helpers.stylized_print("You continue right, towards the exit of the tunnel.")
            Player.player_location = "alley"
            displaying_menu = False
            return "alley"

        elif player_choice == "3":
            Helpers.stylized_print("You turn back to the cave.")
            print("\n")
            Player.player_location = "cave"
            displaying_menu = False
            return "cave"

        else:
            print("Please choose a valid option.")