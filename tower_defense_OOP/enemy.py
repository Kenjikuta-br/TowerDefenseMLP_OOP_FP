import pygame
class Enemy:
    def __init__(self, name, health, x, y, speed, manager):
        self.name = name
        self.health = health
        self.x = x
        self.y = y
        self.speed = speed
        self.manager = manager  # Referência ao gerenciador
        self.manager.add_enemy(self)  # Adiciona o inimigo automaticamente
        self.rect = pygame.Rect(x, y, 30, 30)  # Defines the area of the enemy
        self.is_dead = False  # Inicializa o atributo is_dead

    def take_damage(self, amount):
        """Method to receive damage"""
        self.health -= amount
        if self.health <= 0:
            self.die()  # Calls the method to kill the enemy when health reaches zero

    def move(self):
        """Moves the enemy to the right"""
        self.x += self.speed
        self.rect.x = self.x

    def draw(self, screen):
        """Draws the enemy on the screen"""
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Red

    def die(self):
        """Kills the enemy by marking it as dead and removing it from the game"""
        self.is_dead = True
        print(f"{self.name} was defeated!")
        #if self in enemies_list:  # Check if the enemy is still in the list
        #    enemies_list.remove(self)  # Remove the enemy from the list
        self.manager.remove_enemy(self)  # Remove o inimigo do gerenciador
       

    def __del__(self):
        """Destructor method to clean up resources when the enemy is destroyed"""
        if not self.is_dead:
            print(f"Warning: {self.name} was not properly destroyed!")
        else:
            print(f"{self.name} was destroyed and cleaned up.")
        # Clean up additional resources if necessary (e.g., sounds, images, etc.)

        