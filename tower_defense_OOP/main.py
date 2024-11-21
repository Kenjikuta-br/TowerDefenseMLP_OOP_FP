import pygame
from tower import Tower
from enemy import Enemy
import settings

# Inicializa o Pygame
pygame.init()

# Configura a tela do jogo
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")

# Inicializa a torre e o inimigo
tower = Tower(200, 250, 10, 300)
enemy = Enemy("Goblin", 100, 50, 250, 1)

# Loop principal do jogo
running = True
while running:
    screen.fill(settings.BACKGROUND_COLOR)

    # Verifica os eventos (como o fechamento da janela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento do inimigo
    enemy.move()

    # Torre ataca se o inimigo estiver dentro do alcance
    tower.attack(enemy)

    # Desenha a torre e o inimigo
    tower.draw(screen)
    enemy.draw(screen)

    # Atualiza a tela
    pygame.display.update()

    # Define a taxa de atualização do jogo
    pygame.time.Clock().tick(60)

# Encerra o Pygame
pygame.quit()