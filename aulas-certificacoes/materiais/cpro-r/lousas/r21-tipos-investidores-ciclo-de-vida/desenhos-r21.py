DESENHOS["portao_embarque"] = {
    "aspecto": 0.62,
    "descricao": "três portas lado a lado marcadas C, Q e P: as áreas do aeroporto (comum, qualificado, profissional)",
    "tracos": [
        ("fechada", [(0.05, 0.10), (0.29, 0.10), (0.29, 0.56), (0.05, 0.56)]), ("texto", "C", 0.17, 0.32, 0.15),
        ("fechada", [(0.38, 0.10), (0.62, 0.10), (0.62, 0.56), (0.38, 0.56)]), ("texto", "Q", 0.50, 0.32, 0.15),
        ("fechada", [(0.71, 0.10), (0.95, 0.10), (0.95, 0.56), (0.71, 0.56)]), ("texto", "P", 0.83, 0.32, 0.15),
        ("linha", [(0.02, 0.58), (0.98, 0.58)]),
    ],
}

DESENHOS["rota_voo"] = {
    "aspecto": 0.5,
    "descricao": "rota de um voo em arco: subida, cruzeiro e pouso, com um aviãozinho no trecho de cruzeiro (ciclo de vida)",
    "tracos": [
        ("linha", [(0.02, 0.46), (0.98, 0.46)]),
        ("grossa", [(0.04, 0.44), (0.18, 0.30), (0.30, 0.16), (0.40, 0.10), (0.60, 0.10), (0.70, 0.16), (0.84, 0.32), (0.96, 0.44)]),
        ("fechada", [(0.46, 0.04), (0.56, 0.10), (0.46, 0.15)]),
        ("linha", [(0.36, 0.20), (0.36, 0.46)]), ("linha", [(0.66, 0.20), (0.66, 0.46)]),
    ],
}
