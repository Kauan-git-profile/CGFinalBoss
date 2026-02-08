from matematica import Vetor3


class Luz:
    """
    Luz pontual simples.
    """
    def __init__(
        self,
        posicao=Vetor3(5, 5, 5),
        intensidade=1.0
    ):
        self.posicao = posicao
        self.intensidade = intensidade


class Material:
    """
    Material básico para Phong simplificado.
    """
    def __init__(
        self,
        ka=0.1,   # ambiente
        kd=0.7,   # difuso
        ks=0.2,   # especular
        n=10      # brilho
    ):
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.n = n


class Cena:
    """
    Cena 3D: contém objetos, luz e material.
    """

    def __init__(self):
        self.objetos = []
        self.objeto_selecionado = None

        self.luz = Luz()
        self.material = Material()

    # =========================
    # OBJETOS
    # =========================
    def adicionar_objeto(self, objeto):
        self.objetos.append(objeto)
        if self.objeto_selecionado is None:
            self.objeto_selecionado = objeto

    def selecionar_objeto(self, indice):
        if 0 <= indice < len(self.objetos):
            self.objeto_selecionado = self.objetos[indice]

    def proximo_objeto(self):
        if not self.objetos:
            return
        i = self.objetos.index(self.objeto_selecionado)
        self.objeto_selecionado = self.objetos[(i + 1) % len(self.objetos)]

    # =========================
    # TRANSFORMAÇÕES NO OBJETO ATIVO
    # =========================
    def transladar_objeto(self, dx, dy, dz):
        if self.objeto_selecionado:
            self.objeto_selecionado.transladar(dx, dy, dz)

    def rotacionar_objeto(self, rx, ry, rz):
        if self.objeto_selecionado:
            if rx != 0:
                self.objeto_selecionado.rotacionar_x(rx)
            if ry != 0:
                self.objeto_selecionado.rotacionar_y(ry)
            if rz != 0:
                self.objeto_selecionado.rotacionar_z(rz)

    def escalar_objeto(self, fator):
        if self.objeto_selecionado:
            self.objeto_selecionado.escalar(fator)

    # =========================
    # ATUALIZA LUZ / MATERIAL
    # =========================
    def mover_luz(self, dx, dy, dz):
        self.luz.posicao.x += dx
        self.luz.posicao.y += dy
        self.luz.posicao.z += dz

    def ajustar_material(self, ka=None, kd=None, ks=None, n=None):
        if ka is not None:
            self.material.ka = ka
        if kd is not None:
            self.material.kd = kd
        if ks is not None:
            self.material.ks = ks
        if n is not None:
            self.material.n = n
