import pygame
import math
from projectile import create_projectile
from tower import create_tower, is_in_range


def create_ice_tower(x, y, damage, range, sprite_path, manager, slow_effect):
    """Cria a Ice Tower com os parâmetros iniciais."""
    black_tower = create_tower(x, y, damage, range, "Ice Tower", sprite_path, manager)
    black_tower["slow_effect"] = slow_effect

    return black_tower

def attack(tower, enemies, current_time):
    """Ataca o inimigo mais próximo dentro do alcance, se o tempo permitir."""
    if current_time - tower["last_shot_time"] >= tower["shoot_delay"]:
        closest_enemy = None
        closest_distance = float('inf')

        for enemy in enemies:
            if is_in_range(tower, enemy):
                distance = math.sqrt((tower["x"] - enemy["x"]) ** 2 + (tower["y"] - enemy["y"]) ** 2)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_enemy = enemy

        if closest_enemy:
            # Lança um novo projétil em direção ao inimigo mais próximo
            projectile = create_projectile(tower["x"] + tower["rect"].width // 2, tower["y"] + tower["rect"].height // 2, closest_enemy, tower["damage"])
            tower["projectiles"].append(projectile)
            enemy['is_slowed'] = True
            tower["last_shot_time"] = current_time  # Reseta o tempo após o disparo

    return tower