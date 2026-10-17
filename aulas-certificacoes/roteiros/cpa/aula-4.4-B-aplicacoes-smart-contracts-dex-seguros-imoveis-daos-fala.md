# Roteiro de fala — Aula CPA: Aplicações de Smart Contracts — Empréstimos, DEXs, Seguros, Imóveis e DAOs

**Base:**
- aula do repositório `aulas/cpa/aula-4.4-B-aplicacoes-smart-contracts-daos/aula.md`;
- roteiro em PDF `roteiro-4.4.3.5-aplicacoes-smart-contracts` (lote `topico-4.4-defi-blockchain-smart-contracts`);
- APOSTILA-CPA, p. 542;
- Lei 15.040/2024 (seguros) e Código Civil (arts. 108, 481, 482 e 1.245), conferidos na aula do repositório em 29/09/2026.

CPA 4.4.3.5 · 4.4.3.6 · 4.4.3.7 · 4.4.3.8 · 4.4.3.8.1 · 4.4.3.9 · 4.4.3.9.1 · 4.4.3.10 · 4.4.3.10.1 · Módulo 4 · **40 min** · Aula B de 3 do bloco 4.4

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ✏️ = correção da fonte · ➕ = acréscimo desta versão · 🔗 = ponte · ⌨️ = teclas da HP12C · 🖥️ = visor.

---

## Bastidor — antes de gravar

### 🔇 Checagem de escopo (PD × materiais)

| Subitem do PD | Na imagem? | PDF do lote | Apostila | Tratamento |
| --- | --- | --- | --- | --- |
| 4.4.3.5 Aplicações práticas | **Não** | Roteiro p. 6–10 | — | Incluído (decisão do professor) |
| 4.4.3.6 Contratos de empréstimos | **Não** | Roteiro p. 10–15 | — | Incluído; protocolo real trocado por conceito genérico |
| 4.4.3.7 DEXs | Sim | Roteiro p. 15–20 | — | Coberto; protocolo real trocado por conceito genérico |
| 4.4.3.8 Seguros | Sim | Roteiro p. 20–23 | — | Coberto; conferido pela Lei 15.040/2024 |
| 4.4.3.8.1 Apólices automatizadas | Sim | Roteiro p. 23–27 | — | Coberto |
| 4.4.3.9 Imobiliário | Sim | Roteiro p. 27–30 | — | Coberto |
| 4.4.3.9.1 Compra e venda de propriedades | **Não** | Roteiro p. 30–32 | — | Incluído; conferido pelo Código Civil |
| 4.4.3.10 Governança descentralizada | **Não** | Roteiro p. 33–35 | — | Incluído |
| 4.4.3.10.1 DAOs | **Não** | Roteiro p. 35–39 | p. 542 | Incluído |

**Cobertura:** todos os subitens têm material no PDF. A apostila só trata de DAOs.

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto | Base |
| --- | --- | --- | --- | --- |
| 1 | Roteiro p. 12–15 | Mecânica de empréstimo com nome e fórmula de **um protocolo real** | Ensinado como **conceito genérico** (garantia, LTV, limite de liquidação, indicador de saúde). Parâmetros **variam por protocolo** | Padrão do projeto |
| 2 | Roteiro p. 15–17 | DEX com nome de **protocolo real** | Conceito genérico de **AMM**; x × y = k como **ilustração** do modelo clássico | Padrão do projeto |
| 3 | Roteiro p. 22–27 | "Apólice automatizada" | **Não é categoria jurídica**: continua sendo contrato de seguro, feito por **seguradora autorizada** | Lei 15.040/2024, arts. 1º e 2º |
| 4 | Apostila p. 542 | DAO "opera sem estrutura hierárquica" | **Resposta de prova** mantida. **Ressalva:** pode haver poder concentrado; DAO **não é** automaticamente pessoa jurídica | Roteiro em PDF p. 34–38 |
| 5 | Apostila p. 542 | DAO de arrecadação ligada a um conflito armado real | Exemplo **retirado**; caso genérico | Padrão do projeto |

### ➕ Kit HP12C

- 🔇 A HP aparece duas vezes: no **empréstimo com garantia** (LTV e indicador de saúde) e na **DEX** (x × y = k e impacto de preço).
- Preparar com ⌨️ `f` `REG` e ⌨️ `f` `2`.

