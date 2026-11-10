DESENHOS["fita_metrica"] = {
    "aspecto": 0.5,
    "descricao": "fita métrica esticada, com marcações e a ponta enrolada: tirar as medidas (coleta de informações)",
    "tracos": [
        ("fechada", [(0.22, 0.18), (0.96, 0.18), (0.96, 0.32), (0.22, 0.32)]),
        ("elipse", 0.14, 0.25, 0.10, 0.10), ("elipse", 0.14, 0.25, 0.04, 0.04),
        ("linha", [(0.34, 0.18), (0.34, 0.25)]), ("linha", [(0.46, 0.18), (0.46, 0.28)]), ("linha", [(0.58, 0.18), (0.58, 0.25)]),
        ("linha", [(0.70, 0.18), (0.70, 0.28)]), ("linha", [(0.82, 0.18), (0.82, 0.25)]),
    ],
}

DESENHOS["camisa"] = {
    "aspecto": 0.9,
    "descricao": "camisa de frente, com gola em V e botões: a roupa sob medida (a carteira adequada)",
    "tracos": [
        ("fechada", [(0.30, 0.08), (0.42, 0.14), (0.58, 0.14), (0.70, 0.08), (0.92, 0.26), (0.80, 0.38), (0.72, 0.32), (0.72, 0.84), (0.28, 0.84), (0.28, 0.32), (0.20, 0.38), (0.08, 0.26)]),
        ("linha", [(0.42, 0.14), (0.50, 0.28), (0.58, 0.14)]),
        ("ponto", 0.50, 0.42, 0.012), ("ponto", 0.50, 0.56, 0.012), ("ponto", 0.50, 0.70, 0.012),
    ],
}

DESENHOS["tres_cortes"] = {
    "aspecto": 0.5,
    "descricao": "três moldes de roupa de larguras crescentes, marcados C, M e A: os três perfis",
    "tracos": [
        ("fechada", [(0.08, 0.10), (0.24, 0.10), (0.24, 0.42), (0.08, 0.42)]), ("texto", "C", 0.16, 0.26, 0.13),
        ("fechada", [(0.36, 0.10), (0.60, 0.10), (0.60, 0.42), (0.36, 0.42)]), ("texto", "M", 0.48, 0.26, 0.13),
        ("fechada", [(0.70, 0.10), (0.98, 0.10), (0.98, 0.42), (0.70, 0.42)]), ("texto", "A", 0.84, 0.26, 0.13),
        ("linha", [(0.04, 0.45), (0.99, 0.45)]),
    ],
}
