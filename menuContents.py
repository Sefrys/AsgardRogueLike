import sys
import os


def instructions():
    '''Displays HowToPlay instructions.'''
    os.system("clear")
    print("\nUse WSAD keys to move. \n Enter combat by walking onto an enemy, marked by & symbol.\n Good luck!")


def about_game():
    '''Displays game credits'''
    print("\n This game is about this and this made by Filip Hartman and Irek Żagan")


def hall_of_fame():
    '''Displays highest scores'''
    print("\n In progress")


def exit_game():
    '''Gives the choice to exit the game from menu'''
    while True:
        exit_choice = input("Do you wish to exit the game? Y/N: ").upper()
        if exit_choice == "Y":
            exit()
        elif exit_choice == "N":
            break
        else:
            print("Invalid input. Try again")
