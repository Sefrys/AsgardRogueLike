from gameBoard import *
import os

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def generate_map(level="mapTest.txt"):
    levelMap = []
    with open(level, "r") as mapFile:
        for line in mapFile:
            levelMap.append(list(line))
    return levelMap


def movement_hero(mapLevel, hero_symbol="@", wall_symbol="X",
                  entrance_symbol="D", path_symbol=" "):
    x_hero = 2
    y_hero = 14
    hero_step = 1
    mapLevel[y_hero][x_hero] = hero_symbol
    while True:
        for i in mapLevel:
            print(*i)
        key = getch()
        os.system('clear')
        if key == "q":
            break

        if key == "w":
            if (not mapLevel[y_hero - hero_step][x_hero] == wall_symbol and
               not mapLevel[y_hero - hero_step][x_hero] == entrance_symbol):
                mapLevel[y_hero][x_hero] = path_symbol
                y_hero -= hero_step

        if key == "s":
            if (not mapLevel[y_hero + hero_step][x_hero] == wall_symbol and
               not mapLevel[y_hero + hero_step][x_hero] == entrance_symbol):
                mapLevel[y_hero][x_hero] = path_symbol
                y_hero += hero_step

        if key == "a":
            if (not mapLevel[y_hero][x_hero - hero_step] == wall_symbol and
               not mapLevel[y_hero][x_hero - hero_step] == entrance_symbol):
                mapLevel[y_hero][x_hero] = path_symbol
                x_hero -= hero_step

        if key == "d":
            if (not mapLevel[y_hero][x_hero + hero_step] == wall_symbol and
               not mapLevel[y_hero][x_hero + hero_step] == entrance_symbol):
                mapLevel[y_hero][x_hero] = path_symbol
                x_hero += hero_step

        mapLevel[y_hero][x_hero] = hero_symbol


def movement_core():
    mapLevel = generate_map("mapMaze.txt")
    game_board = create_board(mapLevel)
    movement_hero(game_board)
