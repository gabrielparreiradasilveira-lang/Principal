# Aula CPA — Aplicações Práticas de Smart Contracts: Empréstimos, DEXs, Seguros, Imobiliário e DAOs

Sep 29, 2026 · @Boss · Roteiro integrado · 40 min

## Identificação e alinhamento

Aula B de 3 do item **4.4 Finanças Descentralizadas (DEFI)** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), **Módulo 4 — Inovação e desenvolvimento de mercado**. Cobre **4.4.3.5 a 4.4.3.10.1**. A Aula A cobre 4.4 a 4.4.3.4; a Aula C cobre a tokenização (4.4.4). Base: **Roteiro de Aula — Aplicações Práticas de Smart Contracts** (fonte principal, condensado), **APOSTILA-CPA p. 542**, **Lei 15.040/2024** e **Código Civil**, conferidos nesta sessão.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 4.4.3.5 Aplicações práticas de smart contracts | Roteiro p. 6–10 | Conferido |
| 4.4.3.6 Contratos de empréstimos | Roteiro p. 10–15 | Conferido; **protocolo real retirado** (conceitos genéricos) |
| 4.4.3.7 Exchanges descentralizadas (DEXs) | Roteiro p. 15–20 | Conferido, **completo** (decisão do professor); **protocolo real retirado** |
| 4.4.3.8 Seguros | Roteiro p. 20–23 · **Lei 15.040/2024** | Conferido pela lei |
| 4.4.3.8.1 Apólices automatizadas | Roteiro p. 23–27 | Conferido |
| 4.4.3.9 Imobiliário | Roteiro p. 27–30 | Conferido |
| 4.4.3.9.1 Compra e venda de propriedades | Roteiro p. 30–32 · **Código Civil arts. 108, 481, 482, 1.245** | Conferido pela lei |
| 4.4.3.10 Governança descentralizada | Roteiro p. 33–35 | Conferido |
| 4.4.3.10.1 DAOs | Roteiro p. 35–39 · APOSTILA-CPA p. 542 | Conferido |

**Cobertura PD × material:** todos os subitens têm material. Esta aula **substitui** a versão anterior da 4.4-B, que havia sido montada só pela apostila.

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 2 min |
| 2. Metáfora central | 2 min |
| 3. Tópicos (Aplicações e oráculos 2 · Empréstimos 4 · DEXs 6 · Seguros e apólices 4 · Imobiliário e compra e venda 4 · Governança e DAOs 5) | 25 min |
| 4. Por que cai na prova | 4 min |
| 5. Case | 2 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **40 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | Roteiro p. 12–15, 42 | Mecânica de empréstimo e "Health Factor" com nome e fórmula de **um protocolo real** | Ensinados como **conceitos genéricos** (garantia, LTV, limite de liquidação, indicador de saúde da posição). Os parâmetros **variam por protocolo** | Decisão do professor |
| 2 | Roteiro p. 15–17 | DEX com nome de **protocolo real** e suas versões | Conceito genérico de formador de mercado automático (AMM); a fórmula x × y = k aparece como **ilustração** do modelo clássico | Decisão do professor |
| 3 | Roteiro p. 22–27 | "Apólice automatizada" apresentada com cuidado como expressão de mercado | Mantido: **não é categoria jurídica** própria; o contrato continua sendo de seguro, feito por **seguradora autorizada** | Lei 15.040/2024, arts. 1º e 2º |
| 4 | APOSTILA-CPA p. 542 | DAO "opera sem estrutura hierárquica" | **Resposta de prova** mantida. **Ressalva:** pode haver desenvolvedores, delegados e signatários com poder concentrado; DAO **não é** automaticamente pessoa jurídica | Roteiro p. 34–38 |
| 5 | Roteiro p. 49–50 | Questão com 5 alternativas | Nova questão com **4 alternativas (A–D)** | — |

## 1. Fala de abertura — 2 min

