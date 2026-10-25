# Roteiro de fala — Aula CPA: Taxa de Juros Nominal e Taxa de Juros Real

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), item **1.3.1**; APOSTILA-CPA p. 123–125; slides A3472 p. 9–11 (exercício do CDB); aula do repositório `aula-1.3-A-taxas-nominal-efetiva-real-indexador`, da qual esta é o recorte de 10 min.

CPA 1.3.1 · Módulo 1 · **10 min** · Aula G1 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Quantos pães o dinheiro compra.** Toda a aula gira em torno dessa pergunta: o aumento de salário compra mais pão do que antes?

**Onde a metáfora falha:** o pão tem preço próprio, e a inflação não é igual para todos os produtos. A inflação é uma média (o IPCA, por exemplo) que o aluno não vai sentir exatamente igual na sua cesta.

### 🔇 Caso

**Lia** ganha R$ 1.000 e recebe aumento de 8%. A inflação do ano é de 5%.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.1 Taxa nominal e real: como se relacionam, conceitos | Apostila p. 124–125; slides A3472 p. 9–11 | Conferido; fórmula de Fisher |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Apostila p. 124 | Taxa real "desconta o efeito da inflação", sem fórmula exata | Fórmula exata: (1 + nominal) = (1 + real) × (1 + inflação). A subtração é só aproximação |
| 2 | Apostila p. 124 | 10% nominal e 4% de inflação dão real "aproximadamente" 5,77% | Correto: 1,10 ÷ 1,04 − 1 = 5,77%. Subtrair daria 6% |
| 3 | Apostila p. 125 | Taxa "aparente (ou bruta)" = nominal, sem descontar inflação "ou outros custos" | "Bruta" aqui é **antes do imposto**, e não tem relação com a inflação. Separar os dois conceitos |
| 4 | Apostila p. 125 | 12% com inflação de 6% dá real de "cerca de 5,66%" | Correto: 1,12 ÷ 1,06 − 1 = 5,66% |
| 5 | Apostila p. 123–125 | Subitens numerados como "1.80" e "1.81" | Numeração do PD: 1.3.1 |

### 🔇 Dados

| Item | Valor |
| --- | --- |
| Salário de Lia, com aumento de 8% | R$ 1.080 |
| Inflação | 5% |
| Ganho real de Lia | 1,08 ÷ 1,05 − 1 = **2,86%** |
| CDB de 14% a.a. com IPCA de 5,5% (exercício do slide) | Real de **8,06%** a.a. |
| Aplicação de 12% com inflação de 6% (apostila) | Real de **5,66%** a.a. |

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso de Lia: aumento e inflação | 3 min |
| 2. A regra de Fisher | 4 min |
| 3. O sinal do resultado | 3 min |
| **Total** | **10 min** |

---

## 3. Explicação em três blocos

### Bloco 1 — Caso de Lia: aumento e inflação — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue dizer por que um aumento de 8% pode não ser ganho real.

- "Lia ganha mil reais por mês. Recebe um aumento de 8%, e passa a ganhar mil e oitenta. Parece uma boa notícia."
- "Mas o ano teve inflação de 5%. Isso quer dizer que os produtos ficaram 5% mais caros. Antes, com mil reais, ela comprava um certo número de pães. Agora, com mil e oitenta, quantos pães ela compra?"
- "Antes de calcular, duas palavras. **Inflação** é o aumento geral dos preços. **Poder de compra** é a quantidade de bens que o dinheiro consegue comprar."
- "**Taxa nominal** é o número que aparece no contrato ou na propaganda: os oito por cento. **Taxa real** é o ganho depois de tirar a inflação: quanto Lia ganhou de pão, e não de dinheiro."
- **Erro comum:** "oito menos cinco dá três, então o ganho real é três por cento." Não é. A subtração é uma aproximação, e a conta exata dá 2,86%.

**🔗 Ponte:** "Então a conta certa tem que ser feita de outro jeito. Vamos a ela."

---

### Bloco 2 — A regra de Fisher — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular a taxa real com a fórmula de Fisher, e não com a subtração.

