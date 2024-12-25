import pygame
from player import create_player, draw_status
import settings
from tower_menu_manager import (
    create_tower_menu_manager,add_menu, handle_menu_click, update as update_tower_menu_manager, draw as draw_tower_menu_manager
)
from wave_manager import (
    create_wave_manager, add_wave, update_wave_manager, start_next_wave
)
from menu import handle_click
from wave import create_wave
from enemy_goblin import create_goblin
from enemy_slime import create_slime
from enemy_wolf import create_wolf
from enemy_manager import create_enemy_manager, update as update_enemy_manager, draw as draw_enemy_manager



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
    player = create_player(money=300, base_health=150)

    # Create TowerMenuManager
    tower_menu_manager = create_tower_menu_manager()

    # Setup menus for tower placement
    x_start, x_end = 0, 1280
    y_start, y_end = 0, 660
    x_step = 64
    y_step = 110

    for y in range(y_start, y_end, y_step):
        for x in range(x_start, x_end, x_step):
            if can_build_here(x, y):
                add_menu(tower_menu_manager,x, y, tower_menu_manager)

    # Create WaveManager
    enemy_manager = create_enemy_manager()

    path = [(1032, 471), (1032, 251), (328, 251), (328, 141), (1280, 141)]
    enemy1 = create_slime(0, 471, path,player, enemy_manager)
    enemy2 = create_wolf(0, 471, path,player, enemy_manager)


    wave_manager = create_wave_manager(start_x=0, start_y=471, enemy_manager=enemy_manager, player=player, path=path)

    # Create waves
    wave1 = create_wave(1, [(create_slime, 5)], 1, 5)
    wave2 = create_wave(2, [(create_slime, 3), (create_goblin, 2)], 1, 10)
    wave3 = create_wave(3, [(create_goblin, 4), (create_wolf, 1)], 1, 5)

    add_wave(wave_manager, wave1)
    add_wave(wave_manager, wave2)
    add_wave(wave_manager, wave3)

    start_next_wave(wave_manager)

     # Setup clock and game loop
    clock = pygame.time.Clock()
    running = True

    # Variables to track time
    last_time = pygame.time.get_ticks() / 1000  # Time at the start
    delta_time = 0

    # Font for rendering text
    font = pygame.font.Font(None, 36)

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
                menus = tower_menu_manager['menus']
                for i in range(len(menus)):
                    clicked_option = handle_click(menus[i],mouse_pos)
                    if clicked_option:
                        handle_menu_click(tower_menu_manager, clicked_option, i, player)

        # Update and draw towers and enemies
        update_tower_menu_manager(tower_menu_manager, enemy_manager['enemies'], current_time)
        draw_tower_menu_manager(tower_menu_manager, screen)

        # Draw grid
        draw_grid(screen, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        enemy_manager['delta_time'] = delta_time
        update_enemy_manager(enemy_manager)
        draw_enemy_manager(enemy_manager, screen)

        # Draw player status
        draw_status(player, screen, font)

        update_wave_manager(wave_manager, delta_time)



        # Update the screen
        pygame.display.update()

        # Limit FPS to 60
        clock.tick(60)


        
    pygame.quit()

if __name__ == "__main__":
    main()