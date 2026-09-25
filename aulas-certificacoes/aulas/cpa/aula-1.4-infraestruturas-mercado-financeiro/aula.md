# Aula CPA — Infraestruturas do Mercado Financeiro

Sep 25, 2026 · @Boss · Roteiro integrado · 40 min

## Identificação e alinhamento

Aula única de 40 minutos que cobre o item **1.4 Regulação e infraestrutura de mercado** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), Módulo 1, com os subitens **1.4.1 a 1.4.1.5**. Aprofunda o que a aula-referência (itens 1.1.4 e 1.1.5, seção "SPB") apresentou em 5 minutos. As definições de SPB, STR, SPI e Selic são as mesmas; o foco novo é contraparte central, depositário central e entidade registradora.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 1.4.1 IMFs e função de gatekeepers | PDF A3490 p. 3–4 · APOSTILA-CPA p. 158–161 | Conferido, com correção |
| 1.4.1.1 Sistemas de pagamentos | PDF A3490 p. 5 · APOSTILA-CPA p. 159, 162 | Conferido |
| 1.4.1.1.1 SPB | PDF A3490 p. 6, 8 · APOSTILA-CPA p. 162 | Conferido, com correções |
| 1.4.1.1.2 SPI | PDF A3490 p. 7–8 · APOSTILA-CPA p. 162–163 | Conferido |
| 1.4.1.2 Sistema de liquidação de títulos | PDF A3490 p. 9 · APOSTILA-CPA p. 159–160, 176–177 | Conferido |
| 1.4.1.2.1 Selic | PDF A3490 p. 10 · APOSTILA-CPA p. 160, 177 | Conferido, **completado** (Selic como depositário central) |
| 1.4.1.3 Contrapartes centrais | PDF A3490 p. 11 · APOSTILA-CPA p. 160, 175 | Conferido, com correção |
| 1.4.1.4 Depositários centrais | PDF A3490 p. 12 · APOSTILA-CPA p. 160, 175–176 | Conferido |
| 1.4.1.5 Entidade registradora | PDF A3490 p. 13 · APOSTILA-CPA p. 160, 176 | Conferido, com correção |

**Cobertura PD × PDFs:** todos os subitens têm material. As correções foram feitas direto no texto, como você decidiu.

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 3 min |
| 2. Metáfora central | 3 min |
| 3. Tópicos (IMFs e gatekeepers 4 · SPB e SPI 5 · Liquidação e Selic 4 · Contraparte central 4 · Depositário e registradora 5) | 22 min |
| 4. Por que cai na prova | 4 min |
| 5. Case | 3 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **40 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | PDF A3490 p. 4 | Gatekeepers: "B3, Selic, CETIP, **CVM e BCB**" | CVM e BCB são **supervisores**. Gatekeepers são as **IMFs**, as **autorreguladoras**, as **instituições financeiras** e os **profissionais do mercado** | APOSTILA-CPA p. 161 |
| 2 | PDF A3490 p. 4, 13 | "CETIP" como entidade própria; "CIP" | A Cetip foi **incorporada pela B3** em 2017 (hoje segmento de balcão da B3). A CIP passou a se chamar **Núclea** | B3; Núclea |
| 3 | PDF A3490 p. 13 · APOSTILA-CPA p. 160 | Registradoras: "B3, CETIP, CIP, TAG, BLK" | "BLK/PLK" **não confirmado** → retirado. Registradoras de recebíveis homologadas na convenção com o BCB (11/2024): **B3, CERC, Núclea, TAG, CRDC, Grafeno e Quicksoft** | BCB — convenção entre registradoras |
| 4 | PDF A3490 p. 8 | Exemplos do SPB: "TED, **DOC**, boletos" | O **DOC foi extinto** em 2024 | Febraban (ver aula-referência) |
| 5 | APOSTILA-CPA p. 175 | Selic listado como clearing/contraparte central | O Selic **não é contraparte central**: liquida em **LBTR** com **entrega contra pagamento**, sem se interpor entre as partes. É o **depositário central** dos títulos públicos federais | BCB — Selic |
| 6 | PDF A3490 p. 6 | SPB "criado em 2002" | Marco legal: **Lei 10.214/2001**. Em **2002** o SPB foi **reestruturado**, com o STR e a LBTR | Lei 10.214/2001; BCB |
| 7 | PDF A3490 p. 9, 11 | "Câmara de Ações" e "Câmara de Derivativos" da B3 | As câmaras foram integradas na **Câmara B3** | BCB — participantes do Selic (Câmara B3) |

