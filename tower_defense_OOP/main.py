import pygame
from tower import Tower
from enemy import Enemy
from menu import Menu
import settings

# Initialize Pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")

# Initialize the tower and the enemy
# x, y, damage, range
# tower = Tower(200, 250, 10, 150, "tower_defense_OOP/assets/teste.png")
tower = None # Inicialmente, não há torre
# x, y
menu = Menu(100, 100, tower)
# Atualize o menu com as opções corretas
menu.update_options()



# name, health, x, y, speed
# enemy = Enemy("Goblin", 10000, 50, 250, 1)

# Main game loop
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    screen.fill(settings.BACKGROUND_COLOR)

    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            clicked_option = menu.handle_click(mouse_pos)
            if clicked_option == "Criar Torre 1":
                tower = Tower(100, 100, 10, 150,"torre 1" ,"tower_defense_OOP/assets/teste.png")
                menu.tower = tower  # Atualiza a torre no menu
                menu.toggle_visibility()
            elif clicked_option == "Vender Torre":
                tower.sell()
                tower = None  # Remove a torre após vender
                menu.tower = None  # Atualiza o menu para refletir que não há mais torre
                menu.toggle_visibility()

    # Enemy movement
    # enemy.move()

    # Tower attacks if the enemy is within range
    # tower.attack(enemy)

    # Draw the tower and the enemy
    if tower != None:
        tower.draw(screen)
    menu.draw(screen)
    # enemy.draw(screen)

    # Update the screen
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

# Quit Pygame
pygame.quit()
