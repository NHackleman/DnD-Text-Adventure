from character_builder import *
from user_interaction import *
from print_info import *

character = Character('', '', '', {}, '', 0, 0, 0, 0, 0, 0, True)


# <Game start> #

# Name assignment
print('Welcome traveler...')
print('To begin, you must first tell me, what is your name?')
user_input = str(input())
character.name = user_input.capitalize()

print(f'So your name is {character.name} is it?')
print(f'And tell me {character.name} what race would you like to be in this adventure?')

# Build Character
build_character(character)
# Print Character
print_character(character)
