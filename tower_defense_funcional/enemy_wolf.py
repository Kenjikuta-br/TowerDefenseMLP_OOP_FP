from enemy import (
    create_enemy, move_enemy, die, load_spritesheet
)

def create_wolf(x, y, path, player, manager):
    wolf = create_enemy(name="Wolf", health=130, x=x, y=y, speed=3.5, manager=manager, path=path, reward_money=45, player=player, damage=15)
    wolf['pack_attack'] = False
    wolf['animations'] = {
        "walk_down": load_spritesheet("tower_defense_funcional/assets/wolf/walk/D_Walk.png", rows=1, cols=6),
        "walk_up": load_spritesheet("tower_defense_funcional/assets/wolf/walk/U_Walk.png", rows=1, cols=6),
        "walk_side": load_spritesheet("tower_defense_funcional/assets/wolf/walk/S_Walk.png", rows=1, cols=6),
        "death_down": load_spritesheet("tower_defense_funcional/assets/wolf/death/D_Death.png", rows=1, cols=6),
        "death_up": load_spritesheet("tower_defense_funcional/assets/wolf/death/U_Death.png", rows=1, cols=6),
        "death_side": load_spritesheet("tower_defense_funcional/assets/wolf/death/S_Death.png", rows=1, cols=6),
    }
    return wolf

def activate_pack_attack(wolf):
    wolf['pack_attack'] = True
    wolf['damage'] = 12
    print(f"{wolf['name']} activated pack attack! Damage increased to {wolf['damage']}.")

def move_wolf(wolf):
    move_enemy(wolf)
    if wolf['pack_attack']:
        wolf['speed'] = 7

def die_wolf(wolf):
    print(f"The {wolf['name']} was hunted down!")
    die(wolf)