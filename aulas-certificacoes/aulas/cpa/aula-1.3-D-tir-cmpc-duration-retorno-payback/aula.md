# Aula CPA — Prazo Médio, TIR, CMPC, Duration, Alavancagem, Retorno Histórico × Esperado e Payback

Sep 28, 2026 · @Boss · Roteiro integrado · 40 min

## Identificação e alinhamento

Aula D de 5 do item **1.3 Operações do mercado financeiro** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), Módulo 1. Cobre **1.3.3.5** (amortização), **1.3.3.5.1** (prazo médio e vencimento), **1.3.3.5.2** (TIR), **1.3.3.5.5** (CMPC), **1.3.3.5.6** (duration × prazo), **1.3.3.5.6.1** (alavancagem e custos de captação), **1.3.3.6 a 1.3.3.6.2** (retorno histórico e esperado, de um ativo e de uma carteira) e **1.3.6** (payback). Base: PDFs **A3475, A3476 e A3477**, **APOSTILA-CPA p. 129–141**.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 1.3.3.5 Amortização | PDF A3475 p. 5 · APOSTILA-CPA p. 129 | Conferido (detalhe dos sistemas na Aula E) |
| 1.3.3.5.1 Prazo médio e vencimento | PDF A3475 p. 3, 7 | Conferido; fórmula **completada**; exercício **resolvido** |
| 1.3.3.5.2 TIR | PDF A3475 p. 2, 8 · APOSTILA-CPA p. 129–130 | Conferido; exercício **resolvido** |
| 1.3.3.5.5 CMPC | PDF A3475 p. 4, 9 · APOSTILA-CPA p. 133–134 | Conferido; exercício **resolvido** |
| 1.3.3.5.6 Duration × prazo | PDF A3476 p. 6 | Conferido, **com correção** (peso pelo valor presente) |
| 1.3.3.5.6.1 Alavancagem e custos de captação | PDF A3476 p. 7 · APOSTILA-CPA p. 135–136 | Conferido, com correção (custo da dívida) |
| 1.3.3.6 Retorno histórico × esperado | PDF A3476 p. 8–9 | Conferido |
| 1.3.3.6.1 / 1.3.3.6.2 De um ativo / de uma carteira | PDF A3476 p. 10 | **Completado:** fórmula por cenários e da carteira |
| 1.3.6 Payback | PDF A3477 p. 6–9 · APOSTILA-CPA p. 140–141 | Conferido; **payback descontado** e limitações completados |

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 3 min |
| 2. Metáfora central | 3 min |
| 3. Tópicos (Prazo médio 3 · TIR 4 · CMPC e custos de captação 4 · Duration × prazo 3 · Alavancagem 3 · Retorno histórico × esperado 3 · Payback 2) | 22 min |
| 4. Por que cai na prova | 4 min |
| 5. Case | 3 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **40 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | PDF A3476 p. 6 | Duration = "prazo médio ponderado dos fluxos de caixa" | Duration (de Macaulay) = prazo médio ponderado pelo **valor presente** de cada fluxo. O **prazo médio** simples pondera pelos valores **sem desconto** | — |
| 2 | PDF A3476 p. 7 | Alavancagem: ativo sobe 10% → "+100% de retorno" | A conta **ignora os juros do empréstimo**. Alavancagem só amplia o ganho quando o retorno do ativo **supera o custo da dívida** (APOSTILA-CPA p. 135) | — |
| 3 | PDF A3475 p. 3 | Prazo médio "está relacionado à liquidez do ativo" | Prazo médio mede **quando** o dinheiro volta; liquidez é a facilidade de **vender** antes. Relação retirada | — |
| 4 | PDF A3477 p. 7 | Marca comercial no exemplo | Trocada por "máquina de café" (genérico) | — |
| 5 | PDF A3475 p. 6–10 | Exercício sem resposta; nome próprio | **Resolvido**; nome trocado por "o analista" | — |

