import os


# Receives input as width
def get_dimension_width():
    while True:
        try:
            width = int(input("Please enter desired width:   "))
            break
        except ValueError:
            print("Please enter a valid integer for width:   ")
    return(width)


# Receives input as height
def get_dimension_height():
    while True:
        try:
            height = int(input("Please enter desired height:  "))
            break
        except ValueError:
            print("Please enter a valid integer for height:  ")
    return(height)


def create_board(width, height):
    counter = 0
    board = []
    board.append(["X"]*width)

# Creates multiple height list of list elements depending on height value
    for x in range(height):
        board.append([" "]*width)
        counter += 1
        board[counter][0] = "X"
        board[counter][-1] = "X"

    board.append(["X"]*width)
    return(board)


def print_board(board, height):
    counter = 1
    print("\n"*2)
    print("".join(board[0]))

# Prints the heigh columns of the map without bottom and top borders
    for x in range(height - 1):
        print("".join(board[counter]))
        counter += 1
    print("".join(board[-1]))
    print("\n"*2)


def main():

    width = get_dimension_width()
    height = get_dimension_height()
    board = create_board(width, height)
    os.system("clear")
    print_board(board, height)


main()
