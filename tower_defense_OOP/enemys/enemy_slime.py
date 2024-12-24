from .enemy import Enemy

class Slime(Enemy):
    def __init__(self, x, y, path, player, manager):
        # Slime has lower health and speed, but a special healing ability
        super().__init__(name="Slime", health=50, x=x, y=y, speed=2, 
                         manager=manager, path=path, reward_money=10, player=player, damage=5)
        self._healing_rate = 1  # Slime heals itself slowly over time

        animations = {
            "walk_down": self.load_spritesheet("tower_defense_OOP/assets/slime/walk/D_Walk.png", rows=1, cols=6),
            "walk_up": self.load_spritesheet("tower_defense_OOP/assets/slime/walk/U_Walk.png", rows=1, cols=6),
            "walk_side": self.load_spritesheet("tower_defense_OOP/assets/slime/walk/S_Walk.png", rows=1, cols=6),
            "death_down": self.load_spritesheet("tower_defense_OOP/assets/slime/death/D_Death.png", rows=1, cols=6),
            "death_up": self.load_spritesheet("tower_defense_OOP/assets/slime/death/U_Death.png", rows=1, cols=6),
            "death_side": self.load_spritesheet("tower_defense_OOP/assets/slime/death/S_Death.png", rows=1, cols=6),
        }

        self.animations = animations


            
    def move(self):
        """Override the move method to allow for healing"""
        if not self.is_dead:
            #self.health += self._healing_rate  # Heal over time
            super().move()  # Move according to the parent class' movement method
    
    def die(self):
        """Override to display special death message"""
        print(f"The {self.name} was squished!")
        super().die()
