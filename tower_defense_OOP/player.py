import pygame


class Player:
    def __init__(self, money):
        self._money = money

    # Getter for money
    @property
    def money(self):
        return self._money

    # Setter for money
    @money.setter
    def money(self, value):
        self._money = max(0, value)  # O dinheiro não pode ser negativo

    def add_money(self, amount):
        """Adiciona dinheiro ao jogador."""
        if amount > 0:
            self._money += amount

    def spend_money(self, amount):
        """Deduz dinheiro do jogador, se ele tiver saldo suficiente."""
        if 0 <= amount <= self._money:
            self._money -= amount
            return True
        return False  # Retorna False se não houver saldo suficiente

    def draw_money(self, screen, font, position=(10, 10), color=(255, 255, 255)):
        """
        Desenha o dinheiro do jogador na tela.
        
        :param screen: Superfície do Pygame onde o texto será desenhado.
        :param player: Instância da classe Player.
        :param font: Fonte do texto (objeto pygame.font.Font).
        :param position: Posição do texto na tela (x, y).
        :param color: Cor do texto (RGB).
        """
        money_text = f"Dinheiro: ${self.money}"
        money_surface = font.render(money_text, True, color)
        screen.blit(money_surface, position)
