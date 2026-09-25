# Aula CPA — Risco Sistêmico e Acordos de Basileia

Sep 25, 2026 · @Boss · Roteiro integrado · 30 min

## Identificação e alinhamento

Aula A de 2 do bloco **1.4.3 a 1.4.6** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), Módulo 1. Esta aula cobre **1.4.3 Ferramentas utilizadas pelo Bacen para intermediação financeira e suas características**, com **1.4.3.1 Definição de risco sistêmico** e **1.4.3.2 Índice de Basileia I, II e III e os principais riscos (liquidez e alavancagem)**. A Aula B cobre clearing houses, risco de contraparte, B3 e Selic.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 1.4.3 Ferramentas do Bacen para intermediação | PDF A3492 p. 3–4, 7, 14–15 · APOSTILA-CPA p. 169, 173–174 | Conferido, com **nota de atualização** |
| 1.4.3.1 Risco sistêmico | PDF A3492 p. 5–6 · APOSTILA-CPA p. 170 | Conferido |
| 1.4.3.2 Basileia I, II e III; liquidez e alavancagem | PDF A3492 p. 8–13 · APOSTILA-CPA p. 171–173 | Conferido, com **notas de atualização** |

**Cobertura PD × PDFs:** o 1.4.3 está coberto pelo PDF. As divergências com a norma entram como **nota de atualização**, como você decidiu.

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 2 min |
| 2. Metáfora central | 2 min |
| 3. Tópicos (Bacen e intermediação 2 · Risco sistêmico e riscos prudenciais 4 · Acordos de Basileia 3 · PR, RWA e Índice de Basileia 4 · Buffers, liquidez e macroprudenciais 3) | 16 min |
| 4. Por que cai na prova | 3 min |
| 5. Case | 2 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **30 min** |

### Correções feitas na fonte

Conforme sua decisão, os itens abaixo **não alteram o texto-base**; aparecem como **nota de atualização** no tópico correspondente.

| # | Fonte | O material diz | O que diz a norma / fonte oficial | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | PDF A3492 p. 14 · APOSTILA-CPA p. 174 | "ACCPBrasil: permite financiamento de exportações" | ACCPBrasil = **Adicional Contracíclico de Capital Principal**, fixado pelo **Comef**. Em maio/2026 foi **mantido em 0%** | Comef — Ata da 65ª reunião (26–27/05/2026) |
| 2 | PDF A3492 p. 11–12 · APOSTILA-CPA p. 172–173 | "Mínimo de 8% + buffers"; apostila: conservação "2%", contracíclico "até 2%" | **PR 8%**, **Nível I 6%**, **Capital Principal 4,5%** do RWA. Adicionais: **conservação 2,5%**; **contracíclico até 2,5%**; **sistêmico até 2%** (só S1) | Res. CMN 4.958/2021, arts. 4º a 8º |
| 3 | PDF A3492 p. 8 | "Basileia II (2004): inclui riscos de mercado e operacional" | O **risco de mercado** entrou em **1996** (emenda a Basileia I). Basileia II trouxe o **risco operacional** e os **três pilares** (capital, supervisão, disciplina de mercado) | BIS |
| 4 | APOSTILA-CPA p. 172 | Títulos públicos "ponderados em 100%" | O PDF está certo: títulos públicos têm **baixa ponderação**. Percentual exato **não reconferido** nesta sessão | — |
| 5 | APOSTILA-CPA p. 173 | LCR e NSFR como "ferramentas de liquidez" de socorro do BC | LCR e NSFR são **exigências de liquidez** que os **bancos** cumprem, não empréstimos do BC | Basileia III |
| 6 | PDF A3492 p. 11 | Fórmula em imagem | **Índice de Basileia = PR ÷ RWA** | Res. CMN 4.958/2021 |

## 1. Fala de abertura — 2 min

> Você deposita R$ 1.000 no banco. O banco empresta quase tudo. E se muitos tomadores não pagarem? E se todos os depositantes quiserem o dinheiro de volta no mesmo dia?
>
> O Banco Central não empresta seu dinheiro, mas **obriga o banco a ter capital e liquidez suficientes** para aguentar esses sustos.
>
> As regras vêm de acordos internacionais com nome de cidade suíça: **Basileia**. Nesta aula você vai aprender **o risco que elas evitam** e **a conta que mede se um banco está seguro**.

### Objetivo da abertura

Ligar a intermediação bancária aos riscos e às exigências de capital e liquidez.

### Conexão com o Programa Detalhado

CPA 1.4.3, 1.4.3.1 e 1.4.3.2.

## 2. Metáfora central — 2 min

### Metáfora: o prédio e as fundações

