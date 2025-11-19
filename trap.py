import random

from player import Player


class Trap:
    def __init__(self, description: str, damage: int):
        self.description = description
        self.damage = damage

    def trigger(self, player: Player):
        print(f"You landed on {self.description} and lost {self.damage} HP!")
        player.health -= self.damage

AVAILABLE_TRAPS: list[tuple[str, int]] = [
    ("Spike Trap", 10),
    ("Fire Pit", 15),
    ("Bear Trap", 12),
    ("Poison Gas", 15)
]

def get_random_trap() -> Trap:
    description, damage = random.choice(AVAILABLE_TRAPS)
    return Trap(description, damage)