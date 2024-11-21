import pygame

class Enemy:
    def __init__(self, name, health, x, y, speed):
        self.name = name
        self.health = health
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(x, y, 30, 30)  # Define a área do inimigo

    def take_damage(self, amount):
        """Método para receber dano"""
        self.health -= amount
        if self.health <= 0:
            self.die()  # Chama o método para matar o inimigo quando a saúde é zero

    def move(self):
        """Movimenta o inimigo para a direita"""
        self.x += self.speed
        self.rect.x = self.x

    def draw(self, screen):
        """Desenha o inimigo na tela"""
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Vermelho

    def die(self):
        """Método que mata o inimigo, colocando-o fora da tela"""
        print(f"{self.name} foi derrotado!")
        self.x = +1000  # Coloca o inimigo fora da tela
        self.rect.x = self.x

    def __del__(self):
        """Método destrutor chamado quando o objeto é destruído"""
        print(f"{self.name} foi destruído.")
        # Aqui você pode realizar ações adicionais, como liberar recursos ou limpar associações, se necessário.