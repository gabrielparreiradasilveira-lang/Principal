# Roteiro de fala — Aula CPA: DEXs, Seguros e Apólices Automatizadas, Imobiliário e Compra e Venda de Propriedades

**Base:**
- **Programa Detalhado CPA** (ANBIMA, v1.2, rev. 04/06/2025, vigência 01/01/2026), itens 4.4.3.7, 4.4.3.8, 4.4.3.8.1, 4.4.3.9 e 4.4.3.9.1;
- roteiro **4.4-B** (aplicações de smart contracts, 40 min), do qual esta aula é o recorte de 15 min só com tópicos;
- aulas **G14** e **G15** (DeFi, blockchain e smart contracts), que esta aula supõe conhecidas;
- Lei 15.040/2024 (Marco Legal dos Seguros) e Código Civil, conforme conferidos na aula do repositório `aulas/cpa/aula-4.4-B-aplicacoes-smart-contracts-daos/aula.md`.

CPA 4.4.3.7 · 4.4.3.8 · 4.4.3.8.1 · 4.4.3.9 · 4.4.3.9.1 · Módulo 4 · **15 min** · Aula G16 do plano de gravação · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ✏️ = correção da fonte · ➕ = acréscimo desta versão · 🔗 = ponte · ⌨️ = teclas da HP12C · 🖥️ = visor.

---

## Bastidor — antes de gravar

### 🔇 Formato

- Direto aos tópicos do PD, sem as demais etapas.
- Fio condutor: a **máquina de venda automática** das aulas anteriores, agora em três lojas do shopping DeFi: a casa de câmbio (DEX), a corretora de seguros e a imobiliária.

### 🔇 Checagem de escopo (PD × materiais)

| Subitem do PD | PDF do lote | Apostila | Tratamento |
| --- | --- | --- | --- |
| 4.4.3.7 Exchanges descentralizadas (DEXs) | Roteiro p. 15–20 | **Ausente** | Coberto; protocolo real trocado por conceito genérico |
| 4.4.3.8 Seguros | Roteiro p. 20–23 | **Ausente** | Coberto; conferido pela Lei 15.040/2024 |
| 4.4.3.8.1 Apólices automatizadas | Roteiro p. 23–27 | **Ausente** | Coberto |
| 4.4.3.9 Imobiliário | Roteiro p. 27–30 | **Ausente** | Coberto |
| 4.4.3.9.1 Compra e venda de propriedades | Roteiro p. 30–32 | **Ausente** | Coberto; conferido pelo Código Civil |

🔇 A apostila (p. 539–542) só trata de DeFi, blockchain, smart contracts e DAOs. Esta aula depende do material em PDF do lote e das fontes oficiais.

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto | Base |
| --- | --- | --- | --- | --- |
| 1 | Roteiro p. 15–17 | DEX com nome de **protocolo real** | Ensinado como **conceito genérico** de AMM; x × y = k é **ilustração** do modelo clássico. Há DEXs com outras fórmulas e com livro de ofertas | Padrão do projeto |
| 2 | Roteiro p. 22–27 | "Apólice automatizada" | **Não é categoria jurídica**: continua sendo contrato de seguro, feito por **seguradora autorizada** | Lei 15.040/2024, arts. 1º e 2º |
| 3 | Uso comum | Token imobiliário "transfere a propriedade" | A propriedade só se transfere pelo **registro do título no Registro de Imóveis** | Código Civil, art. 1.245 |
| 4 | Uso comum | Pool de liquidez "protegida" | Pool **não é depósito** e **não tem garantia do FGC** | Aula do repositório |
| 5 | PD 4.4.3.7 a 4.4.3.9.1 | Sem numeração diferente da apostila | Numeração do PD mantida | PD CPA |

### 🔇 Dados dos exemplos (pool da DEX)

