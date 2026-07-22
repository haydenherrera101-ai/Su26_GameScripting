import Helpers
import time
import Player

displaying_menu = True
examined_room = False
first_dialogue_loop = True
saw_start_description = False


# Only displays the first time the player enters
def start_description():
    global saw_start_description
    
    print("\n")
    Helpers.stylized_print("Now at the mouth of the tunnel, you step outside")
    Helpers.stylized_print("into a cobblestone alleyway.")	
    Helpers.stylized_print("That's...")
    time.sleep(.5)
    Helpers.stylized_print("...an odd place to put an alleyway.")
    Helpers.stylized_print("The sun is nearly set now, and distant stars shine faintly in the purple sky.")
    Helpers.stylized_print("Were you really in the cave that long?")
    
    saw_start_description = True
    print("\n")

# after the player has already seen the start description and examines the room
def room_description():
    Helpers.stylized_print("Surrounding the alleyway, a contiguous wall of brick buildings.")
    Helpers.stylized_print("They all seem to be businesses that have been long shuttered.")
    Helpers.stylized_print("To the right, the alley leads to a flight of stairs going down.")
    Helpers.stylized_print("In the distance beyond the stairs you can see a huge body of water. An ocean?")
    Helpers.stylized_print("The lights of a small harbor twinkle gently.")
    print("\n")
    Helpers.stylized_print("In front of you, a man leans against a wall.")
    Helpers.stylized_print("He is eyeing you suspiciously while smoking a cigarette.")
    Helpers.stylized_print("Beside him sits a large cardboard box.")
    print("\n")
    
# brief description for when the player comes back to the room
def return_description():
    Helpers.stylized_print("You're standing in the alley.")
    print("\n")
        
# handles both the first visit (room not yet examined) and every visit after
def menu(show_return_description=True):
    global displaying_menu
    global examined_room

    Player.player_location = "alley"

    if not saw_start_description:
        start_description()
    elif show_return_description:
        return_description()

    Helpers.stylized_print("What do you do next?")
    if not examined_room:
        Helpers.stylized_print("\t1. Examine your surroundings")
        Helpers.stylized_print("\t2. Continue down the alleyway")
        Helpers.stylized_print("\t3. Turn back to the tunnel")
    else:
        Helpers.stylized_print("\t1. Approach the man")
        Helpers.stylized_print("\t2. Examine your surroundings")
        Helpers.stylized_print("\t3. Continue down the alleyway")
        Helpers.stylized_print("\t4. Turn back to the tunnel")
    player_choice = input("> ").strip()

    if not examined_room:
        if player_choice == "1":
            room_description()
            examined_room = True
            return menu(show_return_description=False)

        elif player_choice == "2":
            Helpers.stylized_print("You continue to the right, and down the stairs")
            Player.player_location = "trolley"
            displaying_menu = False

        elif player_choice == "3":
            Helpers.stylized_print("You turn back to the tunnel.")
            print("\n")
            Player.player_location = "tunnel"
            displaying_menu = False

        else:
            print("Please choose a valid option.")
    else:
        if player_choice == "1":
            if not Player.flags["metCatMan"]:
                intro_dialogue_menu()
            elif "ornamental key" in Player.player_inventory:
                Helpers.stylized_print("The man regards you with a quiet calm.")
                Helpers.stylized_print("I guess you'll be headin' to that door then?")
                return menu()
            elif "essence of hope" in Player.player_inventory:
                Helpers.stylized_print("The man appears to have calmed down from his apparent existential crisis")
                Helpers.stylized_print(f"Hey again, {player_name}. ")
                Helpers.stylized_print("I've been doin' some thinking. ")
                Helpers.stylized_print("and I dont know if all that M Y S T E R Y -")
                Helpers.stylized_print("he waggles his fingers weakly -")
                Helpers.stylized_print("was really doin' me any good.")
                Helpers.stylized_print("I don't know about you...")
                Helpers.stylized_print("But I think I'm ready to confront who I really am.")
                Helpers.stylized_print("No more hidin'.")
                print("\n")
                Helpers.stylized_print("I've got somethin' for ya.")
                print("\n")
                Helpers.stylized_print("you aquire the ESSENCE OF COURAGE!")
                Helpers.stylized_print("this small orb shines with an iridescent light.")
                print("\n")
                Helpers.stylized_print("Your two essences begin shining brighter and brighter")
                Helpers.stylized_print("until they're so bright you have to shut your eyes.")
                print("\n")
                Helpers.stylized_print("you aquire the ORNAMENTAL KEY!")
                Helpers.stylized_print("it's small but feels way heavier than it should")
                Helpers.stylized_print("and has the same markings that cover the cave door.")

                # didnt add the courage essence cause it doesn't really effect anything once you get key
                Player.player_inventory.remove("essence of hope")
                Player.player_inventory.append("ornamental key")
                return menu()
            elif "cat box" in Player.player_inventory:
                Helpers.stylized_print("The man does not appear to notice you approaching.")
                Helpers.stylized_print("He is lost in thought.")
            else:
                dialouge_menu()

        elif player_choice == "2":
            room_description()
            return menu(show_return_description=False)

        elif player_choice == "3":
            Helpers.stylized_print("You continue to the right, and down the stairs")
            Player.player_location = "trolley"
            displaying_menu = False

        elif player_choice == "4":
            Helpers.stylized_print("You turn back to the tunnel.")
            print("\n")
            Player.player_location = "tunnel"
            displaying_menu = False

        else:
            print("Please choose a valid option.")


