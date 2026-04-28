class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} attacks!")

class Enemy(Character):
    def attack(self):
        print(f"{self.name} attacks aggressively!")


# 👇 Taking input from user
char_name = input("Enter character name: ")
char_health = int(input("Enter character health: "))

enemy_name = input("Enter enemy name: ")
enemy_health = int(input("Enter enemy health: "))

# Creating objects
player = Character(char_name, char_health)
enemy = Enemy(enemy_name, enemy_health)

# Actions
print("\n--- Game Start ---")
player.attack()
enemy.attack()