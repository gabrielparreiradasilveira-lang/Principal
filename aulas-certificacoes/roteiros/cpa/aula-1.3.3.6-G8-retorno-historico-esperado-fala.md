# Roteiro de fala — Aula CPA: Retorno Histórico × Retorno Esperado, de um Ativo e de uma Carteira

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3.6**, **1.3.3.6.1** e **1.3.3.6.2**; slides A3476 p. 5 e 8–10; aula do repositório `aula-1.3-D-tir-cmpc-duration-retorno-payback`.

CPA 1.3.3.6 · 1.3.3.6.1 · 1.3.3.6.2 · Módulo 1 · **10 min** · Aula G8 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Retrovisor e para-brisa.** O retorno histórico é o retrovisor: mostra o que de fato aconteceu. O retorno esperado é o para-brisa: uma projeção, feita com cenários e probabilidades, sobre o que pode acontecer.

**Onde a metáfora falha:** o retrovisor pode mostrar um período atípico, que não se repete. O para-brisa depende de premissas, e a estrada pode mudar. A carteira, que não aparece na metáfora, é só uma média ponderada pelos pesos.

### 🔇 Caso

Um **fundo de ações** com cinco anos de retorno real e três cenários para o próximo ano. Uma carteira de três fundos, com pesos de 50%, 30% e 20%.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3.6 Retorno histórico e esperado | Slides A3476 p. 5, 8, 9 | Conferido |
| 1.3.3.6.1 De um ativo | Slides A3476 p. 10 | Conferido; **concentração de risco** |
| 1.3.3.6.2 De uma carteira | Slides A3476 p. 10 | Conferido; **média ponderada e diversificação** |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3476 p. 8 | Retorno histórico serve para "média, volatilidade, Sharpe" | Correto, mas a média histórica não é o retorno esperado. O slide 9 diz que pode ser muito diferente |
| 2 | Slides A3476 p. 9 | Retorno esperado "usa dados históricos" | Usa dados históricos como uma das entradas, com premissas e cenários |
| 3 | Slides A3476 p. 10 | Retorno de carteira = "média ponderada" | Correto para o retorno esperado. Para o risco, a média não serve: a diversificação reduz o risco sem reduzir o retorno esperado médio |
| 4 | Slides A3476 p. 10 | Riscos concentrados: "Empresa pode quebrar" | Correto como exemplo de risco específico, que a diversificação reduz |

### 🔇 Dados

**Retorno histórico do fundo (5 anos, em %):** 12, −4, 18, 7, 9.

| Medida | Cálculo | Resultado |
| --- | --- | --- |
| Média aritmética histórica | (12 − 4 + 18 + 7 + 9) ÷ 5 | **8,40% a.a.** |
| Retorno geométrico | (1,12 × 0,96 × 1,18 × 1,07 × 1,09)^(1/5) − 1 | **8,15% a.a.** |

**Retorno esperado do próximo ano, por cenários:**

| Cenário | Probabilidade | Retorno | Contribuição |
| --- | --- | --- | --- |
| Otimista | 40% | +25% | +10,0% |
| Base | 40% | +8% | +3,2% |
| Pessimista | 20% | −20% | −4,0% |
| **Retorno esperado** | 100% | — | **9,20%** |

**Carteira:**

| Fundo | Peso | Retorno esperado |
| --- | --- | --- |
| Ações (o caso acima) | 50% | 9,20% |
| Fundo de crescimento | 30% | 14,00% |
| Renda fixa | 20% | 4,00% |
| **Carteira** | 100% | **9,60%** (média ponderada) |

🔇 Cenários e probabilidades são hipóteses didáticas.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso do fundo: o retrovisor | 3 min |
| 2. Os cenários: o para-brisa | 3 min |
| 3. A carteira: média pelo peso | 3 min |
| 4. Fechamento | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em três blocos

### Bloco 1 — Caso do fundo: o retrovisor — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular a média histórica e explicar o que ela mostra.

- "Um fundo de ações tem cinco anos de retorno: doze por cento, menos quatro, mais dezoito, mais sete e mais nove. Qual foi a média?"
- "O **retorno histórico** é o que o fundo efetivamente rendeu no passado. Ele mostra consistência e volatilidade, como um retrovisor mostra o que ficou para trás."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `12` `ENTER` `4` `CHS` `+` `18` `+` `7` `+` `9` `+` `5` `÷` | 🖥️ 8,40 | Média aritmética histórica |