# if this is the first time meeting this man
def intro_dialogue_menu():
    intro_looping = True
    Player.flags["metCatMan"] = True
    global player_name
    
    Helpers.stylized_print("You walk towards the man and he takes another drag off his cigarette.")
    Helpers.stylized_print("Haven't seen you before, what's your name?")
    print("\n")
    player_name = input("> ").strip()
    Player.flags["playerNames"].append(player_name)
    
    Helpers.stylized_print(f"Well, {player_name}, what brings you here? Not often we have visitors.")
    
    while intro_looping:
        print("\n")
        Helpers.stylized_print("\t1. Where's here?")
        Helpers.stylized_print("\t2. Trying to figure that out myself")
        Helpers.stylized_print("\t3. What brings YOU here?")
        Helpers.stylized_print("\t4. Let's talk about something else (move on)")
        print("\n")
        player_response = input("> ").strip()
            
        # Where's here?
        if player_response == "1":
            Helpers.stylized_print("Dunno.")
            Helpers.stylized_print("An in between place, of sorts.")
            Helpers.stylized_print("I try not to think too hard about it.")
            
        # Trying to figure that out myself
        elif player_response == "2":
            Helpers.stylized_print("The man chuckles.")
            Helpers.stylized_print("Not me. I like the not knowin'")
            Helpers.stylized_print("")
            
        # What brings YOU here?
        elif player_response == "3":
            Helpers.stylized_print("The man shrugs.")
            Helpers.stylized_print("Who knows. Little of this, little of that.")
            Helpers.stylized_print("He takes another drag off his cigarette.")
        
        # Leave intro dialouge menu
        elif player_response == "4":
            Helpers.stylized_print("Fair enough")
            intro_looping = False
            print("\n")
            return dialouge_menu()

        else:
            print("Please choose a valid option.")

# Greeting agter        
def greeting():
        Helpers.stylized_print("The man looks at you lazily.")
        Helpers.stylized_print(f"What's on your mind, {player_name}?")
        Helpers.stylized_print("The box beside him rustles slightly.")
        print("\n")
        
def dialouge_menu():
    dialouge_looping = True

    greeting()
    
    while dialouge_looping:
    
        Helpers.stylized_print("\t1. How do I get out of here?")
        Helpers.stylized_print("\t2. Whats's in that box?")
        Helpers.stylized_print("\t3. Nevermind. (leave)")
        if "mirror shard" in Player.player_inventory:
            Helpers.stylized_print("\t4. Show him the mirror shard")

        player_response = input("> ").strip()

        if player_response == "1":
            Helpers.stylized_print("Maybe down those stairs? I dont know.")
            Helpers.stylized_print("Never really leave this spot.")
            Helpers.stylized_print("Don't care much to see anything else.")
            print("\n")
            Helpers.stylized_print("He seems to be attempting to project an air of nonchalance but it feels forced.")
            Helpers.stylized_print("The man clears his throat.")
            print("\n")

        elif player_response == "2":
            cat_dialogue()


        elif player_response == "3":
            Helpers.stylized_print("See ya later!")
            Helpers.stylized_print("\n")
            dialouge_looping = False
            return menu()

        elif player_response == "4" and "mirror shard" in Player.player_inventory:
            show_mirror_shard()
            dialouge_looping = False
            return menu()

        else:
            print("Please choose a valid option.")


