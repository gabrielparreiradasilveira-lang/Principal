# Roteiro de fala — Aula CPA: Sistemas de Amortização — SAC (Constante) e Price (Francês)

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), item **1.3.7**; slides A3478 (SAC, com parcela, amortização e exercício) e A3479 (Tabela Price, fórmula e exemplo); APOSTILA-CPA p. 144–148; aula do repositório `aula-1.3-E-sac-price`, que resolveu os exercícios.

CPA 1.3.7 · Módulo 1 · **20 min** · Aula G12 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula é um **bolo servido em fatias**. O SAC são **fatias de tamanho igual**: a amortização é sempre a mesma, e os juros caem à medida que o bolo diminui. A Price é a **prestação de aluguel**: o pagamento total é sempre o mesmo, mas por dentro a parte que amortiza cresce e a parte de juros diminui. A pergunta da aula: qual dos dois custa mais no total, e por quê?

- Caso: **Lucas** financia R$ 60.000 em 12 meses, a 1,8% a.m., e quer escolher entre o SAC e a Price.

🔇 O slide de SAC usa 100.000 em 10 parcelas semestrais. O slide da Price usa 100.000 em 10 semestres e uma questão de banco. A aula usa outro valor, outro prazo e outra taxa.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.7 Sistemas de amortização (SAC e Price) | Slides A3478 p. 3–9; slides A3479 p. 3–9; apostila p. 144–148 | Conferido; **taxa equivalente semestral** e **parcela da SAC** |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Apostila p. 144 | 30% a.a. equivale a "14,18% ao semestre" | **14,0175%** (1,30^0,5 − 1). A própria apostila (p. 148) e o slide A3478 p. 6 trazem o valor certo |
| 2 | Slides A3479 p. 3 | Price "é mais cara para o tomador" | Com a **mesma taxa**, a Price paga **mais juros no total**, porque amortiza mais devagar no começo. O **valor presente** da dívida é o mesmo, pois a taxa é a mesma. "Mais cara" vale para o total de juros pagos |
| 3 | Slides A3479 p. 3 | "Menor vantagem de se antecipar as parcelas" | Correto na intuição: como os juros caem devagar, quitar antes economiza menos juros no início. Mas depende do prazo |
| 4 | Slides A3478 p. 4 | "A amortização é sempre a mesma: divide o saldo pelo número de parcelas" | Correto. Mas o saldo que se divide é o **saldo devedor do início** do período. A SAC tem juros sobre saldo, e a parcela cai com o saldo |
| 5 | Slides A3479 p. 8–9 | Questão de banco (11168) | **Substituída** por exemplo inédito (padrão do projeto) |

### 🔇 Dados do exemplo (Lucas)

| Item | Valor |
| --- | --- |
| Financiamento | R$ 60.000 |
| Prazo | 12 meses |
| Taxa | 1,8% a.m. |
| Amortização mensal no SAC | 60.000 ÷ 12 = **R$ 5.000** |
| Parcela 1 no SAC | 5.000 + 60.000 × 1,8% = **R$ 6.080** |
| Parcela 7 no SAC | Saldo antes da 7ª = 30.000 → juros 540 → **R$ 5.540** |
| Parcela 12 no SAC | 5.000 + 5.000 × 1,8% = **R$ 5.090** |
| Total pago no SAC | **R$ 67.020** (juros de R$ 7.020) |
| Parcela constante na Price | 60.000 × 1,8% ÷ (1 − 1,018⁻¹²) = **R$ 5.604,12** |
| Total pago na Price | 5.604,12 × 12 = **R$ 67.249,42** (juros de R$ 7.249,42) |
| Diferença de juros | Price paga **R$ 229,42 a mais** no total |

🔇 A parcela da Price é menor que a do SAC no início (5.604 contra 6.080), e maior no fim (5.604 contra 5.090). A soma dá a diferença.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. O bolo em fatias iguais: SAC | 6 min |
| 2. A prestação fixa: Price | 6 min |
| 3. Comparação: quem custa mais | 5 min |
| 4. Fechamento | 3 min |
| **Total** | **20 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — O bolo em fatias iguais: SAC — 6 min

- "No SAC, a amortização é fixa: divide-se o saldo pelo número de parcelas. Lucas paga 5.000 de principal por mês, sempre."
- "Os juros incidem sobre o saldo devedor, que diminui. Por isso, a parcela também diminui: é a fatia de juros que encolhe."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `60000` `ENTER` `12` `÷` | 🖥️ 5.000,00 | Amortização mensal no SAC |
| 2 | ⌨️ `60000` `ENTER` `1,8` `%` `5000` `+` | 🖥️ 6.080,00 | Parcela 1 (principal + juros do primeiro saldo) |

