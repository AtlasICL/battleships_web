# from utils import print_board
# from game_engine import ship_exists

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

def place_battleships(board: list[list], ships: dict[str, int], algorithm = "simple") -> list[list]:
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

    
def main():
    board = initialise_board(10)
    ships = create_battleships()
    board = place_battleships(board, ships)

if __name__ == "__main__":
    main()


