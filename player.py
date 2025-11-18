from attack import Attack

class Player:
    health = 100
    attacks = [
        Attack("Sword", 10),
        Attack("Bow", 8)
    ]

    def __init__(self, name: str):
        self.name = name

    def attack(self):
        # Display attack options to the player
        for i, attack in enumerate(self.attacks, 1):
            print(f"{i} - {attack.name} : {attack.damage} DMG")

player1 = Player("Danny")
player1.attack()