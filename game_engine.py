def ship_exists(coordinates: tuple, board: list[list]) -> bool:
    y, x = coordinates
    if board[y][x] is not None:
        return True
    return False

def attack(coordinates: tuple, board: list[list], battleships: dict[str, int]) -> bool:
    x, y = coordinates
    hit_success: bool = ship_exists((x, y), board)
    if hit_success:
        battleships[board[y][x]] -= 1
        board[y][x] = None
    return hit_success

def cli_coordinates_input() -> tuple:
    pass

def simple_game_loop():
    pass

if __name__ == "__main__":
    simple_game_loop()

