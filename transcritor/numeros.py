"""
Padronização de números no estilo de prova (bancas ANBIMA/FGV).

O Whisper escreve a mesma quantidade de jeitos diferentes dentro de uma aula
("250 mil reais", "R$ 250 mil", "duzentos e cinquenta mil reais"). A função
padronizar() reescreve um parágrafo/legenda num padrão único, mexendo SÓ em
contextos numéricos sem ambiguidade:

  250 mil reais            -> R$ 250 mil
  dez por cento            -> 10%
  dois pontos percentuais  -> 2 p.p.
  13.75%                   -> 13,75%
  D mais dois              -> D+2

Número por extenso só é convertido quando vem logo antes de "reais",
"por cento", "ponto(s) percentual(is)", "centavos" ou logo depois de "D mais".
O resto do texto ("dois anos", "juros reais", "NTN-B 2035") fica intocado.
A função é idempotente: padronizar(padronizar(x)) == padronizar(x).
"""

from __future__ import annotations

import re
from typing import NamedTuple

# ----------------------------------------------------------------------------
# Vocabulário dos números por extenso
# ----------------------------------------------------------------------------

_UNIDADES = {
    "zero": 0, "um": 1, "uma": 1, "dois": 2, "duas": 2, "três": 3, "tres": 3,
    "quatro": 4, "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9,
    "dez": 10, "onze": 11, "doze": 12, "treze": 13, "catorze": 14,
    "quatorze": 14, "quinze": 15, "dezesseis": 16, "dezessete": 17,
    "dezoito": 18, "dezenove": 19,
}
_DEZENAS = {
    "vinte": 20, "trinta": 30, "quarenta": 40, "cinquenta": 50,
    "sessenta": 60, "setenta": 70, "oitenta": 80, "noventa": 90,
}
_CENTENAS = {"cem": 100, "cento": 100}
for _nome, _valor in [("duzent", 200), ("trezent", 300), ("quatrocent", 400),
                      ("quinhent", 500), ("seiscent", 600), ("setecent", 700),
                      ("oitocent", 800), ("novecent", 900)]:
    _CENTENAS[_nome + "os"] = _CENTENAS[_nome + "as"] = _valor
# Grandezas (o Whisper às vezes tira o acento: aceitamos as duas grafias)
_GRANDEZAS = {
    "mil": 10**3,
    "milhão": 10**6, "milhao": 10**6, "milhões": 10**6, "milhoes": 10**6,
    "bilhão": 10**9, "bilhao": 10**9, "bilhões": 10**9, "bilhoes": 10**9,
}
_PALAVRAS = {**_UNIDADES, **_DEZENAS, **_CENTENAS}


def _alternativa(palavras) -> str:
    """Alternância de regex com as palavras mais longas primeiro."""
    return "|".join(sorted(map(re.escape, palavras), key=len, reverse=True))


# ----------------------------------------------------------------------------
# Peças de regex
# ----------------------------------------------------------------------------

# Número em algarismos: 250 | 1.000 | 10.000.000 | 13,75 | 1.500,00
# (não pode estar colado em letra, nem ser pedaço de outro número)
_DIGITOS = (r"(?<![\w.,])(?:[0-9]{1,3}(?:\.[0-9]{3})+|[0-9]+)(?:,[0-9]+)?"
            r"(?!\w|[.,][0-9])")
