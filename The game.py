
# Imports
import random as r
import time as t


# Inventory initializing
inventory = []
in_room_location = []
flashlight = ["flashlight"]

# repeatable and variables
not_valid = "Your answer is not valid\n"

s = 0.04 # speed: Used for text_typer. The lower the number the faster the text appears

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
radio_message_1 = "UNKNOWN: Shhhh.. Shhh... H-Shh lo.. ..483.? \n\tHel.. Sh.. lo?!\n\n"
self_message_1 =str(player_name + ": This damn radio! Hi! Do you copy?\n")

print("\n\n")
print(line)
text_typer(Chapter)
print(line)
print("\n")


# Chapter 1: Radio

text_typer(radio_message_1)
text_typer(self_message_1)

first_pass_radio = 0

def at_radio():
    step_away = 'no'
    radio_count = 0 + first_pass_radio

    while step_away == 'no':

        radio_count += 1

        script_1 = "\nThe door of the cabin is creaking. The strong wind can be heard through the thin walls rustling. Rain and water droplets from the waves bounce off the rooftop. \n"
        script_2 = "The light above you is flickering, and it seems like the storm is only getting worse.\n"
        try_radio = "\nYou give the radio another shot. No success....\nThe tiny lightbulb on the device is glowing red.\n"
        antenna_statement = "\n" + player_name + ": It must be the antenna. I should check it out; the storm is not winding down any time soon.\n\n"
        reveal_boat_number = "Under the tiny red lightbulb is written in faint grey: Axq4835\n"


        if radio_count == 1:
            text_typer(script_1)
            text_typer(script_2)
            text_typer(try_radio)
            text_typer(antenna_statement)
        elif radio_count > 1:
            text_typer(try_radio)
            text_typer(reveal_boat_number)
            text_typer(antenna_statement)


        step_away_message = 'Do you step away from the radio? (yes/no)'
        text_typer(step_away_message)
        step_away = input('\n').strip().lower()

        if step_away == 'yes':
            break
        elif step_away != 'no':
            print("\nValid answers: 'yes' and 'no'")
            step_away = "no"

at_radio()

first_pass_radio += 1

successful_step_away = "\nYour heart is pounding. You dread your every step towards the door; you know it must be done.\n"
text_typer(successful_step_away)

safe_content = ['first aid equipment', 'lighter']

def safe_opened():

    text_typer("The safe opened\n")

    text_typer("Which item would you like to grab?\nInstructions:'All' for all items; 'quit' to quit; otherwise type the item's name to grab the item specified ")
    text_typer("\nSafe content: ")
    print(safe_content)
    action_in_safe = input(''.strip().lower())

    if action_in_safe == 'all':
        while len(safe_content) != 0:
            for item in safe_content:
                inventory.append(item)
                safe_content.remove(item)
        if len(safe_content) == 0:
            return False

    elif action_in_safe != 'quit':
        if action_in_safe in safe_content:
            inventory.append(action_in_safe)
            safe_content.remove(action_in_safe)
        safe_opened()
    elif action_in_safe == 'quit':
        return False

def safe():

    safe_seen = "You are unsure if the items in your safe can be useful in this circumstance."
    open_safe_statement = "\nWould you like to attempt opening the safe? (yes/no)\n"

    text_typer(safe_seen)

    while True:

        text_typer(open_safe_statement)

        attempt_safe = input().strip().lower()

        if attempt_safe == "yes":
            enter_code = "Enter the 4 digit code:\t"
            text_typer(enter_code)
            code_attempt = str(input())
            print()
            if code_attempt == "4835":
                safe_opened()
                break
            else:
                code_incorrect = "The safe did not open\n"
                text_typer(code_incorrect)
        elif attempt_safe == "no":
            return False
        else:
            text_typer(not_valid)
            return True

safe()

palm_approaching_the_door = "\nYour palm is almost touching the door's handle... \n"
remember_flashlight = 'As your hand is gripping the door handle you remember... There is a flashlight in the small closet on your right hand side!\nBelow the shelves is a small window that is made of very thick glass.\nThrough the window you see the water pouring outside. You catch a glimpse of the moon that is almost entirely hidden by the thunder storm.\n\n' \
                      + player_name + ": Time to head out. I have to make it back quick.\n"
grab_flashlight = "\nDo you grab the flashlight? (yes/no)\n"


def leave_cabin():
    text_typer(palm_approaching_the_door)
    out = False
    if "flashlight" not in inventory:
        while out is False:
            text_typer(remember_flashlight)
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


def head_where_in_cabin():
    while True:
        where_next = "\nWhere would you like to go next?\n"
        locations_in_ch1_cabin = "1- The radio\n2- The safe\n3- The door\n\n"

        text_typer(where_next)
        text_typer(locations_in_ch1_cabin)
        next_location_address = input('').strip()

        if next_location_address == '1':
            at_radio()
        elif next_location_address == '2':
            safe()
        elif next_location_address == '3':
            leave_cabin()
            leave_cabin_bool = input("\nExit the cabin? (yes/no)\n").lower().strip()
            if leave_cabin_bool == 'yes':
                break
            elif leave_cabin_bool != 'no':
                text_typer(not_valid)
        else:
            text_typer("Possible inputs are '1', '2', or '3'")


head_where_in_cabin()


try_out_inventory = "\nTo view your inventory type the word: 'inventory'\nTry it out - "

text_typer(try_out_inventory)

type_open = type_open()
access_inventory()

leaving_cabin_statement = "Your hand grips the handle tightly... \nYou take a deep breath..\nYou turn the handle and open the door. Stepping out, you shut the door and it makes a loud thud behind you *thud*"
text_typer(leaving_cabin_statement)



end_of_chapter_1 = '\n\n\nEnd of chapter 1'.upper()
text_typer(end_of_chapter_1)

Chapter = 'CHAPTER 2'
print("\n\n")
print(line)
text_typer(Chapter)
print('')
print(line)
print("\n")


# Ideas:
# To make something interactive (ex. opening the door.) I can make a loop where every certain period of time an integer value decreases by 1. It is first initiated and then increases by 1 every time the player presses on the right botton or solves a puzzle (ex. math questions generated using the random module). For every (correct) answer the increase in 1 gets the player closer to the objective number. If the number reaches the objective number the task is complete. If the number reaches 0 the player fails and has to repeat this task. So, the door keeps shutting unless the player solves the puzzle fast enough
