# Roteiro de fala — Aula CPA: Custo de Oportunidade, Taxa Livre de Risco e CMPC

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3.5.3**, **1.3.3.5.4** e **1.3.3.5.5**; slides A3474 p. 6 e A3475 p. 4; aula do repositório `aula-1.3-D-tir-cmpc-duration-retorno-payback`.

CPA 1.3.3.5.3 · 1.3.3.5.4 · 1.3.3.5.5 · Módulo 1 · **10 min** · Aula G6 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Mistura de cafés.** O dinheiro da empresa vem de fontes com preços diferentes, como cafés de origens diferentes numa mesma lata. O preço médio da lata é o CMPC, pesado pela quantidade de cada café.

**Onde a metáfora falha:** não existe lata física, e o custo do capital próprio não sai do caixa como um pagamento. O peso também é o valor de mercado, e não a quantidade de café. Por isso o CMPC é uma taxa de exigência, e não uma conta de caixa.

### 🔇 Caso

Uma **rede de cafeterias** tem 70% de capital próprio, com custo de 16% a.a., e 30% de dívida, com custo de 12% a.a. antes do imposto. A alíquota de IR sobre a dívida é de 34%.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3.5.3 Custo de oportunidade | Slides A3474 p. 6 | Conferido |
| 1.3.3.5.4 Taxa livre de risco | Slides A3474 p. 6 | **Número datado retirado**; conceito mantido |
| 1.3.3.5.5 CMPC | Slides A3475 p. 4 | Conferido; **fórmula com IR sobre a dívida** |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3474 p. 6 | Taxa livre de risco = "Selic Meta (15%)" | Número datado, retirado. Conceito: retorno de um título sem risco de crédito, de prazo parecido |
| 2 | Slides A3474 p. 6 | Custo de oportunidade: "comparação com CDB de grandes instituições" | Exemplo de baixo risco. O custo de oportunidade é a melhor alternativa de risco comparável, que pode ser maior |
| 3 | Slides A3475 p. 4 | CMPC "é o mínimo que um projeto deve render" | Correto. A regra completa usa o custo da dívida após IR, porque o juro é dedutível. O slide omite isso |
| 4 | Slides A3475 p. 4 | CMPC "é o custo do dinheiro da empresa" | Resumo correto. A fórmula é uma média ponderada pelos pesos de capital próprio e de terceiros |

### 🔇 Dados

| Item | Valor |
| --- | --- |
| Peso do capital próprio | 70%, custo de 16% a.a. |
| Peso da dívida | 30%, custo de 12% a.a. antes do IR |
| Custo da dívida após IR | 12% × (1 − 0,34) = **7,92% a.a.** |
| CMPC | 70% × 16% + 30% × 7,92% = **13,58% a.a.** |
| Alternativa de risco parecido para a rede | Título rendendo 13% a.a. (hipótese) |

🔇 Os números 70/30, 16%, 12% e 34% são do slide e servem como estrutura. A taxa de 16% é a exigência de retorno dos acionistas, e não um valor de mercado.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso da rede e a alternativa de risco parecido | 2 min |
| 2. O custo de oportunidade | 2 min |
| 3. A mistura: conta do CMPC | 5 min |
| 4. Fechamento: a régua da decisão | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — Caso da rede e a alternativa de risco parecido — 2 min

> **Objetivo deste bloco:** ao fim, o aluno consegue explicar o que é taxa livre de risco.

- "A rede de cafeterias tem um dinheiro parado: a diretoria pode abrir uma loja nova, ou aplicar num título com risco parecido, que rende treze por cento ao ano."
- "A **taxa livre de risco** é o retorno de um título que não tem risco de crédito, com prazo parecido. Serve de piso: nenhuma alternativa de risco deveria render menos que ela."
- **Erro comum:** tratar um número de jornal como taxa fixa. A taxa livre de risco muda com o mercado; guarde o conceito, e não o número.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa livre de risco é a de um título sem risco de crédito, de prazo equivalente" | Certo | Conceito |
| "A taxa livre de risco é um valor fixo publicado pela CVM" | Errado | Varia com o mercado |

**🔗 Ponte:** "Se a diretoria abre a loja, ela deixa o título de treze por cento. Isso tem nome."

---

### Bloco 2 — O custo de oportunidade — 2 min

> **Objetivo deste bloco:** ao fim, o aluno consegue identificar o custo de oportunidade numa decisão.

