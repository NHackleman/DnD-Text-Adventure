import random
from weapon_builder import Weapon

class Character:


    def __init__(self, name, race, subclass, attributes, weapon, hp, mp, crit, xp, level, skill_points, is_valid):
        self.name = name
        self.race = race
        self.subclass = subclass
        self.attributes = attributes
        self.weapon = weapon
        self.hp = hp
        self.mp = mp
        self.crit = crit
        self.xp = xp
        self.level = level
        self.skill_points = skill_points
        self.is_valid = is_valid


# Set default stats for human
def build_human(character):
    print('The human is a jack of all trades, and master of none. A wise choice for anyone looking for many different paths for their build.')
    character.hp = 100
    character.mp = 100
    character.attributes = {'str': 1, 'agi': 1, 'int': 1, 'chr': 0}
    
# Set default stats for dwarf
def build_dwarf(character):
    print('The dwarf may not be the most agile of races, but what it lacks in speed, it makes up for in strength and ingenuity.')
    character.hp = 120
    character.mp = 80
    character.attributes = {'str': 2, 'agi': 0, 'int': 1, 'chr': 0}

# Set default stats for elf
def build_elf(character):
    print('The elf is a very cunning and quick race, capable of wielding powerful magic as a mage, or leaping from rooftop to rooftop swiftly as a rogue.')
    character.hp = 80
    character.mp = 120
    character.attributes = {'str': 0, 'agi': 0, 'int': 2, 'chr': 1}

# Set default stats for orc
def build_orc(character):
    print('The orc relies on its brawn over brain. Though unintelligent, the orc can take and deal more damage than any other race through sheer brute force.')
    character.hp = 130
    character.mp = 70
    character.attributes = {'str': 3, 'agi': 0, 'int': 0, 'chr': 0}

def build_warrior(character):
    weapon_sword = Weapon('sword', 'melee', 'physical', 3)

    character.subclass = 'Warrior'
    character.attributes['str'] += 2
    character.attributes['agi'] += 1
    character.hp += 30
    character.crit += 10
    character.weapon = weapon_sword
    return character

def build_cleric(character):
    weapon_mace = Weapon('mace', 'melee', 'physical', 2)
    
    character.subclass = 'Cleric'
    character.attributes['int'] += 2
    character.attributes['chr'] += 1
    character.hp += 10
    character.mp += 10
    character.weapon = weapon_mace
    return character

def build_rogue(character):
    weapon_knife = Weapon('knife', 'melee', 'physical', 1)

    character.subclass = 'Rogue'
    character.attributes['agi'] += 2
    character.attributes['int'] += 1
    character.hp -= 10
    character.crit += 30
    character.weapon = weapon_knife
    return character

def build_mage(character):
    weapon_staff = Weapon('staff', 'ranged', 'magical', 3)

    character.subclass = 'Mage'
    character.attributes['int'] += 3
    character.hp -= 10
    character.mp += 30
    character.weapon = weapon_staff
    return character