import pygame
import math


class Entrada:
    """
    Processa teclado para:
    - mover / rotacionar / escalar objetos
    - trocar objeto selecionado
    - alternar sombreamento
    """

    def __init__(self, cena, rasterizador):
        self.cena = cena
        self.rasterizador = rasterizador

        # Velocidades
        self.vel_trans = 0.05
        self.vel_rot = math.radians(2)
        self.vel_escala = 1.02

    # =========================
    # PROCESSA EVENTOS
    # =========================
    def processar(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:
                self._tecla_pressionada(evento.key)

        return True

    # =========================
    # MAPA DE TECLAS
    # =========================
    def _tecla_pressionada(self, tecla):

        # === Seleção de objeto ===
        if tecla == pygame.K_TAB:
            self.cena.proximo_objeto()

        # === Translação ===
        elif tecla == pygame.K_w:
            self.cena.transladar_objeto(0, 0, -self.vel_trans)
        elif tecla == pygame.K_s:
            self.cena.transladar_objeto(0, 0, self.vel_trans)
        elif tecla == pygame.K_a:
            self.cena.transladar_objeto(-self.vel_trans, 0, 0)
        elif tecla == pygame.K_d:
            self.cena.transladar_objeto(self.vel_trans, 0, 0)
        elif tecla == pygame.K_q:
            self.cena.transladar_objeto(0, self.vel_trans, 0)
        elif tecla == pygame.K_e:
            self.cena.transladar_objeto(0, -self.vel_trans, 0)

        # === Rotação ===
        elif tecla == pygame.K_i:
            self.cena.rotacionar_objeto(-self.vel_rot, 0, 0)
        elif tecla == pygame.K_k:
            self.cena.rotacionar_objeto(self.vel_rot, 0, 0)
        elif tecla == pygame.K_j:
            self.cena.rotacionar_objeto(0, -self.vel_rot, 0)
        elif tecla == pygame.K_l:
            self.cena.rotacionar_objeto(0, self.vel_rot, 0)
        elif tecla == pygame.K_u:
            self.cena.rotacionar_objeto(0, 0, -self.vel_rot)
        elif tecla == pygame.K_o:
            self.cena.rotacionar_objeto(0, 0, self.vel_rot)

        # === Escala uniforme ===
        elif tecla == pygame.K_EQUALS or tecla == pygame.K_PLUS:
            self.cena.escalar_objeto(self.vel_escala)
        elif tecla == pygame.K_MINUS:
            self.cena.escalar_objeto(1 / self.vel_escala)

        # === Alternar sombreamento ===
        elif tecla == pygame.K_p:
            self.rasterizador.modo_phong = not self.rasterizador.modo_phong
