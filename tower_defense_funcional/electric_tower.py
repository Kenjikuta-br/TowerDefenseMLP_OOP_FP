from tower import create_tower, is_in_range
from projectile import create_projectile

def create_electric_tower(x, y, damage, range, sprite_path, manager):
    """Function to create an electric tower."""
    electric_tower = create_tower(x, y, damage, range, "Electric Tower", sprite_path, manager)
    return electric_tower


def attack(electric_tower, enemies, current_time):
    """Check if any enemy is within range and launch a projectile if enough time has passed"""
    if current_time - electric_tower['last_shot_time'] >= electric_tower['shoot_delay']:  # Check if cooldown has passed
        for enemy in enemies:
            if is_in_range(electric_tower, enemy):
                # Launch a new projectile towards the enemy
                projectile = create_projectile(electric_tower['x'] + electric_tower['rect'].width // 2, electric_tower['y'] + electric_tower['rect'].height // 2, enemy, electric_tower['damage'])
                electric_tower['projectiles'].append(projectile)
        electric_tower['last_shot_time'] = current_time  # Reset the timer after firing a projectile