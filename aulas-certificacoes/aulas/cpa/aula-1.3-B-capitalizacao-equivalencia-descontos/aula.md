# Aula CPA — Capitalização Simples × Composta, Proporcionalidade, Equivalência e Descontos

Sep 28, 2026 · @Boss · Roteiro integrado · 40 min

## Identificação e alinhamento

Aula B de 5 do item **1.3 Operações do mercado financeiro** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), Módulo 1. Cobre **1.3.2** (capitalização simples × composta: conceito, desconto, equivalência e proporcionalidade), **1.3.4.3** (juros simples e compostos), **1.3.5** (taxa de desconto comercial) e **1.3.8 / 1.3.8.1** (desconto bancário na antecipação de recebíveis e direitos creditórios). Base: PDFs **A3472 e A3477**, **APOSTILA-CPA p. 138–139** e conceitos clássicos.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 1.3.2 / 1.3.4.3 Simples × composta: conceito | PDF A3472 p. 4–5 · APOSTILA-CPA p. 134 | Conferido; exercícios **resolvidos** |
| 1.3.2 Proporcionalidade e equivalência | PDF A3472 p. 4–5 | Conferido |
| 1.3.2 Desconto (racional × comercial) | PDF A3472 p. 7–8 (só comercial) | **Completado:** desconto racional ("por dentro") |
| 1.3.5 Taxa de desconto comercial | PDF A3477 p. 3–5 · APOSTILA-CPA p. 138–139 | Conferido |
| 1.3.8 / 1.3.8.1 Desconto bancário, recebíveis e direitos creditórios | PDF A3477 p. 3–5 (só duplicata) | **Completado:** taxa administrativa, taxa efetiva e direitos creditórios |

**Cobertura PD × PDFs:** faltavam o **desconto racional** e o **desconto bancário completo**; completados por conceito clássico.

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 3 min |
| 2. Metáfora central | 3 min |
| 3. Tópicos (Simples × composta 5 · Proporcional × equivalente 5 · Desconto racional × comercial 5 · Desconto bancário e recebíveis 7) | 22 min |
| 4. Por que cai na prova | 4 min |
| 5. Case | 3 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **40 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | PDF A3472 p. 8 | "Desconto **composto** de 3% ao mês" (sem dizer qual) | Enunciado **ambíguo**: racional composto → R$ 4.575,71; comercial composto → R$ 4.563,37. A aula usa o **racional composto** (padrão de mercado para trazer a valor presente) e cita o outro | — |
| 2 | PDF A3472 p. 7–8 | Exercícios sem resposta | **Resolvidos**: simples R$ 6.000,00; composto R$ 6.094,97; desconto comercial simples R$ 4.550,00 | — |
| 3 | PDF A3477 p. 3 | Desconto comercial "pode superestimar o custo em prazos longos" | Mais preciso: como incide sobre o **valor futuro**, a **taxa efetiva** da operação é **maior** que a taxa de desconto anunciada, e a diferença cresce com o prazo | — |
| 4 | PDF A3477 p. 7 | Marca comercial citada no exemplo | Trocada por "máquina de café" (genérico) | — |

## 1. Fala de abertura — 3 min

> Você vende R$ 50.000 para um cliente que paga em 90 dias. Mas precisa do dinheiro **hoje**.
>
> O banco antecipa e cobra 3% ao mês. Quanto cai na sua conta? E quanto você **realmente** pagou de juros?
>
> A resposta depende de duas perguntas: **simples ou composto?** E o desconto é **"por fora" ou "por dentro"?**

### Objetivo da abertura

Ligar capitalização e desconto a uma situação real de empresa: antecipar recebíveis.

### Conexão com o Programa Detalhado

CPA 1.3.2, 1.3.4.3, 1.3.5 e 1.3.8.

## 2. Metáfora central — 3 min

### Metáfora: a bola de neve e a escada

> **Juros simples** são uma **escada**: cada degrau tem a mesma altura, porque os juros incidem sempre sobre o **capital inicial**.
>
> **Juros compostos** são uma **bola de neve**: ela rola e cresce sobre o tamanho que **já tem**. Juros sobre juros.
>
> **Descontar** é fazer o caminho de volta: trazer o valor do futuro para hoje. No desconto **"por fora"** (comercial), o banco mede o degrau pelo tamanho **lá de cima** (valor futuro). No **"por dentro"** (racional), mede pelo tamanho **aqui embaixo** (valor presente).

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Escada de degraus iguais | Juros simples (J = C × i × n) |
| Bola de neve | Juros compostos (M = C × (1 + i)^n) |
| Medir pelo alto | Desconto comercial ("por fora", sobre o valor nominal) |
| Medir por baixo | Desconto racional ("por dentro", sobre o valor atual) |

