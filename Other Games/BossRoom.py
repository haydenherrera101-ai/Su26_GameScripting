import sys
import Player
import Helpers

# only displays once, upon entering the boss room
def room_description():
    Helpers.stylized_print("")
    Helpers.stylized_print("You're standing on soft carpet, in a dimly lit office.")
    Helpers.stylized_print("In front of you, an impressively large desk with a man sitting at it.")

# the boss's opening chunk of dialogue
def boss_dialogue():
    Helpers.stylized_print("")
    Helpers.stylized_print("You finally arrived! ")
    Helpers.stylized_print("The man smiles at you from across the room.")
    Helpers.stylized_print("Come, come!")
    Helpers.stylized_print("he gestures at the chair across from him.")
    print("\n")
    Helpers.stylized_print("you approach the man and sit down.")
    print("\n")
    Helpers.stylized_print("Now, I know what you're going to ask me.")
    Helpers.stylized_print("\"Laplace, where am I? Who am I? Why can't I remember anything?")
    Helpers.stylized_print("What am I doing in an office in a cave?\"")
    Helpers.stylized_print("He chuckles.")
    print("\n")
    Helpers.stylized_print("You feel anticipation well in your chest.")
    Helpers.stylized_print("Maybe your questions will finally be answered?")
    print("\n")
    Helpers.stylized_print("Well I'm afraid I dont have any answers for you, my friend. ")
    Helpers.stylized_print("Your stomach drops.")
    print("\n")
    Helpers.stylized_print("The man's eyes glint with mischief.")
    Helpers.stylized_print("But you already have more answers than you think.")
    print("\n")
    Helpers.stylized_print("He clears his throat as if for emphasis, and pulls out from his desk a stack of papers.")



def menu():
    Player.player_location = "BossRoom"

    player_name = Player.flags["playerNames"][0] if Player.flags["playerNames"] else "friend"

    room_description()
    boss_dialogue()

    if Player.flags["playerShadow"] == "animals":
        Helpers.stylized_print("")
        Helpers.stylized_print("In the tunnel shadows you saw animals, running wild across the walls.")
        Helpers.stylized_print("Sounds like you value your freedom and wish to roam as you please.")
        Helpers.stylized_print("A wanderer of sorts, perhaps?")

    elif Player.flags["playerShadow"] == "monsters":
        Helpers.stylized_print("")
        Helpers.stylized_print("In the tunnel shadows you saw monsters skulking about. ")
        Helpers.stylized_print("Sounds like you have some real anxieties running around in that head, yes?")
        Helpers.stylized_print("But hey - a mind that imagines monsters is a mind that's still paying attention.")
        Helpers.stylized_print("Nothing wrong with a little worry, so long as you don't let it wear ya down.")

    elif Player.flags["playerShadow"] == "waters":
        Helpers.stylized_print("")
        Helpers.stylized_print("In the tunnel shadows you saw waters flowing in and out.")
        Helpers.stylized_print("Sounds like you're calm at heart.")
        Helpers.stylized_print("You crave peace and quiet.")

    elif Player.flags["playerShadow"] == "nothing":
        Helpers.stylized_print("")
        Helpers.stylized_print("In the tunnel shadows you saw nothing but...well, shadows.")
        Helpers.stylized_print("Practical and grounded, you don't think too much in metaphors, do you?")
        Helpers.stylized_print("I can appreciate a no nonsense type!")
        Helpers.stylized_print("The man laughs heartily.")

    else:
        Helpers.stylized_print("")

    if Player.flags["playerIdentityOpinion"] == "Better to know less":
        Helpers.stylized_print("")
        Helpers.stylized_print("I'm reading something here about .... M Y S T E R Y?")
        Helpers.stylized_print("Seems like you prefer your life to contain lots of unknowns!")
        Helpers.stylized_print("Keeps ya on your toes, huh?")
        Helpers.stylized_print("He laughs. ")

    elif Player.flags["playerIdentityOpinion"] == "Better to know more":
        Helpers.stylized_print("")
        Helpers.stylized_print("Seems here like you prefer to examine the world around you,")
        Helpers.stylized_print("and reflect on your inner world. ")
        Helpers.stylized_print("We've got a bit of a deep thinker on our hands, do we?")

    else:
        Helpers.stylized_print("")

    if Player.flags["pulledLever"]:
        Helpers.stylized_print("")
        Helpers.stylized_print("Ah yes, and it seems as though as we're willing to make tough decisions!")
        Helpers.stylized_print(f"Pulling that lever must've not been easy, {player_name}!")
        Helpers.stylized_print("But that courage and will to do the right thing is strong in you!")

    else:
        Helpers.stylized_print("")
        Helpers.stylized_print("Ah yes, I see here that you did not pull the lever for the trolley man.")
        Helpers.stylized_print("Bit of an anxious wreck, isn't he? ")
        Helpers.stylized_print("He chuckles.")
        Helpers.stylized_print(f"I understand your hesitancy, {player_name}.")
        Helpers.stylized_print("Sometimes it's not the right choice to intervene")
        Helpers.stylized_print("with the wheels of fate.")

    if Player.flags["puked"]:
        Helpers.stylized_print("")
        Helpers.stylized_print("The man suddenly bursts out laughing, startling you.")
        Helpers.stylized_print("Wow, you sure are stubborn, aren't ya?")
        Helpers.stylized_print("Tried to remember so hard you puked!")
        Helpers.stylized_print("I appreciate the dedication, my friend. ")
        Helpers.stylized_print("The man stifles his laughter and pulls himself together.")

    if Player.flags["mirrorShardDescription"] == "didntLook":
        Helpers.stylized_print("")
        Helpers.stylized_print("When given the chance to look into that mirror and see yourself, ")
        Helpers.stylized_print("you didn't take it. ")
        Helpers.stylized_print("Fascinating. ")
        Helpers.stylized_print(f"Ya running from something, {player_name}? ")
        Helpers.stylized_print("or just not interested in that sort of thing?")
        Helpers.stylized_print("Either way, I say good on ya. Not everything needs starin' at right away.")
        Helpers.stylized_print("Some things are better met on your own time.")

    elif Player.flags["mirrorShardDescription"] == "goodLife":
        Helpers.stylized_print("")
        Helpers.stylized_print("When you looked in that mirror, you saw the face of someone who's had many happy years")
        Helpers.stylized_print("Quick to smile, and easy to make laugh.")
        Helpers.stylized_print("Kind of like me!")
        Helpers.stylized_print("The man laughs yet again.")

    elif Player.flags["mirrorShardDescription"] == "hardLife":
        Helpers.stylized_print("")
        Helpers.stylized_print("When you looked in that mirror, you saw the face of someone who's had some hardships.")
        Helpers.stylized_print("And yet here you stand. ")
        Helpers.stylized_print("If that's not resilience, I dont know what is! ")

    else:
        Helpers.stylized_print("")

    conclusion(player_name)


