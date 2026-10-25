# Roteiro de fala — Aula CPA: Capitalização Simples × Composta

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), item **1.3.2**; APOSTILA-CPA p. 123–125; slides A3472 p. 3–8; aula do repositório `aula-1.3-B-capitalizacao-equivalencia-descontos`, da qual só a parte de capitalização é usada aqui.

CPA 1.3.2 · Módulo 1 · **20 min** · Aula G2 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Bola de neve.** Dois empurrões na mesma ladeira: no simples, a bola ganha sempre o mesmo pedaço de neve; no composto, ela ganha um pedaço proporcional ao tamanho que já tem.

**Onde a metáfora falha:** a bola de neve não perde neve e não tem prazo de validade. Na vida real, o juro composto depende de quando a capitalização acontece (mensal, anual), e o cálculo só vale se a taxa e o período estiverem na mesma unidade.

### 🔇 Caso

**Sofia** guarda R$ 8.000 num título que rende 1,5% ao mês, por 18 meses.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.2 Juros simples × juros compostos | Apostila p. 123–125; slides A3472 p. 3–5 | Conferido |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3472 p. 4 | "Taxa proporcional: 2% ao mês → 24% ao ano" | Vale só no simples. Em composto, a taxa anual equivalente é 1,02¹² − 1 = 26,82% |
| 2 | Slides A3472 p. 5 | Fórmula "FV = PV(1+i)^t" sem explicar o expoente | Em composto, o expoente pode ser fracionário, com a taxa na mesma periodicidade do prazo |
| 3 | Slides A3472 p. 5 | Taxa equivalente i₂ = (1 + i₁)^(n₂/n₁) − 1 | Correta, e é a fórmula usada para converter mês em ano |

### 🔇 Dados

| Item | Valor |
| --- | --- |
| Capital | R$ 8.000 |
| Taxa | 1,5% a.m. |
| Prazo | 18 meses |
| Juros simples | 8.000 × 1,5% × 18 = **R$ 2.160,00** → montante **R$ 10.160,00** |
| Juros compostos | 8.000 × 1,015¹⁸ = **R$ 10.458,73** → juros de R$ 2.458,73 |
| Diferença | **R$ 298,73** a favor da composta |
| Mês 6, simples | Juros de **R$ 720** → montante R$ 8.720 |
| Mês 6, composto | 8.000 × 1,015⁶ = **R$ 8.747,55** |
| Taxa anual efetiva da composta | 1,015¹² − 1 = **19,56%** a.a. |

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso de Sofia e os dois conceitos | 3 min |
| 2. Simples: o mesmo pedaço | 4 min |
| 3. Composto: o pedaço que cresce | 4 min |
| 4. Mês 18: a diferença e a taxa anual | 5 min |
| 5. Qual regime e quando | 4 min |
| **Total** | **20 min** |

---

## 3. Explicação em cinco blocos

### Bloco 1 — Caso de Sofia e os dois conceitos — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue explicar com as próprias palavras o que é juro, montante e prazo.

- "Sofia põe oito mil reais num título. O título paga um e meio por cento ao mês, durante dezoito meses."
- "Antes de calcular, três palavras. **Capital** é o dinheiro que se aplica no começo. **Juros** é o que o capital rende. **Montante** é capital mais juros, o que se tem no fim."
- "A pergunta é: quanto Sofia tem no fim? Depende de como os juros são calculados."
- **Erro comum:** "dezoito meses vezes um e meio dá vinte e sete por cento, e esse é o rendimento total." Só é verdade no regime simples, e mesmo assim não é a taxa anual.

**🔗 Ponte:** "Vamos primeiro com a regra mais simples: juros sempre sobre o capital inicial."

---

### Bloco 2 — Simples: o mesmo pedaço — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o juro simples e mostrar que ele é igual em todo período.

- "No regime simples, o juro de cada mês é sempre o mesmo: um e meio por cento do capital inicial, que é oito mil. Cento e vinte reais por mês."
- "Pela regra: **J = C × i × t**. Capital vezes taxa vezes tempo."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `8000` `ENTER` `1,5` `%` `6` `×` | 🖥️ 720,00 | Juros de 6 meses |
| 2 | ⌨️ `8000` `+` | 🖥️ 8.720,00 | Montante no mês 6 |

- "Repare: o juro do mês 6 é o mesmo do mês 1. A bola simples não acelera."
- **Erro comum:** achar que, no simples, o juro do mês 6 é maior porque o saldo cresceu. O saldo cresceu, mas o juro continua calculado sobre o capital inicial.

**🔗 Ponte:** "E se, em vez de repetir o mesmo pedaço, os juros fossem somados ao saldo?"

---

### Bloco 3 — Composto: o pedaço que cresce — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue explicar por que o juro composto é maior a cada período.

