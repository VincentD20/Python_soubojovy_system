from character import Character

class Fantasy:
    class Mage(Character):
        def __init__(self, name, race):
            super().__init__(name, race, health=200, attack_range=(10, 20), defence=5, damage=25)
            self.mana = 100
            self.magic = ["Fireball", "Ice Spike", "Lightning"]

        def special_attack(self, enemy):
            if self.mana < 10:
                print(f"{self.name} doesn't have enough mana to cast a spell!")
                return
            spell_damage = self.damage + 15
            enemy.health -= max(spell_damage - enemy.defence, 0)
            self.mana -= 10
            print(f"{self.name} casts a powerful spell on {enemy.name} for {spell_damage} damage!")

    class Warrior(Character):
        def __init__(self, name, race):
            super().__init__(name, race, health=400, attack_range=(5, 10), defence=20, damage=40)

        def special_attack(self, enemy):
            damage = self.damage + 20
            enemy.health -= max(damage - enemy.defence, 0)
            print(f"{self.name} performs a heavy strike on {enemy.name} for {damage} damage!")

    class Archer(Character):
        def __init__(self, name, race):
            super().__init__(name, race, health=250, attack_range=(15, 25), defence=10, damage=30)

        def special_attack(self, enemy):
            damage = self.damage + 25
            enemy.health -= max(damage - enemy.defence, 0)
            print(f"{self.name} shoots a precise arrow at {enemy.name} for {damage} damage!")

class Scifi:
    class Power(Character):
        def __init__(self, name, race):
            super().__init__(name, race, health=650, attack_range=(10, 15), defence=20, damage=50)

        def special_attack(self, enemy):
            damage = self.damage + 30
            enemy.health -= max(damage - enemy.defence, 0)
            print(f"{self.name} unleashes power blast on {enemy.name} for {damage} damage!")

    class Mandalorian(Character):
        def __init__(self, name, race):
            super().__init__(name, race, health=500, attack_range=(10, 20), defence=40, damage=40)

        def special_attack(self, enemy):
            damage = self.damage + 15
            enemy.health -= max(damage - enemy.defence, 0)
            print(f"{self.name} fires a barrage on {enemy.name} for {damage} damage!")

    class Trooper(Character):
        def __init__(self, name, race):
            super().__init__(name, race, health=300, attack_range=(5, 15), defence=30, damage=25)

        def special_attack(self, enemy):
            damage = self.damage + 10
            enemy.health -= max(damage - enemy.defence, 0)
            print(f"{self.name} suppresses {enemy.name} for {damage} damage!")

class ModernWorld:
    class Soldier(Character):
        def __init__(self, name, race):
            super().__init__(name, race, health=350, attack_range=(8, 15), defence=20, damage=35)

        def special_attack(self, enemy):
            damage = self.damage + 20
            enemy.health -= max(damage - enemy.defence, 0)
            print(f"{self.name} throws a grenade at {enemy.name} for {damage} damage!")
