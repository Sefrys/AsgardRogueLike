import os
import sys
from characterCreation import *
from menu import *
from introScreen import introduction_title


# Print story of game, wait for enter input/wait some time
# to call display_menu_screen.
def display_intro_screen():
    introduction_title()


# Display menu choices
def display_menu_screen():
    display_menu()
    while True:
        try:
            choice_menu = int(input("What do you want to choose: "))
            if choice_menu == 1:
                menu_new_game()
            elif choice_menu == 2:
                break
            elif choice_menu == 3:
                break
            elif choice_menu == 4:
                break
            elif choice_menu == 5:
                break
            else:
                print("Number out of range")
        except ValueError:
            print("Invalid input")

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
    display_intro_screen()
    display_menu_screen()


def main():
    game_core()


main()
