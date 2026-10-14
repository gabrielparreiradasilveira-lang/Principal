# Roteiro de fala — Aula CPA: Tesouro Direto: Plataforma, Produtos, Renda+ e Educa+

**Base:**
- documento "14-10 GRAVAR- Tesouro Direto, Renda+, Educa+ e custódia" (Google Docs);
- aula do repositório `aulas/cpa/aula-2.1.1-B-tesouro-direto/aula.md`;
- APOSTILA-CPA, p. 204–212 e 218–221.

O documento original não foi alterado.

CPA 2.1.1.1.1.4 · 2.1.1.1.2 · Módulo 2 · **50 min** (passou de 40 para 50 min por causa dos cálculos na HP12C) · Aula B de 2 (a Aula A cobriu LFT, LTN, NTN-B, NTN-B Principal e NTN-F)

**Legenda:**
- **negrito** = marcador do conteúdo;
- "texto entre aspas" = fala;
- 🔇 = bastidor, sem fala;
- ➕ = acréscimo desta versão;
- 🔗 = ponte para o próximo tópico;
- ⌨️ = teclas da HP12C;
- 🖥️ = o que aparece no visor.

---

## Bastidor — antes de gravar

> 🔇 **O documento está incompleto e tem um valor perdido.**
> - A etapa 4 termina nas pegadinhas, sem frase de fixação.
> - Faltam o case, a questão e a revisão final.
> - Os tópicos não têm frase de fixação.
> - Na correção 3, o trecho "R$ 2 milhões por mês por CPF (desde 18/11/2024; antes era R$ 1 milhão)" virou equação. O documento mostra só "R⟦vazio⟧ 1 milhão)".
>
> Tudo foi recuperado da aula do repositório. O que é novo está marcado com ➕.

### 🔇 Correções da fonte (resumo para quem grava)

| # | O material diz | O correto | Base |
| --- | --- | --- | --- |
| 1 | Apostila p. 207–208: custódia do Renda+ na acumulação de 0% / 0,20% / 0,10% por faixa de prazo (Educa+ idem) | Essas faixas valem **só na venda antecipada**, sobre o valor de resgate: **0,50%** (Renda+ até 10 anos; Educa+ até 7 anos), 0,20% e 0,10%. **Mantido até a conversão: 0%** | B3 — tarifas do Tesouro Direto |
| 2 | Apostila p. 206: investimento "a partir de R$ 30" | Desde **18/11/2024**, **sem valor mínimo**: compra em múltiplos de 0,01 título | B3 / Tesouro Direto |
| 3 | PDF A017 p. 3: limite "R$ 2 milhões por mês" | Correto: **R$ 2 milhões por mês por CPF**, somando todos os títulos (desde 18/11/2024; antes, R$ 1 milhão) | B3 / Tesouro Direto |
| 4 | PDF A017 p. 6: custódia de 0,20% a.a. "sobre o valor bruto atual" | Correto. Complemento: **provisionada diariamente** e **cobrada** em vendas, vencimentos e pagamentos de cupom | B3 |

### ➕ Kit HP12C (mostrar na tela uma vez)

| O que fazer | Teclas | Por quê |
| --- | --- | --- |
| Limpar tudo | ⌨️ `f` `REG` | Apaga dados de cálculos anteriores |
| Duas casas decimais | ⌨️ `f` `2` | Reais e centavos |
| Pagamentos no fim | ⌨️ `g` `END` | Padrão para títulos e parcelas mensais |
| Sinal | O que sai do bolso entra com ⌨️ `CHS` | Preço pago aparece negativo |
| Variação percentual | Valor antigo ⌨️ `ENTER`, valor novo ⌨️ `Δ%` (tecla ao lado de `%`) | Mede quanto o preço subiu ou caiu, em % |

- "Prepare a HP comigo: f REG para limpar, f 2 para duas casas e g END. Lembre: o que sai do bolso entra negativo, com CHS. E hoje vamos usar a tecla delta porcento, que mede quanto um valor variou."

---

## 1. Fala de abertura — 3 min

- **Antes de 2002**
  - "Até 2002, comprar título público era coisa de banco. Uma pessoa comum não tinha como emprestar diretamente para o governo. Hoje, qualquer pessoa com CPF, uma conta em corretora e alguns centavos consegue."

- **A primeira pegadinha**
  - "Mas 'Tesouro Direto' é um investimento? Não. É uma plataforma, um programa. O investimento é o título que você compra lá dentro. Guarde isso, porque a prova cobra."

- **Os títulos com objetivo de vida**
  - "Dentro dessa plataforma existem dois títulos desenhados para objetivos de vida. O Renda+ funciona como uma aposentadoria que paga todo mês por 20 anos. O Educa+ paga a faculdade dos filhos por 5 anos. E aqui vem o detalhe que a prova adora: no Renda+ 2040, o ano 2040 não é o vencimento. É o começo dos pagamentos."

- **A promessa da aula**
  - "Nesta aula você vai entender como funciona a plataforma, quais produtos existem, por que o preço de um título sobe e desce, como o Renda+ e o Educa+ pagam e quanto custa guardar tudo isso. E vamos fazer as contas na HP12C."

**🔗 Ponte:** "Para começar, uma imagem: o governo tem duas lojas."

---

## 2. Metáfora central — 3 min

### Metáfora: o atacado e o varejo do governo

