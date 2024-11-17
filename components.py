import json
import random

SHIP_SIZES = {
    "Aircraft_Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}

def char_ship_type(ship_in) -> str:
    abbreviations = {
        'Aircraft_Carrier': 'A',
        'Battleship': 'B',
        'Cruiser': 'C',
        'Submarine': 'S',
        'Destroyer': 'D',
        None: '-'
    }
    return abbreviations[ship_in]

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
    
    for ship, placement in placement_data.items():
        start_y = int(placement[1])
        start_x = int(placement[0])
        y_iter = 0
        x_iter = 0
        if placement[2] == 'h':
            x_iter = 1
        if placement[2] == 'v':
            y_iter = 1
        for i in range(SHIP_SIZES[ship]):
            board[start_y + i * y_iter][start_x + i * x_iter] = ship
    return board

def make_random_board() -> list[list[str | None]]:
    board = initialise_board()
    ships_to_place = []
    with open("placement.json", 'r') as ifstream:
        ships_placed_by_player = json.load(ifstream)
        ships_to_place = list(ships_placed_by_player.keys())

    for ship_name in ships_to_place:
        ship_length = SHIP_SIZES[ship_name]
        place_ship(board, ship_length, ship_name)

    print_board(board)
    return board

def place_ship(board, ship_length, ship_name) -> None:
    placed = False
    while not placed:
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

def get_player_ships(filepath):
    output: dict[str, int] = {}
    with open(filepath, 'r') as ifstream:
        placement_data = json.load(ifstream)
        for ship_name in placement_data:
            output[ship_name] = SHIP_SIZES[ship_name]
    return output
    
def main():
    # shouldn't be running this file
    make_random_board()
    pass

if __name__ == "__main__":
    main()