| Recurso | Teclas | Para que serve aqui |
| --- | --- | --- |
| Limpar | ⌨️ `f` `REG` | Zera pilha e memórias |
| Percentual do total | ⌨️ total `ENTER` parte `%T` | LTV = dívida ÷ garantia |
| Guardar e chamar | ⌨️ `STO` `1` · `RCL` `1` | Guardar a constante k da pool |
| Trocar X e Y | ⌨️ `x≷y` | Ordem da subtração |

### 🔇 Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Abertura | 2 min |
| 2. Metáfora | 2 min |
| 3. Tópicos (3.1 Aplicações 2 · 3.2 Empréstimos 5 · 3.3 DEXs 7 · 3.4 Seguros 5 · 3.5 Imóveis 4 · 3.6 DAOs 5) | 28 min |
| 4. Por que cai | 3 min |
| 5. Case | 2 min |
| 6. Questões | 2 min |
| 7. Revisão | 1 min |
| **Total** | **40 min** |

---

## 1. Fala de abertura — 2 min

- **Um dia na vida de um usuário de DeFi**
  - "Imagine um investidor que deposita tokens como garantia e pega um empréstimo sem falar com gerente. Troca parte do dinheiro numa bolsa sem corretora. Contrata um seguro de safra que paga sozinho se não chover. E, com outros investidores, vota para comprar uma sala comercial."

- **O alerta**
  - "Tudo isso usa smart contracts. Mas o código executa regras. Ele não garante o preço, não substitui a seguradora e não passa a escritura do imóvel."

- **A pergunta da aula**
  - "O que o código automatiza, e o que continua dependendo de pessoas, instituições e leis?"

- 🔇 Conexão com o PD: CPA 4.4.3.5 a 4.4.3.10.1. Vem depois da 4.4-A (DeFi, blockchain e smart contracts) e antes da 4.4-C (tokenização).

**🔗 Ponte:** "Vamos usar uma máquina com sensor."

---

## 2. Metáfora central — 2 min

### Metáfora: a máquina de regras com sensor

- **A máquina**
  - "Pense numa máquina com sensor: ela recebe uma entrada, confere a condição e entrega o resultado. Garantia suficiente e preço válido: empréstimo liberado. Chuva abaixo do limite: seguro pago. Quórum atingido e maioria: decisão executada."

- **O sensor que erra**
  - "O sensor é o oráculo. Se ele medir errado, a máquina executa o erro com perfeição. E a máquina tem um manual de emergência: a governança, que pode pausar ou mudar regras."

### Correspondência técnica

| Máquina com sensor | Aplicações de smart contracts |
| --- | --- |
| Máquina | Smart contract |
| Sensor | **Oráculo** |
| Botão | Transação assinada |
| Saída | Pagamento, liquidação, troca, decisão executada |
| Livro de registros | Blockchain |
| Manual de emergência | **Governança**, pausa, **multisig** |

### Frase de fixação

> **O código executa a regra; não garante o dado nem substitui a lei.**

**🔗 Ponte:** "Primeiro, o que dá para automatizar."

---

## 3. Explicação dos tópicos — 28 min

### 3.1 Aplicações práticas de smart contracts — 2 min · CPA 4.4.3.5

- **A regra vira critério de máquina**
  - "Para virar smart contract, a regra precisa ser verificável por máquina: se a garantia é maior que o limite, e a assinatura é válida, e está dentro do prazo, então libera o ativo."

| Aplicação | O que o código faz |
| --- | --- |
| **Escrow digital** | Segura o pagamento e libera quando a condição é cumprida |
| **Liquidação atômica** | Entrega o ativo e o pagamento **na mesma operação**: ninguém entrega sem receber |
| Empréstimo | Garantia, dívida, juros e liquidação |
| Troca (DEX) | Converte um token em outro |
| Seguro | Paga quando o gatilho é atingido |
| Imobiliário | Coordena pagamentos e direitos representados |
| Governança | Executa decisões votadas |

> **O smart contract executa o que foi programado, não o que as partes imaginaram.**

**🔗 Ponte:** "A aplicação mais usada: empréstimo com garantia."

---

### 3.2 Contratos de empréstimos — 5 min · CPA 4.4.3.6

