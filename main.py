from character import *
from classes import *
import random

worlds = ["Sci-fi", "Fantasy", "Modern world"]


def enemy(world):
    if world == "Sci-fi":
        return [
            Character("Darth Vader", "Human", 1000, (10, 20), 10, 50),
            Character("B1-Series Battle Droid", "Droid", 200, (5, 10), 5, 15),
            Character("IG-88 Assassin Droid", "Droid", 350, (7, 12), 6, 25),
            Character("Sith Inquisitor", "Dark Side Force User", 600, (10, 18), 8, 40),
            Character("Clone Trooper", "Human Clone", 300, (6, 10), 7, 20)
        ]
    
    elif world == "Fantasy":
        return [
            Character("Fire Dragon", "Dragon", 800, (15, 25), 12, 60),
            Character("Elf Warrior", "Elf", 300, (8, 15), 7, 30),
            Character("Necromancer", "Undead", 400, (7, 14), 6, 35),
            Character("Goblin King", "Goblin", 350, (5, 10), 5, 25),
            Character("Dark Sorcerer", "Human", 500, (10, 17), 8, 40)
        ]

    else:
        return [
            Character("Elite Soldier", "Human", 250, (6, 12), 7, 25),
            Character("Sniper", "Human", 150, (10, 20), 3, 20),
            Character("Terrorist Leader", "Human", 300, (7, 14), 6, 30),
            Character("Juggernaut", "Armored Human", 500, (5, 10), 12, 40),
            Character("Street Fighter", "Brawler", 180, (6, 12), 5, 20)
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
        role = input(f"Which role do you want in {world}: {list(roles.keys())}")
        if role in roles:
            return roles[role]
        else:
            print("Invalid role. Please select from list.")


def player_turn(player, enemy):
    print("\nChoose your action:")
    print("1 - Attack")
    print("2 - Special Attack")
    print("3 - Heal")
    print("4 - Parry")
    print("5 - Dodge")

    choice = input("Your choice: ")
    if choice == "1":
        player.attack(enemy)
    elif choice == "2":
        player.special_attack(enemy)
    elif choice == "3":
        player.heal()
    elif choice == "4":
        player.parry()
    elif choice == "5":
        if player.dodge():
            return True  
    else:
        print("Invalid choice.")
    return False

def enemy_turn(enemy, player):
    print(f"\n{enemy.name}'s turn:")
    enemy.attack(player)
    player.take_damage(enemy)



while True:
    world1 = input(f"In which world would you want to figth {worlds}?")
    if world1 not in worlds:
        print("This world in not in choices.")
        continue


    name = input("Write name for your character: ")
    race = input("Write a race for your character: ")
    RoleClass = select_role(world1)
    player = 
    break

while True:
    enemies = enemy(world1)
    while enemies:
        enemy_to_fight = random.choice(enemies)
        enemy_to_fight =  Character(enemy_to_fight.name, enemy_to_fight.rasa, enemy_to_fight.health,
                          enemy_to_fight.attack_range, enemy_to_fight.defence0, enemy_to_fight.damage)
        print(f"Your opponent is: {enemy_to_fight.name} ({enemy_to_fight.rasa}), Health: {enemy_to_fight.health}")
        print(f"Battle beggings!\n Your opponent is: {enemy_to_fight.name} ({enemy_to_fight.rasa}), Health: {enemy_to_fight.health}")

        while player.health > 0 and enemy.health > 0:
            dodged = player_turn(player, enemy)
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated!")
                enemies.remove(enemy_to_fight)
                break

            if not dodged:
                enemy_turn(enemy, player)

            if player.health <= 0:
                print(f"{player.name} has fallen in battle...")
        if player.health <= 0:
            print("Game over.")
            break
    if player.health <= 0 or not enemies:
        print("You defeated all your enemies. You win.\n Thanks for playing my game.")
        break