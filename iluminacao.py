from matematica import Vetor3


# =========================
# UTILIDADES
# =========================
def clamp(valor, minimo=0, maximo=255):
    return max(minimo, min(int(valor), maximo))


# =========================
# SOMBREAMENTO CONSTANTE
# =========================
def sombreamento_constante(normal, luz_dir, intensidade_luz=1.0):
    """
    Iluminação difusa simples (Lambert).
    Calculada uma vez por face.
    """
    n = normal.normalizar()
    l = luz_dir.normalizar()

    intensidade = max(0.0, n.produto_escalar(l)) * intensidade_luz
    cor = clamp(255 * intensidade)

    return (cor, cor, cor)


# =========================
# PHONG SIMPLIFICADO (POR PIXEL)
# =========================
def phong(
    normal,
    posicao_pixel,
    posicao_luz,
    posicao_camera,
    material
):
    """
    Modelo de iluminação Phong simplificado:
    ambiente + difuso + especular
    """

    # Vetores
    n = normal.normalizar()
    l = (posicao_luz - posicao_pixel).normalizar()
    v = (posicao_camera - posicao_pixel).normalizar()

    # Ambiente
    Ia = material.ka

    # Difuso (Lambert)
    Id = material.kd * max(0.0, n.produto_escalar(l))

    # Especular
    r = n * (2 * n.produto_escalar(l)) - l
    Is = material.ks * max(0.0, r.produto_escalar(v)) ** material.n

    intensidade = Ia + Id + Is
    cor = clamp(255 * intensidade)

    return (cor, cor, cor)
