
# Imports
import random as r
import time as t



# Welcome message

print('\n\nThe Lost Explorer: Quest in the Forgotten Island')
line = '*******************************************************'
print(line)





# Main information collection

print('')

def text_typer(text, time):
    """
    Purpose: To print text like it is being typed (not in bursts).

    Pre-conditions:
    :param text: Text to be printed
    :param time: time between each letter printed

    Post-condition: text printed
    :return: none
    """
    for letter in text:
        t.sleep(time)
        print(letter, end='')


player_name = input('Name: ')
print(line, '\n\n')
Hello_explorer = 'Hello ' + player_name + '!'

text_typer(Hello_explorer, 0.09)
print('\n')




# Start game?

ask_ready = 'This is a text-based game. Are you ready for the adventure?  (yes/no)\n'
ready_bool = False
quit_counter = 0
text_typer(ask_ready, 0.03)

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
            print('\n')
            print(line)
            quit()
        else:
            if quit_counter == 0:
                text_typer(emm, 0.1)
                text_typer(not_expected, 0.02)
            elif quit_counter == 1:
                text_typer(clear_throat, 0.01)
            elif quit_counter == 2:
                text_typer(emm, 0.08)
                text_typer(help, 0.015)
            elif quit_counter == 3:
                text_typer(angry, 0.03)
            elif quit_counter == 4:
                text_typer(last_chance, 0.04)


    quit_counter += 1

print('\nGood you goof.. I am working on the rest. Maybe try saying no?')

