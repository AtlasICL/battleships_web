import random

def generate_pairs(n: int) -> list[tuple]:
    return [(i, j) for i in range(n) for j in range(n)]

class AIAttacker:
    def __init__(self, board_size: int):
        self.possible_attacks: list[tuple] = generate_pairs(board_size)

    def get_attack(self):
        attack = random.choice(self.possible_attacks)
        self.possible_attacks.remove(attack)
        return attack
    