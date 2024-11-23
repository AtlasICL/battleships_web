import components

def ship_exists_at_coords(coordinates: tuple, board: list[list[str | None]]) -> bool:
    x, y = coordinates
    if board[y][x] is not None:
        return True
    return False

def display_welcome_message() -> None:
    print("Welcome to Battleships game")

def display_hit_miss_msg(hit_success: bool) -> None:
    print("HIT!" if hit_success else "MISS!")

def attack(coordinates: tuple, board: list[list[str | None]], battleships: dict[str, int]) -> bool:
    x, y = coordinates
    hit_success: bool = ship_exists_at_coords((x, y), board)
    if hit_success:
        battleships[board[y][x]] -= 1
        board[y][x] = None
    return hit_success

def cli_coordinates_input() -> tuple:
    x = int(input("Please enter *X* coordinate --> "))
    y = int(input("Please enter *Y* coordinate --> "))
    return (x, y)

def is_all_ships_sunk(ships: dict[str, int]) -> bool:
    all_nil = True
    for ship_length in ships.values():
        if ship_length > 0:
            all_nil = False
    return all_nil


def simple_game_loop() -> None:
    display_welcome_message()
    board = components.initialise_board()
    ships = components.create_battleships()
    board = components.place_battleships(board, ships, "custom")

    all_ships_sunk: bool = is_all_ships_sunk(ships)
    
    while not all_ships_sunk:
        components.print_board(board)
        (x, y) = cli_coordinates_input()
        attack((x, y), board, ships)
        all_ships_sunk = is_all_ships_sunk(ships)

    print("game over")
        
    

if __name__ == "__main__":
    simple_game_loop()

