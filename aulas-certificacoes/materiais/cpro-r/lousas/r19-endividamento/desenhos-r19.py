# -*- coding: utf-8 -*-
"""
Biblioteca de desenhos simples (estilo rabisco de lousa) usados pelo lousa.py.

Cada desenho é descrito numa caixa de largura 1 e altura = "aspecto".
Primitivas (coordenadas nessa caixa):
  ("linha",  [(x, y), ...])            traço livre passando pelos pontos
  ("fechada", [(x, y), ...])           traço livre que volta ao primeiro ponto
  ("elipse", cx, cy, rx, ry)           contorno à mão, com "passada" no fim (não fecha perfeito)
  ("arco",   cx, cy, rx, ry, a0, a1)   pedaço de elipse, ângulos em graus (0 = direita, 90 = baixo)
  ("grossa", [(x, y), ...])            traço com o dobro da espessura (ex.: mercúrio do termômetro)
  ("ponto",  cx, cy, r)                bolinha cheia
  ("texto",  "R$", cx, cy, tam)        texto na fonte da lousa; tam relativo à largura

Para criar um desenho novo: acrescente uma entrada em DESENHOS com "aspecto",
"descricao" e "tracos". Mantenha poucos traços: rabisco de professor, não ilustração.
"""
import math


def _estrela(n=5, r_ext=0.48, r_int=0.2, cx=0.5, cy=0.52):
    pts = []
    for i in range(2 * n + 1):
        r = r_ext if i % 2 == 0 else r_int
        a = -math.pi / 2 + i * math.pi / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


