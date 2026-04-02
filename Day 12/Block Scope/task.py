game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemies():
    game_level = 2
    if game_level < 5:
        new_enemy = enemies[0]
        print(new_enemy)

create_enemies()