| Item | Valor |
| --- | --- |
| Pool | 100 tokens A e 10.000 tokens B → preço de 100 B por A; **k = 1.000.000** |
| Ordem grande | Paga 1.000 B → recebe **9,09 A** → preço médio **110 B por A** (10% acima) |
| Ordem pequena | Paga 100 B → recebe **0,99 A** → preço médio **101 B por A** (1% acima) |

Sem taxa, por simplicidade. Valores hipotéticos.

### 🔇 Cronograma

| Tópico | Tempo |
| --- | --- |
| 3.1 Exchanges descentralizadas (DEXs) | 6 min |
| 3.2 Seguros e apólices automatizadas | 4,5 min |
| 3.3 Imobiliário e compra e venda de propriedades | 4,5 min |
| **Total** | **15 min** |

---

## 3. Explicação dos tópicos — 15 min

### 3.1 Exchanges descentralizadas (DEXs) — 6 min · CPA 4.4.3.7

- **O que é**
  - "DEX é uma bolsa descentralizada: um protocolo de troca de criptoativos feito por smart contracts, em geral sem uma corretora guardando os ativos. Muitas usam o formador de mercado automático, o AMM."

| Conceito | O que é |
| --- | --- |
| **AMM** | O preço vem de uma **fórmula**, e não de ordens casadas |
| **Pool de liquidez** | Reserva com **dois tokens** contra a qual o usuário troca |
| **x × y = k** | x e y são as reservas; k é constante. Um lado sobe, o outro cai, o preço muda |
| **Provedor de liquidez (LP)** | Deposita os dois tokens e recebe parte das **taxas** |
| ***Swap*** | A troca de um token por outro na pool |
| ***Price impact*** | Mudança de preço causada pelo **tamanho da própria ordem** |
| ***Slippage*** | Diferença **total** entre o preço esperado e o executado |
| ***Impermanent loss*** | Perda de oportunidade do **LP** frente a só **guardar** os tokens |
| ***Front-running*** | Alguém passa **na frente** da ordem vista na rede e piora o preço da vítima |

- **O exemplo da pool**
  - "A pool tem 100 tokens A e 10 mil tokens B. O preço é 100 B por A. Multiplicando, k é 1 milhão, e esse número não pode mudar. Se eu coloco 1.000 de B, a pool fica com 11 mil de B. Para k continuar 1 milhão, sobram 1 milhão dividido por 11 mil: 90,91 de A. Eu levo a diferença: 9,09 de A."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `100` `ENTER` `10000` `×` `STO` `1` | 🖥️ 1.000.000,00 | k da pool, guardado |
| 2 | ⌨️ `100` `ENTER` `RCL` `1` `11000` `÷` `−` | 🖥️ 9,09 | A recebido na ordem grande |
| 3 | ⌨️ `STO` `2` `1000` `RCL` `2` `÷` | 🖥️ 110,00 | Preço médio: 110 B por A, 10% acima |
| 4 | ⌨️ `100` `ENTER` `RCL` `1` `10100` `÷` `−` | 🖥️ 0,99 | A recebido na ordem pequena (100 B) |
| 5 | ⌨️ `STO` `3` `100` `RCL` `3` `÷` | 🖥️ 101,00 | Preço médio: 101 B por A, 1% acima |

  - "Paguei 1.000 por 9,09: preço médio de 110. A tela mostrava 100. Esses 10% são o impacto de preço da minha própria ordem. Com uma ordem de só 100 de B, o preço médio é 101: impacto de 1%. Quanto maior a ordem em relação à pool, pior o preço."
  - 🔇 O passo 2 usa a pilha da HP12C: `100 ENTER` coloca o saldo atual de A, `RCL 1` busca k, `11000 ÷` divide e `−` subtrai. Valores hipotéticos; x × y = k é ilustração do modelo clássico.

- **DEX × exchange centralizada**

| DEX | Exchange centralizada |
| --- | --- |
| Protocolo e smart contracts | Empresa e sistemas próprios |
| Ativos na **carteira do usuário** | Ativos sob **custódia** da plataforma |
| Pool (AMM) ou livro na blockchain | Livro de ofertas central |
| Riscos de código, oráculo, rede e carteira | Riscos da empresa, da custódia e de contraparte |

