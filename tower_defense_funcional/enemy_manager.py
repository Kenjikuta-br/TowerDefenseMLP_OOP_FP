from enemy import move_enemy, update_animation, draw_enemy

def create_enemy_manager(delta_time=0):
    return {
        'enemies': [],
        'delta_time': delta_time
    }



def add_enemy(enemy_manager, enemy):
        """Adiciona um inimigo à lista."""
        enemy_manager['enemies'].append(enemy)

def remove_enemy(enemy_manager, enemy):
    """Remove um inimigo da lista, se ele existir."""
    if enemy in enemy_manager['enemies']:
        enemy_manager['enemies'].remove(enemy)

def update(enemy_manager):
        """Atualiza o estado de todos os inimigos."""
        for enemy in enemy_manager['enemies']:
            if not enemy['is_dead']:
                move_enemy(enemy)
                update_animation(enemy, enemy_manager['delta_time'])

def draw(enemy_manager, screen):
    """Desenha todos os inimigos na tela."""
    for enemy in enemy_manager['enemies']:
        draw_enemy(enemy, screen)


