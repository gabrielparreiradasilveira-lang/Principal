# Aula CPA — Tributação de Renda Fixa e IOF

Sep 25, 2026 · @Boss · Roteiro integrado · 40 min

## Identificação e alinhamento

Aula B de 2 do bloco **2.1.1.1.8 a 2.1.1.1.12** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), Módulo 2. Esta aula cobre **2.1.1.1.11 Tributação de aplicações de renda fixa** e **2.1.1.1.12 Imposto sobre Operações Financeiras (IOF)**. A Aula A cobriu poupança, TR e TLP.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 2.1.1.1.11 Tributação de renda fixa (IR, tabela regressiva, fato gerador, isenções) | PDF A0126 (p. 5–11) · APOSTILA-CPA p. 254, 256–260 | Conferido, com correções |
| 2.1.1.1.12 IOF | PDF A0126 (p. 3–4, 11) · APOSTILA-CPA p. 255–256 | Conferido |
| Come-cotas dos fundos | PDF A0126 (p. 8–9) · APOSTILA-CPA p. 258–259 | Citado de forma breve (tema dos fundos) |
| MP 1.303/2025 (IR único de 17,5%) | — | **Perdeu a validade** em outubro de 2025 → **nota de atualização** |

**Cobertura PD × PDFs:** nenhum subitem ficou sem material.

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 3 min |
| 2. Metáfora central | 3 min |
| 3. Tópicos (IOF 6 · IR e tabela regressiva 7 · Quem segue a tabela e quem é isento 6 · Comparando isento × tributado 3) | 22 min |
| 4. Por que cai na prova | 4 min |
| 5. Case | 3 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **40 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | PDF A0126 p. 5 | Base do IR: "rendimento líquido, isto é, a diferença entre o valor resgatado e o valor aplicado" | Base do IR = **rendimento bruto menos o IOF** (quando houver). Se o resgate ocorrer a partir do 30º dia, a base é o rendimento bruto | APOSTILA-CPA p. 255–257; legislação do IR |
| 2 | PDF A0126 p. 7 · APOSTILA-CPA p. 258 | Tabela regressiva inclui "títulos de capitalização (parcela de rendimento)" | Tributação da capitalização **não reconferida** → **retirada** da lista (fora do escopo deste item) | — |
| 3 | PDF A0126 p. 10 | Isentos: CRI, CRA, LCI, LCA, LIG, poupança, debêntures incentivadas e fundos de infraestrutura | Correto **para pessoa física**. Complemento: só as debêntures **incentivadas (Lei 12.431)** são isentas; as de **infraestrutura (Lei 14.801)** são tributadas (ver aula de debêntures) | Lei 12.431/2011; Lei 14.801/2024 |
| 4 | — | Material não trata da MP 1.303/2025 | A MP propunha **IR único de 17,5%**, mas **perdeu a validade em outubro de 2025**. A tabela regressiva **continua valendo** | Congresso Nacional |

## 1. Fala de abertura — 3 min

> Você aplica R$ 10 mil num CDB, rende R$ 100 e precisa do dinheiro 15 dias depois. Quanto sobra dos R$ 100?
>
> Menos de R$ 40. Metade vai para o **IOF**, e do que sobra ainda sai **Imposto de Renda**.
>
> Agora a mesma aplicação, deixada por mais de dois anos: o IOF some, e o IR cai de 22,5% para 15%. **O governo premia quem espera.**
>
> E tem aplicações em que o Leão não cobra nada da pessoa física: poupança, LCI, LCA, CRI, CRA. Mas "isento" não quer dizer "melhor": às vezes um CDB tributado rende mais no bolso.
>
> Nesta aula você vai dominar as **duas tabelas regressivas** — IOF e IR —, a **ordem de cálculo**, **quem é tributado e quem é isento** e como **comparar** um investimento isento com um tributado.

### Objetivo da abertura

Mostrar que o prazo muda o imposto e que é preciso comparar investimentos pelo rendimento líquido.

### Conexão com o Programa Detalhado

CPA 2.1.1.1.11 e 2.1.1.1.12.

## 2. Metáfora central — 3 min

### Metáfora: as duas cancelas do estacionamento

