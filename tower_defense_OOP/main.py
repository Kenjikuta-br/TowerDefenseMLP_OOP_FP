import pygame
from tower import Tower
from enemy import Enemy
import settings

# Initialize Pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")

# Initialize the tower and the enemy
tower = Tower(200, 250, 10, 300)
enemy = Enemy("Goblin", 100, 50, 250, 1)

# Main game loop
running = True
while running:
    screen.fill(settings.BACKGROUND_COLOR)

    # Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Enemy movement
    enemy.move()

    # Tower attacks if the enemy is within range
    tower.attack(enemy)

    # Draw the tower and the enemy
    tower.draw(screen)
    enemy.draw(screen)

    # Update the screen
    pygame.display.update()

    # Set the game frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
