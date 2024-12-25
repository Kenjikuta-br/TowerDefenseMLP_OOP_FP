import pygame
import math
from .projectile import Projectile

class IceProjectile(Projectile):
    def __init__(self, x, y, target, damage):
        super().__init__(x, y, target, damage)
        self._current_frame = 0  # Current frame in the animation sequence
        self._frame_count = len(self._ice_frames)
        self._angle = 0  # Angle to rotate the projectile based on movement direction
        self._animation_speed = 0.2  # Speed at which frames change

    def calculate_angle(self):
        """Calculate the angle of rotation based on the direction to the target."""
        direction_x = self._target.rect.x - self._x
        direction_y = self._target.rect.y - self._y
        self._angle = math.degrees(math.atan2(-direction_y, direction_x))  # Negative Y for pygame's coordinate system

    def move(self):
        """Overrides move method to include angle calculation."""
        super().move()
        self.calculate_angle()

    def animate(self):
        """Advance the animation frame."""
        self._current_frame += self._animation_speed
        if self._current_frame >= self._frame_count:
            self._current_frame = 0

    def draw(self, screen):
        """Draws the animated ice projectile with rotation."""
        self.animate()  # Update animation frame
        current_frame_image = self._ice_frames[int(self._current_frame)]
        
        # Rotate the image based on movement direction
        rotated_image = pygame.transform.rotate(current_frame_image, self._angle)
        rotated_rect = rotated_image.get_rect(center=(self._x, self._y))
        
        # Draw the rotated frame
        screen.blit(rotated_image, rotated_rect)

    def check_collision(self):
        """Check if the projectile collides with the enemy"""
        if self._rect.colliderect(self._target.rect):
            self._target.take_damage(self._damage)  # Cause damage
            self._target.slow(3.0)  # Apply slowing effect to the enemy, duration of 3.0 seconds
            return True  # Projectile has hit the enemy
        return False