> Imagine que seu rendimento é um carro estacionado. Para sair, ele passa por **duas cancelas**, nesta ordem.
>
> A primeira é a do **IOF**: a **multa por sair cedo**. Se o carro ficou menos de 30 dias, paga uma multa alta — **96% no primeiro dia**, caindo aos poucos até **zero no 30º dia**. Ela incide sobre **todo o rendimento**.
>
> A segunda é a do **IR**: a **tarifa do estacionamento**, que fica **mais barata quanto mais tempo** o carro fica. **22,5%** até 180 dias, **20%** até 360, **17,5%** até 720 e **15%** depois disso. Ela incide sobre **o que sobrou** depois da primeira cancela.
>
> Alguns carros têm **passe livre**: poupança, LCI, LCA, CRI, CRA e debêntures incentivadas passam sem pagar, se o dono for **pessoa física**.
>
> E quem cobra? O próprio **estacionamento** — a instituição financeira **retém na fonte** na hora da saída.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Primeira cancela: multa por sair cedo | IOF regressivo, só nos primeiros 29 dias |
| Multa sobre todo o rendimento | IOF incide sobre o rendimento bruto |
| Segunda cancela: tarifa que cai com o tempo | IR pela tabela regressiva (22,5% → 15%) |
| Tarifa sobre o que sobrou | IR incide sobre o rendimento após o IOF |
| Passe livre | Isenções para pessoa física |
| Estacionamento cobra na saída | Retenção na fonte pela instituição |
| Momento da saída | Fato gerador: resgate, vencimento, amortização, cupom |

### Frase de fixação

> **Primeiro a multa por sair cedo (IOF sobre o bruto), depois a tarifa que cai com o tempo (IR sobre o que sobrou).**

## 3. Explicação dos tópicos — 22 min

### 3.1 IOF — Imposto sobre Operações Financeiras — 6 min

#### O que é

Imposto que, nas aplicações de renda fixa, funciona como **desestímulo ao curtíssimo prazo**.

#### Como funciona

| Elemento | Regra |
| --- | --- |
| **Base de cálculo** | **Rendimento bruto** |
| **Fato gerador** | Resgate (total ou parcial), vencimento ou amortização **antes de 30 dias** |
| **Alíquota** | **Regressiva por dia**: 96% no 1º dia → **0% a partir do 30º dia** |
| **Recolhimento** | **Retido na fonte** pela instituição financeira |

**Tabela regressiva do IOF (percentual sobre o rendimento):**

| Dia | % | Dia | % | Dia | % |
| --- | --- | --- | --- | --- | --- |
| 1 | 96 | 11 | 63 | 21 | 30 |
| 2 | 93 | 12 | 60 | 22 | 26 |
| 3 | 90 | 13 | 56 | 23 | 23 |
| 4 | 86 | 14 | 53 | 24 | 20 |
| 5 | 83 | 15 | **50** | 25 | 16 |
| 6 | 80 | 16 | 46 | 26 | 13 |
| 7 | 76 | 17 | 43 | 27 | 10 |
| 8 | 73 | 18 | 40 | 28 | 6 |
| 9 | 70 | 19 | 36 | 29 | 3 |
| 10 | 66 | 20 | 33 | **30** | **0** |

**Macete:** a tabela cai em blocos de **3 e 4 pontos** (96, 93, 90 → 86, 83, 80, 76 …). Âncoras: **dia 15 = 50%**; **dia 30 = 0%**.

#### O que a prova pode confundir

- **IOF incide sobre o rendimento**, não sobre o valor aplicado.
- **A partir do 30º dia, IOF zero.**

#### Frase de fixação

> **IOF: multa sobre o rendimento para quem sai antes de 30 dias — 96% no dia 1, 50% no dia 15, zero no dia 30.**

#### Alinhamento ao PD

CPA 2.1.1.1.12.

---

### 3.2 Imposto de Renda e tabela regressiva — 7 min

#### Como funciona

| Elemento | Regra |
| --- | --- |
| **Base de cálculo** | Rendimento **bruto menos o IOF** (se houver) |
| **Fato gerador** | Rendimento disponível: **resgate** total ou parcial, **vencimento**, **amortização**, **pagamento de cupom** |
| **Recolhimento** | **Retido na fonte** pela instituição financeira |
| **Prazo** | Contado da **data da aplicação** até a data do evento |

**Tabela regressiva do IR:**

| Prazo da aplicação | Alíquota |
| --- | --- |
| Até 180 dias | **22,5%** |
| De 181 a 360 dias | **20%** |
| De 361 a 720 dias | **17,5%** |
| Acima de 720 dias | **15%** |

**Ordem de cálculo:** rendimento bruto → **IOF** (se < 30 dias) → sobre o que sobrou, **IR** → rendimento líquido.

#### Exemplo prático