- **O alerta**
  - ✏️ "Pool de liquidez não é depósito bancário. Não há garantia do FGC. O risco do provedor de liquidez é o impermanent loss e também o de código."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Price impact e slippage são sinônimos" | Errado | Impacto é efeito da **própria ordem**; *slippage* é a diferença **total** |
| "Impermanent loss é risco do trader" | Errado | É risco do **provedor de liquidez** |
| "Pool de liquidez tem garantia do FGC" | Errado | Não é depósito, **sem FGC** |
| "Na DEX com AMM, a fórmula da pool define o preço" | Certo | Modelo clássico |

> **Na DEX com AMM, o usuário troca contra a pool; a fórmula dá o preço, e o tamanho da ordem move esse preço.**

**🔗 Ponte:** "Agora, uma aplicação em que a lei pesa muito: o seguro."

---

### 3.2 Seguros e apólices automatizadas — 4,5 min · CPA 4.4.3.8 e 4.4.3.8.1

- **O contrato de seguro pela lei**
  - "Pela Lei 15.040, de 2024, o Marco Legal dos Seguros, no contrato de seguro a seguradora, mediante o prêmio, garante interesse legítimo do segurado contra riscos predeterminados. E só entidades autorizadas podem fazer contratos de seguro. Smart contract não é seguradora."

- **Dois modelos**

| Tipo | Como paga | Ponto de atenção |
| --- | --- | --- |
| **Tradicional (indenizatório)** | Depois do aviso e da **regulação do sinistro**, que apura o dano | Mais lento; paga o dano apurado |
| **Paramétrico** | Quando um **índice objetivo** atinge o **gatilho** (chuva, vento, temperatura) | **Risco de base**: o pagamento pode ser **maior ou menor** que o prejuízo |

- **Apólice automatizada**
  - "Apólice automatizada é expressão de mercado: parte do fluxo roda por software ou smart contract. Cotação, emissão, cobrança, conferência do índice e pagamento. Mas juridicamente continua sendo contrato de seguro, com seguradora autorizada, cobertura, exclusões e direito de contestar."

- **O fluxo**
  - "Apólice agrícola, mais chuva abaixo do limite, mais fonte de dados válida, mais vigência ativa: pagamento paramétrico."
  - "O oráculo, que vimos na G15, é a peça-chave. Ele leva o dado de chuva até o contrato. Se o oráculo errar, o contrato paga certo com o dado errado."

| Passo da apólice | Quem faz |
| --- | --- |
| Contratação e prêmio | Segurado e seguradora autorizada |
| Medição do índice | Fonte de dados / oráculo |
| Conferência do gatilho | Smart contract |
| Pagamento | Automático, se o gatilho for atingido |
| Contestação | Direito do segurado, **continua existindo** |

- ✏️ "A expressão 'apólice automatizada' não é uma categoria jurídica nova. É tecnologia aplicada a um contrato que a lei já regula."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Seguro paramétrico paga exatamente o prejuízo" | Errado | Paga pelo **gatilho**; há **risco de base** |
| "Com smart contract, qualquer empresa pode oferecer seguro" | Errado | Só **entidade autorizada** (Lei 15.040/2024, art. 2º) |
| "Apólice automatizada é uma nova espécie jurídica de contrato" | Errado | É **tecnologia** aplicada ao contrato de seguro |

> **No paramétrico, o gatilho é objetivo; a indenização pode não ser igual ao dano.**

**🔗 Ponte:** "Outra área em que o código esbarra na lei: imóveis."

---

### 3.3 Imobiliário e compra e venda de propriedades — 4,5 min · CPA 4.4.3.9 e 4.4.3.9.1

