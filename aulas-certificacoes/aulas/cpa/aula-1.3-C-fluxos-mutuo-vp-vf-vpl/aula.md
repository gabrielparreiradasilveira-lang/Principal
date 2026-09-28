# Aula CPA — Fluxos de Pagamento e de Caixa, Cupom × Amortização, Mútuo, VP, VF, VPL e Taxa de Desconto

Sep 28, 2026 · @Boss · Roteiro integrado · 40 min

## Identificação e alinhamento

Aula C de 5 do item **1.3 Operações do mercado financeiro** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), Módulo 1. Cobre **1.3.3** (juros × tempo de alocação), **1.3.3.1** (amortização e juros no crédito privado), **1.3.3.2 a 1.3.3.2.3** (capitalização em empréstimos e mútuo; fluxo de pagamentos; fluxo de caixa; VP, VF e VPL), **1.3.3.3** (taxa de desconto), **1.3.3.5.3** (custo de oportunidade) e **1.3.3.5.4** (taxa livre de risco). Base: PDFs **A3473 e A3474**, **APOSTILA-CPA p. 126–129 e 133–135** e o **Código Civil**.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 1.3.3 Juros × tempo de alocação | PDF A3476 (só título) · APOSTILA-CPA p. 134–135 | **Completado pela apostila** |
| 1.3.3.1 Amortização e juros no crédito privado | PDF A3473 p. 5–7 | Conferido, **com correção** (bullet × zero cupom) |
| 1.3.3.2 Capitalização em empréstimos e mútuo | PDF A3474 p. 5 · **Código Civil arts. 586–591** | **Mútuo completado pela lei** |
| 1.3.3.2.1 Fluxo de pagamentos | PDF A3473 p. 3 · APOSTILA-CPA p. 126–127 | Conferido; definição da apostila **corrigida** |
| 1.3.3.2.2 Fluxo de caixa: cupom, amortizações e valores | PDF A3473 p. 3–7 | Conferido |
| 1.3.3.2.3 VP, VF e VPL | PDF A3474 p. 3–9 · APOSTILA-CPA p. 128–129 | Conferido; exercícios **resolvidos** |
| 1.3.3.3 Taxa de desconto | PDF A3474 p. 6 · APOSTILA-CPA p. 128 | Conferido; número datado **retirado** |
| 1.3.3.5.3 Custo de oportunidade | PDF A3474 p. 6 · APOSTILA-CPA p. 133 | Completado pela apostila |
| 1.3.3.5.4 Taxa livre de risco | PDF A3474 p. 6 · APOSTILA-CPA p. 128 | Completado pela apostila |

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 3 min |
| 2. Metáfora central | 3 min |
| 3. Tópicos (Juros × tempo 2 · Fluxo de pagamentos × fluxo de caixa 3 · Mútuo 3 · Cupom e amortização 4 · VP e VF 3 · Taxa de desconto, custo de oportunidade e taxa livre de risco 3 · VPL 4) | 22 min |
| 4. Por que cai na prova | 4 min |
| 5. Case | 3 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **40 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | PDF A3473 p. 6 | "Títulos sem cupom **(bullet)**" | **Bullet** = principal pago **de uma vez no vencimento**; pode ter cupom no meio. Título **sem cupom** é o **zero cupom** (ex.: LTN). O slide 7 do próprio PDF usa "bullet" no sentido certo | — |
| 2 | APOSTILA-CPA p. 126 | Fluxo de pagamentos = "registro das **saídas**" | Fluxo de pagamentos = **cronograma contratual** de pagamentos futuros (entradas ou saídas). Fluxo de caixa = o que **efetivamente** entrou e saiu (PDF A3473 p. 3) | — |
| 3 | APOSTILA-CPA p. 130 | VPL do imóvel = −R$ 3.360 | Com Selic de 15% a.a. convertida para mês (1,1715% a.m.), o VPL é **≈ −R$ 3.531,77**. A TIR de **1,14% a.m.** confere | — |
| 4 | PDF A3474 p. 6 | Taxa livre de risco = "Selic Meta (15%)" | Número datado → **retirado**; ensinado o conceito (título público federal pós-fixado / Selic) | — |
| 5 | PDF A3474 p. 9 | Nome próprio inventado no exemplo | Trocado por "um corretor" (genérico) | — |
| 6 | — | Material não trata de mútuo | Mútuo = empréstimo de **coisa fungível** (CC art. 586); transfere a propriedade (art. 587); com fim econômico, **presumem-se juros** (art. 591, redação da Lei 14.905/2024) | Código Civil |