## 1. Fala de abertura — 3 min

> Um analista tem um projeto de R$ 500 mil que devolve R$ 200 mil, R$ 225 mil e R$ 225 mil em três anos.
>
> A empresa paga, em média, 13,37% ao ano pelo dinheiro que usa. O projeto rende 14,05%.
>
> Então ele cria valor, por pouco. Hoje vamos aprender a calcular esses dois números, **TIR** e **CMPC**, e mais: prazo médio, duration, alavancagem, retorno esperado e payback.

### Objetivo da abertura

Mostrar que decidir um investimento é comparar o **retorno do projeto** com o **custo do dinheiro**.

### Conexão com o Programa Detalhado

CPA 1.3.3.5 a 1.3.3.6.2 e 1.3.6.

## 2. Metáfora central — 3 min

### Metáfora: a gangorra do investimento

> De um lado da gangorra fica o **retorno do projeto** (a **TIR**). Do outro, o **custo do dinheiro** (o **CMPC**).
>
> Se a TIR pesa mais, a gangorra desce para o lado do lucro: o projeto **cria valor**.
>
> O **prazo médio** e a **duration** dizem **quão longe do centro** está o dinheiro: quanto mais longe, mais a gangorra balança quando os juros mudam.
>
> A **alavancagem** é **alongar a tábua**: amplia o movimento para cima e para baixo.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Peso do retorno | TIR |
| Peso do custo | CMPC |
| Distância do centro | Prazo médio / duration |
| Tábua mais longa | Alavancagem |

### Frase de fixação

> **TIR contra CMPC: quem pesa mais decide.**

## 3. Explicação dos tópicos — 22 min

### 3.1 Prazo médio e vencimento — 3 min

#### Como funciona

| Conceito | Definição |
| --- | --- |
| **Vencimento (prazo)** | Data do **último** fluxo |
| **Prazo médio** | Tempo médio em que os fluxos são recebidos, ponderado pelos valores |

> **Prazo médio = Σ (tempo × fluxo) ÷ Σ fluxos**

**Exercício (PDF A3475):** fluxos de R$ 200 mil (ano 1), R$ 225 mil (ano 2), R$ 225 mil (ano 3).

| Passo | Conta | Resultado |
| --- | --- | --- |
| Σ tempo × fluxo | 1×200 + 2×225 + 3×225 | 1.325 |
| Σ fluxos | 200 + 225 + 225 | 650 |
| Prazo médio | 1.325 ÷ 650 | **2,04 anos** |

Quanto **maior** o prazo médio, **maior** a sensibilidade do preço aos juros.

#### Frase de fixação

> **Vencimento é o último pagamento; prazo médio é o centro de gravidade dos pagamentos.**

#### Alinhamento ao PD

CPA 1.3.3.5 e 1.3.3.5.1.

---

### 3.2 Taxa Interna de Retorno (TIR) — 4 min

#### O que é

**TIR** é a **taxa de desconto que zera o VPL**. É a rentabilidade média por período que o fluxo de caixa entrega.

#### Como funciona

**Exercício (PDF A3475):** investimento de R$ 500 mil; recebe 200, 225 e 225 (mil).

**HP12C:** `f CLX` · `500000 CHS g CF0` · `200000 g CFj` · `225000 g CFj` · `2 g Nj` · `f IRR` → **14,05% a.a.**

| Comparação | Decisão |
| --- | --- |
| TIR > custo de capital (CMPC/TMA) | Cria valor (≈ VPL > 0) |
| TIR = custo de capital | Indiferente (VPL = 0) |
| TIR < custo de capital | Destrói valor (VPL < 0) |

#### O que a prova pode confundir

- **TIR não é taxa de desconto escolhida**: é o **resultado** do fluxo.
- TIR e VPL andam juntos: TIR acima da TMA ⇔ VPL positivo nessa TMA.

#### Frase de fixação

> **TIR é a taxa que zera o VPL.**

