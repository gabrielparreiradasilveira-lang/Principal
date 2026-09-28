# Aula CPA — Meios de Pagamento: Conceitos, Arranjo, Adquirente e Subadquirente

Sep 28, 2026 · @Boss · Roteiro integrado · 40 min

## Identificação e alinhamento

Aula B de 2 do item **4.7 Fintechs e meios de pagamento** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), **Módulo 4 — Inovação e desenvolvimento de mercado**. Cobre **4.7.6** (meios de pagamento), **4.7.6.1** (conceitos), **4.7.6.2** (arranjo), **4.7.6.3** (adquirente) e **4.7.6.4** (sub-adquirente, grafado "Sub-adquitente" no PD). Base: **Roteiro de Aula 4.7** (fonte principal, condensado), PDF **A5708**, **APOSTILA-CPA p. 553–555**, **Lei 12.865/2013**, **Res. BCB 80** e **Res. BCB 150**, conferidas nesta sessão.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 4.7.6 / 4.7.6.1 Meios de pagamento e conceitos | Roteiro p. 26–34 · PDF A5708 p. 5 · APOSTILA-CPA p. 553–554 | Conferido pela **Lei 12.865, art. 6º**; DOC **corrigido** |
| 4.7.6.2 Arranjo | Roteiro p. 34–37 · PDF A5708 p. 6 | Conferido pela Lei 12.865 e Res. BCB 150 |
| 4.7.6.3 Adquirente | Roteiro p. 37–40 · PDF A5708 p. 7 · APOSTILA-CPA p. 554 | **Corrigido** ("adquirente autoriza") pela **Res. BCB 80, art. 3º, III** |
| 4.7.6.4 Subadquirente | Roteiro p. 40–43 · PDF A5708 p. 8 | Conferido pela **Res. BCB 150** (subcredenciador); **Res. BCB 522/2025** como nota |

**Cobertura PD × PDFs:** todos os subitens têm material.

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 3 min |
| 2. Metáfora central | 3 min |
| 3. Tópicos (Meios de pagamento e conceitos 6 · Fluxo do cartão e do Pix 4 · Arranjo 4 · Adquirente 4 · Subadquirente 4) | 22 min |
| 4. Por que cai na prova | 4 min |
| 5. Case | 3 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **40 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | PDF A5708 p. 5 · APOSTILA-CPA p. 554 | Meios de pagamento incluem "TED/**DOC**" | **O DOC foi extinto**: último envio em 15/01/2024 e encerramento dos sistemas em 29/02/2024 | Febraban |
| 2 | PDF A5708 p. 7 · APOSTILA-CPA p. 554 | Adquirente "captura, **autoriza** e liquida" | Quem **autoriza** é o **emissor** (lado do pagador). O credenciador/adquirente **habilita o recebedor**, captura e encaminha a transação e **participa da liquidação como credor perante o emissor** | Res. BCB 80, art. 3º, III |
| 3 | PDF A5708 p. 9 | Cartão: "Cliente → Bandeira → Emissor → Adquirente → Subadquirente → Lojista" | Ordem trocada. Autorização: lojista (subadquirente) → **adquirente** → rede do **arranjo/bandeira** → **emissor** autoriza ou recusa. A liquidação faz o **caminho de volta** até o lojista | Roteiro p. 31–32; Res. BCB 150 |
| 4 | PDF A5708 p. 9 · APOSTILA-CPA p. 554 | Pix: "Cliente → Instituição de Pagamento → Lojista" | Pagador → **instituição do pagador** (banco **ou** IP) → **infraestrutura do Pix** (liquidação no **SPI**, do BCB) → **instituição do recebedor** → recebedor | BCB — Pix |
| 5 | Roteiro p. 1 · PD | Grafia "Sub-adquitente" | **Subadquirente** (mercado) = **subcredenciador** (termo da norma) | Res. BCB 150 |
| 6 | APOSTILA-CPA p. 554 · PDF A5708 | Empresas e marcas reais como exemplo de adquirente, subadquirente e carteira digital | Trocadas por exemplos genéricos | — |
| 7 | — | Material não trata da **Res. BCB 522/2025** | Subcredenciadores passam a participar **obrigatoriamente da liquidação centralizada** nos arranjos sujeitos a ela; instituidor monitora os participantes. Entra como **nota** | Res. BCB 522/2025 |

## 1. Fala de abertura — 3 min

