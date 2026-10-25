# Roteiro de fala — Aula CPA: Taxas de Juros — Efetiva, Prefixada × Pós-Fixada, Juros Simples × Compostos

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.4**, **1.3.4.1** (nominal, efetiva e real), **1.3.4.2** (prefixada e pós-fixada) e **1.3.4.3** (juros simples e compostos); APOSTILA-CPA p. 123–125; slides A3472 p. 4–13; aula do repositório `aula-1.3-A-taxas-nominal-efetiva-real-indexador`.

CPA 1.3.4 · 1.3.4.1 · 1.3.4.2 · 1.3.4.3 · Módulo 1 · **10 min** · Aula G9 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Contrato de aluguel.** Há dois tipos: o aluguel de valor fixo, que não muda durante o contrato (pré-fixado), e o aluguel reajustado por um índice (pós-fixado). A escolha entre eles é a escolha de quem aceita o risco do índice.

**Onde a metáfora falha:** o aluguel reajustado tem periodicidade e teto definidos por lei. O CDI não é um índice de reajuste de aluguel. E o contrato de aluguel não tem o risco de crédito de um título: o inquilino paga, ou não paga, e o investidor no título também depende do emissor.

### 🔇 Caso

**Marta** tem R$ 10.000 para aplicar e duas opções: um título que paga 12% a.a. fixo, ou um que paga 105% do CDI.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.4.1 Nominal, efetiva e real | Slides A3472 p. 5–11; apostila p. 124 | Conferido; **efetiva ilustrada** |
| 1.3.4.2 Prefixada e pós-fixada | Slides A3472 p. 13 | Conferido; **híbrida incluída** |
| 1.3.4.3 Simples e compostos | Slides A3472 p. 3–5 | Conferido; resumido |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3472 p. 13 | "Tesouro Prefixado 2027 pagando 10,50% a.a." | Número datado. Ensina-se o conceito |
| 2 | Slides A3472 p. 13 | Pós-fixada: "CDB que paga 100% do CDI" | Correto. O rendimento depende do CDI efetivo; não há nominal fixa garantida |
| 3 | Apostila p. 124 | "Taxa efetiva: 10% ao ano, ou 1% ao mês" | Não confundir: a efetiva reflete a capitalização e pode ser maior que a nominal |
| 4 | Slides A3472 p. 4 | "Taxa proporcional: 2% ao mês → 24% ao ano" | Vale só no simples. Em composto, a efetiva anual é 26,82% |
| 5 | Slides A3472 p. 13 | "Taxa híbrida: Tesouro IPCA+ paga 5,50% + IPCA" | Correto na estrutura; o nome e o número são datados |

### 🔇 Dados

| Item | Valor |
| --- | --- |
| Opção A: taxa fixa | 12% a.a. |
| Opção B: 105% do CDI | Com CDI de 9%, rende 9,45%; com CDI de 14%, rende 14,70% |
| Ponto de equilíbrio | CDI de **11,43%** a.a. (12 ÷ 1,05) |
| Cartão: taxa nominal | 2% a.m. |
| Cartão: taxa efetiva anual | 1,02¹² − 1 = **26,82%** a.a. |
| R$ 10.000 a 2% a.m., 12 meses: simples | **R$ 12.400** |
| R$ 10.000 a 2% a.m., 12 meses: composto | **R$ 12.682,42** |

🔇 Valores hipotéticos. Não há produto específico.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso de Marta: fixo ou pelo CDI | 3 min |
| 2. O equilíbrio entre as duas opções | 2 min |
| 3. O rótulo do cartão: nominal e efetiva | 3 min |
| 4. Simples e composto, em uma conta | 1 min |
| 5. Fechamento | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — Caso de Marta: fixo ou pelo CDI — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue distinguir taxa pré-fixada, pós-fixada e híbrida.

- "Marta tem dez mil reais e duas opções. A primeira paga doze por cento ao ano, fixo. Ela sabe, desde o começo, quanto terá no vencimento. Esse é o **pré-fixado**."
- "A segunda paga cento e cinco por cento do **CDI**, uma taxa de referência do mercado. O valor exato só se conhece no fim. Esse é o **pós-fixado**."
- "Uma terceira forma mistura as duas: uma parte fixa mais um índice, como o IPCA. Chama-se **híbrido**."
- **Erro comum:** achar que o pós-fixado sempre rende mais, por ser atrelado a um índice que sobe. Depende do que o índice fizer.

| Tipo | Quando se sabe o valor | Exemplo |
| --- | --- | --- |
| **Pré-fixado** | Na contratação | Título com taxa fixa |
| **Pós-fixado** | No vencimento | CDB com 100% do CDI |
| **Híbrido** | Parte na contratação, parte no índice | Título atrelado ao IPCA com juro fixo |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Na pós-fixada, o valor exato do rendimento só é conhecido no vencimento" | Certo | Slides A3472 p. 13 |
| "A pós-fixada garante a rentabilidade nominal fixa" | Errado | Não garante |