#### Alinhamento ao PD

CPA 1.3.3.5.2.

---

### 3.3 CMPC e custos de captação — 4 min

#### O que é

**CMPC (WACC)** é o **custo médio** que a empresa paga pelo capital que usa, ponderando **capital próprio** (sócios) e **capital de terceiros** (dívida).

#### Como funciona

> **CMPC = %Próprio × Ke + %Terceiros × Kd × (1 − IR)**

| Fonte de captação | Custo | Observação |
| --- | --- | --- |
| **Capital próprio (Ke)** | Retorno exigido pelos sócios | Mais **caro**: o sócio corre mais risco |
| **Capital de terceiros (Kd)** | Juros da dívida | Mais **barato**; juros são **dedutíveis** do IR (benefício fiscal) |

**Exercício (PDF A3475):** 60% próprio a 17%; 40% dívida a 12%; IR 34%.

| Passo | Conta | Resultado |
| --- | --- | --- |
| Parte própria | 0,60 × 17% | 10,20% |
| Parte dívida | 0,40 × 12% × (1 − 0,34) | 3,168% |
| **CMPC** | 10,20% + 3,168% | **13,37% a.a.** |

**Decisão:** TIR 14,05% > CMPC 13,37% → **viável**. VPL a 13,37% ≈ **+R$ 5.905**.

#### O que a prova pode confundir

- O **IR reduz só o custo da dívida**, não o do capital próprio.
- CMPC é a **taxa de corte** para aceitar projetos.

#### Frase de fixação

> **CMPC é o preço médio do dinheiro da empresa; projeto bom rende mais que ele.**

#### Alinhamento ao PD

CPA 1.3.3.5.5 e 1.3.3.5.6.1.

---

### 3.4 Duration × prazo — 3 min

#### Como funciona

| Conceito | Definição |
| --- | --- |
| **Prazo** | Tempo até o vencimento |
| **Duration (Macaulay)** | Prazo médio dos fluxos ponderado pelo **valor presente** de cada fluxo |

No exemplo acima (desconto pela TIR de 14,05%): duration ≈ **1,95 ano**, menor que o prazo médio simples (2,04) e que o vencimento (3).

| Título | Duration |
| --- | --- |
| **Zero cupom** | **Igual ao prazo** |
| **Com cupom ou amortizante** | **Menor que o prazo** |

**Uso:** quanto **maior a duration**, **maior** a variação do preço quando os juros mudam (risco de mercado).

#### Frase de fixação

> **Zero cupom: duration = prazo; com cupom: duration < prazo.**

#### Alinhamento ao PD

CPA 1.3.3.5.6.

---

### 3.5 Alavancagem financeira — 3 min

#### O que é

**Alavancagem** é usar **recursos de terceiros** para investir mais do que o próprio capital. Amplia **ganhos e perdas**.

#### Como funciona

**Exemplo (APOSTILA-CPA p. 135, com custo da dívida):** capital próprio R$ 10.000 + empréstimo R$ 20.000 (custo de 5% no período) = R$ 30.000 investidos.

| Cenário | Resultado do ativo | Juros da dívida | Resultado líquido | Sobre o capital próprio |
| --- | --- | --- | --- | --- |
| Ativo **+10%** | +3.000 | −1.000 | +2.000 | **+20%** |
| Ativo **−10%** | −3.000 | −1.000 | −4.000 | **−40%** |
| Sem alavancagem, +10% | +1.000 | — | +1.000 | +10% |

| Tipo | Condição |
| --- | --- |
| **Alavancagem positiva** | Retorno do ativo > custo da dívida |
| **Alavancagem negativa** | Retorno do ativo < custo da dívida |

#### Frase de fixação

> **Alavancagem alonga a tábua: sobe mais e cai mais.**

#### Alinhamento ao PD

CPA 1.3.3.5.6.1.

---

### 3.6 Retorno histórico × retorno esperado (ativo e carteira) — 3 min

