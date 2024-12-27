import math
from projectile import create_projectile
import pygame

def create_black_projectile(x, y, target, damage):

    projectile = create_projectile(x, y, target, damage)

    projectile['current_frame_index'] = 0
    projectile['animation_speed'] = 10
    projectile['frame_counter'] = 0
    projectile['scale_factor'] = 0.5 
    projectile['type'] = 'black'

    return projectile

def draw_black_projectile(projectile, screen):
        """Draw the projectile with animation, orientation, and scaling"""
        # Update frame index
        projectile['frame_counter'] += 1
        if projectile['frame_counter'] >= projectile['animation_speed']:
            projectile['frame_counter'] = 0
            projectile['current_frame_index'] = (projectile['current_frame_index'] + 1) % len(projectile['black_frames'])

        # Get the current frame
        current_frame = projectile['black_frames'][projectile['current_frame_index']]

        # Scale down the frame
        scaled_frame = pygame.transform.scale(
            current_frame,
            (int(current_frame.get_width() * projectile['scale_factor']), int(current_frame.get_height() * projectile['scale_factor']))
        )

        # Rotate the scaled frame
        rotated_frame = pygame.transform.rotate(
            scaled_frame,
            -math.degrees(math.atan2(projectile['target']['rect'].y - projectile['y'], projectile['target']['rect'].x - projectile['x']))
        )

        # Update rect to match the scaled frame's center
        rotated_rect = rotated_frame.get_rect(center=(projectile['x'], projectile['y']))

        # Draw the rotated and scaled frame
        screen.blit(rotated_frame, rotated_rect)