> Carlos deposita tokens como garantia e pega um empréstimo sem falar com gerente. Troca parte do dinheiro em uma bolsa sem corretora. Contrata um seguro de safra que paga sozinho se não chover. E, junto com outros investidores, **vota** para comprar uma sala comercial.
>
> Tudo isso usa **smart contracts**. Mas cuidado: o código **executa regras**. Ele **não** garante o preço, **não** substitui a seguradora e **não** passa a escritura do imóvel.
>
> Hoje a pergunta é: **o que o código automatiza, e o que continua dependendo de pessoas, instituições e leis?**

### Objetivo da abertura

Mostrar as aplicações práticas e, desde o início, separar **execução técnica** de **validade jurídica**.

### Conexão com o Programa Detalhado

CPA 4.4.3.5 a 4.4.3.10.1.

## 2. Metáfora central — 2 min

### Metáfora: a máquina de regras com sensor

> Pense em uma máquina com **sensor**: recebe uma entrada, confere a condição e entrega o resultado.
>
> - **Garantia suficiente + preço válido** → empréstimo liberado.
> - **Chuva abaixo do limite** → seguro pago.
> - **Quórum atingido + maioria** → decisão executada.
>
> O **sensor** é o **oráculo**: se ele medir errado, a máquina executa **o erro** com perfeição. E a máquina tem um **manual de emergência**: a **governança**, que pode pausar ou mudar regras.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Máquina | Smart contract |
| Sensor | Oráculo (dado externo) |
| Botão | Transação assinada |
| Saída | Pagamento, liquidação, troca, execução de decisão |
| Livro de registros | Blockchain |
| Manual de emergência | Governança, pausa, carteira de várias assinaturas |

### Frase de fixação

> **O código executa a regra; não garante o dado nem substitui a lei.**

## 3. Explicação dos tópicos — 25 min

### 3.1 Aplicações práticas de smart contracts — 2 min

#### Como funciona

A regra precisa virar **critério verificável por máquina**:

> Se garantia ≥ limite **e** assinatura válida **e** dentro do prazo → liberar o ativo.

| Aplicação | O que o código faz |
| --- | --- |
| **Escrow digital** | Segura o pagamento e libera quando a condição é cumprida |
| **Liquidação atômica** | Entrega o ativo e o pagamento **na mesma operação**, reduzindo o risco de uma parte entregar sem receber |
| Empréstimo | Garantia, dívida, juros e liquidação |
| Troca (DEX) | Converte um token em outro |
| Seguro | Paga quando o gatilho é atingido |
| Imobiliário | Coordena pagamentos e direitos representados |
| Governança | Executa decisões votadas |

**Oráculo:** o contrato não "enxerga" o mundo real (preço, chuva, matrícula de imóvel). O oráculo traz esse dado — com riscos de **erro, atraso e manipulação**.

#### Frase de fixação

> **O smart contract executa o que foi programado, não o que as partes imaginaram.**

#### Alinhamento ao PD

CPA 4.4.3.5.

---

### 3.2 Aplicação em contratos de empréstimos — 4 min

#### Como funciona

| Passo | O que acontece |
| --- | --- |
| 1 | Usuário deposita um ativo como **garantia (colateral)** |
| 2 | O **oráculo** informa o preço da garantia |
| 3 | O contrato calcula quanto pode ser emprestado |
| 4 | Libera o empréstimo e registra dívida e juros |
| 5 | Quitada a dívida, a garantia é devolvida |
| 6 | Se a garantia perde valor demais → **liquidação** automática |

| Conceito | O que é |
| --- | --- |
| **Sobrecolateralização** | A garantia vale **mais** que o empréstimo (ex.: garantia 100, empréstimo 60) |
| **LTV** (loan-to-value) | Dívida ÷ valor da garantia (no exemplo, **60%**) |
| **Limite de liquidação** | Percentual da garantia a partir do qual a posição pode ser liquidada |
| **Indicador de saúde da posição** | Alguns protocolos calculam: (garantia × limite de liquidação) ÷ dívida; **abaixo de 1** = risco de liquidação |
| **Liquidante** | Participante que paga parte da dívida e recebe garantia com desconto (bônus) |

**Exemplo ilustrativo:** garantia 10.000; limite de liquidação 80%; dívida 6.000 → indicador = 8.000 ÷ 6.000 = **1,33**. Se a garantia cai para 7.000 → 5.600 ÷ 6.000 = **0,93** → posição **liquidável**.