_PALAVRA = rf"\b(?:{_alternativa(_PALAVRAS.keys() | _GRANDEZAS.keys())})\b"
_ATOMO = rf"(?:{_DIGITOS}|{_PALAVRA})"
# Sequência de átomos ligados por espaço ou " e ": "duzentos e cinquenta mil",
# "2 mil e 500". Não começa logo depois de "por " (o "cento" de "por cento").
_INTEIRO = rf"(?<!por\s){_ATOMO}(?:\s+(?:e\s+)?{_ATOMO})*"
# Parte depois da "vírgula" falada: algarismos ou palavras, sem grandezas
_ATOMO_DEC = rf"(?:[0-9]+|\b(?:{_alternativa(_PALAVRAS)})\b)"
_DECIMAL = rf"{_ATOMO_DEC}(?:\s+(?:e\s+)?{_ATOMO_DEC})*"
_VIRGULA = r"\s+v[ií]rgula\s+"
_GRANDEZA = rf"\b(?:{_alternativa(_GRANDEZAS)})\b"
# Número sem grandeza solta no fim (porcentagem, p.p.)
_NUMERO = rf"(?P<int>{_INTEIRO})(?:{_VIRGULA}(?P<dec>{_DECIMAL}))?"

_FLAGS = re.IGNORECASE

# 13.75 -> 13,75 (ponto seguido de 1 ou 2 dígitos é decimal; de 3 é milhar)
_RE_PONTO_DECIMAL = re.compile(r"(?<![\w.,])([0-9]+)\.([0-9]{1,2})(?![0-9]|[.,][0-9])")

# Número de seção/horário não é decimal: "item 3.2", "módulo 4.9", "às 10.30", "10.30h"
_PALAVRAS_SECAO = ("item", "itens", "módulo", "capítulo", "cap.", "seção", "questão",
                   "questões", "tabela", "quadro", "figura", "anexo", "artigo", "art.",
                   "parágrafo", "inciso", "versão", "aula", "slide", "às", "as")
_RE_ANTES_SECAO = re.compile(
    rf"(?<!\w)(?:{'|'.join(re.escape(p) for p in _PALAVRAS_SECAO)})\s*(?:n[º°o]\.?\s*|n\.\s*)?$",
    re.IGNORECASE)
_RE_DEPOIS_HORA = re.compile(r"\s*(?:horas?|h)(?!\w)", re.IGNORECASE)


def _troca_ponto_decimal(m: re.Match) -> str:
    if (_RE_ANTES_SECAO.search(m.string, 0, m.start())
            or _RE_DEPOIS_HORA.match(m.string, m.end())):
        return m.group(0)
    return f"{m.group(1)},{m.group(2)}"

# 10 por cento | 10 % | dez por cento | meio por cento | um e meio por cento
_RE_PERCENTUAL = re.compile(
    rf"(?:(?P<meio>\bmeio)|{_NUMERO}(?P<emeio>\s+e\s+meio)?)"
    r"\s*(?:por\s+cento\b|%)", _FLAGS)

# 2 pontos percentuais | 0,5 ponto percentual  (o ponto final da frase é
# absorvido pela abreviação: "2 pontos percentuais." -> "2 p.p.")
_RE_PONTOS_PERCENTUAIS = re.compile(
    rf"{_NUMERO}\s+pontos?\s+percentua(?:is|l)\b(?:\.(?!\.))?", _FLAGS)

# [R$] 250 mil [de] reais [e 50 centavos]
_RE_MOEDA = re.compile(
    rf"(?P<rs>\bR\s*\$\s*)?(?P<int>{_INTEIRO})"
    rf"(?:{_VIRGULA}(?P<dec>{_DECIMAL})(?:\s+(?P<mag>{_GRANDEZA}))?)?"
    rf"(?P<de>\s+de)?\s+reais\b"
    rf"(?P<cauda>\s+e\s+(?P<cent>{_INTEIRO})\s+centavos\b)?", _FLAGS)

# R$250 | R $ 250 | R$  250 -> R$ 250
_RE_CIFRAO = re.compile(r"\bR\s*\$\s*(?=[0-9])")

# cinquenta centavos -> 50 centavos
_RE_CENTAVOS = re.compile(rf"(?P<int>{_INTEIRO})\s+centavos\b", _FLAGS)

# D mais 2 | D + 2 | d mais dois | D zero -> D+N  ("dê mais dois" não casa)
_RE_LIQUIDACAO = re.compile(
    rf"(?<!\w)D(?:(?:\s*\+\s*|\s+mais\s+)(?P<num>{_INTEIRO})|\s+(?P<zero>zero)\b)",
    _FLAGS)

