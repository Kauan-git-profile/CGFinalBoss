class ZBuffer:
    """
    Z-buffer clássico:
    guarda a menor profundidade (z) já desenhada em cada pixel.
    """

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.limpar()

    # =========================
    # LIMPA O Z-BUFFER
    # =========================
    def limpar(self):
        """
        Inicializa todas as profundidades com infinito
        (nenhum pixel desenhado ainda).
        """
        self.buffer = [
            [float('inf') for _ in range(self.largura)]
            for _ in range(self.altura)
        ]

    # =========================
    # TESTE DE PROFUNDIDADE
    # =========================
    def testar_e_atualizar(self, x, y, z):
        """
        Retorna True se o pixel deve ser desenhado
        (ou seja, está mais próximo da câmera).
        """
        if x < 0 or x >= self.largura or y < 0 or y >= self.altura:
            return False

        if z < self.buffer[y][x]:
            self.buffer[y][x] = z
            return True

        return False