#### O que a prova pode confundir

- **LTV não é juros**; o indicador de saúde **não é score de crédito**.
- Parâmetros **mudam de protocolo para protocolo**.

#### Frase de fixação

> **No empréstimo DeFi, a garantia protege, o oráculo mede e o código liquida.**

#### Alinhamento ao PD

CPA 4.4.3.6.

---

### 3.3 Exchanges descentralizadas (DEXs) — 6 min

#### O que é

**DEX** é um protocolo de **troca de criptoativos por smart contracts**, em geral **sem uma corretora central** guardando os ativos. Muitas usam **AMM** (formador de mercado automático), mas também existem DEXs com livro de ofertas.

#### Como funciona

| Conceito | O que é |
| --- | --- |
| **AMM** | O preço é dado por uma **fórmula**, não por ofertas casadas |
| **Pool de liquidez** | Reserva com **dois tokens** contra a qual o usuário troca |
| **x × y = k** (modelo clássico) | x e y são as reservas; k é constante: quando um lado sobe, o outro cai, e o preço muda |
| **LP** (provedor de liquidez) | Deposita os dois tokens na pool e recebe parte das **taxas** |
| **Swap** | A troca de um token por outro na pool |
| **Price impact** | Mudança de preço causada pelo **tamanho da própria ordem** frente à liquidez da pool |
| **Slippage** | Diferença **total** entre o preço esperado e o executado (impacto + mercado + espera) |
| **Tolerância de slippage** | Limite definido pelo usuário; se ultrapassado, a transação **reverte** |
| **Impermanent loss** | Perda de oportunidade do **LP** quando os preços dos dois tokens mudam, comparada a só **guardar** os tokens fora da pool; as taxas podem compensar, **sem garantia** |
| **Front-running / MEV** | Quem ordena as transações pode lucrar passando **na frente** de uma ordem vista antes de ser executada |
| **Ataque sandwich** | O atacante **compra antes** e **vende depois** da ordem da vítima, piorando o preço dela |

| DEX | Exchange centralizada |
| --- | --- |
| Protocolo e smart contracts | Empresa e sistemas próprios |
| Ativos na **carteira do usuário** | Ativos sob custódia da plataforma |
| Pool / AMM ou livro on-chain | Livro de ofertas central |
| Riscos de código, oráculo, rede e carteira | Riscos da empresa, da custódia e de contraparte |

**Outros riscos:** token falso, baixa liquidez, taxas de rede altas, aprovação de token excessiva.

#### O que a prova pode confundir

- **Price impact ≠ slippage ≠ impermanent loss.**
- Impermanent loss é risco do **LP**, não do trader.
- **Pool de liquidez não é depósito bancário.**

#### Frase de fixação

> **Na DEX com AMM, o usuário troca contra a pool; a fórmula dá o preço, e o tamanho da ordem move esse preço.**

#### Alinhamento ao PD

CPA 4.4.3.7.

---

### 3.4 Seguros e apólices automatizadas — 4 min

#### O que é

**Contrato de seguro** (Lei 15.040/2024, art. 1º): a **seguradora**, mediante o **prêmio**, garante **interesse legítimo** do segurado contra **riscos predeterminados**. **Só entidades autorizadas** podem fazer contratos de seguro (art. 2º).

#### Como funciona

| Tipo | Como paga | Ponto de atenção |
| --- | --- | --- |
| **Tradicional (indenizatório)** | Após aviso e **regulação do sinistro** (apuração do dano) | Mais lento, paga o dano apurado |
| **Paramétrico** | Quando um **índice objetivo** atinge o **gatilho** (chuva, vento, temperatura) | **Risco de base**: o pagamento pode ser **maior ou menor** que o prejuízo real |

**Apólice automatizada:** expressão de **mercado/tecnologia** para uma apólice em que parte do fluxo roda por software ou smart contract (cotação, emissão, cobrança, checagem do índice, pagamento). **Não é categoria jurídica própria**: continua sendo contrato de seguro, com seguradora autorizada, cobertura, exclusões e direito de contestar.

> Apólice agrícola + chuva abaixo do limite + fonte de dados válida + vigência ativa → pagamento paramétrico

