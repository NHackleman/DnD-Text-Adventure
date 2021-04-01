from weapon_builder import Weapon
from character_builder import *

# Build User's character
def build_character(character):
    
    race = str(input('What race would you like to play?\nHuman    Dwarf    Elf    Orc\n')).lower().strip()
    subclass = ''

    # Build character
    if race == 'human' or race == 'dwarf' or race == 'elf' or race == 'orc':
        if race == 'human':
            character.race = race.capitalize()
            build_human(character)

            print('You may choose the following classes:\nWarrior    Cleric    Rogue    Mage')
            subclass = str(input()).lower().strip()

            if subclass == 'warrior' or subclass == 'cleric' or subclass == 'rogue' or subclass == 'mage':
                if subclass == 'warrior':
                    build_warrior(character)
                elif subclass == 'cleric':
                    build_cleric(character)
                elif subclass == 'rogue':
                    build_rogue(character)
                elif subclass == 'mage':
                    build_mage(character)
            else:
                print('Incorrect class...')
                character.is_valid == False


        elif race == 'dwarf':
            character.race = race.capitalize()
            build_dwarf(character)

            print('You may choose the following classes:\nWarrior    Cleric')
            subclass = str(input()).lower().strip()

            if subclass == 'warrior' or subclass == 'cleric':
                if subclass == 'warrior':
                    build_warrior(character)
                elif subclass == 'cleric':
                    build_cleric(character)
            else:
                print('Incorrect subclass...')
                character.is_valid == False

        elif race == 'elf':
            character.race = race.capitalize()
            build_elf(character)

            print('You may choose the following classes:\nCleric    Rogue    Mage')
            subclass = str(input()).lower().strip()

            if subclass == 'cleric' or subclass == 'rogue' or subclass == 'mage':
                if subclass == 'cleric':
                    build_cleric(character)
                elif subclass == 'rogue':
                    build_rogue(character)
                elif subclass == 'mage':
                    build_mage(character)
            else:
                print('Incorrect class...')
                character.is_valid == False
        else:
            character.race = race.capitalize()
            build_orc(character)
            build_warrior(character)
        
        character.level = 0
        character.xp = 0
        return character

    else:
        print('Incorrect race...')
        character.is_valid = False