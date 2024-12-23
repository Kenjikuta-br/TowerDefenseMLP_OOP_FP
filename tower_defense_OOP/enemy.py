import pygame
import math

class Enemy:
    def __init__(self, name, health, x, y, speed, manager, path):
        self._name = name
        self._health = health
        self._x = x
        self._y = y
        self._speed = speed
        self._manager = manager  # Reference to the manager
        self._manager.add_enemy(self)  # Automatically adds the enemy
        self._rect = pygame.Rect(x, y, 30, 30)  # Defines the area of the enemy
        self._is_dead = False  # Initializes the is_dead attribute
        self._is_slowed = False
        self._slow_effect = 2  # Divide speed by slow_effect if slowed
        self._path = path  # List of waypoints (e.g., [(x1, y1), (x2, y2), ...])
        self._current_waypoint = 0  # Index of the next waypoint to move towards

    # Property for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    # Property for health
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value

    # Property for x
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._rect.x = value  # Update rect position when x changes

    # Property for y
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._rect.y = value  # Update rect position when y changes

    # Property for speed
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Speed cannot be negative.")
        self._speed = value

    # Property for manager
    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, value):
        if not value:
            raise ValueError("Manager cannot be None.")
        self._manager = value

    # Property for rect
    @property
    def rect(self):
        return self._rect

    # Property for is_dead
    @property
    def is_dead(self):
        return self._is_dead

    # Property for is_slowed
    @property
    def is_slowed(self):
        return self._is_slowed

    @is_slowed.setter
    def is_slowed(self, value):
        self._is_slowed = value

    # Property for slow_effect
    @property
    def slow_effect(self):
        return self._slow_effect

    @slow_effect.setter
    def slow_effect(self, value):
        if value <= 0:
            raise ValueError("Slow effect must be positive.")
        self._slow_effect = value

    # Property for path
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if not isinstance(value, list):
            raise ValueError("Path must be a list of waypoints.")
        self._path = value

    # Property for current_waypoint
    @property
    def current_waypoint(self):
        return self._current_waypoint

    @current_waypoint.setter
    def current_waypoint(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Current waypoint must be a non-negative integer.")
        self._current_waypoint = value

    def take_damage(self, amount):
        """Method to receive damage"""
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")
        self.health -= amount
        if self.health <= 0:
            self.die()  # Calls the method to kill the enemy when health reaches zero

    def move(self):
        """Moves the enemy along the path"""
        if self._current_waypoint < len(self._path):
            target_x, target_y = self._path[self._current_waypoint]
            dx = target_x - self.x
            dy = target_y - self.y
            distance = math.sqrt(dx**2 + dy**2)

            # Calculate the speed considering the slow effect
            current_speed = self.speed / self._slow_effect if self._is_slowed else self.speed

            if distance <= current_speed:
                # Reached the waypoint
                self.x = target_x
                self.y = target_y
                self._current_waypoint += 1  # Move to the next waypoint
            else:
                # Move towards the waypoint
                self.x += (dx / distance) * current_speed
                self.y += (dy / distance) * current_speed

    def draw(self, screen):
        """Draws the enemy on the screen"""
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Red

    def die(self):
        """Kills the enemy by marking it as dead and removing it from the game"""
        self._is_dead = True
        print(f"{self.name} was defeated!")
        self.manager.remove_enemy(self)  # Removes the enemy from the manager

    def slow(self):
        """Applies the slow effect to the enemy"""
        self.is_slowed = True

    def __del__(self):
        """Destructor method to clean up resources when the enemy is destroyed"""
        if not self.is_dead:
            print(f"Warning: {self.name} was not properly destroyed!")
        else:
            print(f"{self.name} was destroyed and cleaned up.")
