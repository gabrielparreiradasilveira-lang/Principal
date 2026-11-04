# -*- coding: utf-8 -*-
"""
Moldes de lousa: o roteiro diz O QUE vai na lousa e o molde calcula ONDE e em que tamanho.

Cada slide com "molde" vira a lista de elementos comum do lousa.py (titulo, texto, fracao, caixa...).
O tamanho da letra é o maior que cabe (de 40 até o mínimo de 28 px do padrão X8); se nem 28 couber,
sai um aviso pedindo para dividir a lousa. Elementos extras em "elementos" são desenhados por cima.

Moldes: mito_verdade, metafora, topicos, colunas, pegadinhas, hp12c (campos em references/formato.md).
"""
import desenhos as DES

TOPO, BASE = 24, 1040         # título começa em y 24; nada passa de y 1040
X0, X1 = 80, 1520             # faixa do texto: livre do logo (x >= 1560) e da webcam (x >= 1600)
TAMS = [40, 38, 36, 34, 32, 30, 28]


class ErroMolde(Exception):
    pass


def _medir(L, el, tipo="texto"):
    return L.el_texto(dict(el), "molde", tipo, medir=True)


def _maior_que_cabe(L, montar, cabe, tams=TAMS):
    """Primeiro tamanho (do maior para o menor) cujo bloco montado cabe; senão o menor, com aviso."""
    for t in tams:
        els = montar(t)
        if cabe(els, t):
            return t, els
    L.avisos.append("molde: o texto não coube nem no tamanho mínimo; condense ou divida a lousa")
    return tams[-1], montar(tams[-1])


def _titulo(L, spec, els):
    el = {"tipo": "titulo", "texto": spec.get("titulo", ""), "tamanho": spec.get("tamanho_titulo", 42),
          "largura": 1500}
    _, h = _medir(L, el, "titulo")
    els.append(el)
    return TOPO + h + el["tamanho"] * 0.45 + 40  # sublinhado + respiro


def _destaque(L, d, els, x=90, largura=1380):
    """Frase de destaque na base, com moldura; devolve o y onde ela começa (com a moldura)."""
    if not d:
        return BASE
    d = {"texto": d} if isinstance(d, str) else d
    el = {"tipo": "texto", "id": "destaque", "texto": d["texto"], "x": x, "largura": largura,
          "tamanho": d.get("tamanho", 40), "cor": d.get("cor", "verde"), "lista": False}
    _, h = _medir(L, el)
    el["y"] = BASE - 26 - h
    els += [el, {"tipo": "caixa", "alvo": "destaque", "margem": 26, "cor": d.get("moldura", "amarelo")}]
    return el["y"] - 26


def _aspecto(nome):
    if nome not in DES.DESENHOS:
        raise ErroMolde(f"desenho {nome!r} não existe. Disponíveis:\n{DES.lista()}")
    return DES.DESENHOS[nome]["aspecto"]


def _formula(L, f, d, wd, hd, y, els):
    """Fórmula (fração) em moldura amarela à esquerda e o desenho, se houver, à direita; devolve o novo y."""
    tf = f.get("tamanho", 64)
    while True:
        W, H = L.el_fracao(dict(f, tamanho=tf), "molde", medir=True)
        if W <= X1 - X0 - 80 - (wd + 60 if d else 0) or tf <= 40:
            break
        tf -= 4
    els += [dict(f, tipo="fracao", id="formula", x=X0 + 40, y=y + 34, tamanho=tf),
            {"tipo": "caixa", "alvo": "formula", "margem": 34}]
    if d:
        els.append({"tipo": "desenho", "nome": d["nome"], "cor": d.get("cor", "branco"), "largura": wd,
                    "x": X1 + 20 - wd, "y": y})
    return max(y + 34 + H + 34, y + hd) + 50


