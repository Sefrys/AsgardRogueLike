import sys
import os


def display_menu():
    indent = 5
    offset = 2
    # to extract to external file
    menu_options = {1: "Start game",
                    2: "How-to-play",
                    3: "Hall of Fame",
                    4: "About screen",
                    5: "Exit game"}
    key_lenght = 1
    value_lenght = 0
    for i in menu_options.values():
        if int(len(i)) > value_lenght:
            value_lenght = int(len(i))

    dash_bar = key_lenght + value_lenght + offset

    print("\n"*3 + "{:>{width}}{:}".format("_"*dash_bar, "\n", width=(indent+value_lenght + offset)))
    for i in menu_options:
        print("{:>{width}}{:{w}}{:<}".format(i, ".", menu_options[i], width=indent, w=offset))
    print("{:>{width}}".format("_"*dash_bar, width=(indent+value_lenght + offset)))
    print("\n"*3)

def instructions():
    os.system("clear")
    print("\nUse WSAD keys to move. \n Enter combat by walking onto an enemy, marked by X.\n Good luck!")


def about_game():
    print("\n This game is about this and this made by Filip Hartman and Irek Żagan")
