from tower import create_tower, is_in_range
import math
from black_projectile import create_black_projectile
from projectile import create_projectile

def create_black_tower(x, y, damage, range, sprite_path, manager, shoot_delay):
    black_tower = create_tower(x, y, damage, range, "Black Tower", sprite_path, manager, shoot_delay)
    return black_tower

def attack(black_tower, enemies, current_time):
    """Attack the closest enemy within range if enough time has passed"""
    if current_time - black_tower['last_shot_time'] >= black_tower['shoot_delay']:  # Check if cooldown has passed
        closest_enemy = None
        closest_distance = float('inf')  # Start with an infinitely large distance

        for enemy in enemies:
            if is_in_range(black_tower, enemy):  # Check if the enemy is within range
                #self.x e etc é o canto superior direito, por isso pegar width e height // 2 para pegar o centro da torre, mesma coisa para o enemy que usa uma sprite 48x48
                distance = math.sqrt(((black_tower['x'] + black_tower['sprite'].get_width() // 2) - (enemy['x'] + 24)) ** 2 + ((black_tower['y'] + black_tower['sprite'].get_height() // 2) - (enemy['y']+24)) ** 2)
                if distance < closest_distance:  # Update the closest enemy
                    closest_distance = distance
                    closest_enemy = enemy
                    #print(f"{enemy.name}")
        if closest_enemy != None:  # If there's an enemy within range, attack it
            # Launch a new projectile towards the closest enemy
            projectile = create_black_projectile(black_tower['x'] + black_tower['rect'].width // 2, black_tower['y'] + black_tower['rect'].height // 2, closest_enemy, black_tower['damage'])
            black_tower['projectiles'].append(projectile)
            black_tower['last_shot_time'] = current_time  # Reset the timer after firing a projectile