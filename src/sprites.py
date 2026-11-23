"""
ARQUIVO: src/sprites.py
RESPONSABILIDADE: Define os personagens e objetos móveis do jogo (Espiã, Soldados, Gerente).
"""
import pygame


# =====================================================================
# 1. PROTAGONISTA: ESPIÃ DO EXÉRCITO BRASILEIRO
# =====================================================================
class Espia:
    def __init__(self, x, y, largura=20, altura=20, velocidade=5):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.velocidade = velocidade
        self.cor = (0, 184, 148)  # Verde Exército Brasileiro

    def mover(self, limite_largura, limite_altura):
        """Move a Espiã com Setas ou WASD e impede que saia do tabuleiro."""
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.rect.y += self.velocidade

        # Trava nas bordas do tabuleiro (0 a 900px de largura / 0 a 700px de altura)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > limite_largura:
            self.rect.right = limite_largura
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > limite_altura:
            self.rect.bottom = limite_altura

    def desenhar(self, tela):
        """Desenha o retângulo da Espiã com borda preta."""
        pygame.draw.rect(tela, self.cor, self.rect)
        pygame.draw.rect(tela, (0, 0, 0), self.rect, 2)


# =====================================================================
# 2. INIMIGOS: SOLDADOS DA NVIDIDIOS
# =====================================================================
class Soldado:
    def __init__(self, x, y, vel_x=4, vel_y=3, tamanho=24):
        self.rect = pygame.Rect(x, y, tamanho, tamanho)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.cor = (214, 48, 49)  # Vermelho

    def atualizar(self, limite_largura, limite_altura):
        """Movimenta o soldado e inverte a direção ao encostar nas bordas."""
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.left <= 0 or self.rect.right >= limite_largura:
            self.vel_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= limite_altura:
            self.vel_y *= -1

    def desenhar(self, tela):
        """Desenha o círculo vermelho do Soldado com borda preta."""
        pygame.draw.circle(tela, self.cor, self.rect.center, 12)
        pygame.draw.circle(tela, (0, 0, 0), self.rect.center, 12, 2)