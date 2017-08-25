def display_menu_screen():
    indent = 5
    offset = 2
#to extract to external file
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

    print("{:>{width}}{:}".format(
        "_"*dash_bar, "\n", width=(indent+value_lenght + offset)))
    for i in menu_options:
        print("{:>{width}}{:{w}}{:<}".format(
                i, ".", menu_options[i], width=indent, w=offset))
    print("{:>{width}}".format(
        "_"*dash_bar, width=(indent+value_lenght + offset)))


def menu_choose():
        while True:
            try:
                choice_menu = int(input("What to you want to choose: "))
                if choice_menu == 1:
                    break
                elif choice_menu == 2:
                    break
                elif choice_menu == 3:
                    break
                elif choice_menu == 4:
                    break
                elif choice_menu == 5:
                    break
                else:
                    print("Number out of range")
                    continue
            except ValueError:
                print("Invalid input")

display_menu_screen()
menu_choose()
