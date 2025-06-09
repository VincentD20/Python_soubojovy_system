import random

class Character:
    def __init__(self, name, race, health, attack_range, defence, damage):
        self.name = name
        self.race = race
        self.health = health
        self.attack_range = attack_range
        self.defence = defence
        self.damage = damage
        self.is_dodging = False
        self.is_parrying = False

    def attack(self, enemy):

        action_chance = random.randint(1, 100)
        
        if action_chance <= 20:
            parry_chance = random.randint(1, 20)
            guess = random.randint(1, 20)
            if parry_chance == guess:
                print(f"{enemy.name} parried {self.name}'s attack and counterattacks!")
                enemy.attack(self)
                return
            else:
                print(f"{enemy.name} tried to parry but failed.")

        elif 20 < action_chance <= 50:
            dodge_chance = random.randint(1, 100)
            if dodge_chance <= 60:
                print(f"{enemy.name} dodged {self.name}'s attack!")
                return
            else:
                print(f"{enemy.name} tried to dodge but failed.")

        dmg = random.randint(*self.attack_range) + self.damage
        net_damage = dmg - enemy.defence
        if net_damage < 0:
            net_damage = 0
        enemy.health -= net_damage
        print(f"{self.name} attacks {enemy.name} for {net_damage} damage!")


    
    def heal(self):
        heal_amount = random.randint(10, 25)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount}. Current health: {self.health}")
    
    def parry(self):
        chance  = random.randint(1, 20)
        guess = random.randint(1, 20)
        if chance == guess:
            self.is_parrying = True
        else:
            self.is_parrying = False
    
    def dodge(self):
        chance = random.randint(1, 100)
        if chance <= 30:
            self.is_dodging = True
            return True
        else:
            self.is_dodging = False
            return False