**🔗 Ponte:** "Então, com que CDI a opção de Marta empata com a de doze por cento?"

---

### Bloco 2 — O equilíbrio entre as duas opções — 2 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o ponto de equilíbrio entre uma taxa fixa e uma taxa atrelada a um percentual do CDI.

- "Marta empata se o CDI ficar em onze vírgula quarenta e três por cento. Acima disso, a opção pós rende mais. Abaixo, rende menos."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `12` `ENTER` `1,05` `÷` | 🖥️ 11,43 | CDI de equilíbrio |

- **Erro comum:** comparar 12% com 105% de qualquer CDI, sem perguntar qual é o CDI. A conta só faz sentido com um CDI estimado.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Com CDI acima do ponto de equilíbrio, a opção pós-fixada rende mais" | Certo | 105% do CDI supera 12% |

**🔗 Ponte:** "E o rótulo do cartão de crédito? Ali a taxa está em outra unidade."

---

### Bloco 3 — O rótulo do cartão: nominal e efetiva — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue converter uma taxa mensal capitalizada em taxa anual efetiva.

- "O cartão anuncia dois por cento ao mês. Esse é o valor **nominal**: o número do rótulo. A taxa **efetiva** é a que o dinheiro realmente sente, com os juros caindo sobre os juros de cada mês."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `1,02` `ENTER` `12` `y^x` `1` `−` `100` `×` | 🖥️ 26,82 | Taxa efetiva anual |

- "Dois por cento ao mês parecem vinte e quatro por ano. Mas o juro de cada mês entra na base do mês seguinte. O ano custa vinte e seis vírgula oitenta e dois."
- **Erro comum:** multiplicar dois por doze e dizer que o ano custa vinte e quatro. Esse erro subestima o custo do cartão em mais de dois pontos.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa efetiva é sempre igual à nominal" | Errado | Só é igual sem capitalização no período |
| "Dois por cento ao mês capitalizados dão vinte e quatro por cento ao ano efetivos" | Errado | São 26,82% |

**🔗 Ponte:** "Por último, a diferença entre juro simples e juro composto, em uma só conta."

---

### Bloco 4 — Simples e composto, em uma conta — 1 min

> **Objetivo deste bloco:** ao fim, o aluno lembra por que o regime muda o resultado no mesmo prazo.

- "Dez mil reais a dois por cento ao mês, durante doze meses. No simples, o juro é sobre o capital: doze mil e quatrocentos. No composto, o juro entra no saldo: doze mil seiscentos e oitenta e dois."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `1,02` `ENTER` `12` `y^x` `10000` `×` | 🖥️ 12.682,42 | Montante composto |

- **Erro comum:** achar que os dois regimes dão o mesmo resultado em doze meses. Não dão: a diferença vem do juro sobre juro.

> **Simples cresce pelo capital; composto cresce pelo que já cresceu.**

### Bloco 5 — Fechamento — 1 min

- 🔇 **Fechamento:** "Antes de assinar, leia o rótulo: a taxa nominal pode esconder a efetiva. Veja o contrato: fixo, pelo índice ou híbrido. E confirme a conta: simples ou composto." Próxima aula: G10, desconto comercial e bancário.

---

## Lista de pegadinhas com nome

1. **Pegadinha do pós sempre melhor** — "A pós-fixada sempre rende mais." Errado: depende do CDI que ocorrer.
2. **Pegadinha da multiplicação da taxa mensal** — "Dois por cento ao mês são vinte e quatro por cento ao ano efetivos." Errado: a efetiva é 26,82%.
3. **Pegadinha do fixo garantido** — "A pós-fixada garante a taxa nominal fixa." Errado: o rendimento acompanha o índice.
4. **Pegadinha do regime escondido** — "No mesmo prazo e taxa, simples e composto dão o mesmo resultado." Errado: o juro sobre juro muda o montante.

---

## Nota de verificação

- PD 1.3.4 a 1.3.4.3 lido no texto do repositório. Apostila p. 124–125 e slides A3472 lidos nesta sessão.
- Cálculos conferidos em Python: 1,02¹² − 1 = 26,82%; 12 ÷ 1,05 = 11,43%; 10.000 × 1,02¹² = 12.682,42; simples 12.400.
- Convenções: CDI de 9% e 14% e 105% do CDI (didáticos); cartão a 2% a.m.
- Números dos títulos prefixados e do IPCA+ do slide são datados e não foram usados.
- Revisão de estrutura: metáfora única (contrato de aluguel), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