DESENHOS = {
    "cabine": {
        "aspecto": 0.72,
        "descricao": "cabine de comando: para-brisa, painel com três mostradores e manche (piloto manual x automático)",
        "tracos": [
            ("linha", [(0.06, 0.30), (0.22, 0.04), (0.78, 0.04), (0.94, 0.30)]),
            ("linha", [(0.5, 0.04), (0.5, 0.30)]),
            ("fechada", [(0.02, 0.30), (0.98, 0.30), (0.98, 0.58), (0.02, 0.58)]),
            ("elipse", 0.2, 0.44, 0.09, 0.09), ("linha", [(0.2, 0.44), (0.26, 0.39)]),
            ("elipse", 0.5, 0.44, 0.09, 0.09), ("linha", [(0.5, 0.44), (0.45, 0.38)]),
            ("elipse", 0.8, 0.44, 0.09, 0.09), ("linha", [(0.8, 0.44), (0.87, 0.47)]),
            ("linha", [(0.5, 0.58), (0.5, 0.66)]),
            ("grossa", [(0.36, 0.66), (0.64, 0.66)]),
            ("linha", [(0.36, 0.61), (0.36, 0.71)]), ("linha", [(0.64, 0.61), (0.64, 0.71)]),
        ],
    },
    "alarme": {"aspecto": 0.9, "descricao": "sino de alarme tocando, com ondas de som dos dois lados (alarme do painel)",
  "tracos": [("elipse",0.5,0.13,0.045,0.045), ("arco",0.5,0.40,0.20,0.22,180,360),
    ("linha",[(0.30,0.40),(0.29,0.62),(0.17,0.74)]), ("linha",[(0.70,0.40),(0.71,0.62),(0.83,0.74)]),
    ("grossa",[(0.15,0.74),(0.85,0.74)]), ("ponto",0.5,0.81,0.05),
    ("arco",0.5,0.42,0.40,0.36,200,235), ("arco",0.5,0.42,0.40,0.36,305,340),
    ("arco",0.5,0.42,0.49,0.44,198,238), ("arco",0.5,0.42,0.49,0.44,302,342)]},
 "caixa_preta": {"aspecto": 0.8, "descricao": "caixa-preta do avião: caixa com alça, duas faixas e a onda da gravação",
  "tracos": [("fechada",[(0.06,0.22),(0.94,0.22),(0.94,0.78),(0.06,0.78)]), ("linha",[(0.36,0.22),(0.36,0.08),(0.64,0.08),(0.64,0.22)]),
    ("linha",[(0.06,0.34),(0.94,0.34)]), ("linha",[(0.06,0.66),(0.94,0.66)]),
    ("linha",[(0.16,0.50),(0.24,0.42),(0.32,0.58),(0.40,0.42),(0.48,0.58),(0.56,0.42),(0.64,0.58),(0.72,0.42),(0.80,0.50)]),
    ("ponto",0.86,0.28,0.025)]},
 "ancora": {"aspecto": 1.0, "descricao": "âncora de navio: argola, haste, travessa e os dois braços curvos com pontas",
  "tracos": [("elipse",0.5,0.08,0.06,0.06), ("grossa",[(0.5,0.14),(0.5,0.90)]), ("linha",[(0.32,0.26),(0.68,0.26)]),
    ("arco",0.5,0.62,0.36,0.30,0,180), ("linha",[(0.86,0.62),(0.80,0.54)]), ("linha",[(0.86,0.62),(0.94,0.56)]),
    ("linha",[(0.14,0.62),(0.20,0.54)]), ("linha",[(0.14,0.62),(0.06,0.56)])]},
 "mostrador": {
        "aspecto": 0.62,
        "descricao": "mostrador do painel (um instrumento isolado, um ativo olhado sozinho)",
        "tracos": [
            ("arco", 0.5, 0.56, 0.46, 0.46, 180, 360),
            ("linha", [(0.04, 0.56), (0.96, 0.56)]),
            ("linha", [(0.12, 0.33), (0.18, 0.37)]), ("linha", [(0.5, 0.12), (0.5, 0.19)]),
            ("linha", [(0.88, 0.33), (0.82, 0.37)]),
            ("grossa", [(0.5, 0.56), (0.2, 0.36)]),
            ("ponto", 0.5, 0.56, 0.035),
        ],
    },
    "rodovia_pedagio": {
        "aspecto": 0.26,
        "descricao": "rodovia com cabine de pedágio na entrada (aporte) e na saída (resgate)",
        "tracos": [
            ("linha", [(0.0, 0.17), (0.5, 0.168), (1.0, 0.172)]),
            ("linha", [(0.0, 0.25), (0.5, 0.252), (1.0, 0.248)]),
            ("linha", [(0.27, 0.21), (0.33, 0.21)]), ("linha", [(0.42, 0.21), (0.48, 0.21)]),
            ("linha", [(0.57, 0.21), (0.63, 0.21)]),
            ("fechada", [(0.05, 0.155), (0.05, 0.05), (0.16, 0.05), (0.16, 0.155)]),
            ("fechada", [(0.035, 0.05), (0.175, 0.05), (0.16, 0.015), (0.05, 0.015)]),
            ("fechada", [(0.08, 0.07), (0.13, 0.07), (0.13, 0.11), (0.08, 0.11)]),
            ("grossa", [(0.16, 0.13), (0.25, 0.13)]),
            ("fechada", [(0.84, 0.155), (0.84, 0.05), (0.95, 0.05), (0.95, 0.155)]),
            ("fechada", [(0.825, 0.05), (0.965, 0.05), (0.95, 0.015), (0.84, 0.015)]),
            ("fechada", [(0.87, 0.07), (0.92, 0.07), (0.92, 0.11), (0.87, 0.11)]),
            ("grossa", [(0.84, 0.13), (0.75, 0.13)]),
        ],
    },
    "carro": {
        "aspecto": 0.58,
        "descricao": "carro de perfil (juros = freio/acelerador, economia andando)",
        "tracos": [
            ("fechada", [(0.0, 0.30), (0.02, 0.48), (1.0, 0.48), (0.99, 0.30), (0.83, 0.27),
                         (0.71, 0.04), (0.31, 0.04), (0.18, 0.28)]),
            ("elipse", 0.25, 0.49, 0.1, 0.1),
            ("elipse", 0.74, 0.49, 0.1, 0.1),
        ],
    },
    "balao": {
        "aspecto": 1.45,
        "descricao": "balão de festa (inflação = balão inchando)",
        "tracos": [
            ("elipse", 0.5, 0.46, 0.38, 0.44),
            ("fechada", [(0.45, 0.94), (0.55, 0.94), (0.5, 0.89)]),
            ("linha", [(0.5, 0.95), (0.56, 1.08), (0.44, 1.22), (0.52, 1.43)]),
        ],
    },
    "lampada": {
        "aspecto": 1.15,
        "descricao": "lâmpada acesa (ideia, sacada, conceito-chave)",
        "tracos": [
            ("arco", 0.5, 0.42, 0.27, 0.29, 140, 400),
            ("linha", [(0.29, 0.6), (0.37, 0.72), (0.37, 0.84)]),
            ("linha", [(0.71, 0.6), (0.63, 0.72), (0.63, 0.84)]),
            ("linha", [(0.35, 0.86), (0.65, 0.86)]),
            ("linha", [(0.37, 0.95), (0.63, 0.95)]),
            ("linha", [(0.43, 1.04), (0.57, 1.04)]),
            ("linha", [(0.5, 0.0), (0.5, 0.07)]),
            ("linha", [(0.12, 0.13), (0.18, 0.19)]),
            ("linha", [(0.88, 0.13), (0.82, 0.19)]),
            ("linha", [(0.0, 0.42), (0.09, 0.42)]),
            ("linha", [(1.0, 0.42), (0.91, 0.42)]),
        ],
    },
    "grafico_alta": {
        "aspecto": 0.8,
        "descricao": "gráfico subindo (alta de preço, juros, PIB)",
        "tracos": [
            ("linha", [(0.04, 0.0), (0.04, 0.76), (1.0, 0.76)]),
            ("linha", [(0.1, 0.66), (0.3, 0.5), (0.45, 0.56), (0.65, 0.3), (0.78, 0.36), (0.95, 0.08)]),
            ("linha", [(0.82, 0.1), (0.95, 0.08), (0.95, 0.22)]),
        ],
    },
    "grafico_baixa": {
        "aspecto": 0.8,
        "descricao": "gráfico caindo (queda de preço, recessão)",
        "tracos": [
            ("linha", [(0.04, 0.0), (0.04, 0.76), (1.0, 0.76)]),
            ("linha", [(0.1, 0.1), (0.3, 0.26), (0.45, 0.2), (0.65, 0.46), (0.78, 0.4), (0.95, 0.66)]),
            ("linha", [(0.82, 0.66), (0.95, 0.66), (0.95, 0.52)]),
        ],
    },
    "casa": {
        "aspecto": 0.9,
        "descricao": "casa (imóvel, família, orçamento doméstico)",
        "tracos": [
            ("linha", [(0.15, 0.42), (0.15, 0.88), (0.85, 0.88), (0.85, 0.42)]),
            ("linha", [(0.04, 0.47), (0.5, 0.05), (0.96, 0.47)]),
            ("linha", [(0.42, 0.88), (0.42, 0.62), (0.58, 0.62), (0.58, 0.88)]),
        ],
    },
    "banco": {
        "aspecto": 0.85,
        "descricao": "prédio com colunas (Banco Central, banco, instituição)",
        "tracos": [
            ("fechada", [(0.05, 0.3), (0.5, 0.04), (0.95, 0.3)]),
            ("linha", [(0.2, 0.36), (0.2, 0.72)]),
            ("linha", [(0.4, 0.36), (0.4, 0.72)]),
            ("linha", [(0.6, 0.36), (0.6, 0.72)]),
            ("linha", [(0.8, 0.36), (0.8, 0.72)]),
            ("linha", [(0.08, 0.76), (0.92, 0.76)]),
            ("linha", [(0.02, 0.84), (0.98, 0.84)]),
        ],
    },
    "dinheiro": {
        "aspecto": 0.5,
        "descricao": "cédula de dinheiro",
        "tracos": [
            ("fechada", [(0.0, 0.0), (1.0, 0.0), (1.0, 0.5), (0.0, 0.5)]),
            ("elipse", 0.5, 0.25, 0.13, 0.15),
            ("texto", "$", 0.5, 0.26, 0.2),
        ],
    },
    "moeda": {
        "aspecto": 1.0,
        "descricao": "moeda com cifrão",
        "tracos": [
            ("elipse", 0.5, 0.5, 0.46, 0.46),
            ("texto", "$", 0.5, 0.52, 0.55),
        ],
    },
    "cofrinho": {
        "aspecto": 0.78,
        "descricao": "cofrinho de porquinho (poupança, reserva)",
        "tracos": [
            ("elipse", 0.48, 0.42, 0.4, 0.29),
            ("elipse", 0.9, 0.42, 0.06, 0.09),
            ("linha", [(0.26, 0.2), (0.3, 0.03), (0.41, 0.15)]),
            ("linha", [(0.24, 0.66), (0.24, 0.78)]),
            ("linha", [(0.38, 0.7), (0.38, 0.78)]),
            ("linha", [(0.6, 0.7), (0.6, 0.78)]),
            ("linha", [(0.74, 0.65), (0.74, 0.78)]),
            ("linha", [(0.4, 0.16), (0.56, 0.16)]),
            ("linha", [(0.08, 0.38), (0.02, 0.33), (0.05, 0.27)]),
            ("ponto", 0.73, 0.33, 0.022),
        ],
    },
    "termometro": {
        "aspecto": 2.2,
        "descricao": "termômetro (inflação, aquecimento da economia)",
        "tracos": [
            ("arco", 0.5, 0.16, 0.13, 0.11, 180, 360),
            ("linha", [(0.37, 0.16), (0.37, 1.7)]),
            ("linha", [(0.63, 0.16), (0.63, 1.7)]),
            ("arco", 0.5, 1.9, 0.27, 0.26, -60, 240),
            ("grossa", [(0.5, 0.75), (0.5, 1.85)]),
            ("ponto", 0.5, 1.9, 0.14),
            ("linha", [(0.68, 0.45), (0.8, 0.45)]),
            ("linha", [(0.68, 0.75), (0.8, 0.75)]),
            ("linha", [(0.68, 1.05), (0.8, 1.05)]),
            ("linha", [(0.68, 1.35), (0.8, 1.35)]),
        ],
    },
    "alvo": {
        "aspecto": 1.0,
        "descricao": "alvo com flecha (meta de inflação, objetivo)",
        "tracos": [
            ("elipse", 0.46, 0.54, 0.43, 0.43),
            ("elipse", 0.46, 0.54, 0.28, 0.28),
            ("elipse", 0.46, 0.54, 0.12, 0.12),
            ("linha", [(0.98, 0.02), (0.5, 0.5)]),
            ("linha", [(0.86, 0.02), (0.98, 0.02), (0.98, 0.14)]),
        ],
    },
    "balanca": {
        "aspecto": 0.85,
        "descricao": "balança de dois pratos (equilíbrio, oferta x demanda, justiça)",
        "tracos": [
            ("elipse", 0.5, 0.1, 0.035, 0.035),
            ("linha", [(0.5, 0.14), (0.5, 0.78)]),
            ("linha", [(0.32, 0.8), (0.68, 0.8)]),
            ("linha", [(0.08, 0.2), (0.92, 0.2)]),
            ("linha", [(0.08, 0.2), (0.0, 0.5)]),
            ("linha", [(0.08, 0.2), (0.17, 0.5)]),
            ("arco", 0.085, 0.5, 0.11, 0.07, 0, 180),
            ("linha", [(0.92, 0.2), (0.83, 0.5)]),
            ("linha", [(0.92, 0.2), (1.0, 0.5)]),
            ("arco", 0.915, 0.5, 0.11, 0.07, 0, 180),
        ],
    },
    "ampulheta": {
        "aspecto": 1.3,
        "descricao": "ampulheta (tempo, prazo, carência, juros compostos)",
        "tracos": [
            ("linha", [(0.12, 0.04), (0.88, 0.04)]),
            ("linha", [(0.12, 1.26), (0.88, 1.26)]),
            ("linha", [(0.22, 0.04), (0.22, 0.26), (0.47, 0.65), (0.22, 1.04), (0.22, 1.26)]),
            ("linha", [(0.78, 0.04), (0.78, 0.26), (0.53, 0.65), (0.78, 1.04), (0.78, 1.26)]),
            ("linha", [(0.35, 1.2), (0.5, 1.08), (0.65, 1.2)]),
        ],
    },
    "pessoa": {
        "aspecto": 1.6,
        "descricao": "boneco palito (cliente, investidor, pessoa)",
        "tracos": [
            ("elipse", 0.5, 0.18, 0.15, 0.15),
            ("linha", [(0.5, 0.34), (0.5, 0.95)]),
            ("linha", [(0.12, 0.62), (0.5, 0.48), (0.88, 0.62)]),
            ("linha", [(0.22, 1.55), (0.5, 0.95), (0.78, 1.55)]),
        ],
    },
    "check": {
        "aspecto": 0.8,
        "descricao": "sinal de certo",
        "tracos": [("linha", [(0.04, 0.44), (0.36, 0.76), (0.96, 0.04)])],
    },
    "xis": {
        "aspecto": 1.0,
        "descricao": "sinal de errado (X)",
        "tracos": [("linha", [(0.06, 0.06), (0.94, 0.94)]), ("linha", [(0.94, 0.06), (0.06, 0.94)])],
    },
    "estrela": {
        "aspecto": 1.0,
        "descricao": "estrela (destaque, cai muito na prova)",
        "tracos": [("linha", _estrela())],
    },
    "exclamacao": {
        "aspecto": 1.0,
        "descricao": "triângulo de alerta com exclamação (pegadinha)",
        "tracos": [
            ("fechada", [(0.5, 0.04), (0.97, 0.9), (0.03, 0.9)]),
            ("linha", [(0.5, 0.32), (0.5, 0.62)]),
            ("ponto", 0.5, 0.75, 0.035),
        ],
    },
    "caminhao": {
        "aspecto": 0.55,
        "descricao": "caminhão de mudança (transferência de custódia, levar os ativos)",
        "tracos": [
            ("fechada", [(0.02, 0.04), (0.62, 0.04), (0.62, 0.42), (0.02, 0.42)]),
            ("linha", [(0.62, 0.15), (0.8, 0.15), (0.96, 0.29), (0.96, 0.42), (0.62, 0.42)]),
            ("fechada", [(0.67, 0.19), (0.79, 0.19), (0.89, 0.28), (0.67, 0.28)]),
            ("linha", [(0.12, 0.14), (0.3, 0.14), (0.3, 0.32), (0.12, 0.32), (0.12, 0.14)]),
            ("linha", [(0.36, 0.2), (0.52, 0.2), (0.52, 0.32), (0.36, 0.32), (0.36, 0.2)]),
            ("elipse", 0.19, 0.44, 0.075, 0.075),
            ("elipse", 0.8, 0.44, 0.075, 0.075),
        ],
    },
    "prancheta": {
        "aspecto": 1.3,
        "descricao": "prancheta com ficha (cadastro, perfil do cliente, ficha do paciente)",
        "tracos": [
            ("fechada", [(0.08, 0.1), (0.92, 0.1), (0.92, 1.26), (0.08, 1.26)]),
            ("fechada", [(0.34, 0.02), (0.66, 0.02), (0.66, 0.17), (0.34, 0.17)]),
            ("linha", [(0.22, 0.4), (0.78, 0.4)]),
            ("linha", [(0.22, 0.58), (0.78, 0.58)]),
            ("linha", [(0.22, 0.76), (0.66, 0.76)]),
            ("linha", [(0.22, 0.94), (0.72, 0.94)]),
        ],
    },
    "balanca_peso": {
        "aspecto": 1.0,
        "descricao": "balança de banheiro vista de cima (peso atual x ideal, check-up)",
        "tracos": [
            ("fechada", [(0.05, 0.05), (0.95, 0.05), (0.95, 0.95), (0.05, 0.95)]),
            ("arco", 0.5, 0.33, 0.2, 0.16, 180, 360),
            ("linha", [(0.3, 0.33), (0.7, 0.33)]),
            ("linha", [(0.5, 0.33), (0.6, 0.2)]),
            ("elipse", 0.32, 0.68, 0.1, 0.15),
            ("elipse", 0.68, 0.68, 0.1, 0.15),
        ],
    },
    "tubo_ensaio": {
        "aspecto": 1.4,
        "descricao": "tubo de ensaio com líquido (exame, indicador, teste)",
        "tracos": [
            ("linha", [(0.26, 0.05), (0.74, 0.05)]),
            ("linha", [(0.35, 0.05), (0.35, 1.12)]),
            ("linha", [(0.65, 0.05), (0.65, 1.12)]),
            ("arco", 0.5, 1.12, 0.15, 0.17, 0, 180),
            ("linha", [(0.35, 0.66), (0.43, 0.62), (0.5, 0.67), (0.58, 0.62), (0.65, 0.66)]),
            ("linha", [(0.42, 0.82), (0.42, 0.9)]),
            ("linha", [(0.56, 0.95), (0.56, 1.03)]),
        ],
    },
    "receita": {
        "aspecto": 1.3,
        "descricao": "receita médica com Rx (recomendação, plano de ação)",
        "tracos": [
            ("fechada", [(0.1, 0.04), (0.9, 0.04), (0.9, 1.26), (0.1, 1.26)]),
            ("texto", "Rx", 0.34, 0.27, 0.3),
            ("linha", [(0.22, 0.56), (0.78, 0.56)]),
            ("linha", [(0.22, 0.73), (0.78, 0.73)]),
            ("linha", [(0.22, 0.9), (0.6, 0.9)]),
            ("linha", [(0.48, 1.12), (0.56, 1.03), (0.62, 1.13), (0.7, 1.04), (0.8, 1.09)]),
        ],
    },
    "onibus": {
        "aspecto": 0.46,
        "descricao": "ônibus de linha (ativo livre de risco, caminho seguro e constante)",
        "tracos": [
            ("fechada", [(0.02, 0.05), (0.95, 0.05), (0.99, 0.12), (0.99, 0.37), (0.02, 0.37)]),
            ("fechada", [(0.07, 0.11), (0.19, 0.11), (0.19, 0.21), (0.07, 0.21)]),
            ("fechada", [(0.25, 0.11), (0.37, 0.11), (0.37, 0.21), (0.25, 0.21)]),
            ("fechada", [(0.43, 0.11), (0.55, 0.11), (0.55, 0.21), (0.43, 0.21)]),
            ("fechada", [(0.61, 0.11), (0.73, 0.11), (0.73, 0.21), (0.61, 0.21)]),
            ("linha", [(0.8, 0.11), (0.8, 0.37)]),
            ("linha", [(0.85, 0.11), (0.96, 0.11), (0.97, 0.24), (0.85, 0.24), (0.85, 0.11)]),
            ("elipse", 0.2, 0.39, 0.065, 0.065),
            ("elipse", 0.73, 0.39, 0.065, 0.065),
        ],
    },
    "placa": {
        "aspecto": 1.0,
        "descricao": "placa de estrada com o nome da cidade (destino, meta, objetivo do cliente)",
        "tracos": [
            ("fechada", [(0.04, 0.04), (0.96, 0.04), (0.96, 0.5), (0.04, 0.5)]),
            ("linha", [(0.2, 0.19), (0.8, 0.19)]),
            ("linha", [(0.3, 0.34), (0.7, 0.34)]),
            ("linha", [(0.24, 0.5), (0.24, 0.98)]),
            ("linha", [(0.76, 0.5), (0.76, 0.98)]),
        ],
    },
    "combustivel": {
        "aspecto": 0.9,
        "descricao": "marcador de combustível na reserva (tanque inteiro gasto, risco total)",
        "tracos": [
            ("arco", 0.5, 0.55, 0.45, 0.45, 180, 360),
            ("linha", [(0.05, 0.55), (0.95, 0.55)]),
            ("linha", [(0.09, 0.39), (0.15, 0.42)]),
            ("linha", [(0.5, 0.1), (0.5, 0.17)]),
            ("linha", [(0.91, 0.39), (0.85, 0.42)]),
            ("grossa", [(0.5, 0.55), (0.14, 0.48)]),
            ("ponto", 0.5, 0.55, 0.035),
            ("fechada", [(0.5, 0.64), (0.56, 0.75), (0.55, 0.82), (0.5, 0.86), (0.45, 0.82), (0.44, 0.75)]),
        ],
    },
    "serra": {
        "aspecto": 0.82,
        "descricao": "serra com a estrada subindo em zigue-zague (inclinação da pista, risco de mercado, beta)",
        "tracos": [
            ("linha", [(0.0, 0.8), (0.42, 0.06), (0.62, 0.4), (0.76, 0.22), (1.0, 0.8)]),
            ("linha", [(0.08, 0.79), (0.62, 0.69), (0.3, 0.56), (0.6, 0.44), (0.38, 0.33), (0.47, 0.22)]),
            ("linha", [(0.0, 0.8), (1.0, 0.8)]),
        ],
    },
    "mar": {
        "aspecto": 0.8,
        "descricao": "mar com ondas, um barco a vela e um navio (maré = risco de mercado, barcos = ativos)",
        "tracos": [
            ("linha", [(0.0, 0.62), (0.1, 0.57), (0.2, 0.62), (0.3, 0.57), (0.4, 0.62), (0.5, 0.57), (0.6, 0.62),
                       (0.7, 0.57), (0.8, 0.62), (0.9, 0.57), (1.0, 0.62)]),
            ("linha", [(0.05, 0.74), (0.15, 0.69), (0.25, 0.74), (0.35, 0.69), (0.45, 0.74), (0.55, 0.69),
                       (0.65, 0.74), (0.75, 0.69), (0.85, 0.74), (0.95, 0.69)]),
            ("fechada", [(0.06, 0.5), (0.36, 0.5), (0.31, 0.58), (0.11, 0.58)]),
            ("linha", [(0.21, 0.5), (0.21, 0.22)]),
            ("fechada", [(0.21, 0.24), (0.34, 0.46), (0.21, 0.46)]),
            ("fechada", [(0.48, 0.44), (0.97, 0.44), (0.91, 0.58), (0.54, 0.58)]),
            ("fechada", [(0.6, 0.3), (0.82, 0.3), (0.82, 0.44), (0.6, 0.44)]),
            ("fechada", [(0.7, 0.15), (0.77, 0.15), (0.77, 0.3), (0.7, 0.3)]),
        ],
    },
    "fronteira_eficiente": {
        "aspecto": 0.95,
        "descricao": "gráfico risco × retorno com a fronteira eficiente e carteiras dominadas abaixo",
        "tracos": [
            ("linha", [(0.1, 0.06), (0.1, 0.8), (0.98, 0.8)]),
            ("linha", [(0.14, 0.7), (0.22, 0.5), (0.34, 0.35), (0.5, 0.25), (0.7, 0.18), (0.94, 0.14)]),
            ("ponto", 0.36, 0.58, 0.02), ("ponto", 0.5, 0.5, 0.02), ("ponto", 0.64, 0.6, 0.02),
            ("ponto", 0.28, 0.68, 0.02), ("ponto", 0.78, 0.44, 0.02),
            ("texto", "RETORNO", 0.3, 0.0, 0.08),
            ("texto", "RISCO", 0.78, 0.9, 0.08),
        ],
    },
    "diversificacao": {
        "aspecto": 0.95,
        "descricao": "risco × número de ativos: a curva cai e encosta no piso do risco sistemático",
        "tracos": [
            ("linha", [(0.1, 0.06), (0.1, 0.8), (0.98, 0.8)]),
            ("linha", [(0.13, 0.1), (0.2, 0.32), (0.3, 0.45), (0.45, 0.53), (0.65, 0.57), (0.95, 0.585)]),
            ("linha", [(0.12, 0.62), (0.2, 0.62)]), ("linha", [(0.28, 0.62), (0.36, 0.62)]),
            ("linha", [(0.44, 0.62), (0.52, 0.62)]), ("linha", [(0.6, 0.62), (0.68, 0.62)]),
            ("linha", [(0.76, 0.62), (0.84, 0.62)]), ("linha", [(0.9, 0.62), (0.97, 0.62)]),
            ("texto", "RISCO", 0.24, 0.0, 0.08),
            ("texto", "Nº DE ATIVOS", 0.62, 0.9, 0.08),
        ],
    },
}


