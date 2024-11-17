import json

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
            # NOTE: board[row] could raise index error
            # but I think here we are safe becase of the assert above
        return board
    elif algorithm == "custom":
        board = make_custom_board("placement.json")
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

def get_player_ships(filepath):
    output: dict[str, int] = {}
    with open(filepath, 'r') as ifstream:
        placement_data = json.load(ifstream)
        for ship_name in placement_data:
            output[ship_name] = SHIP_SIZES[ship_name]
    return output
    
def main():
    # shouldn't be running this file
    return

if __name__ == "__main__":
    main()


