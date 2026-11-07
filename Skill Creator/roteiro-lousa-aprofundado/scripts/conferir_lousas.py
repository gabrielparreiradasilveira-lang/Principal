# -*- coding: utf-8 -*-
"""
Confere as lousas de uma aula antes da entrega.

Uso: python3 conferir_lousas.py roteiro.md lousas.json [-o pasta_dos_png]

Desenha cada lousa do JSON (o mesmo motor do lousa.py) e aponta como pendência:
- aviso do gerador (texto cortado, canto do logo ou da webcam invadido, letra abaixo de 28 px...);
- ocupação abaixo de 70% da altura útil (lousa com metade da tela vazia);
- faixa horizontal vazia de mais de 120 px (buraco no meio ou pé vazio);
- 8 palavras seguidas iguais à fala do mesmo vídeo e bloco (a lousa complementa a fala, não a repete);
- menção à apostila (ela é fonte interna e não aparece no material);
- PNG cujo nome não segue {video}_{bloco}_{slug}.png (ex.: r60a_2_metafora.png, r50-1_4_resolucao.png);
- verde ou vermelho sem ✓/✗ ou palavra-rótulo na mesma linha (a cor nunca carrega o sentido sozinha);
- tópico com mais de 12 palavras;
- lousa sem referência, ou referência sem a descrição simples antes do identificador entre parênteses;
- primeira lousa da aula sem a legenda das cores; Bloco 4 sem a pergunta de recuperação; último vídeo
  sem a síntese da aula; exercício sem premissas ou com conclusão que não diz qual regra gerou a diferença.
Vídeo sem as 4 lousas, referencia false e frase absoluta na lousa saem como aviso.
Sai com código 1 se houver pendência.
"""
import argparse
import os
import re
import sys
import unicodedata

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
PALAVRA = re.compile(r"[0-9A-ZÀ-Þ]+")
N_TOPICO = 12  # palavras por tópico: uma ideia, palavra-chave na frente
TOPICO = re.compile(r"^\s*(?:[-•]|\d{1,2}\.)\s+")
MARCA_COR = re.compile(r"\{(vermelho|verde):([^{}]*)\}")
SIMBOLOS = {"vermelho": "✗✘❌❎✖⚠↓", "verde": "✓✔✅☑↑"}
ROTULOS = {"vermelho": {"ERRADO", "ERRADA", "ERRADOS", "ERRADAS", "ERRO", "FALSO", "FALSA", "MITO", "ALERTA",
                        "CUIDADO", "ATENCAO"},
           "verde": {"CERTO", "CERTA", "CORRETO", "CORRETA", "VERDADE", "VERDADEIRO", "VERDADEIRA", "REGRA"}}
REFERENCIA = re.compile(r"^([^()]+)\(([^()]*\w[^()]*)\)\s*$")
NUMERO_COM_SINAL = re.compile(r"^[+−-]\s?\d")
MECANISMO = re.compile(r"→|\bporque\b|\bpois\b", re.IGNORECASE)


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
    """Palavras em maiúsculas, sem acento, sem marcações {cor:} e com [TECLA] virando TECLA."""
    texto = re.sub(r"\{[a-zA-Z#0-9]+:", " ", texto).replace("}", " ")
    texto = re.sub(r"\[([^\]]+)\]", r" \1 ", texto).replace("\u00a0", " ")
    texto = unicodedata.normalize("NFKD", texto.upper())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return PALAVRA.findall(texto)


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
    return MOLDES.video_bloco(nome_png)


def cor_sem_rotulo(texto):
    """[(cor, linha)] das linhas com {verde:} ou {vermelho:} sem ✓/✗ (ou ⚠, ↑, ↓) nem palavra-rótulo.
    Número com sinal (+15,90%, −29,90%) já diz o sentido sem a cor."""
    out = []
    for linha in texto.split("\n"):
        palavras = set(normalizar(linha))
        for cor in ("vermelho", "verde"):
            trechos = [t.strip() for c, t in MARCA_COR.findall(linha) if c == cor]
            sem_sinal = [t for t in trechos if not NUMERO_COM_SINAL.match(t)]
            if sem_sinal and not (any(x in linha for x in SIMBOLOS[cor]) or palavras & ROTULOS[cor]):
                out.append((cor, linha.strip()))
    return out


