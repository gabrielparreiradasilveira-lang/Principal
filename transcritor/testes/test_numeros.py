#!/usr/bin/env python3
"""
Testes de numeros.padronizar().

Rode:  python3 transcritor/testes/test_numeros.py
(script simples, sem pytest; as funções test_* também rodam no pytest)
"""

from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from numeros import padronizar  # noqa: E402

# (entrada, esperado) — frases como sairiam de uma aula
MOEDA = [
    ("A garantia do FGC vai até 250 mil reais por CPF.",
     "A garantia do FGC vai até R$ 250 mil por CPF."),
    ("A taxa é de 250 reais por ano.", "A taxa é de R$ 250 por ano."),
    ("O fundo tem 1,5 milhão de reais em caixa.", "O fundo tem R$ 1,5 milhão em caixa."),
    ("Captou 3 milhões de reais.", "Captou R$ 3 milhões."),
    ("O patrimônio passa de 2 bilhões de reais.", "O patrimônio passa de R$ 2 bilhões."),
    ("Um bilhão de reais é o limite.", "R$ 1 bilhão é o limite."),
    ("O limite é 1.000 reais por mês.", "O limite é R$ 1.000 por mês."),
    ("Ele investiu R$250 mil no CDB.", "Ele investiu R$ 250 mil no CDB."),
    ("Ele investiu R $ 250 mil no CDB.", "Ele investiu R$ 250 mil no CDB."),
    ("Ele investiu R$  250 mil no CDB.", "Ele investiu R$ 250 mil no CDB."),
    ("A cobertura é de R$ 250 mil reais por instituição.",
     "A cobertura é de R$ 250 mil por instituição."),
    ("O boleto saiu R$ 1.500,00 no total.", "O boleto saiu R$ 1.500,00 no total."),
    ("O FGC cobre até duzentos e cinquenta mil reais.", "O FGC cobre até R$ 250 mil."),
    ("A tarifa é de cinquenta reais.", "A tarifa é de R$ 50."),
    ("Paguei cem reais de corretagem.", "Paguei R$ 100 de corretagem."),
    ("Com mil reais você já começa.", "Com R$ 1 mil você já começa."),
    ("Ele tinha um milhão de reais aplicado.", "Ele tinha R$ 1 milhão aplicado."),
    ("Ele recebeu dois mil e quinhentos reais.", "Ele recebeu R$ 2.500."),
    ("Ele recebeu 2 mil e 500 reais.", "Ele recebeu R$ 2.500."),
    ("A cota custa 2 reais e 50 centavos.", "A cota custa R$ 2,50."),
    ("A cota custa dois reais e cinquenta centavos.", "A cota custa R$ 2,50."),
    ("A cota custa dois reais e cinco centavos.", "A cota custa R$ 2,05."),
    ("Custa cento e vinte e cinco reais.", "Custa R$ 125."),
    ("Ficou em um milhão e duzentos mil reais.", "Ficou em R$ 1.200.000."),
    ("Ficou em vinte e cinco mil reais.", "Ficou em R$ 25 mil."),
    ("Dez reais de taxa.", "R$ 10 de taxa."),
    ("O ativo subiu 1.5 milhão de reais.", "O ativo subiu R$ 1,5 milhão."),
    ("Um vírgula cinco milhão de reais.", "R$ 1,5 milhão."),
    ("Entre 100 e 200 reais por mês.", "Entre 100 e R$ 200 por mês."),
    ("Entre cem e duzentos reais por mês.", "Entre cem e R$ 200 por mês."),
    ("Sobrou cinquenta centavos.", "Sobrou 50 centavos."),
    ("Deu R$ 250 mil reais e 50 centavos.", "Deu R$ 250 mil e 50 centavos."),
    ("Deu 250 mil reais e cinquenta centavos.", "Deu R$ 250 mil e 50 centavos."),
]

PERCENTUAL = [
    ("O fundo rende 10 por cento ao ano.", "O fundo rende 10% ao ano."),
    ("O fundo rende 10 % ao ano.", "O fundo rende 10% ao ano."),
    ("O fundo rende dez por cento ao ano.", "O fundo rende 10% ao ano."),
    ("Dez por cento é a alíquota.", "10% é a alíquota."),
    ("A alavancagem chega a cento e vinte por cento.", "A alavancagem chega a 120%."),
    ("A taxa de administração é meio por cento.", "A taxa de administração é 0,5%."),
    ("A taxa é de um e meio por cento.", "A taxa é de 1,5%."),
    ("A taxa é 1 vírgula 5 por cento.", "A taxa é 1,5%."),
    ("A taxa é um vírgula cinco por cento.", "A taxa é 1,5%."),
    ("A taxa é um vírgula zero cinco por cento.", "A taxa é 1,05%."),
    ("O CDB paga 110 por cento do CDI.", "O CDB paga 110% do CDI."),
    ("O CDB paga 100% do CDI.", "O CDB paga 100% do CDI."),
    ("A Selic estava em 13.75% ao ano.", "A Selic estava em 13,75% ao ano."),
    ("O IOF é de 0.5% na operação.", "O IOF é de 0,5% na operação."),
    ("A alíquota é cem por cento.", "A alíquota é 100%."),
    ("Entre cinco e dez por cento.", "Entre cinco e 10%."),
    ("Rende vinte e cinco por cento.", "Rende 25%."),
]

PONTOS_PERCENTUAIS = [
    ("A Selic subiu 2 pontos percentuais em um ano.",
     "A Selic subiu 2 p.p. em um ano."),
    ("A Selic subiu dois pontos percentuais em um ano.",
     "A Selic subiu 2 p.p. em um ano."),
    ("O spread caiu 0,5 ponto percentual no mês.", "O spread caiu 0,5 p.p. no mês."),
    ("O spread caiu 0.5 ponto percentual.", "O spread caiu 0,5 p.p."),
]

