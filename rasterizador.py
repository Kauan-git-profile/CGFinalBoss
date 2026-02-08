from matematica import Vetor3
from iluminacao import phong, sombreamento_constante


class Rasterizador:
    """
    Rasterizador clássico:
    - varre triângulos
    - testa z-buffer
    - desenha pixel a pixel
    """

    def __init__(self, largura, altura, zbuffer, modo_phong=True):
        self.largura = largura
        self.altura = altura
        self.zbuffer = zbuffer
        self.modo_phong = modo_phong

    # =========================
    # DESENHA UM TRIÂNGULO
    # =========================
    def desenhar_triangulo(
        self,
        tela,
        v1, v2, v3,          # vértices em coordenadas de tela (x,y,z)
        normal,
        pos_luz,
        pos_camera,
        material
    ):
        # Bounding box
        min_x = int(max(0, min(v1.x, v2.x, v3.x)))
        max_x = int(min(self.largura - 1, max(v1.x, v2.x, v3.x)))
        min_y = int(max(0, min(v1.y, v2.y, v3.y)))
        max_y = int(min(self.altura - 1, max(v1.y, v2.y, v3.y)))

        # Área do triângulo (barycentric)
        area = self._area(v1, v2, v3)
        if area == 0:
            return

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                p = Vetor3(x + 0.5, y + 0.5, 0)

                w1 = self._area(p, v2, v3) / area
                w2 = self._area(v1, p, v3) / area
                w3 = self._area(v1, v2, p) / area

                if w1 >= 0 and w2 >= 0 and w3 >= 0:
                    # Interpolação de profundidade
                    z = w1 * v1.z + w2 * v2.z + w3 * v3.z

                    if self.zbuffer.testar_e_atualizar(x, y, z):

                        # Posição do pixel no espaço 3D (aprox.)
                        pos_pixel = Vetor3(
                            w1 * v1.x + w2 * v2.x + w3 * v3.x,
                            w1 * v1.y + w2 * v2.y + w3 * v3.y,
                            z
                        )

                        if self.modo_phong:
                            cor = phong(
                                normal,
                                pos_pixel,
                                pos_luz,
                                pos_camera,
                                material
                            )
                        else:
                            luz_dir = pos_luz - pos_pixel
                            cor = sombreamento_constante(
                                normal,
                                luz_dir
                            )

                        tela.set_at((x, y), cor)

    # =========================
    # FUNÇÕES AUXILIARES
    # =========================
    def _area(self, a, b, c):
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