### Frase de fixação

> **Simples é escada, composto é bola de neve; comercial desconta por fora, racional por dentro.**

## 3. Explicação dos tópicos — 22 min

### 3.1 Capitalização simples × composta — 5 min

#### Como funciona

| Regime | Juros incidem sobre | Fórmula | Uso típico |
| --- | --- | --- | --- |
| **Simples** | Só o capital inicial | **J = C × i × n** · **M = C × (1 + i × n)** | Desconto comercial, cálculos de curto prazo |
| **Composto** | Capital + juros acumulados | **M = C × (1 + i)^n** · **C = M ÷ (1 + i)^n** | Aplicações financeiras, empréstimos |

**Exercício (PDF A3472):** R$ 5.000 a 2% a.m. por 10 meses.

| Regime | Conta | Montante |
| --- | --- | --- |
| Simples | 5.000 × (1 + 0,02 × 10) | **R$ 6.000,00** |
| Composto | 5.000 × 1,02¹⁰ | **R$ 6.094,97** |

**HP12C (composto):** `5000 CHS PV` · `2 i` · `10 n` · `FV` → **6.094,97**.

**Tempo × juros (apostila p. 134):** quanto maior o prazo, maior a distância entre os dois regimes. R$ 1.000 a 10% a.a. por 10 anos: simples = R$ 2.000; composto ≈ **R$ 2.594**.

#### O que a prova pode confundir

- Para **um único período**, simples e composto dão o **mesmo** resultado.
- Com prazo **menor que um período**, o simples rende **mais**; acima de um período, o composto rende **mais**.

#### Frase de fixação

> **Quanto mais tempo, mais a bola de neve se afasta da escada.**

#### Alinhamento ao PD

CPA 1.3.2 e 1.3.4.3.

---

### 3.2 Taxa proporcional × taxa equivalente — 5 min

#### Como funciona

| Conceito | Regime | Regra | Exemplo |
| --- | --- | --- | --- |
| **Proporcional** | Simples | Multiplica ou divide pelo tempo | 2% a.m. ↔ **24% a.a.** |
| **Equivalente** | Composto | **i₂ = (1 + i₁)^(n₂/n₁) − 1** | 2% a.m. ↔ **26,82% a.a.**; 30% a.a. ↔ **14,0175% a.s.** |

**Taxas equivalentes** produzem o **mesmo montante** no mesmo prazo, com capitalizações diferentes.

**HP12C (30% a.a. → semestre):** `1.3 ENTER 0.5 yˣ 1 − 100 ×` → **14,0175**.

#### O que a prova pode confundir

- **Proporcional é do regime simples; equivalente é do composto.**
- 30% a.a. **não** é 15% a.s. em juros compostos.

#### Frase de fixação

> **Proporcional multiplica; equivalente eleva à potência.**

#### Alinhamento ao PD

CPA 1.3.2.

---

### 3.3 Desconto racional × desconto comercial — 5 min

#### O que é

**Desconto** é a diferença entre o **valor nominal** (N, valor no vencimento) e o **valor atual** (A, valor recebido hoje).

#### Como funciona

| Tipo | Base do cálculo | Fórmula (simples) | Exemplo: N = R$ 5.000; 3% a.m.; 3 meses |
| --- | --- | --- | --- |
| **Comercial ("por fora")** | Valor **nominal** | **D = N × i × n** · A = N × (1 − i × n) | D = 450 → **A = R$ 4.550,00** |
| **Racional ("por dentro")** | Valor **atual** | **A = N ÷ (1 + i × n)** | A = 5.000 ÷ 1,09 = **R$ 4.587,16** |
| **Racional composto** | Valor atual, composto | **A = N ÷ (1 + i)^n** | 5.000 ÷ 1,03³ = **R$ 4.575,71** |
| Comercial composto | Valor nominal, composto | A = N × (1 − i)^n | 5.000 × 0,97³ = R$ 4.563,37 |

