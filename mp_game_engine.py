import random

import components, game_engine

players = {}

def get_board_size(board) -> int:
    board_size: int = len(board)
    assert board_size > 0, "BOARD LEN 0"
    return board_size

def display_mp_welcome() -> None:
    print("--------")
    print("Welcome to battleships game")
    print("You will be asked to enter the coordinates for your attack")
    print("You will then be told whether you got a hit or a miss")
    print("The AI will then take its turn, and you will be told whether it got a hit")
    print("--GOOD LUCK--")

def display_player_win_msg() -> None:
    print("Player wins!")

def display_ai_win_msg() -> None:
    print("Computer wins!")

def display_player_hit(player_attack_coords: tuple, player_hit: bool) -> None:
    print(f"Your attack at {player_attack_coords} {"HIT" if player_hit else "MISS"}")

def display_ai_hit(ai_attack_coords: tuple, ai_hit: bool) -> None:
    print(f"AI attacked at {ai_attack_coords} and {"HIT" if ai_hit else "MISSED"}")

def generate_attack(board) -> tuple:
    board_size: int = get_board_size(board)
    attack_x: int = random.randint(0, board_size-1)
    attack_y: int = random.randint(0, board_size-1)
    return attack_x, attack_y


def initialise_players_dict(placements_filepath: str ="placement.json") -> dict[str, dict]:
    user_board = components.make_custom_board(placements_filepath)
    player_ships = components.create_battleships()

    ai_opponent_board = components.make_random_board()

    players = {
        "user": {
            "board": user_board,
            "ships": player_ships
        },
        "ai": {
            "board": ai_opponent_board,
            "ships": player_ships
        }
    }
    return players

def ai_opponent_game_loop():

    global players
    players = initialise_players_dict()

    display_mp_welcome()

    all_user_ships_sunk = False
    all_ai_ships_sunk = False

    while not all_user_ships_sunk and not all_ai_ships_sunk:

        (x, y) = game_engine.cli_coordinates_input()
        player_hit = game_engine.attack((x, y), players["ai"]["board"], players["ai"]["ships"])
        display_player_hit((x, y), player_hit)

        (x, y) = generate_attack(players["user"]["board"])
        ai_hit = game_engine.attack((x, y), players["user"]["board"], players["user"]["ships"])
        display_ai_hit((x, y), ai_hit)

        print("YOUR BOARD STATE:")
        components.print_board(players["user"]["board"])

        all_user_ships_sunk = game_engine.is_all_ships_sunk(players["user"]["ships"])
        all_ai_ships_sunk = game_engine.is_all_ships_sunk(players["ai"]["ships"])

    if all_user_ships_sunk:
        display_ai_win_msg()
    elif all_ai_ships_sunk:
        display_player_win_msg()

    

def main():
    ai_opponent_game_loop()

if __name__ == "__main__":
    main()