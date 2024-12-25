from tower import create_tower

def create_black_tower(x, y, damage, range, sprite_path, manager):
    black_tower = create_tower(x, y, damage, range, "Black Tower", sprite_path, manager)
    return black_tower