> Cada banco é um **prédio**. A carteira de empréstimos é o **peso** que o prédio carrega. O **capital próprio (PR)** é a **fundação**.
>
> Quanto mais pesado e arriscado o que o prédio carrega (**RWA**), mais funda precisa ser a fundação. O **Índice de Basileia** é a **conta do engenheiro**: fundação dividida pelo peso ajustado ao risco. Mínimo de 8%.
>
> Os **buffers** são **vigas extras** para tempestades. O **LCR** e o **NSFR** são a **caixa-d'água do prédio**: água para 30 dias e encanamento estável para o longo prazo.
>
> Se um prédio desaba e derruba o vizinho, e o vizinho derruba o próximo, temos o **risco sistêmico**: o **efeito dominó**.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Fundação | Patrimônio de Referência (PR) |
| Peso ajustado ao risco | Ativos Ponderados pelo Risco (RWA) |
| Conta do engenheiro | Índice de Basileia = PR ÷ RWA |
| Vigas extras | Buffers de capital |
| Caixa-d'água | LCR (30 dias) e NSFR (longo prazo) |
| Prédios caindo em sequência | Risco sistêmico |

### Frase de fixação

> **Quanto mais risco o banco carrega, mais capital precisa ter.**

## 3. Explicação dos tópicos — 16 min

### 3.1 O Bacen e a intermediação financeira — 2 min

#### Como funciona

**Intermediação financeira:** os bancos **captam** de quem tem sobra (poupadores) e **emprestam** a quem precisa (tomadores). Exemplo: você aplica no CDB e o banco empresta a uma empresa.

**O Bacen não é intermediário**: é o **supervisor prudencial**. Cria normas, exige capital e liquidez, monitora riscos, exige planos de capital e de contingência e aplica medidas preventivas.

#### Frase de fixação

> **O banco intermedeia; o Bacen fiscaliza para a intermediação não quebrar o sistema.**

#### Alinhamento ao PD

CPA 1.4.3.

---

### 3.2 Risco sistêmico e riscos prudenciais — 4 min

#### O que é

**Risco sistêmico** é o risco de **colapso do sistema financeiro como um todo**: o problema de uma instituição se espalha para as outras (**efeito dominó**).

#### Como funciona

> quebra de um grande banco → perda de confiança → corrida bancária → retração do crédito → dano à economia real

Para evitá-lo, o Bacen controla os **riscos prudenciais** de cada instituição:

| Risco | O que é |
| --- | --- |
| **Crédito** | Inadimplência de clientes ou contrapartes |
| **Liquidez** | Falta de recursos para honrar obrigações no prazo |
| **Mercado** | Perdas com juros, câmbio e preços |
| **Alavancagem** | Muitas operações com pouco capital próprio |

#### O que a prova pode confundir

- **Risco sistêmico é do sistema; os riscos prudenciais são de cada instituição**, e controlá-los evita o sistêmico.

#### Frase de fixação

> **Controlar o risco de cada banco evita o dominó do sistema.**

#### Alinhamento ao PD

CPA 1.4.3.1.

---

### 3.3 Acordos de Basileia I, II e III — 3 min

#### Como funciona

Acordos do **Comitê de Basileia**, ligado ao **BIS (Banco de Compensações Internacionais)**, que servem de base para as regras prudenciais no mundo.

| Acordo | Ano | Foco (material) |
| --- | --- | --- |
| **Basileia I** | 1988 | **Risco de crédito**; capital mínimo de 8% |
| **Basileia II** | 2004 | Inclui riscos de mercado e **operacional** |
| **Basileia III** | 2010 | Resposta à crise de 2008: **mais e melhor capital**, **buffers**, **liquidez (LCR e NSFR)** e controle da **alavancagem** |

> **Nota de atualização:** o **risco de mercado** foi incorporado em **1996**, por emenda a Basileia I. **Basileia II** trouxe o **risco operacional** e os **três pilares**: requerimento de capital, supervisão e disciplina de mercado.

#### Frase de fixação

> **Basileia I olhou o crédito, II ampliou os riscos, III reforçou capital e liquidez.**

#### Alinhamento ao PD

CPA 1.4.3.2.

---

### 3.4 PR, RWA e Índice de Basileia — 4 min

#### Como funciona

| Conceito | O que é |
| --- | --- |
| **PR — Patrimônio de Referência** | Capital que absorve perdas. **Nível I** (capital principal: ações e lucros retidos) + **Nível II** (dívida subordinada e ajustes) |
| **RWA — Ativos Ponderados pelo Risco** | Ativos ajustados pelo risco: empréstimo arriscado pesa mais; título público pesa pouco |
| **Índice de Basileia** | **PR ÷ RWA**; mínimo de **8%** no Brasil, mais os buffers |

#### Exemplo prático

