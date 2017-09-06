from movement import *


def create_board(levelMap, heroStats):
    interior_width = len(levelMap[0]) + len(heroStats[0])
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
    return game_board


def print_board(board):
    for n in board:
        print("".join(n))


def main():

    levelMap = generate_map("mapMaze.txt")
    heroStats = generate_map("mapTest.txt")
    board = create_board(levelMap, heroStats)
    print_board(board)


main()