## 1. Fala de abertura — 3 min

> Você manda um Pix e o dinheiro chega em segundos. Você compra uma ação e, dois dias úteis depois, ela aparece na sua conta. Você aplica num CDB e o banco nem entrega papel nenhum.
>
> Onde está a ação? Quem garante que o vendedor entrega? Quem prova que o CDB é seu?
>
> Por trás de cada operação existe uma **infraestrutura** que ninguém vê: sistemas que **transferem**, **liquidam**, **garantem**, **guardam** e **registram**.
>
> Nesta aula você vai aprender o **nome e a função** de cada uma, e por que elas protegem o mercado contra o **efeito dominó**.

### Objetivo da abertura

Mostrar que cada etapa de uma operação depende de uma infraestrutura e apresentar as cinco funções.

### Conexão com o Programa Detalhado

CPA 1.4.1 a 1.4.1.5.

## 2. Metáfora central — 3 min

### Metáfora: o aeroporto do dinheiro

> O mercado financeiro funciona como um **aeroporto**.
>
> As **pistas** por onde o dinheiro decola e pousa são os **sistemas de pagamento**: o **STR** é a pista principal entre os bancos; o **SPI** é a pista expressa do **Pix**, aberta 24 horas.
>
> O **portão de embarque**, onde a mala só entra se o bilhete estiver pago, é o **sistema de liquidação**: entrega do título **contra** pagamento. O **Selic** é o portão exclusivo dos **títulos públicos**.
>
> A **companhia aérea que garante o voo**, mesmo se um passageiro faltar, é a **contraparte central**: ela vira o outro lado de todo mundo.
>
> O **cofre de bagagens** é o **depositário central**: guarda os ativos e sabe de quem é cada mala. O **cartório de bordo**, que anota cada passagem vendida, é a **entidade registradora**.
>
> A **ANAC** que fiscaliza tudo são o **BCB** e a **CVM**. E toda a equipe atenta a irregularidades (companhias, agentes, tripulação) são os **gatekeepers**.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Pistas | Sistemas de pagamento (SPB: STR, SPI) |
| Portão que só libera com bilhete pago | Sistema de liquidação (entrega contra pagamento) |
| Portão dos títulos públicos | Selic |
| Companhia que garante o voo | Contraparte central (Câmara B3) |
| Cofre de bagagens | Depositário central (B3; Selic para títulos públicos) |
| Cartório de bordo | Entidade registradora |
| ANAC | Supervisores: BCB e CVM |
| Equipe atenta | Gatekeepers |

### Frase de fixação

> **Pagamento transfere, liquidação troca, contraparte garante, depositário guarda, registradora anota.**

## 3. Explicação dos tópicos — 22 min

### 3.1 IMFs e a função de gatekeepers — 4 min

#### O que é

**Infraestruturas do Mercado Financeiro (IMFs)** são os sistemas e entidades que **transferem recursos**, **compensam e liquidam** operações, **guardam** ativos e **registram** operações, com segurança e eficiência. Seu papel central é reduzir o **risco de contraparte** (a outra parte não cumprir) e o **risco sistêmico** (a falha de um elo derrubar todos).

#### Como funciona

| Tipo de IMF | Função | Exemplos |
| --- | --- | --- |
| Sistema de pagamentos | Transferir recursos | STR, SPI |
| Sistema de liquidação | Trocar ativo por dinheiro | Selic, Câmara B3 |
| Contraparte central | Garantir a liquidação | Câmara B3 |
| Depositário central | Guardar ativos e controlar a titularidade | B3; Selic (títulos públicos) |
| Entidade registradora | Registrar operações e ativos | B3, CERC, Núclea |

