# Aula CPA — Taxas de Juros: Nominal, Efetiva, Real (Fisher), Indexador, Pré × Pós e Bruta × Líquida

Sep 28, 2026 · @Boss · Roteiro integrado · 40 min

## Identificação e alinhamento

Aula A de 5 do item **1.3 Operações do mercado financeiro** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), Módulo 1. Cobre **1.3.1** (nominal × real e indexador), **1.3.4.1** (nominal, efetiva e real — Fisher), **1.3.4.2** (prefixada × pós-fixada) e **1.3.3.4** (taxa bruta × líquida de impostos). Base: PDF **A3472**, **APOSTILA-CPA p. 123–125** e fontes complementares.

| Aula | Conteúdo |
| --- | --- |
| **A (esta)** | Taxas: nominal, efetiva, real, indexador, pré × pós, bruta × líquida |
| B | Capitalização simples × composta, proporcionalidade, equivalência, descontos |
| C | Fluxos, cupom × amortização, mútuo, VP, VF, VPL, taxa de desconto |
| D | Prazo médio, TIR, CMPC, duration, alavancagem, retornos, payback |
| E | SAC × Price |

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 1.3.1 Nominal × real: como se relacionam | PDF A3472 p. 10–11 · APOSTILA-CPA p. 124–125 | Conferido, com correção (nome "Fisher") |
| 1.3.1 Conceito de indexador | PDF A3472 p. 13 (só menção) | **Completado** (conceito clássico) |
| 1.3.4.1 Nominal, efetiva e real (Fisher) | PDF A3472 p. 6, 10–11 · APOSTILA-CPA p. 124–125 | Conferido; exercício **resolvido** |
| 1.3.4.2 Prefixada e pós-fixada | PDF A3472 p. 13 | Conferido; exemplos com taxas inventadas **trocados por genéricos** |
| 1.3.3.4 Taxa bruta × taxa líquida de impostos | PDF A3472 p. 14 · APOSTILA-CPA p. 125 | Conferido; exemplo com a tabela regressiva (Aula 2.1.1.1.8-B) |

**Cobertura PD × PDFs:** todos os subitens têm material, exceto o **conceito de indexador**, completado aqui.

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 3 min |
| 2. Metáfora central | 3 min |
| 3. Tópicos (Os dois sentidos de "nominal" 3 · Taxa efetiva 5 · Taxa real e Fisher 5 · Indexador 3 · Pré, pós e híbrida 3 · Bruta × líquida 3) | 22 min |
| 4. Por que cai na prova | 4 min |
| 5. Case | 3 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **40 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | PDF A3472 p. 10 | "Fórmula de **Fischer**" | Fórmula de **Fisher** (Irving Fisher) | PD CPA 1.3.4.1 |
| 2 | PDF A3472 p. 10 | Taxa nominal = "declarada sem considerar a frequência da capitalização" (um sentido só) | "Nominal" tem **dois sentidos** na prova: (a) **nominal × efetiva**: taxa anunciada com capitalização em outro período; (b) **nominal × real**: taxa antes de descontar a inflação. A aula separa os dois | APOSTILA-CPA p. 124 |
| 3 | PDF A3472 p. 13 | "Tesouro Prefixado 2027 pagando 10,50% a.a."; "Tesouro IPCA+ 2035: 5,50% a.a." | Taxas **não conferidas** → exemplos **genéricos** (X% a.a.; IPCA + Y% a.a.) | — |
| 4 | PDF A3472 p. 11 | Exercício sem resposta | **Resolvido:** taxa real = 1,14 ÷ 1,055 − 1 = **8,06%** | — |

## 1. Fala de abertura — 3 min

> Um CDB rendeu 14% no ano. A inflação foi 5,5%. Quanto você ganhou de verdade?
>
> Metade da sala responde 8,5%. Está **errado**. A conta certa dá **8,06%**.
>
> E um empréstimo que anuncia "24% ao ano, com pagamento mensal"? Na verdade custa **26,82%** ao ano.
>
> Hoje vamos aprender a **ler uma taxa**: nominal, efetiva, real, prefixada, pós-fixada, bruta e líquida.

### Objetivo da abertura

Mostrar que a taxa anunciada quase nunca é a taxa que o investidor recebe.

### Conexão com o Programa Detalhado

CPA 1.3.1, 1.3.4.1, 1.3.4.2 e 1.3.3.4.

## 2. Metáfora central — 3 min

### Metáfora: o salário e o contracheque