## 1. Fala de abertura — 3 min

> Um corretor oferece um imóvel na planta: entrada de 20%, 36 parcelas, e a promessa de valorizar 30% na entrega.
>
> Parece ótimo. Mas quando a gente traz **cada parcela para o dia de hoje** e compara com deixar o dinheiro rendendo a Selic, o negócio **perde dinheiro**.
>
> A ferramenta que mostra isso é o **VPL**. Hoje: fluxos, cupons, amortizações, mútuo e como **trazer o futuro para o presente**.

### Objetivo da abertura

Mostrar que um investimento "lucrativo" pode destruir valor quando o tempo do dinheiro entra na conta.

### Conexão com o Programa Detalhado

CPA 1.3.3 a 1.3.3.3, 1.3.3.5.3 e 1.3.3.5.4.

## 2. Metáfora central — 3 min

### Metáfora: a máquina do tempo do dinheiro

> Dinheiro no futuro vale **menos** que dinheiro hoje, porque hoje ele já poderia estar rendendo.
>
> O **VF** é a máquina do tempo **indo para frente**: quanto o dinheiro de hoje vira amanhã.
>
> O **VP** é a máquina **voltando**: quanto vale hoje o dinheiro de amanhã.
>
> A **taxa de desconto** é o **combustível** da máquina: quanto maior a taxa, mais o futuro "encolhe" na volta.
>
> O **VPL** coloca **todos os fluxos na mesma data**, hoje, e soma. Se sobrar valor, o investimento vale a pena.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Ida para o futuro | Valor Futuro (FV) |
| Volta para hoje | Valor Presente (PV) |
| Combustível | Taxa de desconto (TMA / custo de oportunidade) |
| Tudo na mesma data | Valor Presente Líquido (VPL) |

### Frase de fixação

> **Só se compara dinheiro na mesma data.**

## 3. Explicação dos tópicos — 22 min

### 3.1 Juros × tempo de alocação — 2 min

#### Como funciona

| Efeito do prazo | Explicação |
| --- | --- |
| **Juros compostos** | Quanto mais longo o prazo, mais os juros sobre juros pesam (R$ 1.000 a 10% a.a. por 10 anos ≈ R$ 2.594) |
| **Incerteza** | Prazos longos ficam mais expostos a crises, inflação e juros |
| **Sensibilidade a juros** | Títulos longos oscilam mais de preço (duration, Aula D) |

#### Frase de fixação

> **O tempo multiplica o ganho e também o risco.**

#### Alinhamento ao PD

CPA 1.3.3.

---

### 3.2 Fluxo de pagamentos × fluxo de caixa — 3 min

#### Como funciona

| Conceito | O que é | Natureza |
| --- | --- | --- |
| **Fluxo de pagamentos** | **Cronograma contratual**: quando e quanto será pago ou recebido | O **combinado** |
| **Fluxo de caixa** | Registro das **entradas e saídas efetivas** ao longo do tempo | O **realizado**, e a ferramenta de análise |

**Exemplo (PDF A3473 p. 4):** empréstimo de R$ 1.000, a pagar em 12 parcelas de R$ 100.

| Data | Fluxo (visão de quem emprestou) |
| --- | --- |
| 0 | −1.000 |
| 1 a 12 | +100 por mês |

**Convenção de sinais:** saída = **negativo**; entrada = **positivo** (na HP12C, `CHS`).

#### Frase de fixação

> **Pagamentos é o combinado; caixa é o acontecido.**

#### Alinhamento ao PD

CPA 1.3.3.2.1 e 1.3.3.2.2.

---

### 3.3 Regime de capitalização em empréstimos e mútuo — 3 min

#### O que é

**Mútuo** é o **empréstimo de coisas fungíveis** (que se substituem por outras do mesmo gênero, qualidade e quantidade, como o **dinheiro**). O mutuário devolve **coisa equivalente**, não a mesma (Código Civil, art. 586).

#### Como funciona

