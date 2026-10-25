# Roteiro de fala — Aula CPA: Desconto Comercial, Aplicabilidade do Desconto Bancário e Desconto Bancário Simples

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.5** (taxa de desconto comercial), **1.3.8** (aplicabilidade do desconto bancário na antecipação de recebíveis) e **1.3.8.1** (desconto bancário simples); slides A3477 p. 3–9 (desconto comercial, payback e integração); aula do repositório `aula-1.3-B-capitalizacao-equivalencia-descontos`, que resolveu os exercícios do slide.

CPA 1.3.5 · 1.3.8 · 1.3.8.1 · Módulo 1 · **10 min** · Aula G10 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula é um **vale-presente com desconto para troca antecipada**. Quem tem o vale (o título a receber) quer o dinheiro antes da validade. O banco compra o vale com desconto. O desconto é a taxa pela antecipação. O caso é o de uma **pequena confeitaria** que antecipa uma nota promissória de encomenda corporativa.

- Caso: **Elisa** tem uma nota promissória de R$ 20.000 com vencimento em 60 dias. O banco oferece 2,5% a.m. de desconto. Quanto ela recebe hoje, e qual é a taxa real que está pagando?

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.5 Taxa de desconto comercial | Slides A3477 p. 3–5 | Conferido; **base sobre o valor futuro** |
| 1.3.8 Desconto bancário na antecipação de recebíveis | Slides A3477 p. 9 | Conferido |
| 1.3.8.1 Desconto bancário simples | Slides A3477 p. 3–5 | Conferido; **equivale ao comercial simples** |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3477 p. 3 | Desconto comercial "pode superestimar o custo em prazos longos" | Mais preciso: incide sobre o **valor futuro**. A taxa **efetiva** da operação é **maior** que a taxa anunciada, e a diferença cresce com o prazo |
| 2 | Slides A3472 p. 8 | "Desconto composto de 3% ao mês" (sem dizer qual) | Ambíguo: o **racional composto** e o **comercial composto** dão valores diferentes. Esta aula usa o racional composto, padrão de mercado para trazer a valor presente |
| 3 | Slides A3477 p. 4–5 | Marca comercial no exemplo | Trocada por "nota promissória" (genérico) |
| 4 | Slides A3477 p. 3 | Fórmula D = N × i × n | Correta para o comercial simples. Com "n" em meses, a taxa precisa estar em % ao mês |

### 🔇 Dados do exemplo (Elisa)

| Item | Valor |
| --- | --- |
| Valor nominal (N) | R$ 20.000 |
| Prazo (n) | 60 dias = 2 meses |
| Taxa (i) | 2,5% a.m. |
| Desconto comercial (D = N × i × n) | 20.000 × 2,5% × 2 = **R$ 1.000,00** |
| Valor recebido hoje (comercial) | **R$ 19.000,00** |
| Taxa efetiva da operação (sobre o dinheiro recebido) | (1.000 ÷ 19.000) ÷ 2 = **2,63% a.m.** |
| Racional composto: VP de 20.000 em 2 meses a 2,5% | 20.000 ÷ 1,025² = **R$ 19.036,29** |
| Desconto no racional composto | **R$ 963,71** |

🔇 Por isso a efetiva (2,63%) é maior que 2,5%: o desconto incide sobre o valor **futuro**, mas o dinheiro recebido é o **valor presente**.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. O vale-presente: o desconto comercial | 3 min |
| 2. Quanto o banco realmente cobra | 3 min |
| 3. A antecipação de recebíveis no banco | 3 min |
| 4. Fechamento | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — O vale-presente: desconto comercial — 3 min

- "O desconto comercial é calculado sobre o **valor nominal**, o valor de face do título: D = N × i × n."
- "Se Elisa antecipa 20 mil a 2,5% ao mês, por dois meses, o banco desconta 1.000 reais e paga 19.000."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `20000` `ENTER` `2,5` `%` `2` `×` | 🖥️ 1.000,00 | Desconto comercial |
| 2 | ⌨️ `CHS` `20000` `+` | 🖥️ 19.000,00 | Valor recebido hoje |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O desconto comercial incide sobre o valor nominal do título" | Certo | Slides A3477 p. 3 |
| "O valor recebido no desconto comercial é o nominal menos o desconto" | Certo | Slides A3477 p. 5 |