| Item | Valor |
| --- | --- |
| Ativo de R$ 100 com ponderação de 50% | RWA = **R$ 50** |
| Banco com PR de R$ 12 bi e RWA de R$ 100 bi | Índice = 12 ÷ 100 = **12%** → acima do mínimo |
| Banco com PR de R$ 7 bi e RWA de R$ 100 bi | Índice = **7%** → **abaixo** de 8% |

> **Nota de atualização (Res. CMN 4.958/2021):** os mínimos são **PR 8%**, **Nível I 6%** e **Capital Principal 4,5%** do RWA.

#### O que a prova pode confundir

- **Índice de Basileia maior = banco mais capitalizado.**
- **O denominador é o RWA, não o ativo total.**

#### Frase de fixação

> **Basileia = PR sobre RWA; abaixo de 8%, o banco está desenquadrado.**

#### Alinhamento ao PD

CPA 1.4.3.2.

---

### 3.5 Buffers, liquidez e medidas macroprudenciais — 3 min

#### Como funciona

**Buffers de capital** ("almofadas" além do mínimo):

| Buffer | Função |
| --- | --- |
| **Conservação** | Reserva permanente para tempos de estresse |
| **Contracíclico** | Sobe na bonança para frear o crédito; é liberado na crise |

**Liquidez (Basileia III):**

| Indicador | Exige |
| --- | --- |
| **LCR** (Liquidity Coverage Ratio) | Ativos líquidos de alta qualidade para cobrir **30 dias** de saídas em estresse |
| **NSFR** (Net Stable Funding Ratio) | **Captação estável** para financiar ativos de longo prazo (horizonte de 1 ano) |

**Medidas macroprudenciais do Bacen (material):** depósito compulsório; LLI e LLT; ACCPBrasil.

> **Nota de atualização:**
> - Pela **Res. CMN 4.958/2021**, os buffers (chamados de **Adicional de Capital Principal, ACP**) são: **conservação 2,5%**; **contracíclico até 2,5%**; **sistêmico até 2%** (só bancos do S1).
> - O **ACCPBrasil** é o **Adicional Contracíclico de Capital Principal**, fixado pelo **Comef**, e **não** uma linha de financiamento à exportação. Na reunião de maio/2026 ficou **em 0%**.
> - LCR e NSFR são **exigências** que o banco cumpre, não empréstimos do BC.

#### O que a prova pode confundir

- **Buffer contracíclico sobe na bonança e cai na crise.**
- **LCR = 30 dias; NSFR = longo prazo.**

#### Frase de fixação

> **Buffers dão fôlego de capital; LCR e NSFR dão fôlego de caixa.**

#### Alinhamento ao PD

CPA 1.4.3 e 1.4.3.2.

## 4. Por que isso cai na prova? — 3 min

### Explicação estratégica

A CPA cobra este item por **definição** (risco sistêmico, Basileia), por **fórmula** (PR ÷ RWA, 8%) e por **função** (buffer contracíclico, LCR, NSFR).

### Pontos de atenção

1. **Bacen não intermedeia; supervisiona.**
2. **Risco sistêmico = efeito dominó.**
3. **Riscos prudenciais:** crédito, liquidez, mercado, alavancagem.
4. **Basileia I (1988, crédito) · II (2004) · III (2010, capital e liquidez).**
5. **Índice de Basileia = PR ÷ RWA ≥ 8%.**
6. **LCR 30 dias; NSFR longo prazo.**

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| PR | RWA | Capital × ativos ajustados ao risco |
| Buffer de conservação | Buffer contracíclico | Permanente × varia com o ciclo |
| LCR | NSFR | 30 dias × longo prazo |
| Risco sistêmico | Risco de crédito | Sistema × instituição |

### Palavras-chave da prova

- **"Efeito dominó"**: risco sistêmico.
- **"Ativos ponderados pelo risco"**: RWA.
- **"30 dias de estresse"**: LCR.
- **"Captação estável"**: NSFR.

### Pegadinhas

- "O Bacen capta e empresta recursos do público." **Errado.**
- "O Índice de Basileia divide o PR pelo ativo total." **Errado.**
- "O buffer contracíclico aumenta em crises." **Errado.**

### Frase de fixação

> **Mais risco, mais capital; mais prazo, mais captação estável.**

## 5. Case — 2 min

### Situação

> O Banco Delta (fictício) tem PR de R$ 9 bilhões. Seus ativos somam R$ 200 bilhões, mas, ponderados pelo risco, o RWA é de R$ 100 bilhões. O diretor diz: "Nosso índice é 4,5%, estamos quebrados."

### Conceitos aplicados

| Cálculo | Resultado |
| --- | --- |
| Conta do diretor: 9 ÷ 200 | 4,5% (errado: usou o ativo total) |
| Conta correta: PR ÷ RWA = 9 ÷ 100 | **9%** → acima do mínimo de 8% |

