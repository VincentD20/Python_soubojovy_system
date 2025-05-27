
class Fantasy:
    class Mage(Character):
        def __init__(self, name, race, health, attack_range, mana, defense, damage):
            super().__init__(name, race, health, attack_range, defense, damage)
            self.mana = mana
            self.magic = ["Fire", "Ice", "Water", "Poison"]

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
        def __init__(self, name, race, health, attack_range, defense, damage):
            super().__init__(name, race, health, attack_range, defense, damage)
            self.weapon = ["Sword", "Greatsword", "Axe", "Battleaxe", "Dagger", "Spear", "Warhammer", "Katana"]

    class Archer(Character):
        def __init__(self, name, race, health, attack_range, defense, damage):
            super().__init__(name, race, health, attack_range, defense, damage)
            self.weapon = ["Bow", "Crossbow", "Slingshooter"]
            self.attachment = ["Fire", "Poison", "None", "Explosive"]

class Scifi:
    class Power(Character):
        def __init__(self, name, race, health, attack_range, defense, damage):
            super().__init__(name, race, health, attack_range, defense, damage)
            self.side = ["Dark", "Light"]
            self.color = ["Blue", "Red", "White", "Yellow", "Purple"]

    class Mandalorian(Character):
        def __init__(self, name, race, health, attack_range, defense, damage):
            super().__init__(name, race, health, attack_range, defense, damage)
            self.weapon = []

    class Trooper(Character):
        def __init__(self, name, race, health, attack_range, defense, damage):
            super().__init__(name, race, health, attack_range, defense, damage)

class ModernWorld:
    class Soldier(Character):
        def __init__(self, name, race, health, attack_range, defense, damage):
            super().__init__(name, race, health)
            super().__init__(name, race, health, attack_range, defense, damage)
            self.weapon = ["Sniper", "Pistol", "Light-machine-gun", "Submachine-gun", "Rifle", "Shotgun", "Hands"]
