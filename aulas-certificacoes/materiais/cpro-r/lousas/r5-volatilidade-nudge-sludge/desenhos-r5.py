# ---- desenhos da R5 (céu de pilotos automáticos e painéis) ----
def _aviao(cx, cy, s, ang):
    """Aviãozinho de rabisco centrado em (cx, cy), tamanho s, apontando no ângulo ang (graus; 0 = direita, negativo = sobe)."""
    a = math.radians(ang)
    ca, sa = math.cos(a), math.sin(a)

    def p(x, y):
        return (cx + s * (x * ca - y * sa), cy + s * (x * sa + y * ca))
    return [
        ("grossa", [p(-0.5, 0), p(0.5, 0)]),
        ("linha", [p(0.12, 0), p(-0.12, -0.42), p(-0.02, 0)]),
        ("linha", [p(0.12, 0), p(-0.12, 0.42), p(-0.02, 0)]),
        ("linha", [p(-0.40, 0), p(-0.52, -0.18)]),
        ("linha", [p(-0.40, 0), p(-0.52, 0.18)]),
    ]


def _tracejado(y, x0=0.03, x1=0.97, n=9):
    passo = (x1 - x0) / n
    return [("linha", [(x0 + i * passo, y), (x0 + i * passo + passo * 0.55, y)]) for i in range(n)]


DESENHOS["avioes_subindo"] = {
    "aspecto": 0.8,
    "descricao": "três aviões subindo juntos em diagonal; os de cima passam da linha tracejada (altitude segura): a bolha",
    "tracos": _tracejado(0.36)
    + _aviao(0.18, 0.64, 0.24, -35) + _aviao(0.48, 0.42, 0.24, -35) + _aviao(0.78, 0.18, 0.24, -35),
}

DESENHOS["avioes_mergulhando"] = {
    "aspecto": 0.8,
    "descricao": "três aviões mergulhando juntos em diagonal, saindo de cima da linha tracejada: o estouro",
    "tracos": _tracejado(0.36)
    + _aviao(0.18, 0.16, 0.24, 35) + _aviao(0.48, 0.40, 0.24, 35) + _aviao(0.78, 0.64, 0.24, 35),
}

DESENHOS["painel_claro"] = {
    "aspecto": 0.62,
    "descricao": "painel limpo: um botão grande com visto e só duas teclas pequenas (o botão certo à mão: nudge)",
    "tracos": [
        ("fechada", [(0.03, 0.06), (0.97, 0.06), (0.97, 0.58), (0.03, 0.58)]),
        ("elipse", 0.36, 0.32, 0.17, 0.17),
        ("grossa", [(0.27, 0.32), (0.34, 0.40), (0.47, 0.22)]),
        ("fechada", [(0.66, 0.18), (0.86, 0.18), (0.86, 0.28), (0.66, 0.28)]),
        ("fechada", [(0.66, 0.38), (0.86, 0.38), (0.86, 0.48), (0.66, 0.48)]),
    ],
}

_conf = [("fechada", [(0.03, 0.06), (0.97, 0.06), (0.97, 0.58), (0.03, 0.58)])]
for _i in range(6):
    for _j in range(3):
        _conf.append(("elipse", 0.10 + _i * 0.105, 0.17 + _j * 0.15, 0.03, 0.03))
_conf += [
    ("linha", [(0.70, 0.14), (0.80, 0.30), (0.74, 0.44), (0.90, 0.22), (0.86, 0.50), (0.72, 0.30), (0.92, 0.40)]),
    ("texto", "?", 0.83, 0.30, 0.16),
]
DESENHOS["painel_confuso"] = {
    "aspecto": 0.62,
    "descricao": "painel confuso: muitos botõezinhos iguais, fios embolados e um ponto de interrogação (sludge)",
    "tracos": _conf,
}