> Você aproxima o cartão na maquininha e, em dois segundos, aparece "aprovado".
>
> Nesses dois segundos passaram pelo menos quatro empresas: quem habilitou a loja, a rede da bandeira, o banco que emitiu o cartão e, às vezes, uma plataforma no meio.
>
> Quem **aprovou**? Quem **cobra** do banco? Quem **paga** a loja?
>
> Hoje: **instrumento, conta, arranjo, adquirente e subadquirente**, e por que o Pix tem menos gente no caminho.

### Objetivo da abertura

Mostrar que um pagamento é uma **cadeia** de funções, e que cada função tem um nome e uma regra.

### Conexão com o Programa Detalhado

CPA 4.7.6 a 4.7.6.4.

## 2. Metáfora central — 3 min

### Metáfora: a rede de estradas com pedágio

> Um pagamento é uma **viagem de dinheiro** do pagador até o recebedor.
>
> - O **arranjo** é o **código de trânsito** da rede: define quem pode entrar, como se anda e como se acerta o pedágio.
> - O **instituidor** é o **dono da rodovia**, que escreve esse código (e empresta a marca, a bandeira).
> - O **instrumento** é o **veículo**: cartão, QR Code, celular.
> - O **emissor** entrega o veículo ao **pagador** e decide se ele pode rodar (**autoriza**).
> - O **adquirente** é o **posto de entrada da loja**: habilita o lojista e **cobra o emissor** no acerto final.
> - O **subadquirente** é o **despachante** que coloca lojistas pequenos na rodovia por meio do posto de entrada, mas **não cobra o emissor**.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Código de trânsito | Arranjo de pagamento |
| Dono da rodovia | Instituidor do arranjo |
| Veículo | Instrumento de pagamento |
| Quem entrega o veículo e autoriza | Emissor |
| Posto de entrada da loja | Credenciador / adquirente |
| Despachante | Subcredenciador / subadquirente |

### Frase de fixação

> **O arranjo dá as regras, o emissor autoriza, o adquirente habilita a loja e cobra o emissor.**

## 3. Explicação dos tópicos — 22 min

### 3.1 Meios de pagamento e conceitos — 6 min

#### O que é

**Meio de pagamento** é a solução completa que permite transferir valor entre **pagador** e **recebedor**: instrumento, contas, participantes, regras (arranjo) e infraestrutura de liquidação.

#### Como funciona

**Conceitos da Lei 12.865/2013 (art. 6º):**

| Conceito | Definição legal (resumo) |
| --- | --- |
| **Arranjo de pagamento** | Conjunto de **regras e procedimentos** de um serviço de pagamento ao público, **aceito por mais de um recebedor**, com acesso direto pelos usuários finais |
| **Instituidor do arranjo** | Pessoa jurídica **responsável pelo arranjo** e, quando for o caso, pela **marca** associada |
| **Instituição de pagamento** | Pessoa jurídica que, **aderindo a arranjo**, gere conta de pagamento, emite instrumento, credencia a aceitação, executa remessas etc. |
| **Conta de pagamento** | Conta de **registro** em nome do usuário final, usada para transações de pagamento |
| **Instrumento de pagamento** | **Dispositivo ou procedimentos** combinados com o prestador para **iniciar** uma transação |
| **Moeda eletrônica** | Recursos **armazenados** em dispositivo ou sistema eletrônico para pagar |

**Principais meios no Brasil:** **Pix** · **cartões de crédito, débito e pré-pago** · **boleto** · **TED** · **carteiras digitais** (que em geral usam um cartão ou uma conta por trás).

**Usuário final × participante:** pagador e lojista são **usuários finais**; emissor, adquirente, subadquirente e instituição domicílio são **participantes** do arranjo.

#### O que a prova pode confundir

- **Instrumento ≠ conta**: o cartão inicia; a conta registra.
- **Meio de pagamento ≠ arranjo**: o arranjo é só a camada de regras.
- **DOC não existe mais** (extinto em 2024).

#### Frase de fixação

> **Instrumento inicia, conta registra, arranjo organiza, participantes executam.**

#### Alinhamento ao PD

CPA 4.7.6 e 4.7.6.1.

---

### 3.2 O caminho do cartão e do Pix — 4 min

#### Como funciona

**Cartão (duas fases):**

