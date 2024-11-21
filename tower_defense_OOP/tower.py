import pygame
import math

class Tower:
    def __init__(self, x, y, damage, range):
        self.x = x
        self.y = y
        self.damage = damage
        self.range = range
        self.rect = pygame.Rect(x, y, 50, 50)  # Defines the tower's area

    def attack(self, enemy):
        """Checks if the enemy is within range and attacks"""
        if self.is_in_range(enemy):
            enemy.take_damage(self.damage)
            print(f"The tower attacked {enemy.name} causing {self.damage} damage.")

    def is_in_range(self, enemy):
        """Checks if the enemy is within the tower's range, considering distance"""
        # Calculates the distance between the center of the tower and the center of the enemy
        distance = math.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2)
        return distance <= self.range

    def draw(self, screen):
        """Draws the tower on the screen"""
        pygame.draw.rect(screen, (0, 0, 255), self.rect)  # Blue