| Regra | Artigo do Código Civil |
| --- | --- |
| Mútuo = empréstimo de coisas fungíveis; devolve-se coisa do mesmo gênero, qualidade e quantidade | Art. 586 |
| **Transfere a propriedade** ao mutuário, que assume os riscos | Art. 587 |
| Com **fim econômico**, **presumem-se devidos juros**; sem taxa pactuada, aplica-se a **taxa legal** (art. 406) | Art. 591 (redação da Lei 14.905/2024) |
| Taxa legal = **Selic deduzido o índice de atualização monetária** (IPCA) | Art. 406, § 1º |

**Regime de capitalização:** empréstimos e financiamentos bancários usam **juros compostos**. A parcela combina **juros + amortização** (Aula E).

#### O que a prova pode confundir

- **Mútuo ≠ comodato:** no comodato (bem infungível, ex.: um carro) devolve-se **a mesma coisa**.
- Emprestar dinheiro é mútuo.

#### Frase de fixação

> **Mútuo é emprestar o que se devolve "igual, mas não o mesmo": dinheiro.**

#### Alinhamento ao PD

CPA 1.3.3.2.

---

### 3.4 Cupom e amortização no crédito privado — 4 min

#### Como funciona

| Estrutura | Juros (cupom) | Principal | Exemplos |
| --- | --- | --- | --- |
| **Zero cupom** | Tudo no vencimento | No vencimento | Tesouro Prefixado sem juros semestrais (LTN), CDB sem liquidez intermediária |
| **Bullet com cupom** | Periódicos (ex.: semestrais) | **De uma vez** no vencimento | Debêntures, títulos públicos com juros semestrais |
| **Amortizante** | Periódicos | **Em parcelas** ao longo do prazo | Debêntures e CRI/CRA com amortização programada |

**Cupom** = pagamento periódico de **juros**. **Amortização** = devolução de parte do **principal**.

| Efeito | Zero cupom | Com cupom / amortizante |
| --- | --- | --- |
| Recebe dinheiro antes? | Não | Sim |
| Prazo médio e duration | Iguais ao vencimento | **Menores** que o vencimento |
| Reinvestimento | Não há | Os cupons precisam ser reinvestidos |

#### O que a prova pode confundir

- **Bullet fala do principal; cupom fala dos juros.**

#### Frase de fixação

> **Cupom devolve juros; amortização devolve o principal; zero cupom devolve tudo no fim.**

#### Alinhamento ao PD

CPA 1.3.3.1 e 1.3.3.2.2.

---

### 3.5 Valor Presente e Valor Futuro — 3 min

#### Como funciona

> **VF = VP × (1 + i)^n** · **VP = VF ÷ (1 + i)^n**

| Tecla da HP12C | Significado |
| --- | --- |
| **n** | Número de períodos |
| **i** | Taxa por período |
| **PV** | Valor presente |
| **PMT** | Parcela periódica |
| **FV** | Valor futuro |
| **CF0 · CFj · Nj** | Fluxo inicial · fluxos seguintes · repetições |
| **NPV · IRR** | VPL · TIR |

**Exemplo:** quanto vale hoje R$ 10.000 a receber em 2 anos, com taxa de 10% a.a.? 10.000 ÷ 1,1² = **R$ 8.264,46**.

#### Frase de fixação

> **VF leva para frente multiplicando; VP traz para trás dividindo.**

#### Alinhamento ao PD

CPA 1.3.3.2.3.

---

### 3.6 Taxa de desconto, custo de oportunidade e taxa livre de risco — 3 min

#### Como funciona

| Conceito | Definição | Referência típica |
| --- | --- | --- |
| **Taxa de desconto** | Taxa usada para trazer fluxos futuros a valor presente | A TMA do investidor |
| **Taxa Mínima de Atratividade (TMA)** | Retorno mínimo exigido para aceitar um investimento | Definida pelo investidor |
| **Custo de oportunidade** | Retorno da **melhor alternativa que se abandona** ao escolher um investimento | Ex.: CDB de banco grande, % do CDI |
| **Taxa livre de risco** | Retorno de um ativo com risco de crédito mínimo | No Brasil: **título público federal pós-fixado / Selic** |

**Lógica (apostila p. 128):** se um projeto rende **menos** que a taxa livre de risco, não compensa correr o risco.

#### O que a prova pode confundir

- **Custo de oportunidade não é despesa paga**: é o que se **deixa de ganhar**.

#### Frase de fixação

> **Toda escolha tem um preço: o que você deixou de ganhar na alternativa.**

