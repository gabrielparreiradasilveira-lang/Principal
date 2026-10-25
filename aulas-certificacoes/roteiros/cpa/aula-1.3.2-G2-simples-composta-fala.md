# Roteiro de fala — Aula CPA: Capitalização Simples × Composta

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), item **1.3.2**; APOSTILA-CPA p. 123–125; slides A3472 p. 3–8 (juros simples, juros compostos, taxa proporcional e efetiva); aula do repositório `aula-1.3-B-capitalizacao-equivalencia-descontos`, da qual só a parte de capitalização é usada aqui.

CPA 1.3.2 · Módulo 1 · **20 min** · Aula G2 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula não segue o formato "tópico, metáfora, exemplo". Ela é uma **corrida de duas bolas de neve**. A ideia: ao longo de 18 meses, uma bola rola com o mesmo tamanho de empurrão (simples) e a outra cresce sobre si mesma (composta). O professor mostra o cálculo em duas etapas: primeiro o mês 6, depois o mês 18.

- Caso: **Sofia** guarda R$ 8.000 num título de 1,5% ao mês, por 18 meses.
- 🔇 A fala não usa "escada" nem "juros sobre juros" como metáfora central. Isso fica para a G9 e a G3.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.2 Juros simples × juros compostos | Apostila p. 123–125; slides A3472 p. 3–5 | Conferido |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3472 p. 4 | "Taxa proporcional: 2% ao mês → 24% ao ano" | Correto **apenas no regime simples**. Em composto, a taxa anual equivalente é 1,02¹² − 1 = 26,82%, e não 24% |
| 2 | Slides A3472 p. 5 | Fórmula de capitalização composta "FV = PV(1+i)^t" sem o "t" inteiro | O expoente pode ser fracionário em composto, com a taxa convertida para a mesma periodicidade do prazo |
| 3 | Slide 5 | Taxa equivalente composta i₂ = (1 + i₁)^(n₂/n₁) − 1 | Correto, e é a fórmula que a aula usa para converter mês em ano |

### 🔇 Dados do exemplo (Sofia)

| Item | Valor |
| --- | --- |
| Capital | R$ 8.000 |
| Taxa | 1,5% a.m. |
| Prazo | 18 meses |
| Juros simples | 8.000 × 1,5% × 18 = **R$ 2.160,00** → montante **R$ 10.160,00** |
| Juros compostos | 8.000 × 1,015¹⁸ = **R$ 10.458,73** → juros de R$ 2.458,73 |
| Diferença | **R$ 298,73** a favor da composta, só pelo efeito de juros sobre juros |
| Taxa anual efetiva da composta | 1,015¹² − 1 = **19,56%** a.a. (contra 18% a.a. no simples) |

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. A corrida das duas bolas (conceito) | 4 min |
| 2. Simples: a conta do mês 6 | 3 min |
| 3. Composta: a conta do mês 6 e o salto | 4 min |
| 4. O mês 18 e a diferença | 5 min |
| 5. Qual regime usar e quando | 4 min |
| **Total** | **20 min** |

---

## 3. Explicação em cinco blocos

### Bloco 1 — A corrida das duas bolas — 4 min

- "Imagine duas bolas de neve na mesma ladeira. As duas começam com o mesmo tamanho, de oito mil reais."
- "A primeira, a do **simples**, ganha sempre o mesmo pedaço de neve: 1,5% do **capital inicial**, a cada mês. Não importa quanto a bola já cresceu."
- "A segunda, a do **composto**, ganha 1,5% do **tamanho que tem agora**. Ela cresce sobre o que já cresceu."
- "Por isso o simples é uma escada de degraus iguais, e o composto é a bola de neve."

| Pergunta de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "No regime simples, os juros incidem sobre o capital inicial" | Certo | Slides A3472 p. 4 |
| "No regime composto, os juros se acumulam sobre o montante anterior" | Certo | Slides A3472 p. 5 |

> **Simples: sempre o mesmo pedaço do início. Composto: sobre o que já cresceu.**

**🔗 Ponte:** "Vamos medir a bola simples no mês 6."

---

### Bloco 2 — Simples: a conta do mês 6 — 3 min

