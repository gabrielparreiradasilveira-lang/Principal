# Roteiro de fala — Aula CPA: Juros × Tempo de Alocação, Fluxo de Pagamentos, Fluxo de Caixa, VP, VF e VPL

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3**, **1.3.3.1**, **1.3.3.2**, **1.3.3.2.1**, **1.3.3.2.2** e **1.3.3.2.3**; APOSTILA-CPA p. 126–131; slides A3473 (fluxos de caixa e de pagamentos; cupom e bullet) e A3474 (VP, VF, VPL e taxa de desconto); aula do repositório `aula-1.3-C-fluxos-mutuo-vp-vf-vpl`.

CPA 1.3.3 · 1.3.3.1 · 1.3.3.2 · 1.3.3.2.1 · 1.3.3.2.2 · 1.3.3.2.3 · Módulo 1 · **20 min** · Aula G3 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte · ➕ = acréscimo · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Estrutura desta aula

Esta aula é um **filme e seu roteiro**. O **fluxo de pagamentos** é o roteiro escrito antes da filmagem: diz o que deve acontecer e quando. O **fluxo de caixa** é o filme: mostra o que de fato aconteceu. Depois, a aula **traz todas as datas para o mesmo dia**, como quem converte moedas de países diferentes antes de comparar preços. Essa conversão é o valor presente.

- Caso: uma **loja de móveis** recebe 12 cheques de R$ 1.500 e decide se vale pagar R$ 15.000 à vista por eles, ou se é melhor esperar. A conta usa VP e VPL.
- 🔇 A aula não repete o caso do empréstimo de R$ 1.000 em 12 parcelas dos slides. Usa o mesmo tipo de conta, mas com outra pergunta.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3 Juros × tempo de alocação | Apostila p. 126–128 | Conferido |
| 1.3.3.1 Amortização e juros de crédito privado | Slides A3473 p. 6–7 | Conferido; **cupom e bullet** |
| 1.3.3.2 Regime de capitalização em empréstimo e mútuo | Apostila p. 128; aula 1.3-C (CC arts. 586 a 591) | Conferido |
| 1.3.3.2.1 Fluxo de pagamentos | Slides A3473 p. 3 | Conferido |
| 1.3.3.2.2 Fluxo de caixa: cupom e amortização | Slides A3473 p. 3–7 | Conferido |
| 1.3.3.2.3 VP, VF e VPL | Slides A3474 p. 3, 7 | Conferido |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3473 p. 6 | "Títulos sem cupom (**bullet**)" | **Bullet** é o principal pago de uma vez no vencimento, podendo haver cupom no meio. Título **sem cupom** é o **zero cupom** (ex.: LTN). O slide 7 usa "bullet" no sentido certo |
| 2 | Apostila p. 126 | Fluxo de pagamentos é o "registro das saídas" | Fluxo de pagamentos é o **cronograma contratual**, com entradas **ou** saídas. Fluxo de caixa é o que **efetivamente** entrou e saiu |
| 3 | Slides A3474 p. 6 | "Taxa livre de risco: Selic Meta (15%)" | **Número datado, retirado.** A aula ensina o conceito: título público pós-fixado ou a referência de juros do país |
| 4 | Slides A3474 p. 9 | Exemplo com nome próprio de corretor | Trocado por "um corretor" |
| 5 | Apostila p. 130 | VPL de um imóvel = −R$ 3.360 | Com taxa de 15% a.a. convertida para o mês, o cálculo dá ≈ −R$ 3.531,77 (conferido na aula 1.3-C). Não usado aqui |

### 🔇 Dados do exemplo (loja de móveis)

| Item | Valor |
| --- | --- |
| Cheques | 12 parcelas de R$ 1.500, a cada 30 dias, a primeira em 30 dias |
| Taxa de desconto (custo de oportunidade) | 2% a.m. |
| VP dos 12 cheques | **R$ 15.863,01** |
| Pagamento à vista proposto | R$ 15.000 |
| VPL de pagar à vista | 15.000 → **R$ 863,01 de VPL** para quem recebe |

🔇 Caso didático. Para a loja, a leitura correta é: receber parcelado vale R$ 863 mais do que o valor à vista. Se a taxa de desconto fosse 3% a.m., o VP dos cheques cairia e o VPL ficaria negativo para quem pagasse à vista. Confira a taxa de desconto antes de decidir.

**Título com cupom (exemplo do slide, trocado):** nominal R$ 10.000, cupom de 3% por semestre, 3 anos, principal no fim. Descontado a 5% a.s., o VP é **R$ 8.984,86** (cupons de R$ 1.522,71 + principal de R$ 7.462,15).

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. O roteiro e o filme | 4 min |
| 2. Cupom × bullet | 4 min |
| 3. Trazer a data: o valor presente | 5 min |
| 4. VPL e a decisão da loja | 5 min |
| 5. Taxa de desconto: a régua | 2 min |
| **Total** | **20 min** |

---

## 3. Explicação em cinco blocos

### Bloco 1 — O roteiro e o filme — 4 min

- "O **fluxo de pagamentos** é o que está no contrato: quanto e quando. É o roteiro."
- "O **fluxo de caixa** é o que de fato entrou e saiu. É o filme."
- "Os dois podem ser diferentes. Um cheque pré-datado está no roteiro, mas pode não ser pago."

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O fluxo de pagamentos é o registro das saídas de caixa" | Errado | É o cronograma contratual, com entradas ou saídas |
| "O fluxo de caixa mostra o que de fato aconteceu" | Certo | Slides A3473 p. 3 |

