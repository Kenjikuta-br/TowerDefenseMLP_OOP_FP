import pygame

# Constantes para o tamanho da torre
X_TOWER = 64
Y_TOWER = 110

def create_menu(x, y, manager, tower=None):
    """Cria um menu com posição, opções e visibilidade"""
    return {
        'x': x,
        'y': y,
        'width': 64,
        'height': 110,
        'font': pygame.font.Font(None, 12),  # Fonte do texto
        'background_color': (50, 50, 50),
        'text_color': (255, 255, 255),
        'is_visible': False,
        'option_height': 30,
        'tower': tower,
        'manager': manager,
        'options': []
    }

def toggle_visibility(menu):
    """Alterna a visibilidade do menu"""
    menu['is_visible'] = not menu['is_visible']

def show_visibility(menu):
    """Deixa visível o Menu"""
    menu['is_visible'] = True

def hide_visibility(menu):
    """Deixa invisível o Menu"""
    menu['is_visible'] = False

def update_options(menu):
    """Atualiza as opções do menu dependendo do estado da torre"""
    if menu['tower'] is None:
        menu['options'] = ["Criar Torre 1", "Criar Torre 2", "Criar Torre 3"]
    else:
        menu['options'] = ["Vender Torre", "Upgrade Torre"]

def draw(menu, screen):
    """Desenha o menu e suas opções."""
    if menu['is_visible']:
        update_options(menu)  # Atualiza as opções dependendo do estado da torre

        # Desenhar o fundo do menu
        pygame.draw.rect(screen, menu['background_color'], (menu['x'], menu['y'], menu['width'], menu['height']))

        # Desenhar as opções do menu
        for i, option in enumerate(menu['options']):
            text_surface = menu['font'].render(option, True, menu['text_color'])
            screen.blit(text_surface, (menu['x'] + 10, menu['y'] + i * menu['option_height'] + 5))
    elif not menu['is_visible'] and menu['tower'] is None:
        # Desenhar o fundo do menu
        pygame.draw.rect(screen, menu['background_color'], (menu['x'], menu['y'], X_TOWER, Y_TOWER))

def handle_click(menu, mouse_pos):
    """Lida com cliques no menu."""
    if menu['is_visible']:
        # Verifica se o clique foi dentro do menu
        if menu['x'] <= mouse_pos[0] <= menu['x'] + menu['width'] and menu['y'] <= mouse_pos[1] <= menu['y'] + menu['height']:
            # Identifica qual opção foi clicada
            index = (mouse_pos[1] - menu['y']) // menu['option_height']
            if index < len(menu['options']):
                return menu['options'][index]  # Retorna a opção selecionada
        else:
            toggle_visibility(menu)  # Alterna a visibilidade
    else:
        # Verifica se o clique foi dentro da área do menu para ativar ou desativar a visibilidade
        if menu['x'] <= mouse_pos[0] <= menu['x'] + menu['width'] and menu['y'] <= mouse_pos[1] <= menu['y'] + menu['height']:
            toggle_visibility(menu)  # Alterna a visibilidade
    return None  # Retorna None e o menu atualizado
