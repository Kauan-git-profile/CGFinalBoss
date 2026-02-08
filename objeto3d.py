from matematica import (
    Matriz4,
    matriz_translacao,
    matriz_rotacao_x,
    matriz_rotacao_y,
    matriz_rotacao_z,
    matriz_escala
)


class Objeto3D:
    """
    Objeto 3D genérico da cena.
    Contém uma malha (ex: Cubo) e sua matriz de modelagem.
    """

    def __init__(self, malha):
        self.malha = malha

        # Parâmetros de transformação
        self.tx = 0.0
        self.ty = 0.0
        self.tz = 0.0

        self.rx = 0.0
        self.ry = 0.0
        self.rz = 0.0

        self.escala = 1.0  # escala uniforme (obrigatório)

        self.matriz_model = Matriz4.identidade()
        self.atualizar_matriz_model()

    # =========================
    # ATUALIZA MATRIZ MODEL
    # =========================
    def atualizar_matriz_model(self):
        """
        Ordem correta:
        Escala → Rotação → Translação
        """
        m_escala = matriz_escala(self.escala)
        m_rx = matriz_rotacao_x(self.rx)
        m_ry = matriz_rotacao_y(self.ry)
        m_rz = matriz_rotacao_z(self.rz)
        m_trans = matriz_translacao(self.tx, self.ty, self.tz)

        self.matriz_model = (
            m_trans *
            m_rz *
            m_ry *
            m_rx *
            m_escala
        )

    # =========================
    # TRANSFORMAÇÕES
    # =========================
    def transladar(self, dx, dy, dz):
        self.tx += dx
        self.ty += dy
        self.tz += dz
        self.atualizar_matriz_model()

    def rotacionar_x(self, angulo):
        self.rx += angulo
        self.atualizar_matriz_model()

    def rotacionar_y(self, angulo):
        self.ry += angulo
        self.atualizar_matriz_model()

    def rotacionar_z(self, angulo):
        self.rz += angulo
        self.atualizar_matriz_model()

    def escalar(self, fator):
        """
        Escala uniforme (mantém o objeto como cubo).
        """
        self.escala *= fator
        self.atualizar_matriz_model()

    # =========================
    # APLICA MODEL MATRIX
    # =========================
    def transformar_vertice(self, vertice):
        """
        Aplica a matriz de modelagem em um vértice.
        """
        from matematica import Vetor4
        v4 = Vetor4(vertice.x, vertice.y, vertice.z, 1.0)
        v_transformado = self.matriz_model.multiplicar_vetor4(v4)
        return v_transformado.to_vetor3()
