"""Confere um roteiro de lousa antes da entrega.

Uso:
    python3 conferir_roteiro.py roteiro.md [--pd 4.9,4.9.1,4.9.2]

Lê o Markdown da resposta completa (diagnóstico, plano, vídeos, checklist) e
aponta o que precisa ser corrigido. Sai com código 1 se houver pendência.
Espera o formato do esqueleto do SKILL.md: título "# R60A · ..." ou "# R50-1 · ..." por vídeo,
blocos "## 1." a "## 4." e as marcações [Ação na Lousa] e [Locução Direta] em cada bloco.
O roteiro não leva Nota de bastidor (o professor não usa).
Também aponta qualquer menção à apostila: ela é fonte interna e não aparece no material.
"""
import argparse
import re
import sys

PALAVRAS_POR_MIN = 95
MIN_PAL, ALVO_PAL, MAX_PAL = 570, 665, 760

WORD = re.compile(r"[0-9A-Za-zÀ-ÿ]+(?:[.,'’-][0-9A-Za-zÀ-ÿ]+)*")
VIDEO = re.compile(r"^#{1,2}\s*\**\s*(R\d{2,3}(?:[A-Z]|-\d))\b")
BLOCO = re.compile(r"^#{2,4}\s*\**\s*(?:Bloco\s*)?([1-9])[.\s—-]")
BLOCOS_ESPERADOS = [1, 2, 3, 4]
TITULO_FORTE = re.compile(r"^#{1,3}\s")
NOTA_INICIO = re.compile(r"^\s*(?:#{1,6}\s*|\*\*\s*)\**\s*Nota de bastidor", re.IGNORECASE)
ITEM_PD = re.compile(r"\b(\d{1,2}(?:\.\d{1,2}){1,3})\b")
LATEX = re.compile(r"(?<![A-Za-z])\$|\\(beta|alpha|sigma|frac|sqrt|rho|text|mathbf|sum|rightarrow|overline|epsilon)")
NOTA_0_10 = re.compile(r"\b(10|[0-9])(,\d)?\s*/\s*10\b(?!/\d)|Nota Global", re.IGNORECASE)
FORMULA_PESADA = re.compile(r"√|\\sqrt|\\sum|∑|Σ(?!\+)|sqrt")
DATA = re.compile(
    r"\b(19[5-9]\d|20[0-4]\d)\b|\b\d{1,2}/\d{1,2}/\d{2,4}\b|"
    r"\b(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)[a-zç]*[./ ]+(de )?\d{4}\b",
    re.IGNORECASE)
ABSOLUTA = re.compile(
    r"\b(sempre|nunca|jamais|imposs[íi]vel|garant\w*|elimin\w*|zera\w*|sem risco|"
    r"n[ãa]o (?:tem|h[áa]) risco|sem custo|isent\w*|isenç\w*|apenas|somente|qualquer|nenhum\w*|"
    r"s[óo] (?:vale|existe|incide|serve|para|quando|se|é))\b",
    re.IGNORECASE)


def dividir_videos(linhas):
    videos, atual = [], None
    for linha in linhas:
        m = VIDEO.match(linha)
        if m:
            atual = [m.group(1), [linha]]
            videos.append(atual)
        elif atual is not None:
            atual[1].append(linha)
    return videos or [["único", linhas]]


def separar(linhas):
    """Devolve {bloco: [linhas de fala]}, linhas de lousa e o texto da Nota de bastidor ('' se não houver)."""
    fala, lousa, modo, bloco = {}, [], None, 0
    for i, linha in enumerate(linhas):
        if NOTA_INICIO.match(linha):
            return fala, lousa, "\n".join(linhas[i:]) or " "
        m = BLOCO.match(linha)
        if m:
            bloco, modo = int(m.group(1)), None
            continue
        if "Locução Direta" in linha:
            modo = "fala"
            resto = re.split(r"Locução Direta\]?\**", linha, maxsplit=1)[-1].strip(" ]*:`")
            if resto:
                fala.setdefault(bloco, []).append(resto)
            continue
        if "Ação na Lousa" in linha:
            modo = "lousa"
            continue
        if TITULO_FORTE.match(linha):
            modo = None
            continue
        if modo == "fala" and not linha.strip().startswith("|"):
            fala.setdefault(bloco, []).append(linha)
        elif modo == "lousa":
            lousa.append(linha)
    return fala, lousa, ""


def frases(texto):
    return [f.strip() for f in re.split(r"(?<=[.!?])\s+|\n+", texto) if f.strip()]


