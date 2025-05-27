from character import *
from classes import *
import random

worlds = ["Sci-fi", "Fantasy", "Modern world"]

def enemy(world):
    if world == "Sci-fi":
        return [
            Character("Darth Vader", "Human", 1000),
            Character("B1-Series Battle Droid", "Droid", 200),
            Character("IG-88 Assassin Droid", "Droid", 350),
            Character("Sith Inquisitor", "Dark Side Force User", 600),
            Character("Clone Trooper", "Human Clone", 300)
        ]
    
    elif world == "Fantasy":
        return [
            Character("Fire Dragon", "Dragon", 800),
            Character("Elf Warrior", "Elf", 300),
            Character("Necromancer", "Undead", 400),
            Character("Goblin King", "Goblin", 350),
            Character("Dark Sorcerer", "Human", 500)
        ]

    else:
        return [
            Character("Elite Soldier", "Human", 250),
            Character("Sniper", "Human", 150),
            Character("Terrorist Leader", "Human", 300),
            Character("Juggernaut", "Armored Human", 500),
            Character("Street Fighter", "Brawler", 180)
        ]

def select_role(world):
    if world == "Sci-fi":
        roles = {
            "Power": Scifi.Power,
            "Mandalorian": Scifi.Mandalorian,
            "Trooper": Scifi.Trooper
        }
    elif world == "Fantasy":
        roles = {
            "Mage": Fantasy.Mage,
            "Warrior": Fantasy.Warrior,
            "Archer": Fantasy.Archer
        }
    else:
        roles = {
            "Soldier": ModernWorld.Soldier
        }
    
    while True:
        role = input(f"Vyberte si roli ve světě {world}: {list(roles.keys())}")
        if role in roles:
            return roles[role]
        else:
            print("Invalid role. Please select from list.")
    

while True:
    world1 = input(f"V jakém světě chcete bojovat {worlds}?")
    if world1 not in worlds:
        print("Tento svět není v nabídce.")
        continue

    if world1 == "Sci-fi":
        zivoty = 500
    elif world1 == "Fantasy":
        zivoty = 250
    else:
        zivoty = 100

    name = input("Napište mi jméno postavy: ")
    race = input("Napište svou rasu: ")
    RoleClass = select_role(world1)


    enemies = enemy(world1)
    enemy_to_fight = random.choice(enemies)
    print(f"Your opponent is: {enemy_to_fight.name} ({enemy_to_fight.rasa}), Health: {enemy_to_fight.health}")

    break

print(f"Battle beggings!\n Your opponent is: {enemy_to_fight.name} ({enemy_to_fight.rasa}), Health: {enemy_to_fight.health}")

while True:
    