- "No regime composto, os juros do mês entram no saldo, e no mês seguinte rendem também. É juro sobre juro."
- "A regra: **M = C × (1 + i)^t**. O montante é o capital vezes um mais a taxa, elevado ao número de meses."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `1,015` `ENTER` `6` `y^x` `8000` `×` | 🖥️ 8.747,55 | Montante composto no mês 6 |

- "No mês 6, a composta está em oito mil setecentos e quarenta e sete reais. O simples está em oito mil e setecentos e vinte. A diferença é de vinte e sete reais, e cresce com o tempo."
- **Erro comum:** usar a fórmula do simples com juro composto, e somar juros mês a mês sobre o capital inicial. Esse erro tira o efeito que dá nome ao regime.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Em composto, os juros de um período passam a render nos períodos seguintes" | Certo | Juros sobre juros |
| "A taxa proporcional é válida para o regime composto" | Errado | Só vale no simples |

**🔗 Ponte:** "E no mês dezoito, que é o prazo de verdade de Sofia?"

---

### Bloco 4 — Mês 18: a diferença e a taxa anual — 5 min

> **Objetivo deste bloco:** ao fim, o aluno consegue comparar os dois regimes no mesmo prazo e converter uma taxa mensal em taxa anual efetiva.

| Regime | Montante no mês 18 | Juros acumulados | Taxa anual |
| --- | --- | --- | --- |
| **Simples** | R$ 10.160,00 | R$ 2.160,00 | 18,00% |
| **Composto** | R$ 10.458,73 | R$ 2.458,73 | 19,56% |

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `8000` `CHS` `PV` `1,5` `i` `18` `n` `FV` | 🖥️ 10.458,73 | Montante composto |
| 2 | ⌨️ `1,015` `ENTER` `12` `y^x` `1` `−` `100` `×` | 🖥️ 19,56 | Taxa anual efetiva |

- "Em um ano e meio, a composta rende quase trezentos reais a mais. E a taxa anual efetiva é 19,56%, e não os dezoito por cento que o simples sugere."
- 🔇 O `CHS` antes do `PV` é só para o montante sair positivo.
- **Erro comum:** multiplicar um e meio por doze e dizer que a taxa anual é dezoito por cento. Isso é a taxa anual do regime simples, e não o rendimento efetivo do composto.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "No mesmo prazo e taxa, o composto rende mais que o simples" | Certo | Desde que haja mais de um período |
| "A taxa efetiva anual de 1,5% ao mês é 18%" | Errado | É 19,56% |

**🔗 Ponte:** "Mas em que situação cada regime aparece na vida real?"

---

### Bloco 5 — Qual regime e quando — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue identificar o regime de uma oferta antes de comparar taxas.

| Regime | Onde aparece | Por quê |
| --- | --- | --- |
| **Simples** | Cálculos didáticos, alguns descontos comerciais, prazos curtos | Simplicidade |
| **Composto** | Aplicações financeiras, empréstimos bancários, padrão de mercado | Reflete o rendimento real |

- "Quando alguém oferece dois por cento ao mês, pergunte: é simples ou composto? A conta anual muda."
- **Erro comum:** achar que, com prazo de um mês, os dois regimes dão resultados diferentes. Dão o mesmo, porque não há juro sobre juro em um período só. A diferença começa no segundo período.

> **Simples cresce pelo capital; composto cresce pelo que já cresceu.**

- 🔇 **Fechamento:** "Duas bolas começam iguais e terminam diferentes. A diferença é só o efeito de crescer sobre o que já cresceu." Próxima aula: G3, fluxos e valor presente.

---

## Lista de pegadinhas com nome

1. **Pegadinha do fator proporcional** — "Dois por cento ao mês são vinte e quatro por cento ao ano." Errado no composto: a taxa anual efetiva é 26,82%.
2. **Pegadinha do juro que cresce no simples** — "No regime simples, o juro do mês seis é maior que o do mês um." Errado: o juro é igual em todo período.
3. **Pegadinha do primeiro período** — "Com um mês de prazo, simples e composto já dão resultados diferentes." Errado: no primeiro período não há juro sobre juro. A diferença começa no segundo.
4. **Pegadinha da escolha pelo número** — "Como a taxa é a mesma, o regime não importa." Errado: a mesma taxa rende diferente conforme o regime, e o regime precisa estar escrito na oferta.

---

## Nota de verificação

- PD 1.3.2 lido no texto do repositório. Apostila p. 123–125 e slides A3472 lidos nesta sessão.
- Cálculos conferidos em Python: simples 2.160,00 e montante 10.160,00; composto 10.458,73; taxa efetiva 19,56%; mês 6 composto 8.747,55 (1,015⁶ × 8.000); simples 8.720,00.
- Convenções: capital de R$ 8.000 e taxa de 1,5% a.m. (didáticos).
- Revisão de estrutura: metáfora única (bola de neve), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala.
