import pygame
import math

class Projectile:
    def __init__(self, x, y, target, damage):
        self._x = x
        self._y = y
        self._target = target
        self._damage = damage
        self._speed = 5  # Speed at which the projectile moves
        self._image = pygame.Surface((10, 10))  # Small circle for the projectile
        self._image.fill((0, 0, 255))  # Color of the projectile (Blue)
        self._rect = self._image.get_rect(center=(x, y))  # Position of the projectile

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._rect.centerx = value  # Update rect position when x changes

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._rect.centery = value  # Update rect position when y changes

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        if value is None:
            raise ValueError("Target cannot be None.")
        self._target = value

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        if value < 0:
            raise ValueError("Damage cannot be negative.")
        self._damage = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value <= 0:
            raise ValueError("Speed must be positive.")
        self._speed = value

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self._image

    def move(self):
        """Moves the projectile towards the target"""
        # Calculate direction towards the target
        direction_x = self._target.rect.x - self._x
        direction_y = self._target.rect.y - self._y
        distance = math.sqrt(direction_x**2 + direction_y**2)
        
        # Normalize direction vector
        direction_x /= distance
        direction_y /= distance
        
        # Move the projectile
        self.x += direction_x * self._speed
        self.y += direction_y * self._speed

    def check_collision(self):
        """Check if the projectile collides with the enemy"""
        if self._rect.colliderect(self._target.rect):
            self._target.take_damage(self._damage)  # Cause damage
            return True  # Projectile has hit the enemy
        return False

    def draw(self, screen):
        """Draws the projectile on the screen"""
        screen.blit(self._image, self._rect)