> Pense na taxa como um **salário**:
>
> - A **taxa nominal** é o **salário que está no contrato**.
> - A **taxa efetiva** é o que você recebe **no período completo**, contando os reajustes no meio do caminho (os juros sobre juros).
> - A **taxa líquida** é o **contracheque depois do imposto**.
> - A **taxa real** é o que o salário **compra no mercado**, depois da inflação.
> - O **indexador** é a **cláusula de reajuste**: diz se o salário acompanha o CDI, o IPCA ou outro índice.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Salário do contrato | Taxa nominal |
| Salário com reajustes no período | Taxa efetiva |
| Contracheque | Taxa líquida de impostos |
| Poder de compra | Taxa real |
| Cláusula de reajuste | Indexador |

### Frase de fixação

> **Contrato, período, contracheque e mercado: nominal, efetiva, líquida e real.**

## 3. Explicação dos tópicos — 22 min

### 3.1 Os dois sentidos de "taxa nominal" — 3 min

#### Como funciona

| Par | Pergunta que ele responde | Exemplo |
| --- | --- | --- |
| **Nominal × efetiva** | A taxa anunciada considera a capitalização? | "24% a.a. capitalizados mensalmente" é nominal; o custo efetivo é 26,82% a.a. |
| **Nominal × real** | A taxa já descontou a inflação? | CDB de 14% é nominal; descontada a inflação de 5,5%, sobram 8,06% reais |

#### O que a prova pode confundir

- Leia o **par** do enunciado: se aparece **inflação**, o par é nominal × real; se aparece **capitalização**, é nominal × efetiva.

#### Frase de fixação

> **Nominal contra efetiva fala de capitalização; nominal contra real fala de inflação.**

#### Alinhamento ao PD

CPA 1.3.1 e 1.3.4.1.

---

### 3.2 Taxa efetiva — 5 min

#### O que é

**Taxa efetiva** é a taxa **realmente obtida** no período, considerando os **juros sobre juros**. Serve para **comparar** produtos com capitalizações diferentes.

#### Como funciona

> **Taxa efetiva = (1 + taxa do período)^(nº de períodos) − 1**

| Exemplo | Conta | Resultado |
| --- | --- | --- |
| 1% ao mês → ao ano | 1,01¹² − 1 | **12,68% a.a.** |
| 24% a.a. capitalizados mensalmente (= 2% a.m.) | 1,02¹² − 1 | **26,82% a.a.** |

**HP12C (1% a.m.):** `100 CHS PV` · `1 i` · `12 n` · `FV` → 112,68 → **12,68%**.

#### O que a prova pode confundir

- A taxa efetiva é **maior** que a nominal quando há capitalização mais de uma vez no período.
- **Não** se multiplica 1% × 12 em juros compostos (isso é taxa **proporcional**, Aula B).

#### Frase de fixação

> **Efetiva é a taxa que o dinheiro sente no período inteiro.**

#### Alinhamento ao PD

CPA 1.3.4.1.

---

### 3.3 Taxa real e fórmula de Fisher — 5 min

#### O que é

**Taxa real** é o ganho de **poder de compra**: o que a aplicação rendeu **acima da inflação**.

#### Como funciona

> **(1 + nominal) = (1 + real) × (1 + inflação)**
>
> **Taxa real = (1 + nominal) ÷ (1 + inflação) − 1**

**Exercício (PDF A3472 p. 11):** CDB de 14% a.a.; IPCA de 5,5%.

| Passo | Conta | Resultado |
| --- | --- | --- |
| 1 | 1,14 ÷ 1,055 | 1,080569 |
| 2 | − 1 | **8,06% a.a.** |

**HP12C:** `1.14 ENTER 1.055 ÷ 1 − 100 ×` → **8,06**.

**Exemplo da apostila (p. 125):** 12% nominal com 6% de inflação → 1,12 ÷ 1,06 − 1 = **5,66%**.

| Situação | Leitura |
| --- | --- |
| Nominal > inflação | Taxa real **positiva**: ganhou poder de compra |
| Nominal = inflação | Taxa real **zero** |
| Nominal < inflação | Taxa real **negativa**: perdeu poder de compra |

#### O que a prova pode confundir

- **14% − 5,5% = 8,5% é aproximação, não a resposta.** A prova costuma colocar 8,5% como distrator.

#### Frase de fixação

> **Na taxa real, divide; não subtrai.**

#### Alinhamento ao PD

CPA 1.3.1 e 1.3.4.1.

---

### 3.4 Conceito de indexador — 3 min

