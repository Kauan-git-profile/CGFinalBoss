import math

# =========================
# Vetor 3D
# =========================
class Vetor3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, v):
        return Vetor3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):
        return Vetor3(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, escalar):
        return Vetor3(self.x * escalar, self.y * escalar, self.z * escalar)

    def produto_escalar(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def produto_vetorial(self, v):
        return Vetor3(
            self.y * v.z - self.z * v.y,
            self.z * v.x - self.x * v.z,
            self.x * v.y - self.y * v.x
        )

    def magnitude(self):
        return math.sqrt(self.produto_escalar(self))

    def normalizar(self):
        mag = self.magnitude()
        if mag == 0:
            return Vetor3(0, 0, 0)
        return self * (1.0 / mag)

    def __repr__(self):
        return f"Vetor3({self.x:.3f}, {self.y:.3f}, {self.z:.3f})"


# =========================
# Vetor 4D (homogêneo)
# =========================
class Vetor4:
    def __init__(self, x, y, z, w=1.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def to_vetor3(self):
        if self.w == 0:
            return Vetor3(self.x, self.y, self.z)
        return Vetor3(self.x / self.w, self.y / self.w, self.z / self.w)


# =========================
# Matriz 4x4
# =========================
class Matriz4:
    def __init__(self, m=None):
        if m:
            self.m = m
        else:
            self.m = [[0.0] * 4 for _ in range(4)]

    @staticmethod
    def identidade():
        return Matriz4([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def __mul__(self, outra):
        # multiplicação matriz x matriz
        resultado = Matriz4()
        for i in range(4):
            for j in range(4):
                resultado.m[i][j] = sum(self.m[i][k] * outra.m[k][j] for k in range(4))
        return resultado

    def multiplicar_vetor4(self, v):
        x = v.x * self.m[0][0] + v.y * self.m[0][1] + v.z * self.m[0][2] + v.w * self.m[0][3]
        y = v.x * self.m[1][0] + v.y * self.m[1][1] + v.z * self.m[1][2] + v.w * self.m[1][3]
        z = v.x * self.m[2][0] + v.y * self.m[2][1] + v.z * self.m[2][2] + v.w * self.m[2][3]
        w = v.x * self.m[3][0] + v.y * self.m[3][1] + v.z * self.m[3][2] + v.w * self.m[3][3]
        return Vetor4(x, y, z, w)


# =========================
# Matrizes de Transformação
# =========================
def matriz_translacao(tx, ty, tz):
    return Matriz4([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def matriz_escala(s):
    return Matriz4([
        [s, 0, 0, 0],
        [0, s, 0, 0],
        [0, 0, s, 0],
        [0, 0, 0, 1]
    ])

def matriz_rotacao_x(angulo):
    c = math.cos(angulo)
    s = math.sin(angulo)
    return Matriz4([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s, c, 0],
        [0, 0, 0, 1]
    ])

def matriz_rotacao_y(angulo):
    c = math.cos(angulo)
    s = math.sin(angulo)
    return Matriz4([
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s, 0, c, 0],
        [0, 0, 0, 1]
    ])

def matriz_rotacao_z(angulo):
    c = math.cos(angulo)
    s = math.sin(angulo)
    return Matriz4([
        [c, -s, 0, 0],
        [s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