**Leitura:** o desconto **comercial** é **maior** que o racional para a mesma taxa: é o preferido dos bancos na antecipação.

**Taxa efetiva do desconto comercial:** quem recebeu R$ 4.550 e devolverá R$ 5.000 em 3 meses pagou (5.000 ÷ 4.550)^(1/3) − 1 ≈ **3,19% a.m. compostos**, acima dos 3% anunciados.

#### O que a prova pode confundir

- **"Por fora" = comercial = sobre o valor de face.**
- **Desconto racional composto = trazer a valor presente** (é o PV da HP12C).

#### Frase de fixação

> **Por fora pesa mais: o banco calcula sobre o valor cheio.**

#### Alinhamento ao PD

CPA 1.3.2 e 1.3.5.

---

### 3.4 Desconto bancário na antecipação de recebíveis e direitos creditórios — 7 min

#### O que é

**Desconto bancário** é a **antecipação** de um valor a receber (duplicata, cheque pré-datado, recebível de cartão, outros **direitos creditórios**): o banco paga hoje e fica com o direito de receber no vencimento, cobrando um desconto.

#### Como funciona

**Desconto bancário simples** = desconto comercial simples + **taxa administrativa** (h), cobrada sobre o valor nominal:

> **D = N × (i × n + h)** · **Valor líquido = N − D**

**Exemplo (APOSTILA-CPA p. 138–139 / PDF A3477):** duplicata de R$ 50.000, 90 dias, 3% a.m.

| Versão | Conta | Desconto | Líquido |
| --- | --- | --- | --- |
| Só desconto comercial | 50.000 × 0,03 × 3 | R$ 4.500 | **R$ 45.500** |
| Com taxa administrativa de 1% (exemplo genérico) | 50.000 × (0,09 + 0,01) | R$ 5.000 | **R$ 45.000** |

Além do desconto e das tarifas, a operação pode ter **tributos** (ex.: IOF sobre operações de crédito), que também aumentam o custo efetivo.

| Conceito | Explicação |
| --- | --- |
| **Recebível** | Valor que a empresa tem a receber (venda a prazo) |
| **Direitos creditórios** | Termo amplo para créditos a receber; podem ser vendidos a bancos ou a **FIDCs** (fundos de direitos creditórios) |
| **Para que serve** | Capital de giro: transforma venda a prazo em caixa hoje |
| **Custo real** | Sempre calcule a **taxa efetiva**: desconto + tarifas + tributos sobre o valor líquido recebido |

#### O que a prova pode confundir

- A taxa anunciada **subestima** o custo: o custo efetivo é maior.
- Desconto bancário **simples** usa a lógica do desconto **comercial** (sobre o valor nominal).

#### Frase de fixação

> **Antecipar recebível é vender o futuro com desconto por fora; some as tarifas para saber o custo real.**

#### Alinhamento ao PD

CPA 1.3.8 e 1.3.8.1.

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

A CPA pede **montante** (simples e composto), **taxa equivalente**, **valor líquido de uma duplicata** e a diferença entre **comercial e racional**.

### Pontos de atenção

1. **Simples: M = C(1 + in). Composto: M = C(1 + i)^n.**
2. **Proporcional (simples) × equivalente (composto).**
3. **Comercial: D = N × i × n (por fora).**
4. **Racional: A = N ÷ (1 + in) (por dentro).**
5. **Desconto bancário = comercial + taxa administrativa.**

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Juros simples | Juros compostos | Sobre o capital × sobre o montante |
| Taxa proporcional | Taxa equivalente | Multiplica × potência |
| Desconto comercial | Desconto racional | Sobre o nominal × sobre o atual |

### Palavras-chave da prova

- **"Por fora"**: comercial.
- **"Por dentro"**: racional.
- **"Mesmo montante no mesmo prazo"**: taxas equivalentes.

### Pegadinhas

- "12% a.a. equivalem a 1% a.m. em juros compostos." **Errado:** 1% a.m. equivale a 12,68% a.a.
- "O desconto racional é maior que o comercial." **Errado:** é menor.

### Frase de fixação

> **Descubra o regime e a base do desconto antes de fazer a conta.**

## 5. Case — 3 min

### Situação

> Um empreendedor tem uma nota de R$ 50.000 para receber em 90 dias e quer comprar à vista uma máquina de R$ 30.000. O banco oferece desconto comercial simples de 3% a.m.