# ---------------------------------------------------------------- moldes
def mito_verdade(L, spec, els):
    y0 = _titulo(L, spec, els)
    if spec.get("caso"):  # linha "Caso:" das aberturas dos roteiros novos, logo abaixo do título
        c = {"tipo": "texto", "id": "caso", "texto": spec["caso"], "x": X0, "y": y0 + 10, "largura": X1 - X0,
             "tamanho": 32, "lista": False}
        els.append(c)
        y0 += 10 + _medir(L, c)[1]
    mitos, verdade = spec.get("mitos", []), spec.get("verdade", "")
    fim = BASE - 40
    gap = 170  # o X do riscar passa da letra: espaço para não encostar no mito de baixo

    def montar(t):
        return [{"tipo": "texto", "id": f"mito{i + 1}", "texto": m, "x": 90, "largura": 760, "tamanho": t,
                 "cor": "vermelho", "lista": False} for i, m in enumerate(mitos)]

    def cabe(es, t):
        return sum(_medir(L, e)[1] for e in es) + gap * (len(es) - 1) <= fim - y0 - 40

    t, ms = _maior_que_cabe(L, montar, cabe, [46, 44, 42, 40, 38, 36, 34, 32])
    hs = [_medir(L, e)[1] for e in ms]
    total = sum(hs) + gap * (len(hs) - 1)
    y = y0 + max(40, (fim - y0 - total) / 2)
    for e, h in zip(ms, hs):
        e["y"] = y
        y += h + gap
    meio = y0 + max(40, (fim - y0 - total) / 2) + total / 2
    v = {"tipo": "texto", "id": "verdade", "texto": verdade, "x": 1070, "largura": 460, "cor": "verde",
         "lista": False}
    for tv in (48, 46, 44, 42, 40, 38, 36):
        v["tamanho"] = tv
        hv = _medir(L, v)[1]
        if hv <= 380:
            break
    v["y"] = max(y0 + 40, meio - hv / 2 - (90 if spec.get("desenho") else 0))
    els += ms + [{"tipo": "riscar", "alvo": e["id"]} for e in ms]
    els += [v, {"tipo": "caixa", "alvo": "verdade"}]
    d = spec.get("desenho")
    if d:
        d = {"nome": d} if isinstance(d, str) else d
        w = d.get("largura", 220)
        yd = v["y"] + hv + 30 + 60
        if yd + w * _aspecto(d["nome"]) <= BASE:
            els.append({"tipo": "desenho", "nome": d["nome"], "cor": d.get("cor", "branco"), "largura": w,
                        "x": 1300 - w / 2, "y": yd})
    els += [{"tipo": "seta", "de": e["id"], "para": "verdade", "curva": 0.1 if i % 2 == 0 else -0.1}
            for i, e in enumerate(ms)]


def metafora(L, spec, els):
    _titulo(L, spec, els)
    itens = spec.get("itens", [])
    n = max(1, len(itens))
    yr = spec.get("y_estrada", 520)
    if spec.get("estrada", True):
        els += [{"tipo": "livre", "pontos": [[70, yr], [700, yr - 4], [1540, yr + 2]], "espessura": 5},
                {"tipo": "livre", "pontos": [[70, yr + 90], [800, yr + 94], [1540, yr + 86]], "espessura": 5}]
        els += [{"tipo": "livre", "pontos": [[x, yr + 45], [x + 80, yr + 44]], "espessura": 4}
                for x in range(120, 1500, 190)]
    colw = (X1 + 40 - X0) / n
    for i, it in enumerate(itens):
        cx = X0 + colw * (i + 0.5)
        w = min(colw * 0.78, 400) * (0.78 if it.get("extra") else 1)
        asp = _aspecto(it["desenho"])
        if w * asp > yr - 200:
            w = (yr - 200) / asp
        we = w * 0.45 if it.get("extra") else 0
        x = cx - (w + (20 + we if we else 0)) / 2
        y = yr - 6 - w * asp
        els.append({"tipo": "desenho", "nome": it["desenho"], "cor": it.get("cor", "branco"), "largura": w,
                    "x": x, "y": y})
        if we:
            els.append({"tipo": "desenho", "nome": it["extra"], "cor": it.get("cor_extra", "vermelho"),
                        "largura": we, "x": x + w + 20, "y": max(y - 30, 200)})

    def montar(t):
        return [{"tipo": "texto", "id": f"leg{i + 1}", "x": X0 + colw * i + 10, "y": yr + 150,
                 "largura": colw - 24, "tamanho": t,
                 "texto": f"{i + 1}. {{laranja:{it['nome']}}} → {it['legenda']}"} for i, it in enumerate(itens)]

    def cabe(es, t):
        ms = [_medir(L, e) for e in es]
        return all(w <= e["largura"] + 1 for (w, _), e in zip(ms, es)) and max(h for _, h in ms) <= BASE - yr - 150

    _, legs = _maior_que_cabe(L, montar, cabe, [38, 36, 34, 32, 30, 28])
    els += legs


