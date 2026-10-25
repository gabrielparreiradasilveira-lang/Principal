# Roteiro de fala — Aula CPA: Custo de Oportunidade, Taxa Livre de Risco e CMPC

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3.5.3**, **1.3.3.5.4** e **1.3.3.5.5**; slides A3474 p. 6 (taxa de desconto) e A3475 p. 4 (CMPC); aula do repositório `aula-1.3-D-tir-cmpc-duration-retorno-payback`.

CPA 1.3.3.5.3 · 1.3.3.5.4 · 1.3.3.5.5 · Módulo 1 · **10 min** · Aula G6 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula é uma **mistura de cafés**. O CMPC é o **preço médio do pote**: cada tipo de café (dinheiro próprio, dinheiro emprestado) tem um preço, e o pote tem o preço médio ponderado pela quantidade. O custo de oportunidade é o **café que você deixou no balcão** ao escolher outro. A taxa livre de risco é o **café de referência** que todo mundo conhece.

- Caso: uma rede de **cafeterias** com 70% de capital próprio e 30% de dívida. Quanto custa, em média, cada real que a rede usa?

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3.5.3 Custo de oportunidade | Slides A3474 p. 6 | Conferido |
| 1.3.3.5.4 Taxa livre de risco | Slides A3474 p. 6 | **Número datado retirado**; conceito mantido |
| 1.3.3.5.5 CMPC | Slides A3475 p. 4 | Conferido; **fórmula com IR sobre a dívida** |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3474 p. 6 | Taxa livre de risco = "Selic Meta (15%)" | Número datado, retirado. Conceito: o retorno de um título público de prazo equivalente, sem risco de crédito |
| 2 | Slides A3474 p. 6 | "Custo de oportunidade: comparação com CDB de grandes instituições" | Correto como exemplo de baixo risco, mas o custo de oportunidade é **o melhor retorno que se abre mão**, e pode ser qualquer alternativa de risco equivalente |
| 3 | Slides A3475 p. 4 | CMPC "é o mínimo que um projeto deve render" | Correto. A regra completa usa o custo **após IR** da dívida, porque o juro é dedutível. O slide omite essa parte |
| 4 | Slides A3475 p. 4 | "É o custo do dinheiro da empresa" | Correto como resumo; a fórmula é média ponderada pelos pesos de capital próprio e de terceiros |

### 🔇 Dados do exemplo (cafeterias)

| Item | Valor |
| --- | --- |
| Peso do capital próprio | 70%, com custo de 16% a.a. |
| Peso da dívida | 30%, com custo de 12% a.a. antes do IR |
| Alíquota de IR sobre a dívida | 34% (hipótese do slide A3475) |
| Custo da dívida após IR | 12% × (1 − 0,34) = **7,92% a.a.** |
| CMPC | 70% × 16% + 30% × 7,92% = **13,58% a.a.** |
| Custo de oportunidade do café de referência | Título de risco equivalente, rendendo 13% a.a. (hipótese) |

🔇 Os números 70/30, 16%, 12% e 34% são do slide e servem como estrutura. A taxa de 16% sobre o capital próprio é a exigência de retorno dos acionistas, não um valor de mercado.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. O café de referência e a taxa livre de risco | 2 min |
| 2. O café deixado no balcão: custo de oportunidade | 2 min |
| 3. O pote de café: a conta do CMPC | 5 min |
| 4. Fechamento: a régua da decisão | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — O café de referência: taxa livre de risco — 2 min

- "Taxa livre de risco é o retorno de um investimento sem risco de crédito, de prazo equivalente. É o café de referência: todo mundo sabe o sabor."
- ✏️ "Muitos materiais citam a Selic com um número fixo. Ela muda. Guarde o conceito, não o número."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa livre de risco é aquela sem risco de crédito, de prazo equivalente" | Certo | Conceito |
| "A taxa livre de risco é um valor fixo que a CVM publica" | Errado | Varia com o mercado |

> **Taxa livre de risco: o café de referência. Sem risco de crédito, prazo equivalente.**

**🔗 Ponte:** "E quando você escolhe um café, deixa outros no balcão. Isso é o custo de oportunidade."

---

### Bloco 2 — O café deixado no balcão: custo de oportunidade — 2 min

- "Custo de oportunidade é o retorno da melhor alternativa que você **não** escolheu, de risco comparável."
- "Se a cafeteria usa o dinheiro numa loja nova, ela deixa de ganhar o que ganharia em um título de 13%. Esse é o custo."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O custo de oportunidade é a melhor alternativa que se abre mão, de risco comparável" | Certo | Slides A3474 p. 6 |
| "O custo de oportunidade é sempre igual à taxa livre de risco" | Errado | É a alternativa de risco comparável, que pode ser maior |

> **Custo de oportunidade é o café que você deixou no balcão.**

**🔗 Ponte:** "Agora, misturar o dinheiro próprio com o emprestado."

---

### Bloco 3 — O pote de café: a conta do CMPC — 5 min

- "CMPC é o **custo médio ponderado de capital**: o preço médio do pote, pesado pela quantidade de cada tipo de café."
- "O café do capital próprio custa 16%. O café da dívida custa 12%, mas o imposto reduz esse custo para 7,92%, porque o juro é dedutível."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `0,7` `ENTER` `16` `×` | 🖥️ 11,20 | Contribuição do capital próprio |
| 2 | ⌨️ `0,3` `ENTER` `12` `×` `0,66` `×` | 🖥️ 2,38 | Contribuição da dívida após IR |
| 3 | ⌨️ `+` | 🖥️ 13,58 | CMPC em % ao ano |

- 🔇 No passo 2, `0,66` é 1 − 34%. Usar a alíquota direta (34%) é outro caminho que dá o mesmo resultado.
- ➕ "Se a alíquota de IR não existisse, o custo da dívida seria 12% e o CMPC subiria para 14,4%. O imposto é um desconto real no custo do dinheiro."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O IR reduz o custo efetivo da dívida na CMPC" | Certo | Juros são dedutíveis |
| "Na CMPC, o custo do capital próprio entra sem ponderação" | Errado | Entra com o peso de 70% |

> **CMPC: o preço médio do pote, com o imposto descontando o café da dívida.**

**🔗 Ponte:** "O CMPC é a régua de corte de um projeto. Como a régua se usa?"

---

### Bloco 4 — Fechamento: a régua da decisão — 1 min

- "Se a TIR do projeto (G5) for maior que o CMPC, o projeto gera valor. Se for menor, destrói."
- "A taxa livre de risco é o piso de comparação; o custo de oportunidade, a alternativa; e o CMPC, a régua de corte."

> **Taxa livre de risco é o piso; custo de oportunidade é a alternativa; CMPC é a régua de corte.**

- 🔇 Fechamento: "O café de referência, o café do balcão e o pote de café misturam as três ideias: piso, alternativa e régua de corte."

---

## Nota de verificação

- PD 1.3.3.5.3 a 1.3.3.5.5 lido no texto do repositório. Slides A3474 e A3475 lidos nesta sessão.
- Cálculos conferidos em Python: 12% × (1 − 0,34) = 7,92%; 0,7 × 16 + 0,3 × 7,92 = 13,576 ≈ 13,58%; sem IR, 0,7 × 16 + 0,3 × 12 = 14,4%.
- Convenções: pesos 70/30, custos de 16% e 12%, alíquota de 34% (slide) e a taxa de 13% para o título de referência (hipótese).
- Sem norma específica: CMPC é conceito de finanças corporativas clássico. A taxa livre de risco não foi reaberta com número vigente.