- "**Custo de oportunidade** é o retorno da melhor alternativa que se deixa de lado, desde que tenha risco comparável. Se a rede abre a loja, ela deixa de ganhar os treze por cento."
- **Erro comum:** achar que o custo de oportunidade é sempre igual à taxa livre de risco. A taxa livre de risco é o piso; o custo de oportunidade é a alternativa de risco comparável, que pode ser maior.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O custo de oportunidade é a melhor alternativa abandonada, de risco comparável" | Certo | Slides A3474 p. 6 |
| "O custo de oportunidade é sempre igual à taxa livre de risco" | Errado | Pode ser maior |

**🔗 Ponte:** "E quando o dinheiro vem de mais de uma fonte?"

---

### Bloco 3 — A mistura: conta do CMPC — 5 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o CMPC com pesos e com a dedução do imposto.

- "A rede usa dois tipos de dinheiro: o dos donos, que exigem dezesseis por cento, e o emprestado, que custa doze antes do imposto. Qual é o custo médio de cada real que a rede usa?"
- "O juro da dívida é dedutível do imposto. Por isso, o custo real da dívida é menor: doze por cento vezes sessenta e seis por cento, que dá sete vírgula noventa e dois."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `0,7` `ENTER` `16` `×` | 🖥️ 11,20 | Contribuição do capital próprio |
| 2 | ⌨️ `0,3` `ENTER` `12` `×` `0,66` `×` | 🖥️ 2,38 | Contribuição da dívida após IR |
| 3 | ⌨️ `+` | 🖥️ 13,58 | CMPC, em % ao ano |

- 🔇 No passo 2, `0,66` é 1 − 34%. Dá o mesmo resultado usar a alíquota de 34% diretamente.
- **Erro comum:** tirar a média simples de dezesseis e doze e achar quatorze por cento. Os pesos importam: a dívida pesa menos, porque é trinta por cento da mistura.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O IR reduz o custo efetivo da dívida na CMPC" | Certo | Juros são dedutíveis |
| "Na CMPC, o custo do capital próprio entra sem ponderação" | Errado | Entra com o peso de 70% |

> **CMPC: média ponderada pelo peso de cada fonte, com o imposto descontando o juro da dívida.**

**🔗 Ponte:** "Com o CMPC, a rede tem uma régua. Como ela se usa?"

---

### Bloco 4 — Fechamento: a régua da decisão — 1 min

> **Objetivo deste bloco:** ao fim, o aluno consegue ordenar piso, alternativa e régua de corte.

- "Se a TIR do projeto (G5) for maior que o CMPC, o projeto gera valor. Se for menor, destrói."
- **Erro comum:** comparar a TIR com a taxa de juros da dívida, sem a média dos custos. A régua é o CMPC.

> **Taxa livre de risco é o piso; custo de oportunidade é a alternativa; CMPC é a régua de corte.**

- 🔇 **Fechamento:** "O piso mostra o mínimo sem risco; a alternativa mostra o que se deixa de ganhar; e o CMPC mostra o que o dinheiro custa, em média." Próxima aula: G7, duration e alavancagem.

---

## Lista de pegadinhas com nome

1. **Pegadinha da média simples** — "A CMPC é a média de 16% e 12%, ou seja, 14%." Errado: pondere pelos pesos e aplique o IR sobre a dívida. O resultado é 13,58%.
2. **Pegadinha da alternativa igual ao piso** — "O custo de oportunidade é sempre a taxa livre de risco." Errado: a taxa livre de risco é o piso; a alternativa pode render mais.
3. **Pegadinha do juro sem imposto** — "A dívida custa 12% na CMPC." Errado: após o IR, custa 7,92%.
4. **Pegadinha do número de jornal** — "A Selic de hoje é a taxa livre de risco, para sempre." Errado: é um número datado; o conceito é que deve ser ensinado.

---

## Nota de verificação

- PD 1.3.3.5.3 a 1.3.3.5.5 lido no texto do repositório. Slides A3474 e A3475 lidos nesta sessão.
- Cálculos conferidos em Python: 12% × (1 − 0,34) = 7,92%; 0,7 × 16 + 0,3 × 7,92 = 13,576 ≈ 13,58%; média simples de 16 e 12 = 14%.
- Convenções: pesos 70/30, custos de 16% e 12%, alíquota de 34% (slide) e título de 13% (hipótese).
- Revisão de estrutura: metáfora única (mistura de cafés), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
