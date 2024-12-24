from .enemy import Enemy

class Goblin(Enemy):
    def __init__(self, x, y, path, player, manager):
        # Goblins have more health and damage but are slower 
        super().__init__(name="Goblin", health=100, x=x, y=y, speed=3, 
                         manager=manager, path=path, reward_money=20, player=player, damage=15)
        self._stealth = False  # Goblins have a stealth ability that can be toggled
        animations = {
            "walk_down": self.load_spritesheet("tower_defense_OOP/assets/goblin/walk/D_Walk.png", rows=1, cols=6),
            "walk_up": self.load_spritesheet("tower_defense_OOP/assets/goblin/walk/U_Walk.png", rows=1, cols=6),
            "walk_side": self.load_spritesheet("tower_defense_OOP/assets/goblin/walk/S_Walk.png", rows=1, cols=6),
            "death_down": self.load_spritesheet("tower_defense_OOP/assets/goblin/death/D_Death.png", rows=1, cols=6),
            "death_up": self.load_spritesheet("tower_defense_OOP/assets/goblin/death/U_Death.png", rows=1, cols=6),
            "death_side": self.load_spritesheet("tower_defense_OOP/assets/goblin/death/S_Death.png", rows=1, cols=6),
        }

        self.animations = animations
    
    def toggle_stealth(self):
        """Goblins can toggle their stealth mode."""
        self._stealth = not self._stealth
        print(f"Stealth mode: {'Activated' if self._stealth else 'Deactivated'}")
    
    def move(self):
        """Override to add stealth functionality"""
        if self._stealth:
            # Goblins move slower while in stealth mode
            self._speed = 1
        else:
            self._speed = 3
        
        super().move()  # Call the parent class move method

    def die(self):
        """Override to show a different death message"""
        print(f"The {self.name} was slain!")
        super().die()