- **As duas lojas**
  - "O governo vende os seus títulos em duas lojas. A primeira é o atacado, o Sistema Selic. Lá só entram instituições financeiras autorizadas, em operações gigantes, com todos os títulos e com os nomes técnicos: LFT, LTN, NTN-B."

- **O varejo**
  - "A segunda é o varejo, o Tesouro Direto, a loja para pessoas físicas. Os produtos são os mesmos do atacado, mas com nomes amigáveis na prateleira: Tesouro Selic, Tesouro Prefixado, Tesouro IPCA+. Você entra pela porta de um banco ou corretora, o agente de custódia, e a loja garante que compra o produto de volta todos os dias."

- **As embalagens especiais**
  - "Nessa loja existem dois produtos com embalagem especial. O Renda+ é um cofre de aposentadoria que, a partir do ano escrito no nome, vira 20 anos de mesada. O Educa+ é um cofre da faculdade que vira 5 anos de mesada."

- **O aluguel do cofre**
  - "E a loja cobra um pequeno aluguel pelo cofre: a taxa de custódia."

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Atacado para instituições | Sistema Selic |
| Varejo para pessoas físicas | Tesouro Direto |
| Nomes técnicos × nomes amigáveis | LFT, LTN, NTN-B × Tesouro Selic, Prefixado, IPCA+ |
| Porta de entrada | Agente de custódia (banco ou corretora) |
| Loja compra de volta todo dia | Recompra diária pelo Tesouro, a preço de mercado |
| Cofre de aposentadoria com 20 anos de mesada | Tesouro Renda+ |
| Cofre da faculdade com 5 anos de mesada | Tesouro Educa+ |
| Aluguel do cofre | Taxa de custódia da B3 |

> **➕ Selic é o atacado; Tesouro Direto é o varejo para pessoa física. Mesmos títulos, nomes amigáveis, recompra garantida e aluguel do cofre.**

**🔗 Ponte:** "Vamos olhar as duas lojas lado a lado."

---

## 3. Explicação dos tópicos — 31 min

### 3.1 Sistema Selic × Tesouro Direto — 4 min · CPA 2.1.1.1.1.4

| Tópico | Sistema Selic | Tesouro Direto |
| --- | --- | --- |
| Função | Liquidação e custódia de títulos públicos em grandes operações | Programa de compra e venda de títulos públicos por pessoas físicas, pela internet |
| Público | Instituições financeiras autorizadas pelo BC | **Somente pessoas físicas** |
| Títulos | Todos os títulos do mercado interno | Seleção de títulos, com nomes simplificados |
| Volume | Operações de grande porte | Limite de **R$ 2 milhões por mês por CPF** |
| Acesso | Direto, pelas instituições | Por meio de **agente de custódia** (banco ou corretora) |

- **Sistema Selic**
  - "O Sistema Selic, Sistema Especial de Liquidação e de Custódia, é o grande cartório eletrônico dos títulos públicos, operado pelo Banco Central. Liquidar é a troca efetiva de título por dinheiro. Custodiar é guardar e registrar quem é o dono. Lá as instituições negociam bilhões por dia."
  - "Cuidado com o nome: o Sistema Selic dá nome à taxa Selic, porque a taxa básica é a média das operações compromissadas de um dia registradas nele. Mas sistema e taxa são coisas diferentes."

- **Tesouro Direto**
  - "O Tesouro Direto foi criado em 2002 pelo Tesouro Nacional, em parceria com a B3, para que a pessoa física compre título público pela internet. Só pessoa física. Empresa não entra. A empresa que quer título público compra pelo mercado institucional, por meio de um banco."

- **Agente de custódia**
  - "E a pessoa física não entra sozinha: precisa de um agente de custódia, que é o banco ou a corretora habilitada. Ele faz o cadastro, transmite as ordens e responde pelo cliente na B3."

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O Tesouro Direto é um investimento de renda fixa" | Errado | É um programa; o investimento é o título |
| "Empresas podem investir pelo Tesouro Direto" | Errado | Só pessoas físicas |
| "O investidor acessa o Tesouro Direto sem intermediário" | Errado | Precisa de um agente de custódia |
| "Sistema Selic e taxa Selic são a mesma coisa" | Errado | Sistema de liquidação × taxa básica de juros |

> **➕ Tesouro Direto: programa, só pessoa física, via banco ou corretora.**

**🔗 Ponte:** "Entrando na loja de varejo, quais são as regras da casa?"

---

### 3.2 Regras da plataforma — 5 min · CPA 2.1.1.1.1.4

| Regra | Conteúdo |
| --- | --- |
| Quem pode | Pessoas físicas com CPF, cadastradas em um agente de custódia |
| Onde negociar | Site/app do Tesouro Direto ou da instituição financeira |
| Valor mínimo | **Não há**, desde 18/11/2024: compra em múltiplos de 0,01 título |
| Limite máximo | **R$ 2 milhões por mês por CPF**, somando todos os títulos |
| Liquidez | **Recompra diária** garantida pelo Tesouro, **a preço de mercado** |
| Exceções à liquidez | Renda+ e Educa+: **carência de 60 dias** após a compra; o Tesouro pode suspender negociações em dias de volatilidade extrema |
| Horário | Negociação em dias úteis, das 9h30 às 18h |
| Tributação (resumo) | IR pela tabela regressiva da renda fixa (22,5% → 15%; 15% acima de 720 dias) e IOF para resgates em menos de 30 dias |

