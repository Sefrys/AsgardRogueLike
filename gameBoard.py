def create_board(levelMap, board_symbol="#"):
    interior_width = len(levelMap[0])
    interior_height = len(levelMap)
    boundary = 2
    width = int(interior_width) + boundary
    height = int(interior_height) + boundary
    game_board = [[" "] * width for row in range(height)]

    for row in [0, -1]:
        for col in range(int(width)):
            game_board[row].insert(col, board_symbol)

    for row in range(1, int(height)-1):
        game_board[row][0] = board_symbol
        game_board[row][-1] = board_symbol

    for row in range(1, interior_width - 1):
        for col in range(1, interior_height - 1):
            game_board[col][row] = levelMap[col-1][row-1]
    return game_board


def main():
    pass


main()
