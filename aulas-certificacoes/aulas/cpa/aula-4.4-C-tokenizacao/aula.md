# Aula CPA — Tokenização: Conceito, Tipos de Tokens, Benefícios, Riscos e Aplicações

Sep 29, 2026 · @Boss · Roteiro integrado · 40 min

## Identificação e alinhamento

Aula C de 3 do item **4.4 Finanças Descentralizadas (DEFI)** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), **Módulo 4 — Inovação e desenvolvimento de mercado**. Cobre **4.4.4 a 4.4.4.5**. Base: **Roteiro de Aula — Tokenização** (fonte principal, condensado), **APOSTILA-CPA p. 542–545**, **Parecer de Orientação CVM 40/2022**, **Lei 14.478/2022** e **Decreto 11.563/2023**, conferidos nesta sessão.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 4.4.4 / 4.4.4.1 Conceito básico | Roteiro p. 6–11 · APOSTILA-CPA p. 542 | Conferido |
| 4.4.4.2 Tipos de tokens | APOSTILA-CPA p. 543 · Roteiro p. 11–16 · **Parecer CVM 40** | **Lista da apostila encaixada na taxonomia da CVM** |
| 4.4.4.3 Benefícios | APOSTILA-CPA p. 544–545 · Roteiro p. 16–22 | **Apostila como resposta de prova + ressalva** |
| 4.4.4.4 Riscos e desafios | APOSTILA-CPA p. 544 · Roteiro p. 22–31 | Conferido; competência BC × CVM pelo **Decreto 11.563/2023** |
| 4.4.4.5 Ativos financeiros, imóveis e artes | Roteiro p. 31–38 · APOSTILA-CPA p. 542–545 | Conferido; Código Civil art. 1.245 |

**Cobertura PD × material:** todos os subitens têm material. Esta aula **substitui** o rascunho anterior de tokenização (que estava na antiga 4.4-B).

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 3 min |
| 2. Metáfora central | 3 min |
| 3. Tópicos (Conceito 4 · Tipos de tokens 6 · Benefícios 4 · Riscos e competências 4 · Financeiros, imóveis e arte 4) | 22 min |
| 4. Por que cai na prova | 4 min |
| 5. Case | 3 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **40 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | APOSTILA-CPA p. 544 | Benefícios: "liquidez e liquidação instantânea", registros "públicos e imutáveis, aumentando a segurança", eliminação de "cartórios e bancos" | **Resposta de prova (apostila):** fracionamento, acesso, liquidez 24/7, transparência, menor custo. **Ressalva (roteiro):** são **potenciais**: fracionar não cria compradores; registro não prova autenticidade; token de imóvel não substitui o registro em cartório | Código Civil, art. 1.245 |
| 2 | APOSTILA-CPA p. 543 | Lista de 7 tipos de token, sem agrupamento | Os 7 tipos **encaixam** nos 3 grupos funcionais da CVM (pagamento, utilidade, referenciado a ativo), que **não são exclusivos** | Parecer CVM 40/2022 |
| 3 | APOSTILA-CPA p. 543 | Exemplos com nomes e códigos de criptoativos reais | Trocados por exemplos genéricos | — |
| 4 | Roteiro p. 34 | Exemplos de infraestrutura de uma bolsa real | Tratado como "infraestrutura de mercado regulada" | — |
| 5 | Roteiro p. 49–50 | Questão com 5 alternativas | Nova questão com **4 alternativas (A–D)** | — |

## 1. Fala de abertura — 3 min

> Um imóvel de R$ 1 milhão dividido em 10 mil tokens de R$ 100. Você compra dez.
>
> Pergunta: você virou **dono de um pedaço do apartamento**?
>
> Depende. O token pode dar **parte do aluguel**, um **crédito**, uma **cota** — ou só uma promessa. A escritura continua no cartório.
>
> Hoje: o que é **tokenização**, os **tipos de token**, o que ela **promete** e o que ela **não resolve**.

### Objetivo da abertura

Mostrar a regra central: **o token representa; o contrato e a lei definem o direito**.

### Conexão com o Programa Detalhado

CPA 4.4.4 a 4.4.4.5.

## 2. Metáfora central — 3 min

### Metáfora: a etiqueta digital com manual de direitos

