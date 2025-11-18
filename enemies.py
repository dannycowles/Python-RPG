from attack import Attack
from abc import ABC
import random
import time

class Enemy(ABC):
    def __init__(self, name: str, health: float, attacks: list[Attack]):
        self.name = name
        self.health = health
        self.attacks = attacks

    def attack(self):
        # Attack message
        print(f'{self.name} attacks.')
        time.sleep(1)

        # Select random attack from enemy and display info to user
        selected_attack = random.choice(self.attacks)
        print(f'{self.name} uses {selected_attack.name} for {selected_attack.damage} damage!')

class Skeleton(Enemy):
    name = "Skeleton"
    health = 100
    attacks = [
        Attack("Slash", 5),
        Attack("Bone Throw", 4),
        Attack("Chomp", 6)
    ]

    def __init__(self):
        super().__init__(self.name, self.health, self.attacks)


class Dragon(Enemy):
    name = "Dragon"
    health = 150
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


enemies: list[Enemy] = [Skeleton(), Dragon(), Zombie()]

for enemy in enemies:
    enemy.attack()
    print()