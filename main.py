import random

# Rolls a six sided dice
def roll_dice() -> int:
    return random.randint(1,6)


def main():
    while True:
        roll = roll_dice()
        print(f"You rolled a {roll}!")


if __name__ == '__main__':
    main()

