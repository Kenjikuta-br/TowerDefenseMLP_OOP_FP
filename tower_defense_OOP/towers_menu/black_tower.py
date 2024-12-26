from .tower import Tower
import math
from projectiles.black_projectile import BlackProjectile


class BlackTower(Tower):
    def __init__(self, x, y, damage, range, sprite_path, manager, shoot_delay):
        super().__init__(x, y, damage, range, "Black Tower", sprite_path, manager, shoot_delay)

    def attack(self, enemies, current_time):
        """Attack the closest enemy within range if enough time has passed"""
        if current_time - self.last_shot_time >= self.shoot_delay:  # Check if cooldown has passed
            closest_enemy = None
            closest_distance = float('inf')  # Start with an infinitely large distance

            for enemy in enemies:
                if self.is_in_range(enemy):  # Check if the enemy is within range
                    #self.x e etc é o canto superior direito, por isso pegar width e height // 2 para pegar o centro da torre, mesma coisa para o enemy que tem rect(20,20)
                    distance = math.sqrt(((self.x + self.sprite.get_width() // 2) - (enemy.x + 24)) ** 2 + ((self.y + self.sprite.get_height() // 2) - (enemy.y+24)) ** 2)
                    if distance < closest_distance:  # Update the closest enemy
                        closest_distance = distance
                        closest_enemy = enemy
                        #print(f"{enemy.name}")

            if closest_enemy != None:  # If there's an enemy within range, attack it
                # Launch a new projectile towards the closest enemy
                projectile = BlackProjectile(self.x + self.rect.width // 2, self.y + self.rect.height // 2, closest_enemy, self.damage)
                self.projectiles.append(projectile)
                self.last_shot_time = current_time  # Reset the timer after firing a projectile