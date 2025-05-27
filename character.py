import random

class Character:
    def __init__(self, name, race, health, attack_range, defence, damage):
        self.attack_range = attack_range
        self.defence0 = defence
        self.damage = damage
        self.name = name
        self.rasa = race
        self.health = health


    def attack(self, enemy):
        enemy.health -= self.damage
        print(f"{self.name} attacks {enemy.name} for {self.damage} damage!")
    
    def defence(self):
        kostka = int(input(f"Parry the attack (guess the number - 1 to 20):"))
        number = random.randint(1, 20)
        if kostka == number:
            print(f"You parried the attack! Your health: {self.health}")
        else:
            damage_taken = self.damage - random.randint(1, self.defence)
            if damage_taken < 0:
                damage_taken = 0
            self.health -= damage_taken
            print(f"The enemy hit you. You took {damage_taken} damage. Your health: {self.health}")