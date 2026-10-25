# Roteiro de fala — Aula CPA: Taxa de Juros Nominal e Taxa de Juros Real

**Base:**
- **Programa Detalhado CPA** (ANBIMA, v1.2, rev. 04/06/2025, vigência 01/01/2026), item 1.3.1;
- APOSTILA-CPA, p. 123–125;
- material de aula `00-fontes/materiais-aula/topico-1.3-operacoes-mercado-financeiro/` (slides A3472, p. 11, com o exercício do CDB);
- aula do repositório `aulas/cpa/aula-1.3-A-taxas-nominal-efetiva-real-indexador/aula.md` (40 min), da qual esta é o recorte de 10 min só com o item 1.3.1.

CPA 1.3.1 · Módulo 1 · **10 min** · Aula G1 do plano de gravação · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ✏️ = correção da fonte · ➕ = acréscimo desta versão · 🔗 = ponte · ⌨️ = teclas da HP12C · 🖥️ = visor.

---

## Bastidor — antes de gravar

### 🔇 Formato

- Direto aos tópicos do PD, sem as demais etapas.
- Fio condutor: o **salário de R$ 1.000**. Em um ano de inflação de 5%, o aumento "de 14%" compra menos do que parece. O exemplo serve para o contraste nominal × real.
- A efetiva (1.3.4.1) fica na G9, e a equivalência de taxas, na G2. Aqui só o par nominal × real.

### 🔇 Checagem de escopo (PD × materiais)

| Subitem do PD | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.1 Taxa de juros nominal e real: como se relacionam e conceitos | Apostila p. 124–125; slides A3472 p. 11 | Conferido; **fórmula de Fisher** e exercício do CDB |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto | Base |
| --- | --- | --- | --- | --- |
| 1 | Apostila p. 124 | "A taxa real é a que desconta o efeito da inflação" (sem fórmula exata) | A fórmula exata é **(1 + nominal) = (1 + real) × (1 + inflação)**. A subtração (nominal − inflação) é só **aproximação** | Fórmula de Fisher |
| 2 | Apostila p. 124 | "Nominal de 10% e inflação de 4% → real de **aproximadamente** 5,77%" | Correto como resultado exato da fórmula: 1,10 ÷ 1,04 − 1 = 5,77%. A subtração daria 6%, que é o erro a evitar | Cálculo conferido |
| 3 | Apostila p. 125 | "Taxa aparente (ou **bruta**)" = nominal, sem descontar inflação **ou outros custos** | Cuidado com o termo: **bruta** aqui significa **antes dos impostos**. Para inflação, é o nominal. A taxa bruta × líquida está na aula 1.3-A e na G1 não entra | Apostila p. 125 |
| 4 | Apostila p. 125 | Exemplo "12% com inflação de 6% → real de cerca de 5,66%" | Correto: 1,12 ÷ 1,06 − 1 = 5,66%. A subtração daria 6%, o mesmo erro | Cálculo conferido |
| 5 | Apostila p. 123–125 | Subitens numerados como "1.80" e "1.81" | Numeração do PD: 1.3.1 | PD CPA |

### 🔇 Dados dos exemplos

| Item | Valor |
| --- | --- |
| CDB de 14% a.a. com IPCA de 5,5% (exercício do slide) | Real de **8,06%** a.a. |
| Aplicação de 12% com inflação de 6% (apostila) | Real de **5,66%** a.a. |
| Diferença entre a subtração e Fisher no caso do CDB | 8,50% × 8,06%: **0,44 ponto** |
| Salário de R$ 1.000 com aumento nominal de 8% e inflação de 5% | Ganho real de **2,86%** |

### 🔇 Cronograma

| Tópico | Tempo |
| --- | --- |
| 3.1 Taxa nominal: o que ela anuncia | 2 min |
| 3.2 Taxa real e a fórmula de Fisher | 5 min |
| 3.3 Leitura do resultado: positiva, zero ou negativa | 3 min |
| **Total** | **10 min** |

---

## 3. Explicação dos tópicos — 10 min

### 3.1 Taxa nominal: o que ela anuncia — 2 min · CPA 1.3.1 · Apostila p. 124

- **A definição**
  - "A taxa nominal é a taxa declarada ou anunciada em contrato, produto ou propaganda. Quando o banco diz 'juros de 24% ao ano', está falando da nominal."

- **O que ela não mostra**
  - "A nominal não diz quanto o dinheiro ganhou de poder de compra. Ela ignora a inflação. Por isso, precisamos de uma segunda taxa."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa nominal é a anunciada em contratos e produtos" | Certo | Apostila p. 124 |
| "A taxa nominal já desconta a inflação" | Errado | Ela **não** desconta a inflação |

> **Nominal é o que está escrito; real é o que sobra depois da inflação.**

**🔗 Ponte:** "Como calcular essa sobra?"

---

### 3.2 Taxa real e a fórmula de Fisher — 5 min · CPA 1.3.1 · Apostila p. 124–125

- **A taxa real**
  - "A taxa real é o ganho de poder de compra: o que a aplicação rendeu acima da inflação."

- **A fórmula**
  - "A fórmula exata é a de Fisher: um mais a nominal é igual a um mais a real, multiplicado por um mais a inflação. Isolando a real, divide-se, em vez de subtrair."