- "A regra é: um mais a taxa nominal é igual a um mais a taxa real, multiplicado por um mais a inflação. Isolando a real, a conta **divide**, em vez de subtrair."

> **(1 + nominal) = (1 + real) × (1 + inflação)**
>
> **Taxa real = (1 + nominal) ÷ (1 + inflação) − 1**

- "Agora o caso de Lia, em números: um vírgula oito, dividido por um vírgula cinco, menos um."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1,08` `ENTER` `1,05` `÷` | 🖥️ 1,0286 | Fator de ganho real |
| 2 | ⌨️ `1` `−` `100` `×` | 🖥️ 2,86 | Ganho real de Lia, em % |

- "Dois vírgula oitenta e seis por cento. Ela ganhou um pouco mais de poder de compra, mas bem menos do que os oito que apareceram no papel."
- **Erro comum:** no CDB de 14% com inflação de 5,5%, a subtração dá 8,5%. A conta exata dá **8,06%**. Com 12% e 6%, a subtração dá 6%, e a conta exata dá **5,66%**. A diferença cresce quando a inflação sobe.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa real é obtida dividindo (1 + nominal) por (1 + inflação) e subtraindo 1" | Certo | Fisher |
| "A taxa real de 14% com inflação de 5,5% é 8,5%" | Errado | É 8,06%; 8,5% é aproximação |

> **Na taxa real, divide; não subtrai.**

**🔗 Ponte:** "E quando o ganho real é negativo? Veja um caso."

---

### Bloco 3 — O sinal do resultado — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue ler o sinal da taxa real e dizer se houve ganho ou perda de poder de compra.

- "Imagine que uma aplicação rendeu três por cento, e a inflação foi de dez. O dinheiro cresceu no papel, mas perdeu poder de compra."
- "Se a taxa nominal é maior que a inflação, a real é positiva. Se é igual, a real é zero: o dinheiro só manteve o poder de compra. Se é menor, a real é negativa."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1,03` `ENTER` `1,10` `÷` | 🖥️ 0,9364 | Fator real, menor que 1 |
| 2 | ⌨️ `1` `−` `100` `×` | 🖥️ −6,36 | Taxa real negativa, em % |

- **Erro comum:** "a aplicação rendeu, então ganhou." Rendeu no papel. Se a inflação foi maior, o poder de compra caiu.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Quando a nominal é igual à inflação, a taxa real é zero" | Certo | Fisher |
| "Uma aplicação que rende positivo sempre aumenta o poder de compra" | Errado | Pode ser negativa, se a inflação for maior |

> **Positiva, zero ou negativa: a inflação é o teste de verdade.**

- 🔇 **Fechamento:** "A nominal é o que está anunciado. A real é o ganho de pão, calculado com divisão. E o sinal diz se o dinheiro ganhou ou perdeu poder de compra." Próxima aula: G2, capitalização simples e composta.

---

## Lista de pegadinhas com nome

1. **Pegadinha da subtração** — "A taxa real é 14% menos 5,5%, ou seja, 8,5%." Errado: divide-se, e o resultado é 8,06%.
2. **Pegadinha do "rendeu, logo ganhou"** — "A aplicação rendeu 3% e a inflação foi de 10%, então o investidor ganhou poder de compra." Errado: a taxa real é negativa, e ele perdeu.
3. **Pegadinha da palavra trocada** — "Taxa bruta é a que desconta a inflação." Errado: bruta é antes do imposto. A inflação é tratada pela taxa real.

---

## Nota de verificação

- PD 1.3.1 lido no texto do repositório. Apostila p. 124–125 e slides A3472 lidos nesta sessão.
- Cálculos conferidos em Python: 1,08 ÷ 1,05 − 1 = 2,86%; 1,14 ÷ 1,055 − 1 = 8,06%; 1,12 ÷ 1,06 − 1 = 5,66%; 1,10 ÷ 1,04 − 1 = 5,77%; 1,03 ÷ 1,10 − 1 = −6,36%.
- Convenções: salário de R$ 1.000, aumento de 8% e inflação de 5% (didáticos).
- Revisão de estrutura: metáfora única, caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala.