#### O que é

**Indexador** é o **índice de referência** que corrige ou remunera um contrato ou investimento ao longo do tempo. O valor final só é conhecido quando o índice é apurado.

#### Como funciona

| Indexador | O que mede | Onde aparece |
| --- | --- | --- |
| **CDI / Taxa DI** | Juro entre bancos (B3) | CDB, LCI, LCA, fundos DI |
| **Selic** | Juro básico com título público | Tesouro Selic |
| **IPCA** | Inflação oficial (IBGE) | Tesouro IPCA+, debêntures, CRI/CRA |
| **IGP-M** | Inflação geral (FGV) | Aluguéis, contratos antigos |
| **TR** | Taxa Referencial (BCB) | Poupança, FGTS, financiamento imobiliário |

**Relação com a taxa real:** um título **IPCA + Y%** entrega a **inflação** (pelo indexador) e mais uma **taxa real** de Y%.

#### O que a prova pode confundir

- Indexador **não é** a taxa total: é a parte que varia.
- Pós-fixado sempre tem indexador; prefixado não tem.

#### Frase de fixação

> **Indexador é a cláusula de reajuste do investimento.**

#### Alinhamento ao PD

CPA 1.3.1.

---

### 3.5 Taxas prefixada, pós-fixada e híbrida — 3 min

#### Como funciona

| Tipo | Como é a taxa | Quando se sabe o rendimento | Exemplo genérico |
| --- | --- | --- | --- |
| **Prefixada** | Definida no início | Já na aplicação | Título prefixado a X% a.a. |
| **Pós-fixada** | Percentual de um indexador | Só no fim | CDB 100% do CDI |
| **Híbrida** | Parte fixa + indexador | Parte fixa já; parte variável no fim | IPCA + Y% a.a. |

| Cenário | Quem ganha |
| --- | --- |
| Juros **caem** depois da aplicação | **Prefixado** (travou taxa maior) |
| Juros **sobem** | **Pós-fixado** (acompanha a alta) |
| Inflação **dispara** | **Híbrido IPCA+** (protege o poder de compra) |

#### O que a prova pode confundir

- Prefixado sabe a taxa, mas **tem risco de mercado** se vendido antes do vencimento.

#### Frase de fixação

> **Pré trava, pós acompanha, híbrido protege da inflação.**

#### Alinhamento ao PD

CPA 1.3.4.2.

---

### 3.6 Taxa bruta × taxa líquida de impostos — 3 min

#### Como funciona

> **Taxa líquida = taxa bruta × (1 − alíquota do IR)**

(Válida sobre o rendimento do período, quando o IR incide só no resgate.)

**Exemplo:** CDB de 12% no período, resgatado entre 361 e 720 dias (IR de 17,5%, tabela regressiva da Aula 2.1.1.1.8-B).

| Passo | Conta | Resultado |
| --- | --- | --- |
| 1 | 12% × (1 − 0,175) | **9,90%** |

**Comparação com produto isento:** uma LCI isenta de IR que paga 10% **ganha** do CDB acima (9,90% líquido), mesmo com taxa bruta menor.

#### O que a prova pode confundir

- Compare sempre **líquido com líquido**.
- IR incide sobre o **rendimento**, não sobre o valor aplicado.

#### Frase de fixação

> **Compare o contracheque, não o salário do contrato.**

#### Alinhamento ao PD

CPA 1.3.3.4.

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

A CPA cobra **Fisher** (com a subtração como distrator), **efetiva × nominal** e **qual investimento rende mais líquido**.

### Pontos de atenção

1. **Taxa real = (1 + nominal) ÷ (1 + inflação) − 1.**
2. **Efetiva = (1 + i)^n − 1.**
3. **Indexador = índice que corrige o pós-fixado.**
4. **Pré trava; pós acompanha; híbrido = inflação + taxa real.**
5. **Líquida = bruta × (1 − IR).**

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Nominal | Efetiva | Anunciada × obtida com capitalização |
| Nominal | Real | Antes × depois da inflação |
| Prefixada | Pós-fixada | Taxa conhecida × depende do indexador |
| Bruta | Líquida | Antes × depois do IR |

### Palavras-chave da prova

- **"Poder de compra"**: taxa real.
- **"Capitalizados mensalmente"**: taxa nominal × efetiva.
- **"% do CDI"**: pós-fixado.

### Pegadinhas

- "A taxa real é a nominal menos a inflação." **Errado** (aproximação).
- "2% ao mês equivalem a 24% ao ano em juros compostos." **Errado:** 26,82%.

