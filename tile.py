from abc import ABC, abstractmethod

from enemies import get_random_enemy
from trap import get_random_trap
from item import get_random_item
from player import Player
from battle import battle


class Tile(ABC):
    @abstractmethod
    def on_land(self, player: Player):
        pass

class EmptyTile(Tile):
    def on_land(self, player: Player):
        print("You landed on an empty tile, you are safe!")

class EnemyTile(Tile):
    def __init__(self):
        self.enemy = get_random_enemy()

    def on_land(self, player: Player):
        battle_result = battle(player, self.enemy)
        if not battle_result:
            print(f"Sorry {player.name}, you lose...")
            return

class ItemTile(Tile):
    def __init__(self):
        self.item = get_random_item()

    def on_land(self, player: Player):
        player.pickup_item(self.item)

class TrapTile(Tile):
    def __init__(self):
        self.trap = get_random_trap()

    def on_land(self, player: Player):
        self.trap.trigger(player)