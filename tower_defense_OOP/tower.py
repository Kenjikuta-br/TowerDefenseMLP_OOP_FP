import pygame
import math

class Tower:
    def __init__(self, x, y, damage, range):
        self.x = x
        self.y = y
        self.damage = damage
        self.range = range
        self.rect = pygame.Rect(x, y, 50, 50)  # Define a área da torre

    def attack(self, enemy):
        """Verifica se o inimigo está dentro do alcance e ataca"""
        if self.is_in_range(enemy):
            enemy.take_damage(self.damage)
            print(f"Torre atacou {enemy.name} causando {self.damage} de dano.")

    def is_in_range(self, enemy):
        """Verifica se o inimigo está dentro do alcance da torre, considerando distância"""
        # Calcula a distância entre o centro da torre e o centro do inimigo
        distance = math.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2)
        return distance <= self.range

    def draw(self, screen):
        """Desenha a torre na tela"""
        pygame.draw.rect(screen, (0, 0, 255), self.rect)  # Azul