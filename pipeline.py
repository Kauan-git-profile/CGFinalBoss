from matematica import Vetor3
from rasterizador import Rasterizador


class Pipeline:
    """
    Pipeline gráfico clássico:
    Model → View → Projection → NDC → Viewport → Rasterização
    """

    def __init__(self, camera, rasterizador, largura, altura):
        self.camera = camera
        self.rasterizador = rasterizador
        self.largura = largura
        self.altura = altura

    # =========================
    # VIEWPORT
    # =========================
    def _viewport(self, v):
        """
        Converte NDC [-1,1] para coordenadas de tela
        """
        x = int((v.x + 1) * 0.5 * self.largura)
        y = int((1 - (v.y + 1) * 0.5) * self.altura)
        return Vetor3(x, y, v.z)

    # =========================
    # DESENHA UM OBJETO
    # =========================
    def desenhar_objeto(self, tela, objeto, cena):
        """
        Percorre todos os triângulos do objeto
        e aplica o pipeline completo.
        """
        for v1, v2, v3, normal in objeto.malha.obter_triangulos():

            # ===== MODEL =====
            w1 = objeto.transformar_vertice(v1)
            w2 = objeto.transformar_vertice(v2)
            w3 = objeto.transformar_vertice(v3)

            # ===== VIEW + PROJECTION =====
            c1 = self.camera.pipeline_camera(w1)
            c2 = self.camera.pipeline_camera(w2)
            c3 = self.camera.pipeline_camera(w3)

            # Clipping simples (descarta atrás da câmera)
            if c1.z < -1 or c2.z < -1 or c3.z < -1:
                continue

            # ===== VIEWPORT =====
            s1 = self._viewport(c1)
            s2 = self._viewport(c2)
            s3 = self._viewport(c3)

            # ===== RASTERIZAÇÃO =====
            self.rasterizador.desenhar_triangulo(
                tela,
                s1, s2, s3,
                normal,
                cena.luz.posicao,
                self.camera.posicao,
                cena.material
            )

    # =========================
    # DESENHA A CENA
    # =========================
    def desenhar_cena(self, tela, cena):
        for objeto in cena.objetos:
            self.desenhar_objeto(tela, objeto, cena)
