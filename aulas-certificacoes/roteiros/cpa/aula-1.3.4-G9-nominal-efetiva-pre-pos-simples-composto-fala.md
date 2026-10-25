# Roteiro de fala — Aula CPA: Taxas de Juros — Efetiva, Prefixada × Pós-Fixada, Juros Simples × Compostos

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.4**, **1.3.4.1** (nominal, efetiva e real), **1.3.4.2** (prefixada e pós-fixada) e **1.3.4.3** (juros simples e compostos); APOSTILA-CPA p. 123–125; slides A3472 p. 4–13; aula do repositório `aula-1.3-A-taxas-nominal-efetiva-real-indexador`.

CPA 1.3.4 · 1.3.4.1 · 1.3.4.2 · 1.3.4.3 · Módulo 1 · **10 min** · Aula G9 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula é um **rótulo de embalagem** com duas perguntas e uma troca de contrato. O rótulo de um produto traz a taxa **nominal** e a **efetiva**, e a pergunta é: o que está escrito é o que se paga? O contrato de aluguel mostra o outro eixo: **pré-fixado** (preço fixo) ou **pós-fixado** (reajustado por um índice). O caso é uma escolha entre dois contratos de aluguel de um mesmo imóvel.

- Caso: **Marta** precisa escolher entre um financiamento a taxa fixa de 12% a.a. e um reajustado por 105% do CDI. Ela também quer saber, no rótulo de um cartão, qual é a taxa efetiva.

🔇 Nominal × real foi a G1. Simples × composto está aqui de forma resumida; a aula G2 aprofunda.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.4.1 Nominal, efetiva e real | Slides A3472 p. 5–11; apostila p. 124 | Conferido; **efetiva ilustrada** |
| 1.3.4.2 Prefixada e pós-fixada | Slides A3472 p. 13 | Conferido; **híbrida incluída** |
| 1.3.4.3 Simples e compostos | Slides A3472 p. 3–5 | Conferido; resumido |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3472 p. 13 | "Tesouro Prefixado 2027 pagando 10,50% a.a." | Número datado. Ensina-se o conceito |
| 2 | Slides A3472 p. 13 | Pós-fixada: "CDB que paga 100% do CDI" | Correto. Mas o rendimento depende do CDI efetivo, e não há garantia de nominal fixa |
| 3 | Apostila p. 124 | "Taxa efetiva: 10% ao ano, ou 1% ao mês" | Não confundir: a efetiva é a que reflete a capitalização, e pode ser maior que a nominal |
| 4 | Slides A3472 p. 4 | "Taxa proporcional: 2% ao mês → 24% ao ano" | Vale só no simples. Em composto, a efetiva anual é 26,82% |
| 5 | Slides A3472 p. 13 | "Taxa híbrida: Tesouro IPCA+ paga 5,50% + IPCA" | Correto: uma parte prefixada e uma pós-fixada, mas o nome do produto e o número são datados |

### 🔇 Dados do exemplo (Marta)

| Item | Valor |
| --- | --- |
| Opção A: taxa fixa | 12% a.a. |
| Opção B: 105% do CDI | Com CDI de 9% → 9,45%; com CDI de 14% → 14,70% |
| Ponto de equilíbrio | CDI de **11,43%** a.a. (12 ÷ 1,05) |
| Taxa nominal de um cartão | 2% a.m. |
| Taxa efetiva anual do cartão | 1,02¹² − 1 = **26,82%** a.a. |
| Simples × composto (R$ 10.000, 2% a.m., 12 meses) | Simples: **R$ 12.400**; composto: **R$ 12.682,42** |

🔇 Valores hipotéticos. Não há produto específico.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. O rótulo: nominal e efetiva | 3 min |
| 2. O contrato: pré × pós | 4 min |
| 3. Simples × composto, em uma linha | 2 min |
| 4. Fechamento | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — O rótulo: nominal e efetiva — 3 min

