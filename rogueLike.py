import os
import sys
import datetime
from introScreen import *
from menuContents import *
from displayMenu import *
from characterCreation import *
from movementMapDisplay import *
from combatEngine import *
from highscore import *


def fetch_current_time():
    current_time = datetime.datetime.now()
    return(current_time)


# Print story of game, wait for enter input/wait some time
# to call display_menu_screen
def display_intro_screen():
    '''Displays the introduction screen'''
    introduction_title()


# Display menu choices
def display_menu_screen():
    '''Displays the menu screen and asks for sub-menu choice'''
    display_menu()
    while True:
        choices_for_menu = [1, 2, 3, 4, 5]
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
            elif choice_menu not in choices_for_menu:
                display_menu()
                print("Number out of range")
        except ValueError:
            print("Invalid menu choice input")
            os.system('clear')
            display_menu()


def fetch_play_time(start_time, stop_time):
    time_diff = stop_time - start_time
    time_diff = str(time_diff).strip(":")
    time_diff = time_diff[2:7]
    time_minutes_elapsed = time_diff[:2]
    time_seconds_elasped = time_diff[3:]
    time_elapsed = int(time_minutes_elapsed)*60 + int(time_seconds_elasped)
    with open('exportedNameClassHP.csv', 'a') as highscore_file:
        highscore_file.write(str(time_elapsed))
    highscore_core()


# Initiates new game sequence; character creation
def menu_new_game():
    '''Starts a new game'''
    os.system("clear")
    create_character()
    start_time = fetch_current_time()
    movement_core(start_time)


def game_end(start_time):
    stop_time = fetch_current_time()
    fetch_play_time(start_time, stop_time)
    exit()


def combat_encounter():
    '''Runs the combat engine upon combat encounter'''
    combat_core()


def main():
    '''Initializes the game content'''
    display_intro_screen()
    display_menu_screen()


if __name__ == "__main__":
    main()
