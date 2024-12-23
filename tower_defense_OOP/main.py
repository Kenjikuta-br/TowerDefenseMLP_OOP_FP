import pygame
from player import Player
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

def draw_grid(screen, grid_width, grid_height, cell_width=64, cell_height=110, color=(255, 255, 255)):
    """
    Draws a simple grid on the screen at specified multiples of cell_width and cell_height.
    
    :param screen: The Pygame screen surface to draw the grid on.
    :param grid_width: The width of the screen or area where the grid will be drawn.
    :param grid_height: The height of the screen or area where the grid will be drawn.
    :param cell_width: The width of each grid cell (default is 64 pixels).
    :param cell_height: The height of each grid cell (default is 110 pixels).
    :param color: The color of the grid lines (default is white).
    """
    # Draw vertical lines (every cell_width pixels)
    for x in range(0, grid_width, cell_width):
        pygame.draw.line(screen, color, (x, 0), (x, grid_height))
    
    # Draw horizontal lines (every cell_height pixels)
    for y in range(0, grid_height, cell_height):
        pygame.draw.line(screen, color, (0, y), (grid_width, y))

# Criar fonte para desenhar o texto
font = pygame.font.Font(None, 36)

# Criar instância do jogador
player = Player(money=1000)

# Criação do TowerMenuManager
tower_menu_manager = TowerMenuManager()

def can_build_here(x,y):
    x_step = 64
    y_step = 110
    #superior left, cause has the display of money
    if(0*x_step <= x < 4*x_step and 0*y_step <= y < 1*y_step):
        return False
    #path of the enemies, cant have towers there
    elif(5*x_step <= x < 20*x_step and 1*y_step <= y < 2*y_step):
        return False 
    elif(5*x_step <= x < 17*x_step and 2*y_step <= y < 3*y_step):
        return False 
    elif(16*x_step <= x < 17*x_step and 3*y_step <= y < 5*y_step):
        return False 
    elif(0*x_step <= x < 17*x_step and 4*y_step <= y < 5*y_step):
        return False 
    else:
        return True

x_start, x_end = 0, 1280  # Bounds for x
y_start, y_end = 0, 660   # Bounds for y

x_step = 64  # Increment for x
y_step = 110 # Increment for y

for y in range(y_start, y_end, y_step):
    for x in range(x_start, x_end, x_step):

        if(can_build_here(x,y)):
            tower_menu_manager.add_menu(x,y,tower_menu_manager)

        

# name, health, x, y, speed
enemy_manager = EnemyManager()

#path
path = [(1056, 495), (1056, 275), (352, 275), (352,165), (1280, 156)]

# Criar inimigos//  self, name, health, x, y, speed, manager, path
enemy1 = Enemy("Goblin", 100, 0, 495, 2, enemy_manager,path)
enemy2 = Enemy("Orc", 150, 0, 495, 1, enemy_manager, path)

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
            for i in range(71):
                clicked_option = menus[i].handle_click(mouse_pos)
                if clicked_option:
                    tower_menu_manager.handle_menu_click(clicked_option, i, player)



    # Desenhar o dinheiro do jogador
    player.draw_money(screen,font)

    tower_menu_manager.update(enemy_manager.enemies, current_time)  # Atualiza todas as torres
    tower_menu_manager.draw(screen)  # Desenha todas as torres e projéteis

    draw_grid(screen, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)  # Draw the grid with the screen's size

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