def topicos(L, spec, els):
    y = _titulo(L, spec, els)
    d = spec.get("desenho")
    d = {"nome": d} if isinstance(d, str) else d
    wd = d.get("largura", 240) if d else 0
    hd = wd * _aspecto(d["nome"]) if d else 0
    larg = X1 - X0
    if spec.get("formula"):
        y = _formula(L, spec["formula"], d, wd, hd, y, els)
        d = None  # já desenhado ao lado da fórmula
    if spec.get("subtitulo"):
        sub = {"tipo": "subtitulo", "texto": spec["subtitulo"], "x": X0, "y": y, "tamanho": 38}
        els.append(sub)
        y += _medir(L, sub, "subtitulo")[1] + 34
    fim = _destaque(L, spec.get("destaque"), els) - 40
    if spec.get("largura_texto"):  # deixa espaço à direita para elementos extras
        larg = min(larg, float(spec["largura_texto"]))
    if d:  # desenho à direita do texto
        larg -= wd + 60
        els.append({"tipo": "desenho", "nome": d["nome"], "cor": d.get("cor", "branco"), "largura": wd,
                    "x": X1 + 20 - wd, "y": y})
    if spec.get("texto"):
        def montar(t):
            return [{"tipo": "texto", "id": "corpo", "texto": spec["texto"], "x": X0, "y": y, "largura": larg,
                     "tamanho": t, "entrelinha": 1.45}]

        _, corpo = _maior_que_cabe(L, montar, lambda es, t: _medir(L, es[0])[1] <= fim - y,
                                   [spec.get("tamanho_max", 40)] + [t for t in TAMS if t < spec.get("tamanho_max", 40)])
        corpo[0]["y"] = y + max(0.0, fim - y - _medir(L, corpo[0])[1]) * 0.3  # sobra de espaço: desce um pouco
        els += corpo


