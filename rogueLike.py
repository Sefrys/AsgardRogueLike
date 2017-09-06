import os
import sys
from characterCreation import *
from displayMenu import *
from menu_contents import *
from introScreen import *
from combatEngine import *


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
                break
            elif choice_menu == 2:
                os.system("clear")
                instructions()
                display_menu()
            elif choice_menu == 3:
                os.system("clear")
                hall_of_fame()
                display_menu()
            elif choice_menu == 4:
                os.system("clear")
                about_game()
                display_menu()
            elif choice_menu == 5:
                exit_game()
                os.system("clear")
                display_menu()
            else:
                print("Number out of range")
        except ValueError:
            print("Invalid input")


# Initiates new game sequence; character creation
def menu_new_game():
    os.system("clear")
    create_character()
    combat_encounter()


def combat_encounter():
    combat_core()


# initiates game fucntions
def game_core():
    display_intro_screen()
    display_menu_screen()


def main():
    game_core()


main()
