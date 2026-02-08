import math
from matematica import Vetor3, Vetor4, Matriz4


class Camera:
    def __init__(
        self,
        posicao=Vetor3(0, 0, 5),
        alvo=Vetor3(0, 0, 0),
        up=Vetor3(0, 1, 0),
        fov=math.radians(60),
        aspect=4/3,
        near=0.1,
        far=100.0
    ):
        self.posicao = posicao
        self.alvo = alvo
        self.up = up

        self.fov = fov
        self.aspect = aspect
        self.near = near
        self.far = far

        self.matriz_view = self._calcular_view()
        self.matriz_projecao = self._calcular_projecao()

    # =========================
    # MATRIZ VIEW (LookAt)
    # =========================
    def _calcular_view(self):
        # Vetor direção (z da câmera)
        z = (self.posicao - self.alvo).normalizar()

        # Vetor x da câmera
        x = self.up.produto_vetorial(z).normalizar()

        # Vetor y da câmera
        y = z.produto_vetorial(x)

        tx = -x.produto_escalar(self.posicao)
        ty = -y.produto_escalar(self.posicao)
        tz = -z.produto_escalar(self.posicao)

        return Matriz4([
            [x.x, x.y, x.z, tx],
            [y.x, y.y, y.z, ty],
            [z.x, z.y, z.z, tz],
            [0,   0,   0,   1]
        ])

    # =========================
    # MATRIZ DE PROJEÇÃO PERSPECTIVA
    # =========================
    def _calcular_projecao(self):
        f = 1.0 / math.tan(self.fov / 2.0)
        a = self.aspect
        n = self.near
        f_far = self.far

        return Matriz4([
            [f/a, 0,  0,                    0],
            [0,   f,  0,                    0],
            [0,   0,  (f_far+n)/(n-f_far), (2*f_far*n)/(n-f_far)],
            [0,   0, -1,                    0]
        ])

    # =========================
    # ATUALIZAÇÕES DINÂMICAS
    # =========================
    def atualizar_view(self):
        self.matriz_view = self._calcular_view()

    def atualizar_projecao(self):
        self.matriz_projecao = self._calcular_projecao()

    # =========================
    # PIPELINE: VIEW → PROJECTION
    # =========================
    def transformar_para_camera(self, vertice):
        v4 = Vetor4(vertice.x, vertice.y, vertice.z, 1.0)
        return self.matriz_view.multiplicar_vetor4(v4)

    def projetar(self, vertice_camera):
        return self.matriz_projecao.multiplicar_vetor4(vertice_camera)

    def pipeline_camera(self, vertice):
        """
        Model (já aplicado antes) → View → Projection → NDC
        """
        v_camera = self.transformar_para_camera(vertice)
        v_clip = self.projetar(v_camera)
        return v_clip.to_vetor3()
