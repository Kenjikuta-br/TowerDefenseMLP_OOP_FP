import pygame
from enemys.enemy_goblin import Goblin
from enemys.enemy_slime import Slime
from enemys.enemy_wolf import Wolf

class WaveManager:
    def __init__(self, start_x, start_y, enemy_manager, player, path):
        self.x = start_x #x where the enemies are spawned
        self.y = start_y #y where the enemies are spawned
        self.enemy_manager = enemy_manager  # Referência ao gerenciador de inimigos
        self.player = player  # Referência ao jogador
        self.waves = []  # Lista de todas as waves
        self.current_wave_index = -1  # Índice da wave atual
        self.time_since_last_spawn = 0  # Tempo desde o último spawn
        self.time_since_last_wave = 0  # Tempo desde o final da última wave
        self.enemies_to_spawn = []  # Lista de inimigos restantes na wave atual
        self.path = path #path que os inimigos tem de passar
        self.display_wave_timer = 0  # Timer para exibir "Wave começou!"

    def add_wave(self, wave):
        self.waves.append(wave)

    def start_next_wave(self):
        """Inicia a próxima wave"""
        self.current_wave_index += 1
        if self.current_wave_index < len(self.waves):
            wave = self.waves[self.current_wave_index]
            print(f"Wave {wave.number} começou!")
            self.enemies_to_spawn = []
            for enemy_class, count in wave.enemies:
                self.enemies_to_spawn.extend([enemy_class] * count)
            self.time_since_last_spawn = 0
            self.display_wave_timer = 1.5  # Exibir "Wave começou!" por 3 segundos
        else:
            print("Todas as waves foram completadas!")

    def update(self, delta_time):
        """Atualiza a lógica das waves"""
        if self.current_wave_index >= len(self.waves):
            return  # Todas as waves foram completadas
        
        # Atualizar o timer de exibição do texto da wave
        if self.display_wave_timer > 0:
            self.display_wave_timer -= delta_time


        # Se ainda há inimigos para spawnar na wave atual
        if self.enemies_to_spawn:
            self.time_since_last_spawn += delta_time
            current_wave = self.waves[self.current_wave_index]
            if self.time_since_last_spawn >= current_wave.spawn_delay:
                enemy_class = self.enemies_to_spawn.pop(0)  # Pega o próximo inimigo
                self.spawn_enemy(enemy_class)
                self.time_since_last_spawn = 0
        # Se todos os inimigos foram spawnados e mortos, inicia a próxima wave
        elif not self.enemy_manager.enemies:  # Verifica se todos os inimigos foram derrotados
            self.time_since_last_wave += delta_time
            current_wave = self.waves[self.current_wave_index]
            if self.time_since_last_wave >= current_wave.next_wave_delay:
                self.time_since_last_wave = 0
                self.start_next_wave()

    def spawn_enemy(self, enemy_class):
        """Spawna um inimigo no jogo"""


        if enemy_class== Goblin:
            enemy = enemy_class(self.x, self.y, self.path, self.player, self.enemy_manager)
        elif enemy_class == Slime:
            enemy = enemy_class(self.x, self.y, self.path, self.player, self.enemy_manager)
        elif enemy_class == Wolf:
            enemy = enemy_class(self.x, self.y, self.path, self.player, self.enemy_manager)
        else:
            raise ValueError("Unknown enemy class")

        print(f"Spawnando inimigo: {enemy.name}")

    def draw(self, screen, font_timer, font_big):
        """Desenha informações da wave na tela"""
        if self.current_wave_index < len(self.waves) and self.current_wave_index >= 0:
            wave_number = self.waves[self.current_wave_index].number
            next_wave_timer = max(0, self.waves[self.current_wave_index].next_wave_delay - self.time_since_last_wave)

            # Desenhar a wave atual e o tempo para a próxima wave
            wave_text = font_timer.render(f"Wave Atual: {wave_number}", True, (255, 255, 255))
            next_wave_text = font_timer.render(f"Próxima wave em: {int(next_wave_timer)}s", True,  (255, 255, 255))

            screen.blit(wave_text, (10, 600))
            screen.blit(next_wave_text, (10, 630))

        # Exibir "Wave começou!" em grande quando uma nova wave iniciar
        if self.display_wave_timer > 0:
            wave_start_text = font_big.render(f"Wave {self.waves[self.current_wave_index].number} começou!", True, (255, 0, 0))
            text_rect = wave_start_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(wave_start_text, text_rect)
