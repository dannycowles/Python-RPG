from board import Board
from player import Player
from tile import *
from battle import *


def main():
    # Game loop testing
    player_name = input("Enter your name: ")
    player = Player(player_name)
    board = Board()

    # Roll dice and get tile that player lands on
    player.roll_dice()
    landed_tile = board.get_tile(player.board_position)

    # Perform action based on tile landed on
    match landed_tile:
        case EnemyTile():
            battle(player, landed_tile.enemy)
        # case TrapTile():
        #     print("trap tile")
        # case ItemTile():
        #     print("item tile")
        # case EmptyTile():
        #     print("You landed on an empty tile, you are safe!")


if __name__ == '__main__':
    main()