🔇 Passo 2: `60000 ENTER 1,8 %` dá 1.080 de juros. O `+` soma 5.000 e chega a 6.080. Para a parcela 7, use o saldo de 30.000: `30000 ENTER 1,8 % 5000 +` dá 5.540.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "No SAC, a amortização é constante e a parcela diminui ao longo do tempo" | Certo | Slides A3478 p. 4 |
| "No SAC, os juros são calculados sobre o valor inicial do financiamento" | Errado | Incidem sobre o **saldo devedor** |

> **SAC: fatia de principal igual; juro cai; a parcela cai junto.**

**🔗 Ponte:** "E a Price? É a prestação que não muda."

---

### Bloco 2 — A prestação fixa: Price — 6 min

- "Na Price, a **parcela é constante**. Por dentro, porém, a parte que amortiza cresce e a parte de juros diminui. A soma é sempre a mesma."
- ✏️ "O slide diz que a Price 'é mais cara para o tomador'. Com a mesma taxa, o valor presente é igual. O que é maior é o **total de juros pagos**, porque a Price amortiza mais devagar no início."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `60000` `CHS` `PV` `1,8` `i` `12` `n` `PMT` | 🖥️ 5.604,12 | Parcela constante da Price |
| 2 | ⌨️ `RCL` `PMT` `12` `×` | 🖥️ 67.249,42 | Total pago na Price |

- 🔇 A fórmula está nos slides: PMT = PV × i ÷ (1 − (1+i)^−n). O passo 1 da HP12C faz a mesma conta.
- ➕ "Repare: na Price, o principal da primeira parcela é 5.604,12 − 1.080 = 4.524,12. O SAC, no mesmo mês, amortiza 5.000."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Na Price, a parcela é constante e os juros diminuem ao longo do tempo" | Certo | Slides A3479 p. 4 |
| "Com a mesma taxa, a Price tem valor presente diferente do SAC" | Errado | O valor presente é o mesmo |

> **Price: parcela fixa; por dentro, mais principal a cada mês.**

**🔗 Ponte:** "Afinal, qual dos dois custa mais?"

---

### Bloco 3 — Comparação: quem custa mais — 5 min

| Critério | SAC | Price |
| --- | --- | --- |
| Primeira parcela | **R$ 6.080** (mais alta) | R$ 5.604 |
| Última parcela | **R$ 5.090** (mais baixa) | R$ 5.604 |
| Total de juros | **R$ 7.020** | R$ 7.249 |
| Amortização no início | Maior | Menor |

- "O SAC custa **menos** no total, porque amortiza mais cedo. A Price custa mais no total, mas a parcela inicial é menor. Para quem tem fôlego no início, o SAC economiza. Para quem precisa de parcela leve no começo, a Price ajuda."
- ✏️ "Atenção: no valor presente, a dívida é a mesma. A diferença real é o **fluxo** de pagamentos."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O SAC tem total de juros menor que a Price para a mesma taxa e prazo" | Certo | Amortiza mais cedo |
| "A Price tem primeira parcela menor que a do SAC" | Certo | Por dentro, a Price mistura principal e juros |

> **Mesma taxa, mesmo prazo: o SAC paga menos juros no total; a Price paga parcela leve no começo.**

**🔗 Ponte:** "Vamos fechar com o que Lucas deveria escolher."

---

### Bloco 4 — Fechamento — 3 min

- "Se Lucas consegue pagar 6.080 no primeiro mês, o SAC é mais barato. Se a parcela precisa caber em 5.600 desde o início, a Price é a escolha."
- ➕ "Em qualquer dos dois, a taxa anunciada precisa ser comparada pelo CET, como vimos na F6. O sistema de amortização não substitui a conta do custo efetivo."

> **Sistema de amortização muda o fluxo; a conta do custo efetivo continua sendo a referência.**

- 🔇 Fechamento: "O SAC é o bolo em fatias iguais: paga menos juros e tem primeira parcela alta. A Price é a prestação fixa: parcela leve no começo e mais juros no total."

---

## Nota de verificação

- PD 1.3.7 lido no texto do repositório. Slides A3478 e A3479 e apostila p. 144–148 lidos nesta sessão.
- Cálculos conferidos em Python: amortização 5.000; parcela 1 do SAC = 6.080; parcela 7 = 5.540; parcela 12 = 5.090; juros totais do SAC = 7.020; PMT da Price = 5.604,12; total da Price = 67.249,42; juros = 7.249,42; diferença 229,42.
- Convenções: financiamento de R$ 60.000, 12 meses e 1,8% a.m. (didáticos); a questão de banco do slide foi substituída.
- Taxa equivalente semestral: 1,30^0,5 − 1 = 14,0175%.