- **Sem mínimo, com teto**
  - "Desde novembro de 2024, não existe mais valor mínimo. Você compra frações de 0,01 título, então dá para começar com poucos reais. A apostila ainda fala em 30 reais, e isso está desatualizado. O teto é de 2 milhões de reais por mês por CPF, somando todos os títulos."

- **Recompra diária, a preço de mercado**
  - "A grande vantagem é a liquidez: o Tesouro compra o título de volta todo dia útil. Mas atenção às três palavras do final: a preço de mercado. Recompra garantida não é rentabilidade garantida. Se você vender antes do vencimento, recebe o preço do dia, que pode ser maior ou menor do que você pagou. Vamos ver isso em número no próximo tópico."

- **Carência**
  - "Renda+ e Educa+ têm uma exceção: carência de 60 dias depois da compra antes de poder vender. E, em dias de muita turbulência no mercado, o Tesouro pode suspender as negociações temporariamente."

- **Imposto**
  - "O imposto é o da renda fixa: tabela regressiva de 22,5% até 180 dias, 20% até 360, 17,5% até 720 e 15% acima disso. E IOF se você resgatar em menos de 30 dias."

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Recompra garantida assegura a rentabilidade contratada" | Errado | Recompra a preço de mercado; a taxa contratada só é garantida no vencimento |
| "É preciso investir no mínimo R$ 30" | Errado | Sem mínimo desde 18/11/2024 |
| "Todos os títulos têm carência de 60 dias" | Errado | Só Renda+ e Educa+ |
| "O limite mensal é de R$ 1 milhão" | Errado | R$ 2 milhões desde 18/11/2024 |

> **➕ Sem mínimo, até R$ 2 milhões por mês, recompra diária a preço de mercado, com carência de 60 dias só no Renda+ e no Educa+.**

**🔗 Ponte:** "Agora, as prateleiras: quais produtos estão à venda e por que o preço deles muda todo dia."

---

### 3.3 Produtos tradicionais — 9 min · CPA 2.1.1.1.2

| Produto (nome no varejo) | Título de mercado | Rentabilidade | Fluxo | Indicado para |
| --- | --- | --- | --- | --- |
| Tesouro Selic | LFT | Selic | Tudo no vencimento | Reserva de emergência, curto prazo |
| Tesouro Prefixado | LTN | Taxa fixa | Tudo no vencimento | Prazo definido; expectativa de queda dos juros |
| Tesouro Prefixado com Juros Semestrais | NTN-F | Taxa fixa + cupom de 10% a.a. | Cupons semestrais | Renda semestral com taxa fixa |
| Tesouro IPCA+ | NTN-B Principal | IPCA + taxa real | Tudo no vencimento | Longo prazo com proteção contra a inflação |
| Tesouro IPCA+ com Juros Semestrais | NTN-B | IPCA + taxa real + cupom de 6% a.a. | Cupons semestrais | Renda semestral protegida da inflação |

- **Os três sabores**
  - "São três sabores. Pós-fixado: o Tesouro Selic, que acompanha a taxa Selic. Prefixado: você sabe hoje exatamente quanto vai receber no vencimento. Híbrido: o IPCA+, que paga a inflação mais uma taxa real. Cada um tem a versão com juros semestrais, que paga cupons, ou seja, parte dos juros a cada seis meses, em vez de tudo no fim."

- **Marcação a mercado**
  - "Agora o ponto mais importante do tópico. O preço dos títulos muda todo dia conforme as taxas de juros do mercado. Isso é a marcação a mercado. A regra é uma gangorra: juros sobem, preço cai; juros caem, preço sobe. E quanto mais longo o título, mais forte a gangorra."

#### ➕ Exemplo prático 1 — a gangorra do prefixado (LTN, 3 anos, valor de face R$ 1.000)

| Taxa de mercado | Preço = 1.000 ÷ (1 + taxa)³ |
| --- | --- |
| 12% a.a. | R$ 711,78 |
| **13% a.a. (compra)** | **R$ 693,05** |
| 14% a.a. | R$ 674,97 (−2,61%) |

