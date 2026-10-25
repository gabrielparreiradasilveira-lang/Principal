# Roteiro de fala — Aula CPA: Taxa de Desconto e Taxa Bruta × Líquida de Impostos

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3.3** e **1.3.3.4**; APOSTILA-CPA p. 124–125 (taxa aparente ou bruta); slides A3474 p. 6 (taxa de desconto) e A3472 p. 14 (taxa bruta e líquida); aulas do repositório 1.3-C e 1.3-A.

CPA 1.3.3.3 · 1.3.3.4 · Módulo 1 · **10 min** · Aula G4 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula é uma **conta de restaurante**. O preço do prato é a taxa bruta. Antes de chegar ao que sobra no bolso, há couvert, serviço e imposto. A taxa de desconto é a **régua** com que se mede o valor de hoje, e não entra na conta de impostos, mas aparece na mesma conversa.

- Caso: **Renan** aplica R$ 10.000 num CDB de 14% a.a., por dois anos. Ele quer saber quanto sobra depois do imposto de renda e quanto valeria, hoje, R$ 1.200 que ele receberá daqui a um ano.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3.3 Taxa de desconto | Slides A3474 p. 6; aula 1.3-C | Conferido; **tipos ilustrados sem número datado** |
| 1.3.3.4 Taxa bruta × líquida de impostos | Slides A3472 p. 14; apostila p. 125 | Conferido; **"bruta" e "aparente" esclarecidos** |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Apostila p. 125 | "Taxa aparente (ou bruta): nominal, sem descontar inflação **ou outros custos**" | Em **taxa bruta de impostos**, "bruta" significa **antes do imposto**. Já a taxa real desconta a inflação. São três conceitos distintos; a prova cobra essa separação |
| 2 | Slides A3474 p. 6 | Taxa livre de risco = "Selic Meta (15%)" | Número datado, retirado. Ensina-se o conceito |
| 3 | Slides A3472 p. 14 | Exemplo de taxa bruta e líquida | Usado com alíquotas da tabela regressiva de renda fixa (ver nota de verificação) |

### 🔇 Dados do exemplo (Renan)

| Item | Valor |
| --- | --- |
| CDB: aplicação | R$ 10.000 |
| Taxa bruta | 14% a.a., por 2 anos |
| Valor bruto ao fim de 2 anos | 10.000 × 1,14² = **R$ 12.996,00** |
| Ganho bruto | R$ 2.996,00 |
| IR sobre o ganho (alíquota de 15%, prazo acima de 720 dias) | **R$ 449,40** |
| Valor líquido | **R$ 12.546,60** |
| Taxa líquida anual equivalente | (12.546,60 ÷ 10.000)^(1/2) − 1 = **12,01% a.a.** |
| Taxa de desconto de Renan | 14% a.a. (para trazer R$ 1.200 de daqui a um ano) |
| VP de R$ 1.200 com desconto de 14% | **R$ 1.052,63** |

🔇 A alíquota de 15% vale para aplicações acima de 720 dias. Pela tabela regressiva de renda fixa, a alíquota é 22,5% até 180 dias, 20% de 181 a 360, 17,5% de 361 a 720 e 15% acima. Conferir na regra vigente antes de gravar. Não reabri a norma nesta sessão.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. A régua: taxa de desconto | 3 min |
| 2. O restaurante: bruta, imposto e líquida | 4 min |
| 3. A conta do Renan | 2 min |
| 4. Quando as duas taxas se confundem | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — A régua: taxa de desconto — 3 min

