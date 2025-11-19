from board import Board
from tile import *
import time


def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    board = Board()

    while True:
        # Roll dice and get tile that player lands on
        player.roll_dice()

        # If the player has reached the end of the board, they win!
        if player.board_position >= len(board.tiles):
            print(f"Congratulations {player.name}, you win!")
            return

        landed_tile = board.get_tile(player.board_position)

        # Perform action based on type of tile the player lands on
        landed_tile.on_land(player)
        time.sleep(1)
        input("Press any key to continue...")

if __name__ == '__main__':
    main()

