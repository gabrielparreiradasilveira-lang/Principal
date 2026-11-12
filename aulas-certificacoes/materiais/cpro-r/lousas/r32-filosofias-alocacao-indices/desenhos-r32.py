# Desenho usado nas lousas da R32 (C-PRO R 3.3.2 a 3.3.3.3) que não vem na skill.
# Para reutilizar, acrescente esta entrada ao dicionário DESENHOS de
# scripts/desenhos.py da skill roteiro-lousa-aprofundado.

DESENHOS_R32 = {
    "placar_indice": {
        "aspecto": 0.9,
        "descricao": "placar de estádio com a palavra ÍNDICE e uma linha de cotação subindo, sobre dois pés (o benchmark)",
        "tracos": [
            ("fechada", [(0.08, 0.08), (0.92, 0.08), (0.92, 0.66), (0.08, 0.66)]),
            ("texto", "ÍNDICE", 0.50, 0.20, 0.12),
            ("linha", [(0.14, 0.56), (0.30, 0.45), (0.44, 0.50), (0.60, 0.36), (0.74, 0.40), (0.86, 0.30)]),
            ("linha", [(0.30, 0.66), (0.30, 0.88)]), ("linha", [(0.70, 0.66), (0.70, 0.88)]),
            ("linha", [(0.20, 0.88), (0.80, 0.88)]),
        ],
    },
}
