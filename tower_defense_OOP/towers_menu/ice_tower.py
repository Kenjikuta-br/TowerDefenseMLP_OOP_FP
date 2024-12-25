from .tower import Tower
import math
from projectiles.ice_projectile import IceProjectile

class IceTower(Tower):
    def __init__(self, x, y, damage, range, sprite_path, manager, slow_effect):
        super().__init__(x, y, damage, range, "Ice Tower", sprite_path, manager)
        self._slow_effect = slow_effect  # Percentage to slow enemies
    
    def attack(self, enemies, current_time):
        """Attack the closest enemy within range if enough time has passed"""
        if current_time - self.last_shot_time >= self.shoot_delay:  # Check if cooldown has passed
            closest_enemy = None
            closest_distance = float('inf')  # Start with an infinitely large distance

            for enemy in enemies:
                if self.is_in_range(enemy):  # Check if the enemy is within range
                    distance = math.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2)
                    if distance < closest_distance:  # Update the closest enemy
                        closest_distance = distance
                        closest_enemy = enemy

            if closest_enemy != None:  # If there's an enemy within range, attack it
                # Launch a new projectile towards the closest enemy
                projectile = IceProjectile(self.x + self.rect.width // 2, self.y + self.rect.height // 2, closest_enemy, self.damage)
                self.projectiles.append(projectile)
                self.last_shot_time = current_time  # Reset the timer after firing a projectile