# the final choice, after the boss has recapped everything to the player
def conclusion(player_name):
    print("\n")
    Helpers.stylized_print(f"well, what do you think, {player_name}?")
    Helpers.stylized_print("\t1. This description feels accurate.")
    Helpers.stylized_print("\t2. This description feels inaccurate.")
    player_response = input("> ").strip()

    if player_response == "1":
        Helpers.stylized_print("See, I'm always right!")
        Helpers.stylized_print("The man sits back in his chair, pleased with himself.")
        Helpers.stylized_print("He chuckles. Just kidding.")
        print("\n")
        Helpers.stylized_print("In the end, it was you who had the answers you were seeking.")
        print("\n")
        Helpers.stylized_print("A warmth settles in your chest, something steady and familiar.")
        Helpers.stylized_print("The man rises and ambles over to open the door for you, still smiling warmly.")
        Helpers.stylized_print("Go on now. You know where you're headed.")
        Helpers.stylized_print("You step out of the office, and the door clicks shut softly behind you.")
        print("\n")
        Helpers.stylized_print("THANK YOU FOR PLAYING!")
        
    elif player_response == "2":
        Helpers.stylized_print("Now you might be suprised but I'm actually glad to hear that!")
        Helpers.stylized_print("The man sits back in his chair, pleased with himself.")
        Helpers.stylized_print("In finding out what doesn't feel like you,")
        Helpers.stylized_print("I hope you've found out more about what DOES")
        print("\n")
        Helpers.stylized_print("In the end, it was you who had the answers you were seeking.")
        print("\n")
        Helpers.stylized_print("You feel lighter somehow, like you've set down something you didn't know you were carrying.")
        Helpers.stylized_print("The man rises and ambles over to open the door for you, still smiling warmly.")
        Helpers.stylized_print("Go on now. You know where you're headed.")
        Helpers.stylized_print("You step out of the office, and the door clicks shut softly behind you.")
        print("\n")
        Helpers.stylized_print("THANK YOU FOR PLAYING!")


    else:
        print("Please choose a valid option.")
        return conclusion(player_name)

    sys.exit()