#### Alinhamento ao PD

CPA 1.3.3.3, 1.3.3.5.3 e 1.3.3.5.4.

---

### 3.7 Valor Presente Líquido (VPL) — 4 min

#### O que é

**VPL** = soma dos fluxos futuros trazidos a valor presente pela taxa de desconto **menos** o investimento inicial.

#### Como funciona

| Resultado | Decisão |
| --- | --- |
| **VPL > 0** | Gera valor → **investir** |
| **VPL = 0** | Indiferente (rende exatamente a taxa de desconto) |
| **VPL < 0** | Destrói valor → procurar outra alternativa |

**Exercício 1 (PDF A3474 p. 5):** emprestei R$ 1.000 e vou receber 12 × R$ 100.

| Taxa de desconto | VPL | Leitura |
| --- | --- | --- |
| 2% a.m. | **+R$ 57,53** | Vale mais que a alternativa de 2% a.m. |
| TIR da operação | **≈ 2,92% a.m.** | Taxa que zera o VPL (Aula D) |

**HP12C:** `f CLX` · `1000 CHS g CF0` · `100 g CFj` · `12 g Nj` · `2 i` · `f NPV` → **57,53**.

**Exercício 2 (PDF A3474 p. 9):** imóvel de R$ 500.000; entrada de 20% (R$ 100.000); 36 × R$ 11.150; recompra por R$ 650.000 no mês 37; alternativa = Selic de 15% a.a.

| Passo | Conta | Resultado |
| --- | --- | --- |
| 1. Taxa mensal equivalente | 1,15^(1/12) − 1 | 1,1715% a.m. |
| 2. Fluxo | CF0 = −100.000 · CFj = −11.150 (36×) · CFj = +650.000 | — |
| 3. VPL | `f NPV` | **≈ −R$ 3.531,77** |
| 4. TIR | `f IRR` | **≈ 1,14% a.m.** < 1,1715% |

**Decisão:** VPL negativo → o imóvel rende **menos** que a Selic. **Não compensa.**

#### O que a prova pode confundir

- **Lucro nominal ≠ VPL positivo**: o imóvel "ganha" R$ 148.600 em reais, mas perde para a alternativa.

#### Frase de fixação

> **VPL positivo cria valor; negativo destrói.**

#### Alinhamento ao PD

CPA 1.3.3.2.3.

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

A CPA cobra a **regra de decisão do VPL**, a leitura de **fluxos** (zero cupom, bullet, amortizante) e os conceitos de **custo de oportunidade** e **taxa livre de risco**.

### Pontos de atenção

1. **VP = VF ÷ (1 + i)^n.**
2. **VPL > 0 → investe.**
3. **Bullet = principal no fim; zero cupom = nada no meio.**
4. **Mútuo = empréstimo de coisa fungível (dinheiro).**
5. **Custo de oportunidade = o que se deixa de ganhar.**

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Fluxo de pagamentos | Fluxo de caixa | Contratado × realizado |
| Zero cupom | Com cupom | Tudo no fim × juros no meio |
| Mútuo | Comodato | Fungível (devolve equivalente) × infungível (devolve o mesmo) |
| VP | VF | Hoje × futuro |

### Palavras-chave da prova

- **"Trazer a valor presente"**: VP / desconto.
- **"Taxa mínima de atratividade"**: taxa de desconto.
- **"Alternativa abandonada"**: custo de oportunidade.

### Pegadinhas

- "VPL igual a zero significa prejuízo." **Errado:** rende exatamente a taxa de desconto.
- "Todo título bullet é zero cupom." **Errado.**

### Frase de fixação

> **Coloque tudo na data de hoje e compare com a melhor alternativa.**

## 5. Case — 3 min

### Situação

> Um investidor pode aplicar R$ 100.000 em um projeto que devolve R$ 60.000 em 1 ano e R$ 60.000 em 2 anos. A alternativa sem risco rende 10% a.a.

### Conceitos aplicados

| Passo | Conta | Resultado |
| --- | --- | --- |
| VP do ano 1 | 60.000 ÷ 1,10 | R$ 54.545,45 |
| VP do ano 2 | 60.000 ÷ 1,10² | R$ 49.586,78 |
| VPL | 54.545,45 + 49.586,78 − 100.000 | **+R$ 4.132,23** |

### Síntese do case

