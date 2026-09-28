# Aula CPA — Sistemas de Amortização: SAC × Price

Sep 28, 2026 · @Boss · Roteiro integrado · 30 min

## Identificação e alinhamento

Aula E de 5 do item **1.3 Operações do mercado financeiro** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), Módulo 1. Cobre **1.3.7 Sistemas de amortização (SAC e Price)**. Base: PDFs **A3478 e A3479** e **APOSTILA-CPA p. 130–131 e 141–149**.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 1.3.7 SAC | PDF A3478 · APOSTILA-CPA p. 130–131, 141–145 | Conferido; apostila **corrigida** (taxa semestral); exercícios **resolvidos** |
| 1.3.7 Price | PDF A3479 · APOSTILA-CPA p. 131, 145–149 | Conferido, com ajuste ("mais caro"); exercícios **resolvidos**; questão do banco **substituída** por inédita |

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 2 min |
| 2. Metáfora central | 2 min |
| 3. Tópicos (SAC 6 · Price 6 · Comparação e portabilidade 4) | 16 min |
| 4. Por que cai na prova | 3 min |
| 5. Case | 2 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **30 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | APOSTILA-CPA p. 144 | 30% a.a. equivale a "**14,18%** ao semestre" | **14,0175% a.s.** (1,30^0,5 − 1). A própria apostila (p. 148) e o PDF A3478 p. 6 trazem o valor certo | — |
| 2 | PDF A3479 p. 3 | Price "é mais caro para o tomador" | Com a **mesma taxa**, o Price paga **mais juros no total**, porque amortiza mais devagar no começo; mas o custo **a valor presente é o mesmo** (a taxa é a mesma). "Mais caro" vale para o **total de juros pagos** | — |
| 3 | PDF A3479 p. 8–9 | Questão "(11168)" de banco de questões | **Substituída por questão inédita** (padrão do projeto); a conta original confere: economia de **R$ 522,76/mês** | — |
| 4 | PDF A3478 p. 8–9 | Exercícios sem resposta | **Resolvidos**: 7ª parcela SAC semestral = R$ 15.607,02; 2ª parcela SAC mensal = R$ 11.800,00 | — |

## 1. Fala de abertura — 2 min

> Dois vizinhos financiaram R$ 100 mil, com a **mesma taxa** e o **mesmo prazo**.
>
> Um paga parcelas que **começam altas e vão caindo**. O outro paga **sempre o mesmo valor**.
>
> No fim, um pagou **mais juros** que o outro. Qual? E por quê? Hoje: **SAC × Price**.

### Objetivo da abertura

Mostrar que o mesmo empréstimo pode ter parcelas e juros totais diferentes conforme o sistema.

### Conexão com o Programa Detalhado

CPA 1.3.7.

## 2. Metáfora central — 2 min

### Metáfora: a pilha de tijolos

> A dívida é uma **pilha de tijolos**. Cada parcela tira tijolos (amortização) e paga um "aluguel" pelos tijolos que ainda estão na pilha (juros).
>
> No **SAC**, você tira **sempre a mesma quantidade** de tijolos. A pilha cai rápido, o aluguel cai junto, e a parcela **diminui**.
>
> No **Price**, a parcela é **sempre igual**. No começo, quase tudo vai para o aluguel e você tira **poucos** tijolos. Com o tempo, sobra mais para tirar tijolos.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Pilha de tijolos | Saldo devedor |
| Tirar tijolos | Amortização |
| Aluguel dos tijolos | Juros sobre o saldo devedor |
| Mesma quantidade tirada | SAC (amortização constante) |
| Mesmo valor pago | Price (parcela constante) |

### Frase de fixação

> **SAC tira sempre os mesmos tijolos; Price paga sempre o mesmo valor.**

## 3. Explicação dos tópicos — 16 min

### 3.1 SAC — Sistema de Amortização Constante — 6 min

#### Como funciona

| Elemento | Regra |
| --- | --- |
| **Amortização** | **Constante** = saldo inicial ÷ nº de parcelas |
| **Juros** | Taxa × saldo devedor → **decrescentes** |
| **Parcela** | Amortização + juros → **decrescente** |
| Uso típico | **Financiamento imobiliário** |

**Exemplo (APOSTILA-CPA p. 144–145):** R$ 100.000 em 10 parcelas mensais, 2% a.m.

| Parcela | Saldo antes | Juros (2%) | Amortização | Parcela | Saldo depois |
| --- | --- | --- | --- | --- | --- |
| 1 | 100.000 | 2.000 | 10.000 | **12.000** | 90.000 |
| 2 | 90.000 | 1.800 | 10.000 | **11.800** | 80.000 |
| 3 | 80.000 | 1.600 | 10.000 | **11.600** | 70.000 |

**Fórmula de uma parcela específica:**

> **PMTₜ = (PV ÷ n) × [1 + (n − t + 1) × i]**