DECIMAL = [
    ("A Selic estava em 13.75 ao ano.", "A Selic estava em 13,75 ao ano."),
    ("O fundo tem 1.000 cotistas.", "O fundo tem 1.000 cotistas."),
    ("O fundo tem 10.000.000 de cotas.", "O fundo tem 10.000.000 de cotas."),
    ("A Lei 14.754 mudou os fundos fechados.", "A Lei 14.754 mudou os fundos fechados."),
]

LIQUIDACAO = [
    ("A liquidação é em D mais 2.", "A liquidação é em D+2."),
    ("A liquidação é em D + 2.", "A liquidação é em D+2."),
    ("A liquidação é em D+ 2.", "A liquidação é em D+2."),
    ("O resgate cai em d mais 1 útil.", "O resgate cai em D+1 útil."),
    ("O resgate é D mais zero.", "O resgate é D+0."),
    ("O resgate é D mais dois.", "O resgate é D+2."),
    ("O resgate é D zero.", "O resgate é D+0."),
    ("O fundo tem cotização em D+30.", "O fundo tem cotização em D+30."),
    ("Agora dê mais dois exemplos.", "Agora dê mais dois exemplos."),
]

# Nada aqui pode mudar
INALTERADOS = [
    "Os juros reais são a taxa nominal menos a inflação.",
    "Há motivos reais para isso.",
    "Compare os valores reais com os nominais.",
    "Faz dois anos que ele estuda.",
    "Ele tentou três vezes a prova.",
    "Escolha um fundo de renda fixa.",
    "O primeiro passo é ler o regulamento.",
    "O título vence em 2035.",
    "A certificação CPA-20 é exigida.",
    "Compre a NTN-B 2035 hoje.",
    "Ela paga IPCA mais 5% ao ano.",
    "Cento é uma palavra antiga.",
    "O real valorizou.",
    "Um milhão de pessoas investem.",
    "O D é a data da operação.",
    "Dê mais atenção ao prospecto.",
]

ESQUISITOS = ["", " ", ".", "...", "%", "R$", "R $", "reais", "por cento", "D mais",
              "e e e", "D +", "vírgula", "1.", ".5", "0", "\n\t", "😀 reais",
              "cento por cento", "milhão de reais", "e cinquenta centavos"]


def _verificar_pares(pares):
    falhas = []
    for entrada, esperado in pares:
        obtido = padronizar(entrada)
        if obtido != esperado:
            falhas.append(f"entrada:  {entrada!r}\n  esperado: {esperado!r}\n  obtido:   {obtido!r}")
        elif padronizar(obtido) != obtido:
            falhas.append(f"não idempotente: {entrada!r} -> {obtido!r} -> {padronizar(obtido)!r}")
    return falhas


def _todos_os_pares():
    return (MOEDA + PERCENTUAL + PONTOS_PERCENTUAIS + DECIMAL + LIQUIDACAO
            + [(t, t) for t in INALTERADOS])


def _verificar_esquisitos():
    falhas = []
    longo = " ".join(t for par in _todos_os_pares() for t in par) * 50
    for texto in ESQUISITOS + [longo]:
        try:
            uma = padronizar(texto)
            if padronizar(uma) != uma:
                falhas.append(f"não idempotente: {texto[:60]!r}")
        except Exception as erro:  # noqa: BLE001 - o teste é justamente "não levanta"
            falhas.append(f"levantou {erro!r} com {texto[:60]!r}")
    return falhas


def _verificar_aleatorios(quantidade=3000):
    """Frases aleatórias montadas com o vocabulário numérico: não pode levantar
    e tem que ser idempotente."""
    vocab = ("um dois três dez vinte cento cem duzentos mil milhão milhões de e "
             "reais por cento % pontos ponto percentuais percentual centavos D d "
             "mais + zero meio vírgula R$ R $ 1 2 10 250 1.000 1,5 13.75 0.5 . , "
             "juros CDI dê").split()
    sorteio = random.Random(20261105)
    falhas = []
    for _ in range(quantidade):
        texto = " ".join(sorteio.choice(vocab) for _ in range(sorteio.randint(1, 12)))
        try:
            uma = padronizar(texto)
            if padronizar(uma) != uma:
                falhas.append(f"não idempotente: {texto!r} -> {uma!r} -> {padronizar(uma)!r}")
        except Exception as erro:  # noqa: BLE001
            falhas.append(f"levantou {erro!r} com {texto!r}")
    return falhas


def test_moeda():
    assert not _verificar_pares(MOEDA)


def test_percentual():
    assert not _verificar_pares(PERCENTUAL)


def test_pontos_percentuais():
    assert not _verificar_pares(PONTOS_PERCENTUAIS)


def test_decimal():
    assert not _verificar_pares(DECIMAL)


def test_liquidacao():
    assert not _verificar_pares(LIQUIDACAO)


def test_inalterados():
    assert not _verificar_pares([(t, t) for t in INALTERADOS])


def test_textos_esquisitos():
    assert not _verificar_esquisitos()


def test_aleatorios():
    assert not _verificar_aleatorios()


def main() -> int:
    pares = _todos_os_pares()
    falhas = _verificar_pares(pares) + _verificar_esquisitos()
    falhas_aleatorias = _verificar_aleatorios()
    falhas += falhas_aleatorias
    total = len(pares) + len(ESQUISITOS) + 1 + 3000
    for f in falhas:
        print("FALHA:", f)
    if falhas:
        print(f"FALHOU: {len(falhas)} de {total}")
        return 1
    print(f"OK: {total} casos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