**Na HP12C**

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` | 🖥️ 0,00 | Limpa |
| 2 | ⌨️ `1000` `FV` | 🖥️ 1.000,00 | Valor de face no vencimento |
| 3 | ⌨️ `3` `n` · `13` `i` · `PV` | 🖥️ −693,05 | Preço de compra a 13% |
| 4 | ⌨️ `14` `i` · `PV` | 🖥️ −674,97 | Preço se o mercado for a 14% |
| 5 | ⌨️ `12` `i` · `PV` | 🖥️ −711,78 | Preço se o mercado for a 12% |
| 6 | ⌨️ `693,05` `ENTER` `674,97` `Δ%` | 🖥️ −2,61 | Perda de preço com +1 ponto |

- "Na HP: f REG, 1.000 em FV, porque é o que o título paga no vencimento. 3 em n, 13 em i, PV: 693,05, negativo porque é o que você paga. Agora o mercado sobe para 14%: digite 14, i, PV. O preço cai para 674,97. Se cair para 12%, sobe para 711,78. Para medir a perda: 693,05, ENTER, 674,97, delta porcento. Menos 2,61%."

#### ➕ Exemplo prático 2 — quem segura até o vencimento (LTN comprada a 13%)

| Item | Valor |
| --- | --- |
| Pago | R$ 693,05 |
| Recebe no vencimento | R$ 1.000,00 |
| Rendimento bruto | R$ 306,95 |
| IR (3 anos > 720 dias → 15%) | R$ 46,04 |
| Líquido | R$ 953,96 |
| Rentabilidade líquida | ≈ 11,24% a.a. (sem considerar a custódia) |

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `1000` `ENTER` `693,05` `-` | 🖥️ 306,95 | Rendimento bruto |
| 2 | ⌨️ `15` `%` | 🖥️ 46,04 | IR |
| 3 | ⌨️ `CHS` `1000` `+` | 🖥️ 953,96 | Valor líquido |
| 4 | ⌨️ `FV` · `693,05` `CHS` `PV` · `3` `n` · `i` | 🖥️ 11,24 | Taxa líquida ao ano |

- "E quem segura até o fim? Recebe os 1.000, não importa o que aconteceu com os juros no meio do caminho. Rendimento bruto de 306,95. Imposto de 15%, porque passou de 720 dias: 46,04. CHS, mais 1.000: líquido de 953,96. Guardo esse valor em FV, coloco 693,05 negativo em PV, 3 em n e peço i: 11,24% ao ano líquidos. A perda do exemplo anterior só existe para quem vende antes."
- 🔇 Simplificação: o cálculo ignora a custódia de 0,20% a.a. e considera os 3 anos como exatos.

#### Exemplo prático 3 — prazo longo, gangorra maior (NTN-B Principal, 10 anos, VNA hipotético de R$ 4.500)

| Taxa real de mercado | Cotação = 1 ÷ (1 + taxa)¹⁰ | Preço = VNA × cotação |
| --- | --- | --- |
| **7% a.a. (compra)** | 50,83% | **R$ 2.287,57** |
| 8% a.a. | 46,32% | R$ 2.084,37 (−8,88%) |

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` · `4500` `FV` | 🖥️ 4.500,00 | VNA (valor atualizado pelo IPCA) |
| 2 | ⌨️ `10` `n` · `7` `i` · `PV` | 🖥️ −2.287,57 | Preço a 7% de taxa real |
| 3 | ⌨️ `8` `i` · `PV` | 🖥️ −2.084,37 | Preço a 8% |
| 4 | ⌨️ `2287,57` `ENTER` `2084,37` `Δ%` | 🖥️ −8,88 | Perda com +1 ponto |

- "VNA é o Valor Nominal Atualizado: o valor do título corrigido pela inflação até hoje. Usei 4.500 como exemplo. Com 10 anos e taxa real de 7%, o preço é 2.287,57. Se a taxa sobe para 8%, cai para 2.084,37: menos 8,88%. Compare: no prefixado de 3 anos, o mesmo 1 ponto derrubou 2,6%; no IPCA+ de 10 anos, quase 9%. Prazo longo, gangorra maior."
- 🔇 VNA hipotético. A Aula A trata a mecânica completa da NTN-B.

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Juros de mercado sobem → preço do prefixado sobe" | Errado | Relação inversa |
| "Título público não tem risco de perda" | Errado | Pode perder na venda antecipada (risco de mercado) |
| "Tesouro Selic = LTN" | Errado | Tesouro Selic = LFT; Prefixado = LTN |
| "Quanto mais longo o título, menor a oscilação" | Errado | Prazo longo = mais volatilidade |

> **➕ Selic = LFT, Prefixado = LTN, IPCA+ = NTN-B Principal: o varejo só troca o nome. E juros sobem, preço cai.**

**🔗 Ponte:** "Agora os dois produtos com embalagem especial, os que viram mesada: Renda+ e Educa+."

---

### 3.4 Tesouro Renda+ e Tesouro Educa+ — 8 min · CPA 2.1.1.1.2

#### O que é

- **Títulos com finalidade**
  - "Renda+ e Educa+ são títulos híbridos: pagam IPCA mais uma taxa real. O que muda é o fluxo, que tem duas fases. Na acumulação, você compra e não recebe nada. Na conversão, o título passa a pagar parcelas mensais corrigidas pela inflação, ou seja, uma mesada que não perde poder de compra."

#### Como funciona

| | Tesouro Renda+ | Tesouro Educa+ |
| --- | --- | --- |
| Objetivo | Complementar a aposentadoria | Custear o ensino superior |
| Pagamentos | **240 parcelas mensais (20 anos)** | **60 parcelas mensais (5 anos)** |
| O ano no nome | **Início** dos pagamentos | **Início** dos pagamentos |
| Exemplo | Renda+ 2040: paga de 15/01/2040 a 15/12/2059 | Educa+ 2040: paga de 15/01/2040 a 15/12/2044 |
| Liquidez | Recompra, com carência de 60 dias após a compra | Idem |
| Volatilidade | Alta (prazo muito longo) | Alta (prazo longo) |
| Isenção de custódia | Mantido + renda de até **6 salários mínimos** | Mantido + renda de até **4 salários mínimos** |

- **O ano do nome**
  - "No Renda+ 2040, as parcelas começam em janeiro de 2040 e vão até dezembro de 2059: são 240 meses, 20 anos. No Educa+ 2040, começam em janeiro de 2040 e vão até dezembro de 2044: 60 meses, 5 anos. Na prova, sempre que aparecer o ano no nome, leia 'começa a pagar em'."

