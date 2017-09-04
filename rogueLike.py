import os
import sys
from characterCreation import *
from menu import *

# Print story of game, wait for enter input/wait some time
# to call display_menu_screen.
def display_intro_screen():
    pass


# Display menu choices
def display_menu_screen():
    run_menu()


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


# Initiates new game sequence; character creation
def menu_new_game():
    os.system("clear")
    create_character()


# initiates game fucntions
def game_core():
    display_menu_screen()
    create_character()


def main():
    game_core()


main()