| Situação | Rendimento bruto | IOF | Base do IR | IR | Líquido |
| --- | --- | --- | --- | --- | --- |
| CDB resgatado no **15º dia** | R$ 100,00 | 50% = **R$ 50,00** | R$ 50,00 | 22,5% = **R$ 11,25** | **R$ 38,75** |
| CDB resgatado com **400 dias** | R$ 1.200,00 | 0 | R$ 1.200,00 | 17,5% = **R$ 210,00** | **R$ 990,00** |
| CDB resgatado com **800 dias** | R$ 2.500,00 | 0 | R$ 2.500,00 | 15% = **R$ 375,00** | **R$ 2.125,00** |

**Fundos (visão rápida):** fundos de renda fixa de **longo prazo**, multimercados e cambiais seguem a tabela completa; fundos de **curto prazo** têm alíquota mínima de **20%**. Há **come-cotas** no último dia útil de **maio e novembro**, pela **menor** alíquota do tipo de fundo (15% ou 20%). Detalhes no tema de fundos.

> **Nota de atualização:** a **MP 1.303/2025** propunha substituir a tabela regressiva por uma **alíquota única de 17,5%**. Ela **perdeu a validade em outubro de 2025**; as regras acima **continuam valendo**.

#### O que a prova pode confundir

- **IR incide sobre o rendimento após o IOF.**
- **Acima de 720 dias = 15%** (721 dias ou mais).
- **O prazo conta da data da aplicação**, não do início do ano.

#### Frase de fixação

> **22,5 · 20 · 17,5 · 15 — a cada 180 dias a tarifa cai, até 15% acima de 720 dias.**

#### Alinhamento ao PD

CPA 2.1.1.1.11.

---

### 3.3 Quem segue a tabela e quem é isento — 6 min

#### Como funciona

**Seguem a tabela regressiva (IR) e o IOF:**

| Grupo | Produtos |
| --- | --- |
| Títulos bancários | **CDB, RDB, LC, LF** |
| Títulos públicos | **Tesouro Direto**: LFT, LTN, NTN-F, NTN-B, NTN-B Principal |
| Títulos corporativos | **Debêntures comuns** e de **infraestrutura (Lei 14.801)**, notas comerciais |
| Outros | **COE**, **DPGE** |
| Fundos | Renda fixa, multimercado, cambial (com come-cotas) |

**Isentos de IR para pessoa física:**

| Setor | Produtos |
| --- | --- |
| Imobiliário | **Poupança**, **LCI**, **LIG**, **CRI** |
| Agronegócio | **LCA**, **CRA** |
| Infraestrutura | **Debêntures incentivadas (Lei 12.431)**, fundos de infraestrutura e de debêntures incentivadas |

A **poupança** é isenta também de **IOF** para pessoa física.

#### O que a prova pode confundir

- **Isenção é para pessoa física**; pessoa jurídica é tributada.
- **Debênture incentivada é isenta; debênture comum e de infraestrutura (14.801) não.**
- **Tesouro Direto segue a tabela regressiva**, como o CDB.

#### Frase de fixação

> **Imobiliário, agro e infraestrutura incentivada: isentos para PF. O resto da renda fixa: tabela regressiva.**

#### Alinhamento ao PD

CPA 2.1.1.1.11.

---

### 3.4 Comparando isento × tributado — 3 min

#### Como funciona

Para comparar, converta tudo para o **líquido**:

> **Taxa líquida do tributado = taxa bruta × (1 − alíquota de IR)**
> **Taxa bruta equivalente do isento = taxa isenta ÷ (1 − alíquota de IR)**

#### Exemplo prático

Prazo de 2 anos e 1 mês (IR de 15%):

| Opção | Taxa | Cálculo | Líquido |
| --- | --- | --- | --- |
| CDB | 110% do CDI | 110% × 0,85 | **93,5% do CDI** |
| LCA | 90% do CDI (isenta) | — | **90% do CDI** |

Aqui o **CDB rende mais** no bolso. A LCA isenta só venceria se pagasse **acima de 93,5% do CDI**, ou seja, 110% × 0,85.

#### O que a prova pode confundir

- **Isento não é sempre melhor.**
- **A alíquota de IR usada na comparação depende do prazo.**

#### Frase de fixação

> **Compare no líquido: multiplique o tributado por (1 − IR) antes de escolher o isento.**

#### Alinhamento ao PD

CPA 2.1.1.1.11.

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

