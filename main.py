from character import *
from classes import *
import random
import time

worlds = ["Sci-fi", "Fantasy", "Modern world"]

def get_enemies(world):
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
        role = input(f"Which role do you want in {world}: {list(roles.keys())} ")
        if role in roles:
            return roles[role]
        else:
            print("Invalid role. Please select from list.")

def player_turn(player, enemy):
    print(f"\n{player.name} - Choose your action:")
    print("1 - Attack")
    print("2 - Special Attack")
    print("3 - Heal")

    choice = input("Your choice: ")
    if choice == "1":
        player.attack(enemy)
        time.sleep(1)
    elif choice == "2":
        if hasattr(player, "special_attack"):
            player.special_attack(enemy)
        else:
            print("No special attack available.")
        time.sleep(1)
    elif choice == "3":
        player.heal()
        time.sleep(1)
    else:
        print("Invalid choice.")
        time.sleep(1)

def enemy_turn(enemy, player):
    print(f"\n{enemy.name}'s turn:")

    actions = ["attack", "special_attack", "heal"]

    while True:
        action = random.choice(actions)

        if action == "attack":
            print(f"{player.name}, you are about to be attacked! Choose your defense: ")
            print("1 - Parry (chance to counterattack)")
            print("2 - Dodge (chance to avoid attack)")

            choice = input("Your choice: ")
            if choice == "1":
                if player.parry(): 
                    print(f"{player.name} parried successfully and counterattacks! Health: {player.health}")
                    player.attack(enemy)
                else:
                    enemy.attack(player)
                    print(f"{player.name} failed to parry.")
                    enemy.attack(player)

            elif choice == "2":
                if player.dodge():
                    print(f"{player.name} dodged the attack! Health: {player.health}")
                else:
                    print(f"{player.name} failed to dodge. Health: {player.health}")
                    enemy.attack(player)
            else:
                enemy.attack(player)
            time.sleep(1)
        elif action == "special_attack":
            if hasattr(enemy, "special_attack"):
                enemy.special_attack(player)
                time.sleep(1)
                break
            else:
                continue

        elif action == "heal":
            enemy.heal()
            time.sleep(1)
            break


def main():
    print("Welcome to the Battle Game!\n")
    while True:
        world = input(f"Choose a world {worlds}: ")
        if world not in worlds:
            print("Invalid world. Try again.")
        else:
            break

    name = input("Enter your character's name: ")
    race = input("Enter your character's race: ")
    RoleClass = select_role(world)
    player = RoleClass(name, race)

    enemies = get_enemies(world)

    while enemies and player.health > 0:
        enemy_template = random.choice(enemies)
        enemy = Character(enemy_template.name, enemy_template.race, enemy_template.health, enemy_template.attack_range, enemy_template.defence, enemy_template.damage)
        print(f"\nYour opponent is {enemy.name} ({enemy.race}) with {enemy.health} health.")
        print("Battle begins!")

        while player.health > 0 and enemy.health > 0:
            player_turn(player, enemy)
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated!\n")
                enemies.remove(enemy_template)
                break
            enemy_turn(enemy, player)
            if player.health <= 0:
                print(f"{player.name} has fallen in battle...\nGame over.")
                return

    if player.health > 0:
        print(f"Congratulations {player.name}, you defeated all your enemies! Thanks for playing.")

if __name__ == "__main__":
    main()
