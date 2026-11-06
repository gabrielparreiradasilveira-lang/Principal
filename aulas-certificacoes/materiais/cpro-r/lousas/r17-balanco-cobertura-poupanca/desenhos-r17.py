# Desenhos usados nas lousas da R17 (C-PRO R 2.1.5 a 2.1.7) que não vêm na skill.
# Para reutilizar, acrescente estas entradas ao dicionário DESENHOS de
# scripts/desenhos.py da skill roteiro-lousa-aprofundado.

DESENHOS_R17 = {'camera': {'aspecto': 0.7,
            'descricao': 'câmera fotográfica: corpo, visor, botão e lente (foto de um dia: balanço '
                         'patrimonial)',
            'tracos': [('fechada', [(0.04, 0.18), (0.96, 0.18), (0.96, 0.66), (0.04, 0.66)]),
                       ('fechada', [(0.14, 0.06), (0.38, 0.06), (0.38, 0.18), (0.14, 0.18)]),
                       ('fechada', [(0.72, 0.1), (0.86, 0.1), (0.86, 0.18), (0.72, 0.18)]),
                       ('elipse', 0.5, 0.42, 0.17, 0.17),
                       ('elipse', 0.5, 0.42, 0.08, 0.08),
                       ('fechada', [(0.8, 0.25), (0.9, 0.25), (0.9, 0.31), (0.8, 0.31)])]},
 'filmadora': {'aspecto': 0.62,
               'descricao': 'filmadora antiga: dois rolos de filme, corpo e lente em cone (filme '
                            'mês a mês: índice de poupança)',
               'tracos': [('elipse', 0.2, 0.14, 0.11, 0.11),
                          ('elipse', 0.45, 0.14, 0.11, 0.11),
                          ('ponto', 0.2, 0.14, 0.015),
                          ('ponto', 0.45, 0.14, 0.015),
                          ('fechada', [(0.04, 0.27), (0.62, 0.27), (0.62, 0.58), (0.04, 0.58)]),
                          ('fechada', [(0.62, 0.37), (0.96, 0.27), (0.96, 0.58), (0.62, 0.48)])]}}
