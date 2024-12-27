import math
from projectile import create_projectile
import pygame

def create_electric_projectile(x, y, target, damage):

    projectile = create_projectile(x, y, target, damage)

    projectile['current_frame_index'] = 0
    projectile['animation_speed'] = 5
    projectile['frame_counter'] = 0
    projectile['type'] = 'electric'

    return projectile

def draw_electric_projectile(projectile, screen):
        """Draw the projectile with animation, orientation, and scaling"""
        # Update frame index
        projectile['frame_counter'] += 1
        if projectile['frame_counter'] >= projectile['animation_speed']:
            projectile['frame_counter'] = 0
            projectile['current_frame_index'] = (projectile['current_frame_index'] + 1) % len(projectile['electric_frames'])

        # Get the current frame
        current_frame = projectile['electric_frames'][projectile['current_frame_index']]

        # Rotate the scaled frame
        rotated_frame = pygame.transform.rotate(
            current_frame,
            -math.degrees(math.atan2(projectile['target']['rect'].y - projectile['y'], projectile['target']['rect'].x - projectile['x']))
        )

        # Draw the rotated and scaled frame
        screen.blit(rotated_frame, projectile['rect'])