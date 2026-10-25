# Roteiro de fala — Aula CPA: Amortização, Prazo Médio de Vencimento e Taxa Interna de Retorno (TIR)

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3.5**, **1.3.3.5.1** e **1.3.3.5.2**; slides A3475 p. 2–10 (TIR, prazo médio, amortização e o caso da holding); aula do repositório `aula-1.3-D-tir-cmpc-duration-retorno-payback`.

CPA 1.3.3.5 · 1.3.3.5.1 · 1.3.3.5.2 · Módulo 1 · **20 min** · Aula G5 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula é uma **obra de construção civil**. A amortização são os **tijolos** retirados do muro da dívida, um a um. O prazo médio é o **centro de gravidade** dos pagamentos no tempo. A TIR é a **balança** que equilibra o investimento inicial e o que volta. O caso não é o do slide (holding com CMPC): é uma **rede de cafeterias** que compra uma unidade com financiamento.

- Caso: **Joana** compra uma cafeteria por R$ 300.000, financiados a 10% a.a. em quatro parcelas de amortização constante. A loja gera caixa de 100, 120, 140 e 160 mil nos quatro anos.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3.5 Amortização | Slides A3475 p. 5; aula 1.3-D | Conferido; **periódica e única (bullet)** |
| 1.3.3.5.1 Prazo médio e vencimento | Slides A3475 p. 3; aula 1.3-D | Conferido; **prazo médio ≠ liquidez**, correção da aula 1.3-D |
| 1.3.3.5.2 TIR | Slides A3475 p. 2 | Conferido; regra de decisão |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3475 p. 3 | "Prazo médio está relacionado à liquidez do ativo" | Prazo médio mede **quando o dinheiro volta**; liquidez é a facilidade de vender antes do vencimento. Não são a mesma coisa |
| 2 | Slides A3475 p. 3 | Prazo médio "é a base para o cálculo de Duration" | Correto, e a G7 mostra a diferença: a duration pondera pelo valor **presente**, não pelo valor nominal |
| 3 | Slides A3475 p. 2 | "TIR > CMPC → investimento gera valor" | Correto. Mas a TIR sozinha não diz **quanto** de valor se gera; isso é o VPL (G3) |
| 4 | Slides A3475 p. 5 | "Amortização única (ex.: bullet)" | Bullet é amortização única **no vencimento**. Não confundir com zero cupom (G3) |

### 🔇 Dados do exemplo (Joana)

| Item | Valor |
| --- | --- |
| Investimento inicial | R$ 300.000 |
| Fluxos de caixa | Ano 1: 100.000 · Ano 2: 120.000 · Ano 3: 140.000 · Ano 4: 160.000 |
| TIR | **23,96% a.a.** |
| Financiamento | R$ 300.000, 10% a.a., amortização de R$ 75.000 por ano |
| Juros do ano 1 | 300.000 × 10% = **R$ 30.000** → saldo de R$ 225.000 |
| Juros do ano 2 | 225.000 × 10% = **R$ 22.500** → saldo de R$ 150.000 |
| Juros do ano 3 | 150.000 × 10% = **R$ 15.000** → saldo de R$ 75.000 |
| Juros do ano 4 | 75.000 × 10% = **R$ 7.500** → saldo zero |
| Prazo médio dos fluxos | Σ(t × CFt) ÷ ΣCFt = (1×100 + 2×120 + 3×140 + 4×160) ÷ 520 = 1.400 ÷ 520 = **2,69 anos** |

🔇 Valores hipotéticos. A TIR de 23,96% é maior que a taxa de 10% do financiamento e, portanto, o projeto cria valor sobre a dívida. A conta de CMPC é do roteiro G6.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Os tijolos da amortização | 5 min |
| 2. O centro de gravidade: prazo médio | 5 min |
| 3. A balança: TIR | 7 min |
| 4. Como decidir com a TIR | 3 min |
| **Total** | **20 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — Os tijolos da amortização — 5 min

- "Amortizar é tirar tijolos do muro da dívida. Cada pagamento de amortização retira um pedaço do principal. Os juros são o aluguel do tijolo que ainda está no muro."
- "Há dois jeitos comuns: amortização **periódica**, com tijolos saindo a cada período, e amortização **única**, em que todos saem no vencimento (bullet)."
- "Joana paga R$ 75.000 de amortização por ano. Os juros caem à medida que o muro encolhe."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `300000` `ENTER` `10` `%` | 🖥️ 30.000,00 | Juros do ano 1 |
| 2 | ⌨️ `225000` `ENTER` `10` `%` | 🖥️ 22.500,00 | Juros do ano 2 |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Na amortização constante, os juros caem ao longo do tempo" | Certo | O saldo devedor cai |
| "Amortização única significa pagar o principal em parcelas iguais" | Errado | É o principal **no vencimento** |

