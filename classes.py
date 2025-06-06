from character import Character

class Fantasy: 
    class Mage(Character):
        def __init__(self, name, race):
            health = 200
            attack_range = 20
            defence = 5
            damage = 25
            mana = 100
            super().__init__(name, race, health, attack_range, defence, damage)
            self.mana = mana

        def cast_spell(self, enemy, spell):
            if spell not in self.magic:
                print(f"{spell} is not available!")
                return
            if self.mana < 10:
                print(f"{self.name} doesn't have enough mana!")
                return
            spell_damage = self.damage + 5
            print(f"{self.name} casts {spell} on {enemy.name} for {spell_damage} damage!")
            enemy.health -= spell_damage
            self.mana -= 10

    class Warrior(Character):
        def __init__(self, name, race):
            health = 400
            attack_range = 2
            defence = 20
            damage = 40
            super().__init__(name, race, health, attack_range, defence, damage)

    class Archer(Character):
        def __init__(self, name, race):
            health = 250
            attack_range = 50
            defence = 10
            damage = 60
            super().__init__(name, race, health, attack_range, defence, damage)
            

class Scifi:
    class Power(Character):
        def __init__(self, name, race, health, attack_range, defence, damage):
            super().__init__(name, race, health, attack_range, defence, damage)
            self.side = ["Dark", "Light"]
            self.color = ["Blue", "Red", "White", "Yellow", "Purple"]

    class Mandalorian(Character):
        def __init__(self, name, race, health, attack_range, defence, damage):
            super().__init__(name, race, health, attack_range, defence, damage)

    class Trooper(Character):
        def __init__(self, name, race, health, attack_range, defence, damage):
            super().__init__(name, race, health, attack_range, defence, damage)

class ModernWorld:
    class Soldier(Character):
        def __init__(self, name, race, health, attack_range, defence, damage):
            super().__init__(name, race, health, attack_range, defence, damage)
    class Sniper(Character):
        def __init__(self, name, race, health, attack_range, defence, damage):
            super().__init__(name, race, health, attack_range, defence, damage)
