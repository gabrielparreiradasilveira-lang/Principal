# Roteiro de fala — Aula CPA: Retorno Histórico × Retorno Esperado, de um Ativo e de uma Carteira

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3.6**, **1.3.3.6.1** e **1.3.3.6.2**; slides A3476 p. 5 e 8–10 (retorno histórico, retorno esperado e carteira); aula do repositório `aula-1.3-D-tir-cmpc-duration-retorno-payback`.

CPA 1.3.3.6 · 1.3.3.6.1 · 1.3.3.6.2 · Módulo 1 · **10 min** · Aula G8 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula é um **retrovisor e um para-brisa**. O retorno histórico é o retrovisor: mostra o que de fato aconteceu, e não para onde o carro vai. O retorno esperado é o para-brisa: é uma projeção, feita com cenários e probabilidades. A carteira é uma **frota de carros** em que cada um tem um peso: o retorno da frota é a média ponderada.

- Caso: um fundo de ações com cinco anos de retorno real e três cenários para o próximo ano.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3.6 Retorno histórico e esperado | Slides A3476 p. 5, 8, 9 | Conferido |
| 1.3.3.6.1 De um ativo | Slides A3476 p. 10 | Conferido; **concentração de risco** |
| 1.3.3.6.2 De uma carteira | Slides A3476 p. 10 | Conferido; **média ponderada e diversificação** |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3476 p. 8 | Retorno histórico serve para "calcular média, volatilidade, Sharpe" | Correto. Mas a média histórica **não é** o retorno esperado. O slide 9 diz "pode ser muito diferente", e a aula insiste nisso |
| 2 | Slides A3476 p. 9 | Retorno esperado "usa dados históricos" | Usa dados históricos **como uma das entradas**, mas com premissas e cenários. Não é a média do passado |
| 3 | Slides A3476 p. 10 | Retorno de carteira = "média ponderada" | Correto para o **retorno esperado**. Para o **risco**, a média não serve: a diversificação reduz o risco sem reduzir o retorno esperado |
| 4 | Slides A3476 p. 10 | Riscos concentrados, "Empresa pode quebrar" | Correto como exemplo de risco específico, que a diversificação reduz |

### 🔇 Dados do exemplo

**Retorno histórico do fundo (5 anos, em %):** 12, −4, 18, 7, 9.

| Medida | Cálculo | Resultado |
| --- | --- | --- |
| Média aritmética histórica | (12 − 4 + 18 + 7 + 9) ÷ 5 | **8,40% a.a.** |
| Retorno geométrico (anual composto) | (1,12 × 0,96 × 1,18 × 1,07 × 1,09)^(1/5) − 1 | **8,15% a.a.** |

**Retorno esperado do próximo ano, por cenários:**

| Cenário | Probabilidade | Retorno | Contribuição |
| --- | --- | --- | --- |
| Otimista | 40% | +25% | +10,0% |
| Base | 40% | +8% | +3,2% |
| Pessimista | 20% | −20% | −4,0% |
| **Retorno esperado** | 100% | — | **9,20%** |

**Carteira (três fundos, pesos de 50%, 30% e 20%):**

| Fundo | Peso | Retorno esperado |
| --- | --- | --- |
| Ações (do exemplo acima) | 50% | 9,20% |
| Fundo de crescimento | 30% | 14,00% |
| Renda fixa | 20% | 4,00% |
| **Carteira** | 100% | **9,60%** (média ponderada) |

🔇 Cenários e probabilidades são hipóteses didáticas. Não são projeção de produto.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. O retrovisor: retorno histórico | 3 min |
| 2. O para-brisa: retorno esperado | 3 min |
| 3. A frota: retorno de carteira | 3 min |
| 4. Fechamento | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em três blocos

### Bloco 1 — O retrovisor: retorno histórico — 3 min

- "O retorno histórico é o que o ativo efetivamente rendeu no passado. Serve para ver consistência, volatilidade e medidas como o índice Sharpe."
- ✏️ "A média histórica de 8,4% parece o retorno esperado. Não é: o retrovisor mostra onde o carro esteve, não para onde vai."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `12` `ENTER` `4` `CHS` `+` `18` `+` `7` `+` `9` `+` `5` `÷` | 🖥️ 8,40 | Média aritmética histórica |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O retorno histórico é o retorno esperado para o próximo período" | Errado | É o que aconteceu |
| "O retorno histórico serve para avaliar a consistência de desempenho" | Certo | Slides A3476 p. 8 |

> **Retrovisor: mostra o que passou. O para-brisa é outra conta.**

**🔗 Ponte:** "E para o para-brisa, o que se usa?"

---

### Bloco 2 — O para-brisa: retorno esperado — 3 min

- "O retorno esperado é a média dos cenários, ponderada pela probabilidade de cada um."
- "Com 40% de chance de +25%, 40% de +8% e 20% de −20%, o retorno esperado é 9,2%."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `0,4` `ENTER` `25` `×` `0,4` `ENTER` `8` `×` `+` `0,2` `ENTER` `20` `CHS` `×` `+` | 🖥️ 9,20 | Retorno esperado, em % |

- 🔇 Note a sequência com a pilha: a primeira parcela fica na pilha enquanto as outras são somadas.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O retorno esperado é a média dos cenários ponderada pelas probabilidades" | Certo | Slides A3476 p. 9 |
| "O retorno esperado é a média aritmética dos retornos passados" | Errado | Usa cenários e probabilidades |

> **Para-brisa: a média dos cenários, ponderada pela chance de cada um.**

**🔗 Ponte:** "E quando o investimento é uma carteira, não um ativo só?"

---

### Bloco 3 — A frota: retorno de carteira — 3 min

- "O retorno esperado da carteira é a média ponderada dos retornos esperados de cada ativo."
- "Mas o risco não é média: a diversificação reduz o risco sem reduzir o retorno esperado médio."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `0,5` `ENTER` `9,2` `×` `0,3` `ENTER` `14` `×` `+` `0,2` `ENTER` `4` `×` `+` | 🖥️ 9,60 | Retorno esperado da carteira, em % |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O retorno esperado da carteira é a média ponderada pelos pesos dos ativos" | Certo | Slides A3476 p. 10 |
| "Diversificar aumenta o retorno esperado médio da carteira" | Errado | Reduz o risco; o retorno médio fica na média dos ativos |

> **Carteira: média ponderada pelo peso. Risco: a diversificação reduz, o retorno médio não muda.**

- 🔇 Fechamento: "O retrovisor mostra o passado; o para-brisa, a média dos cenários; e a carteira, a média ponderada pelo peso de cada ativo."

---

## Nota de verificação

- PD 1.3.3.6 a 1.3.3.6.2 lido no texto do repositório. Slides A3476 p. 5 e 8–10 lidos nesta sessão.
- Cálculos conferidos em Python: média aritmética 8,40%; geométrica 8,15%; retorno esperado 0,4×25 + 0,4×8 − 0,2×20 = 9,20%; carteira 0,5×9,2 + 0,3×14 + 0,2×4 = 9,60%.
- Convenções: cinco anos de retorno, cenários e probabilidades, e os fundos de crescimento e renda fixa com 14% e 4% (didáticos).
- Sharpe citado sem fórmula, como no slide. Sem norma específica.
