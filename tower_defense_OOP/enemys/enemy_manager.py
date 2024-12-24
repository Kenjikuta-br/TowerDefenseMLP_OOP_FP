class EnemyManager:
    def __init__(self, delta_time=0):
        self.__enemies = []
        self.__delta_time = delta_time

    @property
    def enemies(self):
        """Getter para acessar a lista de inimigos."""
        return self.__enemies

    @enemies.setter
    def enemies(self, enemies):
        """Setter para definir a lista de inimigos."""
        if isinstance(enemies, list):  # Verifica se é uma lista
            self.__enemies = enemies
        else:
            raise ValueError("Enemies deve ser uma lista.")
        
    @property
    def delta_time(self):
        """Getter para acessar o delta_time"""
        return self.__delta_time

    @delta_time.setter
    def delta_time(self, delta_time):
        """Setter para definir delta_time."""
        self.__delta_time = delta_time
        

    def add_enemy(self, enemy):
        """Adiciona um inimigo à lista."""
        self.__enemies.append(enemy)

    def remove_enemy(self, enemy):
        """Remove um inimigo da lista, se ele existir."""
        if enemy in self.__enemies:
            self.__enemies.remove(enemy)

    def update(self):
        """Atualiza o estado de todos os inimigos."""
        for enemy in self.enemies:
            if not enemy.is_dead:
                enemy.move()
                enemy.update_animation(self.delta_time)

    def draw(self, screen):
        """Desenha todos os inimigos na tela."""
        for enemy in self.__enemies:
            enemy.draw(screen)
