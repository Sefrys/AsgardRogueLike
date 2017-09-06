def display_menu():
    '''Display menu options in a stylized format'''
    indent = 5
    offset = 2
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
