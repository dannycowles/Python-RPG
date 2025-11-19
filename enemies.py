from attack import Attack
from abc import ABC
import random
import time

class Enemy(ABC):
    def __init__(self, name: str, health: int, attacks: list[Attack]):
        self.name = name
        self.health = health
        self.max_health = health
        self.attacks = attacks

    def select_attack(self) -> Attack:
        # Attack message
        print(f"{self.name}'s turn.")
        time.sleep(1)
        selected_attack = random.choice(self.attacks)
        return selected_attack

class Skeleton(Enemy):
    name = "Skeleton"
    health = 75
    attacks = [
        Attack("Slash", 5),
        Attack("Bone Throw", 4),
        Attack("Chomp", 6)
    ]

    def __init__(self):
        super().__init__(self.name, self.health, self.attacks)


class Dragon(Enemy):
    name = "Dragon"
    health = 100
    attacks = [
        Attack("Fire Breath", 8),
        Attack("Tail Swipe", 6),
        Attack("Bite", 10)
    ]

    def __init__(self):
        super().__init__(self.name, self.health, self.attacks)


class Zombie(Enemy):
    name = "Zombie"
    health = 75
    attacks = [
        Attack("Bite", 4),
        Attack("Grab", 3)
    ]

    def __init__(self):
        super().__init__(self.name, self.health, self.attacks)


# Registry of all available enemy class types
AVAILABLE_ENEMIES: list[type[Enemy]] = [
    Skeleton,
    Dragon,
    Zombie
]

# Used when player lands on an enemy tile, retrieves a random enemy
def get_random_enemy() -> Enemy:
    enemy = random.choice(AVAILABLE_ENEMIES)
    return enemy()
