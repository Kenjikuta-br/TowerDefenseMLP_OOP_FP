from .ice_tower import IceTower
from .electric_tower import ElectricTower
from .black_tower import BlackTower
from .menu import Menu

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

    def add_tower(self, tower, index=None):
        """Substitui uma torre existente na lista ou adiciona uma nova torre"""
        print(f"index:{index}")
        print(f"lenght:{len(self.__towers)}")
        
        if index is not None and 0 <= index < len(self.__towers):
            # Substitui a torre existente no índice fornecido
            self.__towers[index] = tower
            print(f"Torre {tower.type} substituída no índice {index} em ({tower.x}, {tower.y})")


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
                tower.draw_tower(screen)  # Desenha cada torre
        for menu in self.__menus:
            menu.draw(screen)  # Desenha cada menu
        for tower in self.__towers:
            if tower != None:
                tower.draw_projectiles(screen)  # Desenha cada torre
        

    
    def handle_menu_click(self, clicked_option, index, player):
        menus = self.menus
        menu = menus[index]
        towers = self.towers

        # Define the costs of the towers
        tower_costs = {
            "Criar Torre 1": 100,  # Cost for Tower 1
            "Criar Torre 2": 150,  # Cost for Ice Tower
            "Criar Torre 3": 200   # Cost for Electric Tower
        }

        """Função que lida com a interação do menu e realiza ações correspondentes."""
        if clicked_option in tower_costs:
            # Check if the player has enough money
            cost = tower_costs[clicked_option]
            if player.money >= cost:
                if clicked_option == "Criar Torre 1":
                    # Create Tower 1
                    new_tower = BlackTower(menu.x, menu.y, 10, 200, "tower_defense_OOP/assets/black_tower.png", self)
                    self.add_tower(new_tower, index)
                    menu.tower = new_tower
                    print("Criando Torre 1")
                elif clicked_option == "Criar Torre 2":
                    # Create Ice Tower
                    new_tower = IceTower(menu.x, menu.y, 10, 200, "tower_defense_OOP/assets/ice_tower.png", self, 2)
                    self.add_tower(new_tower, index)
                    menu.tower = new_tower
                    print("Criando Torre 2")
                elif clicked_option == "Criar Torre 3":
                    # Create Electric Tower
                    new_tower = ElectricTower(menu.x, menu.y, 10, 200, "tower_defense_OOP/assets/electric_tower.png", self)
                    self.add_tower(new_tower, index)
                    menu.tower = new_tower
                    print("Criando Torre 3")
                
                # Deduct the cost from the player's money
                player.money -= cost
                print(f"Dinheiro restante: {player.money}")
                
                # Toggle menu visibility
                menu.toggle_visibility()
            else:
                print("Dinheiro insuficiente para criar essa torre!")
        elif clicked_option == "Vender Torre":
            if menu.tower:
                # Add money back to the player when selling the tower
                sell_price = 50  # Example: Towers are sold for 50 (adjust as needed)
                player.money += sell_price
                print(f"Vendendo Torre. Dinheiro ganho: {sell_price}. Dinheiro total: {player.money}")
                
                # Remove the tower
                menu.tower.sell()
                towers[index] = None  # Remove the tower from the list
                menu.tower = None     # Update the menu to reflect no tower
                menu.toggle_visibility()
            else:
                print("Nenhuma torre para vender!")