> **Amortizar é tirar tijolos do muro: o juro cai com a altura.**

**🔗 Ponte:** "Depois de tirar os tijolos, onde está o centro do pagamento no tempo?"

---

### Bloco 2 — O centro de gravidade: prazo médio — 5 min

- "O **prazo médio** é o tempo médio em que o dinheiro volta, pesado pelo tamanho de cada fluxo. É o centro de gravidade."
- ✏️ "O slide diz que o prazo médio mede a liquidez. Não: mede quando o dinheiro volta. Liquidez é a facilidade de vender antes."

| Ano (t) | Fluxo (CFt) | t × CFt |
| --- | --- | --- |
| 1 | 100.000 | 100.000 |
| 2 | 120.000 | 240.000 |
| 3 | 140.000 | 420.000 |
| 4 | 160.000 | 640.000 |
| **Soma** | **520.000** | **1.400.000** |

- Prazo médio = 1.400.000 ÷ 520.000 = **2,69 anos**.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1400000` `ENTER` `520000` `÷` | 🖥️ 2,69 | Prazo médio, em anos |

- 🔇 Esta conta é ponderada pelos valores **nominais**. A duration (G7) pondera pelo valor **presente**. Não confundir as duas.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Quanto maior o prazo médio, maior a sensibilidade à taxa de juros" | Certo | Slides A3475 p. 3 |
| "Prazo médio e liquidez são a mesma coisa" | Errado | Prazo médio mede quando o dinheiro volta |

> **Prazo médio é o centro de gravidade dos recebimentos no tempo.**

**🔗 Ponte:** "Agora a balança: o investimento de 300 mil volta mesmo valendo a pena?"

---

### Bloco 3 — A balança: TIR — 7 min

- "A **TIR** é a taxa que zera o VPL: a taxa em que o valor presente dos recebimentos iguala o investimento. É a taxa de equilíbrio da balança."
- "Se a TIR for maior que a exigência de quem investe (CMPC, G6), o investimento gera valor. Se for menor, destrói."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `300000` `CHS` `g` `CF0` | 🖥️ −300.000,00 | Investimento inicial (fluxo zero) |
| 2 | ⌨️ `100000` `g` `CFj` `120000` `g` `CFj` `140000` `g` `CFj` `160000` `g` `CFj` | 🖥️ 160.000,00 | Fluxos dos anos 1 a 4 |
| 3 | ⌨️ `f` `IRR` | 🖥️ 23,96 | TIR, em % ao ano |

- "Vinte e três vírgula noventa e seis por cento ao ano. Esse é o retorno que a cafeteria oferece sobre os 300 mil."
- 🔇 A HP12C usa `g CF0` para o fluxo inicial e `g CFj` para cada fluxo seguinte. Não entre o fluxo do ano 0 como positivo: o investimento é saída.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A TIR é a taxa que zera o VPL" | Certo | Slides A3475 p. 2 |
| "Com TIR maior que a exigência de retorno, o investimento destrói valor" | Errado | Gera valor |

> **TIR: a taxa que equilibra a balança. Acima da exigência, gera valor.**

---

### Bloco 4 — Como decidir com a TIR — 3 min

- "Se a TIR de 23,96% fica acima da exigência de 13,58% (a CMPC da G6, para uma empresa com essa estrutura), a cafeteria cria valor."
- ➕ "Mas cuidado: a TIR sozinha não diz o **tamanho** do valor criado. Para isso, o VPL. Dois projetos podem ter TIR parecida e VPL bem diferente."
- 🔇 Esse cuidado conecta com a G3 (VPL) e com a G6 (CMPC).

> **TIR diz a taxa; VPL diz o tamanho. A decisão precisa dos dois.**

- 🔇 Fechamento: "Amortizar é tirar tijolos; o prazo médio mostra quando o dinheiro volta; a TIR é a taxa de equilíbrio; e a decisão precisa da exigência de retorno."

---

## Nota de verificação

- PD 1.3.3.5 a 1.3.3.5.2 lido no texto do repositório. Slides A3475 lidos nesta sessão.
- Cálculos conferidos em Python: TIR de −300.000 e fluxos 100, 120, 140 e 160 mil = 23,96%; saldo devedor e juros: 30.000, 22.500, 15.000 e 7.500; prazo médio nominal (1.400.000 ÷ 520.000) = 2,69 anos.
- Teclas de fluxo (`g CF0`, `g CFj`, `f IRR`) conferidas na sequência padrão da HP12C; confirmar no equipamento antes de gravar.
- Convenções: financiamento de 10% a.a. e fluxos de caixa do caso da cafeteria são didáticos.
- Sem norma: TIR, prazo médio e amortização são matemática financeira clássica.