- "A taxa de desconto é a régua que traz valores futuros para hoje. Não é um imposto, nem um custo: é a exigência de quem avalia."
- "Três réguas aparecem na literatura: a taxa livre de risco, o custo de oportunidade (quanto eu ganharia em outra alternativa de baixo risco) e a taxa mínima de atratividade, definida pelo investidor."
- "Quando o Renan quer 1.200 de daqui a um ano, a régua de 14% diz que esse valor vale hoje 1.052,63."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1200` `ENTER` `1,14` `÷` | 🖥️ 1.052,63 | Valor presente de R$ 1.200 à régua de 14% |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa de desconto é um imposto sobre o investimento" | Errado | É uma régua de avaliação |
| "O custo de oportunidade é a rentabilidade de outro investimento de baixo risco" | Certo | Slides A3474 p. 6 |

> **A régua mede o valor de hoje: quem escolhe a régua escolhe o resultado.**

**🔗 Ponte:** "Agora, o que sobra do rendimento depois que o imposto passa pela mesa."

---

### Bloco 2 — O restaurante: bruta, imposto e líquida — 4 min

- "A taxa **bruta** é o preço do prato. A taxa **líquida** é o que sobra depois do couvert, do serviço e do imposto."
- "No CDB, o imposto de renda incide sobre o **ganho**, e não sobre o valor aplicado. Por isso o cálculo começa pelo ganho."

| Conceito | Base |
| --- | --- |
| **Bruta** | Antes de imposto |
| **Líquida** | Depois de imposto |
| **Real** | Depois de inflação (G1). Não se confunde com líquida |

- ✏️ "A apostila chama a bruta de aparente. Isso não quer dizer que ela desconte a inflação. Bruta é antes do imposto; real é depois da inflação. A prova troca os dois."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Taxa bruta é a taxa após descontar o imposto de renda" | Errado | Bruta é **antes** do imposto |
| "O imposto de renda incide sobre o valor aplicado" | Errado | Incide sobre o **ganho** |
| "Taxa real e taxa líquida são a mesma coisa" | Errado | Uma desconta a inflação; a outra, o imposto |

> **Bruta é antes do imposto; líquida é depois; real é depois da inflação.**

**🔗 Ponte:** "Vamos à conta do Renan."

---

### Bloco 3 — A conta do Renan — 2 min

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `10000` `CHS` `PV` `14` `i` `2` `n` `FV` | 🖥️ 12.996,00 | Valor bruto em 2 anos |
| 2 | ⌨️ `2996` `ENTER` `15` `%` `−` `10000` `+` | 🖥️ 12.546,60 | Valor líquido: ganho de 2.996 menos IR de 449,40, somado ao capital |
| 3 | ⌨️ `10000` `CHS` `PV` `12546,60` `FV` `2` `n` `i` | 🖥️ 12,01 | Taxa líquida anual |

- 🔇 No passo 2, `15 %` aplicado ao ganho de 2.996 dá 449,40. O visor mostra o resultado líquido direto.
- "Repare: 14% bruto virou 12,01% líquido. Quase dois pontos de imposto e prazo."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Com 14% bruto e alíquota de 15%, a taxa líquida anual fica em 11,9%" | Errado | Fica em 12,01%, pela composição |
| "Aplicações acima de 720 dias têm alíquota de 15%" | Certo | Tabela regressiva de renda fixa (conferir) |

**🔗 Ponte:** "Quando a bruta e a líquida viram a mesma coisa?"

---

### Bloco 4 — Quando as taxas se confundem — 1 min

- "Em produto isento, como a LCI ou a LCA para pessoa física, a bruta é igual à líquida. O imposto é zero."
- 🔇 Isenção de LCI/LCA para pessoa física citada de memória; conferir na regra vigente.

> **Isento: bruta e líquida se encontram. Tributado: a diferença é o imposto sobre o ganho.**

- 🔇 Fechamento: "A régua da taxa de desconto mede o valor de hoje; a taxa bruta é antes do imposto; a líquida, depois; e o imposto incide sobre o ganho, não sobre o capital."

---

## Nota de verificação

- PD 1.3.3.3 e 1.3.3.4 lidos no texto do repositório. Apostila p. 124–125 e slides A3472 e A3474 lidos nesta sessão.
- Cálculos conferidos em Python: 10.000 × 1,14² = 12.996,00; IR 15% sobre 2.996 = 449,40; líquido 12.546,60; taxa líquida anual 12,01%; 1.200 ÷ 1,14 = 1.052,63.
- **Não reaberto nesta sessão:** tabela regressiva de IR de renda fixa (22,5%, 20%, 17,5%, 15%) e isenção de LCI/LCA. Citados de memória.
- Convenção: taxa de 14% a.a. e régua de 14% (exemplo didático).
