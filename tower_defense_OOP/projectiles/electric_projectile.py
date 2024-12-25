import pygame
import math
from .projectile import Projectile

class ElectricProjectile(Projectile):
    def __init__(self, x, y, target, damage):
        super().__init__(x, y, target, damage)
        self._current_frame_index = 0
        self._animation_speed = 5  # Number of frames to wait before switching
        self._frame_counter = 0  # Keeps track of frame timing

    def draw(self, screen):
        """Override draw to handle animation"""
        # Update frame index
        self._frame_counter += 1
        if self._frame_counter >= self._animation_speed:
            self._frame_counter = 0
            self._current_frame_index = (self._current_frame_index + 1) % len(self._electric_frames)

        # Draw the current frame
        current_frame = self._electric_frames[self._current_frame_index]
        rotated_frame = pygame.transform.rotate(
            current_frame,
            -math.degrees(math.atan2(self._target.rect.y - self.y, self._target.rect.x - self.x))
        )
        screen.blit(rotated_frame, self._rect)