| Passo | O que acontece |
| --- | --- |
| 1 | O usuário deposita um ativo como **garantia (colateral)** |
| 2 | O **oráculo** informa o preço da garantia |
| 3 | O contrato calcula quanto pode ser emprestado |
| 4 | Libera o empréstimo e registra dívida e juros |
| 5 | Quitada a dívida, a garantia volta |
| 6 | Se a garantia perde valor demais → **liquidação automática** |

| Conceito | O que é |
| --- | --- |
| **Sobrecolateralização** | A garantia vale **mais** que o empréstimo |
| **LTV** (*loan-to-value*) | Dívida ÷ valor da garantia |
| **Limite de liquidação** | Percentual da garantia a partir do qual a posição pode ser liquidada |
| **Indicador de saúde** | Em alguns protocolos: (garantia × limite de liquidação) ÷ dívida; **abaixo de 1** = liquidável |
| **Liquidante** | Quem paga parte da dívida e recebe garantia com desconto |

- **Por que a garantia é maior**
  - "No DeFi não há análise de renda nem cadastro como no banco. A proteção é a garantia, e ela é maior que a dívida porque o preço do token oscila muito."

#### ➕ Exemplo prático 1 — LTV e indicador de saúde

Garantia de **R$ 10.000**, dívida de **R$ 6.000**, limite de liquidação de **80%**. Depois, a garantia cai para **R$ 7.000**.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` | 🖥️ 0,00 | Pilha limpa |
| 2 | ⌨️ `10000` `ENTER` `6000` `%T` | 🖥️ 60,00 | **LTV de 60%** |
| 3 | ⌨️ `10000` `ENTER` `0,8` `×` `6000` `÷` | 🖥️ 1,33 | Indicador de saúde **1,33**: posição saudável |
| 4 | ⌨️ `7000` `ENTER` `0,8` `×` `6000` `÷` | 🖥️ 0,93 | Garantia caiu: indicador **0,93**, **abaixo de 1** |

- "Com garantia de 10 mil e dívida de 6 mil, o LTV é 60%. O indicador é 10 mil vezes 80%, 8 mil, dividido por 6 mil: 1,33. Saudável. Se a garantia cai para 7 mil: 7 mil vezes 80%, 5.600, dividido por 6 mil: 0,93. Abaixo de 1. O contrato pode liquidar a posição sozinho, sem aviso de gerente."
- 🔇 Valores hipotéticos. Na HP, a vírgula decimal digita-se com a tecla `.`. Os parâmetros (80%, fórmula do indicador) **variam por protocolo**.

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "No empréstimo DeFi, a garantia costuma ser menor que o valor emprestado" | Errado | **Sobrecolateralização**: garantia maior |
| "LTV é a taxa de juros do empréstimo" | Errado | É **dívida ÷ garantia** |
| "A liquidação depende de decisão de um gerente" | Errado | É **automática** pelo contrato |

> **No empréstimo DeFi, a garantia protege, o oráculo mede e o código liquida.**

**🔗 Ponte:** "E onde o usuário troca um token por outro? Na DEX."

---

### 3.3 Exchanges descentralizadas (DEXs) — 7 min · CPA 4.4.3.7

- **O que é**
  - "DEX é uma bolsa descentralizada: um protocolo de troca de criptoativos por smart contracts, em geral sem uma corretora guardando os ativos. Muitas usam o formador de mercado automático, o AMM."

| Conceito | O que é |
| --- | --- |
| **AMM** | O preço vem de uma **fórmula**, não de ordens casadas |
| **Pool de liquidez** | Reserva com **dois tokens** contra a qual o usuário troca |
| **x × y = k** | x e y são as reservas; k é constante. Um lado sobe, o outro cai, o preço muda |
| **LP** (provedor de liquidez) | Deposita os dois tokens e recebe parte das **taxas** |
| ***Swap*** | A troca de um token por outro na pool |
| ***Price impact*** | Mudança de preço causada pelo **tamanho da própria ordem** |
| ***Slippage*** | Diferença **total** entre o preço esperado e o executado |
| **Tolerância de *slippage*** | Limite do usuário; se ultrapassado, a transação **reverte** |
| ***Impermanent loss*** | Perda de oportunidade do **LP** frente a só **guardar** os tokens |
| ***Front-running*** / ataque *sandwich* | Alguém passa **na frente** da ordem vista na rede e piora o preço da vítima |

#### ➕ Exemplo prático 2 — x × y = k e o impacto de preço

Pool com **100 tokens A** e **10.000 tokens B**: preço inicial de **100 B por A**. Sem taxa, para simplificar.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` | 🖥️ 0,00 | Pilha limpa |
| 2 | ⌨️ `100` `ENTER` `10000` `×` `STO` `1` | 🖥️ 1.000.000,00 | **k = 1.000.000**, guardado |
| 3 | ⌨️ `100` `ENTER` `RCL` `1` `11000` `÷` `-` | 🖥️ 9,09 | Ordem **grande**: paga 1.000 B (pool vai a 11.000 B) e recebe **9,09 A** |
| 4 | ⌨️ `STO` `2` `1000` `RCL` `2` `÷` | 🖥️ 110,00 | Preço médio **110 B por A**: **10% acima** de 100 |
| 5 | ⌨️ `100` `ENTER` `RCL` `1` `10100` `÷` `-` | 🖥️ 0,99 | Ordem **pequena**: paga 100 B e recebe **0,99 A** |
| 6 | ⌨️ `STO` `3` `100` `RCL` `3` `÷` | 🖥️ 101,00 | Preço médio **101 B por A**: só **1% acima** |

