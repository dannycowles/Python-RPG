from enemies import *
from tile import *


class Board:
    def __init__(self):
        self.tiles : list[Tile] = [
            EnemyTile(Skeleton()),
            EmptyTile(),
            EnemyTile(Dragon()),
            EnemyTile(Zombie()),
            TrapTile(Trap("Spike Trap", 10)),
            EmptyTile()
        ]

    def get_tile(self, index: int) -> Tile:
        return self.tiles[index]