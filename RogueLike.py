import os
import sys
import time
import collections
from ClassDefaultTemplates import *


# Print story of game, wait for enter input/wait some time
# to call display_menu_screen.
def display_intro_screen():
    pass


# Display menu choices
def display_menu_screen():
    pass


# Info about WSAD movement, attributes and dice combat
def menu_display_how_to_play():
    pass


# highscores, records --- Irek
def menu_display_hall_of_fame():
    pass


# What the game is about, credits
def menu_display_about_screen():
    pass


# Exits the program, ask Y/N
def menu_exit_game():
    pass


# Irek
# Initiates new game sequence; character creation
def menu_new_game():
    os.system("clear")
    create_character()


def print_class_attributes(player_class, warrior_attr_default, rogue_attr_default, mage_attr_default):
    ''' Print out the current class attribute table.'''

    print("Your class attributes:" + "\n")
    if player_class == "warrior":
        player_class_attr = collections.OrderedDict(sorted(warrior_attr_default.items()))
        for attr, value, in player_class_attr.items():
            print('{} ---- {}'.format(attr, value))

    elif player_class == "rogue":
        player_class_attr = collections.OrderedDict(sorted(rogue_attr_default.items()))
        for attr, value, in player_class_attr.items():
            print('{} ---- {}'.format(attr, value))

    elif player_class == "mage":
        player_class_attr = collections.OrderedDict(sorted(mage_attr_default.items()))
        for attr, value, in player_class_attr.items():
            print('{} ---- {}'.format(attr, value))
    return(player_class_attr)


def slow_print(string, delay=.03):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)


def create_character():
    '''Choose name, class, print attribute table, assign new
       attributes to character. Option to reset atr. to deafult.'''

    list_of_classes = ["warrior", "mage", "rogue"]
    string_ask_name = ("Welcome!" + "\n" + "What is your name, traveler?" + "\n")
    slow_print(string_ask_name)

    while True:
        player_name = input("My name is: ").title().strip()
        if all(x.isalpha() or x.isspace() for x in player_name):
            string_answer_valid_name = ("Very well, nice to meet you, " + player_name + "." + "\n"
                                        + "Now, are you a warrior, a mage, or a rogue?" + "\n")
            slow_print(string_answer_valid_name)
            break
        else:
            string_answer_invalid_name = ("I'm sorry, you have to tell me your real name. " + "\n")
            slow_print(string_answer_invalid_name)

    while True:
        player_class = input("I am a: ").lower().strip()
        if player_class not in list_of_classes:
            string_answer_invalid_class = ("Surely you jest, you must be either a warrior, a mage, or a rogue!" + "\n")
            slow_print(string_answer_invalid_class)

        else:
            string_answer_valid_class = ("A " + player_class + "? Good. Let's see what you are capable of then!" + "\n")
            slow_print(string_answer_valid_class)

            break
    time.sleep(2)

    os.system('clear')
    # imported default class attribute dictionaries.
    player_class_attr = print_class_attributes(player_class, warrior_attr_default,
                                               rogue_attr_default, mage_attr_default)

    time.sleep(2)
    available_attribute_points = 15
    string_ask_attribute_distribution = ("\n" + "Now that we can see your attributes, "
                                         + "let's improve them a little." + "\n" + "I can give you at most "
                                         + str(available_attribute_points) + " points to spend on improving your stats."
                                         + "\n" + "So choose wisely!" + "\n")
    slow_print(string_ask_attribute_distribution)
    # Choosing attributes to increase, and modify current class attribute dictionary
    while available_attribute_points > 0:
        # String variable incase of  input error in choosing number of points to assign
        string_invalid_input = ("\n" + "I'm not sure I understand you, let's try again" + "\n")
        string_out_of_points = ("\n" + "You don't have enough points to do that!" + "\n")
        string_ask_target_attribute = ("\n" + "Which attribute do you wish to improve?" + "\n")
        slow_print(string_ask_target_attribute)