> **Desconto comercial: sobre o valor de face, do jeito que está escrito no título.**

**🔗 Ponte:** "Mas quanto o banco cobra de verdade?"

---

### Bloco 2 — Quanto o banco realmente cobra — 3 min

- ✏️ "O desconto de 2,5% ao mês não é a taxa que Elisa paga. Ela recebe 19.000 e deve 20.000 em dois meses."
- "Sobre o dinheiro que recebeu, a taxa é de 2,63% ao mês. O desconto sobre o valor de face esconde uma taxa maior."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `1000` `ENTER` `19000` `÷` `2` `÷` `100` `×` | 🖥️ 2,63 | Taxa efetiva mensal da operação |

- ➕ "No racional composto, o banco trocaria 20.000 em dois meses por 19.036,29 hoje. Então, a taxa de desconto de 2,5% a.m. no racional daria um desconto de 963,71. O comercial, com o mesmo 2,5%, cobra mais. Compare as duas bases antes de aceitar a oferta."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa efetiva do desconto comercial é igual à taxa de desconto anunciada" | Errado | É maior, porque incide sobre o valor futuro |
| "O desconto racional composto é sempre igual ao comercial simples" | Errado | São bases diferentes |

> **Desconto sobre o valor de face esconde uma taxa maior sobre o dinheiro recebido.**

**🔗 Ponte:** "E quando o banco faz isso de forma recorrente, como na antecipação de recebíveis?"

---

### Bloco 3 — A antecipação de recebíveis no banco — 3 min

- "Antecipação de recebíveis é o banco comprar, com desconto, o que você tem a receber: duplicatas, cheques, notas, faturas de cartão."
- "O banco aplica o desconto bancário simples: a mesma conta do comercial. O risco do devedor, porém, pode entrar no preço."

| Ativo antecipado | Desconto | Quem paga o risco |
| --- | --- | --- |
| Nota promissória | Desconto comercial simples | Elisa, na taxa |
| Cheque pré-datado | Desconto bancário simples | Elisa, na taxa |
| Fatura de cartão | Desconto bancário simples | Elisa, na taxa, com risco de chargeback |

- 🔇 A tabela assume que o risco do emissor não muda o cálculo. Na prática, a instituição pode cobrar mais por devedores de risco maior.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Na antecipação de recebíveis, o banco compra o título com desconto" | Certo | Slides A3477 p. 9 |
| "O desconto bancário simples segue a mesma lógica do comercial simples" | Certo | Aula 1.3-B |

> **Antecipar é vender o futuro com desconto. Quem recebe antes paga pelo tempo e pelo risco.**

**🔗 Ponte:** "Fechamos com a conta da Elisa, de ponta a ponta."

---

### Bloco 4 — Fechamento — 1 min

> **Comercial: sobre o valor de face. Efetiva: sobre o dinheiro que se recebe.**

- 🔇 Fechamento: "O desconto comercial de 2,5% ao mês, sobre 20.000 em dois meses, custa a Elisa 2,63% ao mês, porque incide sobre o valor futuro e não sobre o dinheiro de hoje."

---

## Nota de verificação

- PD 1.3.5, 1.3.8 e 1.3.8.1 lidos no texto do repositório. Slides A3477 lidos nesta sessão.
- Cálculos conferidos em Python: 20.000 × 2,5% × 2 = 1.000; 20.000 − 1.000 = 19.000; (1.000 ÷ 19.000) ÷ 2 = 2,63% a.m.; 20.000 ÷ 1,025² = 19.036,29.
- Convenções: nota promissória de R$ 20.000 e taxa de 2,5% a.m. (didática); a tabela de tipos de ativo não é regra de norma.
- Incidência de IOF sobre desconto de títulos citada de forma geral; alíquotas não reabertas.
