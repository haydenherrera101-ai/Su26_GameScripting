# Philosphy themed text based game v1

# Player is presented a series of scenarios / questions
# Their answers impact the ending 
# and are designed to make the player build the identity of their character
# Basically an interactive story, VERY text heavy
# This is a shortened demo version so it feels pretty..incomplete

# To work on:
#   - making the end of the game less of an info dump and more interactive
#   - ideally there would be still images for each area and function more like a point and click 
#   - I have lots of other areas and NPC's written, just need to be implemented




import Cave
import Tunnel
import Player
import Alley
import Trolley
import BossRoom

def main():
    Cave.start_description()

    while True:
        if Player.player_location == "cave":
            Cave.menu()
        elif Player.player_location == "tunnel":
            Tunnel.menu()
        elif Player.player_location == "alley":
            Alley.menu()
        elif Player.player_location == "trolley":
            Trolley.menu()
        elif Player.player_location == "BossRoom":
            BossRoom.menu()


if __name__ == "__main__":
    main()
