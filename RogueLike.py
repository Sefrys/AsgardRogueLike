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
                                 + "Now, are you a warrior, a mage or a rogue?" + "\n")
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
            answer_invalid_class = ("Surely you jest, you must be either a warrior, a mage or a rogue!" + "\n")
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
    # class attributes
    warrior_atr = {'STR': 17,
                   'CON': 19,
                   'DEX': 6,
                   'INT': 7, }

    rogue_atr = {'STR': 9,
                 'CON': 15,
                 'DEX': 21,
                 'INT': 9, }

    mage_atr = {'STR': 5,
                'CON': 13,
                'DEX': 12,
                'INT': 18, }

    print("Your " + player_class + " class attributes:" + "\n")
    if player_class == "warrior":
        for atr, value, in warrior_atr.items():
            print('{} ---- {}'.format(atr, value))
    elif player_class == "rogue":
        for atr, value, in rogue_atr.items():
            print('{} ---- {}'.format(atr, value))
    else:
        for atr, value, in mage_atr.items():
            print('{} ---- {}'.format(atr, value))

    time.sleep(1.25)
    ask_attribute_distribution = ("\n" + "Now that we see what you can do, let's improve your attributes a little."
                                  + "\n" + "I can give you at most fifteen points to spend improving your stats."
                                  + "\n" + "So choose wisely!" + "\n")
    for i in ask_attribute_distribution:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.03)


# initiates game fucntions
def game_core():
    create_character()


def main():
    game_core()


main()
