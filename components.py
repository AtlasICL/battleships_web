from utils import print_board

def initialise_board(size: int =10) -> list[list]:
    empty_board = [[None for _ in range(size)] for _ in range(size)]
    return empty_board

def create_battleships(filename: str ="battleships.txt") -> dict[str, int]:
    battleships: dict = {} 
    with open(filename, 'r') as istream:
        for line in istream:
            ship_name, ship_size = line.strip().split(":")
            battleships[ship_name] = int(ship_size)
    return battleships

def place_battleships(board: list[list], ships: dict[str, int]) -> list[list]:
    pass
    

def main():
    board: list[list] = initialise_board()
    ships: dict[str: int] = create_battleships()
    board = place_battleships(board, ships)
    print_board(board)

if __name__ == "__main__":
    main()