- "A pool tem 100 de A e 10 mil de B. Multiplicando, k é 1 milhão, e esse número não pode mudar. Se eu coloco 1.000 de B, a pool fica com 11 mil de B. Para k continuar 1 milhão, sobram 1 milhão dividido por 11 mil: 90,91 de A. Eu levo a diferença: 9,09 de A."
- "Paguei 1.000 por 9,09: preço médio de 110. A tela mostrava 100. Esses 10% são o impacto de preço da minha própria ordem. Com uma ordem de só 100 de B, o preço médio fica em 101: impacto de 1%. Quanto maior a ordem em relação à pool, pior o preço."
- 🔇 Valores hipotéticos. A fórmula x × y = k ilustra o modelo clássico; há DEXs com outras fórmulas e com livro de ofertas.

| DEX | Exchange centralizada |
| --- | --- |
| Protocolo e smart contracts | Empresa e sistemas próprios |
| Ativos na **carteira do usuário** | Ativos sob custódia da plataforma |
| Pool / AMM ou livro na blockchain | Livro de ofertas central |
| Riscos de código, oráculo, rede e carteira | Riscos da empresa, da custódia e de contraparte |

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "*Price impact* e *slippage* são sinônimos" | Errado | Impacto é efeito da **própria ordem**; *slippage* é a diferença **total** |
| "*Impermanent loss* é risco do trader" | Errado | É risco do **provedor de liquidez** |
| "Pool de liquidez é um depósito bancário com garantia do FGC" | Errado | Não é depósito, **sem FGC** |

> **Na DEX com AMM, o usuário troca contra a pool; a fórmula dá o preço, e o tamanho da ordem move esse preço.**

**🔗 Ponte:** "Agora, uma aplicação em que a lei pesa muito: o seguro."

---

### 3.4 Seguros e apólices automatizadas — 5 min · CPA 4.4.3.8 e 4.4.3.8.1

- **O contrato de seguro pela lei**
  - "Pela Lei 15.040, de 2024, no contrato de seguro a seguradora, mediante o prêmio, garante interesse legítimo do segurado contra riscos predeterminados. E só entidades autorizadas podem fazer contratos de seguro. Smart contract não é seguradora."

| Tipo | Como paga | Ponto de atenção |
| --- | --- | --- |
| **Tradicional (indenizatório)** | Após aviso e **regulação do sinistro** (apuração do dano) | Mais lento; paga o dano apurado |
| **Paramétrico** | Quando um **índice objetivo** atinge o **gatilho** (chuva, vento, temperatura) | **Risco de base**: o pagamento pode ser **maior ou menor** que o prejuízo |

- **Apólice automatizada**
  - "Apólice automatizada é uma expressão de mercado: parte do fluxo roda por software ou smart contract. Cotação, emissão, cobrança, conferência do índice, pagamento. Mas juridicamente continua sendo contrato de seguro, com seguradora autorizada, cobertura, exclusões e direito de contestar."

