from enemy_goblin import create_goblin
from enemy_slime import create_slime
from enemy_wolf import create_wolf

def create_wave_manager(start_x, start_y, enemy_manager, player, path):
    return {
        'x': start_x,
        'y': start_y,
        'enemy_manager': enemy_manager,
        'player': player,
        'waves': [],
        'current_wave_index': -1,
        'time_since_last_spawn': 0,
        'time_since_last_wave': 0,
        'enemies_to_spawn': [],
        'path': path
    }

def add_wave(wave_manager, wave):
    wave_manager['waves'].append(wave)

def start_next_wave(wave_manager):
    wave_manager['current_wave_index'] += 1
    if wave_manager['current_wave_index'] < len(wave_manager['waves']):
        wave = wave_manager['waves'][wave_manager['current_wave_index']]
        print(f"Wave {wave['number']} começou!")
        wave_manager['enemies_to_spawn'] = []
        for enemy_class, count in wave['enemies']:
            wave_manager['enemies_to_spawn'].extend([enemy_class] * count)
        wave_manager['time_since_last_spawn'] = 0
    else:
        print("Todas as waves foram completadas!")

def update_wave_manager(wave_manager, delta_time):
    if wave_manager['current_wave_index'] >= len(wave_manager['waves']):
        return  # Todas as waves foram completadas

    # Se ainda há inimigos para spawnar na wave atual
    if wave_manager['enemies_to_spawn']:
        wave_manager['time_since_last_spawn'] += delta_time
        current_wave = wave_manager['waves'][wave_manager['current_wave_index']]
        if wave_manager['time_since_last_spawn'] >= current_wave['spawn_delay']:
            enemy_class = wave_manager['enemies_to_spawn'].pop(0)  # Pega o próximo inimigo
            spawn_enemy(wave_manager, enemy_class)
            wave_manager['time_since_last_spawn'] = 0
    # Se todos os inimigos foram spawnados e mortos, inicia a próxima wave
    elif not wave_manager['enemy_manager']['enemies']:  # Verifica se todos os inimigos foram derrotados
        wave_manager['time_since_last_wave'] += delta_time
        current_wave = wave_manager['waves'][wave_manager['current_wave_index']]
        if wave_manager['time_since_last_wave'] >= current_wave['next_wave_delay']:
            wave_manager['time_since_last_wave'] = 0
            start_next_wave(wave_manager)

def spawn_enemy(wave_manager, enemy_class):
    if enemy_class == create_goblin:
        enemy = create_goblin(wave_manager['x'], wave_manager['y'], wave_manager['path'], wave_manager['player'], wave_manager['enemy_manager'])
    elif enemy_class == create_slime:
        enemy = create_slime(wave_manager['x'], wave_manager['y'], wave_manager['path'], wave_manager['player'], wave_manager['enemy_manager'])
    elif enemy_class == create_wolf:
        enemy = create_wolf(wave_manager['x'], wave_manager['y'], wave_manager['path'], wave_manager['player'], wave_manager['enemy_manager'])
    else:
        raise ValueError("Unknown enemy class")

    print(f"Spawnando inimigo: {enemy['name']}")