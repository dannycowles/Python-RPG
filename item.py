from abc import ABC, abstractmethod
import random
from typing import TYPE_CHECKING

from enemies import Enemy

if TYPE_CHECKING:
    from player import Player


class Item(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def use(self, player: "Player", enemy: Enemy = None):
        pass


class HealthPotion(Item):
    def __init__(self, healing: int = 50):
        super().__init__("Instant Health Potion")
        self.healing = healing

    def use(self, player: "Player", enemy: Enemy = None):
        print(f"You have been healed for {self.healing} HP")
        player.health = min(player.health + self.healing, player.max_health)

class DamagePotion(Item):
    def __init__(self, damage: int = 50):
        super().__init__("Damage Potion")
        self.damage = damage

    def use(self, player: "Player", enemy: Enemy = None):
        print(f"{enemy.name} has been hit for {self.damage} damage")
        enemy.health = max(0, enemy.health - self.damage)


# Registry of all available item classes
AVAILABLE_ITEMS: list[type[Item]] = [
    HealthPotion,
    DamagePotion
]

# Used when a player lands on an item tile, returns a random item from the registry
def get_random_item() -> Item:
    item_class = random.choice(AVAILABLE_ITEMS)
    return item_class()