def topicos_longos(texto, n=N_TOPICO):
    """[(palavras, linha)] dos tópicos ("- ", "• ", "1. ", com ou sem recuo) com mais de n palavras (números não contam)."""
    out = []
    for linha in texto.split("\n"):
        m = TOPICO.match(linha)
        if not m:
            continue
        corpo = re.sub(r"\{[a-zA-Z#0-9]+:", " ", linha[m.end():]).replace("}", " ").replace("\u00a0", " ")
        corpo = re.sub(r"\[([^\]]+)\]", r" \1 ", corpo)
        k = sum(1 for t in corpo.split() if t != "R$" and any(c.isalpha() for c in t))  # número e R$ não contam
        if k > n:
            out.append((k, linha.strip()))
    return out


def referencia_ok(r):
    """Descrição que qualquer aluno entende (2 palavras ou mais) e o identificador entre parênteses:
    "LEI DO IR DA PREVIDÊNCIA (LEI 11.053/2004)"."""
    m = REFERENCIA.match(str(r).strip())
    if not m:
        return False
    palavras = [re.sub(r"[^\w]|\d|_", "", t) for t in m.group(1).split()]
    palavras = [t for t in palavras if t]
    return len(palavras) >= 2 and any(len(t) >= 5 for t in palavras)  # sigla solta ("IN RFB") não basta


def texto_corpo(elementos):
    """Só os blocos de texto (sem título e subtítulo): onde moram os tópicos."""
    return texto_da_lousa([e for e in elementos if e.get("tipo") == "texto"])


def linhas_de_cor(spec):
    """Trechos que o molde pinta inteiros de verde ou vermelho (destaque, conclusão e resultado com cor
    própria), escritos como {cor:texto} para a mesma checagem do texto. O resultado sem cor própria é a
    resposta certa da conta, em verde, e não precisa de rótulo."""
    def limpo(t):
        return re.sub(r"\{[a-zA-Z#0-9]+:([^{}]*)\}", r"\1", str(t))
    out = []
    for chave in ("destaque", "conclusao"):
        d = spec.get(chave)
        if not d:
            continue
        texto, cor = (d, "verde") if isinstance(d, str) else (d.get("texto", ""), d.get("cor", "verde"))
        if cor in ("verde", "vermelho"):
            out.append(f"{{{cor}:{limpo(texto)}}}")
    for c in spec.get("cenarios") or []:
        if isinstance(c, dict) and c.get("cor") in ("verde", "vermelho"):
            out.append(f"{{{c['cor']}:{limpo(c.get('resultado', ''))}}}")
    return out


def absolutas(texto):
    """Linhas da lousa com frase absoluta, para o teste do contraexemplo."""
    return [l.strip() for l in texto.split("\n") if CR.ABSOLUTA.search(l)]