def lista():
    """Texto com os desenhos disponíveis (para --desenhos)."""
    linhas = []
    for nome in sorted(DESENHOS):
        d = DESENHOS[nome]
        linhas.append(f"  {nome:<14} altura = {d['aspecto']:.2f} x largura  — {d['descricao']}")
    return "\n".join(linhas)


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


# ---- desenhos da R7 (avião próprio × ações de companhias aéreas) ----
DESENHOS["aviao_hangar"] = {
    "aspecto": 0.75,
    "descricao": "um avião só, parado dentro de um hangar em arco, com uma chave de manutenção ao lado (investimento real)",
    "tracos": [
        ("arco", 0.5, 0.66, 0.46, 0.56, 180, 360),
        ("linha", [(0.04, 0.66), (0.96, 0.66)]),
        ("linha", [(0.04, 0.66), (0.04, 0.72)]), ("linha", [(0.96, 0.66), (0.96, 0.72)]),
    ] + _aviao(0.46, 0.45, 0.40, 0) + [
        ("linha", [(0.80, 0.60), (0.88, 0.48)]),
        ("elipse", 0.895, 0.455, 0.035, 0.035),
    ],
}

DESENHOS["tela_companhias"] = {
    "aspecto": 0.75,
    "descricao": "tela de cotações com uma linha que oscila e três aviõezinhos (ações de várias companhias aéreas: investimento financeiro)",
    "tracos": [
        ("fechada", [(0.04, 0.04), (0.96, 0.04), (0.96, 0.56), (0.04, 0.56)]),
        ("linha", [(0.5, 0.56), (0.5, 0.66)]),
        ("linha", [(0.32, 0.68), (0.68, 0.68)]),
        ("linha", [(0.10, 0.44), (0.24, 0.32), (0.36, 0.40), (0.52, 0.22), (0.66, 0.34), (0.80, 0.18), (0.90, 0.26)]),
    ] + _aviao(0.22, 0.16, 0.12, -20) + _aviao(0.50, 0.12, 0.12, -20) + _aviao(0.78, 0.44, 0.12, -20),
}


