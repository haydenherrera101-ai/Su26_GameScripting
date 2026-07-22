import time
import Player
import Helpers


examined_room = False
displaying_menu = True

# Only displays once, upon starting up the game
def start_description():
    Helpers.stylized_print("You find yourself standing before a large, imposing door.")
    Helpers.stylized_print("How did you get here?")
    Helpers.stylized_print("How long have you been standing here?")
    time.sleep(.5)
    Helpers.stylized_print("Actually...")
    time.sleep(.5)
    Helpers.stylized_print("Who are you?")
    print("\n")
    Helpers.stylized_print("Enter your name: ")
    player_name = input("> ").strip()
    Player.flags["playerNames"].append(player_name)
    print("\n")
    Helpers.stylized_print(f"{player_name}, {player_name}...")
    Helpers.stylized_print("maybe that's right.")
    time.sleep(.5)
    Helpers.stylized_print("You desperately try to remember anything about yourself, but are coming up blank.")
    print("\n")


def describe_room():
    Helpers.stylized_print("You're in a cave, the humid underground air clinging to your skin.")
    Helpers.stylized_print("You hear the faint sound of wind whistling through the cavern.")
    Helpers.stylized_print("A hole in the cave ceiling above you lets in a shaft of light.")
    Helpers.stylized_print("It's daytime outside, wherever you are.")
    Helpers.stylized_print("You notice the cave branches off to the right, to a tunnel.")
    print("\n")
    Helpers.stylized_print("In front of you, built into the cave wall, a large imposing door.")
    Helpers.stylized_print("You get the feeling that it's been there for centuries.")
    Helpers.stylized_print("The wooden surface is intricately carved with symbols you've never seen before.")
    Helpers.stylized_print("Moss decorates the edges of the frame. Something about this door unsettles you.")

# handles both the first visit (room not yet examined) and every visit after
def menu():
    global examined_room, displaying_menu
    displaying_menu = True

    while Player.player_location == "cave" and displaying_menu:
        Helpers.stylized_print("What do you do next?")
        if not examined_room:
            Helpers.stylized_print("\t1. Try to remember")
            Helpers.stylized_print("\t2. Examine your surroundings")
            player_choice = input("> ").strip()

            if player_choice == "1":
                remember()
            elif player_choice == "2":
                describe_room()
                print("\n")
                examined_room = True
            else:
                print("Please choose a valid option.")
        else:
            Helpers.stylized_print("\t1. Open the door")
            Helpers.stylized_print("\t2. Enter the tunnel to the right")
            Helpers.stylized_print("\t3. Examine your surroundings")
            Helpers.stylized_print("\t4. Try to remember")
            player_choice = input("> ").strip()

            if player_choice == "1":
                if "ornamental key" in Player.player_inventory:
                    Helpers.stylized_print("Armed with the key, the door doesn't seem so menacing anymore.")
                    Helpers.stylized_print("You put the key in the lock, push open the heavy door, ")
                    Helpers.stylized_print("and step through the doorway.")

                    Player.player_location = "BossRoom"
                    displaying_menu = False

                else:
                    if Player.flags["puked"]:
                        Helpers.stylized_print("You sidestep your puke puddle and approach the door.")
                    else:
                        Helpers.stylized_print("You approach the door.")

                    Helpers.stylized_print("It seems to grow in size, towering over you.")
                    Helpers.stylized_print("You search for a door handle and realize there is none.")
                    Helpers.stylized_print("You try to push the door open but it doesn't budge.")
                    Helpers.stylized_print("The door seems to taunt you. Smugly.")
                    Helpers.stylized_print("Only a small keyhole. You'll have to come back with a key.")
                    print("\n")

            elif player_choice == "2":
                Helpers.stylized_print("You head to the right, down a dimly lit tunnel.")
                print("\n")
                Player.player_location = "tunnel"
                displaying_menu = False

            elif player_choice == "3":
                describe_room()
                print("\n")

            elif player_choice == "4":
                remember()
                print("\n")

            else:
                print("Please choose a valid option.")

# function to try remembering, if you get to puke condition this does effect the outcome of the game
def remember():
    if Player.flags["rememberedCount"] == 0:
        Helpers.stylized_print("You close your eyes and direct your attention toward the middle of your head.")
        Helpers.stylized_print("Who are you? Where are you? How did you get here?")
        Helpers.stylized_print("The questions swirl through your mind and after a moment of intense contemplation,")
        Helpers.stylized_print("you have gleaned nothing except a headache.")
        Helpers.stylized_print("Good job.")
        print("\n")
        Player.flags["rememberedCount"] += 1
        return

    if Player.flags["rememberedCount"] == 1:
        Helpers.stylized_print("This time you take a different approach.")
        Helpers.stylized_print("Maybe if you just act casual you can catch your memories of guard.")
        Helpers.stylized_print("Yes, be chill.")
        print("\n")
        Helpers.stylized_print("\"I dont even care if I remember anything,\" You think to yourself.")
        Helpers.stylized_print("You twiddle your thumbs in front of you. \"Yep, all good over here,\"")
        time.sleep(2)
        print("\n")
        Helpers.stylized_print("...Now! Suddenly you focus all of your willpower on the void between your ears,")
        Helpers.stylized_print("begging to find anything.")
        Helpers.stylized_print("Nothing. Your devious plan did not appear to work.")
        Helpers.stylized_print("You exhale deeply, a bit winded.")
        print("\n")
        Player.flags["rememberedCount"] += 1
        return

    if Player.flags["rememberedCount"] == 2:
        Helpers.stylized_print("You're really testing it now, buddy.")
        Helpers.stylized_print("Clenching your fists, you focus inward yet again")
        Helpers.stylized_print("You beg yourself to recall a single shred of information.")
        Helpers.stylized_print("A feeling then, like you're about to sneeze.")
        Helpers.stylized_print("Are you doing it? Is this remembering?")
        Helpers.stylized_print("You brace yourself for the wave of memories to flood in..")
        time.sleep(2)
        print("\n")
        Helpers.stylized_print("...and promptly throw up all over the ground.")
        Helpers.stylized_print("Maybe that's enough remembering for now.")
        print("\n")
        Player.flags["rememberedCount"] += 1
        Player.flags["puked"] = True
        return

    if Player.flags["rememberedCount"] >= 3:
        Helpers.stylized_print("Seriously? You smell like puke.")
        Helpers.stylized_print("Quit it.")
        print("\n")
        return
