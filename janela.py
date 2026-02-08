import pygame


class Janela:
    """
    Responsável apenas por:
    - criar a janela
    - fornecer a superfície de desenho (framebuffer)
    - atualizar a tela
    """

    def __init__(self, largura, altura, titulo="Modelador 3D"):
        pygame.init()

        self.largura = largura
        self.altura = altura

        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption(titulo)

        self.clock = pygame.time.Clock()

    # =========================
    # LIMPA FRAMEBUFFER
    # =========================
    def limpar(self, cor=(0, 0, 0)):
        self.tela.fill(cor)

    # =========================
    # ATUALIZA JANELA
    # =========================
    def atualizar(self, fps=60):
        pygame.display.flip()
        self.clock.tick(fps)

    # =========================
    # FINALIZA
    # =========================
    def fechar(self):
        pygame.quit()