# ---- desenhos da R8 (escada rolante que desce, elevador, prédio) ----
def _degraus(x0, y0, x1, y1, n=7):
    pts = []
    dx, dy = (x1 - x0) / n, (y1 - y0) / n
    for k in range(n):
        x, y = x0 + k * dx, y0 + k * dy
        pts += [(x, y), (x + dx, y)]
    pts.append((x1, y1))
    return ("linha", pts)


def _boneco(cx, cy, s):
    return [
        ("elipse", cx, cy - 0.30 * s, 0.07 * s, 0.07 * s),
        ("linha", [(cx, cy - 0.23 * s), (cx, cy)]),
        ("linha", [(cx - 0.10 * s, cy - 0.15 * s), (cx + 0.10 * s, cy - 0.15 * s)]),
        ("linha", [(cx, cy), (cx - 0.07 * s, cy + 0.14 * s)]),
        ("linha", [(cx, cy), (cx + 0.07 * s, cy + 0.14 * s)]),
    ]


_ESCADA = [
    _degraus(0.06, 0.16, 0.86, 0.66),
    ("linha", [(0.06, 0.06), (0.86, 0.56)]),
    ("linha", [(0.06, 0.16), (0.06, 0.06)]), ("linha", [(0.86, 0.66), (0.86, 0.56)]),
    ("linha", [(0.66, 0.68), (0.80, 0.76)]), ("linha", [(0.80, 0.76), (0.72, 0.77)]), ("linha", [(0.80, 0.76), (0.77, 0.69)]),
]

