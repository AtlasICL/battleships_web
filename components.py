import json
import random

def get_board_size(board) -> int:
    board_size: int = len(board)
    assert board_size > 0, "BOARD LEN 0"
    return board_size

def print_board(board: list[list[str | None]]) -> None:
    print(f"BOARD OF SIZE {len(board)}x{len(board[0])}")
    for y in range(len(board)):
        print(f"{[char_ship_type(board[y][x]) for x in range(len(board[y]))]}")

def initialise_board(size: int =10) -> list[list]:
    empty_board = [[None for _ in range(size)] for _ in range(size)]
    return empty_board

def create_battleships(filename: str ="battleships.txt") -> dict[str, int]:
    battleships: dict = {} 
    with open(filename, 'r') as ifstream:
        for line in ifstream:
            ship_name, ship_size = line.strip().split(":")
            battleships[ship_name] = int(ship_size)
    return battleships

def place_battleships(board: list[list], ships: dict[str, int], algorithm="simple") -> list[list]:
    if algorithm == "simple":
        assert len(ships) <= len(board), "TOO MANY SHIPS"
        for ship_size in ships.values():
            assert ship_size <= len(board), "SHIP TOO BIG"
        row: int = 0
        for ship_name, ship_size in ships.items():
            for x in range(ship_size):
                board[row][x] = ship_name
            row += 1
        return board
    elif algorithm == "custom":
        board = make_custom_board("placement.json")
        return board
    elif algorithm == "random":
        board = make_random_board(ships)
        return board

def load_placements_from_json(filename):
    with open(filename, 'r') as ifstream:
        placement_data = json.load(ifstream)
    return placement_data

def make_custom_board(filename) -> list[list[str | None]]:
    placement_data = load_placements_from_json(filename)
    board = initialise_board()
    ship_sizes = create_battleships()
    
    for ship, placement in placement_data.items():
        start_y = int(placement[1])
        start_x = int(placement[0])
        y_iter = 0
        x_iter = 0
        if placement[2] == 'h':
            x_iter = 1
        if placement[2] == 'v':
            y_iter = 1
        for i in range(ship_sizes[ship]):
            board[start_y + i * y_iter][start_x + i * x_iter] = ship
    return board

def make_custom_board_from_json(user_ship_placement) -> list[list[str | None]]:
    board = initialise_board()
    ship_sizes = create_battleships()
    for ship, placement in user_ship_placement.items():
        start_y = int(placement[1])
        start_x = int(placement[0])
        y_iter = 0
        x_iter = 0
        if placement[2] == 'h':
            x_iter = 1
        if placement[2] == 'v':
            y_iter = 1
        for i in range(ship_sizes[ship]):
            board[start_y + i * y_iter][start_x + i * x_iter] = ship
    return board


def make_random_board() -> list[list[str | None]]:
    board = initialise_board()
    ship_sizes = create_battleships()
    ships_to_place = []
    with open("placement.json", 'r') as ifstream:
        ships_placed_by_player = json.load(ifstream)
        ships_to_place = list(ships_placed_by_player.keys())

    for ship_name in ships_to_place:
        ship_length = ship_sizes[ship_name]
        place_ship(board, ship_length, ship_name)

    return board

def place_ship(board, ship_length, ship_name) -> None:
    placed: bool = False
    MAX_ATTEMPTS: int = 100
    attempt_counter: int = 0
    while not placed and attempt_counter < MAX_ATTEMPTS:
        attempt_counter += 1
        start_y = random.randint(0, len(board)-1)
        start_x = random.randint(0, len(board)-1)
        direction = random.choice(['h', 'v'])
        if can_place_ship(board, ship_length, start_x, start_y, direction):
            if direction == 'h':
                for i in range(ship_length):
                    board[start_y][start_x + i] = ship_name
            elif direction == 'v':
                for i in range(ship_length):
                    board[start_y + i][start_x] = ship_name
            placed = True
            attempt_counter = 0

def can_place_ship(board: list[list], ship_length, start_x, start_y, direction):
    if direction == 'h':
        if start_x + ship_length > len(board):
            return False
        for i in range(ship_length):
            if board[start_y][start_x + i] is not None:
                return False
    elif direction == 'v':
        if start_y + ship_length > len(board):
            return False
        for i in range(ship_length):
            if board[start_y + i][start_x] is not None:
                return False
    return True

def char_ship_type(ship_in) -> str:
    """
    This function is for more readable printing of the board.
    Instead of printing out "Cruiser", it outputs "C" instead,
    allowing for a "square" printing of the board. It also returns '-'
    for a None value. 
    """
    abbreviations = {
        'Aircraft_Carrier': 'A',
        'Battleship': 'B',
        'Cruiser': 'C',
        'Submarine': 'S',
        'Destroyer': 'D',
        None: '-'
    }
    return abbreviations[ship_in]