| Fase | Caminho | Quem decide |
| --- | --- | --- |
| **Autorização** | Loja → (subadquirente) → **adquirente** → rede do arranjo/bandeira → **emissor** | **Emissor** aprova ou recusa (saldo, limite, risco) |
| **Liquidação** | Emissor → **adquirente** (credor perante o emissor) → (subadquirente) → loja, na instituição domicílio | Regras do arranjo |

**Pix:**

| Passo | Quem |
| --- | --- |
| 1. Pagador lê o QR Code ou digita a chave | Usuário final |
| 2. Instituição do pagador autentica e envia | Banco **ou** IP participante |
| 3. Liquidação instantânea | **SPI**, infraestrutura do **BCB** (instituidor do arranjo Pix) |
| 4. Instituição do recebedor credita | Banco **ou** IP participante |

**Por que o Pix tem menos elos:** não há adquirente nem bandeira; a liquidação é direta entre as instituições do pagador e do recebedor, no sistema do BCB.

#### O que a prova pode confundir

- **Autorização ≠ liquidação.**
- **Chave Pix ≠ conta**: a chave só identifica a conta.

#### Frase de fixação

> **No cartão, o emissor autoriza e o adquirente cobra; no Pix, a liquidação vai direto pelo sistema do BCB.**

#### Alinhamento ao PD

CPA 4.7.6.1.

---

### 3.3 Arranjo de pagamento — 4 min

#### Como funciona

| Ponto | Explicação |
| --- | --- |
| Definição | **Regras e procedimentos** do serviço de pagamento, aceito por **mais de um recebedor** (Lei 12.865, art. 6º, I) |
| Instituidor | Responsável pelas regras e pela **marca** (ex.: uma bandeira de cartão; o **BCB** no Pix) |
| O que as regras definem | Participação, aceitação, autorização, segurança, riscos, tarifas, **liquidação**, disputas |
| Não é arranjo | Cartão de loja aceito **só** pela própria empresa emissora (Lei 12.865, art. 6º, § 3º) |

| Tipo (Res. BCB 150) | Característica |
| --- | --- |
| **Aberto** | Qualquer instituição que cumpra os critérios do regulamento pode participar |
| **Fechado** | Gestão de conta, emissão e credenciamento concentrados no **próprio instituidor** (ou em seu grupo) |

#### O que a prova pode confundir

- **Arranjo ≠ bandeira ≠ cartão**: a bandeira é a **marca** do instituidor; o cartão é o **instrumento**.
- Arranjo fechado **não é ilegal**.

#### Frase de fixação

> **Arranjo é o código de trânsito; o instituidor é o dono da rodovia.**

#### Alinhamento ao PD

CPA 4.7.6.2.

---

### 3.4 Adquirente (credenciador) — 4 min

#### O que é

**Adquirente** é o nome de mercado do **credenciador**: instituição de pagamento que, **sem gerenciar conta de pagamento**, (a) **habilita recebedores** a aceitar instrumentos de um arranjo e (b) **participa da liquidação como credor perante o emissor** (Res. BCB 80, art. 3º, III).

#### Como funciona

| Adquirente faz | Adquirente não faz |
| --- | --- |
| Habilita o lojista (maquininha, link, e-commerce) | Não emite o cartão |
| Captura e encaminha a venda | Não **autoriza** a compra (é o emissor) |
| Cobra do emissor e repassa ao lojista | Não gerencia a conta do pagador |

| Adquirente | Emissor |
| --- | --- |
| Lado do **recebedor** | Lado do **pagador** |
| Habilita a loja | Entrega o cartão ao cliente |
| **Credor** perante o emissor na liquidação | **Autoriza** ou recusa a transação |

**Autorização do BCB:** desde a **Res. BCB 494/2025**, o credenciador precisa de autorização **antes** de começar; quem já atuava sem ela deve pedir de 1º a 31/05/2026.

#### O que a prova pode confundir

- **Adquirente ≠ bandeira ≠ emissor.**

#### Frase de fixação

> **Adquirente habilita a loja e cobra o emissor; emissor atende o pagador e autoriza.**

#### Alinhamento ao PD

CPA 4.7.6.3.

---

### 3.5 Subadquirente (subcredenciador) — 4 min

#### O que é

**Subadquirente** é o nome de mercado do **subcredenciador**: participante do arranjo que **habilita, exclusivamente, o usuário final recebedor** a aceitar instrumentos de pagamento, **mas não participa da liquidação como credor perante o emissor** (Res. BCB 150).

#### Como funciona