- "Lendo o rótulo, a taxa **nominal** é a anunciada. A taxa **efetiva** é a que o dinheiro realmente sente, depois da capitalização."
- "O cartão anuncia 2% ao mês. Parece pouco. Mas, capitalizado mês a mês, o ano vira 26,82%."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `1,02` `ENTER` `12` `y^x` `1` `−` `100` `×` | 🖥️ 26,82 | Taxa efetiva anual |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa efetiva é sempre igual à taxa nominal" | Errado | Só é igual sem capitalização no período |
| "2% ao mês capitalizados dão 24% ao ano efetivos" | Errado | São 26,82% |

> **Nominal é o que está no rótulo; efetiva é o que o dinheiro sente.**

**🔗 Ponte:** "Agora, o contrato: o preço fica fixo ou acompanha um índice?"

---

### Bloco 2 — O contrato: pré × pós — 4 min

- "Na **pré-fixada**, a taxa é conhecida na contratação. O investidor sabe o valor no vencimento."
- "Na **pós-fixada**, o rendimento está atrelado a um índice, como o CDI. O valor exato só se conhece no fim."
- "A **híbrida** combina as duas: uma parte fixa mais um índice, como o IPCA. Protege o poder de compra."

| Tipo | Quando se sabe o valor | Exemplo |
| --- | --- | --- |
| **Pré-fixada** | Na contratação | Título prefixado |
| **Pós-fixada** | No vencimento | CDB com 100% do CDI |
| **Híbrida** | Parte na contratação, parte no índice | Título atrelado ao IPCA com juro fixo |

- "Marta compara: a 12% fixo, ela sabe o que vai pagar. A 105% do CDI, depende do CDI do período."
- "O ponto de equilíbrio é um CDI de 11,43%. Se o CDI ficar acima, a pós-fixada custa mais; se ficar abaixo, custa menos."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `12` `ENTER` `1,05` `÷` | 🖥️ 11,43 | CDI de equilíbrio |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Na pós-fixada, o valor exato do rendimento só é conhecido no vencimento" | Certo | Slides A3472 p. 13 |
| "Título híbrido combina parte prefixada com parte pós-fixada" | Certo | Slides A3472 p. 13 |
| "A pós-fixada garante a rentabilidade nominal fixa" | Errado | Não garante |

> **Pré: sabe antes. Pós: sabe depois. Híbrida: um pouco de cada.**

**🔗 Ponte:** "Por último, a conta por dentro: simples ou composto?"

---

### Bloco 3 — Simples × composto, em uma linha — 2 min

- "Simples: o juro é sempre sobre o capital inicial. Composto: sobre o montante acumulado. Na G2 vimos o detalhe."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `8000` `ENTER` `1,5` `%` `18` `×` | 🖥️ 2.160,00 | Juros simples, em 18 meses |

- 🔇 Esse passo é a mesma conta da G2. Use só para lembrar a diferença.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Taxa proporcional aplica-se a juros compostos" | Errado | Só simples |
| "Juros compostos incidem sobre o montante acumulado" | Certo | Slides A3472 p. 5 |

> **Simples cresce pelo capital; composto cresce pelo que já cresceu.**

### Bloco 4 — Fechamento — 1 min

> **Rótulo: nominal e efetiva. Contrato: pré, pós ou híbrido. Conta: simples ou composto.**

- 🔇 Fechamento: "Antes de assinar, leia o rótulo (nominal ou efetiva), veja o contrato (pré, pós ou híbrido) e confirme a conta (simples ou composto)."

---

## Nota de verificação

- PD 1.3.4 a 1.3.4.3 lido no texto do repositório. Apostila p. 124–125 e slides A3472 lidos nesta sessão.
- Cálculos conferidos em Python: 1,02¹² − 1 = 26,82%; 12 ÷ 1,05 = 11,43%; 10.000 × 1,02¹² = 12.682,42; simples 12.400.
- Convenções: CDI de 9% e 14% e 105% do CDI (didáticos); cenário de cartão de 2% a.m.
- Números dos títulos prefixados e do IPCA+ do slide são datados e não foram usados.
