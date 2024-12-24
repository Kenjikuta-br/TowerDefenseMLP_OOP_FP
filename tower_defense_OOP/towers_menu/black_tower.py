from .tower import Tower


class BlackTower(Tower):
    def __init__(self, x, y, damage, range, sprite_path, manager):
        super().__init__(x, y, damage, range, "Black Tower", sprite_path, manager)