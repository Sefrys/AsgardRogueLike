import sys
import os


def instructions():
    os.system("clear")
    print("\nUse WSAD keys to move. \n Enter combat by walking onto an enemy, marked by X.\n Good luck!")


def about_game():
    print("\n This game is about this and this made by Filip Hartman and Irek Żagan")


def hall_of_fame():
    print("\n In progress")

def exit_game():
    while True:
        exit_choice = input("Do you wish to exit the game? Y/N: ").upper()
        if exit_choice == "Y":
            exit()
        elif exit_choice == "N":
            break
        else:
            print("Invalid input. Try again")