#### O que a prova pode confundir

- **Smart contract não é seguradora.**
- **Seguro paramétrico não paga "exatamente o dano".**

#### Frase de fixação

> **No paramétrico, o gatilho é objetivo; a indenização pode não ser igual ao dano.**

#### Alinhamento ao PD

CPA 4.4.3.8 e 4.4.3.8.1.

---

### 3.5 Imobiliário e compra e venda de propriedades — 4 min

#### Como funciona

**Usos de smart contracts no imobiliário:** escrow, pagamento condicionado, distribuição de aluguéis, tokenização de **direitos econômicos**, governança de ativos coletivos.

**Regras do Código Civil (conferidas):**

| Artigo | Regra |
| --- | --- |
| **481** | Compra e venda: um se obriga a **transferir o domínio**, o outro a **pagar o preço** |
| **482** | A compra e venda pura é **perfeita** quando as partes concordam sobre **objeto e preço** |
| **108** | **Escritura pública** é essencial para direitos reais sobre imóveis acima de **30 salários mínimos** (salvo lei em contrário) |
| **1.245** | A propriedade só se transfere pelo **registro do título no Registro de Imóveis** |

> Acordo sobre objeto e preço → escritura (quando exigida) → título → **registro** → transferência da propriedade

| O token pode ser | O token **não é** automaticamente |
| --- | --- |
| Direito contratual, participação econômica, recebível, cota, direito a renda | Matrícula, escritura, propriedade registrada, posse ou garantia real |

**Financiamento:** a **alienação fiduciária** (Lei 9.514/1997) segue rito jurídico próprio — não se confunde com a liquidação automática de um protocolo DeFi. **LTV imobiliário** = saldo devedor ÷ valor do imóvel (ex.: 300 mil ÷ 500 mil = 60%).

#### Frase de fixação

> **Tokenizar o direito não é transferir o domínio: a propriedade passa pelo registro.**

#### Alinhamento ao PD

CPA 4.4.3.9 e 4.4.3.9.1.

---

### 3.6 Governança descentralizada e DAOs — 5 min

#### O que é

**Governança descentralizada:** decisões de um protocolo (taxas, parâmetros de risco, uso da tesouraria, atualizações) tomadas pelos **participantes**, e não só por uma autoridade central.

**DAO** (Organização Autônoma Descentralizada): organização **sem hierarquia tradicional**, com **regras em smart contracts** e **decisões por votação** dos membros (APOSTILA-CPA p. 542).

#### Como funciona

> Proposta → discussão → votação → **quórum e maioria** → prazo de espera (timelock) → execução automática ou por carteira de várias assinaturas (multisig)

| Componente | Função |
| --- | --- |
| Contrato de governança | Regras de proposta, voto e execução |
| Token de governança | Dá poder de voto conforme o desenho |
| Tesouraria | Recursos coletivos movimentados por regras |
| Quórum / maioria | Participação mínima / resultado aprovado |
| **Timelock** | Intervalo entre aprovação e execução |
| **Multisig** | Exige várias assinaturas para executar |
| Delegação | Transfere o poder de voto a um representante |

| Ressalva | Por quê |
| --- | --- |
| **Votar ≠ executar** | A execução pode depender de timelock, multisig ou executor |
| **Descentralizado ≠ igualitário** | Poucos detentores de tokens, fundadores ou signatários podem concentrar poder |
| **Token de governança ≠ ação** | Não dá automaticamente participação societária |
| **DAO ≠ pessoa jurídica** | Não é, por si só; e o rótulo não cria imunidade regulatória |
| **Voto da DAO ≠ escritura** | A DAO pode votar comprar um imóvel, mas a transferência segue a lei |

#### Frase de fixação

> **DAO distribui decisões em código; não garante poder igual nem dispensa a lei.**

#### Alinhamento ao PD

CPA 4.4.3.10 e 4.4.3.10.1.

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

A CPA descreve uma situação e pergunta **qual mecanismo** está em uso ou **o que o código não resolve**.

### Pontos de atenção