DESENHOS["escada_desce"] = {
    "aspecto": 0.8,
    "descricao": "escada rolante descendo (seta para baixo) com um boneco parado num degrau: o dinheiro parado desce com a inflação",
    "tracos": _ESCADA + _boneco(0.42, 0.34, 0.42),
}

DESENHOS["escada_sobe"] = {
    "aspecto": 0.8,
    "descricao": "a mesma escada rolante que desce, com um boneco subindo mais rápido e uma seta grande para cima: o ganho real",
    "tracos": _ESCADA + _boneco(0.42, 0.34, 0.42) + [
        ("grossa", [(0.58, 0.40), (0.30, 0.10)]), ("grossa", [(0.30, 0.10), (0.42, 0.11)]), ("grossa", [(0.30, 0.10), (0.31, 0.22)]),
    ],
}

DESENHOS["elevador"] = {
    "aspecto": 0.9,
    "descricao": "elevador expresso: porta dupla, visor com setas e painel lateral de botões (o banco digital)",
    "tracos": [
        ("fechada", [(0.18, 0.14), (0.70, 0.14), (0.70, 0.86), (0.18, 0.86)]),
        ("linha", [(0.44, 0.14), (0.44, 0.86)]),
        ("fechada", [(0.30, 0.02), (0.58, 0.02), (0.58, 0.10), (0.30, 0.10)]),
        ("linha", [(0.38, 0.08), (0.41, 0.04), (0.44, 0.08)]), ("linha", [(0.47, 0.04), (0.50, 0.08), (0.53, 0.04)]),
        ("fechada", [(0.78, 0.30), (0.92, 0.30), (0.92, 0.66), (0.78, 0.66)]),
        ("elipse", 0.85, 0.38, 0.03, 0.03), ("elipse", 0.85, 0.48, 0.03, 0.03), ("elipse", 0.85, 0.58, 0.03, 0.03),
    ],
}

