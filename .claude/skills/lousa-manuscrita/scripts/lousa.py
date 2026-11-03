#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lousa.py — gera imagens de lousa escrita à mão (padrão 1920x1080, fundo de slide)
a partir de um roteiro JSON. Só depende do Pillow.

Uso:
  python3 lousa.py roteiro.json                    gera o(s) PNG(s) do roteiro
  python3 lousa.py roteiro.json -o pasta/          grava na pasta indicada (ou num .png, se for 1 lousa)
  python3 lousa.py roteiro.json --grade            também grava *_grade.png (grade de 100 px + caixas
                                                   de cada elemento) para conferir posições
  python3 lousa.py roteiro.json --pptx aula.pptx   junta as imagens num .pptx, uma por slide
  python3 lousa.py --desenhos                      lista os desenhos prontos

Formato do roteiro: references/formato.md (na pasta da skill).
"""
import argparse
import json
import math
import os
import random
import re
import sys

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
except ImportError:  # pragma: no cover
    sys.exit("Este script precisa do Pillow: pip install pillow")

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.dont_write_bytecode = True  # não deixa __pycache__ dentro da pasta da skill
import desenhos as DES  # noqa: E402
import moldes as MOLDES  # noqa: E402

RAIZ = os.path.dirname(AQUI)
FONTE_PADRAO = os.path.join(RAIZ, "assets", "fontes", "PermanentMarker-Regular.ttf")
# Rótulo das teclas da HP12C: letra de mão mais limpa (na Permanent Marker, G e S parecem 6 e 5).
FONTE_TECLA = os.path.join(RAIZ, "assets", "fontes", "Pangolin-Regular.ttf")

SS = 2  # desenha em 2x e reduz no fim: borda suave sem perder o tremor

# Cores medidas no molde do professor (amarelo, vermelho, verde, branco) + complementares.
PALETA = {
    "amarelo": "#FFD400",
    "vermelho": "#FF3B3B",
    "verde": "#7CFF3A",
    "branco": "#F2F2F2",
    "azul": "#38C6FF",
    "laranja": "#FF9A1F",
    "rosa": "#FF5FC8",
    "roxo": "#B98CFF",
    "cinza": "#9A9A9A",
    "ciano": "#2FE0F5",  # subtítulos (padrão visual X8)
}
FUNDOS = {"preto": "#000000", "grafite": "#1B1B1D", "lousa": "#1E3528", "azul-noite": "#0D1B2A"}

# Símbolos que a fonte não tem: as setas viram rabisco de seta; o resto vira texto equivalente.
SETAS_TEXTO = {"→": 0, "←": 180, "↑": -90, "↓": 90, "↗": -40, "↘": 40, "⇒": 0}
TROCAS = {"≥": ">=", "≤": "<=", "≠": "=/=", "\t": " ", "\r": "", "∑": "Σ", "∆": "Δ"}
MARCA = re.compile(r"\{([#\w-]+):((?:[^{}]|_\{[^{}]*\})*)\}")  # {cor:trecho}, aceita _{índice} dentro
SUB = re.compile(r"_\{([^{}]*)\}")  # R_{f} = índice (subscrito) escrito menor e mais baixo
# Emojis viram desenho (padrão X8): check verde, X vermelho, triângulo de alerta vermelho.
EMOJIS = {"✅": "✓", "✔": "✓", "☑": "✓", "✓": "✓", "❌": "✗", "✗": "✗", "✘": "✗", "❎": "✗",
          "✖": "✗", "⚠": "⚠"}
GREGOS = {"σ", "β"}  # minúsculas gregas: a fonte não tem, e .upper() viraria Σ (somatório) e Β (parece B)
DESENHADOS = set(SETAS_TEXTO) | {"✓", "✗", "⚠", "Σ", "Δ"} | GREGOS  # desenhados à mão, não vêm da fonte
SUB_ESC, SUB_DESCE = 0.6, 0.22  # índice: 60% do tamanho (nunca abaixo de 28 px), 22% abaixo da linha
INVISIVEIS = {"\ufe0f", "\ufe0e", "\u200d"}  # seletores de emoji
ESPACOS = (" ", "\u00a0")  # \u00a0 = espaço que não quebra linha (ex.: "20%\u00a0A.A.")
MACRON = "\u0304"  # barra em cima (x̄ da HP12C)
TECLA = re.compile(r"\[([^\[\]\n]{1,14})\]")  # [ENTER] = tecla da HP12C em caixinha
MARCADOR_NUM = re.compile(r"(\d{1,2})[.)] ")  # "1. " no começo da linha = número em circulinho
# Cantos que ficam livres (padrão X8): logo no alto à direita, webcam embaixo à direita.
AREAS_LIVRES = [["logo X8", 1560, 0, 1920, 190], ["webcam", 1600, 760, 1920, 1080]]
LATEX = re.compile(r"\\[A-Za-z]+|\$[^$\n]+\$|\^\{|_\{")
DECIMAL_PONTO = re.compile(r"(?<![\d.,])\d+\.\d{1,2}(?![\d.])")
SEM_MILHAR = re.compile(r"(?<![\d.,])\d{5,}(?![\d.,])")
ITEM_PD = re.compile(r"(cpa|c-?pro[- ]?[ri]?|cfp|cga|cge|pd|item|itens|art|módulo|modulo|r)\W*$")


class ErroRoteiro(Exception):
    pass


def rgb(valor, padrao):
    v = valor if valor not in (None, "") else padrao
    if isinstance(v, (list, tuple)) and len(v) == 3:
        return tuple(int(c) for c in v)
    v = PALETA.get(str(v).lower(), FUNDOS.get(str(v).lower(), v))
    if not isinstance(v, str) or not re.fullmatch(r"#[0-9A-Fa-f]{6}", v):
        raise ErroRoteiro(f"cor inválida: {valor!r} (use {', '.join(PALETA)} ou #RRGGBB)")
    return tuple(int(v[i:i + 2], 16) for i in (1, 3, 5))


class Ruido:
    """Soma de senos com fase aleatória: ondulação suave ao longo de s (em px)."""

    def __init__(self, rng, ondas):
        self.c = [(2 * math.pi / (L * rng.uniform(0.7, 1.3)), A * rng.uniform(0.6, 1.0),
                   rng.uniform(0, 2 * math.pi)) for L, A in ondas]

    def __call__(self, s):
        return sum(A * math.sin(w * s + f) for w, A, f in self.c)


def densificar(pts, passo=3.0):
    out = [tuple(pts[0])]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / passo))
        out += [(x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n) for i in range(1, n + 1)]
    return out


def bezier(p0, c, p1, n):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t * t * p1[0],
             (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t * t * p1[1])
            for t in (i / n for i in range(n + 1))]


def uniao(a, b):
    return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))


def quebrar(chars, larg_max, medir):
    """Quebra a lista de (caractere, cor) em linhas que cabem em larg_max (px)."""
    pars = [[]]
    for c in chars:
        if c[0] == "\n":
            pars.append([])
        else:
            pars[-1].append(c)
    linhas = []
    for par in pars:
        palavras, atual = [], []
        for c in par:
            if c[0] == " ":
                if atual:
                    palavras.append(atual)
                    atual = []
            else:
                atual.append(c)
        if atual:
            palavras.append(atual)
        if not palavras:
            linhas.append([])
            continue
        linha = palavras[0]
        for pw in palavras[1:]:
            cand = linha + [(" ", None)] + pw
            if larg_max and medir(cand) > larg_max:
                linhas.append(linha)
                linha = pw
            else:
                linha = cand
        linhas.append(linha)
    return linhas


class Lousa:
    def __init__(self, spec, pasta_roteiro, avisos):
        self.W = int(spec.get("largura", 1920))
        self.H = int(spec.get("altura", 1080))
        self.imp_base = self.imp = float(spec.get("imperfeicao", 1.0))
        self.peso_base = self.peso = float(spec.get("peso", 1.0))  # engrossa a letra (0 = fonte pura)
        # padrão X8: letra reta, alinhada e em caixa alta; o tremor fica nos traços (caixas, setas, desenhos)
        self.tremor_texto = float(spec.get("tremor_texto", 0.0))
        self.maiusculas = bool(spec.get("maiusculas", True))
        areas = spec.get("areas_livres", AREAS_LIVRES)
        self.areas = [list(a) for a in (areas or [])]
        self.rng = random.Random(spec.get("semente", 7))
        # ruído do fundo/giz com semente própria: mesma semente = mesma imagem, byte a byte
        self.rng_fundo = random.Random(f"fundo-{spec.get('semente', 7)}")
        self.avisos = avisos
        fonte = spec.get("fonte")
        if fonte:
            self.fonte_path = fonte if os.path.isabs(fonte) else os.path.join(pasta_roteiro, fonte)
            self.deslant = float(spec.get("endireitar", 0.0))
        else:
            self.fonte_path = FONTE_PADRAO
            # a Permanent Marker é levemente inclinada; o molde é em pé
            self.deslant = float(spec.get("endireitar", 0.16))
        if not os.path.exists(self.fonte_path):
            raise ErroRoteiro(f"fonte não encontrada: {self.fonte_path}")
        fundo = spec.get("fundo", "preto")
        self.giz = bool(spec.get("giz", fundo == "lousa"))
        self.bg = self.criar_fundo(fundo, bool(spec.get("textura", fundo == "lousa")))
        self.canvas = self.bg.copy()
        self.draw = ImageDraw.Draw(self.canvas)
        self.reg = {}
        self._fontes, self._masc, self._tem = {}, {}, {}
        self._notdef = None
        self._modo_tecla = False  # True enquanto mede/desenha o rótulo de uma tecla

    # ------------------------------------------------------------------ fundo
    def criar_fundo(self, nome, textura):
        cor = rgb(nome, "preto")
        W, H = self.W * SS, self.H * SS
        im = Image.new("RGB", (W, H), cor)
        if textura:
            clara = Image.new("RGB", (W, H), (255, 255, 255))
            # pó de giz apagado: manchas grandes e fracas (sem padrão de "camuflagem")
            manchas = self.ruido((self.W // 160 + 2, self.H // 160 + 2)).resize((W, H), Image.BICUBIC)
            manchas = manchas.filter(ImageFilter.GaussianBlur(40 * SS))
            im = Image.composite(clara, im, manchas.point(lambda v: max(0, min(16, int((v - 118) * 0.6)))))
            grao = self.ruido((W, H))  # ~7% dos pontos com um leve pó claro
            im = Image.composite(clara, im, grao.point(lambda v: max(0, min(18, v - 237))))
        return im

    def ruido(self, tam):
        """Imagem L de ruído uniforme 0–255, reprodutível pela semente."""
        return Image.frombytes("L", tam, self.rng_fundo.randbytes(tam[0] * tam[1]))

    # ------------------------------------------------------------------ traço à mão
    def tracar(self, pts, cor, larg=5.0, ondula=1.0, serrilha=0.3, tremor=0.6):
        """Desenha um traço livre: ondulação lenta + serrilha média (borda de caixa do molde)
        + tremor fino + espessura que varia."""
        p = densificar(pts, 3.0)
        if len(p) < 2:
            return
        imp, rng = self.imp, self.rng
        s = [0.0]
        for a, b in zip(p, p[1:]):
            s.append(s[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
        baixo = Ruido(rng, [(320, 2.6), (140, 1.3)])
        medio = Ruido(rng, [(46, 1.6), (27, 0.9)])
        alto = Ruido(rng, [(14, 0.5), (8, 0.25)])
        varl = Ruido(rng, [(90, 0.12), (35, 0.06)])
        n = len(p)
        out, ws = [], []
        for i in range(n):
            x0, y0 = p[max(0, i - 1)]
            x1, y1 = p[min(n - 1, i + 1)]
            L = math.hypot(x1 - x0, y1 - y0) or 1.0
            nx, ny = -(y1 - y0) / L, (x1 - x0) / L
            d = imp * (ondula * baixo(s[i]) + serrilha * medio(s[i]) + tremor * alto(s[i]))
            out.append(((p[i][0] + nx * d) * SS, (p[i][1] + ny * d) * SS))
            ws.append(max(1.2, larg * (1 + imp * varl(s[i]))) * SS)
        for i in range(n - 1):
            self.draw.line([out[i], out[i + 1]], fill=cor, width=max(1, round((ws[i] + ws[i + 1]) / 2)))
        for (x, y), w in zip(out, ws):
            r = w / 2
            self.draw.ellipse([x - r, y - r, x + r, y + r], fill=cor)

    def pts_elipse(self, cx, cy, rx, ry, a0=None, a1=None, giro=0.0):
        rng, imp = self.rng, self.imp
        fechada = a0 is None
        if fechada:  # dá uma "passada" além do início, como quem fecha o círculo à mão
            ini = rng.uniform(0, 2 * math.pi)
            fim = ini + 2 * math.pi + rng.uniform(0.25, 0.55) * max(imp, 0.3)
        else:
            ini, fim = math.radians(a0), math.radians(a1)
        perim = math.pi * (rx + ry) * abs(fim - ini) / (2 * math.pi)
        n = max(12, int(perim / 4))
        mod = Ruido(rng, [(max(60.0, perim / 2), 0.035 * imp)])
        espiral = rng.uniform(-0.05, 0.05) * imp if fechada else 0.0
        cg, sg = math.cos(giro), math.sin(giro)
        pts = []
        for i in range(n + 1):
            t = i / n
            a = ini + (fim - ini) * t
            k = 1 + mod(t * perim) + espiral * t
            ex, ey = rx * k * math.cos(a), ry * k * math.sin(a)
            pts.append((cx + ex * cg - ey * sg, cy + ex * sg + ey * cg))
        return pts

    def ponta_seta(self, tip, ang, tam, cor, larg):
        ab = math.radians(27 + self.rng.gauss(0, 3) * self.imp)
        w1 = (tip[0] - tam * math.cos(ang - ab), tip[1] - tam * math.sin(ang - ab))
        w2 = (tip[0] - tam * math.cos(ang + ab), tip[1] - tam * math.sin(ang + ab))
        self.tracar([w1, tip, w2], cor, larg, ondula=0.25, tremor=0.4)

    # ------------------------------------------------------------------ letras
    def fonte(self, tam):
        caminho = FONTE_TECLA if self._modo_tecla and os.path.exists(FONTE_TECLA) else self.fonte_path
        k = (caminho, max(4, round(tam * SS)))
        if k not in self._fontes:
            self._fontes[k] = ImageFont.truetype(caminho, k[1])
        return self._fontes[k]

    def em_tecla(self, func, *args):
        """Executa func com a fonte das teclas ligada."""
        antes, self._modo_tecla = self._modo_tecla, True
        try:
            return func(*args)
        finally:
            self._modo_tecla = antes

    def tem_glifo(self, ch):
        if ch.isspace() or ch in DESENHADOS or ord(ch) < 127:
            return True
        if ch not in self._tem:
            f = self.fonte(40)

            def desenho(c):  # caractere ausente sai igual ao glifo "vazio" (.notdef) da fonte
                im = Image.new("L", (200, 200), 0)
                ImageDraw.Draw(im).text((40, 40), c, font=f, fill=255)
                return im.tobytes()

            if self._notdef is None:
                self._notdef = desenho("")
            self._tem[ch] = desenho(ch) != self._notdef
        return self._tem[ch]

    def avanco(self, ch, tam):
        """Largura de um item de texto: letra, tecla "\\x01ROTULO", letra com barra "\\x02x" ou símbolo desenhado."""
        if ch.startswith("\x01"):
            tk = self.tam_tecla(tam)
            return self.em_tecla(lambda: sum(self.avanco(t, tk) for t in self.rotulo(ch[1:]))) + tam * 0.62
        if ch.startswith("\x03"):  # índice (subscrito)
            return self.avanco(ch[1:], self.tam_sub(tam))
        if ch.startswith("\x02"):
            ch = ch[1:]
        if ch == "\u00a0":
            ch = " "
        if ch == "σ":
            return tam * 0.6
        if ch == "β":
            return tam * 0.56
        if ch in SETAS_TEXTO or ch in ("✓", "✗", "⚠"):
            return tam * 0.95
        if ch in ("Σ", "Δ"):
            return tam * 0.62
        return self.fonte(tam).getlength(ch) / SS

    @staticmethod
    def tam_sub(tam):
        return max(28.0, tam * SUB_ESC)  # índice também respeita o mínimo de 28 px do padrão X8

    @staticmethod
    def tam_tecla(tam):
        return max(28.0, tam * 0.8)  # rótulo da tecla: nunca abaixo do mínimo de 28 px

    @staticmethod
    def rotulo(rot):
        """Itens do rótulo de uma tecla (x̄ vira "\\x02x"; ∑ vira Σ)."""
        out = []
        for c in rot:
            if c in INVISIVEIS:
                continue
            if c == MACRON and out:
                out[-1] = "\x02" + out[-1][-1]
                continue
            out.append(TROCAS[c] if c in ("∑", "∆") else c)
        return out

    def metricas(self, tam):
        f = self.fonte(tam)
        cap = -f.getbbox("H", anchor="ls")[1] / SS
        desc = f.getbbox("Qgjpy,", anchor="ls")[3] / SS
        return cap, desc

    def mascara(self, ch, tam):
        raio = round(self.peso * tam * SS * 0.015)
        k = (ch, round(tam * SS), raio, self._modo_tecla)
        if k not in self._masc:
            f = self.fonte(tam)
            l, t, r, b = f.getbbox(ch, anchor="ls")
            pad = int(tam * SS * 0.5) + 4
            im = Image.new("L", (max(1, r - l) + 2 * pad, max(1, b - t) + 2 * pad), 0)
            ax, ay = pad - l, pad - t
            ImageDraw.Draw(im).text((ax, ay), ch, font=f, fill=255, anchor="ls")
            if raio > 0:  # traço de pincel mais gordo, como no molde
                im = im.filter(ImageFilter.MaxFilter(2 * raio + 1))
            self._masc[k] = (im, ax, ay)
        return self._masc[k]

    def letra(self, ch, x, base, tam, cor, ang=0.0, esc=1.0):
        """Desenha uma letra com a base em (x, base), girada/escalada e endireitada."""
        im, ax, ay = self.mascara(ch, tam)
        k, c, s = (0.0 if self._modo_tecla else self.deslant), math.cos(ang), math.sin(ang)
        F = (esc * c, esc * (c * k - s), esc * s, esc * (s * k + c))
        det = F[0] * F[3] - F[1] * F[2]
        i00, i01, i10, i11 = F[3] / det, -F[1] / det, -F[2] / det, F[0] / det
        data = (i00, i01, ax - i00 * ax - i01 * ay, i10, i11, ay - i10 * ax - i11 * ay)
        tm = im.transform(im.size, Image.AFFINE, data, resample=Image.BICUBIC)
        X, Y = round(x * SS - ax), round(base * SS - ay)
        self.canvas.paste(cor, (X, Y, X + im.size[0], Y + im.size[1]), tm)

    def seta_no_texto(self, ch, x, base, tam, cor):
        ang = math.radians(SETAS_TEXTO[ch])
        cx, cy = x + tam * 0.47, base - tam * 0.36
        L = tam * 0.36
        p0 = (cx - L * math.cos(ang), cy - L * math.sin(ang))
        p1 = (cx + L * math.cos(ang), cy + L * math.sin(ang))
        larg = max(2.5, tam * 0.085)
        self.tracar([p0, p1], cor, larg, ondula=0.15, tremor=0.3)
        self.ponta_seta(p1, ang, tam * 0.28, cor, larg)

    def glifo_desenhado(self, ch, x, base, tam, cor):
        """Emojis e símbolos sem glifo na fonte, desenhados à mão: ✓ verde, ✗ vermelho, ⚠ vermelho, Σ."""
        cap, _ = self.metricas(tam)
        w = self.avanco(ch, tam)
        larg = max(2.5, tam * 0.085)
        if ch == "✓":
            self.tracar([(x + 0.12 * w, base - 0.48 * cap), (x + 0.4 * w, base - 0.04 * cap),
                         (x + 0.9 * w, base - cap)], rgb(None, "verde"), larg * 1.2, ondula=0.15, serrilha=0.2,
                        tremor=0.3)
        elif ch == "✗":
            vm = rgb(None, "vermelho")
            self.tracar([(x + 0.15 * w, base - 0.95 * cap), (x + 0.85 * w, base)], vm, larg * 1.1, ondula=0.15,
                        serrilha=0.2, tremor=0.3)
            self.tracar([(x + 0.85 * w, base - 0.95 * cap), (x + 0.15 * w, base)], vm, larg * 1.1, ondula=0.15,
                        serrilha=0.2, tremor=0.3)
        elif ch == "⚠":
            vm = rgb(None, "vermelho")
            self.tracar([(x + 0.5 * w, base - 1.05 * cap), (x + 0.97 * w, base), (x + 0.03 * w, base),
                         (x + 0.5 * w, base - 1.05 * cap), (x + 0.56 * w, base - 0.95 * cap)], vm, larg,
                        ondula=0.12, serrilha=0.2, tremor=0.3)
            self.tracar([(x + 0.5 * w, base - 0.7 * cap), (x + 0.5 * w, base - 0.34 * cap)], vm, larg,
                        ondula=0.05, serrilha=0.1, tremor=0.2)
            r = larg * 0.8
            px, py = (x + 0.5 * w) * SS, (base - 0.15 * cap) * SS
            self.draw.ellipse([px - r * SS, py - r * SS, px + r * SS, py + r * SS], fill=vm)
        elif ch == "Δ":  # tecla Δ% da HP12C
            self.tracar([(x + 0.5 * w, base - cap), (x + 0.92 * w, base), (x + 0.08 * w, base),
                         (x + 0.5 * w, base - cap), (x + 0.6 * w, base - 0.8 * cap)], cor, larg, ondula=0.08,
                        serrilha=0.15, tremor=0.2)
        elif ch == "σ":  # sigma minúsculo (desvio-padrão): bolinha com o traço saindo pela direita, no topo
            ry = 0.37 * cap
            cx, cy, rx = x + 0.4 * w, base - ry, 0.32 * w
            self.tracar(self.pts_elipse(cx, cy, rx, ry, -60, 300), cor, larg, ondula=0.08, serrilha=0.15,
                        tremor=0.2)
            self.tracar([(cx, cy - ry), (x + 0.98 * w, cy - ry - 0.03 * cap)], cor, larg, ondula=0.05,
                        serrilha=0.1, tremor=0.2)
        elif ch == "β":  # beta minúsculo (risco sistemático): haste que desce da linha e duas barrigas
            xh = x + 0.16 * w
            self.tracar([(xh, base - 0.98 * cap), (xh, base + 0.3 * tam)], cor, larg, ondula=0.05, serrilha=0.1,
                        tremor=0.2)
            self.tracar(self.pts_elipse(xh, base - 0.78 * cap, 0.56 * w, 0.2 * cap, -90, 90), cor, larg,
                        ondula=0.06, serrilha=0.12, tremor=0.2)
            self.tracar(self.pts_elipse(xh, base - 0.29 * cap, 0.74 * w, 0.29 * cap, -90, 90), cor, larg,
                        ondula=0.06, serrilha=0.12, tremor=0.2)
        elif ch == "Σ":
            self.tracar([(x + 0.9 * w, base - cap), (x + 0.1 * w, base - cap), (x + 0.55 * w, base - 0.5 * cap),
                         (x + 0.1 * w, base), (x + 0.9 * w, base)], cor, larg, ondula=0.08, serrilha=0.15,
                        tremor=0.2)

    def retangulo(self, x0, y0, x1, y1, cor, larg, passada=9.0, ondula=0.5, serrilha=1.5, tremor=0.6):
        """Retângulo à mão: quatro traços, cantos que não batem e passam um pouco do ponto."""
        rng, imp = self.rng, self.imp
        j = min(3.0, (x1 - x0) / 40, (y1 - y0) / 15) * imp
        cantos = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        cantos = [(cx + rng.gauss(0, j), cy + rng.gauss(0, j)) for cx, cy in cantos]
        for i in range(4):
            p, q = cantos[i], cantos[(i + 1) % 4]
            L = math.hypot(q[0] - p[0], q[1] - p[1]) or 1
            ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L
            e0, e1 = rng.uniform(-0.25, 0.8) * passada * imp, rng.uniform(0, 1) * passada * imp
            self.tracar([(p[0] - ux * e0, p[1] - uy * e0), (q[0] + ux * e1, q[1] + uy * e1)],
                        cor, larg, ondula=ondula, serrilha=serrilha, tremor=tremor)
        return cantos

    def tecla(self, rot, x, base, tam, cor):
        """Tecla da HP12C: rótulo dentro de uma caixinha desenhada à mão, na linha do texto."""
        self.em_tecla(self._tecla, rot, x, base, tam, cor)

    def _tecla(self, rot, x, base, tam, cor):
        tk = self.tam_tecla(tam)
        capk, _ = self.metricas(tk)
        itens = self.rotulo(rot)
        padx, gap = tam * 0.22, tam * 0.18
        lw = sum(self.avanco(t, tk) for t in itens)
        x0 = x + gap / 2
        self.retangulo(x0, base - capk - tam * 0.34, x0 + lw + 2 * padx, base + tam * 0.2, cor,
                       max(2.2, tam * 0.06), passada=3.0, ondula=0.12, serrilha=0.3, tremor=0.3)
        cx = x0 + padx
        for t in itens:
            self.desenhar_token(t, cx, base, tk, cor)
            cx += self.avanco(t, tk)

    def desenhar_token(self, ch, x, base, tam, cor, ang=0.0, esc=1.0):
        if ch.startswith("\x03"):  # índice: menor e abaixo da linha
            if ch[1:] != " ":
                self.desenhar_token(ch[1:], x, base + tam * SUB_DESCE, self.tam_sub(tam), cor, ang, esc)
        elif ch.startswith("\x01"):
            self.tecla(ch[1:], x, base, tam, cor)
        elif ch.startswith("\x02"):  # letra com barra em cima (x̄)
            c = ch[1:]
            self.desenhar_token(c, x, base, tam, cor, ang, esc)
            cap, _ = self.metricas(tam)
            w, yb = self.avanco(c, tam), base - cap - tam * 0.11
            self.tracar([(x + w * 0.12, yb), (x + w * 0.88, yb)], cor, max(2.0, tam * 0.07), ondula=0.05,
                        serrilha=0.1, tremor=0.2)
        elif ch in SETAS_TEXTO:
            self.seta_no_texto(ch, x, base, tam, cor)
        elif ch in DESENHADOS:
            self.glifo_desenhado(ch, x, base, tam, cor)
        else:
            self.letra(ch, x, base, tam, cor, ang, esc)

    def dim_circulo(self, num, tam, cap):
        tn = max(28.0, tam * 0.66)
        capn, _ = self.metricas(tn)
        wn = sum(self.avanco(c, tn) for c in num)
        return max(cap * 1.32, capn * 1.85, wn * 1.45 + 4), tn

    def largura_marcador(self, marcador, tam, cap):
        if marcador[0] == "num":
            return self.dim_circulo(marcador[1], tam, cap)[0] + tam * 0.42
        return tam * 0.72

    def desenhar_marcador(self, marcador, x, base, tam, cap):
        """Número de lista dentro de circulinho (padrão X8) ou marcador de tópico/subitem."""
        cor = marcador[2]
        if marcador[0] == "num":
            d, tn = self.dim_circulo(marcador[1], tam, cap)
            cx, cy = x + d / 2, base - cap / 2
            self.tracar(self.pts_elipse(cx, cy, d / 2, d / 2), cor, max(2.5, tam * 0.07), ondula=0.12,
                        serrilha=0.3, tremor=0.4)
            capn, _ = self.metricas(tn)
            xx = cx - sum(self.avanco(c, tn) for c in marcador[1]) / 2
            for c in marcador[1]:
                self.letra(c, xx, cy + capn / 2, tn, cor)
                xx += self.avanco(c, tn)
        elif marcador[1] == 0:  # tópico: bolinha cheia
            r = tam * 0.13
            px, py = (x + r * 1.4) * SS, (base - cap * 0.45) * SS
            self.draw.ellipse([px - r * SS, py - r * SS, px + r * SS, py + r * SS], fill=cor)
        else:  # subtópico/subitem: tracinho
            self.tracar([(x, base - cap * 0.45), (x + tam * 0.32, base - cap * 0.45)], cor,
                        max(2.5, tam * 0.08), ondula=0.05, serrilha=0.1, tremor=0.2)

    def checar_texto(self, texto, onde):
        """Regras do padrão X8 que dá para conferir no texto: sem LaTeX, vírgula decimal, ponto de milhar."""
        limpo = TECLA.sub(" ", SUB.sub(r"\1", MARCA.sub(r"\2", texto))).replace("R$", "R ")  # R$ não é LaTeX
        m = LATEX.search(limpo)
        if m:
            self.avisos.append(f"{onde}: sobra de LaTeX ({m.group(0)!r}); escreva como texto comum")
        for m in DECIMAL_PONTO.finditer(limpo):
            if not ITEM_PD.search(limpo[max(0, m.start() - 12):m.start()].lower()):
                self.avisos.append(f"{onde}: {m.group(0)!r} usa ponto decimal; o padrão é vírgula decimal")
                break
        m = SEM_MILHAR.search(limpo)
        if m:
            self.avisos.append(f"{onde}: {m.group(0)!r} sem ponto de milhar (ex.: 10.000)")

    def marcar(self, texto, cor_base, onde, maiusculas=False):
        """Aplica {cor:trecho}, [TECLA], caixa alta e trocas; devolve [(item, cor)]."""
        trechos, pos = [], 0
        for m in MARCA.finditer(texto):
            trechos.append((texto[pos:m.start()], cor_base))
            try:
                c2 = rgb(m.group(1), None)
            except ErroRoteiro:
                self.avisos.append(f"{onde}: cor desconhecida em {{{m.group(1)}:...}}; usei a cor do texto")
                c2 = cor_base
            trechos.append((m.group(2), c2))
            pos = m.end()
        trechos.append((texto[pos:], cor_base))
        out, faltou = [], set()

        def junta(c, k):
            if c in INVISIVEIS:
                return
            if c == MACRON:
                if out and len(out[-1][0]) == 1 and out[-1][0] not in " \n":
                    out[-1] = ("\x02" + out[-1][0], out[-1][1])
                return
            c = EMOJIS.get(c, c)
            if c in TROCAS:
                out.extend((t, k) for t in TROCAS[c])
            elif c == "\n" or self.tem_glifo(c):
                out.append((c, k))
            else:
                faltou.add(c)

        def alta(s):  # caixa alta sem estragar σ e β
            return "".join(c if c in GREGOS else c.upper() for c in s) if maiusculas else s

        for trecho0, k in trechos:
            pedacos, q = [], 0
            for ms in SUB.finditer(trecho0):
                pedacos += [(trecho0[q:ms.start()], False), (ms.group(1), True)]
                q = ms.end()
            pedacos.append((trecho0[q:], False))
            for trecho, sub in pedacos:
                if sub:  # índice: cada letra vira "\x03letra"
                    for c in alta(trecho):
                        c = TROCAS.get(c, c) if len(TROCAS.get(c, c)) == 1 else c
                        if c in INVISIVEIS:
                            continue
                        if c == " " or self.tem_glifo(c):
                            out.append(("\x03" + c, k))
                        else:
                            faltou.add(c)
                    continue
                p = 0
                for m in list(TECLA.finditer(trecho)) + [None]:
                    parte = trecho[p:m.start()] if m else trecho[p:]
                    for c in alta(parte):
                        junta(c, k)
                    if m:  # tecla também em caixa alta: nesta fonte o "g" minúsculo parece "6"
                        rot = m.group(1).strip()
                        out.append(("\x01" + (rot.upper() if maiusculas else rot), k))
                        p = m.end()
        if faltou:
            self.avisos.append(f"{onde}: a fonte não tem {''.join(sorted(faltou))!r}; caractere(s) omitido(s)")
        return out

    # ------------------------------------------------------------------ posição e alvos
    def bbox_de(self, ref, onde):
        if isinstance(ref, (list, tuple)) and len(ref) == 4:
            return tuple(float(v) for v in ref)
        if isinstance(ref, (list, tuple)) and len(ref) == 2:
            return (float(ref[0]), float(ref[1]), float(ref[0]), float(ref[1]))
        if ref not in self.reg:
            ids = ", ".join(self.reg) or "nenhum ainda"
            raise ErroRoteiro(f"{onde}: id {ref!r} não existe (ids já desenhados: {ids}). "
                              "Lembre: o alvo precisa vir ANTES no roteiro.")
        return self.reg[ref]["bbox"]

    def posicionar(self, el, w, h, onde):
        x, y = el.get("x"), el.get("y")
        dist = float(el.get("distancia", 40))
        for chave in ("abaixo_de", "acima_de", "direita_de", "esquerda_de"):
            if chave not in el:
                continue
            b = self.bbox_de(el[chave], onde)
            cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
            if chave == "abaixo_de":
                x = cx - w / 2 if x is None else x
                y = b[3] + dist if y is None else y
            elif chave == "acima_de":
                x = cx - w / 2 if x is None else x
                y = b[1] - dist - h if y is None else y
            elif chave == "direita_de":
                x = b[2] + dist if x is None else x
                y = cy - h / 2 if y is None else y
            else:
                x = b[0] - dist - w if x is None else x
                y = cy - h / 2 if y is None else y
        if x == "centro":
            x = (self.W - w) / 2
        if y == "centro":
            y = (self.H - h) / 2
        if x is None or y is None:
            raise ErroRoteiro(f"{onde}: falta posição (x e y, ou abaixo_de/acima_de/direita_de/esquerda_de)")
        return float(x), float(y)

    def registrar(self, el, tipo, bbox, cor, **extra):
        i = el.get("id") or f"{tipo}{len(self.reg) + 1}"
        if el.get("id") in self.reg:
            self.avisos.append(f"id {i!r} repetido; o novo substitui o anterior")
        self.reg[i] = dict(tipo=tipo, bbox=bbox, cor=cor, **extra)
        return i

    def expandir(self, ref, bbox):
        if isinstance(ref, str) and ref in self.reg:
            self.reg[ref]["bbox"] = uniao(self.reg[ref]["bbox"], bbox)

    def alvo(self, el, onde):
        """bbox, cor e registro do alvo (por id) ou da área x/y/largura/altura."""
        if "alvo" in el:
            b = self.bbox_de(el["alvo"], onde)
            info = self.reg.get(el["alvo"]) if isinstance(el["alvo"], str) else None
            return b, (info or {}).get("cor"), info
        if all(k in el for k in ("x", "y", "largura", "altura")):
            x, y = float(el["x"]), float(el["y"])
            return (x, y, x + float(el["largura"]), y + float(el["altura"])), None, None
        raise ErroRoteiro(f"{onde}: informe 'alvo' (id) ou x, y, largura e altura")

    # ------------------------------------------------------------------ elementos
    def el_texto(self, el, onde, tipo="texto", medir=False):
        so_medir = medir
        """Desenha um bloco de texto; com medir=True só devolve (largura, altura), sem desenhar nem avisar."""
        if so_medir is True:  # mede sem deixar avisos (a medida de verdade roda com medir="ja")
            guarda, self.avisos = self.avisos, []
            try:
                return self.el_texto(el, onde, tipo, medir="ja")
            finally:
                self.avisos = guarda
        titulo = tipo == "titulo"
        tam = float(el.get("tamanho", {"titulo": 44, "subtitulo": 40}.get(tipo, 36)))
        cor_base = rgb(el.get("cor"), {"titulo": "amarelo", "subtitulo": "ciano"}.get(tipo, "branco"))
        esp = float(el.get("espacamento", 0.1))
        entre = float(el.get("entrelinha", 1.38))
        alinhar = el.get("alinhar", "esquerda")
        larg_max = el.get("largura")
        larg_max = float(larg_max) if larg_max else None
        texto = str(el.get("texto", ""))
        self.checar_texto(texto, onde)
        toks = self.marcar(texto, cor_base, onde, bool(el.get("maiusculas", self.maiusculas)))
        usar_lista = bool(el.get("lista", tipo == "texto"))
        cap, desc = self.metricas(tam)

        def medir(cs):
            return sum(self.avanco(c, tam) * (1 + esp) + (tam * 0.1 if c in ESPACOS else 0) for c, _ in cs)

        # parágrafos: 2 espaços no início = 1 nível de recuo; "1. " = circulinho; "- " ou "• " = tópico
        pars = [[]]
        for t in toks:
            if t[0] == "\n":
                pars.append([])
            else:
                pars[-1].append(t)
        linhas = []
        for par in pars:
            nivel = 0
            while len(par) >= 2 and par[0][0] == " " and par[1][0] == " ":
                par, nivel = par[2:], nivel + 1
            while par and par[0][0] == " ":
                par = par[1:]
            marcador = None
            if usar_lista and par:
                inicio = "".join(t[0] if len(t[0]) == 1 else "#" for t in par[:5])
                m = MARCADOR_NUM.match(inicio)
                if m:
                    marcador, par = ("num", m.group(1), par[0][1]), par[m.end():]
                elif inicio[:2] in ("- ", "• "):
                    marcador, par = ("ponto", nivel, par[0][1]), par[2:]
            recuo = nivel * tam * 1.1
            lm = self.largura_marcador(marcador, tam, cap) if marcador else 0.0
            disp = max(tam * 3, larg_max - recuo - lm) if larg_max else None
            for j, l in enumerate(quebrar(par, disp, medir)):
                linhas.append(dict(toks=l, xm=recuo, recuo=recuo + lm, marcador=marcador if j == 0 else None))
        lws = [ln["recuo"] + medir(ln["toks"]) for ln in linhas]
        if larg_max and any(lw > larg_max + 1 for lw in lws):
            self.avisos.append(f"{onde}: palavra não cabe em largura={larg_max:.0f}; aumente a largura")
        lh = tam * entre
        wref = larg_max if (larg_max and alinhar != "esquerda") else max(lws or [0])
        h = cap + (len(linhas) - 1) * lh + desc
        if so_medir:
            return max(lws or [0.0]), h
        if titulo:
            el = dict({"x": 40, "y": 24}, **el)
        x, y = self.posicionar(el, wref, h, onde)

        imp, rng = self.tremor_texto, self.rng  # padrão X8: 0 = reta e alinhada
        caixas, xs0 = [], []
        for i, (ln, lw) in enumerate(zip(linhas, lws)):
            off = {"centro": (wref - lw) / 2, "direita": wref - lw}.get(alinhar, 0.0)
            lx = x + off + rng.gauss(0, 3) * imp
            base0 = y + cap + i * lh
            incl = rng.gauss(0, 0.006) * imp
            onda = Ruido(rng, [(tam * 6, tam * 0.022 * imp), (tam * 2.5, tam * 0.012 * imp)])
            if ln["marcador"]:
                self.desenhar_marcador(ln["marcador"], lx + ln["xm"], base0, tam, cap)
            cx = lx + ln["recuo"]
            for ch, cor in ln["toks"]:
                adv = self.avanco(ch, tam) * (1 + esp)
                if ch in ESPACOS:
                    cx += adv + tam * 0.1 + rng.gauss(0, tam * 0.03) * imp
                    continue
                base = base0 + incl * (cx - lx) + onda(cx - lx) + rng.gauss(0, tam * 0.028) * imp
                ang = max(-0.09, min(0.09, rng.gauss(0, math.radians(2.2) * imp) + incl))
                esc = max(0.9, min(1.1, 1 + rng.gauss(0, 0.035) * imp))
                self.desenhar_token(ch, cx, base, tam, cor, ang, esc)
                cx += adv + rng.gauss(0, tam * 0.018) * imp
            caixas.append((lx + ln["recuo"], base0, max(cx, lx + ln["recuo"])))
            xs0.append(lx + ln["xm"])
        x0 = min(xs0, default=x)
        x1 = max((c[2] for c in caixas), default=x)
        bbox = (x0, y, x1, y + h)
        if el.get("sublinhado", titulo):
            yb = caixas[-1][1] + tam * 0.45 if caixas else y + h
            self.tracar([(x0 - 6, yb), (x1 + 10, yb + rng.gauss(0, 1.5))], cor_base,
                        float(el.get("espessura_sublinhado", 3.4)), ondula=0.55, tremor=0.7)
            bbox = (bbox[0] - 6, bbox[1], bbox[2] + 10, yb + 4)
        return self.registrar(el, tipo, bbox, cor_base, linhas=caixas, tam=tam, cap=cap)

    def largura_texto(self, texto, tam, maiusculas, esp=0.1):
        """Largura de uma linha de texto (sem desenhar e sem repetir avisos)."""
        guarda, self.avisos = self.avisos, []
        try:
            toks = self.marcar(texto, (255, 255, 255), "", maiusculas)
        finally:
            self.avisos = guarda
        return sum(self.avanco(c, tam) * (1 + esp) + (tam * 0.1 if c in ESPACOS else 0) for c, _ in toks)

    def el_fracao(self, el, onde, medir=False):
        """Fórmula com fração escrita à mão: [antes] numerador sobre denominador [depois]."""
        tam = float(el.get("tamanho", 52))
        maiusc = bool(el.get("maiusculas", self.maiusculas))
        cor = el.get("cor", "branco")
        antes, depois = str(el.get("antes", "")), str(el.get("depois", ""))
        num, den = str(el.get("num", "")), str(el.get("den", ""))
        if not num or not den:
            raise ErroRoteiro(f"{onde}: 'fracao' precisa de 'num' (numerador) e 'den' (denominador)")
        cap, desc = self.metricas(tam)
        gap = tam * 0.35
        wa = self.largura_texto(antes, tam, maiusc) if antes else 0.0
        wd_ = self.largura_texto(depois, tam, maiusc) if depois else 0.0
        wn, wd = self.largura_texto(num, tam, maiusc), self.largura_texto(den, tam, maiusc)
        wb = max(wn, wd) + tam * 0.5
        y_bar = cap + max(desc * 0.8, tam * (SUB_DESCE + 0.2)) + tam * 0.08  # do topo do numerador (cabe índice)
        y_den = y_bar + tam * 0.3
        W = wa + (gap if antes else 0) + wb + (gap if depois else 0) + wd_
        H = y_den + cap + desc
        if medir:
            return W, H
        x, y = self.posicionar(el, W, H, onde)
        antes_reg = set(self.reg)
        base = dict(tamanho=tam, cor=cor, lista=False, maiusculas=maiusc, espacamento=0.1)
        xb = x + wa + (gap if antes else 0)
        if antes:
            self.el_texto(dict(base, texto=antes, x=x, y=y + y_bar - cap / 2), onde + " antes")
        self.el_texto(dict(base, texto=num, x=xb + (wb - wn) / 2, y=y), onde + " numerador")
        self.el_texto(dict(base, texto=den, x=xb + (wb - wd) / 2, y=y + y_den), onde + " denominador")
        if depois:
            self.el_texto(dict(base, texto=depois, x=xb + wb + gap, y=y + y_bar - cap / 2), onde + " depois")
        for i in set(self.reg) - antes_reg:  # as partes contam como um elemento só
            del self.reg[i]
        cb = rgb(el.get("cor_barra", cor), "branco")
        self.tracar([(xb, y + y_bar), (xb + wb, y + y_bar + self.rng.gauss(0, 1.2))], cb, max(3.0, tam * 0.075),
                    ondula=0.25, serrilha=0.3, tremor=0.4)
        return self.registrar(el, "fracao", (x, y, x + W, y + H), rgb(cor, "branco"), tam=tam, cap=cap)

    def el_caixa(self, el, onde):
        b, cor_alvo, _ = self.alvo(el, onde)
        m = float(el.get("margem", 30))
        cor = rgb(el.get("cor"), "amarelo")  # padrão X8: molduras em amarelo
        larg = float(el.get("espessura", 5.5))
        rng, imp = self.rng, self.imp
        cantos = [(b[0] - m, b[1] - m), (b[2] + m, b[1] - m), (b[2] + m, b[3] + m), (b[0] - m, b[3] + m)]
        cantos = [(cx + rng.gauss(0, 3) * imp, cy + rng.gauss(0, 3) * imp) for cx, cy in cantos]
        for i in range(4):
            p, q = cantos[i], cantos[(i + 1) % 4]
            L = math.hypot(q[0] - p[0], q[1] - p[1]) or 1
            ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L
            e0, e1 = rng.uniform(-2, 7) * imp, rng.uniform(0, 9) * imp  # passa um pouco do canto
            self.tracar([(p[0] - ux * e0, p[1] - uy * e0), (q[0] + ux * e1, q[1] + uy * e1)],
                        cor, larg, ondula=0.5, serrilha=1.5, tremor=0.6)
        caixa = (min(c[0] for c in cantos) - larg, min(c[1] for c in cantos) - larg,
                 max(c[0] for c in cantos) + larg, max(c[1] for c in cantos) + larg)
        self.expandir(el.get("alvo"), caixa)
        return self.registrar(el, "caixa", caixa, cor)

    def el_circular(self, el, onde):
        b, cor_alvo, _ = self.alvo(el, onde)
        m = float(el.get("margem", 22))
        cor = rgb(el.get("cor"), "amarelo")
        larg = float(el.get("espessura", 5.0))
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        w, h = b[2] - b[0], b[3] - b[1]
        if w > 2.2 * h:  # frase comprida: "cápsula" (elipse cortaria as pontas do texto)
            pts = self.pts_capsula(b[0] - m, b[1] - m, b[2] + m, b[3] + m)
            self.tracar(pts, cor, larg, ondula=0.8, serrilha=0.4, tremor=0.6)
            caixa = (b[0] - m - larg - 8, b[1] - m - larg - 8, b[2] + m + larg + 8, b[3] + m + larg + 8)
        else:  # elipse que contém os cantos do texto (fator raiz de 2)
            rx, ry = w / 2 * 1.38 + m, h / 2 * 1.38 + m
            pts = self.pts_elipse(cx, cy, rx, ry, giro=math.radians(self.rng.gauss(0, 2)))
            self.tracar(pts, cor, larg, ondula=min(1.0, (rx + ry) / 150), tremor=0.6)
            caixa = (cx - rx * 1.06 - larg, cy - ry * 1.06 - larg, cx + rx * 1.06 + larg, cy + ry * 1.06 + larg)
        self.expandir(el.get("alvo"), caixa)
        return self.registrar(el, "circulo", caixa, cor)

    def pts_capsula(self, x0, y0, x1, y1):
        """Contorno de pílula (retângulo com pontas redondas) com início/fim que não se encontram."""
        rng, imp = self.rng, self.imp
        r = (y1 - y0) / 2
        cy = (y0 + y1) / 2
        pts = [(x0 + r + rng.uniform(-10, 20), y0 + rng.gauss(0, 3) * imp), (x1 - r, y0)]
        pts += [(x1 - r + r * math.cos(a), cy + r * math.sin(a))
                for a in (math.radians(-90 + 10 * i) for i in range(19))]
        pts += [(x0 + r, y1)]
        pts += [(x0 + r + r * math.cos(a), cy + r * math.sin(a))
                for a in (math.radians(90 + 10 * i) for i in range(19))]
        pts += [(x0 + r + rng.uniform(40, 90) * max(imp, 0.3), y0 - rng.uniform(4, 12) * imp)]
        return pts

    def el_riscar(self, el, onde):
        b, cor_alvo, info = self.alvo(el, onde)
        cor = rgb(el.get("cor"), "vermelho")  # padrão X8: vermelho = errado
        larg = float(el.get("espessura", 4.2))
        rng, imp = self.rng, self.imp
        if el.get("estilo", "x") == "linha":
            linhas = (info or {}).get("linhas") or [(b[0], (b[1] + b[3]) / 2 + 10, b[2])]
            cap = (info or {}).get("cap", 20)
            for lx0, base, lx1 in linhas:
                yy = base - cap * 0.42
                self.tracar([(lx0 - 8, yy + rng.gauss(0, 2)), (lx1 + 8, yy + rng.gauss(0, 2))],
                            cor, larg, ondula=0.6, tremor=0.6)
            return self.registrar(el, "risco", b, cor)
        mx, my = float(el.get("margem", 38)), float(el.get("margem", 38)) * 1.2
        x0, y0, x1, y1 = b[0] - mx, b[1] - my, b[2] + mx, b[3] + my
        for p, q in (((x0, y0), (x1, y1)), ((x0, y1), (x1, y0))):
            p = (p[0] + rng.gauss(0, 6) * imp, p[1] + rng.gauss(0, 6) * imp)
            q = (q[0] + rng.gauss(0, 6) * imp, q[1] + rng.gauss(0, 6) * imp)
            L = math.hypot(q[0] - p[0], q[1] - p[1])
            arco = rng.gauss(0, 0.035) * L * imp
            mid = ((p[0] + q[0]) / 2 - (q[1] - p[1]) / L * arco, (p[1] + q[1]) / 2 + (q[0] - p[0]) / L * arco)
            self.tracar(bezier(p, mid, q, max(8, int(L / 6))), cor, larg, ondula=1.0, tremor=0.5)
        caixa = (x0 - 12, y0 - 12, x1 + 12, y1 + 12)
        self.expandir(el.get("alvo"), caixa)
        return self.registrar(el, "risco", caixa, cor)

    def el_sublinhar(self, el, onde):
        b, cor_alvo, info = self.alvo(el, onde)
        cor = rgb(el.get("cor"), cor_alvo or PALETA["amarelo"])
        larg = float(el.get("espessura", 4.0))
        linhas = (info or {}).get("linhas") or [(b[0], b[3] - 6, b[2])]
        tam = (info or {}).get("tam", 40)
        bb = b
        for lx0, base, lx1 in (linhas[-1:] if el.get("so_ultima_linha") else linhas):
            yy = base + tam * 0.2
            self.tracar([(lx0 - 4, yy + self.rng.gauss(0, 1.5)), (lx1 + 8, yy + self.rng.gauss(0, 1.5))],
                        cor, larg, ondula=0.6, tremor=0.7)
            bb = uniao(bb, (lx0 - 4, yy - 6, lx1 + 8, yy + 8))
        self.expandir(el.get("alvo"), bb)
        return self.registrar(el, "sublinhado", bb, cor)

    def ancoras(self, de, para, folga, onde):
        A, B = self.bbox_de(de, onde), self.bbox_de(para, onde)
        if A[0] == A[2] and A[1] == A[3] and B[0] == B[2] and B[1] == B[3]:
            return (A[0], A[1]), (B[0], B[1])
        ca, cb = ((A[0] + A[2]) / 2, (A[1] + A[3]) / 2), ((B[0] + B[2]) / 2, (B[1] + B[3]) / 2)
        dx, dy = cb[0] - ca[0], cb[1] - ca[1]
        meia_w = (A[2] - A[0] + B[2] - B[0]) / 2 or 1
        meia_h = (A[3] - A[1] + B[3] - B[1]) / 2 or 1
        if abs(dx) / meia_w >= abs(dy) / meia_h:  # lado a lado: seta horizontal
            lo, hi = max(A[1], B[1]), min(A[3], B[3])
            ya, yb = ((lo + hi) / 2,) * 2 if lo < hi else (ca[1], cb[1])
            if dx > 0:
                return (A[2] + folga, ya), (B[0] - folga, yb)
            return (A[0] - folga, ya), (B[2] + folga, yb)
        lo, hi = max(A[0], B[0]), min(A[2], B[2])
        xa, xb = ((lo + hi) / 2,) * 2 if lo < hi else (ca[0], cb[0])
        if dy > 0:
            return (xa, A[3] + folga), (xb, B[1] - folga)
        return (xa, A[1] - folga), (xb, B[3] + folga)

    def el_seta(self, el, onde, ponta=True):
        cor = rgb(el.get("cor"), "branco")
        larg = float(el.get("espessura", 5.0))
        if "pontos" in el:
            pts = [tuple(map(float, p)) for p in el["pontos"]]
            if len(pts) < 2:
                raise ErroRoteiro(f"{onde}: 'pontos' precisa de pelo menos 2 pares [x, y]")
            self.tracar(pts, cor, larg, ondula=1.0, tremor=0.6)
            p0, p_seg, p_ant, p1 = pts[0], pts[1], pts[-2], pts[-1]
        else:
            if "de" not in el or "para" not in el:
                raise ErroRoteiro(f"{onde}: informe 'de' e 'para' (ids ou [x, y]) ou 'pontos'")
            p0, p1 = self.ancoras(el["de"], el["para"], float(el.get("folga", 28)), onde)
            L = math.hypot(p1[0] - p0[0], p1[1] - p0[1]) or 1
            curva = el.get("curva")
            curva = float(curva) if curva is not None else self.rng.gauss(0, 0.07)
            mid = ((p0[0] + p1[0]) / 2 - (p1[1] - p0[1]) / L * curva * L,
                   (p0[1] + p1[1]) / 2 + (p1[0] - p0[0]) / L * curva * L)
            self.tracar(bezier(p0, mid, p1, max(8, int(L / 6))), cor, larg, ondula=1.1, tremor=0.6)
            p_ant = p_seg = mid
        L = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
        if ponta:
            tam = float(el.get("tamanho_ponta", max(22, min(36, 0.09 * L + 14))))
            self.ponta_seta(p1, math.atan2(p1[1] - p_ant[1], p1[0] - p_ant[0]), tam, cor, larg)
            if el.get("duas_pontas"):
                self.ponta_seta(p0, math.atan2(p0[1] - p_seg[1], p0[0] - p_seg[0]), tam, cor, larg)
        caixa = (min(p0[0], p1[0]) - 20, min(p0[1], p1[1]) - 20, max(p0[0], p1[0]) + 20, max(p0[1], p1[1]) + 20)
        return self.registrar(el, "seta" if ponta else "linha", caixa, cor)

    def el_desenho(self, el, onde):
        nome = el.get("nome")
        if nome not in DES.DESENHOS:
            raise ErroRoteiro(f"{onde}: desenho {nome!r} não existe. Disponíveis:\n{DES.lista()}")
        d = DES.DESENHOS[nome]
        w = float(el.get("largura", 200))
        h = w * d["aspecto"]
        x, y = self.posicionar(el, w, h, onde)
        cor = rgb(el.get("cor"), "branco")
        larg = float(el.get("espessura", max(3.0, min(6.0, w / 45))))
        esc = max(0.3, min(1.0, w / 260))  # desenho pequeno treme menos

        def T(px, py):
            return (x + px * w, y + py * w)

        for prim in d["tracos"]:
            tipo = prim[0]
            if tipo in ("linha", "fechada", "grossa"):
                pts = [T(*p) for p in prim[1]]
                if tipo == "fechada":
                    a, b = pts[0], pts[1]
                    pts = pts + [pts[0], (a[0] + (b[0] - a[0]) * 0.12, a[1] + (b[1] - a[1]) * 0.12)]
                self.tracar(pts, cor, larg * (2 if tipo == "grossa" else 1), ondula=esc, tremor=0.8 * esc)
            elif tipo in ("elipse", "arco"):
                _, cx, cy, rx, ry = prim[:5]
                a0, a1 = (prim[5], prim[6]) if tipo == "arco" else (None, None)
                X, Y = T(cx, cy)
                pts = self.pts_elipse(X, Y, rx * w, ry * w, a0, a1)
                self.tracar(pts, cor, larg, ondula=min(esc, (rx + ry) * w / 150), serrilha=0.6 * esc, tremor=0.6 * esc)
            elif tipo == "ponto":
                (X, Y), r = T(prim[1], prim[2]), prim[3] * w
                self.draw.ellipse([(X - r) * SS, (Y - r) * SS, (X + r) * SS, (Y + r) * SS], fill=cor)
            elif tipo == "texto":
                txt, (X, Y), tam = prim[1], T(prim[2], prim[3]), prim[4] * w
                cap, _ = self.metricas(tam)
                cx = X - sum(self.avanco(c, tam) for c in txt) / 2
                for c in txt:
                    self.letra(c, cx, Y + cap / 2, tam, cor, self.rng.gauss(0, 0.03) * self.imp)
                    cx += self.avanco(c, tam)
        return self.registrar(el, "desenho", (x - larg, y - larg, x + w + larg, y + h + larg), cor)

    def el_livre(self, el, onde):
        cor = rgb(el.get("cor"), "branco")
        larg = float(el.get("espessura", 4.5))
        pts = [tuple(map(float, p)) for p in el.get("pontos", [])]
        if len(pts) < 2:
            raise ErroRoteiro(f"{onde}: 'livre' precisa de 'pontos' com pelo menos 2 pares [x, y]")
        if el.get("fechado"):
            pts = pts + [pts[0]]
        self.tracar(pts, cor, larg, ondula=1.0, tremor=0.8)
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        return self.registrar(el, "livre", (min(xs) - larg, min(ys) - larg, max(xs) + larg, max(ys) + larg), cor)

    # ------------------------------------------------------------------ montagem
    def desenhar(self, elementos):
        acoes = {
            "titulo": lambda e, o: self.el_texto(e, o, "titulo"),
            "subtitulo": lambda e, o: self.el_texto(e, o, "subtitulo"),
            "texto": lambda e, o: self.el_texto(e, o, "texto"),
            "fracao": self.el_fracao,
            "caixa": self.el_caixa,
            "circular": self.el_circular,
            "riscar": self.el_riscar,
            "sublinhar": self.el_sublinhar,
            "desenho": self.el_desenho,
            "livre": self.el_livre,
            "seta": self.el_seta,
            "linha": lambda e, o: self.el_seta(e, o, ponta=False),
        }
        # setas e linhas por último: assim apontam para as bordas já com caixa/risco
        ordem = [e for e in elementos if e.get("tipo") not in ("seta", "linha")] + \
                [e for e in elementos if e.get("tipo") in ("seta", "linha")]
        for n, el in enumerate(ordem, 1):
            tipo = el.get("tipo")
            onde = f"elemento {el.get('id') or n} ({tipo})"
            if tipo not in acoes:
                raise ErroRoteiro(f"{onde}: tipo desconhecido. Use: {', '.join(acoes)}")
            self.imp = float(el.get("imperfeicao", self.imp_base))
            self.peso = float(el.get("peso", self.peso_base))
            acoes[tipo](el, onde)
        self.imp, self.peso = self.imp_base, self.peso_base

    def finalizar(self):
        img = self.canvas
        if self.giz:  # falhas de giz: devolve o fundo em ~20% dos pontos do traço
            manter = self.ruido(img.size).point(lambda v: 0 if v < 51 else 255)
            img = Image.composite(img, self.bg, manter)
        return img.resize((self.W, self.H), Image.LANCZOS)

    def conferir(self):
        mx, my = 20, 14
        for i, r in self.reg.items():
            x0, y0, x1, y1 = r["bbox"]
            if x0 < mx or y0 < my or x1 > self.W - mx or y1 > self.H - my:
                self.avisos.append(f"{i!r} encosta/sai da borda: x {x0:.0f}–{x1:.0f}, y {y0:.0f}–{y1:.0f} "
                                   f"(tela {self.W}x{self.H})")
            if r["tipo"] in ("texto", "titulo", "subtitulo", "fracao") and r["tam"] < 28:
                self.avisos.append(f"{i!r} com tamanho {r['tam']:.0f}: abaixo do mínimo de 28 px do padrão")
            for nome, zx0, zy0, zx1, zy1 in self.areas:  # cantos do logo X8 e da webcam
                if min(x1, zx1) - max(x0, zx0) > 2 and min(y1, zy1) - max(y0, zy0) > 2:
                    self.avisos.append(f"{i!r} invade a área livre do {nome} (x {zx0}–{zx1}, y {zy0}–{zy1})")
        itens = [(i, r) for i, r in self.reg.items()
                 if r["tipo"] in ("texto", "titulo", "subtitulo", "desenho", "fracao")]
        for a in range(len(itens)):
            for b in range(a + 1, len(itens)):
                (ia, ra), (ib, rb) = itens[a], itens[b]
                A, B = ra["bbox"], rb["bbox"]
                ix = min(A[2], B[2]) - max(A[0], B[0])
                iy = min(A[3], B[3]) - max(A[1], B[1])
                if ix > 4 and iy > 4:
                    self.avisos.append(f"{ia!r} e {ib!r} se sobrepõem ({ix:.0f}x{iy:.0f} px)")


def grade(img, reg, areas=()):
    g = img.convert("RGB").copy()
    d = ImageDraw.Draw(g)
    W, H = g.size
    for nome, zx0, zy0, zx1, zy1 in areas:  # cantos reservados (logo, webcam)
        d.rectangle([zx0, zy0, zx1 - 1, zy1 - 1], outline=(255, 0, 200), width=3)
        d.text((zx0 + 6, zy0 + 6), f"livre: {nome}", fill=(255, 0, 200))
    for x in range(0, W, 100):
        d.line([(x, 0), (x, H)], fill=(70, 70, 70) if x % 500 else (120, 120, 120), width=1)
        d.text((x + 3, 3), str(x), fill=(160, 160, 160))
    for y in range(0, H, 100):
        d.line([(0, y), (W, y)], fill=(70, 70, 70) if y % 500 else (120, 120, 120), width=1)
        d.text((3, y + 3), str(y), fill=(160, 160, 160))
    for i, r in reg.items():
        x0, y0, x1, y1 = r["bbox"]
        d.rectangle([x0, y0, x1, y1], outline=(0, 200, 255), width=1)
        d.text((x0 + 2, y1 + 2), i, fill=(0, 200, 255))
    return g


def carregar(caminho):
    with open(caminho, encoding="utf-8") as f:
        spec = json.load(f)
    if isinstance(spec, list):
        return [dict(s) for s in spec]
    if "slides" in spec:
        padrao = {k: v for k, v in spec.items() if k not in ("slides", "padrao")}
        padrao.update(spec.get("padrao", {}))
        return [dict(padrao, **s) for s in spec["slides"]]
    return [spec]


def dizer(msg):
    """print que aguenta a saída cortada (ex.: "| head"): as lousas seguintes continuam sendo geradas."""
    try:
        print(msg, flush=True)
    except BrokenPipeError:
        sys.stdout = open(os.devnull, "w")


def montar_pptx(pngs, destino, W, H):
    try:
        from pptx import Presentation
        from pptx.util import Emu
    except ImportError:
        dizer("⚠ python-pptx não instalado (pip install python-pptx); .pptx não gerado")
        return False
    prs = Presentation()
    prs.slide_width = Emu(12192000)
    prs.slide_height = Emu(round(12192000 * H / W))
    for p in pngs:
        s = prs.slides.add_slide(prs.slide_layouts[6])
        s.shapes.add_picture(p, 0, 0, prs.slide_width, prs.slide_height)
    prs.save(destino)
    return True


def main(argv=None):
    ap = argparse.ArgumentParser(description="Gera lousas escritas à mão (PNG) a partir de um roteiro JSON.")
    ap.add_argument("roteiro", nargs="?", help="arquivo .json com a(s) lousa(s)")
    ap.add_argument("-o", "--saida", help="pasta de saída (ou arquivo .png, se o roteiro tiver 1 lousa)")
    ap.add_argument("--grade", action="store_true", help="grava também *_grade.png para conferir posições")
    ap.add_argument("--pptx", help="junta as imagens geradas neste .pptx (1 por slide)")
    ap.add_argument("--desenhos", action="store_true", help="lista os desenhos prontos e sai")
    a = ap.parse_args(argv)
    if a.desenhos:
        dizer("Desenhos prontos (tipo \"desenho\", campo \"nome\"):\n" + DES.lista())
        return 0
    if not a.roteiro:
        ap.error("informe o roteiro .json (ou use --desenhos)")
    pasta = os.path.dirname(os.path.abspath(a.roteiro))
    base = os.path.splitext(os.path.basename(a.roteiro))[0]
    try:
        slides = carregar(a.roteiro)
    except (OSError, json.JSONDecodeError) as e:
        dizer(f"✖ não consegui ler o roteiro: {e}")
        return 2
    gerados, falhas, dims = [], 0, (1920, 1080)
    dir_saida = a.saida or pasta
    if a.saida and a.saida.lower().endswith(".png") and len(slides) > 1:
        # -o lousa.png com várias lousas: vira lousa_01.png, lousa_02.png… na mesma pasta
        dir_saida = os.path.dirname(a.saida) or "."
        base = os.path.splitext(os.path.basename(a.saida))[0]
    for n, spec in enumerate(slides, 1):
        if a.saida and a.saida.lower().endswith(".png") and len(slides) == 1:
            destino = a.saida
        else:
            nome = spec.get("saida") or (f"{base}_{n:02d}.png" if len(slides) > 1 else f"{base}.png")
            destino = nome if os.path.isabs(nome) else os.path.join(dir_saida, nome)
        os.makedirs(os.path.dirname(os.path.abspath(destino)), exist_ok=True)
        avisos = []
        try:
            lousa = Lousa(spec, pasta, avisos)
            elementos = spec.get("elementos", [])
            if spec.get("molde"):  # molde = posições e tamanhos calculados sozinhos (scripts/moldes.py)
                elementos = MOLDES.expandir(lousa, spec) + elementos
            lousa.desenhar(elementos)
            lousa.conferir()
        except (ErroRoteiro, MOLDES.ErroMolde) as e:
            dizer(f"✖ lousa {n}: {e}")
            falhas += 1
            continue
        except (ValueError, TypeError, AttributeError) as e:  # ex.: "x": "abc" ou elemento que não é objeto
            dizer(f"✖ lousa {n}: valor inválido no roteiro ({e}). Números (x, y, tamanho, largura…) "
                  "devem ser números; cada elemento deve ser um objeto {...}")
            falhas += 1
            continue
        img = lousa.finalizar()
        img.save(destino, optimize=True)
        gerados.append(destino)
        dims = (lousa.W, lousa.H)
        dizer(f"✔ {destino} ({lousa.W}x{lousa.H})")
        for i, r in lousa.reg.items():
            x0, y0, x1, y1 = r["bbox"]
            dizer(f"   {i:<16} {r['tipo']:<10} x {x0:6.0f}–{x1:<6.0f} y {y0:6.0f}–{y1:<6.0f}")
        for av in avisos:
            dizer(f"   ⚠ {av}")
        if a.grade:
            gpath = os.path.splitext(destino)[0] + "_grade.png"
            grade(img, lousa.reg, lousa.areas).save(gpath)
            dizer(f"   grade: {gpath}")
    if a.pptx and gerados and montar_pptx(gerados, a.pptx, *dims):
        dizer(f"✔ {a.pptx} ({len(gerados)} slide(s))")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
