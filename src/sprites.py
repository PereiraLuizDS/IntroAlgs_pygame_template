"""
ARQUIVO: src/sprites.py
RESPONSABILIDADE: Define os personagens e objetos móveis do jogo (Espiã, Soldados, Gerente).
"""
import pygame


class Espia:
    def __init__(self, x, y, largura=20, altura=20, velocidade=5):
        # Cria o retângulo da personagem na posição inicial (x, y)
        self.rect = pygame.Rect(x, y, largura, altura)
        self.velocidade = velocidade
        self.cor = (0, 184, 148)  # Verde Exército Brasileiro

    def mover(self, limite_largura, limite_altura):
        # Verifica quais teclas estão pressionadas no momento
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.rect.y += self.velocidade

        # Limita o movimento para não sair da tela nem entrar no painel lateral (900px)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > limite_largura:
            self.rect.right = limite_largura
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > limite_altura:
            self.rect.bottom = limite_altura

    def desenhar(self, tela):
        # Desenha o retângulo preenchido e uma borda preta fina para destaque
        pygame.draw.rect(tela, self.cor, self.rect)
        pygame.draw.rect(tela, (0, 0, 0), self.rect, 2)