- **O fluxo**
  - "Apólice agrícola, mais chuva abaixo do limite, mais fonte de dados válida, mais vigência ativa: pagamento paramétrico."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Seguro paramétrico paga exatamente o prejuízo" | Errado | Paga pelo **gatilho**; há **risco de base** |
| "Com smart contract, qualquer empresa pode oferecer seguro" | Errado | Só **entidade autorizada** (Lei 15.040/2024, art. 2º) |
| "Apólice automatizada é uma nova espécie jurídica de contrato" | Errado | É **tecnologia** aplicada ao contrato de seguro |

> **No paramétrico, o gatilho é objetivo; a indenização pode não ser igual ao dano.**

**🔗 Ponte:** "Outra área em que o código esbarra na lei: imóveis."

---

### 3.5 Imobiliário e compra e venda de propriedades — 4 min · CPA 4.4.3.9 e 4.4.3.9.1

- **Onde o smart contract ajuda**
  - "No imobiliário, o código ajuda em escrow, pagamento condicionado, distribuição de aluguéis, tokenização de direitos econômicos e governança de imóveis coletivos."

- **O que a lei exige**

| Artigo do Código Civil | Regra |
| --- | --- |
| **481** | Na compra e venda, um se obriga a **transferir o domínio** e o outro a **pagar o preço** |
| **482** | A compra e venda pura é **perfeita** quando as partes concordam sobre **objeto e preço** |
| **108** | **Escritura pública** é essencial para direitos reais sobre imóveis acima de **30 salários mínimos** (salvo lei em contrário) |
| **1.245** | A propriedade só se transfere pelo **registro do título no Registro de Imóveis** |

- **A sequência**
  - "Acordo sobre objeto e preço, escritura quando exigida, título, registro, e só aí a propriedade muda de dono."

| O token pode ser | O token **não é**, sozinho |
| --- | --- |
| Direito contratual, participação econômica, recebível, cota, direito a renda | Matrícula, escritura, propriedade registrada, posse ou garantia real |

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Token imobiliário registrado em blockchain transfere a propriedade" | Errado | Propriedade só com **registro** (CC 1.245) |
| "Smart contract dispensa a escritura pública" | Errado | CC 108 continua valendo |

> **Tokenizar o direito não é transferir o domínio: a propriedade passa pelo registro.**

**🔗 Ponte:** "E quem decide as regras de um protocolo? A governança."

---

### 3.6 Governança descentralizada e DAOs — 5 min · CPA 4.4.3.10 e 4.4.3.10.1 · Apostila p. 542

- **Governança descentralizada**
  - "As decisões de um protocolo, como taxas, parâmetros de risco e uso do caixa, são tomadas pelos participantes, e não só por uma autoridade central."

- **DAO**
  - "DAO é a Organização Autônoma Descentralizada: uma organização sem hierarquia tradicional, com regras em smart contracts e decisões por votação dos membros."

- **O ciclo**
  - "Proposta, discussão, votação, quórum e maioria, prazo de espera e execução, automática ou por uma carteira que exige várias assinaturas."

| Componente | Função |
| --- | --- |
| Token de governança | Dá poder de voto conforme o desenho |
| Tesouraria | Recursos coletivos movidos por regras |
| Quórum / maioria | Participação mínima / resultado aprovado |
| ***Timelock*** | Intervalo entre aprovação e execução |
| ***Multisig*** | Várias assinaturas para executar |
| Delegação | Passar o voto a um representante |

| Ressalva | Por quê |
| --- | --- |
| **Votar ≠ executar** | A execução pode depender de *timelock*, *multisig* ou executor |
| **Descentralizado ≠ igualitário** | Poucos detentores de tokens podem concentrar poder |
| **Token de governança ≠ ação** | Não dá participação societária automaticamente |
| **DAO ≠ pessoa jurídica** | Não é, por si só; o rótulo não dá imunidade regulatória |

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Voto aprovado na DAO é sempre executado na hora" | Errado | Pode haver ***timelock*** e ***multisig*** |
| "Em toda DAO o poder de voto é igual entre os membros" | Errado | Depende dos tokens e do desenho |

