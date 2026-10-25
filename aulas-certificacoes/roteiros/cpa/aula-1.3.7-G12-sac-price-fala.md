# Roteiro de fala — Aula CPA: Sistemas de Amortização — SAC (Constante) e Price (Francês)

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), item **1.3.7**; slides A3478 (SAC) e A3479 (Tabela Price); APOSTILA-CPA p. 144–148; aula do repositório `aula-1.3-E-sac-price`, que resolveu os exercícios.

CPA 1.3.7 · Módulo 1 · **20 min** · Aula G12 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Bolo em fatias.** No SAC, as fatias têm sempre o mesmo tamanho de principal, e os juros diminuem à medida que o bolo encolhe. Na Price, a prestação tem sempre o mesmo valor, mas o recheio por dentro muda: cada vez mais é principal, e cada vez menos é juro.

**Onde a metáfora falha:** fatia de bolo não cobra juro. O saldo devedor não encolhe fisicamente, e a prestação da Price não é uma fatia de tamanho fixo de principal. A metáfora ajuda a ver a composição, mas não a taxa.

### 🔇 Caso

**Lucas** financia R$ 60.000 em 12 meses, a 1,8% a.m., e precisa escolher entre o SAC e a Price.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.7 Sistemas de amortização (SAC e Price) | Slides A3478 p. 3–9; slides A3479 p. 3–9; apostila p. 144–148 | Conferido; **taxa equivalente semestral** e **parcela da SAC** |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Apostila p. 144 | 30% a.a. equivale a "14,18% ao semestre" | 14,0175% (1,30^0,5 − 1). A própria apostila (p. 148) e o slide A3478 p. 6 trazem o valor certo |
| 2 | Slides A3479 p. 3 | Price "é mais cara para o tomador" | Com a mesma taxa, a Price paga mais juros no total, porque amortiza mais devagar no começo. O valor presente da dívida é o mesmo. "Mais cara" vale para o total de juros |
| 3 | Slides A3479 p. 3 | "Menor vantagem de se antecipar as parcelas" | Correto na intuição: como os juros caem devagar, quitar antes economiza menos juros no início. Depende do prazo |
| 4 | Slides A3478 p. 4 | "A amortização divide o saldo pelo número de parcelas" | Correto, mas o saldo que se divide é o saldo devedor do início do período. Os juros incidem sobre o saldo, e a parcela cai com ele |
| 5 | Slides A3479 p. 8–9 | Questão de banco (11168) | Substituída por exemplo inédito |

### 🔇 Dados

| Item | Valor |
| --- | --- |
| Financiamento | R$ 60.000, 12 meses, 1,8% a.m. |
| Amortização mensal no SAC | 60.000 ÷ 12 = **R$ 5.000** |
| Parcela 1 no SAC | 5.000 + 60.000 × 1,8% = **R$ 6.080** |
| Parcela 7 no SAC | Saldo antes da 7ª = 30.000 → juros de 540 → **R$ 5.540** |
| Parcela 12 no SAC | 5.000 + 5.000 × 1,8% = **R$ 5.090** |
| Total pago no SAC | **R$ 67.020** (juros de R$ 7.020) |
| Parcela constante na Price | 60.000 × 1,8% ÷ (1 − 1,018⁻¹²) = **R$ 5.604,12** |
| Total pago na Price | 5.604,12 × 12 = **R$ 67.249,42** (juros de R$ 7.249,42) |
| Diferença de juros | A Price paga **R$ 229,42 a mais** no total |

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso de Lucas e o SAC: fatias iguais | 6 min |
| 2. A Price: prestação fixa | 6 min |
| 3. Comparação: quem custa mais | 5 min |
| 4. Fechamento | 3 min |
| **Total** | **20 min** |

---

## 3. Explicação em quatro blocos

### Bloco 1 — Caso de Lucas e o SAC: fatias iguais — 6 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular a parcela de um financiamento pelo SAC em qualquer mês.

- "Lucas pega sessenta mil reais emprestados, para pagar em doze meses, a um e oito décimos por cento ao mês. Antes de calcular, duas palavras. **Saldo devedor** é quanto ainda falta pagar. **Amortização** é a parte da prestação que reduz esse saldo. **Juros** são calculados sobre o saldo, e não sobre o valor inicial."
- "No SAC, a amortização é sempre a mesma: sessenta mil divididos por doze, cinco mil por mês. A parte de juros é que muda, porque o saldo muda."
- "No primeiro mês, o saldo é sessenta mil. Os juros são um vírgula oito por cento disso: mil e oitenta. A parcela é cinco mil mais mil e oitenta: seis mil e oitenta."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `60000` `ENTER` `12` `÷` | 🖥️ 5.000,00 | Amortização mensal no SAC |
| 2 | ⌨️ `60000` `ENTER` `1,8` `%` `5000` `+` | 🖥️ 6.080,00 | Parcela 1 |

- "Agora, o sétimo mês. Já foram pagos seis mil de principal, e o saldo é trinta mil. Os juros são quinhentos e quarenta. A parcela é cinco mil e quinhentos e quarenta."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 3 | ⌨️ `30000` `ENTER` `1,8` `%` `5000` `+` | 🖥️ 5.540,00 | Parcela 7 |

- **Erro comum:** achar que a parcela do SAC é fixa. A parte que amortiza é fixa, mas a parcela cai com os juros.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "No SAC, a amortização é constante e a parcela diminui ao longo do tempo" | Certo | Slides A3478 p. 4 |
| "No SAC, os juros incidem sobre o valor inicial do financiamento" | Errado | Incidem sobre o saldo devedor |

