# Roteiro de fala — Aula CPA: Prazo de Retorno (Payback)

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), item **1.3.6**; slides A3477 p. 6–9; aula do repositório `aula-1.3-D-tir-cmpc-duration-retorno-payback`.

CPA 1.3.6 · Módulo 1 · **10 min** · Aula G11 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Barco que se paga.** O investimento é o custo de construir o barco. Cada mês de pesca traz peixe para o caixa. O payback é o tempo até o barco se pagar com o peixe.

**Onde a metáfora falha:** o barco tem custo de manutenção, que o payback simples não desconta. Além disso, o barco continua rendendo depois de pago, e o payback não enxerga esse período. Por isso a aula também trabalha o payback descontado e o VPL.

### 🔇 Caso

Uma **food truck de açaí**, com investimento de R$ 24.000 e entradas líquidas que crescem a cada ano.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.6 Payback | Slides A3477 p. 6–9 | Conferido; **versão simples e descontada** |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3477 p. 6 | Payback é "tempo necessário para recuperar o capital investido" | Correto, mas incompleto: o payback simples ignora o valor do dinheiro no tempo |
| 2 | Slides A3477 p. 8 | Máquina com lucro de R$ 5.000 por mês e custo de R$ 30.000 → 6 meses | Correto: 30.000 ÷ 5.000 = 6. Vale porque o fluxo é constante |
| 3 | Slides A3477 p. 9 | "Sobra de R$ 15.500 de caixa" depois da máquina | Conta correta, mas mistura o payback com a antecipação de recebíveis (G10). São decisões separadas |
| 4 | Slides A3477 p. 6 | Payback como critério único | Não é critério de valor: um projeto pode ter payback curto e destruir valor (G5 e G6) |

### 🔇 Dados

| Ano | Entrada líquida | Acumulado simples | Valor presente a 10% | Acumulado descontado |
| --- | --- | --- | --- | --- |
| 1 | 3.000 | 3.000 | 2.727,27 | 2.727,27 |
| 2 | 5.000 | 8.000 | 4.132,23 | 6.859,50 |
| 3 | 7.000 | 15.000 | 5.259,21 | 12.118,71 |
| 4 | 9.000 | **24.000** | 6.147,12 | 18.265,83 |
| 5 | 10.000 | 34.000 | 6.209,21 | 24.475,04 |

- **Payback simples:** exatamente **4 anos**.
- **Payback descontado a 10% a.a.:** no ano 4 faltam 5.734,17; o fluxo do ano 5, já descontado, é 6.209,21. Logo, 4 + 5.734,17 ÷ 6.209,21 = **4,92 anos**.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso da food truck: o barco e o peixe | 2 min |
| 2. A conta simples: quatro anos | 2 min |
| 3. O valor do tempo: payback descontado | 4 min |
| 4. Quando o payback engana | 2 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — Caso da food truck: o barco e o peixe — 2 min

> **Objetivo deste bloco:** ao fim, o aluno consegue definir payback e dizer o que ele mede.

- "Uma food truck de açaí custa vinte e quatro mil reais. Cada ano, ela deixa um lucro líquido, que cresce conforme o ponto ganha clientela. Quanto tempo leva para o dinheiro voltar?"
- "O **payback** é esse tempo: quanto leva para os fluxos do projeto cobrirem o investimento inicial. Quanto menor, mais rápido o dinheiro volta."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Payback é o tempo necessário para recuperar o capital investido" | Certo | Slides A3477 p. 6 |
| "Payback menor significa projeto sempre mais rentável" | Errado | Payback mede liquidez, não rentabilidade |

**🔗 Ponte:** "A conta mais direta é somar os anos até cobrir o investimento."

---

### Bloco 2 — A conta simples: quatro anos — 2 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o payback simples a partir do acumulado.

- "Os primeiros quatro anos deixam três mil, cinco mil, sete mil e nove mil. Somados, dão vinte e quatro mil, exatamente o investimento. O payback simples é de quatro anos."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `3000` `ENTER` `5000` `+` `7000` `+` `9000` `+` | 🖥️ 24.000,00 | Soma dos quatro primeiros anos |