def main():
    ap = argparse.ArgumentParser(description="Confere um roteiro de lousa antes da entrega.")
    ap.add_argument("arquivo")
    ap.add_argument("--pd", default="", help="itens do PD na ordem oficial, separados por vírgula")
    a = ap.parse_args()

    texto = open(a.arquivo, encoding="utf-8").read()
    pendencias, avisos, absolutas = [], [], []
    fala_toda, lousa_toda, itens_vistos = [], [], []

    print("=== Conferência do roteiro ===\n")
    for nome, linhas in dividir_videos(texto.split("\n")):
        corpo = "\n".join(linhas)
        fala, lousa, nota = separar(linhas)
        por_bloco = {b: len(WORD.findall("\n".join(l))) for b, l in sorted(fala.items())}
        total = sum(por_bloco.values())
        fala_txt = "\n".join("\n".join(l) for l in fala.values())
        fala_toda.append(fala_txt)
        lousa_toda += lousa
        blocos = sorted({int(m.group(1)) for l in linhas if (m := BLOCO.match(l))})
        cab = ITEM_PD.findall("\n".join(linhas[:8]))
        if cab:
            itens_vistos.append(cab[0])

        situacao = "ok"
        if total < MIN_PAL:
            situacao = "ABAIXO DO MÍNIMO"
            pendencias.append(f"{nome}: {total} palavras, abaixo de {MIN_PAL} (raso, ou devia juntar com o item vizinho)")
        elif total > MAX_PAL:
            situacao = "ACIMA DO TETO"
            pendencias.append(f"{nome}: {total} palavras, acima de {MAX_PAL} (divida ou priorize)")
        elif total > ALVO_PAL + 55:
            situacao = "acima do alvo"
            avisos.append(f"{nome}: {total} palavras; o alvo é ~{ALVO_PAL} (7 min). Veja se não está enchendo")
        detalhe = " · ".join(f"{b}) {n}" for b, n in por_bloco.items())
        print(f"{nome}: {detalhe} = {total} palavras → ~{total / PALAVRAS_POR_MIN:.1f} min [{situacao}]")

        if blocos != BLOCOS_ESPERADOS:
            pendencias.append(f"{nome}: blocos encontrados {blocos}; o vídeo tem os blocos {BLOCOS_ESPERADOS}")
        if corpo.count("Ação na Lousa") < 4 or corpo.count("Locução Direta") < 4:
            pendencias.append(f"{nome}: faltam marcações [Ação na Lousa] ou [Locução Direta]")
        if nota:
            pendencias.append(f"{nome}: o roteiro não leva Nota de bastidor; tire a seção")
        if not DATA.search(fala_txt):
            if re.search(r"hipot[ée]tic", fala_txt, re.IGNORECASE):
                avisos.append(f"{nome}: sem data na fala; caso hipotético declarado (confira se não havia caso real)")
            else:
                pendencias.append(f"{nome}: sem data na fala e sem caso hipotético declarado")
        for f in frases(fala_txt):
            if ABSOLUTA.search(f):
                absolutas.append(f"{nome}: {f[:160]}")
        for f in lousa:
            if ABSOLUTA.search(f):
                absolutas.append(f"{nome} (lousa): {f.strip()[:160]}")

    fala_txt = "\n".join(fala_toda)
    if (latex := sorted({m.group(0) for m in LATEX.finditer(fala_txt)})):
        pendencias.append(f"LaTeX ou símbolo de fórmula na fala: {latex[:6]}")
    if (apostila := len(re.findall(r"apostila", texto, re.IGNORECASE))):
        pendencias.append(f"A apostila é citada {apostila} vez(es); o material nunca menciona a apostila "
                          "(nem na fala, nem na lousa, nem na Base)")
    if (nota := sorted({m.group(0) for m in NOTA_0_10.finditer(texto)})):
        pendencias.append(f"Autoavaliação de 0 a 10 encontrada: {nota[:4]}")
    if (formula := sorted({m.group(0) for m in FORMULA_PESADA.finditer(chr(10).join(lousa_toda))})):
        pendencias.append(f"Fórmula pesada na lousa (use a forma resumida): {formula}")
    negrito_tabela = sum(1 for l in texto.split("\n") if l.strip().startswith("|") and "**" in l)
    if negrito_tabela:
        pendencias.append(f"{negrito_tabela} linha(s) de tabela com negrito: o Drive mostra os asteriscos")
    if a.pd and itens_vistos:
        ordem = a.pd.split(",")
        idx = [ordem.index(i) for i in itens_vistos if i in ordem]
        if idx != sorted(idx) or len(idx) != len(itens_vistos):
            pendencias.append(f"Vídeos fora da ordem do PD: {itens_vistos} (ordem oficial: {ordem})")
    verificar = texto.count("[VERIFICAR]")

    print(f"\nItens [VERIFICAR] no texto: {verificar}")
    print(f"\nFrases absolutas para o teste do contraexemplo ({len(absolutas)}; a lista é um mínimo, revise também as outras):")
    for f in absolutas[:30]:
        print(f"  - {f}")
    if len(absolutas) > 30:
        print(f"  ... e mais {len(absolutas) - 30}")
    print("\nAvisos:" if avisos else "\nAvisos: nenhum")
    for x in avisos:
        print(f"  - {x}")
    print(f"\nPENDÊNCIAS ({len(pendencias)}):" if pendencias else "\nPENDÊNCIAS: nenhuma")
    for x in pendencias:
        print(f"  - {x}")
    sys.exit(1 if pendencias else 0)


if __name__ == "__main__":
    main()