# seperated out from main dialogue branch because its long
def cat_dialogue():
    Helpers.stylized_print("Oh that old thing?")
    Helpers.stylized_print("A cat.")
    Helpers.stylized_print("Um.")
    Helpers.stylized_print("Or maybe not. Or maybe both.")
    Helpers.stylized_print("He grins. That's the fun of it.")
    Helpers.stylized_print("M Y S T E R Y")
    Helpers.stylized_print("He waves his hands around for emphasis.")
    Helpers.stylized_print("\n")
    Helpers.stylized_print("...")
    time.sleep(.5)
    Helpers.stylized_print("An awkward silence fills the air.")
    Helpers.stylized_print("\n")
    Helpers.stylized_print("Well ya see, if I dont look at it,")
    Helpers.stylized_print("the cat is kinda there and not there at the same time.")
    Helpers.stylized_print("Finding out would ruin the mystery.")
    Helpers.stylized_print("His carefree facade slips a bit, and a slight desperation tinges his words.")
    Helpers.stylized_print("If you simply dont look at somethin, it can be whatever you want it to be!")
    Helpers.stylized_print("\n")
    
    if first_dialogue_loop == True:
        cat_choice()

def cat_choice():
    global first_dialogue_loop
    Helpers.stylized_print("What do you think?")
    Helpers.stylized_print("\t1. You agree with him. The less you know the better! M Y S T E R Y and all that.")
    Helpers.stylized_print("\t2. You disgree with him. Why avoid reality? Better to face it head on.")
    player_response = input("> ").strip()

    if player_response == "1":
        Helpers.stylized_print("Yeah! Maybe you don't even WANT to remember who you are. It's better not knowing.")
        Helpers.stylized_print("Finding that out would require the dreaded.... self reflection!")
        Player.flags["playerIdentityOpinion"] = "Better to know less"
    elif player_response == "2":
        Helpers.stylized_print("Yeah...no. Hiding yourself from the truth isnt mystery, its delusion.")
        Helpers.stylized_print("You imagine there's an awful lot this guy chooses not to look at.")
        Player.flags["playerIdentityOpinion"] = "Better to know more"

    else:
        print("Please choose a valid option.")
        return cat_choice()

    print("\n")

    # makes sure future loops dont ask this question again
    first_dialogue_loop = False


# shows the cat man the mirror shard, once the player has picked it up
def show_mirror_shard():
    Helpers.stylized_print("")
    Helpers.stylized_print("The man looks quizzically at the mirror shard as you hand it to him.")
    Helpers.stylized_print("What's this? ")
    Helpers.stylized_print("He turns it over in his hand and the relfective surface flashes in the starlight. ")
    Helpers.stylized_print("Suddenly horrified, he drops the mirror shard, ")
    Helpers.stylized_print("shattering it into small pieces on the cobblestone.")
    print("\n")
    Helpers.stylized_print("A- a ...mirror?")
    Helpers.stylized_print("He is shaking now and speaking more to himself than you.")
    Helpers.stylized_print("Is that really what I look like? ")
    Helpers.stylized_print("All these years spent looking away, imagining myself to be someone else. ")
    Helpers.stylized_print("Imagining that I'd changed...")
    Helpers.stylized_print("And yet there I am. ")
    print("\n")
    Helpers.stylized_print("You both stand in silence for what feels like an uncomfortably long amount of time.")
    print("\n")
    Helpers.stylized_print("Here, kid. Take it.")
    Helpers.stylized_print("He sounds defeated as he gestures towards the box with a cat(?) in it.")
    print("\n")
    Helpers.stylized_print("Hesitantly, you aquire the CAT(?) BOX!")
    
    Player.player_inventory.append("cat box")
    Player.player_inventory.remove("mirror shard")