### Síntese do case

O Índice de Basileia usa o **RWA**. O Delta está **enquadrado** no mínimo de 8%, mas com pouca folga para os buffers.

### Frase de fixação

> **Basileia se mede sobre o risco, não sobre o tamanho.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 1.4.3.2 Índice de Basileia · **Nível:** Médio

### Questão

Um banco possui Patrimônio de Referência de R$ 6 bilhões e Ativos Ponderados pelo Risco de R$ 80 bilhões. Considerando o requerimento mínimo de 8%, é correto afirmar que o Índice de Basileia desse banco é de:

A) 13,3%, acima do mínimo exigido.

B) 7,5%, abaixo do mínimo exigido.

C) 8%, exatamente no mínimo exigido.

D) 7,5%, acima do mínimo exigido.

### Ponto-chave do enunciado

**PR ÷ RWA** e comparação com **8%**.

### Gabarito

**Alternativa B.**

### Comentário da alternativa correta

6 ÷ 80 = **0,075 = 7,5%**, **abaixo** dos 8%. O banco precisa aumentar o capital ou reduzir o risco da carteira.

### Por que as demais estão incorretas?

- **A:** inverteu a fórmula (80 ÷ 6 ≈ 13,3).
- **C:** o índice é 7,5%, não 8%.
- **D:** o valor está certo, mas 7,5% é **menor** que 8%.

### Armadilhas e macetes

- **Capital em cima, risco embaixo.**

### Referência

Res. CMN 4.958/2021; APOSTILA-CPA p. 169–173; Programa Detalhado CPA, item 1.4.3.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. O Bacen não intermedeia; é supervisor prudencial da intermediação feita pelos bancos.
2. Risco sistêmico: colapso do sistema por efeito dominó; evitado controlando crédito, liquidez, mercado e alavancagem.
3. Basileia I (1988, crédito), II (2004, risco operacional e três pilares), III (2010, capital, buffers, liquidez e alavancagem).
4. Índice de Basileia = PR ÷ RWA, mínimo 8% (nota: Nível I 6%, Capital Principal 4,5%).
5. Buffers de conservação e contracíclico; LCR (30 dias) e NSFR (longo prazo) (nota: ACP 2,5% / até 2,5% / até 2%; ACCPBrasil em 0%).

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Bacen | Supervisor prudencial, não intermediário |
| Risco sistêmico | Efeito dominó |
| Riscos prudenciais | Crédito · liquidez · mercado · alavancagem |
| Basileia | I 1988 · II 2004 · III 2010 |
| Índice de Basileia | PR ÷ RWA ≥ 8% |
| Buffers | Conservação (permanente) · contracíclico (ciclo) |
| Liquidez | LCR 30 dias · NSFR longo prazo |

### Cadeia lógica

> intermediação → riscos prudenciais → exigências de capital (PR ÷ RWA) e liquidez (LCR, NSFR) → bancos sólidos → menos risco sistêmico

### Diferenças que não podem ser confundidas

- **PR ≠ RWA.**
- **LCR ≠ NSFR.**
- **Buffer ≠ compulsório** (capital × reserva de depósitos).

### Frase central da aula

> **Fundação proporcional ao peso e caixa-d'água cheia: é assim que Basileia impede o dominó.**

### Próximo passo de estudo

Aula B: clearing houses, risco de contraparte, B3 e Selic.

## Referências oficiais e status

Último acesso: 2026-09-25.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — item 1.4.3 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. CMN — Resolução CMN 4.958/2021 — requerimentos mínimos de PR, Nível I, Capital Principal e ACP — [LegisWeb](https://www.legisweb.com.br/legislacao/?id=422031) · [BCB (versão em inglês)](https://www.bcb.gov.br/content/financialstability/Brazilian_Prudential_Financial_Regulation_Docs/Resolution_CMN_4958.pdf). **Em vigor.**
3. BCB — Ata da 65ª reunião do Comef (26–27/05/2026) — ACCPBrasil mantido em 0% — [PDF BCB](https://www.bcb.gov.br/content/publicacoes/atascomef/202606/Ata_65_Comef_pt.pdf). **Confirmado.**
4. BIS — Comitê de Basileia (Basileia I, emenda de 1996, Basileia II e III). **Referência internacional.** **Não reaberto nesta sessão.**
5. Normas de LCR e NSFR no Brasil (aplicação ao S1). **Não confirmado nesta sessão.**

Fontes de origem (não oficiais): PDF A3492 "Ferramentas do BACEN para Intermediação Financeira" (`00-fontes/materiais-aula/topico-1.4.3-basileia-risco-sistemico-clearings/`); APOSTILA-CPA, p. 169–174.
