import Player
import Weapons


userInventory = Player.inventory
userInventory["weapons"] = Weapons.weaponList
print(userInventory["weapons"][1][0])
print(Weapons.attack(userInventory["weapons"][1][1], userInventory["weapons"][1][2]))




#user1 = Player.playerStats
#user1["name"] = "Danica"

#user2 = Player.playerStats
#user2["name"] = "Sakan"

#print(user1["name"])
#print(user2["name"])