> **DAO distribui decisões em código; não garante poder igual nem dispensa a lei.**

**🔗 Ponte:** "Agora, por que isso cai."

---

## 4. Por que isso cai na prova? — 3 min

- **Como a banca pergunta**
  - "A CPA descreve uma situação e pergunta qual mecanismo está em uso, ou o que o código não resolve."

### Pontos de atenção

1. **Empréstimo DeFi:** sobrecolateralização, oráculo e liquidação automática.
2. **DEX/AMM:** pool, LP, *price impact*, *slippage* e *impermanent loss* são coisas diferentes.
3. **Seguro:** só seguradora autorizada; paramétrico tem risco de base.
4. **Imóvel:** propriedade só com registro (CC 1.245).
5. **DAO:** regras em código e votação; votar ≠ executar.

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| LTV | Indicador de saúde | Dívida ÷ garantia × métrica de liquidação |
| AMM | Livro de ofertas | Fórmula e pool × ordens casadas |
| *Price impact* | *Slippage* | Tamanho da ordem × diferença total |
| *Slippage* | *Impermanent loss* | Risco do trader × custo de oportunidade do LP |
| Paramétrico | Tradicional | Gatilho × apuração do dano |
| Token imobiliário | Propriedade | Representação × domínio registrado |

### Pegadinhas (todas erradas)

- "Token imobiliário transfere a propriedade."
- "Seguro paramétrico paga exatamente o prejuízo."
- "Voto aprovado na DAO é sempre executado automaticamente."
- "*Price impact* e *slippage* são sinônimos."

> **Tecnologia ≠ direito · automação ≠ segurança · votação ≠ execução · token ≠ propriedade.**

**🔗 Ponte:** "Vamos juntar tudo num caso."

---

## 5. Case — 2 min

- "Um investidor deposita tokens como garantia e toma um empréstimo. Troca parte numa DEX com uma ordem grande para o tamanho da pool, e recebe menos do que a tela mostrava. Contrata, por uma seguradora autorizada, um seguro agrícola paramétrico: a chuva fica abaixo do gatilho e ele recebe 60 mil, embora tenha perdido 100 mil. A DAO de que participa vota a compra de uma sala comercial. Dias depois, o oráculo de preço atrasa numa queda forte, e a garantia parece valer mais do que vale."

| Fato | Conceito |
| --- | --- |
| Garantia e empréstimo | Empréstimo por smart contract |
| Recebeu menos na troca | ***Price impact*** e ***slippage*** |
| Recebeu 60 mil com perda de 100 mil | **Risco de base** do paramétrico |
| DAO vota a compra | **Governança**; a propriedade depende de escritura e registro |
| Oráculo atrasado | **Risco de oráculo**: a liquidação atrasa |

- "O código fez sua parte em cada etapa. Os riscos vieram do dado, da liquidez, do contrato e da lei."

> **A automação diminui etapas manuais, mas não elimina o mundo lá fora.**

**🔗 Ponte:** "Agora, as questões."

---

## 6. Questões comentadas — 2 min

### Questão 1 — Difícil

**CPA · 4.4.3.7 a 4.4.3.9.1 DEXs, seguros e imobiliário · Difícil**

Sobre aplicações práticas de smart contracts, é correto afirmar que:

A) em uma DEX baseada em formador de mercado automático (AMM), o preço resulta do casamento de ordens em um livro de ofertas centralizado, e a *impermanent loss* é a taxa de rede paga pelo usuário.
B) no seguro paramétrico, o pagamento ocorre quando um índice objetivo atinge o gatilho contratado, podendo ser maior ou menor que o prejuízo efetivo do segurado.
C) a representação de um imóvel por token registrado em blockchain transfere a propriedade ao comprador, dispensando escritura e registro.
D) a automação por smart contract permite que qualquer empresa ofereça contratos de seguro, independentemente de autorização.

**Gabarito: B**

- **B (correta):** paga pelo gatilho; há risco de base.
- **A:** no AMM o preço vem da pool e da fórmula; *impermanent loss* é custo de oportunidade do LP.
- **C:** propriedade só com registro (CC 1.245).
- **D:** só entidade autorizada (Lei 15.040/2024, art. 2º).
  - "Resposta B. Paramétrico é gatilho; imóvel é registro; seguro é seguradora autorizada."