#### Como funciona

| Conceito | Definição |
| --- | --- |
| **Retorno histórico** | O que o ativo **efetivamente** rendeu no passado; base para média e volatilidade |
| **Retorno esperado** | Estimativa do retorno **futuro**, por cenários e probabilidades |

**De um ativo:**

> **E(R) = Σ (probabilidade × retorno do cenário)**

| Cenário | Probabilidade | Retorno | Produto |
| --- | --- | --- | --- |
| Otimista | 25% | 30% | 7,5% |
| Base | 50% | 12% | 6,0% |
| Pessimista | 25% | −10% | −2,5% |
| **Retorno esperado** | | | **11,0%** |

**De uma carteira:**

> **E(Rcarteira) = Σ (peso do ativo × retorno esperado do ativo)**

Carteira com 60% no ativo acima (11%) e 40% em renda fixa (10%): 0,6 × 11% + 0,4 × 10% = **10,6%**.

#### O que a prova pode confundir

- **Retorno passado não garante retorno futuro.**
- O **retorno** da carteira é a média ponderada, mas o **risco** da carteira pode ser **menor** que a média dos riscos (diversificação).

#### Frase de fixação

> **Histórico olha o retrovisor; esperado olha o para-brisa.**

#### Alinhamento ao PD

CPA 1.3.3.6, 1.3.3.6.1 e 1.3.3.6.2.

---

### 3.7 Prazo de retorno (payback) — 2 min

#### Como funciona

| Tipo | Como calcula | Exemplo: máquina de R$ 30.000, lucro de R$ 5.000/mês |
| --- | --- | --- |
| **Payback simples** | Investimento ÷ fluxo por período | 30.000 ÷ 5.000 = **6 meses** |
| **Payback descontado** | Acumula os fluxos **trazidos a valor presente** | A 1% a.m.: após 6 meses acumula R$ 28.977 → paga-se **entre 6 e 7 meses** |

**Limitações:** o payback simples **ignora o valor do dinheiro no tempo** e **ignora os fluxos depois** do prazo de retorno. Por isso não substitui VPL e TIR.

#### Frase de fixação

> **Payback diz quando o dinheiro volta, não quanto o projeto vale.**

#### Alinhamento ao PD

CPA 1.3.6.

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

A CPA cobra a **regra TIR × CMPC**, a **fórmula do CMPC** (com IR só na dívida), **duration × prazo** e os **limites do payback**.

### Pontos de atenção

1. **TIR zera o VPL.**
2. **CMPC = %E × Ke + %D × Kd × (1 − IR).**
3. **Duration pondera pelo valor presente; zero cupom: duration = prazo.**
4. **Alavancagem amplia ganho e perda.**
5. **E(R) = Σ probabilidade × retorno.**
6. **Payback simples ignora o tempo do dinheiro.**

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Prazo | Duration | Último fluxo × média ponderada a valor presente |
| TIR | CMPC | Retorno do projeto × custo do dinheiro |
| Capital próprio | Capital de terceiros | Mais caro, sem benefício fiscal × mais barato, juros dedutíveis |
| Payback simples | Payback descontado | Sem × com valor do dinheiro no tempo |

### Palavras-chave da prova

- **"Taxa que zera o VPL"**: TIR.
- **"Taxa de corte"**: CMPC.
- **"Sensibilidade a juros"**: duration.

### Pegadinhas

- "Título com cupons tem duration maior que o prazo." **Errado:** menor.
- "O IR reduz o custo do capital próprio." **Errado:** só o da dívida.

### Frase de fixação

> **Retorno contra custo, prazo contra duration, simples contra descontado.**

## 5. Case — 3 min

### Situação

> O analista compara dois projetos de R$ 500 mil. O projeto 1 tem TIR de 14,05% e payback de cerca de 2,3 anos. O projeto 2 tem TIR de 12% e payback de 2 anos. O CMPC da holding é 13,37%.

