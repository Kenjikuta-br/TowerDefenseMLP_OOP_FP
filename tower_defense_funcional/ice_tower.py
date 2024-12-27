import pygame
import math
from ice_projectile import create_ice_projectile
from projectile import create_projectile
from tower import create_tower, is_in_range


def create_ice_tower(x, y, damage, range, sprite_path, manager, slow_effect, shoot_delay):
    """Cria a Ice Tower com os parâmetros iniciais."""
    black_tower = create_tower(x, y, damage, range, "Ice Tower", sprite_path, manager, shoot_delay)
    black_tower["slow_effect"] = slow_effect

    return black_tower

def attack(tower, enemies, current_time):
    """Ataca o inimigo mais próximo dentro do alcance, se o tempo permitir."""
    if current_time - tower["last_shot_time"] >= tower["shoot_delay"]:
        closest_enemy = None
        closest_distance = float('inf')

        for enemy in enemies:
            if is_in_range(tower, enemy):
                distance = math.sqrt(((tower['x'] + tower['sprite'].get_width() // 2) - (enemy['x'] + 24)) ** 2 + ((tower['y'] + tower['sprite'].get_height() // 2) - (enemy['y']+24)) ** 2)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_enemy = enemy

        if closest_enemy != None:
            # Lança um novo projétil em direção ao inimigo mais próximo
            projectile = create_ice_projectile(tower["x"] + tower["rect"].width // 2, tower["y"] + tower["rect"].height // 2, closest_enemy, tower["damage"])
            tower["projectiles"].append(projectile)
            tower["last_shot_time"] = current_time  # Reseta o tempo após o disparo