### ➕ Questão 2 — Médio

**CPA · 4.4.3.6 Contratos de empréstimos · Médio**

Em um protocolo de empréstimo DeFi, um investidor deposita R$ 10.000 em tokens como garantia e toma R$ 6.000. Nessa situação:

A) o LTV da operação é de 60%, e a garantia superior ao valor emprestado caracteriza a sobrecolateralização.
B) o LTV é de 166%, porque a garantia é maior que a dívida.
C) a liquidação da garantia depende de aprovação manual do gerente do protocolo.
D) a operação é subcolateralizada, pois a dívida é menor que a garantia.

**Gabarito: A**

- **A (correta):** 6.000 ÷ 10.000 = 60%; garantia maior que a dívida.
- **B:** inverteu a conta (garantia ÷ dívida).
- **C:** a liquidação é automática.
- **D:** garantia maior que a dívida é **sobre**colateralização.
  - "Resposta A. Na HP: 10.000 ENTER 6.000 %T dá 60."

### ➕ Questão 3 — Fácil

**CPA · 4.4.3.10.1 DAOs · Fácil**

Uma Organização Autônoma Descentralizada (DAO) caracteriza-se por:

A) ter um diretor-presidente que decide sozinho sobre o uso dos recursos.
B) ter regras codificadas em smart contracts e decisões tomadas por votação dos membros.
C) ser automaticamente uma pessoa jurídica registrada na junta comercial.
D) garantir que todos os membros tenham exatamente o mesmo poder de voto.

**Gabarito: B**

- **B (correta):** definição da apostila (p. 542).
- **A:** não há hierarquia tradicional.
- **C:** DAO não é automaticamente pessoa jurídica.
- **D:** o poder de voto depende do desenho e dos tokens.
  - "Resposta B. Código mais votação."

**🔗 Ponte:** "Para fechar, a revisão."

---

## 7. Revisão final — 1 min

### Resumo em cinco pontos

1. Smart contracts aplicam regras verificáveis; o oráculo traz dados externos com risco próprio.
2. Empréstimo DeFi: garantia maior que a dívida, LTV, limite de liquidação e indicador de saúde (abaixo de 1 = liquidável).
3. DEX/AMM: troca contra a pool pela fórmula x × y = k; ordem grande move o preço; LP corre *impermanent loss*.
4. Seguro: só seguradora autorizada; paramétrico paga pelo gatilho, com risco de base; apólice automatizada é tecnologia, não espécie jurídica.
5. Imóvel: escritura (CC 108) e registro (CC 1.245); DAO: código + votação, com *timelock* e *multisig*.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Empréstimo DeFi | Garantia > dívida · oráculo · liquidação automática |
| LTV | Dívida ÷ garantia |
| Indicador de saúde | (Garantia × limite) ÷ dívida · < 1 liquida |
| AMM | x × y = k · ordem grande = preço pior |
| *Impermanent loss* | Custo de oportunidade do **LP** |
| Seguro | Seguradora autorizada · Lei 15.040/2024 |
| Paramétrico | Gatilho · risco de base |
| Imóvel | Propriedade só com registro (CC 1.245) |
| DAO | Código + votação · votar ≠ executar |

### Cadeia lógica

**Regra verificável → smart contract → dado do oráculo → execução automática → riscos técnicos, jurídicos e de governança**

### Frase central da aula

> **O código executa a regra; o dado, a liquidez, o contrato e a lei continuam decidindo o resultado.**

- "Voltando ao investidor do começo: o empréstimo foi do código, a troca foi da pool, o seguro foi da seguradora e a sala comercial depende do cartório. Na próxima aula: tokenização."

---

## Nota de verificação

- **Base:** aula do repositório (Lei 15.040/2024 e Código Civil conferidos em 29/09/2026), roteiro em PDF do lote e APOSTILA-CPA p. 542. Textos **não reabertos nesta sessão**.
- **Acréscimos (➕):**
  - kit HP12C e dois exemplos (LTV e indicador de saúde; x × y = k com impacto de preço), hipotéticos e sem taxa;
  - questões 2 e 3;
  - tabelas de certo × errado.
- **Retirados:** nomes de protocolos reais e o exemplo da apostila ligado a um conflito armado real.