### Frase de fixação

> **Na dúvida, transforme tudo em fator (1 + taxa) e multiplique ou divida.**

## 5. Case — 3 min

### Situação

> Uma cliente compara: (1) CDB prefixado de 12% a.a. por 2 anos e meio; (2) LCI de 10,5% a.a., isenta; (3) título IPCA + 6% a.a. A inflação esperada é de 4,5% a.a.

### Conceitos aplicados

| Produto | Conta | Resultado |
| --- | --- | --- |
| CDB 12% (IR 15% acima de 720 dias) | 12% × 0,85 | **10,20% líquido** (aproximação anual) |
| LCI isenta | — | **10,50% líquido** |
| IPCA + 6% (antes do IR) | 1,045 × 1,06 − 1 | **10,77% bruto** → × 0,85 ≈ **9,15% líquido** |

### Síntese do case

Com esses números, a LCI isenta vence. Mas se a inflação subir, o IPCA+ melhora e o prefixado piora.

### Frase de fixação

> **Compare líquido, no mesmo prazo, e pergunte o que acontece se a inflação mudar.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 1.3.4.1 Taxa real (Fisher) · **Nível:** Médio

### Questão

Um investidor obteve rentabilidade nominal de 11% em um ano, período em que a inflação foi de 4%. A taxa real de retorno foi de, aproximadamente:

A) 7,00%.

B) 6,73%.

C) 15,44%.

D) 2,75%.

### Ponto-chave do enunciado

"**Taxa real**" com nominal e inflação dadas.

### Gabarito

**Alternativa B.**

### Comentário da alternativa correta

1,11 ÷ 1,04 − 1 = **6,73%** (fórmula de Fisher).

### Por que as demais estão incorretas?

- **A:** 11% − 4% é **aproximação por subtração**, não a taxa real exata.
- **C:** 1,11 × 1,04 − 1: **multiplicou** em vez de dividir.
- **D:** 11 ÷ 4 não tem significado financeiro.

### Armadilhas e macetes

- **Real é "o que sobra" dividindo: 1,11 ÷ 1,04.**

### Referência

APOSTILA-CPA p. 124–125; PDF A3472 p. 10–11; Programa Detalhado CPA, item 1.3.4.1.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. "Nominal" tem dois pares: × efetiva (capitalização) e × real (inflação).
2. Efetiva = (1 + i)^n − 1: 1% a.m. = 12,68% a.a.; 2% a.m. = 26,82% a.a.
3. Fisher: real = (1 + nominal) ÷ (1 + inflação) − 1.
4. Indexador corrige o pós-fixado (CDI, Selic, IPCA, IGP-M, TR); pré trava, pós acompanha, híbrido = inflação + real.
5. Líquida = bruta × (1 − IR); compare sempre líquido com líquido.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Taxa efetiva | (1 + i)^n − 1 |
| Taxa real (Fisher) | (1 + nominal) ÷ (1 + inflação) − 1 |
| Indexador | Índice que corrige o pós-fixado |
| Prefixada | Taxa conhecida na aplicação |
| Pós-fixada | % de um indexador |
| Híbrida | Indexador + taxa fixa (ex.: IPCA + Y%) |
| Taxa líquida | Bruta × (1 − IR) |

### Cadeia lógica

> Taxa do contrato (nominal) → capitalização (efetiva) → imposto (líquida) → inflação (real)

### Diferenças que não podem ser confundidas

- **Efetiva ≠ proporcional.**
- **Real ≠ nominal − inflação.**
- **Bruta ≠ líquida.**

### Frase central da aula

> **Contrato, período, contracheque e mercado: leia a taxa até o fim.**

### Próximo passo de estudo

Aula 1.3-B — Capitalização simples × composta e descontos.

## Referências oficiais e status

Último acesso: 2026-09-28.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — itens 1.3.1, 1.3.3.4, 1.3.4.1 e 1.3.4.2 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. Tabela regressiva de IR (22,5% · 20% · 17,5% · 15%): ver Aula 2.1.1.1.8-B e suas referências. **Em vigor** (MP 1.303/2025 perdeu a validade em out/2025).
3. Fórmulas de taxa efetiva e de Fisher: matemática financeira clássica, sem norma específica.

Fontes de origem (não oficiais): PDF A3472 "Estudo das Taxas de Juros" (`00-fontes/materiais-aula/topico-1.3-operacoes-mercado-financeiro/`); APOSTILA-CPA p. 123–125.