### Conceitos aplicados

| Etapa | Conta | Resultado |
| --- | --- | --- |
| Desconto | 50.000 × 3% × 3 | R$ 4.500 |
| Líquido recebido | 50.000 − 4.500 | **R$ 45.500** |
| Compra da máquina | 45.500 − 30.000 | Sobra **R$ 15.500** em caixa |
| Custo efetivo | (50.000 ÷ 45.500)^(1/3) − 1 | ≈ **3,19% a.m.** |

### Síntese do case

A antecipação resolve o caixa, mas custa mais do que os 3% anunciados. Se a máquina se paga (payback, Aula D), a operação faz sentido.

### Frase de fixação

> **Desconto resolve o caixa hoje; a taxa efetiva mostra o preço de verdade.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 1.3.5 Taxa de desconto comercial · **Nível:** Fácil

### Questão

Uma empresa desconta em um banco uma duplicata de R$ 20.000,00 com vencimento em 60 dias, a uma taxa de desconto comercial simples de 2,5% ao mês. O valor líquido recebido pela empresa será de:

A) R$ 19.000,00.

B) R$ 19.047,62.

C) R$ 18.000,00.

D) R$ 19.500,00.

### Ponto-chave do enunciado

"**Desconto comercial simples**" → por fora, sobre o valor nominal.

### Gabarito

**Alternativa A.**

### Comentário da alternativa correta

D = 20.000 × 0,025 × 2 = R$ 1.000 → líquido = **R$ 19.000,00**.

### Por que as demais estão incorretas?

- **B:** 20.000 ÷ 1,05 é o desconto **racional** simples (por dentro).
- **C:** usou 5% ao mês (dobrou a taxa) ou 4 meses.
- **D:** aplicou só um mês de desconto.

### Armadilhas e macetes

- **Comercial = multiplica o valor de face pela taxa e pelo prazo.**

### Referência

APOSTILA-CPA p. 138–139; PDF A3477 p. 3–5; Programa Detalhado CPA, item 1.3.5.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. Simples: J = C × i × n; composto: M = C × (1 + i)^n; a diferença cresce com o tempo.
2. Proporcional (simples): multiplica pelo tempo; equivalente (composto): (1 + i)^(n₂/n₁) − 1.
3. Comercial (por fora): D = N × i × n; racional (por dentro): A = N ÷ (1 + in); o comercial desconta mais.
4. Desconto bancário simples = comercial + taxa administrativa; pode haver IOF; custo efetivo > taxa anunciada.
5. Antecipar recebíveis e direitos creditórios transforma venda a prazo em caixa hoje.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Juros simples | M = C × (1 + i × n) |
| Juros compostos | M = C × (1 + i)^n |
| Proporcional | 2% a.m. = 24% a.a. (simples) |
| Equivalente | 2% a.m. = 26,82% a.a. (composto) |
| Desconto comercial | D = N × i × n (por fora) |
| Desconto racional | A = N ÷ (1 + i × n) (por dentro) |
| Desconto bancário | D = N × (i × n + h) |

### Cadeia lógica

> Escolher o regime (simples ou composto) → converter a taxa (proporcional ou equivalente) → aplicar o desconto (comercial ou racional) → calcular o custo efetivo

### Diferenças que não podem ser confundidas

- **Proporcional ≠ equivalente.**
- **Comercial ≠ racional.**
- **Taxa anunciada ≠ taxa efetiva.**

### Frase central da aula

> **Escada ou bola de neve, por fora ou por dentro: defina a regra antes da conta.**

### Próximo passo de estudo

Aula 1.3-C — Fluxos de caixa, VP, VF e VPL.

## Referências oficiais e status

Último acesso: 2026-09-28.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — itens 1.3.2, 1.3.4.3, 1.3.5 e 1.3.8 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. Fórmulas de juros e descontos: matemática financeira clássica, sem norma específica.
3. Incidência de IOF em desconto de títulos: citada só de forma geral; alíquotas **não reabertas nesta sessão**.

Fontes de origem (não oficiais): PDFs A3472 "Estudo das Taxas de Juros" e A3477 "Taxa de Desconto Comercial e Payback" (`00-fontes/materiais-aula/topico-1.3-operacoes-mercado-financeiro/`); APOSTILA-CPA p. 134, 138–139.