- "Oito vírgula quarenta por cento ao ano. Mas essa média é do passado. Não é o que se espera para o próximo ano."
- **Erro comum:** tomar a média histórica como retorno esperado. O retrovisor mostra onde o carro esteve, e não para onde ele vai.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O retorno histórico é o retorno esperado para o próximo período" | Errado | É o que aconteceu |
| "O retorno histórico serve para avaliar a consistência de desempenho" | Certo | Slides A3476 p. 8 |

**🔗 Ponte:** "E para o próximo ano? Olhe para a frente."

---

### Bloco 2 — Os cenários: o para-brisa — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o retorno esperado por cenários, ponderado pela probabilidade.

- "Para o próximo ano, há três cenários. Com quarenta por cento de chance, o fundo sobe vinte e cinco. Com quarenta por cento, sobe oito. Com vinte por cento, cai vinte. Qual é o retorno esperado?"
- "O **retorno esperado** é a média dos cenários, pesada pela chance de cada um."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `0,4` `ENTER` `25` `×` `0,4` `ENTER` `8` `×` `+` `0,2` `ENTER` `20` `CHS` `×` `+` | 🖥️ 9,20 | Retorno esperado, em % |

- "Nove vírgula vinte por cento. O número é menor que a média histórica do retrovisor, porque o cenário de queda pesa."
- **Erro comum:** tirar a média simples dos três cenários: vinte e cinco mais oito menos vinte, dividido por três, dá quatro vírgula trinta e três. Sem as probabilidades, a conta não representa o cenário.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O retorno esperado é a média dos cenários ponderada pelas probabilidades" | Certo | Slides A3476 p. 9 |
| "O retorno esperado é a média aritmética dos retornos passados" | Errado | Usa cenários e probabilidades |

**🔗 Ponte:** "E quando o investimento é uma carteira, e não um fundo só?"

---

### Bloco 3 — A carteira: média pelo peso — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o retorno esperado de uma carteira pelos pesos dos ativos.

- "A carteira tem três fundos: cinquenta por cento em ações, trinta em crescimento e vinte em renda fixa. O retorno esperado da carteira é a média dos retornos de cada fundo, pesada pelo peso."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `0,5` `ENTER` `9,2` `×` `0,3` `ENTER` `14` `×` `+` `0,2` `ENTER` `4` `×` `+` | 🖥️ 9,60 | Retorno esperado da carteira, em % |

- "Nove vírgula sessenta por cento. Repare que a diversificação não aumenta esse número: ela reduz o risco. A média fica na média."
- **Erro comum:** tirar a média simples dos três fundos: nove vírgula dois, mais catorze, mais quatro, dividido por três, dá nove vírgula zero sete. O peso importa.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O retorno esperado da carteira é a média ponderada pelos pesos dos ativos" | Certo | Slides A3476 p. 10 |
| "Diversificar aumenta o retorno esperado médio da carteira" | Errado | Reduz o risco; o retorno médio fica na média dos ativos |

> **Carteira: média pelo peso. Risco: a diversificação reduz; o retorno médio não muda por isso.**

- 🔇 **Fechamento:** "O retrovisor mostra o passado; o para-brisa, a média dos cenários; e a carteira, a média pelo peso de cada ativo." Próxima aula: G9, taxas de juros.

---

## Lista de pegadinhas com nome

1. **Pegadinha do retrovisor** — "O retorno histórico de 8,4% é o que se espera." Errado: é o que aconteceu.
2. **Pegadinha da média simples dos cenários** — "A média dos três cenários é o retorno esperado." Errado: pondere pela probabilidade; o resultado é 9,20%.
3. **Pegadinha do peso esquecido** — "A carteira de três fundos rende a média dos três." Errado: pesos de 50%, 30% e 20% dão 9,60%.
4. **Pegadinha do para-brisa certo** — "Como o retorno esperado é calculado, ele é certo." Errado: depende de premissas e cenários.

---

## Nota de verificação

- PD 1.3.3.6 a 1.3.3.6.2 lido no texto do repositório. Slides A3476 lidos nesta sessão.
- Cálculos conferidos em Python: média aritmética 8,40%; geométrica 8,15%; retorno esperado 0,4×25 + 0,4×8 − 0,2×20 = 9,20%; carteira 0,5×9,2 + 0,3×14 + 0,2×4 = 9,60%; média simples dos cenários = 4,33; média simples dos fundos = 9,07.
- Convenções: cinco anos de retorno, cenários e probabilidades, fundos de crescimento e renda fixa (didáticos).
- Sharpe citado sem fórmula, como no slide.
- Revisão de estrutura: metáfora única (retrovisor e para-brisa), casos antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
