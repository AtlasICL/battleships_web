import random
import json

import components
import game_engine

players = {}

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


def initialise_players_dict(placements_filepath: str ="placement.json") -> dict[str, dict]:
    user_board = components.make_custom_board(placements_filepath)
    player_ships = components.get_player_ships(placements_filepath)

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


def main():
    ai_opponent_game_loop()
    print(players)

if __name__ == "__main__":
    main()