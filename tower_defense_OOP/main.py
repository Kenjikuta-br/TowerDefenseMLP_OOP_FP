import pygame
from tower import Tower
from enemy import Enemy
from menu import Menu
from enemy_manager import EnemyManager
from tower_menu_manager import TowerMenuManager
import settings

# Initialize Pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")

# Criação do TowerMenuManager
tower_menu_manager = TowerMenuManager()

tower_menu_manager.add_menu(100,100,tower_menu_manager)
tower_menu_manager.add_menu(300,100,tower_menu_manager)
tower_menu_manager.add_menu(500,100,tower_menu_manager)
tower_menu_manager.add_menu(700,100,tower_menu_manager)

# name, health, x, y, speed
enemy_manager = EnemyManager()

# Criar inimigos
enemy1 = Enemy("Goblin", 100, 50, 50, 2, enemy_manager)
enemy2 = Enemy("Orc", 150, 100, 50, 1, enemy_manager)

clock = pygame.time.Clock()
running = True
dt = 0



# Main game loop
while running:
    screen.fill(settings.BACKGROUND_COLOR)

     # Track elapsed time (in seconds)
    current_time = pygame.time.get_ticks() / 1000  # Get time in seconds

    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for interactions with the mouse and treat the Menu interactions
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
             # Itera sobre cada menu para verificar se houve um clique
            menus = tower_menu_manager.menus
            towers = tower_menu_manager.towers
            for i in range(4):
                clicked_option = menus[i].handle_click(mouse_pos)
                if clicked_option:
                    tower_menu_manager.handle_menu_click(menus[i], towers, clicked_option, i)


    tower_menu_manager.update(enemy_manager.enemies, current_time)  # Atualiza todas as torres
    tower_menu_manager.draw(screen)  # Desenha todas as torres e projéteis

    # Atualizar inimigos no loop do jogo
    enemy_manager.update()
    enemy_manager.draw(screen)


    # Update the screen
    pygame.display.update()


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

# Quit Pygame
pygame.quit()
