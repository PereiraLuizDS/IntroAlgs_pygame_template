"""
ARQUIVO: src/Inicio.py
RESPONSABILIDADE: Tela inicial (Menu) do jogo Missão Brasil.
Exibe o título, a história resumida da missão e aguarda o jogador pressionar 0.
"""
import pygame
from pygame.locals import QUIT
from sys import exit

# =====================================================================
# 1. CORES E TEXTOS DO MENU
# =====================================================================
FUNDO_MENU = (25, 30, 35)
VERDE_BRASIL = (0, 184, 148)
AMARELO_OURO = (253, 203, 110)
BRANCO = (255, 255, 255)


# =====================================================================
# 2. LOOP DA TELA DE MENU
# =====================================================================
def executar_tela_menu(tela, relogio):
    fonte_titulo = pygame.font.SysFont("arial", 42, bold=True)
    fonte_subtitulo = pygame.font.SysFont("arial", 22)
    fonte_instrucao = pygame.font.SysFont("arial", 24, bold=True)

    while True:
        # 2.1 Tratamento de eventos (fechar janela ou apertar 0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                return "JOGAR"

        # 2.2 Limpeza da tela
        tela.fill(FUNDO_MENU)

        # 2.3 Desenho dos textos centralizados na tela (1200x700)
        titulo = fonte_titulo.render("MISSÃO BRASIL: MEU GAME, MINHA VIDA", True, AMARELO_OURO)
        subtitulo = fonte_subtitulo.render("Infiltre-se na Nvividios, roube o HD de IA e jogue na lixeira do banheiro!", True, BRANCO)
        instrucao = fonte_instrucao.render("Pressione 0 para iniciar a operação", True, VERDE_BRASIL)

        tela.blit(titulo, (600 - titulo.get_width() // 2, 220))
        tela.blit(subtitulo, (600 - subtitulo.get_width() // 2, 300))
        tela.blit(instrucao, (600 - instrucao.get_width() // 2, 420))

        # 2.4 Atualização do monitor
        pygame.display.update()
        relogio.tick(60)