> Pense numa **etiqueta digital** colada numa **caixa**.
>
> - A **caixa** é o **ativo** (debênture, imóvel, obra de arte).
> - A **etiqueta** é o **token**: registra quem tem, quanto tem e as transferências.
> - O **livro de etiquetas** é a **blockchain**.
> - O **manual de direitos** é o **contrato e a lei**: diz o que quem tem a etiqueta realmente recebe.
>
> A etiqueta **não cria o conteúdo da caixa**. Para saber o que você comprou, é preciso ler o manual.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Caixa | Ativo ou direito subjacente |
| Etiqueta | Token |
| Livro de etiquetas | DLT / blockchain |
| Manual de direitos | Contrato, regulamento e lei |
| Fiscal | Regulador (CVM, BCB, conforme o caso) |
| Cadeado | Custódia e chave privada |

### Frase de fixação

> **O token é a etiqueta; o direito está no manual.**

## 3. Explicação dos tópicos — 22 min

### 3.1 Conceito básico — 4 min

#### O que é

**Tokenização** é o processo de transformar um **ativo do mundo real, ou um direito sobre ele**, em um **token digital** que pode ser **registrado, negociado e transferido** em blockchain (APOSTILA-CPA p. 542).

#### Como funciona

| Estrutura | O que é |
| --- | --- |
| **Ativo preexistente tokenizado** | O ativo continua existindo fora da rede (debênture, recebível, imóvel); o token o **representa** |
| **Token nativo** | Nasce **direto no ambiente digital** (unidade de protocolo, token de acesso, colecionável digital) |

| Termo | O que é |
| --- | --- |
| **DLT** | Tecnologia de **registro distribuído** (categoria ampla) |
| **Blockchain** | **Uma forma** de DLT (blocos encadeados) |
| **Tokenização** | O **processo** de representação digital |
| **Token** | A **unidade digital** criada e transferida |

**Fluxo:** identificar o ativo → definir os direitos → estruturar o emissor → criar o token → registrar em DLT → ofertar → custodiar e transferir → monitorar riscos.

#### O que a prova pode confundir

- **Tokenização ≠ criar criptomoeda.**
- **DLT ≠ blockchain ≠ token.**
- A tokenização muda a **forma de registro e transferência**, não o risco do ativo (uma debênture tokenizada tem o mesmo devedor).

#### Frase de fixação

> **Tokenizar é criar a representação digital, não apagar a realidade do ativo.**

#### Alinhamento ao PD

CPA 4.4.4 e 4.4.4.1.

---

### 3.2 Tipos de tokens — 6 min

#### Como funciona

**Taxonomia funcional da CVM (Parecer de Orientação 40/2022):**

| Grupo da CVM | Função | Tipos da apostila que se encaixam |
| --- | --- | --- |
| **Token de pagamento** | Replicar funções de **moeda**: unidade de conta, meio de troca, reserva de valor | **Payment token** (criptomoedas) |
| **Token de utilidade** | **Adquirir ou acessar** produtos e serviços | **Utility token** (ex.: token de torcedor com descontos) |
| **Token referenciado a ativo** | Representar um ou mais **ativos tangíveis ou intangíveis** | **Security token**, **stablecoin**, **NFT**, **RWA** (ativo real) |

**Fungível × não fungível (atravessa os grupos):**

| Tipo | Característica |
| --- | --- |
| **Fungível** | Unidades **intercambiáveis**, uma igual à outra |
| **Não fungível (NFT)** | **Único**, com identificador exclusivo |

**Os 7 tipos da apostila, em uma linha cada:**

| Tipo | O que é |
| --- | --- |
| Fungível | Intercambiável |
| NFT | Único e insubstituível |
| Pagamento | Meio de pagamento |
| Stablecoin | Busca **valor estável**, em geral atrelado a moeda |
| Security token | Representa **valor mobiliário** (ação, dívida, cota) |
| RWA | Representa **ativo real** (imóvel, terreno, metal) |
| Utilidade | Dá **acesso** a produto ou serviço |

**Regras da CVM (Parecer 40):**

- As categorias **não são exclusivas nem estanques**: um token pode ter mais de uma função.
- O token referenciado a ativo **pode ou não** ser valor mobiliário: depende da **essência econômica** dos direitos e da função no projeto — não do nome.

#### O que a prova pode confundir

- **"Utility" no nome não afasta a CVM** se o token der expectativa de retorno com oferta pública.
- **Nem todo token é valor mobiliário, e nem todo token digital está fora da CVM.**

#### Frase de fixação

