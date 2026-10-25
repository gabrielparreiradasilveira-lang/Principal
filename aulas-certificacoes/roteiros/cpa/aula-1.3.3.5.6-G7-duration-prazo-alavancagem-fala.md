# Roteiro de fala — Aula CPA: Duration × Prazo e Alavancagem Financeira

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3.5.6** e **1.3.3.5.6.1**; slides A3476 p. 3–7; aula do repositório `aula-1.3-D-tir-cmpc-duration-retorno-payback`, que traz as correções sobre duration e alavancagem.

CPA 1.3.3.5.6 · 1.3.3.5.6.1 · Módulo 1 · **10 min** · Aula G7 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Gangorra.** Os pagamentos de um título são pesos colocados ao longo de uma gangorra. A duration é o ponto de apoio, onde o peso médio se equilibra. Quando o juro sobe, a gangorra inclina, e quanto mais o peso está longe do apoio, mais ela balança.

**Onde a metáfora falha:** a gangorra tem um peso físico e um ponto de apoio. A duration é uma média de tempos ponderada pelo valor presente de cada pagamento, e não uma força física. E a alavancagem, que a gangorra não mostra, tem um custo: o juro da dívida.

### 🔇 Casos

**Caso 1:** um título de 3 anos, valor nominal de 100, com cupom de 10% a.a., comparado com um zero cupom de mesmo prazo, à mesma taxa de 10% a.a.

**Caso 2:** um investidor com R$ 10.000 de capital próprio toma R$ 40.000 a 12% a.a. e compra um imóvel de R$ 50.000 para alugar.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3.5.6 Duration × prazo | Slides A3476 p. 3, 6 | Conferido; **duration ponderada pelo valor presente** |
| 1.3.3.5.6.1 Alavancagem e custo de captações | Slides A3476 p. 4, 7; apostila p. 135 | Conferido; **ganho só amplia se o retorno superar o custo da dívida** |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3476 p. 6 | Duration = "prazo médio ponderado dos fluxos de caixa" | Duration (Macaulay) é o prazo médio ponderado pelo valor presente de cada fluxo |
| 2 | Slides A3476 p. 7 | "Ativo sobe 10%, lucro de R$ 10 mil com R$ 10 mil investidos: +100%" | A conta ignora o juro da dívida. A alavancagem amplia o ganho só quando o retorno supera o custo da dívida |
| 3 | Slides A3476 p. 7 | Ao cair 10%, "perde tudo o que tinha" | A perda depende do nível de alavancagem. O caso 2 mostra uma perda de 23% do capital próprio |
| 4 | Slides A3476 p. 6 | Cupom → menor duration; sem cupom → maior | Correto: o cupom antecipa parte do retorno e reduz a duration |

### 🔇 Dados

**Caso 1 (taxa de 10% a.a., nominal de 100, 3 anos):**

| Título | Fluxos | Preço | Duration |
| --- | --- | --- | --- |
| Com cupom de 10% a.a. (bullet no fim) | 10, 10, 110 | **100,00** | **2,74 anos** |
| Zero cupom | 0, 0, 100 | 75,13 | **3,00 anos** |

**Caso 2 (capital próprio de 10.000; dívida de 40.000 a 12% a.a.; ativo de 50.000):**

| Retorno do ativo | Lucro bruto | Juro da dívida | Lucro líquido | Retorno sobre o capital próprio |
| --- | --- | --- | --- | --- |
| 15% | 7.500 | 4.800 | 2.700 | **27%** |
| 10% | 5.000 | 4.800 | 200 | **2%** |
| 5% | 2.500 | 4.800 | −2.300 | **−23%** |

🔇 Valores hipotéticos. A duration do caso 1 é calculada pela tabela de fluxos descontados: some t × VP de cada fluxo e divida pelo preço.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso 1: a gangorra com cupom e sem cupom | 4 min |
| 2. Duration e prazo: não são a mesma coisa | 2 min |
| 3. Caso 2: a alavanca de um imóvel | 3 min |
| 4. Fechamento | 1 min |
| **Total** | **10 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — Caso 1: a gangorra com cupom e sem cupom — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue explicar por que dois títulos de mesmo prazo têm durations diferentes.

- "Imagine dois títulos de três anos. Um paga cupom de dez por cento por ano, e no fim devolve o principal. Outro não paga nada no meio: recebe tudo no fim. Os dois têm o mesmo prazo. Qual balança mais quando o juro sobe?"
- "A **duration** é o ponto de apoio dos pagamentos: o prazo médio pesado pelo valor presente. Quando o peso está concentrado no fim, o apoio fica longe do começo, e a gangorra balança mais."
- "O título com cupom tem duration de dois vírgula setenta e quatro anos. O zero cupom tem três anos."
- **Erro comum:** achar que duration é o mesmo que prazo. Só são iguais no zero cupom. No título com cupom, parte do dinheiro chega antes, e a duration é menor.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A duration é o prazo médio ponderado pelo valor presente dos fluxos" | Certo | Macaulay |
| "Título com cupom tem duration maior que o zero cupom de mesmo prazo" | Errado | Tem menor duration |