| Ponto | Subadquirente | Adquirente |
| --- | --- | --- |
| Habilita o lojista? | Sim, **exclusivamente** o recebedor | Sim |
| Credor perante o emissor? | **Não** | **Sim** |
| Depende de adquirente? | **Sim**, conecta-se a um | Não |
| Perfil típico | Pequenos lojistas, e-commerce, marketplaces (cadastro simples, checkout) | Lojistas de todos os portes |

**Repasse:** emissor → adquirente → **subadquirente** → lojista.

> **Nota de atualização — Res. BCB 522/2025:** subcredenciadores passam a participar **obrigatoriamente da liquidação centralizada** nos arranjos sujeitos a ela (prazo de adaptação de até 180 dias, até **11/05/2026**, segundo fontes de mercado). O **instituidor** deve monitorar os participantes para garantir que o dinheiro do pagador chegue ao recebedor.

#### O que a prova pode confundir

- **Subadquirente não é "adquirente pequeno"**: a diferença é **não ser credor perante o emissor**.
- Subadquirente **não é automaticamente IP**.

#### Frase de fixação

> **Subadquirente coloca o lojista na rede, mas quem cobra o emissor é o adquirente.**

#### Alinhamento ao PD

CPA 4.7.6.4.

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

A CPA cobra a **definição de arranjo**, a **função de cada participante** e a diferença **adquirente × subadquirente**.

### Pontos de atenção

1. **Arranjo = regras e procedimentos, aceito por mais de um recebedor.**
2. **Instituidor = responsável pelo arranjo e pela marca.**
3. **Emissor autoriza; adquirente habilita a loja e é credor perante o emissor.**
4. **Subadquirente habilita exclusivamente o recebedor e não é credor perante o emissor.**
5. **Pix: liquidação no SPI, do BCB; menos elos.**

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Arranjo | Instrumento | Regras × dispositivo que inicia |
| Emissor | Adquirente | Lado do pagador × lado do recebedor |
| Adquirente | Subadquirente | Credor perante o emissor × não é |
| Arranjo aberto | Arranjo fechado | Qualquer instituição que cumpra critérios × concentrado no instituidor |

### Palavras-chave da prova

- **"Conjunto de regras e procedimentos"**: arranjo.
- **"Habilita recebedores"**: credenciador/adquirente.
- **"Exclusivamente o recebedor" / "não é credor perante o emissor"**: subcredenciador.

### Pegadinhas

- "A adquirente autoriza a transação." **Errado:** quem autoriza é o emissor.
- "Bandeira e emissor são a mesma coisa." **Errado.**
- "O DOC é um meio de pagamento em uso." **Errado:** extinto em 2024.

### Frase de fixação

> **Pergunte: de que lado da venda ele está e se cobra o emissor.**

## 5. Case — 3 min

### Situação

> Uma artesã vende pela internet usando uma plataforma de checkout. O cliente paga com cartão de crédito emitido pelo banco dele. A plataforma repassa o valor à artesã depois de receber da empresa de maquininha com quem tem contrato. Outro cliente paga a mesma peça por Pix.

### Conceitos aplicados

| Personagem | Papel |
| --- | --- |
| Artesã | **Usuário final recebedor** |
| Cliente | **Usuário final pagador** |
| Banco do cliente | **Emissor** — autoriza a compra |
| Plataforma de checkout | **Subadquirente** — habilita a artesã, não é credor perante o emissor |
| Empresa de maquininha | **Adquirente** — credor perante o emissor |
| Bandeira do cartão | **Instituidor** do arranjo |
| Pix | Instituição do pagador → **SPI (BCB)** → instituição da artesã |

### Síntese do case

No cartão, cinco papéis; no Pix, o dinheiro vai de uma instituição à outra pelo sistema do BCB.

### Frase de fixação

> **Mais elos, mais custo; menos elos, mais rapidez.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 4.7.6.3 e 4.7.6.4 Adquirente e subadquirente · **Nível:** Médio

### Questão

Uma empresa de tecnologia cadastra pequenos lojistas e os habilita a aceitar cartões por meio de uma adquirente contratada, repassando a eles os valores recebidos. Essa empresa não participa da liquidação das transações como credora perante o emissor. De acordo com a regulamentação do Banco Central, ela atua como:

A) emissora de instrumento de pagamento.

B) instituidora de arranjo de pagamento.

C) subcredenciadora (subadquirente).

D) credenciadora (adquirente).