> **Pagamento paga, utilidade dá acesso, referenciado representa um ativo — e um token pode ser mais de um.**

#### Alinhamento ao PD

CPA 4.4.4.2.

---

### 3.3 Benefícios da tokenização — 4 min

#### Como funciona

| Benefício (resposta de prova) | Limite (ressalva) |
| --- | --- |
| **Fracionamento**: ativo caro dividido em partes pequenas → **democratiza o acesso** | Fracionar não cria compradores |
| **Liquidez 24/7** e liquidação rápida | Liquidez depende de mercado secundário e demanda |
| **Transparência**: registro de propriedade rastreável | Rastrear a transação não prova a autenticidade do ativo |
| **Menos custos** com intermediários | Segurança, custódia e conformidade continuam custando |
| **Programabilidade**: regras em smart contract (pagamentos e rendimentos automáticos) | Código executa regra errada com perfeição |
| **Pagamento e entrega na mesma operação** (liquidação atômica) | Não elimina risco de crédito do ativo |
| **Registro compartilhado**: menos conciliação entre instituições | Dado errado na entrada continua errado |

**Para a prova (apostila p. 545):** a principal vantagem é **democratizar o acesso** a ativos antes ilíquidos, por meio do **fracionamento**.

#### Frase de fixação

> **Tokenizar fraciona e facilita; benefício é potencial, não garantia.**

#### Alinhamento ao PD

CPA 4.4.4.3.

---

### 3.4 Riscos e desafios: segurança, regulação e tecnologia — 4 min

#### Como funciona

| Dimensão | Riscos |
| --- | --- |
| **Segurança** | Roubo ou **perda da chave privada**; código vulnerável; ataque a oráculo ou a pontes entre redes; golpes (phishing); falha do custodiante. Erro em smart contract pode ser **permanente** |
| **Regulação** | Incerteza jurídica; uso para **lavagem de dinheiro**; definir **quem regula** |
| **Tecnologia** | **Escalabilidade** (volume da rede); **taxas variáveis (gas)**; **consumo de energia**; interoperabilidade entre sistemas |
| **Dados** | Registro imutável × **LGPD** (finalidade, necessidade, segurança, correção de dados) |
| **Econômico** | O ativo mantém seus riscos (inadimplência, vacância, autenticidade da obra) e pode faltar liquidez |

**Quem regula (competências):**

| Situação | Regulador |
| --- | --- |
| **Prestadoras de serviços de ativos virtuais** (troca, custódia, transferência) | **Banco Central** — Decreto 11.563/2023 (regula, autoriza e supervisiona) |
| Token que é **valor mobiliário** ou oferta pública de investimento | **CVM** — Lei 14.478/2022, art. 3º, IV, e Decreto 11.563/2023, art. 3º (competência da CVM preservada) |

> **Nota de atualização:** o BCB regulamentou as prestadoras de serviços de ativos virtuais (Res. BCB 519–521/2025, em vigor desde 02/02/2026). A **Res. CMN 5.274/2025** reforçou a segurança cibernética das instituições autorizadas (ex.: teste de invasão ao menos anual). O BCB também estudou benefícios e desafios da tokenização (Voto BCB 31/2023 e piloto do Drex).

#### Frase de fixação

> **Banco Central cuida de quem presta serviço com ativo virtual; CVM cuida do que é valor mobiliário.**

#### Alinhamento ao PD

CPA 4.4.4.4.

---

### 3.5 Tokenização de ativos financeiros, imóveis e artes — 4 min

#### Como funciona

| Ativo | O token pode representar | O que **não** se presume |
| --- | --- | --- |
| **Financeiro** (debênture, recebível, cota) | A dívida, o fluxo de recebíveis, a participação | Que o risco de crédito sumiu ou que a CVM não se aplica |
| **Imóvel** | Participação econômica, fluxo de aluguel, recebível, cota | Que transfere a **propriedade**: isso só com **registro no Registro de Imóveis** (Código Civil, art. 1.245) |
| **Arte** | Obra digital (NFT), certificado de procedência, licença, fração econômica | **Autenticidade** da obra física, **posse** ou **direitos autorais** (regidos pela Lei 9.610/1998) |

**Exemplo — debênture tokenizada:** mudam o **registro e a transferência**; ficam iguais o **devedor**, a remuneração, o vencimento, as garantias e o **risco de crédito**.

#### O que a prova pode confundir

