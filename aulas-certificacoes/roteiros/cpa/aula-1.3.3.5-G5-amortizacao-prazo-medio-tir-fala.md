# Roteiro de fala — Aula CPA: Amortização, Prazo Médio de Vencimento e Taxa Interna de Retorno (TIR)

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3.5**, **1.3.3.5.1** e **1.3.3.5.2**; slides A3475 p. 2–10; aula do repositório `aula-1.3-D-tir-cmpc-duration-retorno-payback`.

CPA 1.3.3.5 · 1.3.3.5.1 · 1.3.3.5.2 · Módulo 1 · **20 min** · Aula G5 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Tijolos do muro.** Cada pagamento de amortização tira tijolos da dívida. Quando o muro encolhe, os juros, que são o aluguel do tijolo que ainda está no muro, também caem.

**Onde a metáfora falha:** no sistema de amortização constante, os tijolos saem iguais. Na Price, a parte que amortiza muda a cada prestação. O muro não cobra juros, e a dívida não diminui fisicamente. Além disso, o prazo médio não é tempo de vida de nada.

### 🔇 Caso

**Joana** compra uma cafeteria por R$ 300.000, financiados a 10% a.a., com amortização de R$ 75.000 por ano. A loja gera caixa de 100, 120, 140 e 160 mil nos quatro anos.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3.5 Amortização | Slides A3475 p. 5; aula 1.3-D | Conferido; **periódica e única (bullet)** |
| 1.3.3.5.1 Prazo médio e vencimento | Slides A3475 p. 3; aula 1.3-D | Conferido; **prazo médio ≠ liquidez** |
| 1.3.3.5.2 TIR | Slides A3475 p. 2 | Conferido; regra de decisão |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3475 p. 3 | "Prazo médio está relacionado à liquidez do ativo" | Prazo médio mede quando o dinheiro volta; liquidez é a facilidade de vender antes do vencimento |
| 2 | Slides A3475 p. 3 | Prazo médio é "a base para o cálculo de Duration" | Correto. A G7 mostra a diferença: a duration pondera pelo valor presente |
| 3 | Slides A3475 p. 2 | "TIR > CMPC → investimento gera valor" | Correto, mas a TIR sozinha não diz quanto valor se gera; isso é o VPL (G3) |
| 4 | Slides A3475 p. 5 | "Amortização única (ex.: bullet)" | Bullet é amortização única no vencimento; não confundir com zero cupom (G3) |

### 🔇 Dados

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
| Prazo médio dos fluxos | (1×100 + 2×120 + 3×140 + 4×160) ÷ 520 = 1.400 ÷ 520 = **2,69 anos** |

🔇 A TIR de 23,96% é maior que os 10% do financiamento, e a CMPC de 13,58% (G6) é a exigência de retorno. Teclas de fluxo (`g CF0`, `g CFj`, `f IRR`) seguem a sequência padrão da HP12C: confirmar no equipamento antes de gravar.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso de Joana: os primeiros tijolos | 4 min |
| 2. Os juros caem com o muro | 4 min |
| 3. Centro de gravidade: prazo médio | 4 min |
| 4. Balança: TIR | 6 min |
| 5. Decisão: TIR e exigência | 2 min |
| **Total** | **20 min** |

---

## 3. Explicação em cinco blocos

### Bloco 1 — Caso de Joana: os primeiros tijolos — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular os juros do primeiro ano de um financiamento com amortização.

- "Joana financia trezentos mil reais da cafeteria a dez por cento ao ano. Ela vai pagar setenta e cinco mil de principal por ano, durante quatro anos."
- "Antes de calcular, duas palavras. **Amortização** é o pagamento que reduz o principal, a dívida em si. **Juros** é o custo do dinheiro emprestado, calculado sobre o saldo que ainda falta pagar."
- "No primeiro ano, o saldo é de trezentos mil. Os juros são dez por cento disso: trinta mil. O saldo cai para duzentos e vinte e cinco mil."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `300000` `ENTER` `10` `%` | 🖥️ 30.000,00 | Juros do ano 1 |

- **Erro comum:** achar que os juros são iguais em todos os anos, porque a taxa é a mesma. A taxa é a mesma, mas o saldo muda.

**🔗 Ponte:** "Se o saldo cai, os juros também caem. Vamos ver o segundo ano."

---

### Bloco 2 — Os juros caem com o muro — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue explicar por que os juros diminuem a cada ano na amortização constante.

- "No segundo ano, o saldo é de duzentos e vinte e cinco mil. Dez por cento disso dá vinte e dois mil e quinhentos. O terceiro ano dá quinze mil, e o quarto, sete mil e quinhentos. Cada tijolo que sai reduz o aluguel do que sobra."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `225000` `ENTER` `10` `%` | 🖥️ 22.500,00 | Juros do ano 2 |

- **Erro comum:** calcular os juros do ano 2 sobre os trezentos mil iniciais. Os juros incidem sobre o saldo que ainda falta.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Na amortização constante, os juros caem ao longo do tempo" | Certo | O saldo devedor cai |
| "Amortização única significa pagar o principal em parcelas iguais" | Errado | É o principal no vencimento |