DESENHOS["predio_andares"] = {
    "aspecto": 1.0,
    "descricao": "prédio com andares numerados: cada objetivo é um andar (perto = curto prazo; alto = longo prazo)",
    "tracos": [
        ("fechada", [(0.24, 0.06), (0.76, 0.06), (0.76, 0.94), (0.24, 0.94)]),
        ("linha", [(0.24, 0.28), (0.76, 0.28)]), ("linha", [(0.24, 0.50), (0.76, 0.50)]), ("linha", [(0.24, 0.72), (0.76, 0.72)]),
        ("texto", "30", 0.50, 0.17, 0.14), ("texto", "10", 0.50, 0.39, 0.14), ("texto", "3", 0.50, 0.61, 0.14), ("texto", "1", 0.50, 0.83, 0.14),
    ],
}


# ---- desenhos da R9 (maratona) ----
DESENHOS["corredor"] = {
    "aspecto": 0.9,
    "descricao": "corredor de maratona em movimento, inclinado para a frente, com número no peito e linha do chão",
    "tracos": [
        ("elipse", 0.56, 0.12, 0.07, 0.07),
        ("grossa", [(0.54, 0.20), (0.46, 0.50)]),
        ("linha", [(0.53, 0.26), (0.68, 0.34), (0.76, 0.24)]),
        ("linha", [(0.52, 0.27), (0.38, 0.36), (0.32, 0.30)]),
        ("linha", [(0.46, 0.50), (0.62, 0.62), (0.60, 0.80)]),
        ("linha", [(0.46, 0.50), (0.34, 0.66), (0.18, 0.66)]),
        ("fechada", [(0.47, 0.30), (0.55, 0.32), (0.53, 0.40), (0.45, 0.38)]),
        ("linha", [(0.04, 0.84), (0.96, 0.84)]),
        ("linha", [(0.08, 0.30), (0.20, 0.30)]), ("linha", [(0.04, 0.40), (0.18, 0.40)]),
    ],
}

DESENHOS["posto_hidratacao"] = {
    "aspecto": 0.8,
    "descricao": "posto de hidratação: mesa com copos e garrafas e uma placa de água (as fontes de renda)",
    "tracos": [
        ("linha", [(0.06, 0.50), (0.94, 0.50)]),
        ("linha", [(0.12, 0.50), (0.12, 0.76)]), ("linha", [(0.88, 0.50), (0.88, 0.76)]),
        ("linha", [(0.18, 0.50), (0.16, 0.36), (0.26, 0.36), (0.24, 0.50)]),
        ("linha", [(0.34, 0.50), (0.32, 0.36), (0.42, 0.36), (0.40, 0.50)]),
        ("fechada", [(0.52, 0.50), (0.52, 0.30), (0.55, 0.24), (0.59, 0.24), (0.62, 0.30), (0.62, 0.50)]),
        ("fechada", [(0.70, 0.50), (0.70, 0.30), (0.73, 0.24), (0.77, 0.24), (0.80, 0.30), (0.80, 0.50)]),
        ("linha", [(0.50, 0.24), (0.50, 0.04)]),
        ("fechada", [(0.34, 0.04), (0.66, 0.04), (0.66, 0.16), (0.34, 0.16)]),
        ("texto", "H2O", 0.50, 0.10, 0.10),
    ],
}

DESENHOS["corredor_caimbra"] = {
    "aspecto": 0.8,
    "descricao": "corredor sentado no chão segurando a perna, com riscos de dor: a câimbra (o estresse financeiro)",
    "tracos": [
        ("elipse", 0.30, 0.22, 0.07, 0.07),
        ("grossa", [(0.31, 0.30), (0.36, 0.56)]),
        ("linha", [(0.36, 0.56), (0.62, 0.52), (0.82, 0.62)]),
        ("linha", [(0.36, 0.56), (0.52, 0.66), (0.70, 0.66)]),
        ("linha", [(0.33, 0.38), (0.50, 0.48), (0.60, 0.52)]),
        ("linha", [(0.32, 0.40), (0.46, 0.54)]),
        ("linha", [(0.04, 0.70), (0.96, 0.70)]),
        ("linha", [(0.62, 0.36), (0.66, 0.42), (0.70, 0.36), (0.74, 0.42)]),
        ("linha", [(0.72, 0.28), (0.76, 0.34), (0.80, 0.28), (0.84, 0.34)]),
    ],
}

DESENHOS["megafone"] = {
    "aspecto": 0.7,
    "descricao": "megafone com ondas de som: a voz da arquibancada (o finfluencer)",
    "tracos": [
        ("fechada", [(0.10, 0.28), (0.24, 0.28), (0.56, 0.08), (0.56, 0.60), (0.24, 0.40), (0.10, 0.40)]),
        ("linha", [(0.20, 0.40), (0.24, 0.58), (0.32, 0.58), (0.30, 0.44)]),
        ("arco", 0.56, 0.34, 0.12, 0.18, 300, 420),
        ("arco", 0.56, 0.34, 0.24, 0.28, 300, 420),
        ("arco", 0.56, 0.34, 0.36, 0.36, 305, 415),
    ],
}

DESENHOS["pista_buracos"] = {
    "aspecto": 0.8,
    "descricao": "pista em perspectiva com buracos e uma placa de atenção (os riscos para a pessoa investidora)",
    "tracos": [
        ("linha", [(0.40, 0.06), (0.06, 0.76)]), ("linha", [(0.60, 0.06), (0.94, 0.76)]),
        ("linha", [(0.50, 0.10), (0.50, 0.18)]), ("linha", [(0.50, 0.30), (0.50, 0.40)]), ("linha", [(0.50, 0.54), (0.50, 0.66)]),
        ("elipse", 0.36, 0.56, 0.09, 0.04), ("elipse", 0.62, 0.36, 0.06, 0.03), ("elipse", 0.68, 0.64, 0.10, 0.045),
        ("fechada", [(0.82, 0.10), (0.94, 0.30), (0.70, 0.30)]),
        ("texto", "!", 0.82, 0.23, 0.10),
    ],
}


# ---- desenhos da R6 (cabine: o caça-níquel no painel) ----
DESENHOS["caca_niquel"] = {
    "aspecto": 1.0,
    "descricao": "caça-níquel: corpo, visor com três símbolos, alavanca com bola e bandeja de moedas (a bet)",
    "tracos": [
        ("fechada", [(0.14, 0.12), (0.76, 0.12), (0.76, 0.92), (0.14, 0.92)]),
        ("fechada", [(0.20, 0.26), (0.70, 0.26), (0.70, 0.50), (0.20, 0.50)]),
        ("linha", [(0.367, 0.26), (0.367, 0.50)]), ("linha", [(0.533, 0.26), (0.533, 0.50)]),
        ("texto", "7", 0.285, 0.38, 0.13), ("texto", "7", 0.45, 0.38, 0.13), ("texto", "?", 0.615, 0.38, 0.13),
        ("linha", [(0.76, 0.56), (0.86, 0.56), (0.86, 0.22)]),
        ("ponto", 0.86, 0.18, 0.045),
        ("fechada", [(0.26, 0.74), (0.64, 0.74), (0.60, 0.84), (0.30, 0.84)]),
        ("linha", [(0.40, 0.60), (0.50, 0.60)]),
        ("linha", [(0.20, 0.06), (0.26, 0.10)]), ("linha", [(0.45, 0.02), (0.45, 0.09)]), ("linha", [(0.70, 0.06), (0.64, 0.10)]),
    ],
}

