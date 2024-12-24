from .enemy import Enemy

class Wolf(Enemy):
    def __init__(self, x, y, path, player, manager):
        # Wolves have high speed and moderate health, but they deal less damage
        super().__init__(name="Wolf", health=80, x=x, y=y, speed=3, 
                         manager=manager, path=path, reward_money=15, player=player, damage=8)
        self._pack_attack = False  # Wolves can activate pack attack for extra damage
        animations = {
            "walk_down": self.load_spritesheet("tower_defense_OOP/assets/wolf/walk/D_Walk.png", rows=1, cols=6),
            "walk_up": self.load_spritesheet("tower_defense_OOP/assets/wolf/walk/U_Walk.png", rows=1, cols=6),
            "walk_side": self.load_spritesheet("tower_defense_OOP/assets/wolf/walk/S_Walk.png", rows=1, cols=6),
            "death_down": self.load_spritesheet("tower_defense_OOP/assets/wolf/death/D_Death.png", rows=1, cols=6),
            "death_up": self.load_spritesheet("tower_defense_OOP/assets/wolf/death/U_Death.png", rows=1, cols=6),
            "death_side": self.load_spritesheet("tower_defense_OOP/assets/wolf/death/S_Death.png", rows=1, cols=6),
        }

        self.animations = animations
    
    def activate_pack_attack(self):
        """Wolves can trigger a pack attack, increasing their damage"""
        self._pack_attack = True
        self.damage = 12  # Increases damage when pack attack is activated
        print(f"{self.name} activated pack attack! Damage increased to {self.damage}.")
    
    def move(self):
        """Override move to allow for faster movement"""
        super().move()  # Wolves move faster
        if self._pack_attack:
            self.speed = 7  # Increase speed during pack attack
    
    def die(self):
        """Override to show a different death message"""
        print(f"The {self.name} was hunted down!")
        super().die()