- **Debênture tokenizada continua sendo valor mobiliário.**
- **Token de imóvel ≠ matrícula; NFT ≠ direito autoral.**

#### Frase de fixação

> **O ativo mantém sua natureza; a tokenização muda a representação.**

#### Alinhamento ao PD

CPA 4.4.4.5.

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

A CPA cobra **o conceito**, **os tipos**, a **principal vantagem** (fracionamento) e os **riscos**; nas questões mais difíceis, **quem regula**.

### Pontos de atenção

1. **Tokenização = ativo real ou direito → token digital em blockchain.**
2. **CVM: pagamento, utilidade e referenciado a ativo — não exclusivos.**
3. **Security token, stablecoin, NFT e RWA = referenciados a ativo.**
4. **Principal vantagem: fracionamento (democratiza o acesso).**
5. **Riscos: segurança, regulação e tecnologia.**
6. **BCB: prestadoras de ativos virtuais; CVM: valores mobiliários.**

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Token fungível | NFT | Intercambiável × único |
| Token de utilidade | Security token | Acesso a serviço × valor mobiliário |
| Ativo preexistente | Token nativo | Representa algo fora da rede × nasce digital |
| DLT | Blockchain | Categoria × uma forma dela |
| BCB | CVM | Prestadoras de ativos virtuais × valores mobiliários |

### Palavras-chave da prova

- **"Fracionamento", "democratizar"**: benefício da tokenização.
- **"Unidade de conta, meio de troca, reserva de valor"**: token de pagamento.
- **"Acesso a produtos ou serviços"**: token de utilidade.
- **"Representa ativos tangíveis ou intangíveis"**: token referenciado a ativo.

### Pegadinhas

- "Todo token referenciado a ativo é valor mobiliário." **Errado:** pode ou não ser.
- "Fracionar garante liquidez." **Errado.**
- "O Banco Central regula todos os tokens." **Errado:** valores mobiliários ficam com a CVM.

### Frase de fixação

> **Olhe a função e os direitos do token, não o nome.**

## 5. Case — 3 min

### Situação

> Uma plataforma lança três tokens: (1) um token que representa uma debênture de uma empresa; (2) um token que dá desconto no uso do aplicativo da própria plataforma; (3) um token que dá direito a parte dos aluguéis de um prédio, vendido ao público com promessa de retorno. A propaganda diz: "compre e seja dono do prédio".

### Conceitos aplicados

| Token | Classificação | Ponto de atenção |
| --- | --- | --- |
| 1. Debênture | Referenciado a ativo (**security token**) | Continua **valor mobiliário**; mesmo risco de crédito da emissora |
| 2. Desconto no app | **Utilidade** | Se não houver promessa de retorno, tende a ficar fora da CVM |
| 3. Aluguéis do prédio | Referenciado a ativo | Oferta pública com expectativa de retorno → possível **valor mobiliário** (CVM) |
| "Seja dono do prédio" | Propaganda enganosa | Propriedade só com **registro no Registro de Imóveis** |

### Síntese do case

Três tokens, três funções e três tratamentos diferentes, e nenhum transfere o prédio.

### Frase de fixação

> **Mesmo na mesma plataforma, cada token é classificado pelos direitos que entrega.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 4.4.4.2 Tipos de tokens · **Nível:** Médio

### Questão

De acordo com a taxonomia funcional adotada pela CVM para criptoativos, é correto afirmar que:

A) as categorias token de pagamento, token de utilidade e token referenciado a ativo são mutuamente exclusivas, de modo que cada token se enquadra em apenas uma delas.

B) stablecoins, NFTs e security tokens são exemplos de tokens referenciados a ativo, que podem ou não ser valores mobiliários, conforme a essência econômica dos direitos conferidos.

C) todo token de utilidade está automaticamente fora da competência da CVM, independentemente dos direitos que confere.

D) todo token registrado em blockchain é considerado valor mobiliário.

### Ponto-chave do enunciado

"**Taxonomia funcional**" da CVM.

### Gabarito

**Alternativa B.**

### Comentário da alternativa correta

O Parecer CVM 40/2022 cita **security tokens, stablecoins e NFTs** como exemplos de **token referenciado a ativo**, que **pode ou não** ser valor mobiliário, conforme a **essência econômica** dos direitos.

### Por que as demais estão incorretas?

