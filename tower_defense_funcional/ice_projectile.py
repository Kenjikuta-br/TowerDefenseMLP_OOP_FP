from projectile import create_projectile, move_projectile
import math
import pygame
from enemy import take_damage, slow


def create_ice_projectile(x, y, target, damage):
    projectile = create_projectile(x, y, target, damage)
    projectile['current_frame'] = 0  # Current frame in the animation sequence
    projectile['frame_count'] = len(projectile['ice_frames'])
    projectile['angle'] = 0  # Angle to rotate the projectile based on movement direction
    projectile['animation_speed'] = 0.2  # Speed at which frames change
    projectile['type'] = 'ice'
    
    return projectile


def calculate_angle(projectile):
    """Calculate the angle of rotation based on the direction to the target."""
    direction_x = projectile['target']['rect'].x - projectile['x']
    direction_y = projectile['target']['rect'].y - projectile['y']
    projectile['angle'] = math.degrees(math.atan2(-direction_y, direction_x))
      # Negative Y for pygame's coordinate system
def move_ice_projectile(projectile):
    """Overrides move method to include angle calculation."""
    move_projectile(projectile)
    calculate_angle(projectile)


def animate_ice_projectile(projectile):
    """Advance the animation frame."""
    projectile['current_frame'] += projectile['animation_speed']
    if projectile['current_frame'] >= projectile['frame_count']:
        projectile['current_frame'] = 0

def draw_ice_projectile(projectile, screen):
    """Draws the animated ice projectile with rotation."""
    animate_ice_projectile(projectile)  # Update animation frame
    current_frame_image = projectile['ice_frames'][int(projectile['current_frame'])]
    
    # Rotate the image based on movement direction
    rotated_image = pygame.transform.rotate(current_frame_image, projectile['angle'])
    rotated_rect = rotated_image.get_rect(center=(projectile['x'], projectile['y']))
    
    # Draw the rotated frame
    screen.blit(rotated_image, rotated_rect)

def check_collision(ice_projectile):
    if ice_projectile['rect'].colliderect(ice_projectile['target']['rect']):
        take_damage(ice_projectile['target'],(ice_projectile['damage']))
        slow(ice_projectile['target'],(3.0))  # Apply slowing effect to the enemy, duration of 3.0 seconds
        return True
    return False