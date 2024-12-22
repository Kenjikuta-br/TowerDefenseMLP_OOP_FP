import pygame
import math

class Projectile:
    def __init__(self, x, y, target, damage):
        self.x = x
        self.y = y
        self.target = target
        self.damage = damage
        self.speed = 5  # Speed at which the projectile moves
        self.image = pygame.Surface((10, 10))  # Small circle for the projectile
        self.image.fill((0, 0, 255))  # Color of the projectile (Blue)
        self.rect = self.image.get_rect(center=(x, y))  # Position of the projectile

    def move(self):
        """Moves the projectile towards the target"""
        # Calculate direction towards the target
        direction_x = self.target.x - self.x
        direction_y = self.target.y - self.y
        distance = math.sqrt(direction_x**2 + direction_y**2)
        
        # Normalize direction vector
        direction_x /= distance
        direction_y /= distance
        
        # Move the projectile
        self.x += direction_x * self.speed
        self.y += direction_y * self.speed
        self.rect.center = (self.x, self.y)  # Update the position of the rect

    def check_collision(self):
        """Check if the projectile collides with the enemy"""
        if self.rect.colliderect(self.target.rect):
            self.target.take_damage(self.damage)  # Cause damage
            return True  # Projectile has hit the enemy
        return False

    def draw(self, screen):
        """Draws the projectile on the screen"""
        screen.blit(self.image, self.rect)
