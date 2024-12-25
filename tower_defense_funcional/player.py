def create_player(money, base_health):
    """Cria um novo jogador com um valor inicial de dinheiro"""
    return {
        'money': money,
        'base_health': base_health
    }

def add_money(player, amount):
    """Adiciona dinheiro ao jogador"""
    if amount > 0:
        player['money'] += amount

def spend_money(player, amount):
    """Deduz dinheiro do jogador, se ele tiver saldo suficiente"""
    if 0 <= amount <= player['money']:
        player['money'] -= amount
        return True
    return False  # Retorna False se não houver saldo suficiente

def gain_health(player, amount):
    """Aumenta a saúde do jogador em uma quantidade especificada"""
    if amount > 0:
        player['base_health'] += amount

def lose_health(player, amount):
    """Diminui a saúde do jogador em uma quantidade especificada"""
    if amount > 0:
        player['base_health'] = max(0, player['base_health'] - amount)  # A saúde não pode ser negativa
    return player  # Retorna o jogador atualizado



def draw_status(player, screen, font, position=(10, 10), color=(0, 0, 0)):
    """
    Desenha o dinheiro e a saúde do jogador na tela.

    :param player: Dicionário contendo o dinheiro e a saúde do jogador.
    :param screen: Superfície Pygame onde o texto será desenhado.
    :param font: Objeto de fonte para renderizar texto.
    :param position: Posição inicial para a exibição do dinheiro (x, y).
    :param color: Cor do texto (RGB).
    """
    # Desenha o dinheiro
    money_text = f"Money: {player['money']}"
    money_surface = font.render(money_text, True, color)
    screen.blit(money_surface, position)

    # Draw health below money
    health_text = f"Vida: {player['base_health']} HP"
    health_surface = font.render(health_text, True, color)
    screen.blit(health_surface, (position[0], position[1] + 30))  # Offset for health below money