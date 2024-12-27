import pygame
import math
from player import lose_health, add_money

def create_enemy(name, health, x, y, speed, manager, path, reward_money, player, damage=10):
    enemy = {
        'name': name,
        'health': health,
        'x': x,
        'y': y,
        'speed': speed,
        'manager': manager,
        'rect': pygame.Rect(x, y, 20, 20),
        'is_dead': False,
        'path': path,
        'current_waypoint': 0,
        'reward_money': reward_money,
        'player': player,
        'damage': damage,
        'off_set_rect': 14,
        'animations': None,
        'current_animation': "walk_side",
        'animation_frame': 0,
        'animation_speed': 0.1,
        'time_accumulator': 0,
        'facing_right': True,        
        'is_slowed': False,
        'slow_effect': 2,
        'slow_duration': 0,
        'slow_timer': 0
    }
    manager['enemies'].append(enemy)
    return enemy

def take_damage(enemy, amount):
    """Method to receive damage"""
    if amount < 0:
        raise ValueError("Damage amount cannot be negative.")
    enemy['health'] -= amount
    if enemy['health'] <= 0:
        die(enemy)  # Calls the method to kill the enemy when health reaches zero

def update_animation(enemy, delta_time):
    enemy['time_accumulator'] += delta_time
    if enemy['time_accumulator'] >= enemy['animation_speed']:
        enemy['time_accumulator'] = 0
        enemy['animation_frame'] = (enemy['animation_frame'] + 1) % len(enemy['animations'][enemy['current_animation']])
        

def draw_enemy(enemy, screen):
    """Draws the current frame of the animation on the screen."""
    frame = enemy['animations'][enemy['current_animation']][enemy['animation_frame']]
         # Flip the frame if facing left
    if enemy['current_animation'] == "walk_side" and enemy['facing_right']:
        frame = pygame.transform.flip(frame, True, False)
    screen.blit(frame, (enemy['x'], enemy['y']))
    #for debuggin hitbox
    #draw_hitbox(enemy, screen)

def draw_hitbox(enemy, screen, color=(255, 0, 0)):
    pygame.draw.rect(screen, color, enemy['rect'], 2)
    #print(f"position of rect: x={enemy['rect'].x} y={enemy['rect'].y}")


def move_enemy(enemy):
    if enemy['current_waypoint'] < len(enemy['path']):
        target_x, target_y = enemy['path'][enemy['current_waypoint']]
        dx = target_x - enemy['x']
        dy = target_y - enemy['y']
        distance = math.sqrt(dx**2 + dy**2)

        current_speed = enemy['speed'] / enemy['slow_effect'] if enemy['is_slowed'] else enemy['speed']

        if distance <= current_speed:
            enemy['x'] = target_x
            enemy['rect'].x = enemy['x'] + enemy['off_set_rect']
            enemy['y'] = target_y
            enemy['rect'].y = enemy['y'] + enemy['off_set_rect']
            enemy['current_waypoint'] += 1
        else:
            enemy['x'] += (dx / distance) * current_speed
            enemy['rect'].x = enemy['x'] + enemy['off_set_rect'] 
            enemy['y'] += (dy / distance) * current_speed 
            enemy['rect'].y = enemy['y'] + enemy['off_set_rect']

        if abs(dx) > abs(dy):
            enemy['current_animation'] = "walk_side"
            enemy['facing_right'] = dx > 0
        elif dy > 0:
            enemy['current_animation'] = "walk_down"
        else:
            enemy['current_animation'] = "walk_up"
    else:
        reach_base(enemy)


def reach_base(enemy):
    print(f"{enemy['name']} alcançou a base e causou {enemy['damage']} de dano!")
    lose_health(enemy['player'], (enemy['damage']))
    enemy['is_dead'] = True
    if enemy in enemy['manager']['enemies']:
        enemy['manager']['enemies'].remove(enemy)

def die(enemy):
    if enemy['player'] != None:
        if not enemy['is_dead']:
            add_money(enemy['player'],(enemy['reward_money']))
    enemy['is_dead'] = True
    print(f"{enemy['name']} was defeated!")
    
    if enemy in enemy['manager']['enemies']:
        enemy['manager']['enemies'].remove(enemy)


def update(enemy, delta_time):
    if enemy['is_slowed']:
        enemy['slow_timer'] -= delta_time
        if enemy['slow_timer'] <= 0:
            enemy['is_slowed'] = False
            enemy['slow_timer'] = 0


def slow(enemy, duration):
    enemy['is_slowed'] = True
    enemy['slow_timer'] = duration


def load_spritesheet(file, rows, cols):
    # Implementação da função para carregar spritesheet
    sheet = pygame.image.load(file).convert_alpha()
    sheet_width, sheet_height = sheet.get_size()
    frame_width = sheet_width // cols
    frame_height = sheet_height // rows
    frames = []

    for row in range(rows):
        for col in range(cols):
            frame = sheet.subsurface(pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height))
            frames.append(frame)
    return frames