> **Pagamentos: o combinado. Caixa: o acontecido.**

**🔗 Ponte:** "Os títulos pagam de um jeito só, ou em partes. Veja a diferença."

---

### Bloco 2 — Cupom × bullet — 4 min

- "Um título **com cupom** paga juros de tempos em tempos, por exemplo a cada semestre. No fim, devolve o principal."
- "Um título **bullet** não paga nada no meio: tudo vem no vencimento, principal mais juros."
- ✏️ "Atenção: um título sem cupom é o **zero cupom**, como a LTN. O bullet pode ter cupom e ainda assim pagar o principal de uma vez."

| Tipo | Quando paga | Exemplo |
| --- | --- | --- |
| **Com cupom** | Juros em datas fixas e principal no fim | Debêntures com cupom, Tesouro IPCA+ com juros semestrais |
| **Bullet** | Principal de uma vez no vencimento | Pode ter ou não cupom no meio |
| **Zero cupom** | Só um pagamento, no vencimento | LTN |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Um título sem cupom é o mesmo que um bullet" | Errado | Bullet pode ter cupom; zero cupom não tem |
| "Debêntures com cupom pagam juros periodicamente e devolvem o principal no vencimento" | Certo | Slides A3473 p. 7 |

**🔗 Ponte:** "Para comparar um pagamento de hoje com outro de daqui a dois anos, precisamos de uma moeda comum: a data de hoje."

---

### Bloco 3 — Trazer a data: o valor presente — 5 min

- "Valor presente (VP) é quanto vale hoje um pagamento futuro, descontado a uma taxa. Valor futuro (VF) é o inverso: quanto vale daqui a n períodos um valor de hoje."
- "Pense em câmbio: 100 reais de amanhã não valem o mesmo que 100 de hoje. Para comparar, converte-se pela taxa."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1500` `CHS` `PMT` `2` `i` `12` `n` `PV` | 🖥️ 15.863,01 | VP dos 12 cheques a 2% a.m. |

- ➕ "O `CHS` antes do PMT indica que o cheque é um valor a receber, e o VP sai positivo. Sem o sinal, a máquina dá o valor com o sinal oposto."
- 🔇 Antes de usar `PV` no modo de série, confirme que o modo é **postecipado** (padrão: pagamentos no fim do período).

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O VP de uma série de pagamentos futuros é menor que a soma nominal" | Certo | Desconto pela taxa |
| "O VF de um valor de hoje cresce quando a taxa aumenta" | Certo | Juros compostos |

> **Valor presente é o futuro trazido para hoje, pelo câmbio da taxa.**

**🔗 Ponte:** "Com o valor presente, a loja pode decidir."

---

### Bloco 4 — VPL e a decisão da loja — 5 min

- "O **VPL** é o valor presente dos recebimentos menos o valor investido. Se for positivo, a operação gera valor."

| Resultado do VPL | Leitura |
| --- | --- |
| VPL > 0 | Gera valor: vale fazer |
| VPL = 0 | Indiferente |
| VPL < 0 | Não gera valor: procure outra alternativa |

- "A loja pode pagar R$ 15.000 à vista pelos móveis e receber 12 cheques de R$ 1.500. Quem está do outro lado, o fornecedor, recebe um VPL de R$ 863: vale mais o parcelado."
- "A loja, ao contrário, desembolsa 15.000 hoje para receber, em valor presente, 15.863. O VPL para ela é **+R$ 863**. Ela ganha ao esperar."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1500` `CHS` `PMT` `2` `i` `12` `n` `PV` | 🖥️ 15.863,01 | Valor presente dos cheques |
| 2 | ⌨️ `15000` `−` | 🖥️ 863,01 | VPL para a loja |

- 🔇 A segunda linha usa o valor da pilha (15.863,01) menos 15.000. Essa é a leitura de quem recebe os cheques.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Com VPL positivo, o investimento deve ser feito" | Certo | Slides A3474 p. 7 |
| "Um VPL igual a zero torna a operação mais atraente que as demais" | Errado | É indiferente |

> **VPL positivo: gera valor. Negativo: procure outra alternativa.**

**🔗 Ponte:** "E de onde vem a taxa que faz essa conta funcionar?"

---

### Bloco 5 — A taxa de desconto: a régua — 2 min

- "A taxa de desconto é a **régua** que mede o valor de hoje. Três tipos: a taxa livre de risco, o custo de oportunidade e a taxa mínima de atratividade."
- ➕ "Se a loja pudesse aplicar a 2% ao mês sem risco, esse é o custo de oportunidade. Se a régua subir para 3%, a conta muda e o VPL pode ficar negativo."

> **A taxa de desconto é a régua: troque a régua e a decisão pode trocar de sinal.**

- 🔇 Fechamento: "Fluxo de pagamentos é o roteiro e fluxo de caixa é o filme; cupom e bullet dão o ritmo do pagamento; o VP traz tudo para hoje; e o VPL diz se a operação vale."

---

## Nota de verificação

- PD 1.3.3 a 1.3.3.2.3 lido no texto do repositório. Apostila p. 126–130 e slides A3473 e A3474 lidos nesta sessão.
- Cálculos conferidos em Python: VP de 12 × 1.500 a 2% = 15.863,01; VPL = 863,01; cupom de 3% por semestre a 5% a.s.: VP = 8.984,86.
- Convenção: taxa de desconto de 2% a.m., e a taxa de 3% citada só como contraste.
- Sem norma: VP, VF, VPL e taxa de desconto são matemática financeira clássica.
