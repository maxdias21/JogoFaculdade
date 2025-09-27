#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COLOR_GREEN, COLOR_CYAN
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.Entityfactory import EntityFactory

import pygame

import random

from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 2000

        if (game_mode in [MENU_OPTION[1], MENU_OPTION[2]]):
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self, ):
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()

                if isinstance(entity, (Player, Enemy)  ):
                    shoot = entity.shoot()

                    if(shoot is not None):
                        self.entity_list.append(shoot)

                if entity.name == 'Player1':
                    self.level_text(14, f'Player 1 - Health: {entity.health} | Score: {entity.score}', COLOR_GREEN, (10,25))

                if entity.name == 'Player2':
                    self.level_text(14, f'Player 2 - Health: {entity.health} | Score: {entity.score}', COLOR_CYAN, (10,43))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))




            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        # Cria a fonte do texto com nome, tamanho e estilo.
        text_font: pygame.font.Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)

        # Renderiza o texto em uma superfície com cor e transparência.
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()

        # Cria um retângulo para centralizar o texto na posição desejada.
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])

        # Desenha o texto na janela.
        self.window.blit(source=text_surf, dest=text_rect)