def colunas(L, spec, els):
    y = _titulo(L, spec, els)
    if spec.get("formula"):
        d = spec.get("desenho")
        d = {"nome": d} if isinstance(d, str) else d
        wd = d.get("largura", 240) if d else 0
        y = _formula(L, spec["formula"], d, wd, wd * _aspecto(d["nome"]) if d else 0, y, els) - 20
    if spec.get("topo"):
        topo = {"tipo": "texto", "id": "topo", "texto": spec["topo"], "x": X0, "y": y, "largura": X1 - X0,
                "tamanho": spec.get("tamanho_topo", 36), "entrelinha": 1.45}
        els.append(topo)
        y += _medir(L, topo)[1] + 50
    cols = spec.get("colunas", [])[:3]
    pos = [(X0, 780), (980, 600)] if len(cols) < 3 else [(X0, 450), (600, 450), (1120, 440)]
    hts = []
    for (x, w), c in zip(pos, cols):
        ct = {"tipo": "subtitulo", "id": f"ct{len(hts) + 1}", "texto": c["titulo"], "x": x, "y": y,
              "largura": w, "tamanho": 40}
        els += [ct, {"tipo": "sublinhar", "alvo": ct["id"]}]
        hts.append(_medir(L, ct, "subtitulo")[1])
    yc = y + max(hts or [0]) + 50
    fim = _destaque(L, spec.get("destaque"), els) - 40

    def montar(t):
        return [{"tipo": "texto", "id": f"col{i + 1}", "texto": c["texto"], "x": x, "y": yc, "largura": w,
                 "tamanho": t, "entrelinha": 1.42} for i, ((x, w), c) in enumerate(zip(pos, cols))]

    _, cs = _maior_que_cabe(L, montar, lambda es, t: max(_medir(L, e)[1] for e in es) <= fim - yc,
                            [44, 42, 40, 38, 36, 34, 32, 30, 28][4 if len(cols) == 3 else 0:])
    hmax = max(_medir(L, e)[1] for e in cs)
    desce = max(0.0, fim - yc - hmax) * 0.3  # sobra de espaço: desce colunas e títulos juntos
    for e in els:
        if str(e.get("id", "")).startswith("ct") and e.get("tipo") == "subtitulo":
            e["y"] += desce
    for e in cs:
        e["y"] += desce
    y, yc = y + desce, yc + desce
    els += cs
    for (xa, wa), (xb, _) in zip(pos, pos[1:len(cols)]):  # linha à mão entre as colunas
        xd = (xa + wa + xb) / 2
        els.append({"tipo": "linha", "pontos": [[xd, y - 10], [xd - 5, (y + yc + hmax) / 2], [xd + 2, yc + hmax]],
                    "espessura": 4})


def pegadinhas(L, spec, els):
    y = _titulo(L, spec, els)
    linhas = []
    for i, it in enumerate(spec.get("itens", []), 1):
        it = {"frase": it} if isinstance(it, str) else it
        ver = it.get("veredito", "FALSO")
        cor = "verde" if ver.upper().startswith("VERDADE") else "vermelho"
        cor_txt = it.get("cor_correcao", "verde")
        corr = f" {{{cor_txt}:({it['correcao']})}}" if it.get("correcao") else ""
        linhas.append(f"{i}. \"{it['frase']}\" → {{{cor}:{ver}}}{corr}")

    def montar(t):
        return [{"tipo": "texto", "id": "pegas", "texto": "\n\n".join(linhas), "x": X0, "y": y + 10,
                 "largura": 1430, "tamanho": t, "entrelinha": 1.42}]

    _, corpo = _maior_que_cabe(L, montar, lambda es, t: _medir(L, es[0])[1] <= BASE - 30 - y - 10,
                               [38, 36, 34, 32, 30, 28])
    els += corpo + [{"tipo": "caixa", "alvo": "pegas", "margem": 26, "cor": spec.get("moldura", "vermelho")}]


def hp12c(L, spec, els):
    y = _titulo(L, spec, els)
    partes = []
    for i, p in enumerate(spec.get("passos", []), spec.get("primeiro", 1)):
        bloco = f"{i}. {{ciano:{p['nome']}}}\n  - {p['teclas']} → VISOR {{laranja:{p['visor']}}}"
        if p.get("leitura"):
            bloco += f"\n  - {p['leitura']}"
        partes.append(bloco)

    def montar(t):
        return [{"tipo": "texto", "id": "hp", "texto": "\n\n".join(partes), "x": X0, "y": y, "largura": X1 - X0,
                 "tamanho": t, "entrelinha": 1.55}]

    _, corpo = _maior_que_cabe(L, montar, lambda es, t: _medir(L, es[0])[1] <= BASE - y, [36, 34, 32, 30, 28])
    els += corpo


MOLDES = {"mito_verdade": mito_verdade, "metafora": metafora, "topicos": topicos, "colunas": colunas,
          "pegadinhas": pegadinhas, "hp12c": hp12c}


def expandir(L, spec):
    nome = spec["molde"]
    if nome not in MOLDES:
        raise ErroMolde(f"molde {nome!r} não existe. Use: {', '.join(MOLDES)}")
    els = []
    MOLDES[nome](L, spec, els)
    return els
