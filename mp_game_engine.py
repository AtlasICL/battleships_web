import random
import json

import components
import game_engine

players = {}

SHIP_SIZES = {
    "Aircraft_Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}

# we assume the board is always square
def get_board_size() -> int:
    assert len(players) > 0, "EMPTY PLAYER LIST"
    first_player = next(iter(players))
    board_size: int = len(players[first_player]["board"])
    assert board_size > 0, "BOARD LEN 0"
    return board_size

def display_mp_welcome() -> None:
    print("Welcome to battleships game")

def generate_attack() -> tuple:
    board_size: int = get_board_size()
    attack_x: int = random.randint(0, board_size-1)
    attack_y: int = random.randint(0, board_size-1)
    return (attack_x, attack_y)

def load_placements_from_json(filename):
    with open(filename, 'r') as ifstream:
        placement_data = json.load(ifstream)
    return placement_data

def make_custom_board(filename) -> list[list[str | None]]:
    placement_data = load_placements_from_json(filename)
    board = components.initialise_board()
    
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

def initialise_players_dict(placements_filepath: str ="placement.json") -> dict[str, dict]:
    user_board = make_custom_board(placements_filepath)
    player_ships = get_player_ships(placements_filepath)

    players = {
        "user": {
            "board": user_board,
            "ships": player_ships
        },
        "ai": {
            "board": [],
            "ships": {}
        }
    }
    
    return players


def ai_opponent_game_loop():
    display_mp_welcome()
    global players
    players = initialise_players_dict()
    # print(players)



ai_opponent_game_loop()

print(players)

# if __name__ == "__main__":
#     main()