**Supervisão:** **BCB** (sistemas de pagamento, liquidação e ativos financeiros) e **CVM** (valores mobiliários).

**Gatekeepers ("guardiões do portão"):** todos os participantes que **verificam a regularidade**, **previnem fraudes e riscos sistêmicos** e **dão transparência** às operações:

| Quem | Exemplos |
| --- | --- |
| IMFs | B3, Selic |
| Autorreguladoras | ANBIMA, Ancord, Apimec, BSM |
| Instituições financeiras | Bancos, corretoras |
| Profissionais | Assessores de investimento, analistas |

#### O que a prova pode confundir

- **Gatekeeper ≠ supervisor**: BCB e CVM supervisionam; os gatekeepers atuam na linha de frente.

#### Frase de fixação

> **IMF é o encanamento; gatekeeper é quem vigia o portão; BCB e CVM são os fiscais.**

#### Alinhamento ao PD

CPA 1.4.1.

---

### 3.2 Sistemas de pagamentos: SPB e SPI — 5 min

#### Como funciona

**SPB (Sistema de Pagamentos Brasileiro):** conjunto de **entidades, sistemas e procedimentos** de transferência de fundos e de outros ativos financeiros e de compensação e liquidação de pagamentos (Lei 10.214/2001). Reestruturado em **2002**, com a **Liquidação Bruta em Tempo Real (LBTR)**: cada operação é liquidada **uma a uma**, em tempo real, de forma **irrevogável**.

| Sistema | Quem opera | O que faz |
| --- | --- | --- |
| **STR** | BCB | Transfere **reservas** entre instituições, em LBTR (TED entre bancos) |
| **SPI** | BCB | Liquida o **Pix**, em LBTR, **24/7** |
| **Selic** | BCB | Títulos públicos federais (ver 3.3) |
| **Câmara B3** | B3 | Ações, derivativos, câmbio, renda fixa privada |
| **Núclea** (antiga CIP) | Privada | Sistemas de TED e boletos entre bancos |

**SPB × SPI:**

| Critério | SPB | SPI |
| --- | --- | --- |
| Abrangência | Conjunto **amplo** de sistemas | **Um** sistema dentro do SPB |
| Liquidação | Em tempo real (STR) ou diferida, conforme o sistema | **Sempre em tempo real** |
| Horário | Varia por sistema | **24 horas, 7 dias** |
| Exemplos | TED, boletos, cartões | **Pix** |
| Supervisão | BCB | BCB (também operador) |

#### O que a prova pode confundir

- **SPI é parte do SPB**, não um sistema paralelo.
- **O BCB opera três IMFs: STR, Selic e SPI.**

#### Frase de fixação

> **SPB é a rede; STR é a pista dos bancos; SPI é a pista do Pix, aberta 24/7.**

#### Alinhamento ao PD

CPA 1.4.1.1, 1.4.1.1.1 e 1.4.1.1.2.

---

### 3.3 Sistema de liquidação de títulos e o Selic — 4 min

#### Como funciona

**Liquidação** é a etapa **depois da negociação**: o **ativo vai para o comprador** e o **dinheiro vai para o vendedor**. O padrão seguro é a **entrega contra pagamento** (DVP): um só acontece se o outro acontecer.

**Selic — Sistema Especial de Liquidação e de Custódia:**

| Ponto | Regra |
| --- | --- |
| Operador | **Banco Central** |
| Criação | 1979 |
| Ativos | **Títulos públicos federais** |
| Funções | **Registro**, **custódia** (depositário central) e **liquidação** dessas operações |
| Forma de liquidação | **LBTR**, com **entrega contra pagamento** |
| Taxa Selic | Média das operações compromissadas de um dia lastreadas em títulos públicos **registradas no sistema** |

#### O que a prova pode confundir

- **Sistema Selic ≠ taxa Selic.**
- **Títulos públicos → Selic; títulos privados e ações → B3.**
- **Selic não é contraparte central.**

#### Frase de fixação

> **Selic é o portão exclusivo dos títulos públicos: guarda, registra e liquida, um a um, com entrega contra pagamento.**

#### Alinhamento ao PD

