import math

from janela import Janela
from entrada import Entrada
from cena import Cena
from cubo import Cubo
from objeto3d import Objeto3D
from camera import Camera
from zbuffer import ZBuffer
from rasterizador import Rasterizador
from pipeline import Pipeline


# =========================
# CONFIGURAÇÕES
# =========================
LARGURA = 800
ALTURA = 600
FPS = 60


def main():
    # =========================
    # JANELA
    # =========================
    janela = Janela(LARGURA, ALTURA, "Modelador 3D - Computação Gráfica")

    # =========================
    # CENA
    # =========================
    cena = Cena()

    # Cria dois cubos (como no enunciado)
    cubo1 = Objeto3D(Cubo(1.0))
    cubo1.transladar(-1.2, 0, 0)

    cubo2 = Objeto3D(Cubo(1.0))
    cubo2.transladar(1.2, 0, 0)

    cena.adicionar_objeto(cubo1)
    cena.adicionar_objeto(cubo2)

    # =========================
    # CÂMERA
    # =========================
   # =========================
    # CÂMERA
    # =========================
    from matematica import Vetor3

    camera = Camera(
        posicao=Vetor3(0, 0, 5),
        alvo=Vetor3(0, 0, 0)
    )


    # =========================
    # Z-BUFFER
    # =========================
    zbuffer = ZBuffer(LARGURA, ALTURA)

    # =========================
    # RASTERIZADOR
    # =========================
    rasterizador = Rasterizador(
        LARGURA,
        ALTURA,
        zbuffer,
        modo_phong=True
    )

    # =========================
    # PIPELINE
    # =========================
    pipeline = Pipeline(
        camera,
        rasterizador,
        LARGURA,
        ALTURA
    )

    # =========================
    # ENTRADA
    # =========================
    entrada = Entrada(cena, rasterizador)

    # =========================
    # LOOP PRINCIPAL
    # =========================
    rodando = True
    while rodando:
        rodando = entrada.processar()

        janela.limpar((20, 20, 20))
        zbuffer.limpar()

        pipeline.desenhar_cena(janela.tela, cena)

        janela.atualizar(FPS)

    janela.fechar()


if __name__ == "__main__":
    main()
