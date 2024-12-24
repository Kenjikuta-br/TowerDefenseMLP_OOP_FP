import pygame


class Player:
    def __init__(self, money, base_health):
        self._money = money
        self._base_health = base_health

    # Getter for money
    @property
    def money(self):
        return self._money

    # Setter for money
    @money.setter
    def money(self, value):
        self._money = max(0, value)  # Money cannot be negative

    # Getter for health
    @property
    def base_health(self):
        return self._base_health

    # Setter for health
    @base_health.setter
    def base_health(self, value):
        self._base_health = max(0, value)  # Health cannot be negative

    def add_money(self, amount):
        """Adds money to the player."""
        if amount > 0:
            self._money += amount

    def spend_money(self, amount):
        """Deducts money from the player if they have enough balance."""
        if 0 <= amount <= self._money:
            self._money -= amount
            return True
        return False  # Returns False if there isn't enough balance

    def gain_health(self, amount):
        """Increases the player's health by a specified amount."""
        if amount > 0:
            self._base_health += amount

    def lose_health(self, amount):
        """Decreases the player's health by a specified amount."""
        if amount > 0:
            self._base_health = max(0, self._base_health - amount)  # Health cannot go below zero

    def draw_status(self, screen, font, position=(10, 10), color=(255, 255, 255)):
        """
        Draws the player's money and health on the screen.

        :param screen: Pygame surface where the text will be drawn.
        :param font: Font object for rendering text.
        :param position: Starting position for the money display (x, y).
        :param color: Text color (RGB).
        """
        # Draw money
        money_text = f"Dinheiro: ${self.money}"
        money_surface = font.render(money_text, True, color)
        screen.blit(money_surface, position)

        # Draw health below money
        health_text = f"Vida: {self.base_health} HP"
        health_surface = font.render(health_text, True, color)
        screen.blit(health_surface, (position[0], position[1] + 30))  # Offset for health below money
