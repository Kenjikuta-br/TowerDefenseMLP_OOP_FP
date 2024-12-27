import pygame
import math
from projectile import create_projectile, move_projectile, draw_projectile, check_collision
from ice_projectile import create_ice_projectile, draw_ice_projectile, move_ice_projectile
from electric_projectile import create_electric_projectile, draw_electric_projectile
from black_projectile import draw_black_projectile


def create_tower(x, y, damage, range, type, sprite_path, manager, shoot_delay):
    """Cria uma nova torre com as propriedades fornecidas"""
    sprite = pygame.image.load(sprite_path)
    sprite = pygame.transform.scale(sprite, (64, 110))
    rect = sprite.get_rect(topleft=(x, y))
    
    tower = {
        'x': x,
        'y': y,
        'damage': damage,
        'range': range,
        'type': type,
        'sprite': sprite,
        'rect': rect,
        'manager': manager,
        'projectiles': [],
        'last_shot_time': 0,
        'shoot_delay': shoot_delay,
    }
    
    return tower

def attack(tower, enemies, current_time):
    """Ataque a inimigos dentro do alcance da torre"""
    if current_time - tower['last_shot_time'] >= tower['shoot_delay']:
        closest_enemy = None
        closest_distance = float('inf')

        for enemy in enemies:
            if is_in_range(tower, enemy):
                distance = math.sqrt(((tower['x'] + tower['sprite'].get_width() // 2) - (enemy['x'] + 24)) ** 2 + ((tower['y'] + tower['sprite'].get_height() // 2) - (enemy['y']+24)) ** 2)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_enemy = enemy

        if closest_enemy != None:
            #projectile = create_projectile(tower['x'] + tower['rect'].width // 2, tower['y'] + tower['rect'].height // 2, closest_enemy, tower['damage'])
            if tower['type'] == "Black Tower":
                projectile = create_projectile(tower['x'] + tower['sprite'].get_width() // 2, tower['y'] + tower['sprite'].get_height() // 2, closest_enemy, tower['damage'])
            elif tower['type'] == "Ice Tower":
                projectile = create_ice_projectile(tower['x'] + tower['sprite'].get_width() // 2, tower['y'] + tower['sprite'].get_height() // 2, closest_enemy, tower['damage'])
            elif tower['type'] == "Electric Tower":
                projectile = create_electric_projectile(tower['x'] + tower['sprite'].get_width() // 2, tower['y'] + tower['sprite'].get_height() // 2, closest_enemy, tower['damage'])

        
            #projectile = create_projectile(tower['x'] + tower['sprite'].get_width() // 2, tower['y'] + tower['sprite'].get_height() // 2, closest_enemy, tower['damage'], tower['type'])

            tower['projectiles'].append(projectile)
            tower['last_shot_time'] = current_time

def is_in_range(tower, enemy):
    """Verifica se o inimigo está dentro do alcance da torre"""
    distance = math.sqrt(((tower['x'] + tower['sprite'].get_width() // 2) - (enemy['x'] + 24)) ** 2 + ((tower['y'] + tower['sprite'].get_height() // 2) - (enemy['y']+24)) ** 2)
    return distance <= tower['range']

def update_projectiles(tower):
    """Atualiza o movimento e colisões de todos os projéteis da torre"""
    for projectile in tower['projectiles'][:]:
        if tower['type'] == "Ice Tower":
            move_ice_projectile(projectile)
        else:
            move_projectile(projectile)  # Move cada projétil
        if check_collision(projectile):  # Verifica colisão
            tower['projectiles'].remove(projectile)  # Remove o projétil após a colisão

def draw_tower(tower, screen):
    """Desenha a torre e seus projéteis"""
    screen.blit(tower['sprite'], (tower['x'], tower['y']))
    pygame.draw.circle(screen, (0, 255, 0), (tower['x'] + tower['sprite'].get_width() // 2, tower['y'] + tower['sprite'].get_height() // 2), tower['range'], 1)
    
def draw_projectiles(tower, screen):
     # Draw all projectiles
    for projectile in tower['projectiles']:
        #print(f"{tower['type']}")
        if tower['type'] == "Electric Tower":
            draw_electric_projectile(projectile, screen)
        elif tower['type'] == "Ice Tower":
            draw_ice_projectile(projectile, screen)
        else:
            draw_black_projectile(projectile, screen)

def upgrade_tower(tower):
    tower['range'] += 20
    print(f"Torre {tower['type']} foi melhorada! Novo alcance: {tower['range']}")

def sell_tower(tower):
    print(f"Torre {tower['type']} vendida.")