> **SAC: fatia de principal igual; o juro cai; a parcela cai junto.**

**🔗 Ponte:** "E a Price? Aqui a prestação não muda."

---

### Bloco 2 — A Price: prestação fixa — 6 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular a prestação fixa da Price e explicar como a composição muda por dentro.

- "Na Price, a prestação é a mesma em todos os meses. Por dentro, porém, a parte que amortiza cresce e a parte de juros diminui. A soma é sempre a mesma."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `60000` `CHS` `PV` `1,8` `i` `12` `n` `PMT` | 🖥️ 5.604,12 | Prestação fixa da Price |
| 2 | ⌨️ `RCL` `PMT` `12` `×` | 🖥️ 67.249,42 | Total pago na Price |

- "A primeira prestação da Price é de cinco mil seiscentos e quatro. Desses, mil e oitenta são juros. Sobram quatro mil quinhentos e vinte e quatro para amortizar. O SAC, no mesmo mês, amortiza cinco mil."
- "Com a mesma taxa, o valor presente da dívida é igual nos dois sistemas. O que muda é o ritmo: a Price amortiza mais devagar no começo, e por isso paga mais juros no total."
- **Erro comum:** achar que a Price tem amortização constante, como o SAC. Na Price, o que é constante é a prestação, e não a amortização.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Na Price, a prestação é constante e os juros diminuem ao longo do tempo" | Certo | Slides A3479 p. 4 |
| "Com a mesma taxa, a Price tem valor presente maior que o SAC" | Errado | O valor presente é o mesmo |

**🔗 Ponte:** "Então, qual dos dois custa mais?"

---

### Bloco 3 — Comparação: quem custa mais — 5 min

> **Objetivo deste bloco:** ao fim, o aluno consegue comparar SAC e Price pelo total de juros e pela primeira parcela.

| Critério | SAC | Price |
| --- | --- | --- |
| Primeira parcela | **R$ 6.080** (mais alta) | R$ 5.604 |
| Última parcela | **R$ 5.090** (mais baixa) | R$ 5.604 |
| Total de juros | **R$ 7.020** | R$ 7.249 |
| Amortização no início | Maior | Menor |

- "O SAC custa menos no total, porque amortiza mais cedo. A Price custa mais no total, mas a primeira parcela é menor. Quem tem fôlego no começo economiza com o SAC. Quem precisa de parcela leve no começo fica melhor com a Price."
- **Erro comum:** concluir que a Price é sempre mais cara. Com a mesma taxa e o mesmo prazo, ela paga mais juros no total, e isso é tudo o que a comparação mostra.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O SAC tem total de juros menor que a Price para a mesma taxa e prazo" | Certo | Amortiza mais cedo |
| "A Price tem primeira parcela menor que a do SAC" | Certo | Por dentro, a Price mistura principal e juros |

> **Mesma taxa, mesmo prazo: o SAC paga menos juros no total; a Price tem parcela leve no começo.**

**🔗 Ponte:** "E para Lucas, qual escolha faz sentido?"

---

### Bloco 4 — Fechamento — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue escolher entre SAC e Price conforme a capacidade de pagamento.

- "Se Lucas consegue pagar seis mil e oitenta no primeiro mês, o SAC é mais barato. Se a parcela precisa caber em cinco mil e seiscentos desde o início, a Price é a escolha."
- **Erro comum:** escolher pela parcela inicial menor e esquecer o total de juros. Ou o contrário: escolher pelo total e não caber no orçamento do primeiro mês.
- Em qualquer dos dois, a taxa precisa ser comparada pelo custo efetivo total, como na F6. O sistema de amortização muda o fluxo, mas não substitui a conta do custo.

> **O sistema muda o fluxo de pagamentos; o custo efetivo continua sendo a referência.**

- 🔇 **Fechamento:** "O SAC é o bolo em fatias iguais: paga menos juros e tem primeira parcela alta. A Price é a prestação fixa: parcela leve no começo e mais juros no total." Próxima aula do bloco: encerramento do módulo 1.

---

## Lista de pegadinhas com nome

1. **Pegadinha da parcela fixa do SAC** — "No SAC, a parcela é fixa." Errado: a amortização é fixa; a parcela cai com os juros.
2. **Pegadinha do juro sobre o valor inicial** — "No SAC, os juros incidem sobre R$ 60.000 todo mês." Errado: incidem sobre o saldo devedor.
3. **Pegadinha da Price mais cara no valor presente** — "Com a mesma taxa, a Price tem valor presente maior." Errado: o valor presente é o mesmo; a Price paga mais juros no total.
4. **Pegadinha do "sempre"** — "A Price é sempre mais cara." Errado: com a mesma taxa e o mesmo prazo, ela paga mais juros no total, e não necessariamente a primeira parcela.

---

## Nota de verificação

- PD 1.3.7 lido no texto do repositório. Slides A3478 e A3479 e apostila p. 144–148 lidos nesta sessão.
- Cálculos conferidos em Python: amortização 5.000; parcela 1 do SAC = 6.080; parcela 7 = 5.540; parcela 12 = 5.090; juros totais do SAC = 7.020; PMT da Price = 5.604,12; total da Price = 67.249,42; juros = 7.249,42; diferença 229,42; primeiro mês da Price: juros 1.080, principal 4.524,12.
- Convenções: financiamento de R$ 60.000, 12 meses e 1,8% a.m. (didáticos); a questão de banco do slide foi substituída.
- Taxa equivalente semestral: 1,30^0,5 − 1 = 14,0175%.
- Revisão de estrutura: metáfora única (bolo em fatias), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