1. **Empréstimo DeFi: garantia (sobrecolateralização), oráculo e liquidação automática.**
2. **DEX com AMM: pool, LP, price impact, slippage e impermanent loss são coisas diferentes.**
3. **Seguro: só seguradora autorizada (Lei 15.040/2024); paramétrico tem risco de base.**
4. **Imóvel: propriedade só com registro (CC art. 1.245).**
5. **DAO: regras em código e votação; votar ≠ executar.**

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| LTV | Indicador de saúde | Dívida/garantia × métrica de liquidação do protocolo |
| AMM | Livro de ofertas | Fórmula e pool × ordens casadas |
| Price impact | Slippage | Tamanho da ordem × diferença total |
| Slippage | Impermanent loss | Risco do trader × custo de oportunidade do LP |
| Seguro paramétrico | Seguro tradicional | Índice/gatilho × apuração do dano |
| Token imobiliário | Propriedade | Representação digital × domínio registrado |
| Governança | Execução | Decisão aprovada × transação realizada |

### Palavras-chave da prova

- **"Garantia maior que o empréstimo"**: sobrecolateralização.
- **"Pool de dois tokens"**: AMM.
- **"Comparado a apenas manter os tokens"**: impermanent loss.
- **"Índice e gatilho"**: seguro paramétrico.
- **"Quórum", "tesouraria coletiva"**: DAO.

### Pegadinhas

- "Token imobiliário transfere a propriedade do imóvel." **Errado.**
- "Seguro paramétrico paga exatamente o prejuízo." **Errado.**
- "Voto aprovado na DAO é sempre executado automaticamente." **Errado.**
- "Price impact e slippage são sinônimos." **Errado.**

### Frase de fixação

> **Tecnologia ≠ direito · automação ≠ segurança · votação ≠ execução · token ≠ propriedade.**

## 5. Case — 2 min

### Situação

> Carlos deposita tokens como garantia e toma um empréstimo. Troca parte em uma DEX com uma ordem grande para a pool, e recebe menos do que a tela mostrava. Contrata, por uma seguradora autorizada, um seguro agrícola paramétrico: a chuva fica abaixo do gatilho e ele recebe 60 mil, embora tenha perdido 100 mil. A DAO de que participa vota a compra de uma sala comercial. Dias depois, o oráculo de preço atrasa numa queda forte, e a garantia de Carlos parece valer mais do que vale.

### Conceitos aplicados

| Fato | Conceito |
| --- | --- |
| Garantia e empréstimo | Empréstimo por smart contract |
| Recebeu menos na troca | **Price impact** e **slippage** |
| Recebeu 60 mil com perda de 100 mil | **Risco de base** do seguro paramétrico |
| DAO vota a compra | **Governança**; a propriedade depende de escritura e registro |
| Oráculo atrasado | **Risco de oráculo**: a liquidação demora, o protocolo pode ter perda |

### Síntese do case

O código fez sua parte em cada módulo; os riscos vieram do dado, da liquidez, do contrato e da lei.

### Frase de fixação

> **A automação diminui etapas manuais, mas não elimina o mundo lá fora.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 4.4.3.7 a 4.4.3.9.1 DEXs, seguros e imobiliário · **Nível:** Difícil

### Questão

Sobre aplicações práticas de smart contracts, é correto afirmar que:

A) em uma DEX baseada em formador de mercado automático (AMM), o preço resulta do casamento de ordens em um livro de ofertas centralizado, e a impermanent loss é a taxa de rede paga pelo usuário.

B) no seguro paramétrico, o pagamento ocorre quando um índice objetivo atinge o gatilho contratado, podendo ser maior ou menor que o prejuízo efetivo do segurado.

C) a representação de um imóvel por token registrado em blockchain transfere a propriedade ao comprador, dispensando escritura e registro no Registro de Imóveis.

D) a automação por smart contract permite que qualquer empresa ofereça contratos de seguro, independentemente de autorização.

### Ponto-chave do enunciado

Separar **mecanismo técnico** de **regra jurídica** em cada aplicação.

### Gabarito

**Alternativa B.**

### Comentário da alternativa correta

O seguro paramétrico paga pelo **gatilho do índice**, não pela apuração do dano; por isso existe o **risco de base** (pagamento diferente da perda real).

