def create_wave(number, enemies, spawn_delay, next_wave_delay):
    return {
        'number': number,
        'enemies': enemies,  # Lista de inimigos na wave [(EnemyClass, quantidade), ...]
        'spawn_delay': spawn_delay,
        'next_wave_delay': next_wave_delay
    }