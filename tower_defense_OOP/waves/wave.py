class Wave:
    def __init__(self, number, enemies, spawn_delay, next_wave_delay):
        self.number = number  # Número da wave
        self.enemies = enemies  # Lista de inimigos na wave [(EnemyClass, quantidade), ...]
        self.spawn_delay = spawn_delay  # Intervalo entre o spawn de inimigos
        self.next_wave_delay = next_wave_delay  # Tempo até a próxima wave começar
