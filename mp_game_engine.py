import random

import components, game_engine, console_display

players = {}

def generate_pairs(n: int) -> list[tuple]:
    return [(i, j) for i in range(n) for j in range(n)]

def get_possible_attacks(board: list[list[str | None]]) -> list[tuple]:
    board_size: int = len(board)
    return generate_pairs(board_size)

possible_ai_attacks: list[tuple]

def generate_attack() -> tuple:
    global possible_ai_attacks
    ai_attack = random.choice(possible_ai_attacks)
    possible_ai_attacks.remove(ai_attack)
    return ai_attack

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
    global possible_ai_attacks

    players = initialise_players_dict()

    possible_ai_attacks = get_possible_attacks(players["user"]["board"])

    console_display.display_mp_welcome()

    all_user_ships_sunk = False
    all_ai_ships_sunk = False

    while not all_user_ships_sunk and not all_ai_ships_sunk:

        (x, y) = game_engine.cli_coordinates_input()
        player_hit = game_engine.attack((x, y), players["ai"]["board"], players["ai"]["ships"])
        console_display.display_player_hit((x, y), player_hit)

        (x, y) = generate_attack(players["user"]["board"])
        ai_hit = game_engine.attack((x, y), players["user"]["board"], players["user"]["ships"])
        console_display.display_ai_hit((x, y), ai_hit)

        print("YOUR BOARD STATE:")
        components.print_board(players["user"]["board"])

        all_user_ships_sunk = game_engine.is_all_ships_sunk(players["user"]["ships"])
        all_ai_ships_sunk = game_engine.is_all_ships_sunk(players["ai"]["ships"])

    if all_user_ships_sunk:
        console_display.display_ai_win_msg()
    elif all_ai_ships_sunk:
        console_display.display_player_win_msg()

def main():
    ai_opponent_game_loop()

if __name__ == "__main__":
    main()