_RE_SO_DIGITOS = re.compile(r"[0-9]{1,3}(?:\.[0-9]{3})+|[0-9]+")


# ----------------------------------------------------------------------------
# Leitura dos números
# ----------------------------------------------------------------------------

class _Numero(NamedTuple):
    valor: int | None = None      # número calculado (havia palavras)
    escrito: str | None = None    # algarismos mantidos como estavam
    grandeza: str | None = None   # "mil"/"milhão"... mantida depois dos algarismos


def _eh_digito(token: str) -> bool:
    return re.fullmatch(r"[0-9.,]+", token) is not None


def _componente(token: str) -> tuple[int | None, int]:
    """Valor de um pedaço do grupo (< 1000) e o limite do próximo pedaço.

    O próximo pedaço precisa ser menor que o limite: "cento" (100) aceita
    "e vinte"; "vinte" (10) aceita "e cinco"; "cinco" (1) não aceita mais nada.
    É isso que impede "cinco e dez" de virar 15.
    """
    t = token.lower()
    if _RE_SO_DIGITOS.fullmatch(t):
        return int(t.replace(".", "")), 1
    if t in _CENTENAS:
        return _CENTENAS[t], (1 if t == "cem" else 100)
    if t in _DEZENAS:
        return _DEZENAS[t], 10
    if t in _UNIDADES:
        return _UNIDADES[t], 1
    return None, 0


def _valor_inteiro(tokens: list[str]) -> int | None:
    """Converte tokens ("dois", "mil", "e", "500"...) em inteiro, ou None se a
    sequência não for um número bem formado."""
    total = 0
    grupo = None          # valor do grupo corrente (abaixo de mil)
    limite = 0            # o próximo pedaço do grupo tem que ser menor que isto
    cento_aberto = False  # "cento" exige continuação ("cento e vinte")
    ultima_grandeza = None
    depois_de_e = False
    for token in tokens:
        t = token.lower()
        if t == "e":
            if depois_de_e or (grupo is None and ultima_grandeza is None):
                return None
            depois_de_e = True
            continue
        if t in _GRANDEZAS:
            g = _GRANDEZAS[t]
            if depois_de_e or cento_aberto:
                return None
            if ultima_grandeza is not None and g >= ultima_grandeza:
                return None
            if grupo is None:
                if g != 1000:  # "mil" sozinho vale 1000; "milhão" precisa de número
                    return None
                grupo = 1
            if grupo == 0 or grupo >= 1000:
                return None
            total += grupo * g
            ultima_grandeza, grupo, limite = g, None, 0
        else:
            v, novo_limite = _componente(t)
            if v is None:
                return None
            if grupo is None:
                grupo = v
            elif 0 < v < limite:
                grupo += v
            else:
                return None
            limite = novo_limite
            cento_aberto = t == "cento"
        depois_de_e = False
    if depois_de_e or cento_aberto:
        return None
    if grupo is not None:
        if ultima_grandeza is not None and grupo >= 1000:
            return None
        total += grupo
    return total


def _ler(tokens: list[str], manter_grandeza: bool = False) -> _Numero | None:
    """Interpreta os tokens de um número.

    Só algarismos ("250", "1,5") ficam como estão. Em dinheiro, algarismos +
    grandeza ("250 mil", "1,5 milhão") também ficam. O resto é calculado.
    """
    if len(tokens) == 1 and _eh_digito(tokens[0]):
        return _Numero(escrito=tokens[0])
    if (manter_grandeza and len(tokens) == 2 and _eh_digito(tokens[0])
            and tokens[1].lower() in _GRANDEZAS):
        return _Numero(escrito=tokens[0], grandeza=tokens[1])
    if any("," in t for t in tokens):
        return None
    valor = _valor_inteiro(tokens)
    return None if valor is None else _Numero(valor=valor)


