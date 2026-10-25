# Roteiro de fala — Aula CPA: Desconto Comercial, Aplicabilidade do Desconto Bancário e Desconto Bancário Simples

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.5** (taxa de desconto comercial), **1.3.8** (aplicabilidade do desconto bancário na antecipação de recebíveis) e **1.3.8.1** (desconto bancário simples); slides A3477 p. 3–9; aula do repositório `aula-1.3-B-capitalizacao-equivalencia-descontos`, que resolveu os exercícios do slide.

CPA 1.3.5 · 1.3.8 · 1.3.8.1 · Módulo 1 · **10 min** · Aula G10 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Vale-presente com desconto para troca antecipada.** Quem tem o vale (o título a receber) quer o dinheiro antes da validade, e o comprador desconta o vale para pagar à vista.

**Onde a metáfora falha:** o vale-presente tem valor fixo, e a loja que o emite é a mesma que o resgata. Na antecipação bancária, a nota depende do devedor: o banco cobra também pelo risco de quem vai pagar, e não só pelo prazo.

### 🔇 Caso

**Elisa** tem uma nota promissória de R$ 20.000, com vencimento em 60 dias. O banco oferece desconto de 2,5% a.m. Quanto ela recebe hoje, e qual é a taxa que está pagando de fato?

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.5 Taxa de desconto comercial | Slides A3477 p. 3–5 | Conferido; **base sobre o valor futuro** |
| 1.3.8 Desconto bancário na antecipação de recebíveis | Slides A3477 p. 9 | Conferido |
| 1.3.8.1 Desconto bancário simples | Slides A3477 p. 3–5 | Conferido; **equivale ao comercial simples** |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3477 p. 3 | Desconto comercial "pode superestimar o custo em prazos longos" | Incide sobre o valor futuro. A taxa efetiva da operação é maior que a anunciada, e a diferença cresce com o prazo |
| 2 | Slides A3472 p. 8 | "Desconto composto de 3% ao mês" (sem dizer qual) | Ambíguo: o racional composto e o comercial composto dão valores diferentes. Usa-se o racional composto, padrão para trazer a valor presente |
| 3 | Slides A3477 p. 4–5 | Marca comercial no exemplo | Trocada por "nota promissória" |
| 4 | Slides A3477 p. 3 | D = N × i × n | Correta para o comercial simples. O prazo e a taxa precisam estar na mesma unidade (meses) |

### 🔇 Dados

| Item | Valor |
| --- | --- |
| Valor nominal (N) | R$ 20.000 |
| Prazo (n) | 60 dias = 2 meses |
| Taxa anunciada (i) | 2,5% a.m. |
| Desconto comercial | 20.000 × 2,5% × 2 = **R$ 1.000,00** |
| Valor recebido hoje | **R$ 19.000,00** |
| Taxa efetiva da operação | (1.000 ÷ 19.000) ÷ 2 = **2,63% a.m.** |
| Racional composto: VP de 20.000 em 2 meses a 2,5% | 20.000 ÷ 1,025² = **R$ 19.036,29** |
| Desconto no racional composto | **R$ 963,71** |

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso de Elisa: a nota e o desconto | 3 min |
| 2. O custo real da operação | 3 min |
| 3. A antecipação no banco e o risco | 3 min |
| 4. Fechamento | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — Caso de Elisa: a nota e o desconto — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o valor recebido com desconto comercial simples.

- "Elisa tem uma nota de vinte mil reais, que vence daqui a sessenta dias. Ela quer o dinheiro hoje. O banco oferece desconto de dois e meio por cento ao mês."
- "A **nota promissória** é a promessa de pagamento futuro. O **valor nominal** é o número escrito nela. O **desconto** é o que o banco retém por adiantar o pagamento."
- "No desconto comercial, o banco calcula o desconto sobre o valor de face: vinte mil, vezes dois e meio por cento, vezes dois meses. Dá mil reais. Elisa recebe dezenove mil."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `20000` `ENTER` `2,5` `%` `2` `×` | 🖥️ 1.000,00 | Desconto comercial |
| 2 | ⌨️ `CHS` `20000` `+` | 🖥️ 19.000,00 | Valor recebido hoje |

- **Erro comum:** achar que, pagando dois e meio por cento ao mês, o custo da operação é dois e meio por cento. A conta mostra outra coisa, no próximo bloco.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O desconto comercial incide sobre o valor nominal do título" | Certo | Slides A3477 p. 3 |
| "O valor recebido no desconto comercial é o nominal menos o desconto" | Certo | Slides A3477 p. 5 |

**🔗 Ponte:** "Mas quanto Elisa está pagando de verdade?"

