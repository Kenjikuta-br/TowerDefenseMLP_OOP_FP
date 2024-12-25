import pygame
import math
from .projectile import Projectile

class BlackProjectile(Projectile):
    def __init__(self, x, y, target, damage):
        super().__init__(x, y, target, damage)
        self._current_frame_index = 0
        self._animation_speed = 10
        self._frame_counter = 0
        self._scale_factor = 0.5  # Factor to scale down the size (0.5 for 2x smaller)

    def draw(self, screen):
        """Draw the projectile with animation, orientation, and scaling"""
        # Update frame index
        self._frame_counter += 1
        if self._frame_counter >= self._animation_speed:
            self._frame_counter = 0
            self._current_frame_index = (self._current_frame_index + 1) % len(self._black_frames)

        # Get the current frame
        current_frame = self._black_frames[self._current_frame_index]

        # Scale down the frame
        scaled_frame = pygame.transform.scale(
            current_frame,
            (int(current_frame.get_width() * self._scale_factor), int(current_frame.get_height() * self._scale_factor))
        )

        # Rotate the scaled frame
        rotated_frame = pygame.transform.rotate(
            scaled_frame,
            -math.degrees(math.atan2(self._target.rect.y - self.y, self._target.rect.x - self.x))
        )

        # Update rect to match the scaled frame's center
        rotated_rect = rotated_frame.get_rect(center=(self.x, self.y))

        # Draw the rotated and scaled frame
        screen.blit(rotated_frame, rotated_rect)