A CPA cobra tributação de renda fixa em três formatos: **cálculo** (IOF e IR num resgate), **classificação** (isento × tributado) e **comparação** (isento × tributado no líquido). As tabelas de IR e IOF precisam estar **memorizadas**.

### Pontos de atenção

1. **IOF:** rendimento bruto; só antes de 30 dias; 96% → 0%.
2. **IR:** rendimento após o IOF; **22,5 / 20 / 17,5 / 15**.
3. **Ordem:** IOF primeiro, IR depois.
4. **Retenção na fonte** pela instituição, no resgate, vencimento, amortização ou cupom.
5. **Isentos (PF):** poupança, LCI, LCA, LIG, CRI, CRA, debêntures incentivadas.
6. **Compare pelo líquido.**

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| IOF | IR | Até 29 dias, sobre o bruto × tabela regressiva, sobre o que sobrou |
| Até 180 dias | Acima de 720 dias | 22,5% × 15% |
| CDB | LCI/LCA | Tributado × isento (PF) |
| Debênture incentivada | Debênture comum | Isenta × tributada |
| Pessoa física | Pessoa jurídica | Isenções × tributação |

### Palavras-chave da prova

- **"Antes de 30 dias"**: IOF.
- **"Acima de 720 dias"**: 15%.
- **"Rendimento bruto"**: base do IOF.
- **"Retido na fonte"**: responsabilidade da instituição.
- **"Pessoa física"**: condição das isenções.

### Pegadinhas

- "O IOF incide sobre o valor aplicado." **Errado:** sobre o rendimento.
- "O IR incide sobre o rendimento bruto, antes do IOF." **Errado.**
- "Aplicação de 500 dias paga 15% de IR." **Errado:** 17,5%.
- "O Tesouro Direto é isento de IR." **Errado.**
- "LCA isenta sempre rende mais que CDB." **Errado:** compare no líquido.
- "Desde 2026 a renda fixa tem alíquota única de 17,5%." **Errado:** a MP 1.303 perdeu a validade.

### Frase de fixação

> **IOF antes, IR depois; 22,5 · 20 · 17,5 · 15; isento só para PF — e compare sempre no líquido.**

## 5. Case — 3 min

### Situação

> Beatriz, pessoa física, tem R$ 50 mil e três opções para **2 anos e meio**:
>
> - **CDB** a 112% do CDI;
> - **LCI** a 92% do CDI;
> - **Tesouro Selic** (100% da Selic, aproximadamente o CDI), considerado isento por ela "por ser do governo".
>
> Ela também precisou resgatar R$ 5 mil de outro CDB **no 10º dia**, com rendimento de R$ 20.

### Conceitos aplicados

| Situação | Regra | Resultado |
| --- | --- | --- |
| CDB 112% do CDI, > 720 dias | IR 15% | 112% × 0,85 = **95,2% do CDI** líquido |
| LCI 92% do CDI | Isenta para PF | **92% do CDI** líquido |
| Tesouro Selic ≈ 100% do CDI | **Tributado** (tabela regressiva) + custódia | ≈ **85% do CDI** líquido, antes da custódia |
| Resgate no 10º dia, rendimento de R$ 20 | IOF 66% → R$ 13,20; IR 22,5% sobre R$ 6,80 → R$ 1,53 | Líquido de **R$ 5,27** |

### Análise passo a passo

1. **Converter tudo para o líquido** com a alíquota do prazo (15%).
2. **Corrigir o equívoco:** Tesouro Direto **não é isento**.
3. **Resultado:** o CDB (95,2% líquido) vence a LCI (92%) neste cenário, desconsiderando diferenças de risco e de FGC.
4. **Resgate precoce** mostra o peso do IOF: ele consumiu **66%** do rendimento.

### Síntese do case

A decisão certa exige três passos: **prazo → alíquota → rendimento líquido**. E fugir de resgates antes de 30 dias.

### Frase de fixação

> **Prazo define a alíquota, a alíquota define o líquido, e o líquido define a escolha.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 2.1.1.1.11 e 2.1.1.1.12 Tributação de renda fixa e IOF · **Nível:** Médio

### Questão

Um investidor pessoa física aplicou em um CDB e resgatou o valor no 15º dia, obtendo rendimento bruto de R$ 200,00. Considerando a alíquota de IOF de 50% para o 15º dia e a tabela regressiva do Imposto de Renda, o rendimento líquido recebido pelo investidor foi de:

A) R$ 155,00.

B) R$ 100,00.

C) R$ 77,50.

D) R$ 55,00.

### Ponto-chave do enunciado

