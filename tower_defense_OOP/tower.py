import pygame
import math
from projectile import Projectile

class Tower:
    def __init__(self, x, y, damage, range, type, sprite_path, manager):
        self.x = x
        self.y = y
        self.damage = damage
        self.range = range
        self.type = type
        self.sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (64, 110))
        self.rect = self.sprite.get_rect(topleft=(x, y))
        self.manager = manager  # Referência ao TowerManager
        self.projectiles = []  # List to hold projectiles
        self.last_shot_time = 0  # Track the last time a projectile was shot
        self.shoot_delay = 0.5  # Time between shots in seconds (0.5 seconds = 2 shots per second)


    def attack(self, enemies, current_time):
        """Check if any enemy is within range and launch a projectile if enough time has passed"""
        if current_time - self.last_shot_time >= self.shoot_delay:  # Check if cooldown has passed
            for enemy in enemies:
                if self.is_in_range(enemy):
                    # Launch a new projectile towards the enemy
                    projectile = Projectile(self.x + self.rect.width // 2, self.y + self.rect.height // 2, enemy, self.damage)
                    self.projectiles.append(projectile)
            
            self.last_shot_time = current_time  # Reset the timer after firing a projectile


    def is_in_range(self, enemy):
        """Checks if the enemy is within the tower's range"""
        distance = math.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2)
        return distance <= self.range

    def update_projectiles(self):
        """Update the movement and collision of all projectiles"""
        for projectile in self.projectiles[:]:
            projectile.move()  # Move each projectile
            if projectile.check_collision():  # Check for collision
                self.projectiles.remove(projectile)  # Remove projectile after collision

    def draw(self, screen):
        """Draws the tower and its projectiles"""
        screen.blit(self.sprite, (self.x, self.y))
        pygame.draw.circle(screen, (0, 255, 0), (self.x + self.sprite.get_width() // 2, self.y + self.sprite.get_height() // 2), self.range, 1)

        # Draw all projectiles
        for projectile in self.projectiles:
            projectile.draw(screen)

    def upgrade(self):
        self.range += 20
        print(f"Torre {self.type} foi melhorada! Novo alcance: {self.range}")

    def sell(self):
        print(f"Torre {self.type} vendida.")
