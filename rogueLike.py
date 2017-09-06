import os
import sys
from introScreen import *
from menuContents import *
from displayMenu import *
from characterCreation import *
from movementMapDisplay import *
from combatEngine import *


# Print story of game, wait for enter input/wait some time
# to call display_menu_screen.
def display_intro_screen():
    '''Displays the introduction screen'''
    introduction_title()


# Display menu choices
def display_menu_screen():
    '''Displays the menu screen and asks for sub-menu choice'''
    display_menu()
    while True:
        try:
            choice_menu = int(input("What do you want to choose: "))
            os.system("clear")
            if choice_menu == 1:
                menu_new_game()
                break
            elif choice_menu == 2:
                instructions()
                display_menu()
            elif choice_menu == 3:
                hall_of_fame()
                display_menu()
            elif choice_menu == 4:
                about_game()
                display_menu()
            elif choice_menu == 5:
                exit_game()
                display_menu()
            else:
                print("Number out of range")
        except ValueError:
            print("Invalid menu choice input")


# Initiates new game sequence; character creation
def menu_new_game():
    '''Starts a new game'''
    os.system("clear")
    create_character()
    movement_core()


def combat_encounter():
    '''Runs the combat engine upon combat encounter'''
    combat_core()


def main():
    '''Initializes the game content'''
    display_intro_screen()
    display_menu_screen()


if __name__ == "__main__":
    main()
