DESENHOS["roleta"] = {
    "aspecto": 1.0,
    "descricao": "roleta de parque com raios e ponteiro: a disputa da mineração (prova de trabalho)",
    "tracos": [
        ("elipse", 0.5, 0.54, 0.38, 0.38),
        ("elipse", 0.5, 0.54, 0.07, 0.07),
        ("linha", [(0.5, 0.16), (0.5, 0.92)]), ("linha", [(0.12, 0.54), (0.88, 0.54)]),
        ("linha", [(0.23, 0.27), (0.77, 0.81)]), ("linha", [(0.77, 0.27), (0.23, 0.81)]),
        ("fechada", [(0.43, 0.03), (0.57, 0.03), (0.5, 0.17)]),
    ],
}

DESENHOS["livro_caixa"] = {
    "aspecto": 0.72,
    "descricao": "livro-caixa aberto, com lançamentos nas duas páginas: a blockchain, o livro-razão",
    "tracos": [
        ("fechada", [(0.05, 0.10), (0.49, 0.16), (0.49, 0.66), (0.05, 0.60)]),
        ("fechada", [(0.95, 0.10), (0.51, 0.16), (0.51, 0.66), (0.95, 0.60)]),
        ("linha", [(0.12, 0.24), (0.42, 0.28)]), ("linha", [(0.12, 0.34), (0.42, 0.38)]), ("linha", [(0.12, 0.44), (0.42, 0.48)]),
        ("linha", [(0.88, 0.24), (0.58, 0.28)]), ("linha", [(0.88, 0.34), (0.58, 0.38)]), ("linha", [(0.88, 0.44), (0.58, 0.48)]),
        ("grossa", [(0.5, 0.14), (0.5, 0.68)]),
    ],
}

DESENHOS["corrente_blocos"] = {
    "aspecto": 0.36,
    "descricao": "três blocos em fila, ligados por elos, cada um com a faixa do hash no alto: a cadeia de blocos",
    "tracos": [
        ("fechada", [(0.03, 0.05), (0.27, 0.05), (0.27, 0.31), (0.03, 0.31)]),
        ("fechada", [(0.38, 0.05), (0.62, 0.05), (0.62, 0.31), (0.38, 0.31)]),
        ("fechada", [(0.73, 0.05), (0.97, 0.05), (0.97, 0.31), (0.73, 0.31)]),
        ("grossa", [(0.06, 0.11), (0.24, 0.11)]), ("grossa", [(0.41, 0.11), (0.59, 0.11)]), ("grossa", [(0.76, 0.11), (0.94, 0.11)]),
        ("linha", [(0.07, 0.19), (0.23, 0.19)]), ("linha", [(0.07, 0.25), (0.19, 0.25)]),
        ("linha", [(0.42, 0.19), (0.58, 0.19)]), ("linha", [(0.42, 0.25), (0.54, 0.25)]),
        ("linha", [(0.77, 0.19), (0.93, 0.19)]), ("linha", [(0.77, 0.25), (0.89, 0.25)]),
        ("grossa", [(0.27, 0.18), (0.38, 0.18)]), ("grossa", [(0.62, 0.18), (0.73, 0.18)]),
    ],
}

DESENHOS["cracha_fiscal"] = {
    "aspecto": 1.15,
    "descricao": "crachá de fiscal com cordão, foto e linhas: o validador que deixou caução (staking)",
    "tracos": [
        ("linha", [(0.34, 0.03), (0.5, 0.24)]), ("linha", [(0.66, 0.03), (0.5, 0.24)]),
        ("fechada", [(0.22, 0.24), (0.78, 0.24), (0.78, 1.08), (0.22, 1.08)]),
        ("elipse", 0.5, 0.50, 0.13, 0.13),
        ("linha", [(0.32, 0.78), (0.68, 0.78)]), ("linha", [(0.32, 0.92), (0.68, 0.92)]),
    ],
}