def _sufixo_valido(texto: str, manter_grandeza: bool = False, aceita=None):
    """Maior trecho FINAL de `texto` que é um número válido.

    "entre cinco e dez" -> ("entre cinco e ", 10): só o número colado ao
    gatilho ("por cento", "reais"...) é convertido. `aceita` filtra o número
    lido (ex.: centavos < 100). Devolve None se nada serve.
    """
    tokens = list(re.finditer(r"\S+", texto))
    for i, m in enumerate(tokens):
        palavra = m.group().lower()
        if palavra == "e" or (i > 0 and palavra in _GRANDEZAS):
            continue
        numero = _ler([t.group() for t in tokens[i:]], manter_grandeza)
        if numero is not None and (aceita is None or aceita(numero)):
            return texto[:m.start()], numero
    return None


def _prefixo_valido(texto: str):
    """Maior trecho INICIAL de `texto` que é um número válido (para "D mais")."""
    tokens = list(re.finditer(r"\S+", texto))
    for j in range(len(tokens), 0, -1):
        numero = _ler([t.group() for t in tokens[:j]])
        if numero is not None:
            return numero, texto[tokens[j - 1].end():]
    return None


def _ler_decimais(texto: str) -> str | None:
    """Parte depois da "vírgula" falada: "cinco" -> "5", "zero cinco" -> "05"."""
    tokens = texto.split()
    if len(tokens) == 1 and tokens[0].isascii() and tokens[0].isdigit():
        return tokens[0]
    zeros = ""
    while tokens and tokens[0].lower() == "zero":
        zeros += "0"
        tokens.pop(0)
    if not tokens:
        return zeros
    valor = _valor_inteiro(tokens)
    return None if valor is None else zeros + str(valor)


# ----------------------------------------------------------------------------
# Formatação
# ----------------------------------------------------------------------------

def _milhar(n: int) -> str:
    """2500 -> "2.500"."""
    return f"{n:,}".replace(",", ".")


def _texto_simples(numero: _Numero) -> str:
    """Número por extenso completo (porcentagem, p.p., D+N, centavos)."""
    return numero.escrito if numero.escrito is not None else _milhar(numero.valor)


def _valor_em_reais(n: int) -> str:
    """Exatamente N mil / N milhão(ões) / N bilhão(ões) mantém a palavra;
    com resto, escreve o número inteiro: 250000 -> "250 mil", 2500 -> "2.500"."""
    if n >= 10**9 and n % 10**9 == 0:
        q = n // 10**9
        return f"{_milhar(q)} {'bilhão' if q == 1 else 'bilhões'}"
    if 10**6 <= n < 10**9 and n % 10**6 == 0:
        q = n // 10**6
        return f"{q} {'milhão' if q == 1 else 'milhões'}"
    if 1000 <= n < 10**6 and n % 1000 == 0:
        return f"{n // 1000} mil"
    return _milhar(n)


def _eh_grande(palavra: str | None) -> bool:
    """milhão/milhões/bilhão/bilhões (as que pedem "de" antes de "reais")."""
    return bool(palavra) and palavra.lower().startswith(("milh", "bilh"))


def _numero_com_decimais(numero: _Numero, dec: str) -> str | None:
    """Junta parte inteira e decimais faladas: (1, "cinco") -> "1,5"."""
    if numero.grandeza or (numero.escrito and "," in numero.escrito):
        return None
    decimais = _ler_decimais(dec)
    if decimais is None:
        return None
    return f"{_texto_simples(numero)},{decimais}"


# ----------------------------------------------------------------------------
# Substituições
# ----------------------------------------------------------------------------

def _troca_percentual(m: re.Match) -> str:
    if m.group("meio"):
        return "0,5%"
    achado = _sufixo_valido(m.group("int"))
    if achado is None:
        return m.group(0)
    prefixo, numero = achado
    texto = _texto_simples(numero)
    if m.group("dec") is not None:
        texto = _numero_com_decimais(numero, m.group("dec"))
        if texto is None:
            return m.group(0)
    if m.group("emeio"):
        if "," in texto:
            return m.group(0)
        texto += ",5"
    return f"{prefixo}{texto}%"


