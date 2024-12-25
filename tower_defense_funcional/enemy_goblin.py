from enemy import (
    create_enemy, move_enemy,
    die, load_spritesheet
)

def create_goblin(x, y, path, player, manager):
    goblin = create_enemy(name="Goblin", health=100, x=x, y=y, speed=3, manager=manager, path=path, reward_money=20, player=player, damage=15)
    goblin['stealth'] = False
    goblin['animations'] = {
        "walk_down": load_spritesheet("tower_defense_OOP/assets/goblin/walk/D_Walk.png", rows=1, cols=6),
        "walk_up": load_spritesheet("tower_defense_OOP/assets/goblin/walk/U_Walk.png", rows=1, cols=6),
        "walk_side": load_spritesheet("tower_defense_OOP/assets/goblin/walk/S_Walk.png", rows=1, cols=6),
        "death_down": load_spritesheet("tower_defense_OOP/assets/goblin/death/D_Death.png", rows=1, cols=6),
        "death_up": load_spritesheet("tower_defense_OOP/assets/goblin/death/U_Death.png", rows=1, cols=6),
        "death_side": load_spritesheet("tower_defense_OOP/assets/goblin/death/S_Death.png", rows=1, cols=6),
    }
    return goblin

def toggle_stealth(goblin):
    goblin['stealth'] = not goblin['stealth']
    print(f"Stealth mode: {'Activated' if goblin['stealth'] else 'Deactivated'}")

def move_goblin(goblin):
    if goblin['stealth']:
        goblin['speed'] = 1
    else:
        goblin['speed'] = 3
    
    move_enemy(goblin)

def die_goblin(goblin):
    print(f"The {goblin['name']} was slain!")
    die(goblin)