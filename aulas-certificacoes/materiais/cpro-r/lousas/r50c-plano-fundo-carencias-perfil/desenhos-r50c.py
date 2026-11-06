# Desenho usado nas lousas da R50C (C-PRO R 3.7.7 a 3.7.7.2) que não vem na skill.
# Para reutilizar, acrescente esta entrada ao dicionário DESENHOS de
# scripts/desenhos.py da skill roteiro-lousa-aprofundado.

DESENHOS_R50C = {'motor': {'aspecto': 0.8,
           'descricao': 'motor de carro: bloco com três cilindros, virabrequim e escapamento (fundo de '
                        'previdência)',
           'tracos': [('fechada', [(0.08, 0.34), (0.86, 0.34), (0.86, 0.76), (0.08, 0.76)]),
                      ('fechada', [(0.14, 0.08), (0.32, 0.08), (0.32, 0.34), (0.14, 0.34)]),
                      ('fechada', [(0.38, 0.08), (0.56, 0.08), (0.56, 0.34), (0.38, 0.34)]),
                      ('fechada', [(0.62, 0.08), (0.8, 0.08), (0.8, 0.34), (0.62, 0.34)]),
                      ('elipse', 0.47, 0.56, 0.11, 0.11),
                      ('linha', [(0.47, 0.56), (0.55, 0.49)]),
                      ('linha', [(0.86, 0.48), (0.98, 0.48)]),
                      ('linha', [(0.86, 0.6), (0.98, 0.6)])]}}
