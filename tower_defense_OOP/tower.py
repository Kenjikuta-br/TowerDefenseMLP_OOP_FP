import pygame
import math
from projectile import Projectile

class Tower:
    def __init__(self, x, y, damage, range, type, sprite_path, manager):
        self._x = x
        self._y = y
        self._damage = damage
        self._range = range
        self._type = type
        self._sprite = pygame.image.load(sprite_path)
        self._sprite = pygame.transform.scale(self._sprite, (64, 110))
        self._rect = self._sprite.get_rect(topleft=(x, y))
        self._manager = manager  # Referência ao TowerManager
        self._projectiles = []  # Lista para armazenar os projéteis
        self._last_shot_time = 0  # Rastrear o último tempo de disparo
        self._shoot_delay = 0.5  # Tempo entre disparos (em segundos)

    # Getters and Setters for x
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._rect.topleft = (value, self._y)  # Atualiza a posição do rect

    # Getters and Setters for y
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._rect.topleft = (self._x, value)  # Atualiza a posição do rect

    # Getters and Setters for damage
    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    # Getters and Setters for range
    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, value):
        self._range = value

    # Getters and Setters for type
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    # Getters for sprite
    @property
    def sprite(self):
        return self._sprite

    # Getters for rect
    @property
    def rect(self):
        return self._rect

    # Getters and Setters for manager
    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, value):
        self._manager = value

    # Getters for projectiles
    @property
    def projectiles(self):
        return self._projectiles

    # Getter and Setter for last_shot_time
    @property
    def last_shot_time(self):
        return self._last_shot_time

    @last_shot_time.setter
    def last_shot_time(self, value):
        self._last_shot_time = value

    # Getter and Setter for shoot_delay
    @property
    def shoot_delay(self):
        return self._shoot_delay

    @shoot_delay.setter
    def shoot_delay(self, value):
        self._shoot_delay = value


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
                        print(f"{enemy.name}")

            if closest_enemy != None:  # If there's an enemy within range, attack it
                # Launch a new projectile towards the closest enemy
                projectile = Projectile(self.x + self.rect.width // 2, self.y + self.rect.height // 2, closest_enemy, self.damage)
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
            #print(f"{self.type}")
            projectile.draw(screen)

    def upgrade(self):
        self.range += 20
        print(f"Torre {self.type} foi melhorada! Novo alcance: {self.range}")

    def sell(self):
        print(f"Torre {self.type} vendida.")
