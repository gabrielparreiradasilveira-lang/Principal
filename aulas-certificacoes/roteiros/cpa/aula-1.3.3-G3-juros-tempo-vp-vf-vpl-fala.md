# Roteiro de fala — Aula CPA: Juros × Tempo, Fluxo de Pagamentos, Fluxo de Caixa, VP, VF e VPL

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **1.3.3**, **1.3.3.1**, **1.3.3.2**, **1.3.3.2.1**, **1.3.3.2.2** e **1.3.3.2.3**; APOSTILA-CPA p. 126–131; slides A3473 (fluxos; cupom e bullet) e A3474 (VP, VF, VPL e taxa de desconto); aula do repositório `aula-1.3-C-fluxos-mutuo-vp-vf-vpl`.

CPA 1.3.3 · 1.3.3.1 · 1.3.3.2 · 1.3.3.2.1 · 1.3.3.2.2 · 1.3.3.2.3 · Módulo 1 · **20 min** · Aula G3 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Câmbio entre datas.** Um real que chega daqui a um ano não é o mesmo real de hoje. Para comparar, convertemos as datas para a mesma data, usando uma taxa como câmbio. Essa conversão é o valor presente.

**Onde a metáfora falha:** câmbio entre moedas tem uma taxa de mercado. Já a taxa de desconto é uma exigência de quem avalia: ela depende do risco e do custo de oportunidade, e pode ser diferente para duas pessoas diante do mesmo fluxo.

### 🔇 Caso

Uma **loja de móveis** recebe 12 cheques de R$ 1.500, um a cada 30 dias, e precisa decidir se vale mais receber assim ou pagar R$ 15.000 à vista. Taxa de desconto de 2% a.m.

### 🔇 Checagem de escopo

| Subitem | Fonte | Tratamento |
| --- | --- | --- |
| 1.3.3 Juros × tempo de alocação | Apostila p. 126–128 | Conferido |
| 1.3.3.1 Amortização e juros de crédito privado | Slides A3473 p. 6–7 | Conferido; **cupom e bullet** |
| 1.3.3.2 Capitalização em empréstimo e mútuo | Apostila p. 128; aula 1.3-C (CC arts. 586 a 591) | Conferido |
| 1.3.3.2.1 Fluxo de pagamentos | Slides A3473 p. 3 | Conferido |
| 1.3.3.2.2 Fluxo de caixa: cupom e amortização | Slides A3473 p. 3–7 | Conferido |
| 1.3.3.2.3 VP, VF e VPL | Slides A3474 p. 3, 7 | Conferido |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Slides A3473 p. 6 | "Títulos sem cupom (**bullet**)" | Bullet é o principal pago de uma vez no vencimento, podendo haver cupom no meio. Título **sem cupom** é o **zero cupom** (ex.: LTN) |
| 2 | Apostila p. 126 | Fluxo de pagamentos é o "registro das saídas" | Fluxo de pagamentos é o **cronograma contratual**, com entradas ou saídas. Fluxo de caixa é o que efetivamente entrou e saiu |
| 3 | Slides A3474 p. 6 | "Taxa livre de risco: Selic Meta (15%)" | Número datado, retirado. Ensina-se o conceito |
| 4 | Slides A3474 p. 9 | Exemplo com nome próprio de corretor | Trocado por "um corretor" |
| 5 | Apostila p. 130 | VPL de um imóvel = −R$ 3.360 | Com taxa de 15% a.a. convertida para o mês, dá ≈ −R$ 3.531,77 (conferido na aula 1.3-C). Não usado aqui |

### 🔇 Dados

| Item | Valor |
| --- | --- |
| Cheques | 12 parcelas de R$ 1.500, a cada 30 dias |
| Total nominal | R$ 18.000 |
| VP dos 12 cheques a 2% a.m. | **R$ 15.863,01** |
| VPL para a loja de pagar à vista R$ 15.000 | **R$ 863,01** |
| Título com cupom (exemplo trocado) | Nominal R$ 10.000; cupom de 3% por semestre; 3 anos; principal no fim; desconto a 5% a.s. → VP de **R$ 8.984,86** (cupons de R$ 1.522,71 + principal de R$ 7.462,15) |

