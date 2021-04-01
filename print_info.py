def print_character(character):
    print(f"""
    **YOUR CHARACTER**
    Name: {character.name}
    Race: {character.race}
    Class: {character.subclass}
    Attributes: 
        Strength- {character.attributes['str']}
        Agility- {character.attributes['agi']}
        Intelligence- {character.attributes['int']}
        Charisma- {character.attributes['chr']}
    Weapon: {character.weapon.name.capitalize()}
    HP: {character.hp}
    MP: {character.mp}
    Critical Chance: {character.crit}%
    """)