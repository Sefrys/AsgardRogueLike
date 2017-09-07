import sys
import os
from highscore import *


def instructions():
    '''Displays HowToPlay instructions.'''
    os.system("clear")
    print("\nUse WSAD keys to move. \n Enter combat by walking onto an enemy,\
          marked by & or ☼ symbol.\n The boss is a large '%' construction. \
          \nGood luck!")


def about_game():
    '''Displays game credits'''
    print("\n This game is about trying to kill the final boss and pass the checkpoint. \
          \n made by Filip Hartman and Irek Żagan")


def hall_of_fame():
    '''Displays highest scores'''
    display_highscore()


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