# ----- add limiter to attribute assigning -----

        # Define targeted attribute and modify it
        target_attribute = input("I wish to improve: ").upper().strip()
        if target_attribute == "STR" or target_attribute == "STRENGTH":
            while True:
                    string_ask_str_increase_size = ("\n" + "How many points do you wish to assign to strength?" + "\n")
                    slow_print(string_ask_str_increase_size)
                    try:
                        str_increase = int(input("Increase it by: ").strip())
                        if str_increase <= available_attribute_points:
                            player_class_attr['STR'] = player_class_attr.get('STR') + str_increase
                            os.system('clear')
                            print("Your class attributes:" + "\n")
                            for attr, value, in player_class_attr.items():
                                print('{} ---- {}'.format(attr, value))
                            available_attribute_points -= str_increase
                            print("Remaining attribute points: ", available_attribute_points)
                        else:
                            slow_print(string_out_of_points)
                        break
                    except ValueError:
                        slow_print(string_invalid_input)

        elif target_attribute == "DEX" or target_attribute == "DEXTERITY":
            while True:
                    string_ask_dex_increase_size = ("\n" + "How many points do you wish to assign to dexterity?" + "\n")
                    slow_print(string_ask_dex_increase_size)
                    try:
                        dex_increase = int(input("Increase it by: ").strip())
                        if dex_increase <= available_attribute_points:
                            player_class_attr['DEX'] = player_class_attr.get('DEX') + dex_increase
                            os.system('clear')
                            print("Your class attributes:" + "\n")
                            for attr, value, in player_class_attr.items():
                                print('{} ---- {}'.format(attr, value))
                            available_attribute_points -= dex_increase
                            print("Remaining attribute points: ", available_attribute_points)
                        else:
                            slow_print(string_out_of_points)
                        break
                    except ValueError:
                        slow_print(string_invalid_input)

        elif target_attribute == "INT" or target_attribute == "INTELLIGENCE":
            while True:
                    string_ask_int_increase_size = ("\n" + "How many points do you wish to assign to intelligence?"
                                                    + "\n")
                    slow_print(string_ask_int_increase_size)
                    try:
                        int_increase = int(input("Increase it by: ").strip())
                        if int_increase <= available_attribute_points:
                            player_class_attr['INT'] = player_class_attr.get('INT') + int_increase
                            os.system('clear')
                            print("Your class attributes:" + "\n")
                            for attr, value, in player_class_attr.items():
                                print('{} ---- {}'.format(attr, value))
                            available_attribute_points -= int_increase
                            print("Remaining attribute points: ", available_attribute_points)
                        else:
                            slow_print(string_out_of_points)
                        break
                    except ValueError:
                        slow_print(string_invalid_input)

        elif target_attribute == "STA" or target_attribute == "STAMINA":
            while True:
                    string_ask_sta_increase_size = ("\n" + "How many points do you wish to assign to stamina?" + "\n")
                    slow_print(string_ask_sta_increase_size)
                    try:
                        sta_increase = int(input("Increase it by: ").strip())
                        if sta_increase <= available_attribute_points:
                            player_class_attr['STA'] = player_class_attr.get('STA') + sta_increase
                            os.system('clear')
                            print("Your class attributes:" + "\n")
                            for attr, value, in player_class_attr.items():
                                print('{} ---- {}'.format(attr, value))
                            available_attribute_points -= sta_increase
                            print("Remaining attribute points: ", available_attribute_points)
                        else:
                            slow_print(string_out_of_points)
                        break
                    except ValueError:
                        slow_print(string_invalid_input)

        else:
                slow_print(string_invalid_input)
    os.system('clear')
    print("Your class attributes:" + "\n")
    for attr, value, in player_class_attr.items():
        print('{} ---- {}'.format(attr, value))
    used_all_attributes = ("\n" + "You used all of your available attribute points!" + "\n")
    slow_print(used_all_attributes)


# TO DO:
#       sort the printed attribute list
#       Make so you can't assign more points to attributes than available attr.
#       i.e. if I got 8 attr, I can't assign 10 and  have -2 attr remaining. For loop?


# initiates game fucntions
def game_core():
    create_character()


def main():
    game_core()


main()