- **Como contar o fim**
  - "Macete para achar o último pagamento: no Renda+, some 19 ao ano do nome e pense em dezembro. 2040 mais 19 dá 2059. No Educa+, some 4: 2040 mais 4 dá 2044."

- **Como escolher o ano**
  - "Na hora de escolher, o ano deve coincidir com o começo do objetivo. Filha que entra na faculdade em 2041? Educa+ 2041. Aposentadoria em 2050? Renda+ 2050."

- **Volatilidade**
  - "Atenção: são títulos longuíssimos. Pelo que vimos na gangorra, vender antes do prazo pode dar perda grande se os juros subirem. Eles são feitos para ficar até o fim."

#### ➕ Exemplo prático 4 — quanto acumular para uma mesada de R$ 3.000 (raciocínio financeiro)

Objetivo: R$ 3.000 por mês, em reais de hoje, por 240 meses, com taxa real de 6% a.a.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` | 🖥️ 0,00 | Limpa |
| 2 | ⌨️ `1,06` `ENTER` `12` `1/x` `yˣ` | 🖥️ 1,00 | Fator mensal (1,06^(1/12) = 1,0048676; o visor arredonda) |
| 3 | ⌨️ `1` `-` `100` `×` `i` | 🖥️ 0,49 | Taxa real mensal ≈ 0,4868% (a HP guarda todas as casas) |
| 4 | ⌨️ `240` `n` · `3000` `CHS` `PMT` · `PV` | 🖥️ 424.152,93 | Valor necessário no início da renda |

- "Quanto alguém precisa ter acumulado, em valores de hoje, para receber 3 mil por mês durante 20 anos, com taxa real de 6% ao ano? Primeiro, transformo a taxa anual em mensal: 1,06, ENTER, 12, 1 sobre x, y elevado a x. Menos 1, vezes 100, e guardo em i: cerca de 0,49% ao mês. Depois 240 em n, 3 mil negativo em PMT e PV: 424.152,93. É esse o patrimônio, em reais de hoje, que sustenta a mesada."
- 🔇 Raciocínio de valor presente, não a fórmula oficial do título. O valor de cada parcela do Renda+ depende da quantidade de títulos e é informado pelo simulador do Tesouro Direto. O exemplo ignora IR e custódia.

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O Renda+ 2040 vence em 2040" | Errado | Começa a pagar em 2040 e termina em 2059 |
| "O Educa+ paga 20 anos de renda" | Errado | 5 anos (60 parcelas); 20 anos é o Renda+ |
| "Renda+ e Educa+ podem ser vendidos no dia seguinte à compra" | Errado | Carência de 60 dias |
| "O Renda+ paga o valor acumulado de uma vez" | Errado | 240 parcelas mensais |

> **➕ Renda+: 20 anos de mesada. Educa+: 5 anos. Os dois começam no ano do nome, não terminam nele.**

**🔗 Ponte:** "Por fim, o aluguel do cofre: a taxa de custódia."

---

### 3.5 Taxa de custódia — 5 min · CPA 2.1.1.1.1.4

#### Como funciona

- **O que é**
  - "A taxa de custódia é cobrada pela B3 para guardar os títulos e manter o registro de quem é dono. Ela é provisionada todo dia, como uma conta que vai acumulando, e cobrada de fato quando há venda, vencimento ou pagamento de cupom."

| Produto | Regra |
| --- | --- |
| Regra geral (Prefixado, IPCA+, com ou sem juros semestrais) | **0,20% ao ano** sobre o valor dos títulos |
| Tesouro Selic | **Isento até R$ 10.000** por CPF; 0,20% a.a. só sobre o excedente |
| Tesouro Renda+ | **0%** se mantido até a conversão e com renda de até **6 salários mínimos**; 0,10% a.a. sobre o excedente. **Venda antecipada:** 0,50% (até 10 anos), 0,20% (10 a 20 anos), 0,10% (acima de 20 anos), sobre o valor de resgate |
| Tesouro Educa+ | **0%** se mantido e com renda de até **4 salários mínimos**; 0,10% a.a. sobre o excedente. **Venda antecipada:** 0,50% (até 7 anos), 0,20% (7 a 14 anos), 0,10% (acima de 14 anos) |

- **Regra geral e Tesouro Selic**
  - "A regra geral é 0,20% ao ano sobre o valor dos títulos. O Tesouro Selic tem um benefício: os primeiros 10 mil reais são isentos, e a taxa incide só sobre o que passar disso."

- **Renda+ e Educa+**
  - "Renda+ e Educa+ têm regra própria, pensada para premiar quem fica até o fim. Quem mantém o título até a conversão e recebe renda de até 6 salários mínimos no Renda+, ou até 4 no Educa+, não paga custódia. Acima disso, 0,10% ao ano só sobre o excedente. Quem vende antes paga uma taxa sobre o valor do resgate, maior quanto mais cedo sair: 0,50%, 0,20% ou 0,10%. A apostila apresenta essa tabela como se fosse a custódia normal da acumulação, e está errado: ela vale só para a venda antecipada."

#### ➕ Exemplo prático 5 — custódia na HP12C

| Situação | Cálculo | Custódia |
| --- | --- | --- |
| Tesouro IPCA+ com saldo de R$ 14.944,10 | 14.944,10 × 0,20% | ≈ R$ 29,89 ao ano |
| Tesouro Selic com saldo de R$ 25.000 | (25.000 − 10.000) × 0,20% | R$ 30,00 ao ano |
| Tesouro Selic com saldo de R$ 8.000 | Abaixo da isenção | R$ 0,00 |
| Renda+ vendido antes de 10 anos, resgate de R$ 50.000 | 50.000 × 0,50% | R$ 250,00 (uma vez, na venda) |

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `14944,10` `ENTER` `0,2` `%` | 🖥️ 29,89 | Custódia anual do IPCA+ |
| 2 | ⌨️ `25000` `ENTER` `10000` `-` `0,2` `%` | 🖥️ 30,00 | Custódia do Selic: só o excedente |
| 3 | ⌨️ `50000` `ENTER` `0,5` `%` | 🖥️ 250,00 | Taxa da venda antecipada do Renda+ |

- "Três contas rápidas. IPCA+ de 14.944,10: ENTER, 0,2, porcentagem, 29,89 por ano. Tesouro Selic de 25 mil: tiro os 10 mil isentos e calculo 0,2% sobre 15 mil, 30 reais. Renda+ vendido antes de 10 anos com resgate de 50 mil: 0,5%, 250 reais, de uma vez."

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A isenção de custódia até R$ 10 mil vale para todos os títulos" | Errado | Só para o Tesouro Selic |
| "Renda+ paga 0,20% a.a. na acumulação" | Errado | 0% se mantido; taxa só na venda antecipada ou na renda acima do limite |
| "O limite de isenção do Educa+ é de 6 salários mínimos" | Errado | 4 (Educa+) × 6 (Renda+) |
| "A custódia é cobrada só no vencimento" | Errado | Provisionada diariamente; cobrada em vendas, vencimentos e cupons |

> **➕ 0,20% ao ano é a regra. O Selic é isento até R$ 10 mil. Renda+ e Educa+ só cobram se você sair antes ou se a renda passar de 6 ou 4 salários mínimos.**

#### Nota de atualização — Tesouro Reserva (fora do PD vigente)

- "Uma novidade que não está no Programa Detalhado: em maio de 2026, o Tesouro lançou o Tesouro Reserva. É um título atrelado à Selic, sem marcação a mercado, negociável 24 horas por dia, 7 dias por semana, com liquidação via Pix e aplicação a partir de 1 real. Na estreia, foi oferecido aos correntistas do Banco do Brasil. Por enquanto, ele não entra na prova."

**🔗 Ponte:** "Fechamos o conteúdo. Vamos ver como a prova cobra."

---

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

- **Regras e leitura do nome**
  - "A CPA cobra o Tesouro Direto de dois jeitos. Regras objetivas: quem pode, limites, liquidez, custódia. E leitura do nome do Renda+ e do Educa+: o ano e o número de parcelas. Às vezes aparece a lógica da marcação a mercado: juros sobem, preço cai."

### Pontos de atenção

1. **Tesouro Direto:** programa, só pessoa física, via agente de custódia.
2. **Limites:** sem valor mínimo; limite de R$ 2 milhões por mês por CPF.
3. **Liquidez:** recompra diária a preço de mercado; carência de 60 dias em Renda+ e Educa+.
4. **Renda+ e Educa+:** 240 meses no Renda+ e 60 no Educa+; o ano do nome é o início da renda.
5. **Custódia:** 0,20% a.a.; Selic isento até R$ 10 mil; Renda+ e Educa+ com tabelas próprias.
6. **Marcação a mercado:** juros sobem → preço cai; prazo longo → oscilação maior.

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Sistema Selic | Tesouro Direto | Atacado (instituições) × varejo (pessoas físicas) |
| Renda+ | Educa+ | 20 × 5 anos de renda; 6 × 4 salários mínimos |
| Ano do nome | Último pagamento | Início da renda × dezembro de (ano + 19) ou (ano + 4) |
| Recompra garantida | Rentabilidade garantida | Liquidez a preço de mercado × taxa só no vencimento |
| Custódia regra geral | Custódia do Tesouro Selic | 0,20% sobre tudo × isenção até R$ 10 mil |

### Palavras-chave da prova

| Expressão no enunciado | Resposta |
| --- | --- |
| "Programa", "pessoas físicas" | Tesouro Direto |
| "Instituições financeiras", "liquidação" | Sistema Selic |
| "20 anos de pagamentos mensais" | Renda+ |
| "5 anos de pagamentos", "ensino superior" | Educa+ |
| "Agente de custódia" | Banco ou corretora |
| "Venda antes do vencimento" | Preço de mercado (pode haver perda) |

### Pegadinhas (todas erradas)

- "O Tesouro Direto é um tipo de investimento de renda fixa."
- "Empresas podem investir pelo Tesouro Direto."
- "O Renda+ 2040 vence em 2040."
- "A isenção de custódia até R$ 10 mil vale para todos os títulos."
- "É preciso investir no mínimo R$ 30."
- "A recompra diária garante a taxa contratada na venda antecipada."
  - "Leia cada uma, diga 'errado' e explique por quê."

> **➕ Programa para pessoa física, sem mínimo, até R$ 2 milhões por mês, recompra diária. E, no Renda+ e no Educa+, o ano do nome é o começo da mesada.**

**🔗 Ponte:** "Vamos montar a carteira de uma família."

---

## 5. ➕ Case — 4 min

### Situação

- "Paulo tem 40 anos. Ele e a esposa querem três coisas. Primeiro, guardar 15 mil reais de reserva. Segundo, pagar a faculdade da filha de 3 anos, que deve começar em 2041. Terceiro, garantir uma renda complementar a partir de 2050, quando Paulo terá 64 anos. E a empresa do Paulo também quer aplicar o caixa em títulos públicos pelo Tesouro Direto. O que você recomendaria para cada objetivo?"

### Conceitos aplicados

| Objetivo | Produto | Regra aplicada |
| --- | --- | --- |
| Reserva de R$ 15 mil | **Tesouro Selic** | Baixa oscilação; custódia só sobre R$ 5 mil: 5.000 × 0,20% = **R$ 10/ano** |
| Faculdade a partir de 2041 | **Tesouro Educa+ 2041** | 60 parcelas de jan/2041 a dez/2045; custódia 0% se mantido e renda até 4 SM |
| Renda a partir de 2050 | **Tesouro Renda+ 2050** | 240 parcelas de jan/2050 a dez/2069; custódia 0% se mantido e renda até 6 SM |
| Empresa quer usar o Tesouro Direto | **Não pode** | Só pessoas físicas; a empresa investe pelo mercado institucional |

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `15000` `ENTER` `10000` `-` | 🖥️ 5.000,00 | Parte da reserva que paga custódia |
| 2 | ⌨️ `0,2` `%` | 🖥️ 10,00 | Custódia anual da reserva |

### Análise passo a passo

- **1. Reserva**
  - "Para a reserva, Tesouro Selic, porque oscila pouco. A custódia incide só sobre os 5 mil acima da isenção: 10 reais por ano."
- **2. Faculdade**
  - "Para a faculdade em 2041, Educa+ 2041: o ano do nome é o começo. Ele paga de janeiro de 2041 a dezembro de 2045."
- **3. Aposentadoria**
  - "Para a renda a partir de 2050, Renda+ 2050, que paga de janeiro de 2050 a dezembro de 2069. Comprar um Renda+ 2030 seria começar 20 anos cedo demais."
- **4. Empresa**
  - "A empresa fica fora. O Tesouro Direto é só para pessoa física."

### Síntese do case

- "O ano do Renda+ e do Educa+ deve coincidir com o começo do objetivo, não com o fim."

> **Escolha o Renda+ e o Educa+ pelo ano em que o dinheiro precisa começar a entrar.**

**🔗 Ponte:** "Agora, as questões no estilo da prova."

---

## 6. ➕ Questões comentadas — 5 min

### Questão 1 — Médio

**CPA · 2.1.1.1.2 Tesouro Renda+ · Médio**

Um investidor pessoa física adquiriu Tesouro Renda+ 2050 pelo Tesouro Direto. Sobre esse título, é correto afirmar que:

A) o título vence em 2050, quando o investidor recebe o valor acumulado em um único pagamento.
B) os pagamentos mensais começam em 2050 e se estendem por 20 anos, e não há taxa de custódia se o título for mantido e a renda mensal não ultrapassar 6 salários mínimos.
C) incide taxa de custódia de 0,20% ao ano durante toda a fase de acumulação, como nos demais títulos.
D) o título pode ser adquirido tanto por pessoas físicas quanto por pessoas jurídicas, desde que por meio de um agente de custódia.

**Gabarito: B**

- **B (correta):** o ano do nome marca o início das 240 parcelas mensais; custódia zero se mantido e com renda de até 6 SM.
- **A:** 2050 é o início da renda, e o pagamento é mensal, não único.
- **C:** o Renda+ tem tabela própria, sem 0,20% a.a. na acumulação.
- **D:** o Tesouro Direto é exclusivo para pessoas físicas.
  - "Resposta B. Ano do nome é começo; Renda+ são 20 anos; isenção até 6 salários mínimos."

### ➕ Questão 2 — Difícil

**CPA · 2.1.1.1.2 Tesouro Prefixado · Difícil**

Um investidor comprou um Tesouro Prefixado (LTN) com 3 anos até o vencimento, valor de face de R$ 1.000,00, à taxa de 13% a.a. No mesmo dia, as taxas de mercado para esse título subiram para 14% a.a. Considerando capitalização anual, é correto afirmar que:

A) o preço do título sobe para cerca de R$ 711,78, beneficiando o investidor.
B) o preço do título cai para cerca de R$ 674,97; o investidor terá perda apenas se vender antes do vencimento.
C) o investidor deixará de receber R$ 1.000,00 no vencimento, pois a taxa de mercado mudou.
D) a recompra diária garantida pelo Tesouro assegura que a venda antecipada seja feita pela taxa de 13%.

**Gabarito: B**

| Passo | Teclas | Visor |
| --- | --- | --- |
| 1 | ⌨️ `f` `REG` · `1000` `FV` · `3` `n` · `14` `i` · `PV` | 🖥️ −674,97 |

- **B (correta):** com taxa de 14%, 1.000 ÷ 1,14³ = R$ 674,97. A perda só se realiza na venda antecipada; no vencimento, o investidor recebe R$ 1.000 e a taxa contratada.
- **A:** R$ 711,78 é o preço a 12%. Com a alta dos juros, o preço cai.
- **C:** o valor de face no vencimento não muda.
- **D:** a recompra é feita a preço de mercado, não pela taxa da compra.
  - "Resposta B. Juros sobem, preço cai, e quem segura até o vencimento recebe o combinado."

### ➕ Questão 3 — Fácil

**CPA · 2.1.1.1.1.4 Plataforma do Tesouro Direto · Fácil**

Sobre o Tesouro Direto, é correto afirmar que:

A) é um título público de renda fixa negociado pela internet.
B) é um programa de venda de títulos públicos a pessoas físicas, acessado por meio de um agente de custódia.
C) exige investimento mínimo de R$ 30,00 por operação.
D) permite que pessoas jurídicas invistam até R$ 2 milhões por mês.

**Gabarito: B**

- **B (correta):** é um programa, exclusivo para pessoas físicas, acessado via banco ou corretora.
- **A:** não é título; é a plataforma.
- **C:** sem valor mínimo desde 18/11/2024.
- **D:** pessoa jurídica não participa; o limite de R$ 2 milhões é por CPF.
  - "Resposta B. Programa, pessoa física, agente de custódia."

**🔗 Ponte:** "Para fechar, a revisão."

---

## 7. ➕ Revisão final — 3 min

### Resumo em cinco pontos

1. O **Sistema Selic** é o atacado das instituições. O **Tesouro Direto** é o programa de varejo, exclusivo para pessoas físicas, via agente de custódia.
2. Desde 18/11/2024: **sem valor mínimo** e **limite de R$ 2 milhões por mês por CPF**. Recompra diária **a preço de mercado**.
3. **Produtos:** Tesouro Selic (LFT), Prefixado (LTN), IPCA+ (NTN-B Principal) e as versões com juros semestrais (NTN-F e NTN-B). Juros sobem, preço cai; prazo longo, oscilação maior.
4. **Renda+** (20 anos de renda) e **Educa+** (5 anos): o ano no nome é o início dos pagamentos; carência de 60 dias.
5. **Custódia:** 0,20% a.a.; Selic isento até R$ 10 mil; Renda+ e Educa+ com custódia zero se mantidos e com renda até 6 e 4 salários mínimos.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Tesouro Direto | Programa · só PF · via agente de custódia |
| Limites | Sem mínimo · R$ 2 mi/mês por CPF |
| Liquidez | Recompra diária a mercado · Renda+/Educa+ com 60 dias de carência |
| Marcação a mercado | Juros ↑ → preço ↓ · prazo longo → oscila mais |
| Renda+ | 240 meses · ano = início · fim em dez/(ano + 19) · 6 SM |
| Educa+ | 60 meses · ano = início · fim em dez/(ano + 4) · 4 SM |
| Custódia | 0,20% a.a. · Selic isento até R$ 10 mil · venda antecipada de Renda+/Educa+: 0,50 / 0,20 / 0,10% |
| HP12C | Preço: `FV`, `n`, `i`, `PV` · variação: `Δ%` · custódia: `%` |

### Cadeia lógica

**Objetivo do investidor → produto do Tesouro Direto (nome amigável) → título de mercado equivalente → regras da plataforma (limites, recompra, carência) → custo de custódia → resultado líquido**

### Diferenças que não podem ser confundidas

- **Programa ≠ investimento · Sistema Selic ≠ Tesouro Direto · ano do nome ≠ vencimento · recompra garantida ≠ rentabilidade garantida · Renda+ (6 SM, 20 anos) ≠ Educa+ (4 SM, 5 anos).**

### Frase central da aula

> **O Tesouro Direto é o varejo do governo: mesmos títulos com nomes amigáveis, para pessoa física, com recompra diária. E tem dois cofres especiais que viram mesada a partir do ano escrito no nome.**

### Próximo passo de estudo

- "Refaça na HP os exemplos da gangorra e da custódia. Treine a leitura do nome: Renda+ 2045 paga até quando? Educa+ 2038 paga até quando? Na próxima aula: títulos bancários, CPA 2.1.1.1.3."
- 🔇 Respostas: Renda+ 2045 → dez/2064; Educa+ 2038 → dez/2042.

---

## Nota de verificação

- **Valores perdidos no Google Docs:** recuperados da aula do repositório. O trecho da correção 3 tinha virado equação.
- **Contas conferidas por script e pela sequência da HP12C:**
  - LTN: 711,78; 693,05; 674,97; −2,61%; líquido de 953,96; 11,24% a.a.;
  - NTN-B Principal: 2.287,57; 2.084,37; −8,88%;
  - valor necessário para a mesada: 424.152,93;
  - custódia: 29,89; 30,00; 250,00; 10,00.
- **Normas e regras de mercado:** vêm da aula do repositório, conferida em 24/09/2026, e não foram reabertas nesta sessão. São elas: limites e fim do mínimo (18/11/2024), tabelas de custódia da B3, carência de 60 dias, horário e Tesouro Reserva.
  - A página consultada da B3 não exibia a tabela completa de venda antecipada do Renda+/Educa+. Os percentuais foram confirmados nos slides e em fontes de mercado.
- **Acréscimos (➕):**
  - kit HP12C;
  - exemplos 1, 2, 4 e 5 com teclas;
  - Sistema Selic × taxa Selic;
  - tabela do IR regressivo da renda fixa;
  - macete do último pagamento (ano + 19 / ano + 4);
  - questões 2 e 3;
  - custódia da reserva no case.
- **Simplificações declaradas:**
  - o exemplo 2 ignora a custódia;
  - o exemplo 4 é raciocínio de valor presente, não a fórmula oficial do Renda+;
  - o VNA do exemplo 3 é hipotético.
