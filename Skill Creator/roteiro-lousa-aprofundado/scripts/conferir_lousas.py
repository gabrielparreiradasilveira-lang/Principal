# -*- coding: utf-8 -*-
"""
Confere as lousas de uma aula antes da entrega.

Uso: python3 conferir_lousas.py roteiro.md lousas.json [-o pasta_dos_png]

Desenha cada lousa do JSON (o mesmo motor do lousa.py) e aponta como pendência:
- aviso do gerador (texto cortado, canto do logo ou da webcam invadido, letra abaixo de 28 px...);
- ocupação abaixo de 70% da altura útil (lousa com metade da tela vazia);
- faixa horizontal vazia de mais de 120 px (buraco no meio da lousa);
- 8 palavras seguidas iguais à fala do mesmo vídeo e bloco (a lousa complementa a fala, não a repete);
- PNG cujo nome não segue {video}_{bloco}_{slug}.png (ex.: r60a_2_metafora.png, r50-1_4_resolucao.png).
Vídeo sem as 4 lousas sai como aviso. Sai com código 1 se houver pendência.
"""
import argparse
import os
import re
import sys

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from PIL import Image  # noqa: E402

import conferir_roteiro as CR  # noqa: E402
import lousa as LOUSA  # noqa: E402
import moldes as MOLDES  # noqa: E402

TOPO_UTIL, BASE_UTIL = 120, 1040
CANTOS = [(1560, 0, 1920, 190), (1600, 760, 1920, 1080)]  # logo X8 e webcam
OCUPACAO_MIN = 0.70
FAIXA_VAZIA_MAX = 120  # px: a amostra aprovada tem até 38; as lousas antigas rejeitadas, de 92 a 463
N_PALAVRAS = 8
NOME = re.compile(r"^(r\d{2,3}(?:-\d|[a-z]))_([1-4])_")
PALAVRA = re.compile(r"[0-9A-ZÀ-Þ]+")


def ocupacao(png):
    """Fração da altura útil (y 120 a 1040) até a última linha com tinta, sem contar os cantos livres."""
    img = Image.open(png).convert("L").point(lambda v: 255 if v > 40 else 0)
    for c in CANTOS:
        img.paste(0, c)
    caixa = img.crop((0, TOPO_UTIL, img.width, BASE_UTIL)).getbbox()
    if not caixa:
        return 0.0
    return caixa[3] / (BASE_UTIL - TOPO_UTIL)


def faixa_vazia(png):
    """Maior faixa horizontal sem tinta (em px) entre y 120 e 1040, sem contar os cantos livres."""
    img = Image.open(png).convert("L").point(lambda v: 255 if v > 40 else 0)
    for c in CANTOS:
        img.paste(0, c)
    faixa = img.crop((0, TOPO_UTIL, img.width, BASE_UTIL))
    maior = atual = 0
    for y in range(faixa.height):
        if faixa.crop((0, y, faixa.width, y + 1)).getbbox():  # qualquer pixel com tinta
            atual = 0
        else:
            atual += 1
            maior = max(maior, atual)
    return maior


def normalizar(texto):
    texto = re.sub(r"\{[a-zA-Z#0-9]+:", " ", texto).replace("}", " ")
    texto = re.sub(r"\[([^\]]+)\]", r" \1 ", texto).replace(" ", " ")
    return PALAVRA.findall(texto.upper())


def repeticoes(lousa, fala, n=N_PALAVRAS):
    """Trechos de n ou mais palavras seguidas que estão na lousa e na fala (sobrepostos viram um só)."""
    pl, pf = normalizar(lousa), normalizar(fala)
    da_fala = {tuple(pf[i:i + n]) for i in range(len(pf) - n + 1)}
    inicios = [i for i in range(len(pl) - n + 1) if tuple(pl[i:i + n]) in da_fala]
    achadas = []
    for i in inicios:
        if i - 1 in inicios:
            continue  # continuação do trecho anterior
        fim = i
        while fim + 1 in inicios:
            fim += 1
        trecho = " ".join(pl[i:fim + n])
        if trecho not in achadas:
            achadas.append(trecho)
    return achadas


