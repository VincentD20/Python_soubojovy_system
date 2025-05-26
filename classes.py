from character import Character

class Fantasy:
    class Mage(Character):
        def __init__(self, name, race, health, attack_range, mana, defense, damage):
            super().__init__(name, race, health)
            self.attack_range = attack_range
            self.mana = mana
            self.defense = defense
            self.damage = damage
            self.magic = ["Fire", "Ice", "Water", "Poison"]

    class Warrior(Character):
        def __init__(self, name, race, health, attack_range, defense, damage, speed):
            super().__init__(name, race, health)
            self.attack_range = attack_range
            self.speed = speed
            self.defense = defense
            self.damage = damage
            self.weapon = ["Sword", "Greatsword", "Axe", "Battleaxe", "Dagger", "Spear", "Warhammer", "Katana"]

    class Archer(Character):
        def __init__(self, name, race, health, attack_range, defense, damage, speed):
            super().__init__(name, race, health)
            self.attack_range = attack_range
            self.speed = speed
            self.defense = defense
            self.damage = damage
            self.weapon = ["Bow", "Crossbow", "Slingshooter"]
            self.attachment = ["Fire", "Poison", "None", "Explosive"]

class Scifi:
    class Power(Character):
        def __init__(self, name, race, health, attack_range, defense, damage, speed):
            super().__init__(name, race, health)
            self.attack_range = attack_range
            self.speed = speed
            self.defense = defense
            self.damage = damage
            self.side = ["Dark", "Light"]
            self.color = ["Blue", "Red", "White", "Yellow", "Purple"]

    class Mandalorian(Character):
        def __init__(self, name, race, health, attack_range, defense, damage, speed):
            super().__init__(name, race, health)
            self.attack_range = attack_range
            self.speed = speed
            self.defense = defense
            self.damage = damage

    class Trooper(Character):
        def __init__(self, name, race, health, attack_range, defense, damage, speed):
            super().__init__(name, race, health)
            self.attack_range = attack_range
            self.speed = speed
            self.defense = defense
            self.damage = damage

class ModernWorld:
    class Soldier(Character):
        def __init__(self, name, race, health, attack_range, defense, damage, speed):
            super().__init__(name, race, health)
            self.attack_range = attack_range
            self.speed = speed
            self.defense = defense
            self.damage = damage
            self.weapon = ["Sniper", "Pistol", "Light-machine-gun", "Submachine-gun", "Rifle", "Shotgun", "Hands"]
