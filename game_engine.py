import components
import debug

def ship_exists(coordinates: tuple, board: list[list]) -> bool:
    y, x = coordinates
    if board[y][x] is not None:
        return True
    return False

def display_welcome_message() -> None:
    print("Welcome to Battleships game")

def attack(coordinates: tuple, board: list[list], battleships: dict[str, int]) -> bool:
    x, y = coordinates
    hit_success: bool = ship_exists((x, y), board)
    if hit_success:
        battleships[board[y][x]] -= 1
        board[y][x] = None
    return hit_success

def cli_coordinates_input() -> tuple:
    x = int(input("Please enter x coordinate --> "))
    y = int(input("Please enter y coordinate --> "))
    return (x, y)

def simple_game_loop():
    display_welcome_message()
    board = components.initialise_board(5)
    ships = components.create_battleships()
    board = components.place_battleships(board, ships)
    while True:
        debug.print_board(board)
        (x, y) = cli_coordinates_input()
        attack((x, y), board, ships)
    

if __name__ == "__main__":
    simple_game_loop()

