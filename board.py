from tile import *


class Board:
    def __init__(self):
        self.tiles : list[Tile] = [
            EmptyTile(),
            ItemTile(),
            EnemyTile(),
            EmptyTile(),
            TrapTile(),
            EnemyTile(),
            EnemyTile(),
            ItemTile(),
            EnemyTile(),
            ItemTile(),
            EnemyTile(),
            EnemyTile(),
            TrapTile(),
            EnemyTile(),
            EmptyTile()
        ]

    def get_tile(self, index: int) -> Tile:
        return self.tiles[index]