def regras_da_aula(specs):
    """Regras que dependem da posição da lousa na aula; devolve (pendências, avisos)."""
    pend, avis = [], []
    nomes = [s.get("saida") or f"lousa_{n:02d}.png" for n, s in enumerate(specs, 1)]
    vbs = [video_bloco(nm) for nm in nomes]
    videos = [vb[0] for vb in vbs if vb]
    if specs and not specs[0].get("legenda"):
        pend.append(f"{nomes[0]}: a primeira lousa da aula leva a legenda das cores (\"legenda\": true)")
    bloco4, com_pergunta, com_sintese = {}, set(), set()
    for spec, nome, vb in zip(specs, nomes, vbs):
        r = spec.get("referencia")
        if r is False:
            avis.append(f"{nome}: sem referência (referencia false); confirme que a lousa não traz norma, "
                        "dado nem conceito técnico")
        elif not r or not isinstance(r, (str, list, tuple)):
            pend.append(f"{nome}: sem referência; escreva \"referencia\": \"DESCRIÇÃO SIMPLES (IDENTIFICADOR)\"")
        else:
            for x in MOLDES.referencias(spec):
                if not referencia_ok(x):
                    pend.append(f"{nome}: referência \"{x}\" fora do formato \"DESCRIÇÃO SIMPLES (IDENTIFICADOR)\", "
                                "que qualquer aluno entende (ex.: LEI DO IR DA PREVIDÊNCIA (LEI 11.053/2004))")
        for cor, linha in (x for t in linhas_de_cor(spec) for x in cor_sem_rotulo(t)):
            pend.append(f"{nome}: cor sem rótulo ({cor} em \"{linha[:90]}\"); junte ✓ ou ✗ (⚠ no alerta) "
                        "ou uma palavra-rótulo (CERTO, REGRA, ERRADO, ALERTA), ou use \"cor\": \"branco\"")
        if vb and vb[1] == 4:
            bloco4.setdefault(vb[0], []).append(nome)
            p = str(spec.get("pergunta") or "").strip()
            if p.endswith("?"):
                com_pergunta.add(vb[0])
            elif p:
                pend.append(f"{nome}: a pergunta de recuperação termina com \"?\"")
            if str(spec.get("sintese") or "").strip():
                com_sintese.add(vb[0])
        if spec.get("molde") == "exercicio":
            if not str(spec.get("premissas") or "").strip():
                pend.append(f"{nome}: exercício sem premissas (hipotético ou real, bruto ou líquido, o que ficou de fora)")
            c = spec.get("conclusao")
            c = c.get("texto", "") if isinstance(c, dict) else str(c or "")
            if not MECANISMO.search(c):
                pend.append(f"{nome}: a conclusão não diz qual regra produziu a diferença; escreva regra → efeito "
                            "(ou use \"porque\")")
    for v, ns in bloco4.items():
        if v not in com_pergunta:
            pend.append(f"{ns[-1]}: o Bloco 4 do {v.upper()} fecha com a pergunta de recuperação (\"pergunta\": \"...?\")")
    final = videos[-1] if videos else None
    if final in bloco4 and final not in com_sintese:
        pend.append(f"{bloco4[final][-1]}: o último vídeo da aula ({final.upper()}) fecha com a síntese da aula "
                    "(\"sintese\")")
    return pend, avis


def desenhar(spec, pasta):
    """Desenha uma lousa; devolve (avisos, imagem, elementos expandidos)."""
    avisos = []
    L = LOUSA.Lousa(spec, pasta, avisos)
    elementos = MOLDES.montar(L, spec)
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
    specs = LOUSA.carregar(a.lousas)
    print("=== Conferência das lousas ===\n")
    for n, spec in enumerate(specs, 1):
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
        texto = texto_da_lousa(els)
        if "APOSTILA" in normalizar(texto):
            pend.append(f"{nome}: cita a apostila; a lousa nunca menciona a apostila")
        for cor, linha in cor_sem_rotulo(texto):
            pend.append(f"{nome}: cor sem rótulo ({cor} em \"{linha[:90]}\"); junte ✓ ou ✗ (⚠ no alerta) "
                        "ou uma palavra-rótulo (CERTO, REGRA, ERRADO, ALERTA)")
        for k, linha in topicos_longos(texto_corpo(els)):
            pend.append(f"{nome}: tópico com {k} palavras (máximo {N_TOPICO}): \"{linha[:90]}\"; "
                        "uma ideia por tópico, palavra-chave na frente")
        for linha in absolutas(texto_da_lousa([e for e in els if e.get("id") != "referencia"])):  # fonte não é afirmação
            avis.append(f"{nome}: frase absoluta na lousa, faça o teste do contraexemplo: \"{linha[:90]}\"")
        if not vb:
            pend.append(f"{nome}: nome fora do padrão {{video}}_{{bloco}}_{{slug}}.png")
            continue
        blocos_por_video.setdefault(vb[0], set()).add(vb[1])
        fala = falas.get(vb)
        if fala is None:
            pend.append(f"{nome}: não achei a fala do vídeo {vb[0].upper()}, bloco {vb[1]}, no roteiro "
                        "(confira o roteiro passado e o cabeçalho do vídeo); sem ela, a repetição não é conferida")
            continue
        for r in repeticoes(texto_da_lousa(els), fala):
            pend.append(f"{nome}: repete a fala (\"{r.lower()}\"); a lousa deve complementar, não copiar")
    p2, a2 = regras_da_aula(specs)
    pend, avis = pend + p2, avis + a2
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