---

### Bloco 2 — O custo real da operação — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular a taxa efetiva de uma operação de desconto.

- "Elisa recebe dezenove mil e deve vinte mil em dois meses. A taxa efetiva é calculada sobre o dinheiro que ela efetivamente recebe, e não sobre o valor de face."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `1000` `ENTER` `19000` `÷` `2` `÷` `100` `×` | 🖥️ 2,63 | Taxa efetiva mensal da operação |

- "São dois vírgula sessenta e três por cento ao mês, e não dois e meio. O desconto incide sobre um valor futuro maior, mas o dinheiro que entra hoje é menor."
- **Erro comum:** tomar a taxa anunciada como o custo real. A diferença cresce quanto maior o prazo.
- ➕ "Se o banco usasse o racional composto, Elisa receberia dezenove mil e trinta e seis reais e vinte e nove centavos. O desconto cairia para novecentos e sessenta e quatro. Antes de aceitar, compare as duas bases."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa efetiva do desconto comercial é igual à taxa anunciada" | Errado | É maior, porque incide sobre o valor futuro |
| "O desconto racional composto é sempre igual ao comercial simples" | Errado | São bases diferentes |

**🔗 Ponte:** "E quando o banco faz isso todo dia, com muitos clientes, como na antecipação de recebíveis?"

---

### Bloco 3 — A antecipação no banco e o risco — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue identificar o que é antecipação de recebíveis e quem carrega o risco.

- "**Antecipação de recebíveis** é o banco comprar, com desconto, o que a empresa tem a receber: duplicatas, cheques, notas, faturas de cartão."
- "Na conta, o banco usa o desconto bancário simples, que é a mesma conta do comercial simples. O risco de quem vai pagar, porém, entra no preço."

| Ativo antecipado | Conta do desconto | Quem carrega o risco |
| --- | --- | --- |
| Nota promissória | Comercial simples | Quem antecipa, pelo preço |
| Cheque pré-datado | Bancário simples | Quem antecipa, pelo preço |
| Fatura de cartão | Bancário simples | Quem antecipa, com risco de estorno |

- **Erro comum:** achar que, na antecipação, o banco não cobra pelo risco do devedor, só pelo prazo. Cobra pelos dois.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Na antecipação de recebíveis, o banco compra o título com desconto" | Certo | Slides A3477 p. 9 |
| "O desconto bancário simples segue a mesma conta do comercial simples" | Certo | Aula 1.3-B |

> **Antecipar é vender o futuro com desconto: paga-se pelo tempo e pelo risco de quem vai pagar.**

**🔗 Ponte:** "Vamos fechar com a conta de Elisa, de ponta a ponta."

---

### Bloco 4 — Fechamento — 1 min

> **Objetivo deste bloco:** ao fim, o aluno consegue dizer por que o desconto anunciado não é o custo real.

> **Desconto comercial: sobre o valor de face. Taxa efetiva: sobre o dinheiro que se recebe.**

- 🔇 **Fechamento:** "Elisa paga dois e meio por cento ao mês no anúncio, e dois vírgula sessenta e três no cálculo, porque o desconto incide sobre o valor futuro." Próxima aula: G11, payback.

---

## Lista de pegadinhas com nome

1. **Pegadinha da taxa anunciada** — "Desconto de 2,5% ao mês custa 2,5% ao mês." Errado: a efetiva é 2,63%.
2. **Pegadinha do racional pelo comercial** — "Desconto racional e comercial dão o mesmo valor." Errado: as bases são diferentes; o racional dá 963,71 de desconto, e o comercial dá 1.000.
3. **Pegadinha do valor de face** — "O banco paga o valor escrito na nota." Errado: paga o valor de face menos o desconto.
4. **Pegadinha da unidade de prazo** — "O prazo de 60 dias entra na conta como 60 meses." Errado: são 2 meses, e a taxa está ao mês.

---

## Nota de verificação

- PD 1.3.5, 1.3.8 e 1.3.8.1 lidos no texto do repositório. Slides A3477 lidos nesta sessão.
- Cálculos conferidos em Python: 20.000 × 2,5% × 2 = 1.000; 20.000 − 1.000 = 19.000; (1.000 ÷ 19.000) ÷ 2 = 2,63% a.m.; 20.000 ÷ 1,025² = 19.036,29; desconto racional 963,71.
- Convenções: nota promissória de R$ 20.000 e taxa de 2,5% a.m. (didáticas).
- IOF sobre desconto de títulos citado de forma geral; alíquotas não reabertas.
- Revisão de estrutura: metáfora única (vale-presente), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
