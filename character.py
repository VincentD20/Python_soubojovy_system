from classes import *
import random

class Character:
    def __init__(self, name, race, health):
        self.name = name
        self.rasa = race
        self.health = health
    def attack(self, enemy):
        enemy - self.damage
        print()
    def defence(self):
        kostka = input(f"Parry the attack (guess the number - 1 to 20)")
        number = random.randint(1, 20)
        if kostka == number:
            print(f"You parryed the attack. Your health {self.health}")
        else:
            self.health - (self.damage - random.randint(1, self.defence))
            print(f"Nepřítel vás zasáhl. Vaše zdraví: {self.health}")