**🔗 Ponte:** "Mas o que muda, na prática, quando o juro sobe?"

---

### Bloco 2 — Duration e prazo: não são a mesma coisa — 2 min

> **Objetivo deste bloco:** ao fim, o aluno consegue distinguir prazo de duration.

- "Prazo é quanto falta para o vencimento. Duration é o quanto o preço reage ao juro. Quanto maior a duration, maior a sensibilidade: se o juro sobe um ponto, o preço cai, aproximadamente, duration vezes um ponto."
- **Erro comum:** achar que o cupom não muda nada na sensibilidade ao juro. O cupom muda a duration, e a sensibilidade cai com ele.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Maior duration significa maior sensibilidade do preço à taxa" | Certo | Slides A3476 p. 6 |
| "Prazo e duration são sempre iguais" | Errado | Só são iguais no zero cupom |

**🔗 Ponte:** "Agora a alavanca, que amplia o efeito de tudo isso."

---

### Bloco 3 — Caso 2: a alavanca de um imóvel — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o retorno sobre o capital próprio com dívida e identificar quando a alavanca ajuda ou atrapalha.

- "Um investidor põe dez mil de capital e toma quarenta mil a doze por cento ao ano, para comprar um imóvel de cinquenta mil que vai alugar. Se o imóvel valorizar quinze por cento, quanto sobra para ele?"
- "O imóvel valoriza sete mil e quinhentos. Ele paga quatro mil e oitocentos de juros. Sobram dois mil e setecentos, que são vinte e sete por cento do capital próprio de dez mil."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `7500` `ENTER` `4800` `−` | 🖥️ 2.700,00 | Lucro líquido, com imóvel valorizando 15% |
| 2 | ⌨️ `10000` `÷` `100` `×` | 🖥️ 27,00 | Retorno sobre o capital próprio, em % |

- 🔇 Repita a conta com o lucro bruto de 5.000 (10%) e de 2.500 (5%), para mostrar os outros cenários da tabela.
- **Erro comum:** multiplicar o retorno do imóvel pela alavancagem: quinze por cento vezes cinco dá setenta e cinco por cento. A dívida tem custo, e ele precisa ser subtraído antes.
- No cenário de cinco por cento, o imóvel rende menos que o juro. O investidor perde vinte e três por cento do capital próprio. A mesma alavanca que ampliou o ganho amplia a perda.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A alavancagem amplia o ganho sempre, independentemente do custo da dívida" | Errado | Só amplia se o retorno supera o juro |
| "Com alavancagem, a perda pode ser maior que o capital próprio investido" | Certo | Amplifica a perda |

**🔗 Ponte:** "Vamos fechar com a regra que resume as duas ideias."

---

### Bloco 4 — Fechamento — 1 min

> **Objetivo deste bloco:** ao fim, o aluno consegue dizer, em uma frase, o que a duration e a alavancagem medem.

> **Duration mede a sensibilidade do preço ao juro; alavancagem mede quanto a dívida amplia o resultado.**

- 🔇 **Fechamento:** "A gangorra mostra que o peso no tempo define a sensibilidade ao juro. A alavanca mostra que a dívida amplia tudo, para o bem e para o mal." Próxima aula: G8, retorno histórico e esperado.

---

## Lista de pegadinhas com nome

1. **Pegadinha da duration igual ao prazo** — "Dois títulos de 3 anos têm a mesma duration." Errado: o zero cupom tem 3,00, e o título com cupom tem 2,74.
2. **Pegadinha do cupom sem efeito** — "O cupom não muda a sensibilidade ao juro." Errado: reduz a duration.
3. **Pegadinha da multiplicação** — "Com alavancagem de 5 vezes, um retorno de 15% vira 75%." Errado: o juro da dívida precisa ser descontado.
4. **Pegadinha do ganho sem perda** — "Alavancagem só amplia lucro." Errado: amplia a perda também.

---

## Nota de verificação

- PD 1.3.3.5.6 e 1.3.3.5.6.1 lidos no texto do repositório. Slides A3476 lidos nesta sessão.
- Cálculos conferidos em Python: duration do título de 10% a.a. em 3 anos (preço 100) = 2,7355 anos; zero cupom a 10% = 3,00 anos (preço 75,13); alavancagem: (7.500 − 4.800) ÷ 10.000 = 27%; 2%; −23%.
- Convenções: capital de 10.000, dívida de 40.000 a 12% a.a. e cenários de 15%, 10% e 5% (didáticos).
- Revisão de estrutura: metáfora única (gangorra), casos antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
