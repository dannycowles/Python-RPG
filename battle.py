from enemies import Enemy
from item import DamagePotion
from player import Player


def battle(player: Player, enemy: Enemy) -> bool:
    """
    This function simulates a battle sequence between a player and an enemy

    :param player:
    :param enemy:
    :return: True if player wins, False otherwise
    """

    print(f"A {enemy.name} approaches from the shadows...")

    while True:
        # Displays player and enemy health
        print(f"\n{enemy.name}")
        print(f"{enemy.health}/{enemy.max_health} HP")

        print(f"\n{player.name}")
        print(f"{player.health}/{player.max_health} HP")

        # Player's turn
        while True:
            print("""
It's your turn.
1 - Attack
2 - Use Item
            """)

            choice = int(input("Select action: "))
            match choice:
                case 1:
                    selected_attack = player.select_attack()
                    if selected_attack is None:
                        continue

                    # Update enemy's health
                    print(f"{player.name} uses {selected_attack.name} for {selected_attack.damage} damage!")
                    enemy.health -= selected_attack.damage
                    break
                case 2:
                    selected_item = player.select_item()
                    if selected_item is None:
                        continue

                    # Check the type of potion, is it for the player or the enemy
                    if isinstance(selected_item, DamagePotion):
                        selected_item.use(player, enemy)
                    else:
                        selected_item.use(player)
                    player.items.remove(selected_item)
                    break
                case _:
                    print("Invalid action")

        # Check enemy's health to see if they have died
        if enemy.health <= 0:
            print(f"The {enemy.name} has been defeated!")
            return True

        # Enemy's turn
        selected_attack = enemy.select_attack()
        print(f"{enemy.name} uses {selected_attack.name} for {selected_attack.damage} damage!")
        player.health -= selected_attack.damage

        # Check player's health to see if they have died
        if player.health <= 0:
            print("You have been defeated!")
            return False