🔇 Se a taxa de desconto subisse para 3% a.m., o VP cairia e o VPL para quem pagasse à vista ficaria negativo. Confira a taxa antes de decidir.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso dos cheques e os dois fluxos | 4 min |
| 2. Cupom × bullet | 4 min |
| 3. Trazer a data: valor presente | 5 min |
| 4. VPL e a decisão da loja | 5 min |
| 5. A taxa que mede a exigência | 2 min |
| **Total** | **20 min** |

---

## 3. Explicação em cinco blocos

### Bloco 1 — Caso dos cheques e os dois fluxos — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue distinguir o que está combinado do que de fato aconteceu.

- "Uma loja de móveis recebe doze cheques de mil e quinhentos reais, um a cada trinta dias. No total, são dezoito mil reais."
- "Antes de decidir, duas palavras. **Fluxo de pagamentos** é o combinado: quanto e quando, no contrato. **Fluxo de caixa** é o que de fato aconteceu: o extrato bancário, com entradas e saídas."
- "Um cheque pode estar no combinado e não virar caixa, se não for compensado. Por isso a loja olha os dois."
- **Erro comum:** comparar dezoito mil recebidos em um ano com quinze mil pagos hoje, e concluir que o parcelado é melhor. Dezoito mil daqui a um ano não são dezoito mil hoje.

**🔗 Ponte:** "Para comparar valores de datas diferentes, é preciso trazê-los para a mesma data."

---

### Bloco 2 — Cupom × bullet — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue dizer quando um título paga juros no meio do caminho e quando paga tudo no fim.

- "Um título **com cupom** paga juros em datas fixas, por exemplo a cada semestre. No vencimento, devolve o principal."
- "Um título **bullet** é aquele em que o principal volta de uma vez, no vencimento. Pode pagar cupom no meio, ou não."
- "Quando não tem cupom nenhum, ele é um **zero cupom**: uma única entrada, no fim. A LTN é um exemplo."
- **Erro comum:** achar que bullet e sem cupom são a mesma coisa. Um bullet pode pagar juros no meio, e o zero cupom nunca paga.

| Tipo | Quando paga | Exemplo |
| --- | --- | --- |
| **Com cupom** | Juros em datas fixas e principal no fim | Debêntures com cupom; Tesouro IPCA+ com juros semestrais |
| **Bullet** | Principal de uma vez no vencimento | Pode ter ou não cupom no meio |
| **Zero cupom** | Uma única entrada, no vencimento | LTN |

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Um título sem cupom é o mesmo que um bullet" | Errado | Bullet pode ter cupom; zero cupom não tem |
| "Debêntures com cupom pagam juros periodicamente e devolvem o principal no vencimento" | Certo | Slides A3473 p. 7 |

**🔗 Ponte:** "Agora a conversão: como trazer um cheque de daqui a trinta dias para hoje."

---

### Bloco 3 — Trazer a data: valor presente — 5 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o valor presente de uma série de pagamentos futuros.

