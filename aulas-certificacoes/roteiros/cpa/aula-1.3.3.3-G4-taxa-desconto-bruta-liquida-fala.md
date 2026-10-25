# Roteiro de fala — Aula CPA: Taxa de Desconto e Taxa Bruta × Líquida de Impostos

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3.3** e **1.3.3.4**; APOSTILA-CPA p. 124–125; slides A3474 p. 6 e A3472 p. 14; aulas do repositório 1.3-C e 1.3-A.

CPA 1.3.3.3 · 1.3.3.4 · Módulo 1 · **10 min** · Aula G4 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Conta de restaurante.** O preço do prato é a taxa bruta. Antes de chegar ao que sobra no bolso, entram o couvert e o imposto. A taxa líquida é o que sobra.

**Onde a metáfora falha:** no restaurante, o imposto incide sobre a conta toda. No investimento, o imposto de renda incide só sobre o **ganho**, e não sobre o valor aplicado. E a alíquota muda com o prazo, o que não existe na conta do restaurante.

### 🔇 Caso

**Renan** aplica R$ 10.000 num CDB de 14% a.a., por dois anos. Ele quer saber quanto sobra depois do imposto de renda.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3.3 Taxa de desconto | Slides A3474 p. 6; aula 1.3-C | Conferido; **tipos ilustrados sem número datado** |
| 1.3.3.4 Taxa bruta × líquida de impostos | Slides A3472 p. 14; apostila p. 125 | Conferido; **"bruta" e "aparente" separados** |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Apostila p. 125 | "Taxa aparente (ou bruta): nominal, sem descontar inflação ou outros custos" | Em taxa bruta de impostos, "bruta" é **antes do imposto**. Inflação é outro conceito (G1) |
| 2 | Slides A3474 p. 6 | Taxa livre de risco = "Selic Meta (15%)" | Número datado, retirado. Ensina-se o conceito |
| 3 | Slides A3472 p. 14 | Exemplo de taxa bruta e líquida | Usado com alíquotas da tabela regressiva de renda fixa (ver nota de verificação) |

### 🔇 Dados

| Item | Valor |
| --- | --- |
| CDB: aplicação | R$ 10.000 |
| Taxa bruta | 14% a.a., por 2 anos |
| Valor bruto em 2 anos | 10.000 × 1,14² = **R$ 12.996,00** |
| Ganho bruto | R$ 2.996,00 |
| IR sobre o ganho (15%, acima de 720 dias) | **R$ 449,40** |
| Valor líquido | **R$ 12.546,60** |
| Taxa líquida anual | (12.546,60 ÷ 10.000)^(1/2) − 1 = **12,01% a.a.** |
| VP de R$ 1.200 daqui a um ano, com taxa de 14% | **R$ 1.052,63** |

🔇 A alíquota de 15% vale para aplicações acima de 720 dias. Pela tabela regressiva de renda fixa, a alíquota é 22,5% até 180 dias, 20% de 181 a 360, 17,5% de 361 a 720 e 15% acima. **Conferir na regra vigente antes de gravar.**

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso de Renan: o prato e a conta | 3 min |
| 2. Quanto sobra: taxa líquida | 4 min |
| 3. A régua: taxa de desconto | 2 min |
| 4. Quando as duas taxas se encontram | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — Caso de Renan: o prato e a conta — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue distinguir taxa bruta de taxa líquida.

- "Renan põe dez mil reais num CDB que rende quatorze por cento ao ano, por dois anos. Ao fim, o banco mostra doze mil novecentos e noventa e seis reais. Parece que ele ganhou quase três mil."
- "Mas o banco vai descontar o imposto de renda. É como a conta de um restaurante: o preço do prato é o bruto. Depois entram o couvert e o imposto, e o que sobra é o líquido."
- "Quatorze por cento é a taxa **bruta**: antes do imposto. A taxa **líquida** é a que sobra depois."
- **Erro comum:** achar que o imposto de renda incide sobre o valor aplicado. Ele incide sobre o **ganho**, que são os quase três mil.

**🔗 Ponte:** "Vamos fazer a conta do imposto e ver o que sobra."

---

### Bloco 2 — Quanto sobra: taxa líquida — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o imposto sobre o ganho e chegar à taxa líquida anual.

- "O imposto de renda da aplicação é de quinze por cento sobre o ganho de quase três mil reais. São quatrocentos e quarenta e nove reais e quarenta centavos. O líquido fica em doze mil quinhentos e quarenta e seis."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `2996` `ENTER` `15` `%` `−` `10000` `+` | 🖥️ 12.546,60 | Líquido: ganho menos imposto, somado ao capital |
| 2 | ⌨️ `f` `REG` `10000` `CHS` `PV` `12546,60` `FV` `2` `n` `i` | 🖥️ 12,01 | Taxa líquida anual |

