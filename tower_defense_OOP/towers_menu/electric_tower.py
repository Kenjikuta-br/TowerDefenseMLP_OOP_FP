from .tower import Tower
from projectiles.electric_projectile import ElectricProjectile

class ElectricTower(Tower):
    def __init__(self, x, y, damage, range, sprite_path, manager):
        super().__init__(x, y, damage, range, "Electric Tower", sprite_path, manager)


    def attack(self, enemies, current_time):
            """Check if any enemy is within range and launch a projectile if enough time has passed"""
            if current_time - self.last_shot_time >= self.shoot_delay:  # Check if cooldown has passed
                for enemy in enemies:
                    if self.is_in_range(enemy):
                        # Launch a new projectile towards the enemy
                        projectile = ElectricProjectile(self.x + self.rect.width // 2, self.y + self.rect.height // 2, enemy, self.damage)
                        self.projectiles.append(projectile)
                self.last_shot_time = current_time  # Reset the timer after firing a projectile