CPA 1.4.1.2 e 1.4.1.2.1.

---

### 3.4 Contraparte central (CCP) — 4 min

#### O que é

A contraparte central **se interpõe** entre comprador e vendedor: passa a ser **compradora de todo vendedor** e **vendedora de todo comprador**. Se uma parte falhar, a CCP **garante** a liquidação.

#### Como funciona

| Mecanismo | Função |
| --- | --- |
| **Interposição** | O risco deixa de ser "um contra o outro" e passa a ser "cada um contra a CCP" |
| **Garantias (margem)** | Exige depósitos, sobretudo em derivativos, para cobrir possíveis inadimplências |
| **Compensação multilateral** | Calcula o **saldo líquido** de cada participante, reduzindo os valores a liquidar |
| **Resultado** | Menos **risco de contraparte** e menos **contágio** |

**Exemplo:** a **Câmara B3** (ações, com liquidação em D+2, derivativos e câmbio). Regulação: **BCB** e **CVM**.

#### O que a prova pode confundir

- **Contraparte central garante; depositário guarda; registradora anota.**

#### Frase de fixação

> **A contraparte central vira o outro lado de todo mundo — e cobra garantia para isso.**

#### Alinhamento ao PD

CPA 1.4.1.3.

---

### 3.5 Depositários centrais e entidades registradoras — 5 min

#### Como funciona

| Critério | Depositário central | Entidade registradora |
| --- | --- | --- |
| O que faz | **Guarda** (custódia centralizada) os ativos e controla a **titularidade**; efetiva a **transferência** de propriedade | **Registra** ativos e operações, criando o **histórico** (como um cartório) |
| Para quê | Saber **quem é o dono** e evitar que o ativo seja usado duas vezes | **Transparência**, **rastreabilidade** e evitar **dupla negociação ou dupla garantia** |
| Exemplos | **B3** (ações e renda fixa privada); **Selic** (títulos públicos federais) | **B3** (balcão: CDB, LCI, derivativos de balcão), **CERC**, **Núclea**, **TAG** (recebíveis, duplicatas) |
| Autorização | BCB e/ou CVM, conforme o ativo | **BCB** (ativos financeiros) e **CVM** (valores mobiliários) |

**Quando você compra uma ação**, ela **não fica na corretora**: fica no **depositário central da B3**, em seu nome.

#### O que a prova pode confundir

- **Registro ≠ custódia**: registrar é anotar a operação; depositar é guardar o ativo e controlar o dono.
- A **B3** acumula várias funções: bolsa, contraparte central, depositário e registradora.

#### Frase de fixação

> **O depositário é o cofre com o nome do dono; a registradora é o cartório com o histórico.**

#### Alinhamento ao PD

CPA 1.4.1.4 e 1.4.1.5.

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

A CPA cobra este item por **associação**: dada uma função ("garante a liquidação", "guarda os ativos", "registra CDB", "liquida o Pix"), qual é a infraestrutura? Também cobra **quem opera** cada sistema (BCB × B3) e a diferença entre **supervisor e gatekeeper**.

### Pontos de atenção

1. **IMFs:** pagamento, liquidação, contraparte central, depositário, registradora.
2. **BCB opera STR, Selic e SPI**; BCB e CVM supervisionam.
3. **LBTR:** uma a uma, em tempo real, irrevogável.
4. **Selic:** títulos públicos federais; registro, custódia e liquidação; não é CCP.
5. **CCP:** interpõe-se, exige garantias, compensa multilateralmente.
6. **Depositário:** guarda e titularidade. **Registradora:** registro e histórico.

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| SPB | SPI | Conjunto amplo × sistema do Pix, 24/7 |
| Selic | Câmara B3 | Títulos públicos, sem CCP × privados e ações, com CCP |
| Contraparte central | Depositário central | Garante × guarda |
| Depositário central | Registradora | Custódia e titularidade × registro e histórico |
| Supervisor | Gatekeeper | BCB/CVM × IMFs, autorreguladoras, IFs, profissionais |

### Palavras-chave da prova