**🔗 Ponte:** "Depois de tirar os tijolos, onde está o centro dos pagamentos no tempo?"

---

### Bloco 3 — Centro de gravidade: prazo médio — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o prazo médio dos recebimentos.

- "O **prazo médio** é o tempo médio em que o dinheiro volta, pesado pelo tamanho de cada recebimento. Pense numa balança: onde ela se equilibra no tempo."

| Ano (t) | Fluxo (mil reais) | t × fluxo |
| --- | --- | --- |
| 1 | 100 | 100 |
| 2 | 120 | 240 |
| 3 | 140 | 420 |
| 4 | 160 | 640 |
| **Soma** | **520** | **1.400** |

- "Prazo médio = mil e quatrocentos dividido por quinhentos e vinte: dois vírgula sessenta e nove anos."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1400` `ENTER` `520` `÷` | 🖥️ 2,69 | Prazo médio, em anos |

- **Erro comum:** dizer que prazo médio mede liquidez, ou seja, a facilidade de vender. Prazo médio mede quando o dinheiro volta.
- 🔇 Esta conta usa valores nominais. A duration (G7) usa valor presente.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Quanto maior o prazo médio, maior a sensibilidade à taxa de juros" | Certo | Slides A3475 p. 3 |
| "Prazo médio e liquidez são a mesma coisa" | Errado | Prazo médio mede quando o dinheiro volta |

**🔗 Ponte:** "Agora a balança: o investimento de trezentos mil volta com lucro?"

---

### Bloco 4 — Balança: TIR — 6 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular a TIR e explicar o que ela mede.

- "A **TIR** é a taxa que zera o VPL: a taxa em que o valor presente dos recebimentos iguala o investimento. É a taxa de equilíbrio da balança."
- "Joana investe trezentos mil e recebe cem, cento e vinte, cento e quarenta e cento e sessenta mil nos quatro anos. Qual é a taxa de equilíbrio?"

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `300000` `CHS` `g` `CF0` | 🖥️ −300.000,00 | Investimento inicial (fluxo zero) |
| 2 | ⌨️ `100000` `g` `CFj` `120000` `g` `CFj` `140000` `g` `CFj` `160000` `g` `CFj` | 🖥️ 160.000,00 | Fluxos dos anos 1 a 4 |
| 3 | ⌨️ `f` `IRR` | 🖥️ 23,96 | TIR, em % ao ano |

- "Vinte e três vírgula noventa e seis por cento ao ano. É o retorno que a cafeteria oferece sobre os trezentos mil."
- **Erro comum:** dizer que, como a TIR é 23,96%, Joana paga 23,96% de juros. Não paga. Ela paga dez por cento no financiamento. A TIR é o retorno do projeto, e não o custo da dívida.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A TIR é a taxa que zera o VPL" | Certo | Slides A3475 p. 2 |
| "Uma TIR de 23,96% significa que o financiamento custa 23,96%" | Errado | É o retorno do projeto |

**🔗 Ponte:** "Uma TIR alta é boa. Mas quanto ela precisa ser?"

---

### Bloco 5 — Decisão: TIR e exigência — 2 min

> **Objetivo deste bloco:** ao fim, o aluno consegue comparar a TIR com a exigência de retorno.

- "A cafeteria só cria valor se a TIR for maior que a exigência de retorno da empresa, que é a CMPC da G6: treze vírgula cinquenta e oito por cento."
- **Erro comum:** decidir só pela TIR, sem olhar o tamanho do valor criado. A TIR diz a taxa; o VPL diz o tamanho. Dois projetos com TIR parecida podem ter VPL bem diferente.

> **TIR diz a taxa; VPL diz o tamanho. A decisão precisa dos dois.**

- 🔇 **Fechamento:** "Amortizar é tirar tijolos; os juros caem com o muro; o prazo médio mostra quando o dinheiro volta; e a TIR é a taxa de equilíbrio, que se compara com a exigência." Próxima aula: G6, custo de oportunidade e CMPC.

---

## Lista de pegadinhas com nome

1. **Pegadinha do juro constante** — "Na amortização constante, os juros são iguais todo ano." Errado: caem com o saldo.
2. **Pegadinha do prazo médio-liquidez** — "Prazo médio mede a liquidez do ativo." Errado: mede quando o dinheiro volta.
3. **Pegadinha da TIR-juros** — "Com TIR de 23,96%, Joana paga 23,96% de juros." Errado: é o retorno do projeto; a dívida custa 10%.
4. **Pegadinha da TIR sozinha** — "TIR alta garante lucro grande." Errado: a TIR diz a taxa; o VPL diz o tamanho.

---

## Nota de verificação

- PD 1.3.3.5 a 1.3.3.5.2 lido no texto do repositório. Slides A3475 lidos nesta sessão.
- Cálculos conferidos em Python: TIR de −300.000 e fluxos 100, 120, 140 e 160 mil = 23,96%; juros 30.000, 22.500, 15.000 e 7.500; prazo médio 1.400 ÷ 520 = 2,69 anos.
- Convenções: financiamento de 10% a.a. e fluxos da cafeteria (didáticos).
- Revisão de estrutura: metáfora única (tijolos), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