- **Erro comum:** dividir o investimento pela média das entradas: vinte e quatro mil dividido por seis mil e oitocentos, que é a média dos cinco anos, dá três vírgula cinquenta e três anos. A conta certa soma o acumulado, ano a ano, e não usa média.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O payback simples desconta o valor do dinheiro no tempo" | Errado | Não desconta |
| "No payback simples, a food truck se paga no ano 4" | Certo | Acumulado de 24.000 no ano 4 |

**🔗 Ponte:** "Mas quatro anos de hoje valem o mesmo que quatro anos daqui a dez?"

---

### Bloco 3 — O valor do tempo: payback descontado — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o payback descontado e explicar por que ele é maior que o simples.

- "Um real de daqui a quatro anos vale menos que um real de hoje, porque o dinheiro de hoje pode render. O **payback descontado** traz cada fluxo para hoje antes de somar."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `10000` `ENTER` `1,1` `ENTER` `5` `y^x` `÷` | 🖥️ 6.209,21 | Fluxo do ano 5 trazido a valor presente |
| 2 | ⌨️ `24000` `ENTER` `18265,83` `−` `6209,21` `÷` `4` `+` | 🖥️ 4,92 | Payback descontado, em anos |

- "Com a taxa de dez por cento ao ano, o payback descontado é quatro vírgula noventa e dois anos. Quase um ano a mais que o simples."
- 🔇 No passo 2, o número 18.265,83 é o acumulado descontado até o ano 4, da tabela do bastidor.
- **Erro comum:** achar que o payback descontado é menor que o simples. Como o desconto encolhe os fluxos futuros, ele é sempre igual ou maior.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O payback descontado é sempre menor que o payback simples" | Errado | É igual ou maior |
| "O payback descontado considera o custo de oportunidade do dinheiro" | Certo | Desconto pela taxa |

> **Payback descontado: o barco se paga quando o dinheiro, trazido a hoje, cobre o investimento.**

**🔗 Ponte:** "E quando o payback engana? Veja o último bloco."

---

### Bloco 4 — Quando o payback engana — 2 min

> **Objetivo deste bloco:** ao fim, o aluno consegue dizer por que payback não basta para decidir.

- "O payback ignora tudo o que vem depois de se pagar. Imagine dois projetos, ambos com payback de quatro anos. Um continua rendendo dez mil por ano durante dez anos. O outro para no ano quatro. O payback é igual, mas o valor é muito diferente."
- "Por isso a decisão precisa do VPL ou da TIR. Payback é indicador de liquidez, e não de valor."
- **Erro comum:** escolher o projeto de payback mais curto mesmo com VPL negativo. Payback curto não compensa valor negativo.

> **Payback mede a liquidez; o valor está depois dele. Para decidir, use o VPL.**

- 🔇 **Fechamento:** "O barco se paga em quatro anos pela conta simples e em quase cinco pela descontada. O tempo tem preço, e o payback mede a pressa do dinheiro, não o valor do negócio." Próxima aula: G12, sistemas de amortização.

---

## Lista de pegadinhas com nome

1. **Pegadinha da média** — "Payback é o investimento dividido pela média das entradas: 3,53 anos." Errado: some o acumulado ano a ano.
2. **Pegadinha do desconto menor** — "O payback descontado é sempre menor." Errado: é igual ou maior.
3. **Pegadinha do payback como valor** — "Payback curto significa o melhor projeto." Errado: payback mede liquidez.
4. **Pegadinha do depois** — "Depois do payback, o projeto não importa mais." Errado: o valor do projeto está justamente nos anos seguintes.

---

## Nota de verificação

- PD 1.3.6 lido no texto do repositório. Slides A3477 p. 6–9 lidos nesta sessão.
- Cálculos conferidos em Python: acumulado simples 3.000, 8.000, 15.000, 24.000, 34.000; valor presente a 10%: 2.727,27; 4.132,23; 5.259,21; 6.147,12; 6.209,21; acumulado descontado até o ano 4 = 18.265,83; payback descontado = 4 + (24.000 − 18.265,83) ÷ 6.209,21 = 4,92 anos; média das entradas 6.800 e 24.000 ÷ 6.800 = 3,53 anos.
- Convenções: entradas da food truck e taxa de 10% a.a. (didáticas).
- Revisão de estrutura: metáfora única (barco que se paga), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
