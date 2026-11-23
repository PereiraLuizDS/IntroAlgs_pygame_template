"""
ARQUIVO: src/tela.py
RESPONSABILIDADE: Tela principal da partida.
Desenha o tabuleiro quadriculado (área de movimentação), o painel lateral de estatísticas
e gerencia o loop ativo enquanto o jogador está na fase.
"""
import pygame
from pygame.locals import QUIT
from sys import exit
from sprites import Soldado, Espia

# =====================================================================
# 1. INICIALIZAÇÃO E CONFIGURAÇÕES DA JANELA
# =====================================================================
pygame.init()

LARGURA = 1200
ALTURA = 700
FPS = 60  # Limita o jogo a 60 quadros por segundo

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Missão Brasil - Meu Game, Minha Vida")
relogio = pygame.time.Clock()

# =====================================================================
# 2. CORES E FONTES
# =====================================================================
BRANCO = (255, 255, 255)
AZUL_BEBE = (173, 216, 230)
PRETO = (0, 0, 0)
CINZA_BORDA = (80, 80, 80)
VERMELHO = (255, 0, 0)
AZUL_HD = (9, 132, 227)

fonte_titulo = pygame.font.SysFont("arial", 22, bold=True)
fonte_valor = pygame.font.SysFont("arial", 18)

# =====================================================================
# 3. DIMENSÕES DO TABULEIRO E DO PAINEL LATERAL
# =====================================================================
TAMANHO_QUADRADO = 10  # Cada célula da grade tem 10x10 pixels

# O tabuleiro ocupa 90 colunas (900px) e 70 linhas (700px)
COLUNAS = (LARGURA // TAMANHO_QUADRADO) - 30
LINHAS = ALTURA // TAMANHO_QUADRADO

# O painel lateral começa exatamente onde o tabuleiro termina (x = 900)
INICIO_PAINEL_X = COLUNAS * TAMANHO_QUADRADO  # 900px
LARGURA_PAINEL = LARGURA - INICIO_PAINEL_X    # 300px


# =====================================================================
# 4. FUNÇÕES DE DESENHO DO CENÁRIO E PAINEL
# =====================================================================
def desenhar_tabuleiro():
    """Desenha o fundo quadriculado estilo 'The World's Hardest Game' (0 a 900px)."""
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            cor = BRANCO if (linha + coluna) % 2 == 0 else AZUL_BEBE
            pos_x = coluna * TAMANHO_QUADRADO
            pos_y = linha * TAMANHO_QUADRADO
            pygame.draw.rect(tela, cor, (pos_x, pos_y, TAMANHO_QUADRADO, TAMANHO_QUADRADO))


def desenhar_caixa_info(y, altura_caixa, titulo, valor):
    """Cria um cartão de informação no painel lateral direito."""
    margem = 20
    largura_caixa = LARGURA_PAINEL - (margem * 2)  # 260px
    x_caixa = INICIO_PAINEL_X + margem             # 920px

    retangulo = pygame.Rect(x_caixa, y, largura_caixa, altura_caixa)
    pygame.draw.rect(tela, CINZA_BORDA, retangulo, 2, border_radius=6)

    texto_titulo = fonte_titulo.render(titulo, True, AZUL_BEBE)
    texto_valor = fonte_valor.render(valor, True, BRANCO)
    tela.blit(texto_titulo, (x_caixa + 12, y + 8))
    tela.blit(texto_valor, (x_caixa + 12, y + 38))


def desenhar_painel_estatisticas(nome_player="---", tempo="00:00", melhor_tempo="---"):
    """Desenha todo o painel lateral direito (900 a 1200px)."""
    desenhar_caixa_info(y=20,  altura_caixa=70,  titulo="Player:", valor=nome_player)
    desenhar_caixa_info(y=110, altura_caixa=70,  titulo="Tempo:", valor=tempo)
    desenhar_caixa_info(y=200, altura_caixa=80,  titulo="Melhor (Até o momento):", valor=melhor_tempo)
    desenhar_caixa_info(y=300, altura_caixa=380, titulo="Rank Geral:", valor="1. ---")


# =====================================================================
# 5. LOOP PRINCIPAL DO JOGO
# =====================================================================
def executar_tela_jogo():
    # 5.0 Configuração inicial da fase (posições de início)
    POSICAO_INICIAL_ESPIA = (50, 50)
    espia = Espia(*POSICAO_INICIAL_ESPIA)
    soldado = Soldado(x=400, y=300, vel_x=10)
    soldado2 = Soldado(x=450, y=301, vel_x=3)

    hd_rect = pygame.Rect(800, 600, 22, 22)
    hd_coletado = False

    while True:
        # 5.1 Tratamento de eventos (teclado, mouse, fechar janela)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        # 5.2 Atualização de movimento dos personagens
        espia.mover(INICIO_PAINEL_X, ALTURA)
        
        soldado.atualizar(INICIO_PAINEL_X, ALTURA)
        soldado2.atualizar(INICIO_PAINEL_X, ALTURA)
       
       
        # 5.3 Verificação de colisões e regras da partida
        if  espia.rect.colliderect(soldado.rect) or espia.rect.colliderect(soldado2.rect):
            espia.rect.topleft = POSICAO_INICIAL_ESPIA
            hd_coletado = False

        if not hd_coletado and espia.rect.colliderect(hd_rect):
            hd_coletado = True

        # 5.4 Limpeza e desenho dos elementos na tela (do fundo para frente)
        tela.fill(PRETO)
        desenhar_tabuleiro()

        if not hd_coletado:
            pygame.draw.rect(tela, AZUL_HD, hd_rect)

        soldado.desenhar(tela)
        soldado2.desenhar(tela)
        espia.desenhar(tela)
        desenhar_painel_estatisticas()

        # 5.5 Atualização do monitor e controle de velocidade
        pygame.display.update()
        relogio.tick(FPS)