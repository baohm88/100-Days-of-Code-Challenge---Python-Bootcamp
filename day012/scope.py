################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# LOCAL SCOPE

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# GLOBAL SCOPE
player_health =10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

# BLOCK SCOPE
game_level = 3
enemies = ['Skeletion', 'Zombie', 'Alien']
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# MODYFYING GLOBAL SCOPE
enemies = 1
def increase_enemies():
    # global enemies
    # enemies += 1
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# GLOBAL CONSTANTS
PI = 3.14159
URL = 'https://google.com'