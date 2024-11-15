import components, game_engine, random

def print_board(board: list[list]) -> None:
    print(f"BOARD OF SIZE {len(board)}x{len(board[0])}")
    for y in range(len(board)):
        print(board[y])

board = components.initialise_board(4)
ships = components.create_battleships()
board = components.place_battleships(board, ships)

print_board(board)

# y_list = [0, 1, 2, 3]
# x_list = [0, 1, 2, 3]
# for x in x_list:
#     for y in y_list:
#         print(f"Y:{y}, X:{x} -> SHIP:{board[y][x]}")

print(ships)

game_engine.attack((0, 0), board, ships)

print(ships)

print_board(board)