O projeto rende mais que a alternativa sem risco: **VPL positivo**, vale investir (se o risco for aceitável).

### Frase de fixação

> **VPL responde: sobra valor depois de pagar o custo de oportunidade?**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 1.3.3.2.3 VPL · **Nível:** Médio

### Questão

Um projeto exige investimento inicial de R$ 50.000 e gera um único fluxo de R$ 60.500 ao final de dois anos. Considerando taxa mínima de atratividade de 10% ao ano, é correto afirmar que o projeto:

A) tem VPL positivo de R$ 10.500 e deve ser aceito.

B) tem VPL igual a zero, pois rende exatamente a taxa mínima de atratividade.

C) tem VPL negativo, pois o fluxo futuro é menor que o investimento corrigido.

D) tem VPL positivo de R$ 5.000 e deve ser aceito.

### Ponto-chave do enunciado

Trazer R$ 60.500 de dois anos para hoje a 10% a.a.

### Gabarito

**Alternativa B.**

### Comentário da alternativa correta

60.500 ÷ 1,10² = 60.500 ÷ 1,21 = **R$ 50.000**. VPL = 50.000 − 50.000 = **0**: o projeto rende exatamente 10% a.a.

### Por que as demais estão incorretas?

- **A:** subtraiu valores em datas diferentes (60.500 − 50.000), sem descontar.
- **C:** o fluxo trazido a valor presente é **igual** ao investimento, não menor.
- **D:** descontou só **um** ano (60.500 ÷ 1,10 = 55.000 → 55.000 − 50.000 = 5.000); o fluxo está a **dois** anos.

### Armadilhas e macetes

- **Nunca subtraia valores de datas diferentes.**

### Referência

APOSTILA-CPA p. 128–129; PDF A3474 p. 7; Programa Detalhado CPA, item 1.3.3.2.3.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. Fluxo de pagamentos = combinado; fluxo de caixa = realizado; saída negativa, entrada positiva.
2. Mútuo (CC art. 586): empréstimo de coisa fungível; com fim econômico, juros presumidos (art. 591).
3. Zero cupom (tudo no fim) × bullet com cupom (juros no meio, principal no fim) × amortizante (principal em parcelas).
4. VP = VF ÷ (1 + i)^n; a taxa de desconto é a TMA, ligada ao custo de oportunidade e à taxa livre de risco.
5. VPL > 0 investe; = 0 indiferente; < 0 rejeita.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| VF / VP | VF = VP(1 + i)^n · VP = VF ÷ (1 + i)^n |
| VPL | Σ VP dos fluxos − investimento |
| Decisão | VPL > 0 investe · = 0 indiferente · < 0 rejeita |
| Zero cupom | Nada no meio, tudo no fim |
| Bullet | Principal de uma vez no fim |
| Mútuo | Empréstimo de coisa fungível (CC 586) |
| Custo de oportunidade | O que se deixa de ganhar |
| Taxa livre de risco | Título público federal / Selic |

### Cadeia lógica

> Desenhar o fluxo → escolher a taxa de desconto (custo de oportunidade) → trazer tudo a valor presente → VPL decide

### Diferenças que não podem ser confundidas

- **Bullet ≠ zero cupom.**
- **Mútuo ≠ comodato.**
- **Lucro nominal ≠ VPL positivo.**

### Frase central da aula

> **Dinheiro só se compara na mesma data: o VPL é a máquina do tempo do investidor.**

### Próximo passo de estudo

Aula 1.3-D — TIR, prazo médio, CMPC, duration, alavancagem, retornos e payback.

## Referências oficiais e status

Último acesso: 2026-09-28.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — itens 1.3.3 a 1.3.3.3, 1.3.3.5.3 e 1.3.3.5.4 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. Presidência da República — Lei 10.406/2002 (Código Civil) — arts. 586, 587, 591 e 406 (redação da Lei 14.905/2024) — [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm). **Em vigor, alterado.** Conferido nesta sessão.
3. Cálculos de VP, VF e VPL: matemática financeira clássica.

Fontes de origem (não oficiais): PDFs A3473 "Fluxo de Caixa e Fluxo de Pagamentos" e A3474 "Análise de Investimento" (`00-fontes/materiais-aula/topico-1.3-operacoes-mercado-financeiro/`); APOSTILA-CPA p. 126–129, 133–135.
