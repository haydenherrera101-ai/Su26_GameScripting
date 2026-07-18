# Author: Hayden Herrera
# Date: 2026-09-07
# Description: This program would give out an attack and the stats of the weapons used.


import random
#Name, min damage, max damage
weaponList = {1: ["Chain Sword", 25, 75], 2: ["Bolter Gun", 10, 55]}
randColor = ["Alabaster", "Vermillion", "Scarlet", "Opalescent", "Cetrine"]

def critAttack(randAttack, minAttack, maxAttack):
    if maxAttack - randAttack < 6:
        return True
    else:
        return False

def attack (minAttack, maxAttack):
    randAttack = random.randint(minAttack, maxAttack)
    if critAttack(randAttack, minAttack, maxAttack):
        print("Crit Attack!")
        return IsCrit(randAttack, 2)
    return randAttack

def IsCrit(randAttack, mod):
    return randAttack * mod