> **(1 + nominal) = (1 + real) × (1 + inflação)**
>
> **Taxa real = (1 + nominal) ÷ (1 + inflação) − 1**

- ✏️ **Por que não subtrair**
  - "A subtração, 14% menos 5,5%, dá 8,5%. Parece certo, mas é aproximação. A conta exata é 8,06%. A diferença cresce com a inflação. Com 12% e 6%, a subtração dá 6%, e a conta exata dá 5,66%."

- **O exemplo do CDB**
  - "Um CDB paga 14% ao ano, e o IPCA foi de 5,5%. Qual é o ganho real?"

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1,14` `ENTER` `1,055` `÷` | 🖥️ 1,0806 | Fator de crescimento real |
| 2 | ⌨️ `1` `−` `100` `×` | 🖥️ 8,06 | Taxa real em % ao ano |

  - 🔇 Na HP12C, `f` `2` deixa duas casas decimais. O valor 1,14 é o fator da taxa nominal; por isso, dividir por 1,055 é a mesma coisa que aplicar a fórmula.

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A taxa real é obtida dividindo (1 + nominal) por (1 + inflação) e subtraindo 1" | Certo | Fisher |
| "A taxa real de 14% com inflação de 5,5% é 8,5%" | Errado | É **8,06%**; 8,5% é aproximação |
| "A taxa real de 12% com inflação de 6% é de 6%" | Errado | É **5,66%** |

> **Na taxa real, divide; não subtrai.**

**🔗 Ponte:** "E o que significa o sinal do resultado?"

---

### 3.3 Leitura do resultado: positiva, zero ou negativa — 3 min · CPA 1.3.1

- **Três situações**

| Situação | Leitura |
| --- | --- |
| Nominal **maior** que a inflação | Taxa real **positiva**: ganhou poder de compra |
| Nominal **igual** à inflação | Taxa real **zero**: o dinheiro mantém o poder de compra |
| Nominal **menor** que a inflação | Taxa real **negativa**: perdeu poder de compra |

- **O salário da Lia**
  - "Lia ganha 1.000 reais e recebe um aumento de 8%, com inflação de 5%. O salário nominal subiu 80 reais. O real sobe cerca de 2,86%: Lia ganha 1.080 reais e o custo de vida subiu 5%."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1,08` `ENTER` `1,05` `÷` | 🖥️ 1,0286 | Fator de ganho real |
| 2 | ⌨️ `1` `−` `100` `×` | 🖥️ 2,86 | Ganho real de 2,86% |

  - 🔇 O salário real é o mesmo que o nominal de 1.080 dividido pelo custo de vida de 1.050, que dá 1.028,57 em valor de hoje.

- **O erro de quem sobe ou desce no sinal**
  - "Se a taxa nominal fica abaixo da inflação, o resultado real é negativo mesmo que o investimento tenha rendido. Quem aplicou a 3% com inflação de 10% perdeu poder de compra: 3% ÷ 10% dá uma taxa real de −6,36%."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1,03` `ENTER` `1,10` `÷` | 🖥️ 0,9364 | Fator real menor que 1 |
| 2 | ⌨️ `1` `−` `100` `×` | 🖥️ −6,36 | Taxa real negativa |

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Quando a nominal é igual à inflação, a taxa real é zero" | Certo | Fisher |
| "Uma aplicação que rende positivo sempre aumenta o poder de compra" | Errado | Pode ser negativa, se a inflação for maior |
| "Com nominal menor que a inflação, a taxa real é negativa" | Certo | Fisher |

> **Positiva, zero ou negativa: a inflação é o teste de verdade.**

- 🔇 Fechamento em uma frase (sem etapa de revisão): "A nominal é o que está anunciado; a real é o ganho de poder de compra, obtido pela fórmula de Fisher, que divide em vez de subtrair; e o sinal da real diz se o dinheiro ganhou ou perdeu poder de compra." Próxima aula do bloco: G2, capitalização simples × composta.

---

## Nota de verificação

- **Programa Detalhado CPA** (v1.2, rev. 04/06/2025, vigência 01/01/2026): item 1.3.1 lido no texto do PD do repositório.
- **Apostila CPA**, p. 123–125: lidas nesta sessão.
- **Material de aula** (slides A3472, p. 11): exercício do CDB de 14% com IPCA de 5,5%, lido na aula do repositório.
- **Aula do repositório 1.3-A** (28/09/2026): fórmula de Fisher e correções já conferidas ali.
- **Convenções sem força normativa:** o salário de R$ 1.000 com aumento de 8% e inflação de 5% (exemplo didático); a taxa de 3% com inflação de 10% (exemplo para o sinal negativo).
- **Cálculos conferidos em Python:** 1,14 ÷ 1,055 − 1 = 8,06%; 1,12 ÷ 1,06 − 1 = 5,66%; 1,10 ÷ 1,04 − 1 = 5,77%; 1,08 ÷ 1,05 − 1 = 2,86%; 1,03 ÷ 1,10 − 1 = −6,36%.
- **Acréscimos (➕):** o exemplo do salário da Lia, o exemplo da taxa negativa e a comparação entre subtrair e dividir.
