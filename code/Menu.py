#!/usr/bin/python
# -*- coding: utf-8 -*-
# A primeira linha (shebang) indica qual interpretador usar no Linux/Unix.
# A segunda define a codificação do arquivo como UTF-8 (boa prática para lidar com acentos e caracteres especiais).

import pygame
# Importa a biblioteca pygame, usada para jogos em Python.

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


# Importa constantes definidas em outro arquivo do projeto:
# WIN_WIDTH → largura da janela
# COLOR_ORANGE → cor laranja em RGB
# MENU_OPTION → lista com textos das opções do menu
# COLOR_WHITE → cor branca em RGB

class Menu:
    def __init__(self, window):
        # Construtor da classe Menu.
        # 'window' é a janela do jogo onde o menu será desenhado.
        self.window = window

        # Carrega a imagem de fundo do menu a partir da pasta 'asset'.
        self.surf = pygame.image.load('./asset/MenuBg.png')

        # Pega o retângulo da imagem (posição e tamanho).
        # Aqui já define que ela começa no canto superior esquerdo (0,0).
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self ):
        # Carrega e toca a música do menu em loop infinito.
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0

        # Loop principal do menu.
        while True:
            # Desenha a imagem de fundo do menu na janela.
            self.window.blit(source=self.surf, dest=self.rect)

            # Desenha os títulos principais do menu.
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            # Desenha as opções do menu vindas da lista MENU_OPTION.
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_ORANGE, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    # Cada opção é posicionada mais abaixo (200 + 25 * i).
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            # Atualiza a tela (flip troca os buffers de vídeo).
            pygame.display.flip()

            # Captura e trata os eventos do pygame.
            for event in pygame.event.get():
                # Se o usuário clicar no botão de fechar a janela:
                if event.type == pygame.QUIT:
                    print('Quitting...')  # Mensagem no console.
                    pygame.quit()  # Fecha o pygame.
                    quit()  # Encerra o programa.

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]



    # ------------------------------------------------------------
    # Função auxiliar para desenhar texto na tela do menu
    # ------------------------------------------------------------
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Cria a fonte do texto com nome, tamanho e estilo.
        text_font: pygame.font.Font = pygame.font.SysFont('Lucida Sans Typewriter', text_size)

        # Renderiza o texto em uma superfície com cor e transparência.
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()

        # Cria um retângulo para centralizar o texto na posição desejada.
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)

        # Desenha o texto na janela.
        self.window.blit(source=text_surf, dest=text_rect)
