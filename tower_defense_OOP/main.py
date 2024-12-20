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


# Initialize the towers and their respective menus
towers = []
menus = []

# Criando 4 torres com seus menus correspondentes
tower1 = None 
menu1 = Menu(100, 100, tower1)

tower2 = None 
menu2 = Menu(300, 100, tower2)

tower3 = None 
menu3 = Menu(500, 100, tower3)

tower4 = None 
menu4 = Menu(700, 100, tower4)

# Adiciona as torres e menus nas listas
towers.extend([tower1, tower2, tower3, tower4])
menus.extend([menu1, menu2, menu3, menu4])

# Atualize o menu com as opções corretas
# menu.update_options()



# name, health, x, y, speed
# enemy = Enemy("Goblin", 10000, 50, 250, 1)

# Main game loop
clock = pygame.time.Clock()
running = True
dt = 0

def handle_menu_click(menu, tower, clicked_option, index):
    """Função que lida com a interação do menu e realiza ações correspondentes."""
    if clicked_option == "Criar Torre 1":
        new_tower = Tower(menu.x, menu.y, 10, 150, "torre1", "tower_defense_OOP/assets/teste.png")
        menu.tower = new_tower
        towers[index] = new_tower  # Substitui None pela nova torre
        print("criando torre")
        menu.toggle_visibility()
    elif clicked_option == "Vender Torre":
        menu.tower.sell()
        tower = None # Remove a torre após vender
        menu.tower = None   # Atualiza o menu para refletir que não há mais torre
        menu.toggle_visibility()

while running:
    screen.fill(settings.BACKGROUND_COLOR)

    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
             # Itera sobre cada menu para verificar se houve um clique
            for i in range(4):
                clicked_option = menus[i].handle_click(mouse_pos)
                if clicked_option:
                    handle_menu_click(menus[i], towers[i], clicked_option, i)

    # Enemy movement
    # enemy.move()

    # Tower attacks if the enemy is within range
    # tower.attack(enemy)

    # Draw the towers and the menus
    for tower in towers:
        if tower != None:
            tower.draw(screen) 
    for menu in menus:
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