- **"Compradora de todo vendedor"**: contraparte central.
- **"Titularidade" / "custódia"**: depositário central.
- **"Registro" / "rastreabilidade"**: entidade registradora.
- **"24/7" / "Pix"**: SPI.
- **"Títulos públicos federais"**: Selic.

### Pegadinhas

- "O SPI é independente do SPB." **Errado.**
- "O Selic atua como contraparte central." **Errado.**
- "A ação comprada fica guardada na corretora." **Errado.**
- "CVM e BCB são os gatekeepers do mercado." **Errado:** são supervisores.

### Frase de fixação

> **Para cada verbo, uma infraestrutura: transferir, liquidar, garantir, guardar, registrar.**

## 5. Case — 3 min

### Situação

> Em uma mesma manhã, Júlia:
>
> 1. Faz um Pix de R$ 500 no domingo.
> 2. Compra 100 ações na B3.
> 3. Aplica em um CDB do banco.
> 4. Compra Tesouro Selic.
>
> O vendedor das ações quebra antes da liquidação. Júlia quer saber quem garante cada coisa.

### Conceitos aplicados

| Operação | Infraestrutura | Função |
| --- | --- | --- |
| Pix no domingo | **SPI** | Liquidação em tempo real, 24/7 |
| Ações | **Câmara B3** (contraparte central) + **depositário da B3** | A CCP garante a entrega mesmo com o vendedor quebrado; as ações ficam no depositário em nome de Júlia |
| CDB | **Registradora** (balcão B3) | Registra o CDB em nome de Júlia |
| Tesouro Selic | **Selic** | Custódia e liquidação de títulos públicos |

### Análise passo a passo

1. **Identificar o verbo:** transferir, garantir, guardar, registrar, liquidar.
2. **Associar à infraestrutura.**
3. **Quebra do vendedor:** a CCP honra a operação.

### Síntese do case

Júlia recebe as ações porque a **Câmara B3** garante a liquidação.

### Frase de fixação

> **Quem garante a compra na bolsa é a contraparte central, não o vendedor.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 1.4.1.3 a 1.4.1.5 Contraparte central, depositário e registradora · **Nível:** Médio

### Questão

A infraestrutura do mercado financeiro que se interpõe entre comprador e vendedor, torna-se compradora de todo vendedor e vendedora de todo comprador e exige garantias para assegurar a liquidação das operações é denominada:

A) depositário central.

B) entidade registradora.

C) contraparte central.

D) Sistema de Pagamentos Instantâneos (SPI).

### Ponto-chave do enunciado

"**Interpõe-se**", "**compradora de todo vendedor**" e "**exige garantias**".

### Gabarito

**Alternativa C.**

### Comentário da alternativa correta

A **contraparte central** assume o risco de cada lado da operação e exige **garantias** para cobrir eventuais inadimplências. No Brasil, a principal é a **Câmara B3**.

### Por que as demais estão incorretas?

- **A:** o depositário central **guarda** os ativos e controla a titularidade; não se interpõe nas operações.
- **B:** a entidade registradora **registra** ativos e operações, dando transparência; não garante liquidação.
- **D:** o SPI **liquida o Pix** em tempo real; é sistema de pagamentos, não contraparte.

### Armadilhas e macetes

- **Garante = contraparte central. Guarda = depositário. Anota = registradora.**

### Referência

Lei 10.214/2001; Lei 12.810/2013; APOSTILA-CPA p. 158–163 e 174–177; Programa Detalhado CPA, item 1.4.1.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. IMFs transferem, liquidam, garantem, guardam e registram; reduzem risco de contraparte e sistêmico. Supervisão: BCB e CVM. Gatekeepers: IMFs, autorreguladoras, IFs e profissionais.
2. SPB: conjunto de sistemas (Lei 10.214/2001), reestruturado em 2002 com LBTR. STR (reservas), SPI (Pix, 24/7), Selic, Câmara B3, Núclea.
3. Selic: operado pelo BCB; títulos públicos federais; registro, custódia e liquidação em LBTR com entrega contra pagamento; não é CCP.
4. Contraparte central: interpõe-se, exige garantias, compensa; exemplo: Câmara B3.
5. Depositário central guarda e controla a titularidade (B3; Selic). Registradora registra e dá histórico (B3, CERC, Núclea, TAG).

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| IMF | Transfere · liquida · garante · guarda · registra |
| Gatekeepers | IMFs, autorreguladoras, IFs, profissionais (não BCB/CVM) |
| SPB | Conjunto de sistemas · LBTR desde 2002 · Lei 10.214/2001 |
| SPI | Pix · BCB · tempo real · 24/7 |
| Selic | BCB · títulos públicos · LBTR com DVP · não é CCP |
| Contraparte central | Interpõe-se · garantias · Câmara B3 |
| Depositário central | Custódia e titularidade · B3 / Selic |
| Registradora | Registro e histórico · B3, CERC, Núclea, TAG |