- "Juros simples: **J = C × i × t**. Ao final de seis meses:"

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `8000` `ENTER` `1,5` `%` `6` `×` | 🖥️ 720,00 | Juros de 6 meses |
| 2 | ⌨️ `8000` `+` | 🖥️ 8.720,00 | Montante no mês 6 |

- "Repare: o juro do mês 6 é o mesmo que o do mês 1. A bola simples não acelera."
- 🔇 Passo 1: `1,5 %` sobre 8.000 dá 120; `× 6` dá 720. Por isso o `%` vem antes do `×`.

**🔗 Ponte:** "E a bola composta, no mesmo mês?"

---

### Bloco 3 — Composta: a conta do mês 6 e o salto — 4 min

- "Juros compostos: **M = C × (1 + i)^t**. Ao mês 6:"

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `1,015` `ENTER` `6` `y^x` `8000` `×` | 🖥️ 8.747,55 | Montante no mês 6 |

- "No mês 6, a composta já está em R$ 8.747,55, contra R$ 8.720 do simples. A diferença ainda é pequena, de R$ 27,55. Mas repare no **salto**: a diferença cresce com o tempo."
- ✏️ **O slide diz "taxa proporcional 2% ao mês → 24% ao ano"** e vale só no simples. Na composta, o ano de 2% ao mês equivale a 26,82%. Não use 24% para comparar regimes.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa proporcional é válida para o regime composto" | Errado | Só vale no simples |
| "Em composto, a taxa anual equivalente a 2% ao mês é 24%" | Errado | É 26,82% |

**🔗 Ponte:** "E no mês 18, que é o prazo de verdade da Sofia?"

---

### Bloco 4 — O mês 18 e a diferença — 5 min

| Regime | Montante no mês 18 | Juros acumulados | Taxa anual |
| --- | --- | --- | --- |
| **Simples** | R$ 10.160,00 | R$ 2.160,00 | 18,00% |
| **Composto** | R$ 10.458,73 | R$ 2.458,73 | 19,56% |

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `8000` `CHS` `PV` `1,5` `i` `18` `n` `FV` | 🖥️ 10.458,73 | Montante composto |
| 2 | ⌨️ `1,015` `ENTER` `12` `y^x` `1` `−` `100` `×` | 🖥️ 19,56 | Taxa anual efetiva |

- "Em um ano e meio, a composta rende quase R$ 300 a mais. E a taxa efetiva anual é 19,56%, e não os 18% que o simples sugere."
- 🔇 Note que o `CHS` antes do `PV` é só para o FV sair positivo.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "No mesmo prazo e taxa, o composto sempre rende mais que o simples" | Certo | Desde que haja mais de um período |
| "A taxa efetiva anual de 1,5% ao mês é 18%" | Errado | É 19,56% |

**🔗 Ponte:** "Mas, afinal, em que situação cada regime é usado?"

---

### Bloco 5 — Qual regime usar e quando — 4 min

| Regime | Onde aparece | Por quê |
| --- | --- | --- |
| **Simples** | Cálculos didáticos, alguns descontos comerciais, prazos curtos | Simplicidade |
| **Composto** | Aplicações financeiras, empréstimos bancários, o padrão de mercado | Reflete o rendimento real |

- "Quando alguém oferece uma taxa 'de 2% ao mês', pergunte: é simples ou composto? Porque a conta anual muda."
- ➕ **O erro mais comum na prova:** achar que, com prazo de um mês, os dois regimes dão o mesmo. Dão, porque não há juros sobre juros em um período só. A diferença começa no segundo período.

> **Simples vale para a escada; composto, para a bola de neve. Quem compara taxas precisa saber qual regime está escrito.**

- 🔇 Fechamento: "Duas bolas começam iguais e terminam diferentes: a diferença é só o efeito de crescer sobre o que já cresceu."

---

## Nota de verificação

- PD 1.3.2 lido no texto do repositório. Apostila p. 123–125 e slides A3472 lidos nesta sessão.
- Cálculos conferidos em Python: simples 2.160,00 e montante 10.160,00; composto 10.458,73; taxa efetiva 19,56%; mês 6 composto 8.747,55 (1,015⁶ × 8.000) e simples 8.720,00.
- Convenções: capital de R$ 8.000 e taxa de 1,5% a.m. (exemplo didático; não é produto).
- Sem norma específica: matemática financeira clássica.
