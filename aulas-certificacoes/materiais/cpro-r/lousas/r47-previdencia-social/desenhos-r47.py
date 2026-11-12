# Desenhos usados nas lousas da R47 (C-PRO R 3.7.1 a 3.7.1.3) que não vêm na skill.
# Para reutilizar, acrescente estas entradas ao dicionário DESENHOS de
# scripts/desenhos.py da skill roteiro-lousa-aprofundado.

DESENHOS_R47 = {
    "caixa_dagua": {
        "aspecto": 1.0,
        "descricao": "prédio com caixa d'água no telhado escrita INSS, cano descendo até uma torneira pingando (a repartição simples)",
        "tracos": [
            ("fechada", [(0.24, 0.38), (0.70, 0.38), (0.70, 0.96), (0.24, 0.96)]),
            ("fechada", [(0.28, 0.08), (0.66, 0.08), (0.66, 0.30), (0.28, 0.30)]),
            ("linha", [(0.36, 0.30), (0.36, 0.38)]), ("linha", [(0.58, 0.30), (0.58, 0.38)]),
            ("texto", "INSS", 0.47, 0.19, 0.13),
            ("fechada", [(0.31, 0.47), (0.42, 0.47), (0.42, 0.57), (0.31, 0.57)]),
            ("fechada", [(0.52, 0.47), (0.63, 0.47), (0.63, 0.57), (0.52, 0.57)]),
            ("fechada", [(0.31, 0.67), (0.42, 0.67), (0.42, 0.77), (0.31, 0.77)]),
            ("fechada", [(0.52, 0.67), (0.63, 0.67), (0.63, 0.77), (0.52, 0.77)]),
            ("linha", [(0.66, 0.20), (0.86, 0.20), (0.86, 0.82), (0.95, 0.82), (0.95, 0.86)]),
            ("ponto", 0.95, 0.90, 0.012), ("ponto", 0.95, 0.95, 0.012),
        ],
    },
    "torneira": {
        "aspecto": 0.8,
        "descricao": "torneira com registro em cima e filete de água caindo num balde (o benefício e o teto)",
        "tracos": [
            ("linha", [(0.06, 0.16), (0.50, 0.16), (0.50, 0.30), (0.62, 0.30), (0.62, 0.38)]),
            ("linha", [(0.42, 0.06), (0.58, 0.06)]), ("linha", [(0.50, 0.06), (0.50, 0.16)]),
            ("linha", [(0.62, 0.42), (0.62, 0.58)]),
            ("linha", [(0.46, 0.58), (0.50, 0.76), (0.74, 0.76), (0.78, 0.58)]),
            ("linha", [(0.46, 0.58), (0.78, 0.58)]),
        ],
    },
    "torneira_dupla": {
        "aspecto": 0.7,
        "descricao": "duas torneiras no mesmo cano: a da esquerda com jato cheio, a da direita só pingando (acumulação com redutor)",
        "tracos": [
            ("linha", [(0.04, 0.14), (0.96, 0.14)]),
            ("linha", [(0.25, 0.14), (0.25, 0.26), (0.33, 0.26), (0.33, 0.32)]),
            ("linha", [(0.19, 0.06), (0.31, 0.06)]), ("linha", [(0.25, 0.06), (0.25, 0.14)]),
            ("grossa", [(0.33, 0.35), (0.33, 0.58)]),
            ("linha", [(0.70, 0.14), (0.70, 0.26), (0.78, 0.26), (0.78, 0.32)]),
            ("linha", [(0.64, 0.06), (0.76, 0.06)]), ("linha", [(0.70, 0.06), (0.70, 0.14)]),
            ("ponto", 0.78, 0.40, 0.012), ("ponto", 0.78, 0.52, 0.012),
            ("linha", [(0.20, 0.58), (0.23, 0.66), (0.43, 0.66), (0.46, 0.58)]),
            ("linha", [(0.65, 0.58), (0.68, 0.66), (0.88, 0.66), (0.91, 0.58)]),
        ],
    },
}
