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
    list_of_classes = ["warrior", "mage", "rogue"]

    ask_name = "Welcome!" + "\n" + "What is your name, traveler?" + "\n"
    for i in ask_name:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.05)

    while True:
        player_name = input("My name is: ").title()
        if not all(x.isalpha() for x in player_name):
            answer_invalid_name = "I'm sorry, you have to tell me your true name."
            for i in answer_wrong_name:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.05)
        else:
            answer_valid_name = ("Very well, nice to meet you, " + player_name + "." + "\n"
                                 + "Now, are you a warrior, a mage or a rogue?" + "\n")
            for i in answer_valid_name:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.05)
            break

    while True:
        player_class = input("I am a: ").lower()
        if player_class not in list_of_classes:
            answer_invalid_class = "Surely you jest, you must be either a warrior, a mage or a rogue!"
            for i in answer_invalid_class:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.05)
        else:
            answer_valid_class = ("A " + player_class + "? Good. Let's see what you are capable of then!" + "\n")
            for i in answer_valid_class:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.05)
            break




# initiates game fucntions
def game_core():
    create_character()


def main():
    game_core()


main()
