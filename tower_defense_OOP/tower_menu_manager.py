import pygame
from tower import Tower
from menu import Menu

import pygame
from tower import Tower
from menu import Menu

class TowerMenuManager:
    def __init__(self):
        self.__towers = []  # Lista privada de torres
        self.__menus = []   # Lista privada de menus

    @property
    def towers(self):
        """Getter para acessar a lista de torres."""
        return self.__towers

    @towers.setter
    def towers(self, towers):
        """Setter para definir a lista de torres."""
        if isinstance(towers, list):  # Verifica se o valor é uma lista
            self.__towers = towers
        else:
            print("Erro: O valor precisa ser uma lista de torres.")

    @property
    def menus(self):
        """Getter para acessar a lista de menus."""
        return self.__menus

    @menus.setter
    def menus(self, menus):
        """Setter para definir a lista de menus."""
        if isinstance(menus, list):  # Verifica se o valor é uma lista
            self.__menus = menus
        else:
            print("Erro: O valor precisa ser uma lista de menus.")

    def add_menu(self, x, y, manager):
        """Adiciona um novo menu à lista de menus"""
        tower = None
        menu = Menu(x, y, manager, tower)
        self.__towers.append(tower)
        self.__menus.append(menu)

    def add_tower(self, x, y, damage, range, tower_type, sprite_path, index=None):
        """Substitui uma torre existente na lista ou adiciona uma nova torre"""
        tower = Tower(x, y, damage, range, tower_type, sprite_path)
        
        if index is not None and 0 <= index < len(self.__towers):
            # Substitui a torre existente no índice fornecido
            self.__towers[index] = tower
            print(f"Torre {tower_type} substituída no índice {index} em ({x}, {y})")
        else:
            # Caso o índice não seja válido ou não seja fornecido, adiciona ao final
            self.__towers.append(tower)
            print(f"Torre {tower_type} adicionada em ({x}, {y})")

    def remove_tower(self, tower):
        """Remove uma torre da lista de torres"""
        if tower in self.__towers:
            self.__towers.remove(tower)
            print(f"Torre {tower.type} removida.")

    def update(self, enemies, current_time):
        """Atualiza o estado de todas as torres (disparo, projéteis, etc.)"""
        for tower in self.__towers:
            if tower != None:
                tower.attack(enemies, current_time)  # Cada torre verifica se há inimigos dentro do alcance
                tower.update_projectiles()  # Atualiza todos os projéteis da torre

    def draw(self, screen):
        """Desenha todas as torres e seus projéteis"""
        for tower in self.__towers:
            if tower != None:
                tower.draw(screen)  # Desenha cada torre
        for menu in self.__menus:
            menu.draw(screen)  # Desenha cada menu

    def handle_menu_click(self, menu, towers, clicked_option, index):
        """Função que lida com a interação do menu e realiza ações correspondentes."""
        if clicked_option == "Criar Torre 1":
            #x, y, damage, range, type, sprite_path
            new_tower = Tower(menu.x, menu.y, 10, 200, "torre1", "tower_defense_OOP/assets/teste.png", self)
            menu.tower = new_tower
            towers[index] = new_tower  # Substitui None pela nova torre
            print("criando torre")
            menu.toggle_visibility()
        elif clicked_option == "Vender Torre":
            menu.tower.sell()
            towers[index] = None # Remove a torre após vender
            menu.tower = None   # Atualiza o menu para refletir que não há mais torre
            menu.toggle_visibility()
