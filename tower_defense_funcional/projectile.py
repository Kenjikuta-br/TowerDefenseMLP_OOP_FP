import math
import pygame
from enemy import take_damage

def create_projectile(x, y, target, damage):

    projectile = {
        'x': x,
        'y': y,
        'target': target,
        'speed': 5,
        'damage': damage,
        'image': pygame.Surface(10, 10),  # Small circle for the projectile
        'rect': None  # Position of the projectile
    }

    projectile['image'].fill((0, 0, 255))  # Color of the projectile (Blue)
    projectile['rect'] = projectile['image'].get_rect(center=(x, y))  # Position

    return projectile

def move_projectile(projectile):
    direction_x = projectile['target']['rect']['x'] - projectile['x']
    direction_y = projectile['target']['rect']['y'] - projectile['y']
    distance = math.sqrt(direction_x**2 + direction_y**2)
    
    
    direction_x /= distance
    direction_y /= distance
    
    projectile['x'] += direction_x * projectile['speed']
    projectile['y'] += direction_y * projectile['speed']
    projectile['rect'].topleft = (projectile['x'], projectile['y'])

def check_collision(projectile):
    if projectile['rect'].colliderect(projectile['target']['rect']):
        take_damage(projectile['target'],(projectile['damage']))
        return True
    return False

def draw_projectile(projectile, screen):
    screen.blit(projectile['image'], projectile['rect'])