DESENHOS["bilhete_loteria"] = {
    "aspecto": 0.62,
    "descricao": "bilhete de loteria com grade de números e dois marcados (sorteio raro, sonho de riqueza)",
    "tracos": [
        ("fechada", [(0.06, 0.06), (0.94, 0.06), (0.94, 0.56), (0.06, 0.56)]),
        ("linha", [(0.22, 0.06), (0.22, 0.56)]),
        ("texto", "Nº", 0.14, 0.31, 0.08),
        ("elipse", 0.32, 0.18, 0.035, 0.035), ("elipse", 0.44, 0.18, 0.035, 0.035), ("elipse", 0.56, 0.18, 0.035, 0.035),
        ("elipse", 0.68, 0.18, 0.035, 0.035), ("elipse", 0.80, 0.18, 0.035, 0.035),
        ("elipse", 0.32, 0.31, 0.035, 0.035), ("elipse", 0.44, 0.31, 0.035, 0.035), ("elipse", 0.56, 0.31, 0.035, 0.035),
        ("elipse", 0.68, 0.31, 0.035, 0.035), ("elipse", 0.80, 0.31, 0.035, 0.035),
        ("elipse", 0.32, 0.44, 0.035, 0.035), ("elipse", 0.44, 0.44, 0.035, 0.035), ("elipse", 0.56, 0.44, 0.035, 0.035),
        ("elipse", 0.68, 0.44, 0.035, 0.035), ("elipse", 0.80, 0.44, 0.035, 0.035),
        ("linha", [(0.41, 0.15), (0.47, 0.21)]), ("linha", [(0.47, 0.15), (0.41, 0.21)]),
        ("linha", [(0.65, 0.41), (0.71, 0.47)]), ("linha", [(0.71, 0.41), (0.65, 0.47)]),
    ],
}

DESENHOS["placar"] = {
    "aspecto": 0.7,
    "descricao": "placar de jogo com interrogação e uma bola: o resultado que ninguém controla (aposta esportiva)",
    "tracos": [
        ("fechada", [(0.06, 0.08), (0.94, 0.08), (0.94, 0.42), (0.06, 0.42)]),
        ("texto", "? x ?", 0.50, 0.25, 0.16),
        ("linha", [(0.30, 0.42), (0.30, 0.52)]), ("linha", [(0.70, 0.42), (0.70, 0.52)]),
        ("elipse", 0.50, 0.58, 0.11, 0.11),
        ("fechada", [(0.50, 0.53), (0.545, 0.565), (0.53, 0.62), (0.47, 0.62), (0.455, 0.565)]),
        ("linha", [(0.04, 0.68), (0.96, 0.68)]),
    ],
}

DESENHOS["tanque_furado"] = {
    "aspecto": 0.8,
    "descricao": "tanque de combustível com um furo pingando gotas: pequenas apostas acumuladas esvaziam o orçamento",
    "tracos": [
        ("fechada", [(0.14, 0.14), (0.78, 0.14), (0.78, 0.58), (0.14, 0.58)]),
        ("linha", [(0.66, 0.14), (0.66, 0.06), (0.76, 0.06)]),
        ("linha", [(0.14, 0.40), (0.78, 0.40)]),
        ("linha", [(0.20, 0.30), (0.30, 0.30)]),
        ("ponto", 0.46, 0.58, 0.02),
        ("fechada", [(0.46, 0.63), (0.49, 0.67), (0.48, 0.70), (0.46, 0.71), (0.44, 0.70), (0.43, 0.67)]),
        ("fechada", [(0.46, 0.75), (0.49, 0.79), (0.48, 0.82), (0.46, 0.83), (0.44, 0.82), (0.43, 0.79)]),
        ("arco", 0.46, 0.78, 0.16, 0.03, 0, 360),
        ("texto", "R$", 0.46, 0.27, 0.10),
    ],
}


# ---- desenhos da R10 (garimpo) ----
DESENHOS["funil_etapas"] = {
    "aspecto": 0.9,
    "descricao": "funil com quatro faixas (as quatro etapas) e uma pepita saindo embaixo",
    "tracos": [
        ("fechada", [(0.06, 0.06), (0.94, 0.06), (0.60, 0.66), (0.60, 0.80), (0.40, 0.80), (0.40, 0.66)]),
        ("linha", [(0.155, 0.22), (0.845, 0.22)]),
        ("linha", [(0.245, 0.38), (0.755, 0.38)]),
        ("linha", [(0.335, 0.54), (0.665, 0.54)]),
        ("ponto", 0.30, 0.13, 0.02), ("ponto", 0.45, 0.14, 0.02), ("ponto", 0.60, 0.12, 0.02), ("ponto", 0.74, 0.14, 0.02),
        ("ponto", 0.40, 0.30, 0.02), ("ponto", 0.58, 0.30, 0.02),
        ("ponto", 0.50, 0.46, 0.02),
        ("fechada", [(0.50, 0.83), (0.55, 0.86), (0.53, 0.89), (0.47, 0.89), (0.45, 0.86)]),
    ],
}

DESENHOS["bateia"] = {
    "aspecto": 0.6,
    "descricao": "bateia de garimpo vista de lado: prato raso com água e duas pepitas no fundo (o cliente ativado)",
    "tracos": [
        ("elipse", 0.50, 0.20, 0.44, 0.12),
        ("linha", [(0.06, 0.20), (0.36, 0.50), (0.64, 0.50), (0.94, 0.20)]),
        ("arco", 0.50, 0.24, 0.30, 0.06, 20, 160),
        ("fechada", [(0.44, 0.40), (0.48, 0.37), (0.52, 0.40), (0.50, 0.44), (0.45, 0.44)]),
        ("fechada", [(0.55, 0.42), (0.58, 0.40), (0.61, 0.43), (0.58, 0.46)]),
        ("linha", [(0.66, 0.04), (0.70, 0.09)]), ("linha", [(0.78, 0.02), (0.78, 0.08)]),
    ],
}

