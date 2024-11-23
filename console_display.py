def display_mp_welcome() -> None:
    print("--------")
    print("Welcome to battleships game")
    print("You will be asked to enter the coordinates for your attack")
    print("You will then be told whether you got a hit or a miss")
    print("The AI will then take its turn, and you will be told whether it got a hit")
    print("--GOOD LUCK--")

def display_sp_welcome_message() -> None:
    print("Welcome to battleships game")

def display_player_win_msg() -> None:
    print("Player wins!")

def display_ai_win_msg() -> None:
    print("Computer wins!")

def display_player_hit(player_attack_coords: tuple, player_hit: bool) -> None:
    print(f"Your attack at {player_attack_coords} {"HIT" if player_hit else "MISS"}")

def display_ai_hit(ai_attack_coords: tuple, ai_hit: bool) -> None:
    print(f"AI attacked at {ai_attack_coords} and {"HIT" if ai_hit else "MISSED"}")

def display_sp_game_over() -> None:
    print("Game over, thank you for playing")