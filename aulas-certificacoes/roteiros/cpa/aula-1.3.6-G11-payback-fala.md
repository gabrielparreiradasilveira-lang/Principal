# Roteiro de fala — Aula CPA: Prazo de Retorno (Payback)

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), item **1.3.6**; slides A3477 p. 6–9 (conceito e exemplo de payback, integração com desconto comercial); aula do repositório `aula-1.3-D-tir-cmpc-duration-retorno-payback`.

CPA 1.3.6 · Módulo 1 · **10 min** · Aula G11 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula é um **barco que se paga**. O investimento é o custo de construir o barco. Cada mês de pescaria traz peixe para o caixa. O payback é o **tempo até o barco se pagar**. A armadilha é que o barco pode se pagar em quatro anos e continuar rendendo por vinte, e o payback não enxerga isso. Por isso a aula também mostra o **payback descontado**.

- Caso: uma **food truck de açaí**, com investimento de R$ 24.000 e entradas líquidas que crescem a cada ano.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.6 Payback | Slides A3477 p. 6–9 | Conferido; **versão simples e descontada** |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3477 p. 6 | Payback é "tempo necessário para recuperar o capital investido" | Correto, mas incompleto: o payback **simples** ignora o valor do dinheiro no tempo. Para decidir, use o **payback descontado** |
| 2 | Slides A3477 p. 8 | Máquina com lucro de R$ 5.000 por mês, custo de R$ 30.000 → 6 meses | Correto: 30.000 ÷ 5.000 = 6. Vale só porque o fluxo é constante |
| 3 | Slides A3477 p. 9 | "Sobra de R$ 15.500 de caixa" depois da máquina | Conta correta, mas mistura o payback com a antecipação de recebíveis (G10). Separar as decisões |
| 4 | Slides A3477 p. 6 | Payback como critério único | Não é critério de valor: um projeto pode ter payback curto e destruir valor (ver G5 e G6) |

### 🔇 Dados do exemplo (food truck)

| Ano | Entrada líquida | Acumulado (simples) | Desconto a 10% a.a. | Acumulado descontado |
| --- | --- | --- | --- | --- |
| 1 | 3.000 | 3.000 | 2.727,27 | 2.727,27 |
| 2 | 5.000 | 8.000 | 4.132,23 | 6.859,50 |
| 3 | 7.000 | 15.000 | 5.259,21 | 12.118,71 |
| 4 | 9.000 | **24.000** | 6.147,12 | 18.265,83 |
| 5 | 10.000 | 34.000 | 6.209,21 | 24.475,04 |

- **Payback simples:** exatamente **4 anos** (o acumulado chega a 24.000 no ano 4).
- **Payback descontado a 10% a.a.:** o acumulado descontado chega a 18.265,83 no ano 4 e a 24.475,04 no ano 5. Falta 5.734,17 no ano 5, e o fluxo do ano 5 descontado é 6.209,21. Logo, 4 + 5.734,17 ÷ 6.209,21 = **4,92 anos**.

🔇 O payback simples (4 anos) é menor que o descontado (4,92 anos), porque o desconto encarece os fluxos futuros. A diferença é a lição central da aula.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. O barco e o peixe: conceito de payback | 2 min |
| 2. A conta simples: 4 anos | 2 min |
| 3. O barco e o valor do tempo: payback descontado | 4 min |
| 4. Quando o payback engana | 2 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — O barco e o peixe: conceito de payback — 2 min

- "Payback é o tempo que o investimento leva para se pagar com os fluxos que ele gera."
- "Quanto menor o payback, mais rápido o dinheiro volta. É um indicador de liquidez do projeto."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Payback é o tempo necessário para recuperar o capital investido" | Certo | Slides A3477 p. 6 |
| "Payback menor significa projeto sempre mais rentável" | Errado | Payback não mede rentabilidade |

> **Payback é quanto tempo o barco leva para se pagar.**

**🔗 Ponte:** "A conta simples é a primeira que se faz. Vamos a ela."

---

### Bloco 2 — A conta simples: 4 anos — 2 min

- "A food truck investe 24.000. As entradas somam 3.000, 5.000, 7.000 e 9.000 nos quatro primeiros anos. No fim do ano 4, o acumulado chega a 24.000."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `3000` `ENTER` `5000` `+` `7000` `+` `9000` `+` | 🖥️ 24.000,00 | Soma dos quatro primeiros anos |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O payback simples desconta o valor do dinheiro no tempo" | Errado | Não desconta |
| "No payback simples, a food truck se paga no ano 4" | Certo | Acumulado de 24.000 no ano 4 |

> **Payback simples: soma até cobrir o investimento. Não desconta.**

**🔗 Ponte:** "Mas quatro anos de hoje valem o mesmo que quatro anos daqui a dez?"

---

### Bloco 3 — O barco e o valor do tempo: payback descontado — 4 min

- "Não valem. Um real de daqui a quatro anos vale menos que um real de hoje, por causa do custo de oportunidade (G6). O **payback descontado** traz cada fluxo para hoje antes de somar."
- "Com taxa de 10% a.a., o payback descontado é 4,92 anos. Quase um ano a mais que o simples."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `10000` `ENTER` `1,1` `ENTER` `5` `y^x` `÷` | 🖥️ 6.209,21 | Fluxo do ano 5 trazido a valor presente |
| 2 | ⌨️ `24000` `ENTER` `18265,83` `−` `6209,21` `÷` `4` `+` | 🖥️ 4,92 | Payback descontado, em anos |

- 🔇 No passo 2, `18265,83` é o acumulado descontado até o ano 4, que a tabela do bastidor mostra. Os fluxos anteriores somados com desconto dão esse valor.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O payback descontado é sempre menor que o payback simples" | Errado | É sempre **maior ou igual** |
| "O payback descontado considera o custo de oportunidade do dinheiro" | Certo | Desconto pela taxa |

> **Payback descontado: o barco se paga quando o dinheiro, trazido a hoje, cobre o investimento.**

**🔗 Ponte:** "E quando o payback engana?"

---

### Bloco 4 — Quando o payback engana — 2 min

- "O payback ignora o que vem depois de se pagar. Dois projetos com payback de 4 anos podem ter valor muito diferente se um tiver entradas de 10.000 por ano por dez anos e outro, de 3.000 por ano só até o ano 4."
- ➕ "Por isso a decisão precisa do VPL (G3) ou da TIR (G5). Payback é indicador de liquidez, não de valor."

> **Payback mede a liquidez; o valor está depois dele. Para decidir, use o VPL.**

- 🔇 Fechamento: "O barco se paga em quatro anos pela conta simples e em quase cinco pela descontada; o tempo tem preço; e o payback mede a pressa do dinheiro, não o valor do negócio."

---

## Nota de verificação

- PD 1.3.6 lido no texto do repositório. Slides A3477 p. 6–9 lidos nesta sessão.
- Cálculos conferidos em Python: acumulado simples 3.000, 8.000, 15.000, 24.000, 34.000; VP a 10%: 2.727,27; 4.132,23; 5.259,21; 6.147,12; 6.209,21; acumulado descontado até o ano 4 = 18.265,83; payback descontado = 4 + (24.000 − 18.265,83) ÷ 6.209,21 = 4,92 anos.
- Convenções: entradas da food truck e taxa de 10% a.a. (didáticas).
- Sem norma: payback é indicador de finanças clássicas.