- "Repare: quatorze por cento bruto virou doze vírgula zero um líquido. O imposto e o prazo consomem quase dois pontos."
- 🔇 No passo 1, o `15 %` calcula 15% do ganho de 2.996 e mantém esse ganho na pilha. Por isso o `−` desconta o imposto do ganho, e o `10000 +` devolve o capital.
- **Erro comum:** aplicar o imposto na taxa anual: quatorze vezes oitenta e cinco por cento dá onze vírgula nove. Não é assim, porque o imposto incide sobre o ganho acumulado em dois anos.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Com 14% bruto e alíquota de 15%, a taxa líquida anual fica em 11,9%" | Errado | Fica em 12,01%, pela composição |
| "Aplicações acima de 720 dias têm alíquota de 15%" | Certo | Tabela regressiva de renda fixa (conferir) |

**🔗 Ponte:** "E quando a bruta e a líquida são a mesma coisa?"

---

### Bloco 3 — A régua: taxa de desconto — 2 min

> **Objetivo deste bloco:** ao fim, o aluno consegue trazer um valor futuro para hoje com a taxa de desconto.

- "Taxa de desconto é a taxa que a pessoa exige para trazer um valor futuro para hoje. Não é imposto, nem custo cobrado de alguém."
- "Renan quer receber mil e duzentos reais daqui a um ano. Com a exigência de quatorze por cento, esse valor vale hoje mil cinquenta e dois reais e sessenta e três centavos."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1200` `ENTER` `1,14` `÷` | 🖥️ 1.052,63 | VP de R$ 1.200 à exigência de 14% |

- **Erro comum:** subtrair quatorze por cento de mil e duzentos e achar mil e trinta e dois. A conta é divisão, e não subtração.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa de desconto é um imposto sobre o investimento" | Errado | É uma exigência de quem avalia |
| "O custo de oportunidade é a rentabilidade de outro investimento de baixo risco" | Certo | Slides A3474 p. 6 |

**🔗 Ponte:** "Por último, quando as duas taxas se encontram."

---

### Bloco 4 — Quando as duas taxas se encontram — 1 min

> **Objetivo deste bloco:** ao fim, o aluno consegue dizer quando a taxa líquida é igual à bruta.

- "Num produto isento, a conta do restaurante não tem imposto. A bruta é igual à líquida."
- 🔇 Isenção de LCI e LCA para pessoa física citada de memória; conferir na regra vigente.
- **Erro comum:** confundir a taxa real com a líquida. A real desconta a inflação (G1). A líquida desconta o imposto. São duas contas diferentes.

> **Bruta é antes do imposto; líquida é depois; real é depois da inflação.**

- 🔇 **Fechamento:** "O prato é a taxa bruta. O imposto incide sobre o ganho. E a régua da taxa de desconto mede o valor de hoje." Próxima aula: G5, amortização, prazo médio e TIR.

---

## Lista de pegadinhas com nome

1. **Pegadinha do imposto sobre o capital** — "O imposto de renda incide sobre os R$ 10.000 aplicados." Errado: incide sobre o ganho.
2. **Pegadinha da taxa multiplicada** — "Quatorze por cento vezes oitenta e cinco por cento dá a taxa líquida, 11,9%." Errado: o imposto incide sobre o ganho acumulado, e a taxa líquida é 12,01%.
3. **Pegadinha da subtração no desconto** — "Mil e duzentos menos 14% dá mil e trinta e dois." Errado: a conta é divisão por 1,14, e o resultado é 1.052,63.
4. **Pegadinha da palavra gêmea** — "Taxa líquida e taxa real são a mesma coisa." Errado: a líquida desconta o imposto; a real desconta a inflação.

---

## Nota de verificação

- PD 1.3.3.3 e 1.3.3.4 lidos no texto do repositório. Apostila p. 124–125 e slides A3472 e A3474 lidos nesta sessão.
- Cálculos conferidos em Python: 10.000 × 1,14² = 12.996,00; IR 15% sobre 2.996 = 449,40; líquido 12.546,60; taxa líquida anual 12,01%; 1.200 ÷ 1,14 = 1.052,63; 14 × 0,85 = 11,9 (erro comum citado).
- **Não reaberto nesta sessão:** tabela regressiva de IR de renda fixa (22,5%, 20%, 17,5%, 15%) e isenção de LCI e LCA. Citados de memória.
- Convenção: taxa de 14% a.a. e exigência de 14% (didáticos).
- Revisão de estrutura: metáfora única (conta de restaurante), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala.