- **Onde o smart contract ajuda**
  - "No imobiliário, o código ajuda em pagamento condicionado, o chamado escrow; na distribuição de aluguéis; na tokenização de direitos econômicos; e na governança de imóveis coletivos."

| Aplicação | O que o contrato faz |
| --- | --- |
| **Escrow** | Retém o pagamento e só libera quando a condição é cumprida |
| **Aluguel** | Distribui o rendimento entre os participantes |
| **Tokenização** | Representa **direitos** ligados ao imóvel, e não o imóvel |
| **Governança** | Registra votações de condôminos ou cotistas |

- **O que a lei exige**

| Artigo do Código Civil | Regra |
| --- | --- |
| **481** | Na compra e venda, um se obriga a **transferir o domínio** e o outro a **pagar o preço** |
| **482** | A compra e venda pura é **perfeita** quando as partes concordam sobre **objeto e preço** |
| **108** | **Escritura pública** é essencial para direitos reais sobre imóveis acima de **30 salários mínimos** (salvo lei em contrário) |
| **1.245** | A propriedade só se transfere pelo **registro do título no Registro de Imóveis** |

- **A sequência**
  - "Acordo sobre objeto e preço, escritura quando exigida, título, registro, e só aí a propriedade muda de dono. O smart contract pode automatizar etapas, como o pagamento condicionado, mas não pula o registro."

- **O que o token é, e o que não é**

| O token pode ser | O token **não é**, sozinho |
| --- | --- |
| Direito contratual, participação econômica, recebível, cota, direito a renda | Matrícula, escritura, propriedade registrada, posse ou garantia real |

  - 🔇 Tokens que representam participação em empreendimento podem ser valores mobiliários e, nesse caso, ficam sob a CVM. Tratado na aula de tokenização.

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Token imobiliário registrado em blockchain transfere a propriedade" | Errado | Propriedade só com **registro** (CC art. 1.245) |
| "Smart contract dispensa a escritura pública" | Errado | CC art. 108 continua valendo |
| "A compra e venda é perfeita quando as partes concordam sobre o objeto e o preço" | Certo | CC art. 482 |

> **Tokenizar o direito não é transferir o domínio: a propriedade passa pelo registro.**

- 🔇 Fechamento em uma frase (sem etapa de revisão): "Na DEX, a fórmula dá o preço e a ordem grande o piora; no seguro, o smart contract é tecnologia e a seguradora autorizada continua sendo necessária; no imóvel, a propriedade passa pelo registro." Próxima aula do bloco: governança descentralizada e DAOs.

---

## Nota de verificação

- **Programa Detalhado CPA** (v1.2, rev. 04/06/2025, vigência 01/01/2026): itens 4.4.3.7 a 4.4.3.9.1 lidos no texto do PD do repositório.
- **Apostila CPA**, p. 539–542: sem os itens desta aula (só DAOs, no item seguinte).
- **Roteiro 4.4-B** (40 min, do repositório): conteúdo e correções conferidos em 29/09/2026 contra o roteiro em PDF, a Lei 15.040/2024 (arts. 1º e 2º) e o Código Civil (arts. 108, 481, 482 e 1.245). **Textos legais não reabertos nesta sessão.**
- **Citado de memória, sem reabrir o texto:** a observação de que tokens de participação em empreendimento podem ser valores mobiliários sob a CVM (tema da aula de tokenização).
- **Convenções sem força normativa:** o exemplo da pool (100 A, 10.000 B, sem taxa), a lista de aplicações imobiliárias e o fluxo da apólice agrícola.
- **Cálculos conferidos em Python:** k = 100 × 10.000 = 1.000.000; 1.000.000 ÷ 11.000 = 90,91; 100 − 90,91 = 9,09; 1.000 ÷ 9,09 = 110; 1.000.000 ÷ 10.100 = 99,01 → 0,99 A; 100 ÷ 0,99 = 101.
- **Acréscimos (➕):** tabela do fluxo da apólice e tabela das aplicações imobiliárias; a ligação com o oráculo da G15.
