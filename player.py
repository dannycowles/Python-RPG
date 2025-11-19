from attack import Attack
import random

from item import Item, HealthPotion


class Player:
    max_health: int = 100
    board_position: int = 0

    def __init__(self, name: str):
        self.name = name
        self.health: int = 100
        self.attacks: list[Attack] = [
            Attack("Sword", 10),
            Attack("Bow", 8)
        ]
        self.items: list[Item] = [
            HealthPotion(50)
        ]

    def select_attack(self) -> Attack | None:
        while True:
            # Display attack options to the player
            print("\nYour attack options")
            for i, attack in enumerate(self.attacks, 1):
                print(f"{i} - {attack.name} : {attack.damage} DMG")
            print("0 - Back")

            choice = int(input("\nSelect an action: "))

            # Validates player input
            if 1 <= choice <= len(self.attacks):
                return self.attacks[choice - 1]
            elif choice == 0:
                return None
            else:
                print("Invalid action")

    def select_item(self) -> Item | None:
        while True:
            # Display item options to the player
            print("\nYour item options")
            for i, item in enumerate(self.items, 1):
                print(f"{i} - {item.name}")
            print("0 - Back")

            choice = int(input("\nSelect an action: "))

            # Validates player input
            if 1 <= choice <= len(self.items):
                return self.items[choice - 1]
            elif choice == 0:
                return None
            else:
                print("Invalid action")


    def roll_dice(self):
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}")
        self.board_position += roll
