enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


def drink_portion():
    potion_strength = 2
    print(potion_strength)

drink_portion()
