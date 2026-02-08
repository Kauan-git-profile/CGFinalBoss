from matematica import Vetor3


class Cubo:
    """
    Cubo centrado na origem.
    As faces já vêm TRIANGULADAS (necessário para rasterização).
    """

    def __init__(self, tamanho=1.0):
        t = tamanho / 2.0

        # =========================
        # VÉRTICES
        # =========================
        self.vertices = [
            Vetor3(-t, -t, -t),  # 0
            Vetor3( t, -t, -t),  # 1
            Vetor3( t,  t, -t),  # 2
            Vetor3(-t,  t, -t),  # 3
            Vetor3(-t, -t,  t),  # 4
            Vetor3( t, -t,  t),  # 5
            Vetor3( t,  t,  t),  # 6
            Vetor3(-t,  t,  t)   # 7
        ]

        # =========================
        # FACES TRIANGULADAS
        # cada face → 2 triângulos
        # =========================
        self.triangulos = [
            # Face traseira (-Z)
            (0, 1, 2), (0, 2, 3),

            # Face frontal (+Z)
            (4, 6, 5), (4, 7, 6),

            # Face esquerda (-X)
            (0, 3, 7), (0, 7, 4),

            # Face direita (+X)
            (1, 5, 6), (1, 6, 2),

            # Face inferior (-Y)
            (0, 4, 5), (0, 5, 1),

            # Face superior (+Y)
            (3, 2, 6), (3, 6, 7)
        ]

        # =========================
        # NORMAIS POR FACE (1 por 2 triângulos)
        # =========================
        self.normais_face = [
            Vetor3( 0,  0, -1),  # traseira
            Vetor3( 0,  0,  1),  # frontal
            Vetor3(-1,  0,  0),  # esquerda
            Vetor3( 1,  0,  0),  # direita
            Vetor3( 0, -1,  0),  # inferior
            Vetor3( 0,  1,  0)   # superior
        ]

    # =========================
    # OBTÉM NORMAL DE UM TRIÂNGULO
    # =========================
    def normal_do_triangulo(self, indice_triangulo):
        """
        Cada face tem 2 triângulos.
        Usamos a normal da face correspondente.
        """
        indice_face = indice_triangulo // 2
        return self.normais_face[indice_face]

    # =========================
    # ITERADOR DE TRIÂNGULOS
    # =========================
    def obter_triangulos(self):
        """
        Retorna:
        (v1, v2, v3, normal)
        """
        for i, (i1, i2, i3) in enumerate(self.triangulos):
            v1 = self.vertices[i1]
            v2 = self.vertices[i2]
            v3 = self.vertices[i3]
            normal = self.normal_do_triangulo(i)
            yield v1, v2, v3, normal
