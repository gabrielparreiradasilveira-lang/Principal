# Exemplo: um bloco de conteúdo completo, do inventário à fala e à lousa

Tema de exemplo: come-cotas, como Bloco 3 (conteúdo) de um vídeo de ~7 min, que tem ~370 palavras de fala nesse bloco. O objetivo é mostrar a densidade esperada e como a lousa complementa a fala; não copie o texto, copie o método. Regras conferidas em 03/11/2026; confira de novo antes de usar.

## 1. Inventário (trabalho interno)

| Campo | Conteúdo | Vai para |
|---|---|---|
| Definição + sinônimos | Recolhimento antecipado e semestral do IR dos fundos, feito pela redução da quantidade de cotas. Sinônimo na prova: "antecipação semestral do IR". | fala |
| Mecanismo | O governo antecipa o imposto em vez de esperar o resgate → o administrador retém no último dia útil de maio e de novembro → as cotas retidas deixam de render. | fala |
| Espectro | Longo prazo: 15%. Curto prazo: 20%. Fundos de ações: não têm. FII, Fiagro e FIP: fora. Fechados: têm, desde 2024. Curto prazo resgatado depois de 180 dias: nada a completar. | fala (núcleo) e lousa (a lista completa de quem tem e quem não tem) |
| Exemplo numérico | Longo prazo: R$ 100 mil, rendimento de R$ 6 mil → R$ 900 em cotas; resgate com 400 dias → complemento de R$ 150. | fala |
| Segundo exemplo | Curto prazo: rendimento de R$ 4.000 → R$ 800 em cotas; resgate com 150 dias → completa R$ 100; depois de 180 dias, nada. | lousa |
| Conceito vizinho | Come-cotas × IR no resgate; come-cotas × IOF (só em resgates antes de 30 dias). | fala |
| Consequência | Com a mesma rentabilidade bruta, um título que só paga IR no vencimento tende a render mais que um fundo com come-cotas. | fala |
| Pegadinha | "O come-cotas incide sobre o valor aplicado" (falso). "Fundo de ações tem come-cotas em novembro" (falso). | pergunta-gatilho da fala |
| Caso real | Desde 01/01/2024 (Lei 14.754/2023), fundos fechados passaram a ter come-cotas. | fala; a lousa repete o ano |
| Simplificações | Longo × curto prazo pelo prazo médio da carteira; fechado "entidade de investimento" fica fora; ETF de renda fixa também fora. | lousa |

Repare na última coluna: o que a fala não comporta (o segundo exemplo, a lista completa, as exceções) vai para a lousa, e não para uma nota que ninguém lê.

## 2. Roteiro do bloco

```
## 3. Conteúdo Técnico e Roteiro Visual — [4 min]
**[Ação na Lousa - Google Slides]**
- Slide 3 · ao dizer "maio e de novembro", sublinhe MAIO e NOVEMBRO · ao dizer "Quem fica de fora", circule a coluna NÃO TEM
**[Locução Direta]**
"..."
```

## 3. Fala

"Neste vídeo, o come-cotas. É a antecipação semestral do imposto de renda dos fundos. O nome é literal: o imposto é cobrado em cotas. A quantidade de cotas diminui; o valor de cada cota, não.

Por que ele existe? Porque o governo não quer esperar o seu resgate para receber. Então, no último dia útil de maio e de novembro, o administrador retém o imposto sobre o rendimento do período, mesmo que você não tenha resgatado nada. Nos fundos de longo prazo, a alíquota é de 15%; nos de curto prazo, de 20%. Repare: são as menores alíquotas de cada tabela. A diferença fica para o resgate.

Um exemplo, com números hipotéticos e considerando só o rendimento deste semestre. Você tem R$ 100 mil num fundo de longo prazo, que rendeu R$ 6 mil. Em maio, saem 15% de R$ 6 mil: R$ 900, em cotas. Se você resgatar com 400 dias, a tabela pede 17,5%. Então, no resgate, você paga os 2,5 pontos que faltam sobre esses R$ 6 mil: R$ 150.

