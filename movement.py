
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


def movement_hero(mapLevel, hero_symbol="@", wall_symbol="#",
                  entrance_symbol="D", path_symbol="."):
    x_hero = 1
    y_hero = 1
    hero_step = 1
    mapLevel[y_hero][x_hero] = hero_symbol
    while True:
        for i in mapLevel:
            print(*i)
        key = getch()

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


def main():
    mapLevel = generate_map()
    movement_hero(mapLevel)


if __name__ == "__main__":
    main()
