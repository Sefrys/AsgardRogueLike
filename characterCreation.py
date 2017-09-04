import sys
import os
import time
import collections
from classDefaultTemplates import *



def print_class_attributes(attr_class, warrior, rogue, mage):
    ''' Print out the current class attribute table.'''

    print("Your class attributes:\n")
    player_class_attr = collections.OrderedDict(sorted(attr_class.items()))
    for attr, value, in player_class_attr.items():
        print('{} ---- {}'.format(attr, value))
    return(player_class_attr)


def slow_print(string, delay=0):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)


def create_character():
    '''Choose name, class, print attribute table, assign new
       attributes to character. Option to reset atr. to deafult.'''

    list_of_classes = ["warrior", "mage", "rogue"]
    string_ask_name = ("Welcome!\nWhat is your name, traveler?\n")
    slow_print(string_ask_name)

    while True:
        player_name = input("My name is: ").title().strip()
        if all(x.isalpha() or x.isspace() for x in player_name):
            string_answer_valid_name = ("Very well, nice to meet you, " + player_name + ".\n"
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
    if player_class == "warrior":
        attr_class = warrior
    elif player_class == "mage":
        attr_class = mage
    elif player_class == "rogue":
        attr_class = rogue
    time.sleep(2)

    os.system('clear')
    # imported default class attribute dictionaries.
    player_class_attr = print_class_attributes(attr_class, warrior, rogue, mage)

    time.sleep(2)
    available_attribute_points = 15
    string_ask_attribute_distribution = ("\nNow that we can see your attributes, "
                                         + "let's improve them a little.\nI can give you at most "
                                         + str(available_attribute_points) + " points to spend on improving your stats."
                                         + "\nSo choose wisely!\n")
    slow_print(string_ask_attribute_distribution)
    # Choosing attributes to increase, and modify current class attribute dictionary
    while available_attribute_points > 0:
        # String variable incase of  input error in choosing number of points to assign
        string_invalid_input = ("\nI'm not sure I understand you, let's try again\n")
        string_out_of_points = ("\nYou don't have enough points to do that!\n")
        string_ask_target_attribute = ("\nWhich attribute do you wish to improve?\n")
        slow_print(string_ask_target_attribute)

        # Define targeted attribute and modify it
        target_attribute = input("I wish to improve: ").upper().strip()
        atr_list = ["STR", "DEX", "STA", "INT"]
        if target_attribute in atr_list:
            while True:
                    string_ask_atr_increase_size = ("\nHow many points do you wish to assign to {}?\n".format(target_attribute.upper()))
                    slow_print(string_ask_atr_increase_size)
                    try:
                        atr_increase = int(input("Increase it by: ").strip())
                        if atr_increase <= available_attribute_points:
                            player_class_attr[str(target_attribute).upper()] = player_class_attr.get(str(target_attribute).upper()) + atr_increase
                            os.system('clear')
                            print("Your class attributes:\n")
                            for attr, value, in player_class_attr.items():
                                print('{} ---- {}'.format(attr, value))
                            available_attribute_points -= atr_increase
                            print("Remaining attribute points: ", available_attribute_points)
                        else:
                            slow_print(string_out_of_points)
                        break
                    except ValueError:
                        slow_print(string_invalid_input)
        else:
            slow_print(string_invalid_input)
    os.system('clear')
    print("Your class attributes:\n")
    for attr, value, in player_class_attr.items():
        print('{} ---- {}'.format(attr, value))
    used_all_attributes = ("\nYou used all of your available attribute points!\n")
    slow_print(used_all_attributes)