| Exercício | Conta | Resultado |
| --- | --- | --- |
| 2ª parcela (R$ 100 mil, 10×, 2% a.m.) | 10.000 × [1 + 9 × 0,02] | **R$ 11.800,00** |
| 7ª parcela (R$ 100 mil, 10 semestres, 30% a.a. → 14,0175% a.s.) | 10.000 × [1 + 4 × 0,140175] | **R$ 15.607,02** |

**Total de juros (10× a 2% a.m.):** 2% × 10.000 × (10 + 9 + … + 1) = **R$ 11.000,00**.

#### O que a prova pode confundir

- No SAC, a **parcela cai**, mas a **amortização não muda**.
- Converter a taxa com **equivalência** (composta), não proporcionalidade.

#### Frase de fixação

> **SAC: amortização fixa, juros caindo, parcela caindo.**

#### Alinhamento ao PD

CPA 1.3.7.

---

### 3.2 Price — Sistema Francês (parcela constante) — 6 min

#### Como funciona

| Elemento | Regra |
| --- | --- |
| **Parcela** | **Constante** |
| **Juros** | Taxa × saldo devedor → **decrescentes** |
| **Amortização** | Parcela − juros → **crescente** |
| Uso típico | Veículos, crédito pessoal, bens de consumo |

> **PMT = PV × i ÷ [1 − (1 + i)^(−n)]**

**Exemplo 1:** R$ 100.000 em 10 × 2% a.m.

| Parcela | Juros | Amortização | Parcela | Saldo depois |
| --- | --- | --- | --- | --- |
| 1 | 2.000,00 | 9.132,65 | **11.132,65** | 90.867,35 |
| 2 | 1.817,35 | 9.315,31 | **11.132,65** | 81.552,04 |
| 3 | 1.631,04 | 9.501,61 | **11.132,65** | 72.050,43 |

**Total de juros:** 10 × 11.132,65 − 100.000 = **R$ 11.326,53** (maior que os R$ 11.000 do SAC).

**Exemplo 2 (PDF A3479 p. 6 / APOSTILA-CPA p. 148):** R$ 100.000, 10 semestres, 30% a.a.

| Passo | HP12C | Resultado |
| --- | --- | --- |
| Taxa semestral | `1.3 ENTER 0.5 yˣ 1 − 100 ×` | 14,0175% |
| Parcela | `100000 PV` · `14.0175 i` · `10 n` · `PMT` | **R$ 19.184,48** |
| Composição da 1ª | `1 f AMORT` → juros; `x≷y` → amortização | Juros **R$ 14.017,54** · amortização **R$ 5.166,94** |
| Saldo após a 1ª | `RCL PV` | **R$ 94.833,06** |

#### O que a prova pode confundir

- No Price, a **parcela é fixa**, mas a **composição muda**: juros caem, amortização sobe.
- **Antecipar parcelas** no início rende **menos economia** que no SAC, porque o saldo cai devagar.

#### Frase de fixação

> **Price: parcela fixa, juros caindo, amortização subindo.**

#### Alinhamento ao PD

CPA 1.3.7.

---

### 3.3 Comparação e portabilidade — 4 min

#### Como funciona

| Característica | SAC | Price |
| --- | --- | --- |
| Parcela | **Decrescente** | **Constante** |
| Amortização | **Constante** | **Crescente** |
| Juros | Decrescentes | Decrescentes (mais devagar) |
| 1ª parcela | **Maior** | Menor |
| Saldo devedor | Cai **mais rápido** | Cai mais devagar no início |
| Total de juros pagos (mesma taxa e prazo) | **Menor** | **Maior** |
| Custo a valor presente | Igual (mesma taxa) | Igual (mesma taxa) |

**Portabilidade (APOSTILA-CPA p. 148–149):** refinanciar o saldo com taxa menor reduz a parcela. Saldo R$ 490.000, 173 meses, 9,5% → 7,5% a.a. (Price): parcela R$ 5.097,49 → R$ 4.574,74 = economia de **R$ 522,76/mês**.

#### Frase de fixação

> **SAC começa pesado e alivia; Price é constante e paga mais juros no total.**

#### Alinhamento ao PD

CPA 1.3.7.

## 4. Por que isso cai na prova? — 3 min

### Explicação estratégica

A CPA cobra **o que é constante em cada sistema**, **o que cresce e o que cai**, e contas de **parcela**.

### Pontos de atenção

1. **SAC: amortização constante, parcela decrescente.**
2. **Price: parcela constante, amortização crescente.**
3. **Nos dois, os juros caem.**
4. **Mesma taxa e prazo: Price paga mais juros no total.**
5. **Parcela SAC: (PV ÷ n) × [1 + (n − t + 1) × i].**

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| SAC | Price | Amortização fixa × parcela fixa |
| Primeira parcela SAC | Primeira parcela Price | Maior × menor |
| Juros totais SAC | Juros totais Price | Menor × maior |

### Palavras-chave da prova