def _troca_pontos_percentuais(m: re.Match) -> str:
    achado = _sufixo_valido(m.group("int"))
    if achado is None:
        return m.group(0)
    prefixo, numero = achado
    texto = _texto_simples(numero)
    if m.group("dec") is not None:
        texto = _numero_com_decimais(numero, m.group("dec"))
        if texto is None:
            return m.group(0)
    return f"{prefixo}{texto} p.p."


def _troca_moeda(m: re.Match) -> str:
    original = m.group(0)
    achado = _sufixo_valido(m.group("int"), manter_grandeza=True)
    if achado is None:
        return original
    prefixo, numero = achado
    if prefixo and m.group("rs"):
        return original

    # Corpo do valor e a última palavra antes de "reais" (para validar o "de")
    if m.group("dec") is not None:
        corpo = _numero_com_decimais(numero, m.group("dec"))
        if corpo is None:
            return original
        ultima = m.group("mag")
        if ultima:
            corpo += f" {ultima}"
    elif numero.escrito is not None:
        corpo = numero.escrito
        ultima = numero.grandeza
        if ultima:
            corpo += f" {ultima}"
    else:
        corpo = _valor_em_reais(numero.valor)
        ultima = m.group("int").split()[-1]
    if m.group("de") and not _eh_grande(ultima):
        return original

    # "2 reais e 50 centavos" -> "R$ 2,50" (só sem grandeza e sem decimais)
    cauda = m.group("cauda") or ""
    simples = (m.group("dec") is None and not numero.grandeza
               and not (numero.escrito and "," in numero.escrito))
    if cauda and simples:
        centavos = _ler(m.group("cent").split())
        c = None
        if centavos is not None and centavos.valor is not None:
            c = centavos.valor
        elif centavos is not None and centavos.escrito.isdigit():
            c = int(centavos.escrito)
        if c is not None and c < 100:
            return f"{prefixo}R$ {_texto_simples(numero)},{c:02d}"
    # Sem conversão de centavos, a cauda fica como estava
    return f"{prefixo}R$ {corpo}{cauda}"


def _troca_centavos(m: re.Match) -> str:
    # Só palavras viram algarismos, e centavos são sempre menos de 100
    # ("R$ 250 mil e cinquenta centavos" não pode virar "250.050 centavos")
    achado = _sufixo_valido(m.group("int"),
                            aceita=lambda n: n.valor is not None and n.valor < 100)
    if achado is None:
        return m.group(0)
    prefixo, numero = achado
    resto = m.group(0)[len(m.group("int")):]
    return f"{prefixo}{_milhar(numero.valor)}{resto}"


def _troca_liquidacao(m: re.Match) -> str:
    if m.group("zero"):
        return "D+0"
    achado = _prefixo_valido(m.group("num"))
    if achado is None:
        return m.group(0)
    numero, resto = achado
    if numero.escrito and "," in numero.escrito:
        return m.group(0)
    return f"D+{_texto_simples(numero)}{resto}"


def padronizar(texto: str) -> str:
    """Padroniza números no estilo de prova (bancas ANBIMA/FGV): R$, %, p.p., D+N."""
    if not texto:
        return texto
    texto = _RE_PONTO_DECIMAL.sub(_troca_ponto_decimal, texto)
    # Porcentagem antes de moeda: o "cento" de "por cento" não vira número
    texto = _RE_PERCENTUAL.sub(_troca_percentual, texto)
    texto = _RE_PONTOS_PERCENTUAIS.sub(_troca_pontos_percentuais, texto)
    texto = _RE_MOEDA.sub(_troca_moeda, texto)
    texto = _RE_CIFRAO.sub("R$ ", texto)
    texto = _RE_CENTAVOS.sub(_troca_centavos, texto)
    texto = _RE_LIQUIDACAO.sub(_troca_liquidacao, texto)
    return texto
