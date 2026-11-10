DESENHOS["bilheteria"] = {
    "aspecto": 1.0,
    "descricao": "guichê de bilheteria com telhado, janela e balcão: a exchange",
    "tracos": [
        ("fechada", [(0.20, 0.30), (0.80, 0.30), (0.80, 0.96), (0.20, 0.96)]),
        ("fechada", [(0.10, 0.30), (0.50, 0.05), (0.90, 0.30)]),
        ("fechada", [(0.32, 0.42), (0.68, 0.42), (0.68, 0.66), (0.32, 0.66)]),
        ("grossa", [(0.26, 0.72), (0.74, 0.72)]),
        ("texto", "$", 0.50, 0.84, 0.12),
    ],
}

DESENHOS["onibus_excursao"] = {
    "aspecto": 0.95,
    "descricao": "ônibus de excursão com bandeirinha do guia: fundo, ETF e carteira administrada",
    "tracos": [
        ("fechada", [(0.06, 0.26), (0.94, 0.26), (0.94, 0.76), (0.06, 0.76)]),
        ("fechada", [(0.12, 0.34), (0.30, 0.34), (0.30, 0.52), (0.12, 0.52)]),
        ("fechada", [(0.36, 0.34), (0.54, 0.34), (0.54, 0.52), (0.36, 0.52)]),
        ("fechada", [(0.60, 0.34), (0.78, 0.34), (0.78, 0.52), (0.60, 0.52)]),
        ("linha", [(0.84, 0.34), (0.84, 0.76)]),
        ("elipse", 0.26, 0.80, 0.07, 0.07), ("elipse", 0.72, 0.80, 0.07, 0.07),
        ("linha", [(0.50, 0.26), (0.50, 0.03)]),
        ("fechada", [(0.50, 0.03), (0.64, 0.09), (0.50, 0.15)]),
    ],
}
