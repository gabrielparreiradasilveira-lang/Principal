# Roteiro de fala — Aula CPA: Duration × Prazo e Alavancagem Financeira

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3.5.6** e **1.3.3.5.6.1**; slides A3476 p. 3–4 e 6–7 (duration, prazo, alavancagem); aula do repositório `aula-1.3-D-tir-cmpc-duration-retorno-payback`, que traz as correções sobre duration e alavancagem.

CPA 1.3.3.5.6 · 1.3.3.5.6.1 · Módulo 1 · **10 min** · Aula G7 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula usa a **gangorra**. A duration é o **ponto de apoio** da gangorra: onde o peso dos pagamentos se concentra no tempo. Quanto mais o peso está longe do ponto de apoio, mais a gangorra balança quando o juro sobe. A alavancagem é a **alavanca** que multiplica a força de quem empurra, para cima ou para baixo.

- Caso 1: um título de 3 anos com cupom, e outro sem cupom. Qual balança mais quando o juro sobe?
- Caso 2: um investidor que toma emprestado para comprar um imóvel e alugar. A alavanca amplia o ganho e a perda.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3.5.6 Duration × prazo | Slides A3476 p. 3, 6 | Conferido; **duration ponderada pelo valor presente** |
| 1.3.3.5.6.1 Alavancagem e custo de captações | Slides A3476 p. 4, 7; apostila p. 135 | Conferido; **ganho só amplia se o retorno superar o custo da dívida** |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3476 p. 6 | Duration = "prazo médio ponderado dos fluxos de caixa" | Duration (Macaulay) é o prazo médio ponderado pelo **valor presente** de cada fluxo. O prazo médio simples pondera pelos valores **nominais** |
| 2 | Slides A3476 p. 7 | "Ativo sobe 10%, você lucra R$ 10 mil com R$ 10 mil investidos: +100% de retorno" | A conta **ignora o juro da dívida**. A alavancagem amplia o ganho só quando o retorno do ativo supera o custo da dívida |
| 3 | Slides A3476 p. 7 | "Perde tudo o que tinha" ao cair 10% | Com 10% de queda e alavancagem de 5 vezes, a perda é de 50% do capital próprio, e não 100%. A conta do slide usa 10 mil de capital; a aula corrige o cenário |
| 4 | Slides A3476 p. 6 | "Título com cupom → menor duration; sem cupom → maior" | Correto: o cupom antecipa parte do retorno e reduz a duration |

### 🔇 Dados dos exemplos

**Caso 1 — duration (taxa de 10% a.a., nominal de 100, 3 anos):**

| Título | Fluxos | Preço | Duration |
| --- | --- | --- | --- |
| Com cupom de 10% a.a. (bullet no fim) | 10, 10, 110 | **100,00** | **2,74 anos** |
| Sem cupom (zero cupom) | 0, 0, 100 | 75,13 | **3,00 anos** |

**Caso 2 — alavancagem (capital próprio de 10.000, dívida de 40.000 a 12% a.a.):**

| Retorno do ativo (sobre 50.000) | Lucro bruto | Juro da dívida | Lucro líquido | Retorno sobre o capital próprio |
| --- | --- | --- | --- | --- |
| 15% | 7.500 | 4.800 | 2.700 | **27%** |
| 10% | 5.000 | 4.800 | 200 | **2%** |
| 5% | 2.500 | 4.800 | −2.300 | **−23%** |

🔇 Valores hipotéticos. Mostram que a alavanca amplifica o ganho e a perda, e que a dívida só compensa quando o retorno passa do custo do juro.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. A gangorra: duration | 4 min |
| 2. Duration × prazo na prática | 2 min |
| 3. A alavanca: alavancagem financeira | 3 min |
| 4. Fechamento | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — A gangorra: duration — 4 min