DESENHOS["rio"] = {
    "aspecto": 0.6,
    "descricao": "rio largo com margens onduladas, ondas e pedras: muito cascalho passando (o canal online)",
    "tracos": [
        ("linha", [(0.02, 0.10), (0.20, 0.06), (0.40, 0.12), (0.62, 0.06), (0.82, 0.12), (0.98, 0.08)]),
        ("linha", [(0.02, 0.52), (0.22, 0.56), (0.42, 0.50), (0.62, 0.56), (0.80, 0.50), (0.98, 0.54)]),
        ("linha", [(0.12, 0.24), (0.18, 0.21), (0.24, 0.24), (0.30, 0.21)]),
        ("linha", [(0.48, 0.30), (0.54, 0.27), (0.60, 0.30), (0.66, 0.27)]),
        ("linha", [(0.22, 0.40), (0.28, 0.37), (0.34, 0.40), (0.40, 0.37)]),
        ("linha", [(0.72, 0.40), (0.78, 0.37), (0.84, 0.40), (0.90, 0.37)]),
        ("elipse", 0.40, 0.22, 0.03, 0.02), ("elipse", 0.80, 0.26, 0.035, 0.022), ("elipse", 0.58, 0.42, 0.03, 0.02),
    ],
}

DESENHOS["caderno_garimpo"] = {
    "aspecto": 1.0,
    "descricao": "caderno aberto com tracinhos de contagem e uma pepita: baldes lavados por pepita (os indicadores)",
    "tracos": [
        ("fechada", [(0.08, 0.14), (0.50, 0.20), (0.92, 0.14), (0.92, 0.80), (0.50, 0.86), (0.08, 0.80)]),
        ("linha", [(0.50, 0.20), (0.50, 0.86)]),
        ("linha", [(0.16, 0.34), (0.16, 0.46)]), ("linha", [(0.21, 0.35), (0.21, 0.47)]), ("linha", [(0.26, 0.36), (0.26, 0.48)]), ("linha", [(0.31, 0.37), (0.31, 0.49)]),
        ("linha", [(0.13, 0.48), (0.35, 0.36)]),
        ("linha", [(0.16, 0.58), (0.16, 0.70)]), ("linha", [(0.21, 0.59), (0.21, 0.71)]), ("linha", [(0.26, 0.60), (0.26, 0.72)]),
        ("fechada", [(0.66, 0.44), (0.74, 0.38), (0.82, 0.44), (0.79, 0.54), (0.69, 0.54)]),
        ("texto", "÷", 0.72, 0.68, 0.12),
    ],
}


# ---- desenhos da R12 (consulta médica) ----
DESENHOS["estetoscopio"] = {
    "aspecto": 1.0,
    "descricao": "estetoscópio: duas hastes, tubo em Y e o disco na ponta (a consulta, o diagnóstico antes da receita)",
    "tracos": [
        ("ponto", 0.28, 0.08, 0.03), ("ponto", 0.62, 0.08, 0.03),
        ("linha", [(0.28, 0.08), (0.26, 0.30), (0.34, 0.46), (0.45, 0.50)]),
        ("linha", [(0.62, 0.08), (0.64, 0.30), (0.56, 0.46), (0.45, 0.50)]),
        ("linha", [(0.45, 0.50), (0.45, 0.68), (0.52, 0.80), (0.64, 0.82), (0.74, 0.74), (0.76, 0.62)]),
        ("elipse", 0.76, 0.52, 0.10, 0.10),
        ("elipse", 0.76, 0.52, 0.04, 0.04),
    ],
}

DESENHOS["monitor_sinais"] = {
    "aspecto": 0.7,
    "descricao": "monitor de sinais vitais com a linha do batimento (a liquidez: estabilizar antes de tratar)",
    "tracos": [
        ("fechada", [(0.08, 0.08), (0.92, 0.08), (0.92, 0.54), (0.08, 0.54)]),
        ("linha", [(0.14, 0.34), (0.30, 0.34), (0.36, 0.18), (0.44, 0.48), (0.50, 0.26), (0.56, 0.34), (0.86, 0.34)]),
        ("linha", [(0.50, 0.54), (0.50, 0.62)]),
        ("linha", [(0.34, 0.62), (0.66, 0.62)]),
    ],
}


# ---- desenhos da R18 (gelo e água) ----
DESENHOS["copo_cubos"] = {
    "aspecto": 1.0,
    "descricao": "copo com água e cubos de gelo derretendo: o que vira dinheiro na hora (liquidez imediata)",
    "tracos": [
        ("linha", [(0.24, 0.10), (0.32, 0.88), (0.68, 0.88), (0.76, 0.10)]),
        ("linha", [(0.27, 0.40), (0.38, 0.37), (0.50, 0.41), (0.62, 0.37), (0.73, 0.40)]),
        ("fechada", [(0.34, 0.22), (0.46, 0.18), (0.50, 0.30), (0.38, 0.34)]),
        ("fechada", [(0.54, 0.24), (0.66, 0.22), (0.66, 0.34), (0.55, 0.35)]),
        ("fechada", [(0.42, 0.50), (0.54, 0.48), (0.56, 0.60), (0.44, 0.62)]),
        ("linha", [(0.20, 0.94), (0.80, 0.94)]),
    ],
}

DESENHOS["gelo_cadeado"] = {
    "aspecto": 0.9,
    "descricao": "bloco de gelo com cadeado na frente: só derrete na data (ativo sem resgate antes do vencimento)",
    "tracos": [
        ("fechada", [(0.10, 0.26), (0.70, 0.26), (0.70, 0.82), (0.10, 0.82)]),
        ("linha", [(0.10, 0.26), (0.28, 0.10), (0.88, 0.10), (0.70, 0.26)]),
        ("linha", [(0.88, 0.10), (0.88, 0.66), (0.70, 0.82)]),
        ("fechada", [(0.30, 0.52), (0.50, 0.52), (0.50, 0.70), (0.30, 0.70)]),
        ("arco", 0.40, 0.52, 0.07, 0.10, 180, 360),
        ("ponto", 0.40, 0.61, 0.018),
        ("linha", [(0.18, 0.34), (0.26, 0.42)]), ("linha", [(0.56, 0.36), (0.62, 0.42)]),
    ],
}


# ---- desenhos da R19 (mochila na trilha) ----
DESENHOS["mochila"] = {
    "aspecto": 1.1,
    "descricao": "mochila com alças, bolso frontal e uma pedra dentro: o peso das dívidas",
    "tracos": [
        ("fechada", [(0.22, 0.30), (0.30, 0.16), (0.70, 0.16), (0.78, 0.30), (0.80, 0.92), (0.20, 0.92)]),
        ("arco", 0.50, 0.16, 0.12, 0.10, 180, 360),
        ("fechada", [(0.32, 0.56), (0.68, 0.56), (0.68, 0.82), (0.32, 0.82)]),
        ("linha", [(0.32, 0.64), (0.68, 0.64)]),
        ("linha", [(0.22, 0.34), (0.12, 0.50), (0.16, 0.78)]),
        ("linha", [(0.78, 0.34), (0.88, 0.50), (0.84, 0.78)]),
        ("fechada", [(0.40, 0.34), (0.52, 0.30), (0.60, 0.38), (0.54, 0.46), (0.42, 0.44)]),
    ],
}