- **A:** as categorias **não são exclusivas nem estanques**; um token pode ter várias funções.
- **C:** o **nome** não decide; se houver expectativa de retorno com oferta pública, a CVM pode atuar.
- **D:** o registro em blockchain **não define** a natureza jurídica do token.

### Armadilhas e macetes

- **Função e direitos decidem; tecnologia e nome não.**

### Referência

Parecer de Orientação CVM 40/2022; APOSTILA-CPA p. 543; Programa Detalhado CPA, item 4.4.4.2.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. Tokenização: ativo ou direito vira token digital em blockchain; pode ser ativo preexistente ou token nativo; DLT ≠ blockchain ≠ token.
2. CVM: pagamento, utilidade e referenciado a ativo (não exclusivos); os 7 tipos da apostila se encaixam nesses grupos; fungível × NFT.
3. Benefícios: fracionamento (democratiza o acesso), liquidez 24/7, transparência, menos custos, programabilidade — todos potenciais.
4. Riscos: segurança (chave, código), regulação (lavagem, quem regula), tecnologia (escala, gas, energia); BCB regula prestadoras de ativos virtuais; CVM, valores mobiliários.
5. Financeiro, imóvel e arte: o ativo mantém sua natureza e seus riscos; imóvel exige registro; NFT não é direito autoral.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Tokenização | Ativo ou direito → token digital |
| Token de pagamento | Unidade de conta · meio de troca · reserva de valor |
| Token de utilidade | Acesso a produto ou serviço |
| Referenciado a ativo | Security, stablecoin, NFT, RWA · pode ou não ser valor mobiliário |
| Fungível × NFT | Intercambiável × único |
| Benefício-chave | Fracionamento |
| Riscos | Segurança · regulação · tecnologia |
| BCB × CVM | Prestadoras de ativos virtuais × valores mobiliários |
| Imóvel tokenizado | Propriedade só com registro (CC 1.245) |

### Cadeia lógica

> Ativo ou direito → token → registro em DLT → função e direitos → regulador → benefícios potenciais e riscos

### Diferenças que não podem ser confundidas

- **Token ≠ ativo ≠ propriedade.**
- **Fracionamento ≠ liquidez.**
- **BCB ≠ CVM.**

### Frase central da aula

> **O token é a etiqueta; o contrato e a lei são o manual — e o ativo continua com seus riscos.**

### Próximo passo de estudo

Item 4.4.5 — Novas estruturas de mercado (NFT, stablecoins, renda fixa digital, ETFs de cripto e Drex).

## Referências oficiais e status

Último acesso: 2026-09-29.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — itens 4.4.4 a 4.4.4.5 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. CVM — Parecer de Orientação 40, de 11/10/2022 — criptoativos: taxonomia funcional (pagamento, utilidade, referenciado a ativo; categorias não exclusivas) — [cvm.gov.br](https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/pareceres-orientacao/anexos/Pare040.pdf). **Em vigor.** Conferido nesta sessão.
3. Presidência da República — Lei 14.478/2022 — ativos virtuais (art. 3º, IV) — [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14478.htm). **Em vigor.** Conferido nesta sessão.
4. Presidência da República — Decreto 11.563/2023 — competência do Banco Central sobre prestadoras de serviços de ativos virtuais; preserva a CVM (art. 3º) — [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/d11563.htm). **Em vigor.** Conferido nesta sessão.
5. Presidência da República — Código Civil — art. 1.245 — [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm). **Em vigor.** Conferido nesta sessão.
6. CMN — Resolução 5.274/2025 — segurança cibernética (altera a Res. CMN 4.893/2021) — [Grant Thornton](https://www.grantthornton.com.br/insights/artigos-e-publicacoes/seguranca-cibernetica-o-que-muda-com-a-cmn-5.2742025/). **Em vigor** (texto **não reaberto nesta sessão**).
7. BCB — Resoluções 519, 520 e 521/2025 (prestadoras de serviços de ativos virtuais). **Em vigor desde 02/02/2026** (texto **não reaberto nesta sessão**).
8. BCB — Voto BCB 31/2023 e Relatório do Piloto Drex; CVM — página "Criptoativos: quando se aplicam as regras da CVM?"; Lei 9.610/1998 (direitos autorais): citados no roteiro, **não reabertos nesta sessão**.

Fontes de origem (não oficiais): Roteiro de Aula — Tokenização (`00-fontes/materiais-aula/topico-4.4-defi-blockchain-smart-contracts/`); APOSTILA-CPA p. 542–545.
