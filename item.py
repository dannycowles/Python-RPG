from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from player import Player

class Item(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def use(self, player: "Player"):
        pass


class HealthPotion(Item):
    def __init__(self, healing: int):
        super().__init__("Instant Health Potion")
        self.healing = healing

    def use(self, player: "Player"):
        print(f"You have been healed for {self.healing} HP")
        player.health = min(player.health + self.healing, player.max_health)
        pass