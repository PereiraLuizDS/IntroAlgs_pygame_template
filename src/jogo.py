"""
ARQUIVO: src/jogo.py
RESPONSABILIDADE: Arquivo principal (Ponto de entrada do jogo).
Controla o fluxo de estados entre a tela de Menu (Inicio.py) e a tela da Partida (tela.py).
"""
from Inicio import executar_tela_menu
from tela import executar_tela_jogo, tela, relogio


def iniciar_sistema():
    estado_atual = "MENU"

    while True:
        if estado_atual == "MENU":
            estado_atual = executar_tela_menu(tela, relogio)

        elif estado_atual == "JOGAR":
            estado_atual = executar_tela_jogo()


if __name__ == "__main__":
    iniciar_sistema()