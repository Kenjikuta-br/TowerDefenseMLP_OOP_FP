import pygame

class Enemy:
    def __init__(self, name, health, x, y, speed):
        self.name = name
        self.health = health
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(x, y, 30, 30)  # Defines the area of the enemy

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
        """Method that kills the enemy by moving it off the screen"""
        print(f"{self.name} was defeated!")
        self.x = +1000  # Moves the enemy off the screen
        self.rect.x = self.x

    def __del__(self):
        """Destructor method called when the object is destroyed"""
        print(f"{self.name} was destroyed.")
        # Here you can perform additional actions, like releasing resources or cleaning up associ