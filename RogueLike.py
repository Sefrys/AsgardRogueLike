import os
import sys
import time


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


# Irek
# Choose name, class, print attribute table, assign new
# attributes to character. Option to reset atr. to deafult.
def create_character():
    # ask the player for his character name and his class
    list_of_classes = ["warrior", "mage", "rogue"]
    ask_name = "Welcome!" + "\n" + "What is your name, traveler?" + "\n"
    for i in ask_name:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.03)

    while True:
        player_name = input("My name is: ").title()
        if all(x.isalpha() or x.isspace() for x in player_name):
            answer_valid_name = ("Very well, nice to meet you, " + player_name + "." + "\n"
                                 + "Now, are you a warrior, a mage, or a rogue?" + "\n")
            for i in answer_valid_name:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.03)
            break
        else:
            answer_invalid_name = ("I'm sorry, you have to tell me your real name. " + "\n")
            for i in answer_invalid_name:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.03)

    while True:
        player_class = input("I am a: ").lower().strip()
        if player_class not in list_of_classes:
            answer_invalid_class = ("Surely you jest, you must be either a warrior, a mage, or a rogue!" + "\n")
            for i in answer_invalid_class:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.03)
        else:
            answer_valid_class = ("A " + player_class + "? Good. Let's see what you are capable of then!" + "\n")
            for i in answer_valid_class:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.03)
            break
    time.sleep(2)

    os.system('clear')
    # default class attributes dictionaries.
    warrior_attr_default = {'STR': 17,
                            'DEX': 6,
                            'INT': 7,
                            'STA': 19}

    rogue_attr_default = {'STR': 9,
                          'DEX': 21,
                          'INT': 9,
                          'STA': 15}

    mage_attr_default = {'STR': 5,
                         'DEX': 12,
                         'INT': 18,
                         'STA': 13}
    player_class_attr = {}

    # Print out the current class attribute table.
    def print_class_attributes(player_class, warrior_attr_default, rogue_attr_default, mage_attr_default):

        print("Your class attributes:" + "\n")
        if player_class == "warrior":
            player_class_attr = warrior_attr_default
            for attr, value, in player_class_attr.items():
                print('{} ---- {}'.format(attr, value))

        elif player_class == "rogue":
            player_class_attr = rogue_attr_default
            for attr, value, in player_class_attr.items():
                print('{} ---- {}'.format(attr, value))

        elif player_class == "mage":
            player_class_attr = mage_attr_default
            for attr, value, in player_class_attr.items():
                print('{} ---- {}'.format(attr, value))
        return(player_class_attr)

    player_class_attr = print_class_attributes(player_class, warrior_attr_default, rogue_attr_default, mage_attr_default)
    time.sleep(2)

    ask_attribute_distribution = ("\n" + "Now that we see what you can do, let's improve your attributes a little."
                                  + "\n" + "I can give you at most fifteen points to spend improving your stats."
                                  + "\n" + "So choose wisely!" + "\n")
    for i in ask_attribute_distribution:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.03)

    available_attribute_points = 15

    # Choosing attributes to increase, and modify current class attribute dictionary
    while available_attribute_points > 0:
        ask_target_attribute = ("\n" + "Which attribute do you wish to improve?" + "\n")
        # Variable for input error in choosing number of points to assign
        invalid_stat_increase_response = ("\n" + "I'm not sure I understand you, let's try again" + "\n")
        for i in ask_target_attribute:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.03)

        # Define targeted attribute and modify it
        target_attribute = input("I wish to improve: ").upper().strip()
        if target_attribute == "STR":
            while True:
                    ask_str_increase_size = ("\n" + "How many points do you wish to assign to strength?" + "\n")
                    for i in ask_str_increase_size:
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(.03)
                    try:
                        str_increase = int(input("Increase it by: ").strip())
                        player_class_attr['STR'] = player_class_attr.get('STR') + str_increase
                        os.system('clear')
                        print("Your class attributes:" + "\n")
                        for attr, value, in player_class_attr.items():
                            print('{} ---- {}'.format(attr, value))
                        available_attribute_points -= str_increase
                        print("Remaining attribute points: ", available_attribute_points)
                        break
                    except ValueError:
                        for i in invalid_stat_increase_response:
                            sys.stdout.write(i)
                            sys.stdout.flush()
                            time.sleep(.03)
        elif target_attribute == "DEX":
            while True:
                    ask_dex_increase_size = ("\n" + "How many points do you wish to assign to dexterity?" + "\n")
                    for i in ask_dex_increase_size:
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(.03)
                    try:
                        dex_increase = int(input("Increase it by: ").strip())
                        player_class_attr['DEX'] = player_class_attr.get('DEX') + dex_increase
                        os.system('clear')
                        print("Your class attributes:" + "\n")
                        for attr, value, in player_class_attr.items():
                            print('{} ---- {}'.format(attr, value))
                        available_attribute_points -= dex_increase
                        print("Remaining attribute points: ", available_attribute_points)
                        break
                    except ValueError:
                        for i in invalid_stat_increase_response:
                            sys.stdout.write(i)
                            sys.stdout.flush()
                            time.sleep(.03)

        elif target_attribute == "INT":
            while True:
                    ask_int_increase_size = ("\n" + "How many points do you wish to assign to intelligence?" + "\n")
                    for i in ask_int_increase_size:
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(.03)
                    try:
                        int_increase = int(input("Increase it by: ").strip())
                        player_class_attr['INT'] = player_class_attr.get('INT') + int_increase
                        os.system('clear')
                        print("Your class attributes:" + "\n")
                        for attr, value, in player_class_attr.items():
                            print('{} ---- {}'.format(attr, value))
                        available_attribute_points -= int_increase
                        print("Remaining attribute points: ", available_attribute_points)
                        break
                    except ValueError:
                        for i in invalid_stat_increase_response:
                            sys.stdout.write(i)
                            sys.stdout.flush()
                            time.sleep(.03)

        elif target_attribute == "STA":
            while True:
                    ask_sta_increase_size = ("\n" + "How many points do you wish to assign to stamina?" + "\n")
                    for i in ask_sta_increase_size:
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(.03)
                    try:
                        sta_increase = int(input("Increase it by: ").strip())
                        player_class_attr['STA'] = player_class_attr.get('STA') + sta_increase
                        os.system('clear')
                        print("Your class attributes:" + "\n")
                        for attr, value, in player_class_attr.items():
                            print('{} ---- {}'.format(attr, value))
                        available_attribute_points -= sta_increase
                        print("Remaining attribute points: ", available_attribute_points)
                        break
                    except ValueError:
                        for i in invalid_stat_increase_response:
                            sys.stdout.write(i)
                            sys.stdout.flush()
                            time.sleep(.03)
    os.system('clear')
    print("Your class attributes:" + "\n")
    for attr, value, in player_class_attr.items():
        print('{} ---- {}'.format(attr, value))
    used_all_attributes = ("\n" + "You used all of your available attribute points!" + "\n")
    for i in used_all_attributes:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.03)


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