- "Duration é o ponto de apoio dos pagamentos: o prazo médio **pesado pelo valor presente**. Se o peso está concentrado perto do começo, a gangorra balança pouco. Se está no fim, balança muito."
- ✏️ "O slide diz que a duration é prazo médio ponderado dos fluxos. Precisa do adjetivo: pelo valor presente. Sem isso, é o prazo médio simples."
- "Um título sem cupom concentra tudo no fim: duration de 3 anos. Um com cupom antecipa parte do dinheiro: duration de 2,74 anos."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
🔇 A duration de Macaulay não é uma tecla simples da HP12C. Monte a tabela de fluxos descontados (VP de cada fluxo), some t × VP e divida pelo preço. A tabela do bastidor é a conta.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A duration é o prazo médio ponderado pelo valor presente dos fluxos" | Certo | Macaulay |
| "Título com cupom tem duration maior que o zero cupom de mesmo prazo" | Errado | Tem **menor** duration |

> **Duration: o ponto de apoio. Quanto mais o peso está no fim, mais a gangorra balança.**

**🔗 Ponte:** "E quando o juro sobe, a gangorra balança a quanto?"

---

### Bloco 2 — Duration × prazo na prática — 2 min

- "Prazo é quanto falta para o vencimento. Duration é quanto o preço reage ao juro. Dois títulos com o mesmo prazo podem ter durations diferentes."
- "Quanto maior a duration, maior a sensibilidade: se o juro sobe 1 ponto, o preço cai aproximadamente duration vezes 1 ponto."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Prazo e duration são sempre iguais" | Errado | Só são iguais no zero cupom |
| "Maior duration significa maior sensibilidade do preço à taxa" | Certo | Slides A3476 p. 6 |

> **Prazo mede o tempo; duration mede o quanto o preço balança.**

**🔗 Ponte:** "Agora a alavanca, que amplifica tudo isso."

---

### Bloco 3 — A alavanca: alavancagem financeira — 3 min

- "Alavancagem é investir mais do que se tem, usando dinheiro emprestado. Se o retorno do ativo supera o juro, o ganho cresce. Se não supera, a perda cresce."
- ✏️ "O slide diz 'ativo sobe 10%, retorno de 100%'. Esqueceu o juro. A conta correta usa o lucro líquido do juro."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `7500` `ENTER` `4800` `−` | 🖥️ 2.700,00 | Lucro líquido: lucro bruto de 7.500 (15% de 50.000) menos juros de 4.800 (12% de 40.000) |
| 2 | ⌨️ `10000` `÷` `100` `×` | 🖥️ 27,00 | Retorno sobre o capital próprio, em % |

- 🔇 Repita a conta com lucro bruto de 5.000 (10%) e de 2.500 (5%), para mostrar os dois outros cenários da tabela do bastidor.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A alavancagem amplia o ganho sempre, independentemente do custo da dívida" | Errado | Só amplia se o retorno supera o juro |
| "Com alavancagem, a perda pode superar o capital próprio" | Certo | Caso de −23% no cenário de 5% |

> **Alavanca amplia: ganho quando o ativo supera o juro; perda quando não supera.**

**🔗 Ponte:** "Fechamos com a regra que resume as duas."

---

### Bloco 4 — Fechamento — 1 min

> **Duration mede o balanço do preço; alavancagem mede o quanto a dívida amplia o balanço.**

- 🔇 Fechamento: "A gangorra mostra que o peso no tempo define a sensibilidade; a alavanca mostra que a dívida amplia tudo, para o bem e para o mal."

---

## Nota de verificação

- PD 1.3.3.5.6 e 1.3.3.5.6.1 lidos no texto do repositório. Slides A3476 lidos nesta sessão.
- Cálculos conferidos em Python: duration do título de 10% a.a. em 3 anos (bullet, preço 100) = 2,7355 anos; zero cupom de 3 anos a 10% = 3,00 anos (preço 75,13); alavancagem: (50.000 × 15% − 40.000 × 12%) ÷ 10.000 = 27%; 2%; −23%.
- Convenções: capital de 10.000, dívida de 40.000 a 12% a.a. e os cenários de 15%, 10% e 5% (didáticos).
- Sem norma: duration e alavancagem são conceitos de finanças clássicas.
