import pygame
import math

class Tower:
    def __init__(self, x, y, damage, range, type, sprite_path):
        self.x = x
        self.y = y
        self.damage = damage
        self.range = range
        self.type = type  # Tipo da torre (por exemplo: "Torre 1", "Torre 2")
        self.sprite = pygame.image.load(sprite_path)  # Load the sprite
        self.sprite = pygame.transform.scale(self.sprite, (64, 110))  # Scale sprite to fit size
        self.rect = self.sprite.get_rect(topleft=(x, y))  # Position the sprite

    def attack(self, enemy):
        """Checks if the enemy is within range and attacks"""
        if self.is_in_range(enemy):
            enemy.take_damage(self.damage)
            #print(f"The tower attacked {enemy.name} causing {self.damage} damage.")

    def is_in_range(self, enemy):
        """Checks if the enemy is within the tower's range, considering distance"""
        # Calculates the distance between the center of the tower and the center of the enemy
        distance = math.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2)
        return distance <= self.range

    def draw(self, screen):
        """Draws the tower sprite on the screen"""
        screen.blit(self.sprite, (self.x, self.y))  # Draw the sprite at the tower's position (screen.blit uses topleft as default)
        #pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Red

        # Desenha a circunferência representando o alcance
        pygame.draw.circle(
            screen, 
            (0, 255, 0),  # Cor verde
            (self.x + self.sprite.get_width() // 2, self.y + self.sprite.get_height() // 2),  # Centro da circunferência
            self.range,  # Raio da circunferência
            1  # Espessura da borda (1 = apenas o contorno)
        )
    
    def upgrade(self):
        """Faz o upgrade da torre (exemplo)"""
        self.range += 20
        print(f"Torre {self.type} foi melhorada! Novo alcance: {self.range}")
    
    def sell(self):
        """Vende a torre (exemplo)"""
        print(f"Torre {self.type} vendida.")