- **"Prestações decrescentes"**: SAC.
- **"Prestações iguais" / "sistema francês"**: Price.
- **"Amortizações crescentes"**: Price.

### Pegadinhas

- "No SAC, os juros são constantes." **Errado:** a amortização é constante.
- "No Price, a amortização é constante." **Errado:** a parcela é constante.

### Frase de fixação

> **Pergunte: o que é constante? Amortização = SAC; parcela = Price.**

## 5. Case — 2 min

### Situação

> Um casal vai financiar um imóvel. Com o SAC, a primeira parcela é maior, mas cabe no orçamento. Com o Price, a primeira é menor. Eles pretendem fazer amortizações extras nos primeiros anos.

### Conceitos aplicados

| Ponto | Sistema favorecido |
| --- | --- |
| Pagar menos juros no total | **SAC** |
| Parcela inicial menor | **Price** |
| Amortizar extra no início com mais efeito | **SAC** |

### Síntese do case

Se a primeira parcela cabe no bolso e o plano é antecipar, o SAC tende a ser melhor.

### Frase de fixação

> **Cabe no bolso hoje? SAC economiza juros amanhã.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 1.3.7 Sistemas de amortização · **Nível:** Difícil

### Questão

Uma família tem saldo devedor de R$ 300.000,00 em um financiamento pela tabela Price, com 120 parcelas mensais restantes e taxa efetiva de 12% ao ano. Ela consegue portar a dívida para outra instituição, mantendo o prazo e o sistema Price, com taxa efetiva de 10% ao ano. A redução aproximada da parcela mensal será de:

A) R$ 305,15.

B) R$ 500,00.

C) R$ 3.893,26.

D) R$ 25,43.

### Ponto-chave do enunciado

Converter as taxas **anuais efetivas** em **mensais equivalentes** e calcular as duas parcelas.

### Gabarito

**Alternativa A.**

### Comentário da alternativa correta

| Cenário | Taxa mensal | HP12C | Parcela |
| --- | --- | --- | --- |
| Atual | 1,12^(1/12) − 1 ≈ 0,9489% | `300000 PV` · `120 n` · `0.9489 i` · `PMT` | R$ 4.198,42 |
| Nova | 1,10^(1/12) − 1 ≈ 0,7974% | idem com `0.7974 i` | R$ 3.893,26 |
| **Economia** | | | **R$ 305,15** |

### Por que as demais estão incorretas?

- **B:** aplicou a diferença de 2% ao ano sobre o saldo e dividiu por 12 (300.000 × 2% ÷ 12): ignora a amortização e o prazo.
- **C:** é o valor da **nova parcela**, não a redução.
- **D:** dividiu a economia mensal por 12 de novo.

### Armadilhas e macetes

- **Taxa anual efetiva → mensal por equivalência, nunca dividindo por 12.**

### Referência

APOSTILA-CPA p. 145–149; PDF A3479; Programa Detalhado CPA, item 1.3.7.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. SAC: amortização constante (saldo ÷ n), juros e parcela decrescentes.
2. Price: parcela constante (PMT), juros decrescentes, amortização crescente.
3. Mesma taxa e prazo: o Price paga mais juros no total; a valor presente o custo é igual.
4. Parcela SAC: (PV ÷ n) × [1 + (n − t + 1) × i]; Price na HP12C: PV, i, n → PMT; f AMORT e RCL PV.
5. Portabilidade com taxa menor reduz a parcela; converta taxas por equivalência.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| SAC | Amortização fixa · parcela decrescente |
| Price | Parcela fixa · amortização crescente |
| Juros | Caem nos dois sistemas |
| Juros totais | Price > SAC (mesma taxa e prazo) |
| Parcela SAC | (PV ÷ n) × [1 + (n − t + 1) × i] |
| Parcela Price | PV × i ÷ [1 − (1 + i)^(−n)] |
| HP12C | PMT · f AMORT · RCL PV |

### Cadeia lógica

> Converter a taxa → escolher o sistema → calcular parcela → separar juros e amortização → acompanhar o saldo

### Diferenças que não podem ser confundidas

- **Amortização constante ≠ parcela constante.**
- **Juros totais maiores ≠ custo a valor presente maior.**

### Frase central da aula

> **SAC tira sempre os mesmos tijolos; Price paga sempre o mesmo valor.**

### Próximo passo de estudo

Item 1.4 — Regulação (aulas já disponíveis) e revisão do Módulo 1.

## Referências oficiais e status

Último acesso: 2026-09-28.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — item 1.3.7 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. Fórmulas de SAC e Price: matemática financeira clássica, sem norma específica.

Fontes de origem (não oficiais): PDFs A3478 "Sistemas de Amortização" e A3479 "Tabela Price ou Sistema Francês" (`00-fontes/materiais-aula/topico-1.3-operacoes-mercado-financeiro/`); APOSTILA-CPA p. 130–131, 141–149.