"Resgatou no 15º dia" → IOF de 50% e IR de 22,5% (até 180 dias), **nesta ordem**.

### Gabarito

**Alternativa C.**

### Comentário da alternativa correta

1. **IOF:** 50% × R$ 200,00 = **R$ 100,00**. Sobram R$ 100,00.
2. **IR:** 22,5% × R$ 100,00 = **R$ 22,50**.
3. **Líquido:** R$ 200,00 − R$ 100,00 − R$ 22,50 = **R$ 77,50**.

### Por que as demais estão incorretas?

- **A:** aplicou só o IR de 22,5% sobre R$ 200,00 e **ignorou o IOF**.
- **B:** descontou só o IOF e **esqueceu o IR**.
- **D:** somou as alíquotas (50% + 22,5%) sobre o bruto: R$ 200,00 × (1 − 0,725) = R$ 55,00. O IR incide só **sobre o que sobrou** após o IOF.

### Armadilhas e macetes

- **Nunca some as alíquotas**: aplique uma **depois** da outra.
- Até 180 dias → **22,5%**.

### Referência

Tabela regressiva do IOF (Decreto 6.306/2007) e do IR para renda fixa; APOSTILA-CPA p. 255–257; Programa Detalhado CPA, itens 2.1.1.1.11 e 2.1.1.1.12.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. IOF: sobre o rendimento bruto, só em resgates antes de 30 dias; 96% no 1º dia, 50% no 15º, 0% no 30º; retido na fonte.
2. IR: sobre o rendimento após o IOF; 22,5% (até 180 dias), 20% (até 360), 17,5% (até 720), 15% (acima de 720); retido na fonte.
3. Seguem a tabela: CDB, RDB, LC, LF, Tesouro Direto, debêntures comuns e de infraestrutura, COE, DPGE e fundos (com come-cotas).
4. Isentos para PF: poupança, LCI, LCA, LIG, CRI, CRA, debêntures incentivadas e fundos de infraestrutura.
5. Compare sempre no líquido: tributado × (1 − IR) contra o isento. A MP 1.303/2025 (IR único de 17,5%) perdeu a validade.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| IOF | Bruto · < 30 dias · 96% → 0% · dia 15 = 50% |
| IR | Após IOF · 22,5 / 20 / 17,5 / 15 |
| Ordem | IOF → IR |
| Retenção | Na fonte, pela instituição |
| Isentos PF | Poupança · LCI · LCA · LIG · CRI · CRA · debênture incentivada |
| Comparação | Líquido = bruto × (1 − IR) |

### Cadeia lógica

> rendimento bruto → IOF (se < 30 dias) → IR pela tabela do prazo → rendimento líquido → comparação com os isentos

### Diferenças que não podem ser confundidas

- **IOF ≠ IR** (base, prazo e tabela).
- **Rendimento bruto ≠ base do IR** (quando há IOF).
- **Isento (PF) ≠ isento (PJ).**
- **Debênture incentivada ≠ debênture de infraestrutura.**

### Frase central da aula

> **O rendimento sai por duas cancelas — a multa do IOF para quem sai cedo e a tarifa do IR que barateia com o tempo —, e só alguns carros de pessoa física têm passe livre.**

### Próximo passo de estudo

Resolver 10 cálculos de IOF + IR em prazos diferentes e 5 comparações isento × tributado; seguir para os próximos itens do PD.

## Referências oficiais e status

Último acesso: 2026-09-25.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — itens 2.1.1.1.11 e 2.1.1.1.12 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. Presidência da República — Decreto 6.306/2007 — regulamento do IOF (tabela regressiva de 30 dias). **Em vigor.** **Texto não reaberto nesta sessão.**
3. Presidência da República — Lei 11.033/2004 — tabela regressiva do IR na renda fixa e isenções. **Em vigor.** **Texto não reaberto nesta sessão.**
4. Congresso Nacional — MP 1.303/2025 — **perdeu a validade** em outubro de 2025 — [InfoMoney](https://www.infomoney.com.br/minhas-financas/mp-1-303-cai-no-congresso-veja-como-fica-a-tributacao-dos-investimentos-agora/). **Sem efeitos.**
5. Lei 12.431/2011 e Lei 14.801/2024 — regimes de debêntures (ver aula de debêntures). **Em vigor.**

Fontes de origem (não oficiais): PDF A0126 "Tributação de Renda Fixa" (`00-fontes/materiais-aula/topico-2.1.1.1.8-poupanca-tr-tlp-tributacao/`); APOSTILA-CPA, p. 254–260.