### Cadeia lógica

> negociação → contraparte central garante → sistema de liquidação troca ativo por dinheiro → depositário atualiza o dono → registradora mantém o histórico → BCB e CVM supervisionam

### Diferenças que não podem ser confundidas

- **SPB ≠ SPI.**
- **Sistema Selic ≠ taxa Selic.**
- **Contraparte central ≠ depositário ≠ registradora.**
- **Supervisor ≠ gatekeeper.**

### Frase central da aula

> **No aeroporto do dinheiro, cada infraestrutura tem um verbo — e o avião só decola quando todos funcionam.**

### Próximo passo de estudo

Resolver 10 questões de associação "função → infraestrutura" e revisar a seção SPB da aula-referência (1.1.4–1.1.5).

## Referências oficiais e status

Último acesso: 2026-09-25.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — item 1.4 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. Presidência da República — Lei 10.214/2001 — Sistema de Pagamentos Brasileiro — [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/leis/leis_2001/l10214.htm). **Em vigor.** **Texto não reaberto nesta sessão.**
3. Presidência da República — Lei 12.810/2013 — depósito centralizado e registro de ativos financeiros e valores mobiliários. **Em vigor.** **Texto não reaberto nesta sessão.**
4. BCB — Selic: princípios para IMFs e informações de governança (operador: BCB; participantes: Câmara B3, CIP/Núclea) — [DFAM Selic](https://www.bcb.gov.br/content/estabilidadefinanceira/selic/DFAM_Selic.pdf) · [ANBIMA](https://www.anbima.com.br/pt_br/noticias/banco-central-divulga-informacoes-sobre-governanca-e-estrutura-de-operacoes-do-selic.htm). **Em vigor.**
5. BCB — SPI: divulgação de princípios para IMFs — [PDF BCB](https://www.bcb.gov.br/content/estabilidadefinanceira/sistemapagamentosinstantaneos_docs/principios_infraestruturas_mercado_financeiro.pdf). **Em vigor.**
6. BCB — Convenção entre entidades registradoras (recebíveis de arranjos de pagamento) — [PDF BCB](https://www.bcb.gov.br/content/estabilidadefinanceira/spb_docs/convencoes/Conven%C3%A7%C3%A3o%20entre%20Entidades%20Registradoras%20-%20Receb%C3%ADveis%20de%20Arranjos%20de%20Pagamento.pdf). **Em vigor.** Lista das sete registradoras conferida por fonte secundária ([antecipafacil](https://antecipafacil.com.br/registradoras-de-duplicata-escritural)).
7. Conjur — Infraestruturas de mercado e o Banco Central (2025) — [conjur.com.br](https://conjur.com.br/2025-ago-27/infraestruturas-de-mercado-e-o-banco-central-arquitetura-da-confianca/). **Fonte secundária.**
8. Incorporação da Cetip pela B3 (2017) e mudança de nome da CIP para Núclea: **não reconferidos nesta sessão**.

Fontes de origem (não oficiais): PDF A3490 "Regulação e Infraestrutura do Mercado" (`00-fontes/materiais-aula/topico-1.4-infraestrutura-mercado/`); APOSTILA-CPA, p. 158–163 e 174–177; aula-referência `modelos/REFERENCIA-aula-cpa-1.1.4-1.1.5-autorreguladores-fgc-spb.md`, seção 3.4.