### Ponto-chave do enunciado

"**Não participa da liquidação como credora perante o emissor**".

### Gabarito

**Alternativa C.**

### Comentário da alternativa correta

O subcredenciador habilita **exclusivamente o recebedor** e **não é credor perante o emissor** na liquidação (Res. BCB 150).

### Por que as demais estão incorretas?

- **A:** o emissor atende o **pagador** e disponibiliza o instrumento; a empresa atende lojistas.
- **B:** o instituidor é o **responsável pelas regras** e pela marca do arranjo.
- **D:** o credenciador **participa** da liquidação como credor perante o emissor.

### Armadilhas e macetes

- **Credor perante o emissor = adquirente; não credor = subadquirente.**

### Referência

Res. BCB 150; Res. BCB 80, art. 3º, III; Programa Detalhado CPA, itens 4.7.6.3 e 4.7.6.4.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. Meio de pagamento = instrumento + conta + participantes + arranjo + liquidação; DOC foi extinto em 2024.
2. Arranjo = regras e procedimentos aceitos por mais de um recebedor; instituidor responde pelas regras e pela marca; aberto × fechado.
3. Emissor (lado do pagador) autoriza; adquirente/credenciador (lado do recebedor) habilita a loja e é credor perante o emissor.
4. Subadquirente/subcredenciador habilita exclusivamente o recebedor e não é credor perante o emissor; entra na liquidação centralizada (Res. BCB 522/2025).
5. Pix: instituição do pagador → SPI (BCB) → instituição do recebedor.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Arranjo | Regras e procedimentos · mais de um recebedor |
| Instituidor | Responsável pelo arranjo e pela marca |
| Instrumento | Dispositivo que inicia o pagamento |
| Conta de pagamento | Registro em nome do usuário final |
| Emissor | Lado do pagador · autoriza |
| Adquirente | Habilita a loja · credor perante o emissor |
| Subadquirente | Habilita só o recebedor · não é credor perante o emissor |
| Pix | Liquidação no SPI, do BCB |

### Cadeia lógica

> Pagador usa o instrumento → emissor autoriza → arranjo organiza → adquirente (e subadquirente) liquidam para a loja → recebedor recebe

### Diferenças que não podem ser confundidas

- **Arranjo ≠ bandeira ≠ cartão.**
- **Emissor ≠ adquirente.**
- **Adquirente ≠ subadquirente.**

### Frase central da aula

> **O arranjo dá as regras, o emissor autoriza, o adquirente habilita a loja e cobra o emissor.**

### Próximo passo de estudo

Revisar a Aula 4.7-A e o item 4.5 (Open Finance, open investment e open insurance).

## Referências oficiais e status

Último acesso: 2026-09-28.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — itens 4.7.6 a 4.7.6.4 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. Presidência da República — Lei 12.865/2013 — art. 6º (arranjo, instituidor, IP, conta, instrumento, moeda eletrônica) — [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12865.htm). **Em vigor.** Conferido nesta sessão.
3. BCB — Resolução BCB 80/2021 — modalidades de IP (art. 3º: credenciador, iniciador etc.), com alterações da Res. BCB 494/2025 — [bcb.gov.br](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=80). **Em vigor, alterada.** Conferido nesta sessão.
4. BCB — Resolução BCB 150/2021 — regulamento dos arranjos (subcredenciador, instituição domicílio, arranjo aberto e fechado) — [bcb.gov.br](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=150). **Em vigor, alterada.** Conferido nesta sessão.
5. BCB — Resolução BCB 522/2025 — gerenciamento de riscos dos arranjos e participação de subcredenciadores na liquidação centralizada — [LegisWeb](https://www.legisweb.com.br/legislacao/?id=486238) · [NDM Advogados](https://ndmadvogados.com.br/artigo/liquidacao-centralizada-subadquirente/). **Em vigor** (texto da norma **não reaberto nesta sessão**; prazo de 11/05/2026 conforme fonte de mercado).
6. Febraban — encerramento do DOC/TEC (15/01/2024 e 29/02/2024) — [febraban.org.br](https://portal.febraban.org.br/noticia/4050/pt-br/). **Confirmado.**

Fontes de origem (não oficiais): Roteiro de Aula 4.7 e PDF A5708 "Fintechs e meios de pagamentos" (`00-fontes/materiais-aula/topico-4.7-fintechs-meios-pagamento/`); APOSTILA-CPA p. 553–555.
