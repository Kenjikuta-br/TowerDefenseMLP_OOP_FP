import pygame

X_TOWER = 64
Y_TOWER = 110

class Menu:
    def __init__(self, x, y, manager, tower=None):
        self.x = x  # Posição x do menu
        self.y = y  # Posição y do menu
        self.width = 64  # Largura do menu
        self.height = 110  # Altura total do menu (ajustada dinamicamente)
        self.font = pygame.font.Font(None, 12)  # Fonte do texto
        self.background_color = (50, 50, 50)  # Cor de fundo do menu
        self.text_color = (255, 255, 255)  # Cor do texto
        self.is_visible = False  # Define se o menu está visível ou não
        self.option_height = 30  # Altura de cada opção
        self.tower = tower  # Torre na posição (pode ser None se não houver torre)
        self.manager = manager
    
    @property
    def is_visible(self):
        return self.__is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        self.__is_visible = is_visible

    @property
    def tower(self):
        return self.__tower

    @tower.setter
    def tower(self, tower):
        self.__tower = tower

    def toggle_visibility(self):
        """Alterna a visibilidade do menu."""
        self.is_visible = not self.is_visible
    
    def show_visibility(self):
        """Deixa visível o Menu"""
        self.is_visible = True
    
    def hide_visibility(self):
        """Deixa visível o Menu"""
        self.is_visible = False

    def update_options(self):
        """Atualiza as opções do menu dependendo do estado da torre"""
        if self.tower is None:
            self.options = ["Black - 100", "Ice - 150", "Electric - 200"]
        else:
            self.options = ["Vender Torre", "Upgrade Torre"]
    
    def draw(self, screen):
        """Desenha o menu e suas opções."""
        if self.is_visible:
            # Atualiza as opções dependendo do estado da torre
            self.update_options()

            # Desenhar o fundo do menu
            pygame.draw.rect(screen, self.background_color, (self.x, self.y, self.width, self.height))

            # Desenhar as opções do menu
            for i, option in enumerate(self.options):
                text_surface = self.font.render(option, True, self.text_color)
                screen.blit(text_surface, (self.x + 10, self.y + i * self.option_height + 5))
        elif not(self.is_visible) and self.tower is None:
            # Desenhar o fundo do menu
            pygame.draw.rect(screen, self.background_color, (self.x, self.y, X_TOWER, Y_TOWER))



    def handle_click(self, mouse_pos):
        """Lida com cliques no menu."""
        if self.is_visible:
            # Verifica se o clique foi dentro do menu
            if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
                # Identifica qual opção foi clicada
                index = (mouse_pos[1] - self.y) // self.option_height
                if index < len(self.options):
                    return self.options[index]  # Retorna a opção selecionada
            else:
                    self.toggle_visibility()
        else:
            #Verifica se o clique foi dentro da área do menu para ativar ou desativar a visibilidade
            if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
                self.toggle_visibility()
        return None