No fundo de curto prazo, a conta muda. O come-cotas já leva 20%. Se o resgate for depois de 180 dias, não há nada a completar, porque 20% é o piso dessa tabela. Antes de 180 dias, você completa até 22,5%.

Quem fica de fora? Fundos de ações, fundos imobiliários, Fiagro e FIP. E um caso real: até 2023, nos fundos fechados, formato de muitos fundos exclusivos, o imposto só vinha no resgate ou na amortização. Desde janeiro de 2024, pela Lei 14.754, os fundos fechados também têm come-cotas.

Não confunda come-cotas com IOF. Nas aplicações, o IOF sobre o rendimento só incide em resgates antes de 30 dias. O come-cotas acontece a cada seis meses, enquanto o dinheiro fica no fundo.

E daí, para o cliente? Com a mesma rentabilidade bruta, um título que só paga imposto no vencimento tende a render um pouco mais que um fundo com come-cotas: o imposto que ficou no título continuou rendendo.

*Pergunta-gatilho rápida:* o fundo de ações do seu cliente vai ter cotas retidas em novembro? **Não.** Fundo de ações não tem come-cotas: o imposto de 15% é cobrado só no resgate."

## 4. Lousa (o que a fala não mostra)

```json
{"saida": "r00a_3_come-cotas.png", "semente": 302, "molde": "colunas",
 "titulo": "2. COME-COTAS = IR ANTECIPADO EM COTAS",
 "topo": "ÚLTIMO DIA ÚTIL DE {laranja:MAIO} E DE {laranja:NOVEMBRO} · A QUANTIDADE DE COTAS CAI · NO RESGATE, ACERTO ATÉ A ALÍQUOTA DA TABELA",
 "colunas": [
  {"titulo": "TEM COME-COTAS", "texto": "- RENDA FIXA, MULTIMERCADO, CAMBIAL\n- LONGO PRAZO: {laranja:15%} · CURTO PRAZO: {laranja:20%}\n- FECHADOS: {laranja:DESDE 2024} (LEI 14.754/2023)\n- PRAZO MÉDIO DA CARTEIRA DEFINE LONGO OU CURTO"},
  {"titulo": "NÃO TEM", "texto": "- FUNDOS DE AÇÕES: IR SÓ NO RESGATE\n- FII · FIAGRO · FIP\n- ETF DE RENDA FIXA\n- FECHADO \"ENTIDADE DE INVESTIMENTO\""}],
 "destaque": {"texto": "CURTO PRAZO, R$ 4.000 DE RENDIMENTO → SAEM R$ 800 EM COTAS · RESGATE COM 150 DIAS: COMPLETA R$ 100 · DEPOIS DE 180 DIAS: NADA", "cor": "branco", "moldura": "amarelo"},
 "referencia": "TRIBUTAÇÃO DOS FUNDOS DE INVESTIMENTO (LEI 14.754/2023)"}
```

Conferido: sem avisos; a marca `R00A · 3/4` no topo e a fonte no rodapé.

## 5. O que este exemplo faz que um material raso não faz

- A fala diz **por que** a regra existe, faz a **conta** com o complemento no resgate e separa o **vizinho** (IOF).
- A pergunta-gatilho responde com a **regra**, não só com "errado".
- A lousa não repete a fala: traz a **lista completa** de quem tem e quem não tem, as **exceções** (ETF de renda fixa, entidade de investimento, prazo médio) e um **segundo exemplo** (curto prazo), com números que a fala não usa.

## 6. Linha do checklist

3.2 come-cotas: definição ✓ · mecanismo ✓ · espectro ✓ (fala e lousa) · exemplo ✓ (fala; segundo exemplo na lousa) · vizinho ✓ (IOF; IR no resgate) · consequência ✓ · pegadinha ✓ (pergunta-gatilho) · caso real ✓ (Lei 14.754/2023, fundos fechados) · simplificações → lousa.