### Por que as demais estão incorretas?

- **A:** no AMM o preço vem da **pool e da fórmula**; impermanent loss é o **custo de oportunidade do LP**, não taxa de rede.
- **C:** a propriedade imobiliária só se transfere pelo **registro do título** (Código Civil, art. 1.245).
- **D:** só **entidades autorizadas** podem fazer contratos de seguro (Lei 15.040/2024, art. 2º).

### Armadilhas e macetes

- **Paramétrico = gatilho; imóvel = registro; seguro = seguradora autorizada.**

### Referência

Lei 15.040/2024, arts. 1º e 2º; Código Civil, art. 1.245; Programa Detalhado CPA, itens 4.4.3.7 a 4.4.3.9.1.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. Smart contracts aplicam regras verificáveis (escrow, liquidação atômica, empréstimos, trocas, seguros, governança); o oráculo traz dados externos com risco próprio.
2. Empréstimo DeFi: garantia maior que a dívida, LTV, limite de liquidação, indicador de saúde; parâmetros variam por protocolo.
3. DEX/AMM: troca contra a pool; LP ganha taxas e corre impermanent loss; o trader enfrenta price impact, slippage, front-running e sandwich.
4. Seguro: só seguradora autorizada (Lei 15.040/2024); paramétrico paga pelo gatilho, com risco de base; apólice automatizada é tecnologia, não categoria jurídica.
5. Imóvel: compra e venda (CC 481/482), escritura (CC 108) e registro (CC 1.245); DAO: regras em código e votação, com timelock e multisig; votar ≠ executar.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Empréstimo DeFi | Garantia > dívida · oráculo · liquidação automática |
| LTV | Dívida ÷ garantia |
| AMM | Pool de dois tokens · preço pela fórmula |
| Price impact | Efeito do tamanho da própria ordem |
| Slippage | Diferença total esperado × executado |
| Impermanent loss | Custo de oportunidade do LP |
| Seguro | Seguradora autorizada · Lei 15.040/2024 |
| Paramétrico | Gatilho objetivo · risco de base |
| Imóvel | Propriedade só com registro (CC 1.245) |
| DAO | Código + votação · timelock · multisig |

### Cadeia lógica

> Regra verificável → smart contract → dado do oráculo → execução automática → riscos técnicos + jurídicos + governança

### Diferenças que não podem ser confundidas

- **Price impact ≠ slippage ≠ impermanent loss.**
- **Seguro paramétrico ≠ seguro indenizatório.**
- **Token ≠ propriedade · votação ≠ execução.**

### Frase central da aula

> **O código executa a regra; o dado, a liquidez, o contrato e a lei continuam decidindo o resultado.**

### Próximo passo de estudo

Aula 4.4-C — Tokenização.

## Referências oficiais e status

Último acesso: 2026-09-29.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — itens 4.4.3.5 a 4.4.3.10.1 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. Presidência da República — Lei 15.040/2024 — normas de seguro privado (arts. 1º e 2º; vigência 1 ano após a publicação de 10/12/2024) — [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/lei/l15040.htm). **Em vigor.** Conferido nesta sessão.
3. Presidência da República — Lei 10.406/2002 (Código Civil) — arts. 108, 481, 482 e 1.245 — [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm). **Em vigor.** Conferido nesta sessão.
4. Presidência da República — Lei 9.514/1997 — alienação fiduciária de coisa imóvel. **Em vigor** (texto **não reaberto nesta sessão**).
5. CVM — página "Criptoativos: quando se aplicam as regras da CVM?" (atualizada em 06/02/2026, segundo o roteiro) e SUSEP — Sandbox Regulatório (2ª edição): **não confirmados nesta sessão**.
6. Conceitos de AMM, pool, LP, price impact, slippage, impermanent loss, MEV, timelock e multisig: prática de mercado e documentação técnica de protocolos (citadas no roteiro; **não reabertas nesta sessão**).

Fontes de origem (não oficiais): Roteiro de Aula — Aplicações Práticas de Smart Contracts (`00-fontes/materiais-aula/topico-4.4-defi-blockchain-smart-contracts/`); APOSTILA-CPA p. 542.
