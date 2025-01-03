import pygame
from player import Player
from towers_menu import TowerMenuManager
from enemys import Enemy, Slime, Goblin, Wolf, EnemyManager
from towers_menu import Menu
from waves import WaveManager, Wave
import settings

# Initialize Pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")


def draw_grid(screen, grid_width, grid_height, cell_width=64, cell_height=110, color=(255, 255, 255)):
    """
    Draws a simple grid on the screen at specified multiples of cell_width and cell_height.
    """
    for x in range(0, grid_width, cell_width):
        pygame.draw.line(screen, color, (x, 0), (x, grid_height))
    for y in range(0, grid_height, cell_height):
        pygame.draw.line(screen, color, (0, y), (grid_width, y))

def can_build_here(x, y):
    """
    Determines whether a tower can be built at the given x, y coordinates.
    """
    x_step = 64
    y_step = 110
    # Forbidden regions
    if 0 * x_step <= x < 4 * x_step and 0 * y_step <= y < 1 * y_step:
        return False
    elif 5 * x_step <= x < 20 * x_step and 1 * y_step <= y < 2 * y_step:
        return False
    elif 5 * x_step <= x < 17 * x_step and 2 * y_step <= y < 3 * y_step:
        return False
    elif 16 * x_step <= x < 17 * x_step and 3 * y_step <= y < 5 * y_step:
        return False
    elif 0 * x_step <= x < 17 * x_step and 4 * y_step <= y < 5 * y_step:
        return False
    return True

def main():
    # Initialize player
    player = Player(money=450, base_health=100)

    # Create TowerMenuManager
    tower_menu_manager = TowerMenuManager()

    # Setup menus for tower placement
    x_start, x_end = 0, 1280
    y_start, y_end = 0, 660
    x_step = 64
    y_step = 110
    
    for y in range(y_start, y_end, y_step):
        for x in range(x_start, x_end, x_step):
            if can_build_here(x, y):
                tower_menu_manager.add_menu(x, y, tower_menu_manager)

    # Setup enemy manager and path
    enemy_manager = EnemyManager()
    path = [(1032, 471), (1032, 251), (328, 251), (328, 141), (1280, 141)]
    
    wave_manager = WaveManager(0, 471, enemy_manager, player, path)

    # Configurando as waves
    wave1 = Wave(1, [(Slime, 5)], 1, 5)  # 5 Slimes, 1 segundo entre cada spawn, 5 segundos até a próxima wave
    wave2 = Wave(2, [(Slime, 5), (Wolf, 2), (Slime, 5)], 1, 5) 
    wave3 = Wave(3, [(Wolf, 5), (Goblin, 1)], 0.75, 5) 
    wave4 = Wave(4, [(Goblin, 3)], 0.75, 5) 
    wave5 = Wave(5, [(Slime, 10), (Goblin, 5)], 0.5, 5)  


    wave_manager.add_wave(wave1)
    wave_manager.add_wave(wave2)
    wave_manager.add_wave(wave3)
    wave_manager.add_wave(wave4)
    wave_manager.add_wave(wave5)

    # Começando a primeira wave
    wave_manager.start_next_wave()


    # Setup clock and game loop
    clock = pygame.time.Clock()
    running = True

    # Variables to track time
    last_time = pygame.time.get_ticks() / 1000  # Time at the start
    delta_time = 0

    # Font for rendering text
    font = pygame.font.Font(None, 36)
    font_big = pygame.font.Font(None, 100)

    while running:
        screen.fill(settings.BACKGROUND_COLOR)

        # Track elapsed time (in seconds)
        current_time = pygame.time.get_ticks() / 1000

        # Calculate delta time (time difference between frames)
        delta_time = current_time - last_time  # Time that passed since last frame
        
        # Store current time for the next iteration
        last_time = current_time

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                menus = tower_menu_manager.menus
                for i in range(len(menus)):
                    clicked_option = menus[i].handle_click(mouse_pos)
                    if clicked_option:
                        tower_menu_manager.handle_menu_click(clicked_option, i, player)

    

        # Update and draw towers
        tower_menu_manager.update(enemy_manager.enemies, current_time)
        tower_menu_manager.draw(screen)

        # Draw grid
        draw_grid(screen, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        # Update and draw enemies
        enemy_manager.update(delta_time)
        enemy_manager.draw(screen)

        # Draw player status
        player.draw_status(screen, font)

        # Update and draw wave_manager
        wave_manager.update(delta_time)
        wave_manager.draw(screen, font, font_big)



        # Update the screen
        pygame.display.update()

        # Limit FPS to 60
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