### Conceitos aplicados

| Projeto | TIR × CMPC | Decisão |
| --- | --- | --- |
| 1 | 14,05% > 13,37% | **Cria valor** |
| 2 | 12% < 13,37% | **Destrói valor**, apesar do payback menor |

### Síntese do case

Payback curto não salva um projeto que rende menos que o custo do capital.

### Frase de fixação

> **Primeiro TIR × CMPC; payback é critério auxiliar.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 1.3.3.5.5 CMPC · **Nível:** Médio

### Questão

Uma empresa é financiada com 50% de capital próprio, cujo custo é de 16% ao ano, e 50% de dívida, com custo de 10% ao ano. A alíquota de imposto de renda é de 30%. O custo médio ponderado de capital (CMPC) é de:

A) 13,0%.

B) 11,5%.

C) 9,1%.

D) 8,0%.

### Ponto-chave do enunciado

O IR reduz **só** o custo da dívida.

### Gabarito

**Alternativa B.**

### Comentário da alternativa correta

0,5 × 16% + 0,5 × 10% × (1 − 0,30) = 8% + 3,5% = **11,5%**.

### Por que as demais estão incorretas?

- **A:** média simples sem o benefício fiscal da dívida (8% + 5%).
- **C:** aplicou o IR sobre o **total** (13% × 0,7).
- **D:** considerou só a parcela do capital próprio (0,5 × 16%) e esqueceu a dívida.

### Armadilhas e macetes

- **(1 − IR) só multiplica o Kd.**

### Referência

APOSTILA-CPA p. 133–134; PDF A3475 p. 4; Programa Detalhado CPA, item 1.3.3.5.5.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. Prazo médio = Σ(t × fluxo) ÷ Σ fluxos; vencimento = último fluxo.
2. TIR zera o VPL; compare com o CMPC: acima cria valor.
3. CMPC = %E × Ke + %D × Kd × (1 − IR); dívida é mais barata e dedutível.
4. Duration pondera pelo valor presente; zero cupom = prazo; com cupom < prazo. Alavancagem amplia ganho e perda.
5. E(R) = Σ p × R; carteira = média ponderada; payback simples ignora o tempo do dinheiro e os fluxos seguintes.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Prazo médio | Σ(t × F) ÷ ΣF |
| TIR | Taxa que zera o VPL |
| CMPC | %E·Ke + %D·Kd·(1 − IR) |
| Duration | Média ponderada a valor presente · zero cupom = prazo |
| Alavancagem | Positiva se retorno > custo da dívida |
| Retorno esperado | Σ probabilidade × retorno |
| Carteira | Σ peso × retorno |
| Payback | Investimento ÷ fluxo · ignora valor do dinheiro no tempo |

### Cadeia lógica

> Desenhar o fluxo → prazo médio e duration (tempo e risco) → TIR (retorno) → CMPC (custo) → decidir; payback como apoio

### Diferenças que não podem ser confundidas

- **Prazo ≠ prazo médio ≠ duration.**
- **TIR ≠ TMA.**
- **Retorno histórico ≠ esperado.**

### Frase central da aula

> **A gangorra do investimento: TIR de um lado, CMPC do outro; o tempo e a alavancagem aumentam o balanço.**

### Próximo passo de estudo

Aula 1.3-E — SAC × Price.

## Referências oficiais e status

Último acesso: 2026-09-28.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — itens 1.3.3.5 a 1.3.3.6.2 e 1.3.6 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. Fórmulas de TIR, CMPC, duration, retorno esperado e payback: finanças corporativas clássicas, sem norma específica.

Fontes de origem (não oficiais): PDFs A3475 "Amortização, Retorno e Custo de Capital", A3476 "Tempo, Alavancagem e Risco" e A3477 "Taxa de Desconto Comercial e PayBack" (`00-fontes/materiais-aula/topico-1.3-operacoes-mercado-financeiro/`); APOSTILA-CPA p. 129–141.
