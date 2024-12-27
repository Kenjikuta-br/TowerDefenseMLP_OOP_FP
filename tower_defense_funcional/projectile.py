import math
import pygame
from enemy import take_damage

from PIL import Image

def load_gif_frames(gif_path):
    frames = []
    gif = Image.open(gif_path)
    for frame in range(gif.n_frames):
        gif.seek(frame)
        pygame_image = pygame.image.fromstring(gif.tobytes(), gif.size, gif.mode)
        frames.append(pygame_image)
    return frames

def load_png_frames_black(folder_path, frame_count):
    frames = []
    for i in range(frame_count):
        image = pygame.image.load(f"{folder_path}/00{i+1}.png").convert_alpha()
        frames.append(image)
    return frames

def load_png_frames_ice(folder_path, frame_count):
    frames = []
    for i in range(frame_count):
        image = pygame.image.load(f"{folder_path}/1_{i+1}.png").convert_alpha()
        frames.append(image)
    return frames




def create_projectile(x, y, target, damage):
    projectile = {
        'x': x,
        'y': y,
        'target': target,
        'damage': damage,
        'speed': 5,
        'image': pygame.Surface((10, 10)),
        'rect': None,
        'electric_frames': load_gif_frames("tower_defense_funcional/assets/projectiles/electric_projectile/spark.gif"),
        'black_frames': load_png_frames_black("tower_defense_funcional/assets/projectiles/black_projectile", 5),
        'ice_frames': load_png_frames_ice("tower_defense_funcional/assets/projectiles/ice_projectile", 22)
    }
    projectile['image'].fill((0, 0, 255))
    projectile['rect'] = projectile['image'].get_rect(center=(x, y))
    return projectile

def move_projectile(projectile):
    direction_x = projectile['target']['rect'].x - projectile['x']
    direction_y = projectile['target']['rect'].y - projectile['y']
    distance = math.sqrt(direction_x**2 + direction_y**2)


    direction_x /= distance
    direction_y /= distance


    projectile['x'] += direction_x * projectile['speed']
    projectile['rect'].centerx = projectile['x']
    projectile['y'] += direction_y * projectile['speed']
    projectile['rect'].centery = projectile['y']

def check_collision(projectile):
    if projectile['rect'].colliderect(projectile['target']['rect']):
        take_damage(projectile['target'],(projectile['damage']))
        return True
    return False

def draw_projectile(projectile, screen):
    screen.blit(projectile['image'], projectile['rect'])