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
    "estrada": {
        "aspecto": 0.3,
        "descricao": "estrada lisa vista de lado (ativo livre de risco, caminho sem buracos)",
        "tracos": [
            ("linha", [(0.0, 0.05), (0.5, 0.048), (1.0, 0.052)]),
            ("linha", [(0.0, 0.25), (0.5, 0.252), (1.0, 0.248)]),
            ("linha", [(0.06, 0.15), (0.16, 0.15)]), ("linha", [(0.27, 0.15), (0.37, 0.15)]),
            ("linha", [(0.48, 0.15), (0.58, 0.15)]), ("linha", [(0.69, 0.15), (0.79, 0.15)]),
            ("linha", [(0.9, 0.15), (0.99, 0.15)]),
        ],
    },
    "estrada_buracos": {
        "aspecto": 0.3,
        "descricao": "estrada com buracos (risco: o caminho pode sair diferente do previsto)",
        "tracos": [
            ("linha", [(0.0, 0.05), (0.5, 0.048), (1.0, 0.052)]),
            ("linha", [(0.0, 0.25), (0.5, 0.252), (1.0, 0.248)]),
            ("linha", [(0.06, 0.15), (0.16, 0.15)]), ("linha", [(0.48, 0.15), (0.58, 0.15)]),
            ("linha", [(0.9, 0.15), (0.99, 0.15)]),
            ("elipse", 0.27, 0.1, 0.06, 0.025), ("elipse", 0.4, 0.2, 0.05, 0.022),
            ("elipse", 0.7, 0.09, 0.07, 0.026), ("elipse", 0.82, 0.19, 0.045, 0.02),
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
