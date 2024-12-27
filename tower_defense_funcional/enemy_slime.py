from enemy import (
    create_enemy, move_enemy,
    die, load_spritesheet
)

def create_slime(x, y, path, player, manager):
    slime = create_enemy(name="Slime", health=100, x=x, y=y, speed=2, manager=manager, path=path, reward_money=20, player=player, damage=10)
    slime['healing_rate'] = 1
    slime['animations'] = {
        "walk_down": load_spritesheet("tower_defense_funcional/assets/slime/walk/D_Walk.png", rows=1, cols=6),
        "walk_up": load_spritesheet("tower_defense_funcional/assets/slime/walk/U_Walk.png", rows=1, cols=6),
        "walk_side": load_spritesheet("tower_defense_funcional/assets/slime/walk/S_Walk.png", rows=1, cols=6),
        "death_down": load_spritesheet("tower_defense_funcional/assets/slime/death/D_Death.png", rows=1, cols=6),
        "death_up": load_spritesheet("tower_defense_funcional/assets/slime/death/U_Death.png", rows=1, cols=6),
        "death_side": load_spritesheet("tower_defense_funcional/assets/slime/death/S_Death.png", rows=1, cols=6),
    }
    return slime

def move_slime(slime):
    if not slime['is_dead']:
        #slime['health'] += slime['healing_rate']  # Heal over time
        move_enemy(slime)

def die_slime(slime):
    print(f"The {slime['name']} was squished!")
    die(slime)