def video_bloco(nome_png):
    m = NOME.match(os.path.basename(nome_png).lower())
    return (m.group(1), int(m.group(2))) if m else None


def desenhar(spec, pasta):
    """Desenha uma lousa; devolve (avisos, imagem, elementos expandidos)."""
    avisos = []
    L = LOUSA.Lousa(spec, pasta, avisos)
    elementos = spec.get("elementos", [])
    if spec.get("molde"):
        elementos = MOLDES.expandir(L, spec) + elementos
    L.desenhar(elementos)
    L.conferir()
    return avisos, L.finalizar(), elementos


def texto_da_lousa(elementos):
    partes = []
    for e in elementos:
        for k in ("texto", "antes", "num", "den", "depois"):
            if isinstance(e.get(k), str):
                partes.append(e[k])
    return "\n".join(partes)


def falas_do_roteiro(caminho):
    """{(video em minúsculas, bloco): texto da fala}."""
    linhas = open(caminho, encoding="utf-8").read().split("\n")
    out = {}
    for nome, ls in CR.dividir_videos(linhas):
        fala = CR.separar(ls)[0]
        for bloco, l in fala.items():
            out[(nome.lower(), bloco)] = "\n".join(l)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="Confere as lousas de uma aula antes da entrega.")
    ap.add_argument("roteiro")
    ap.add_argument("lousas")
    ap.add_argument("-o", "--saida", help="pasta dos PNG (padrão: a pasta do JSON)")
    a = ap.parse_args(argv)
    pasta = os.path.dirname(os.path.abspath(a.lousas))
    destino = a.saida or pasta
    os.makedirs(destino, exist_ok=True)
    falas = falas_do_roteiro(a.roteiro)
    pend, avis, blocos_por_video = [], [], {}
    print("=== Conferência das lousas ===\n")
    for n, spec in enumerate(LOUSA.carregar(a.lousas), 1):
        nome = spec.get("saida") or f"lousa_{n:02d}.png"
        vb = video_bloco(nome)
        try:
            av, img, els = desenhar(spec, pasta)
        except (LOUSA.ErroRoteiro, MOLDES.ErroMolde, ValueError, TypeError) as e:
            pend.append(f"{nome}: não foi desenhada ({e})")
            continue
        png = os.path.join(destino, nome)
        img.save(png, optimize=True)
        oc = ocupacao(png)
        print(f"{nome}: ocupação {oc:.0%}, {len(av)} aviso(s)")
        pend += [f"{nome}: {x}" for x in av]
        fv = faixa_vazia(png)
        if fv > FAIXA_VAZIA_MAX:
            pend.append(f"{nome}: faixa vazia de {fv} px (máximo {FAIXA_VAZIA_MAX}); distribua ou acrescente conteúdo")
        if oc < OCUPACAO_MIN:
            pend.append(f"{nome}: ocupa só {oc:.0%} da altura útil (mínimo {OCUPACAO_MIN:.0%}); acrescente conteúdo")
        if not vb:
            pend.append(f"{nome}: nome fora do padrão {{video}}_{{bloco}}_{{slug}}.png")
            continue
        blocos_por_video.setdefault(vb[0], set()).add(vb[1])
        fala = falas.get(vb)
        if fala is None:
            avis.append(f"{nome}: não achei a fala do vídeo {vb[0].upper()}, bloco {vb[1]}, no roteiro")
            continue
        for r in repeticoes(texto_da_lousa(els), fala):
            pend.append(f"{nome}: repete a fala (\"{r.lower()}\"); a lousa deve complementar, não copiar")
    for v, bs in sorted(blocos_por_video.items()):
        if bs != {1, 2, 3, 4}:
            avis.append(f"{v.upper()}: lousas dos blocos {sorted(bs)}; o esperado é uma por bloco (1 a 4)")
    print("\nPendências:" if pend else "\nPendências: nenhuma")
    for p in pend:
        print(f"  - {p}")
    if avis:
        print("Avisos:")
        for p in avis:
            print(f"  - {p}")
    return 1 if pend else 0


if __name__ == "__main__":
    sys.exit(main())
