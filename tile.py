from abc import ABC

from enemies import Enemy
from trap import Trap


class Tile(ABC):
    pass

class EmptyTile(Tile):
    pass

class EnemyTile(Tile):
    def __init__(self, enemy: Enemy):
        self.enemy = enemy

class ItemTile(Tile):
    pass

class TrapTile(Tile):
    def __init__(self, trap: Trap):
        self.trap = trap