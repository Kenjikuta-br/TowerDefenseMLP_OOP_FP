from ice_tower import create_ice_tower, attack as attack_ice_tower
from electric_tower import create_electric_tower, attack as attack_electric_tower
from black_tower import create_black_tower, attack as attack_black_tower
from tower import attack, update_projectiles, draw_projectiles, sell_tower, draw_tower
from menu import create_menu, draw as draw_menu, toggle_visibility

def create_tower_menu_manager():
    return {
        'towers': [],
        'menus': []
    }

def add_menu(tower_menu_manager, x, y, manager):
    tower = None
    menu = create_menu(x, y, manager, tower)
    tower_menu_manager['towers'].append(tower)
    tower_menu_manager['menus'].append(menu)


def add_tower(tower_menu_manager, tower, index=None):
    """Substitui uma torre existente na lista ou adiciona uma nova torre"""
    print(f"index:{index}")
    print(f"lenght:{len(tower_menu_manager['towers'])}")
    
    if index is not None and 0 <= index < len(tower_menu_manager['towers']):
        # Substitui a torre existente no índice fornecido
        tower_menu_manager['towers'][index] = tower
        print(f"Torre {tower['type']} substituída no índice {index} em ({tower['x']}, {tower['y']})")


def remove_tower(tower_menu_manager, tower):
    if tower in tower_menu_manager['towers']:
        tower_menu_manager['towers'].remove(tower)
        print(f"Torre {tower['type']} removida.")


def update(tower_menu_manager, enemies, current_time):
    for tower in tower_menu_manager['towers']:
        if tower != None:
            if tower['type'] == "Black Tower":
                attack_black_tower(tower, enemies, current_time)
            elif tower['type'] == "Ice Tower":
                attack_ice_tower(tower, enemies, current_time)
            elif tower['type'] == "Electric Tower":
                attack_electric_tower(tower, enemies, current_time)
            #attack(tower, enemies, current_time)  # Cada torre verifica se há inimigos dentro do alcance

            #attack(tower, enemies, current_time)  # Cada torre verifica se há inimigos dentro do alcance         
            update_projectiles(tower)  # Atualiza todos os projéteis da torre


def draw(tower_menu_manager, screen):
    for tower in tower_menu_manager['towers']:
        if tower != None:
            draw_tower(tower, screen)
    for menu in tower_menu_manager['menus']:
        draw_menu(menu, screen)  # Desenha cada menu
    for tower in tower_menu_manager['towers']:
        if tower != None:
            draw_projectiles(tower, screen)

def handle_menu_click(tower_menu_manager, clicked_option, index, player):
    menus = tower_menu_manager['menus']
    menu = menus[index]
    towers = tower_menu_manager['towers']

    # Define the costs of the towers
    tower_costs = {
        "Black - 100": 100,  # Cost for  Black Tower
        "Ice - 150": 150,  # Cost for Ice Tower
        "Electric - 200": 200   # Cost for Electric Tower
    }

    if clicked_option in tower_costs:
        # Check if the player has enough money
        cost = tower_costs[clicked_option]
        if player['money'] >= cost:
            if clicked_option == "Black - 100":
                # Create Black Tower
                new_tower = create_black_tower(menu['x'], menu['y'], 40, 225, "tower_defense_funcional/assets/black_tower.png", tower_menu_manager, 2.0)
                add_tower(tower_menu_manager, new_tower, index)
                menu['tower'] = new_tower
                print("Criando Torre 1")
            elif clicked_option == "Ice - 150":                
                # Create Ice Tower
                new_tower = create_ice_tower(menu['x'], menu['y'], 10, 150, "tower_defense_funcional/assets/ice_tower.png", tower_menu_manager, 3, 1.0)
                add_tower(tower_menu_manager, new_tower, index)
                menu['tower'] = new_tower
                print("Criando Torre 2")
            elif clicked_option == "Electric - 200":
                # Create Electric Tower
                new_tower = create_electric_tower(menu['x'], menu['y'], 10, 130, "tower_defense_funcional/assets/electric_tower.png", tower_menu_manager, 0.5)
                add_tower(tower_menu_manager, new_tower, index)
                menu['tower'] = new_tower
                print("Criando Torre 3")

            player['money'] -= cost
            print(f"Player money: {player['money']}")
            
            toggle_visibility(menu)
        else:
            print("Dinheiro insuficiente para criar essa torre")
    elif clicked_option == "Vender Torre":
        if menu['tower']:
            sell_price = 50
            player['money'] += sell_price
            print(f"Vendendo Torre. Dinheiro ganho: {sell_price}. Dinheiro total: {player['money']}")

            sell_tower(menu['tower'])

            towers[index] = None
            menu['tower'] = None
            toggle_visibility(menu)
        else:
            print("Nenhuma torre para vender")
