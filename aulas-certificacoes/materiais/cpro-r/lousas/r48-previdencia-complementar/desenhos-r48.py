# Desenho usado nas lousas da R48 (C-PRO R 3.7.2 a 3.7.2.3.4) que não vem na skill.
# Para reutilizar, acrescente esta entrada ao dicionário DESENHOS de
# scripts/desenhos.py da skill roteiro-lousa-aprofundado.

DESENHOS_R48 = {
    "cisterna": {
        "aspecto": 0.9,
        "descricao": "cisterna cilíndrica com nível de água ondulado, plaquinha EU e torneira embaixo (a reserva da previdência complementar no nome do participante)",
        "tracos": [
            ("elipse", 0.46, 0.16, 0.30, 0.07),
            ("linha", [(0.16, 0.16), (0.16, 0.74)]), ("linha", [(0.76, 0.16), (0.76, 0.74)]),
            ("arco", 0.46, 0.74, 0.30, 0.07, 0, 180),
            ("linha", [(0.16, 0.42), (0.28, 0.39), (0.40, 0.43), (0.52, 0.39), (0.64, 0.43), (0.76, 0.40)]),
            ("texto", "EU", 0.46, 0.60, 0.12),
            ("linha", [(0.76, 0.66), (0.90, 0.66), (0.90, 0.72)]),
            ("ponto", 0.90, 0.78, 0.012), ("ponto", 0.90, 0.84, 0.012),
        ],
    },
}
