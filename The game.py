
# Imports
import random as r
import time as t


# Inventory initializing
inventory = []

# repeatable and variables
not_valid = "Your answer is not valid"

s = 1/18 # speed: Used for text_typer. The lower the number the faster the text appears

# Functions
def text_typer(text):
    """
    Purpose: To print text like it is being typed (not in bursts).

    Pre-conditions:
    :param text: Text to be printed
    :param time: time between each letter printed

    Post-condition: text printed
    :return: none
    """
    for letter in text:
        t.sleep(s) # Ideal is time * 0.8.
        print(letter, end='')

def type_open():
    """
    Purpose: to type commands at any time during the game
    :return: word to be examined by other functions
    """
    type_open = input('').lower().strip()
    return type_open

def access_inventory():
    """
    Purpose: To view inventory (inventory is a list)
    Pre-condition: None
    Post-condition: if type_open is set to the string inventory, the inventory is open
    :return: None
    """

    if type_open == "inventory":
        print('')
        print(inventory)
        print('')



# Welcome message

print('\n\nThe Lost Explorer: Quest in the Forgotten Island')
line = '*******************************************************'
print(line)


# Main information collection

print('')

player_name = input('Name: ')
print(line, '\n\n')
Hello_explorer = 'Hello ' + player_name + '!'

text_typer(Hello_explorer)
print('\n')




# Start game?

ask_ready = 'This is a text-based game. Are you ready for the adventure?  (yes/no)\n'
ready_bool = False
quit_counter = 0
text_typer(ask_ready)

while ready_bool is False:

    # Ready? question input
    ask_ready_answer = input().lower().strip()


    if ask_ready_answer == 'yes' or ask_ready_answer == 'ya' or ask_ready_answer == 'y':
        break
    else:
        emm = "emm..."
        not_expected = "that was not expected. Perhaps you meant to type 'yes'?\n"
        clear_throat = "lets try this again.. READY?!\n"
        help = "Do you know how to spell yes?\n"
        angry = "WHAT ARE YOU DOING??!\nInhaling..\nExhaling...\nokay, let's see..\n\nDon't you not want to not play this game?\n"
        last_chance = "...\nYou know... I am not sure of what you are attempting here. There is no point of doing this.\nIf you think you will get somewhere with this, then think again.\nJust say no this time again because I do not think you want to play this game. \nWould you like to play this game?\n"

        if quit_counter == 5:
            print(line)
            print("\n* ACHIEVEMENT: The I'm-no-quitter-when-it-comes-to-quitting ending *")
            print(('\nThanks for playing!').upper())
            print('')
            print(line)
            quit()
        else:
            if quit_counter == 0:
                text_typer(emm)
                text_typer(not_expected)
            elif quit_counter == 1:
                text_typer(clear_throat)
            elif quit_counter == 2:
                text_typer(emm)
                text_typer(help)
            elif quit_counter == 3:
                text_typer(angry)
            elif quit_counter == 4:
                text_typer(last_chance)


    quit_counter += 1

# Story begins. CHAPTER 1.
Chapter = ("Chapter 1\n").upper()
radio_message_1 = "UNKNOWN: Shhhh.. Shhh... H-Shh lo.. ..483? \n\tHel.. Sh.. Hello!\n\n"
self_message_1 =str(player_name + ": This damn radio! Hi! Do you copy?\n")

print("\n\n")
print(line)
text_typer(Chapter)
print(line)
print("\n")


# Radio

text_typer(radio_message_1)
text_typer(self_message_1)

step_away = 'no'

while step_away == 'no':

    script_1 = "\nThe door of the cabin is creaking. The strong wind can be heard through the thin walls rustling. Rain and water droplets from the waves bounce off the rooftop. \n"
    text_typer(script_1)
    script_2 = "The light above you is flickering, and it seems like the storm is only getting worse.\n"
    text_typer(script_2)

    try_radio = "You give the radio another shot. No success....\nThe tiny lightbulb on the device is glowing red.\n\n"\
                + player_name + ": It must be the antenna. I should check it out; the storm is not winding down any " \
                                "time soon.\n\n"
    text_typer(try_radio)

    step_away_message = 'Do you step away from the radio? (yes/no)'
    text_typer(step_away_message)
    step_away = input('\n').strip().lower()

    if step_away == 'yes':
        break
    elif step_away != 'no':
        print("\nValid answers: 'yes' and 'no'")
        step_away = "no"


successful_step_away = "\nYour heart is pounding. You dread your every step towards the door, you know it must be done.\n"
palm_approaching_the_door = "\nYour palm is approaching the door's handle... \n"
remember_flashlight = 'As your hand is gripping the door handle you remember... There is a flashlight in the small closet on your right hand side!\nBelow the shelves is a small window that is made of very thick glass.\nThrough the window you see the water pouring outside. You catch a glimse of the moon that is almost entirely hidden by the thunder storm.\n\n' \
                      + player_name + ": Time to head out. I have to make it back quick.\n"
grab_flashlight = "\nDo you grab the flashlight? (yes/no)\n"

text_typer(successful_step_away)
text_typer(palm_approaching_the_door)
text_typer(remember_flashlight)

out = False

while out is False:
    text_typer(grab_flashlight)
    grab_flashlight_input = input("").strip().lower()

    if grab_flashlight_input == 'yes':
        inventory.append("flashlight")
        out = True
    elif grab_flashlight_input == 'no':
        sure_no = input('Are you sure you would like to step out without a flashlight? (yes/no)\n')
        if sure_no == 'yes':
            out = True
        elif sure_no == 'no':
            out = False
        else:
            text_typer(not_valid)
            out = False
    else:
        text_typer(not_valid)
        out = False

try_out_inventory = "To view your inventory type the word: 'inventory'\nTry it out - "

text_typer(try_out_inventory)

type_open = type_open()
access_inventory()

leave_cabin = "Your hand grips the handle tightly... \nYou take a deep breath..\nYou turn the handle and open the door. Stepping out, you shut the door and it makes a loud thud behind you *thud*"
text_typer(leave_cabin)

end_of_chapter_1 = '\n\nEnd of chapter 1'
text_typer(end_of_chapter_1)

Chapter = 'CHAPTER 2'
print("\n\n")
print(line)
text_typer(Chapter)
print('')
print(line)
print("\n")
