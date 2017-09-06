from movement import *


def create_board(levelMap):
    interior_width = len(levelMap[0])
    interior_height = len(levelMap)
    boundary = 2
    width = int(interior_width) + boundary
    height = int(interior_height) + boundary
    game_board = [[" "] * width for row in range(height)]

    for row in [0, -1]:
        for col in range(int(width)):
            game_board[row].insert(col, "X")

    for row in range(1, int(height)-1):
        game_board[row][0] = "X"
        game_board[row][-1] = "X"

    for row in range(1, interior_width - 1):
        for col in range(1, interior_height - 1):
            game_board[col][row] = levelMap[col-1][row-1]
    return game_board


def print_board(board):
    for n in board:
        print("".join(n))


def main():

    levelMap = generate_map("mapMaze.txt")
    heroStats = generate_map("mapTest.txt")
    board = create_board(levelMap)


    print_board(board)


main()
