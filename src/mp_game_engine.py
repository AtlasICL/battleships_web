import random

players = {
    "Emre": {
        "board": [[None, None], [None, None]],
        "ships": {"s1": 0, "s2": 0}
    },
    "Julia": {
        "board": [['s1', 's1'], ['s2', None]],
        "ships": {"s1": 2, "s2": 1}
    }
}

# this function assumes that board size for the first player
# is the universal board size
def get_board_size() -> int:
    assert len(players) > 0, "EMPTY PLAYER LIST"
    first_player = next(iter(players))
    board_size: int = len(players[first_player]["board"])
    assert board_size > 0, "BOARD LEN 0"
    return board_size

# TODO: implement this?
def initialise_players_dict():
    pass

def display_mp_welcome() -> None:
    print("Welcome to battleships game")

def generate_attack() -> tuple:
    board_size: int = get_board_size()
    attack_x: int = random.randint(0, board_size-1)
    attack_y: int = random.randint(0, board_size-1)
    return (attack_x, attack_y)

def ai_opponent_game_loop():
    display_mp_welcome()
    
    

def main():
    a, b = generate_attack()
    print(a, b)

if __name__ == "__main__":
    main()