import pygame
import math

class Enemy:
    def __init__(self, name, health, x, y, speed, manager, path, reward_money,player, damage=10):
        self._name = name
        self._health = health
        self._x = x
        self._y = y
        self._speed = speed
        self._manager = manager  # Reference to the manager
        self._manager.add_enemy(self)  # Automatically adds the enemy
        self._rect = pygame.Rect(x, y, 20, 20)  # Defines the area of the enemy
        self._is_dead = False  # Initializes the is_dead attribute
        self._is_slowed = False
        self._slow_effect = 2  # Divide speed by slow_effect if slowed
        self._path = path  # List of waypoints (e.g., [(x1, y1), (x2, y2), ...])
        self._current_waypoint = 0  # Index of the next waypoint to move towards
        self._reward_money = reward_money  # Amount of money rewarded when killed
        self.player = player  # Store the player instanc
        self.damage = damage  # Dano que o inimigo causa na base
        #Need to have this offset cause my sprite has empty space and it needs to match the sprite with the hitbox
        self.off_set_rect = 14

         # Animation setup
        self.animations = None  # Dictionary with spritesheets
        self.current_animation = "walk_side"  # Initial animation state
        self.animation_frame = 0
        self.animation_speed = 0.1  # Speed of frame changes
        self.time_accumulator = 0
        self_facing_right = True

    # Properties for reward_money
    @property
    def reward_money(self):
        return self._reward_money

    @reward_money.setter
    def reward_money(self, value):
        if value < 0:
            raise ValueError("Reward money cannot be negative.")
        self._reward_money = value

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
        self._rect.x = value  + self.off_set_rect # Update rect position when x changes

    # Property for y
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._rect.y = value  + self.off_set_rect # Update rect position when y changes

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

    
    def update_animation(self, delta_time):
        """Updates the animation frame based on time."""
        self.time_accumulator += delta_time
        if self.time_accumulator >= self.animation_speed:
            self.time_accumulator = 0
            self.animation_frame = (self.animation_frame + 1) % len(self.animations[self.current_animation])

    def draw(self, screen):
        """Draws the current frame of the animation on the screen."""
        frame = self.animations[self.current_animation][self.animation_frame]
         # Flip the frame if facing left
        if self.current_animation == "walk_side" and self._facing_right:
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, (self._x, self._y))
        #for debuggin hitbox
        #self.draw_hitbox(screen)

    def draw_hitbox(self, screen, color=(255, 0, 0)):
        """
        Draws the enemy's hitbox (rect) on the screen.
        
        Args:
            screen (pygame.Surface): The surface to draw the hitbox on.
            color (tuple): The RGB color of the hitbox (default is red).
        """
        pygame.draw.rect(screen, color, self.rect, 2)  # Draws the rect as a rectangle outline (thickness = 2)
        print(f"position of rect: x={self.rect.x} y={self.rect.y}")

    def move(self):
        """Moves the enemy along the path and updates animation direction."""
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

            # Update animation direction
            if abs(dx) > abs(dy):
                self.current_animation = "walk_side"
                self._facing_right = dx > 0  # True if moving right
            elif dy > 0:
                self.current_animation = "walk_down"
            else:
                self.current_animation = "walk_up"
        else:
            # Enemy reached the end of the path
            self.reach_base()

    def reach_base(self):
        """Causa dano à base do jogador e se remove."""
        print(f"{self.name} alcançou a base e causou {self.damage} de dano!")
        self.player.lose_health(self.damage)
        self._is_dead = True
        self.manager.remove_enemy(self)  # Remove o inimigo do jogo


    def die(self):
        """Kills the enemy by marking it as dead and removing it from the game"""
        if self.player != None:  # Ensure the player exists
            if not(self._is_dead):
                self.player.add_money(self.reward_money)  # Add money to the player
        self._is_dead = True
        print(f"{self.name} was defeated!")

        self.manager.remove_enemy(self)  # Removes the enemy from the manager

    def slow(self):
        """Applies the slow effect to the enemy"""
        self.is_slowed = True


    def load_spritesheet(self, file, rows, cols):
        """Loads a spritesheet and splits it into individual frames."""
        sheet = pygame.image.load(file).convert_alpha()
        sheet_width, sheet_height = sheet.get_size()
        frame_width = sheet_width // cols
        frame_height = sheet_height // rows
        frames = []

        for row in range(rows):
            for col in range(cols):
                frame = sheet.subsurface(pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height))
                frames.append(frame)
        return frames
    

    def __del__(self):
        """Destructor method to clean up resources when the enemy is destroyed"""
        if not self.is_dead:
            print(f"Warning: {self.name} was not properly destroyed!")
        else:
            print(f"{self.name} was destroyed and cleaned up.")