- "Pense em câmbio. Cem reais de amanhã não valem o mesmo que cem reais de hoje. Para comparar, convertemos com uma taxa."
- "O **valor presente**, VP, é quanto vale hoje um pagamento futuro. O **valor futuro**, VF, é o inverso: quanto vale daqui a um tempo um valor de hoje."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1500` `CHS` `PMT` `2` `i` `12` `n` `PV` | 🖥️ 15.863,01 | VP dos 12 cheques a 2% a.m. |

- "O cheque de mil e quinhentos, daqui a trinta dias, vale hoje mil quatrocentos e setenta reais e cinquenta e nove centavos. Somando os doze, o total de hoje é quinze mil oitocentos e sessenta e três."
- 🔇 O `CHS` antes do `PMT` indica que o cheque é um valor a receber, e o VP sai positivo. Confirme que a máquina está no modo de pagamento no fim do período.
- **Erro comum:** achar que o cheque de daqui a trinta dias vale mil e quinhentos hoje. Ele vale menos, porque o dinheiro hoje pode render.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O VP de uma série de pagamentos futuros é menor que a soma nominal" | Certo | Desconto pela taxa |
| "O VF de um valor de hoje cresce quando a taxa aumenta" | Certo | Juros compostos |

**🔗 Ponte:** "Com o VP em mãos, a loja pode comparar o parcelado com o à vista."

---

### Bloco 4 — VPL e a decisão da loja — 5 min

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o VPL e dizer se uma operação gera ou destrói valor.

- "O **VPL**, valor presente líquido, é o valor presente dos recebimentos menos o valor investido. Se for positivo, a operação gera valor. Se for negativo, destrói."

| Resultado do VPL | Leitura |
| --- | --- |
| VPL > 0 | Gera valor: vale fazer |
| VPL = 0 | Indiferente |
| VPL < 0 | Não gera valor: procure outra alternativa |

- "Para a loja, que recebe os cheques, o VPL de pagar quinze mil à vista é de quase oitocentos e sessenta e três reais. Ela ganha ao esperar."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `1500` `CHS` `PMT` `2` `i` `12` `n` `PV` | 🖥️ 15.863,01 | VP dos cheques |
| 2 | ⌨️ `15000` `−` | 🖥️ 863,01 | VPL para a loja |

- 🔇 No passo 2, a máquina subtrai o valor à vista do VP. O resultado positivo é o ganho de quem recebe parcelado.
- **Erro comum:** achar que VPL igual a zero é o melhor resultado. Zero quer dizer indiferente.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Com VPL positivo, o investimento deve ser feito" | Certo | Slides A3474 p. 7 |
| "Um VPL igual a zero torna a operação mais atraente que as demais" | Errado | É indiferente |

> **VPL positivo: gera valor. Negativo: procure outra alternativa.**

**🔗 Ponte:** "E de onde vem a taxa que faz essa conta funcionar?"

---

### Bloco 5 — A taxa que mede a exigência — 2 min

> **Objetivo deste bloco:** ao fim, o aluno consegue explicar o que é a taxa de desconto e por que trocá-la muda a decisão.

- "A taxa de desconto é a taxa que a loja exige para trazer os valores futuros para hoje. Ela depende do que a loja poderia ganhar em outro lugar, com risco parecido."
- "Se a loja pudesse aplicar a dois por cento ao mês, sem risco maior, essa é a taxa de desconto. Se a exigência subir para três por cento, o valor presente cai e o VPL pode virar negativo."
- **Erro comum:** achar que a taxa de desconto é um imposto ou um custo cobrado de alguém. É uma exigência de quem avalia.

> **Troque a taxa de desconto e a decisão pode trocar de sinal.**

- 🔇 **Fechamento:** "Fluxo de pagamentos é o combinado e fluxo de caixa é o que aconteceu. Cupom e bullet mostram o ritmo do pagamento. O VP traz tudo para hoje, e o VPL diz se a operação vale." Próxima aula: G4, taxa de desconto e taxa bruta × líquida.

---

## Lista de pegadinhas com nome

1. **Pegadinha da soma nominal** — "Doze cheques de 1.500 somam 18.000; é melhor que 15.000 à vista." Errado: é preciso trazer cada cheque a valor presente antes de comparar.
2. **Pegadinha da troca de nome** — "Título sem cupom é o bullet." Errado: título sem cupom é o zero cupom. O bullet pode ter cupom.
3. **Pegadinha do zero** — "VPL igual a zero é a melhor operação." Errado: é indiferente.
4. **Pegadinha da taxa cobrada** — "A taxa de desconto é um custo cobrado do cliente." Errado: é uma exigência de quem avalia.

---

## Nota de verificação

- PD 1.3.3 a 1.3.3.2.3 lido no texto do repositório. Apostila p. 126–130 e slides A3473 e A3474 lidos nesta sessão.
- Cálculos conferidos em Python: VP de 12 × 1.500 a 2% = 15.863,01; VPL = 863,01; cupom de 3% por semestre a 5% a.s.: VP = 8.984,86; VP de um cheque = 1.500 ÷ 1,02 = 1.470,59.
- Convenção: taxa de desconto de 2% a.m., e 3% citada só como contraste.
- Revisão de estrutura: metáfora única (câmbio entre datas), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala.
