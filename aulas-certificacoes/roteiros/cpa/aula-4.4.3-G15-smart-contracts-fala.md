# Roteiro de fala — Aula CPA: Smart Contracts, Componentes, Autoexecução e Plataformas

**Base:**
- **Programa Detalhado CPA** (ANBIMA, v1.2, rev. 04/06/2025, vigência 01/01/2026), itens 4.4.3.1 a 4.4.3.4;
- APOSTILA-CPA, p. 541–542;
- roteiro **4.4-A** (DeFi, blockchain e smart contracts), do qual esta aula é a versão de 15 min só com tópicos;
- aula **G14** (finanças tradicionais × DeFi, vantagens e blockchain), que antecede esta.

CPA 4.4.3 · 4.4.3.1 · 4.4.3.2 · 4.4.3.3 · 4.4.3.4 · Módulo 4 · **15 min** · Aula G15 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ✏️ = correção da fonte · ⌨️ = teclas da HP12C · 🖥️ = visor.

---

## Bastidor — antes de gravar

### 🔇 Metáfora única desta aula

**A máquina de venda automática.** Você escolhe, paga o valor certo e a máquina libera o produto, sem vendedor. O smart contract é essa máquina dentro de uma blockchain: a regra é o código, o estoque é o saldo registrado, e o livro de vendas é a blockchain.

**Onde a metáfora falha:** a máquina não depende de nada fora dela. Um smart contract depende de dados do mundo real, como preço ou chuva, que chegam por um oráculo. Se o oráculo errar, o contrato executa certo com dado errado. Além disso, a máquina pode ser trocada; em regra, o contrato implantado não pode ser alterado.

### 🔇 Formato

- Direto aos tópicos do PD, sem as demais etapas.
- Fios condutores: a **máquina de venda** (conceito), um **seguro de atraso de voo** (oráculo) e um **empréstimo com garantia** (autoexecução, com HP12C).

### 🔇 Checagem de escopo (PD × materiais)

| Subitem do PD | Apostila | Tratamento |
| --- | --- | --- |
| 4.4.3.1 Conceito de smart contracts | p. 541 | Conferido; imutabilidade e "Code is Law" com ressalva |
| 4.4.3.2 Componentes e funcionamento | **Ausente** | Coberto pelo roteiro 4.4-A (código, estado, endereço, transação, gas, oráculo, carteira) |
| 4.4.3.3 Contratos autoexecutáveis | p. 541 | Conferido; acrescido o limite do "gatilho" |
| 4.4.3.4 Plataformas de smart contracts | **Ausente** | Coberto pelo roteiro 4.4-A, **simplificado** para o nível da CPA |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Apostila p. 541 | Smart contract "não pode ser alterado" | **Resposta de prova:** imutável depois de implantado. **Ressalva:** é o padrão; há desenhos com atualização ou pausa por governança. Roteiro 4.4-A (Ethereum.org) |
| 2 | Apostila p. 541 | Segurança: "a execução é garantida pela rede" | A rede garante a **execução** como foi escrita. Não garante que o código esteja certo nem que o dado de entrada seja verdadeiro. Roteiro 4.4-A (NIST) |
| 3 | Apostila p. 541–542 | "Code is Law": o código é a autoridade final, "sem apelação" | Expressão de mercado sobre execução literal. **Juridicamente o código não está acima da lei.** Base: Lei 14.478/2022; Parecer CVM 40/2022 |
| 4 | Apostila p. 541 | Smart contract elimina a necessidade de intermediário | Mesma ressalva da G14: reduz a dependência, não a zera |
| 5 | Apostila p. 539–542 | Subitens numerados como "4.3" | Numeração do PD: 4.4.3.1 a 4.4.3.4 |

### 🔇 Dados do exemplo (empréstimo com garantia)

| Item | Valor |
| --- | --- |
| Empréstimo | R$ 10.000,00 |
| Garantia depositada | R$ 15.000,00 (150% do empréstimo) |
| Regra do contrato | Liquida se a garantia valer menos de **120%** do empréstimo |
| Valor-limite da garantia | 10.000 × 120% = **R$ 12.000,00** |
| Queda que dispara a liquidação | (12.000 − 15.000) ÷ 15.000 = **−20%** |

Valores e percentuais são hipóteses didáticas; cada protocolo define os seus.

### 🔇 Cronograma

| Tópico | Tempo |
| --- | --- |
| 3.1 Conceito de smart contracts | 3 min |
| 3.2 Componentes e funcionamento | 4,5 min |
| 3.3 Contratos autoexecutáveis | 3,5 min |
| 3.4 Plataformas de smart contracts | 4 min |
| **Total** | **15 min** |

---

## 3. Explicação dos tópicos — 15 min

### 3.1 Conceito de smart contracts — 3 min · CPA 4.4.3 e 4.4.3.1

> **Objetivo deste bloco:** ao fim, o aluno consegue definir smart contract e dizer por que ele não "pensa", só executa.

- **A definição**
  - "Smart contract, ou contrato inteligente, é um contrato digital autoexecutável escrito em linhas de código. As regras e as consequências do acordo ficam programadas e são executadas automaticamente quando as condições predefinidas são cumpridas."
- **A máquina de venda automática**
  - "A máquina de venda não precisa de vendedor. Você escolhe, paga o valor certo e ela libera. O smart contract é essa máquina dentro de uma blockchain: a regra é o código, o estoque é o saldo registrado e o livro de vendas é a blockchain."
- **Contrato de papel × contrato inteligente**
  - "No contrato de papel, uma pessoa interpreta a cláusula, e se houver divergência, procura-se a Justiça. No smart contract, a cláusula é uma instrução: se acontecer isso, faça aquilo. Não há interpretação, só execução."

| Característica | Ressalva |
| --- | --- |
| **Imutabilidade** | É o padrão; alguns desenhos permitem atualização ou pausa por governança |
| **Transparência** | Público não significa compreensível nem seguro |
| **Segurança** | A rede garante a **execução**, não que o código esteja certo |
| **"Code is Law"** | Expressão de mercado; **não substitui a lei** |

- ✏️ **"Code is Law"**
  - "O código é, para o mercado, a autoridade final, sem apelação. Juridicamente, no Brasil, o código não está acima da lei: proteção do consumidor, lavagem de dinheiro, tributação e a competência da CVM continuam valendo."
- **Erro comum:** achar que smart contract é uma inteligência artificial. É código programado: não pensa, executa.

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Smart contract é uma inteligência artificial" | Errado | É **código programado**: não pensa, executa |
| "As regras de um smart contract são programadas no código" | Certo | Definição de smart contract |
| "Uma vez implantado, o smart contract em regra não pode ser alterado" | Certo | Imutabilidade (padrão) |

> **Smart contract é um contrato em código: não pensa, executa.**

**🔗 Ponte:** "De que ele é feito? Os componentes."

---

### 3.2 Componentes e funcionamento dos smart contracts — 4,5 min · CPA 4.4.3.2

> **Objetivo deste bloco:** ao fim, o aluno consegue identificar cada componente do smart contract e dizer quem faz o quê no fluxo.

- **Os componentes**

| Componente | Função |
| --- | --- |
| **Código** | As regras: depositar, sacar, trocar, liquidar |
| **Estado** | Os dados guardados: saldos, garantias, dívidas |
| **Endereço** | Onde o contrato "mora" na blockchain |
| **Transação** | Mensagem assinada que aciona uma função |
| **Gas** | Custo de processamento pago à rede (não é juros) |
| **Oráculo** | Traz **dados do mundo real** (preço, índice, clima) para o contrato |
| **Carteira** | Guarda a chave e **assina**; não executa a regra |

- **O fluxo**
  - "O código é implantado e ganha um endereço. O usuário assina uma transação na carteira. Os nós da rede executam o contrato. O consenso confirma. O estado é atualizado: o saldo muda, a garantia fica registrada."
- **O gas, com cuidado**
  - "A cada execução, a rede cobra gas pelo processamento. Operação mais complexa, mais gas. Rede congestionada, mais caro. Se a transação falhar por falta de gas, a execução é interrompida, mas a taxa gasta não volta."
- **O oráculo, peça-chave**
  - "O contrato não enxerga o mundo de fora. Imagine um seguro que paga a indenização se o voo atrasar. Quem avisa o contrato que o voo atrasou? O oráculo. Se o oráculo errar, o contrato executa certo com o dado errado."
  - "Por isso protocolos sérios usam mais de uma fonte de dados. Oráculo é um ponto de atenção para quem avalia o risco."
- **Erro comum:** achar que o oráculo valida os blocos. Ele traz dados externos; quem valida são os nós.

| Quem faz o quê | Papel |
| --- | --- |
| **Usuário** | Decide e assina |
| **Carteira** | Guarda a chave e assina |
| **Nós** | Validam, armazenam e propagam |
| **Oráculo** | Leva o dado de fora |
| **Contrato** | Executa a regra |

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O oráculo valida os blocos da rede" | Errado | Oráculo **traz dados externos**; quem valida são os nós |
| "A carteira executa as regras do contrato" | Errado | A carteira **assina**; a rede executa |
| "Gas é o custo de processamento da operação na rede" | Certo | Definição de gas |
| "Se o oráculo informar um dado errado, o contrato executa a regra com o dado errado" | Certo | O contrato não verifica o mundo de fora |

> **Código mais estado, na blockchain; o oráculo traz o mundo de fora.**

**🔗 Ponte:** "Com os dados certos, o contrato roda sozinho. É a autoexecução."

---

### 3.3 Contratos autoexecutáveis — 3,5 min · CPA 4.4.3.3

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o ponto de liquidação de um empréstimo com garantia e explicar o que o contrato faz sem julgar.

- **A lógica "se… então…"**
  - "Se as condições programadas forem cumpridas, então o resultado é executado automaticamente, sem alguém interpretar e fazer cada etapa à mão."
- **O empréstimo com garantia**
  - "Um investidor deposita 15 mil reais em tokens de garantia e toma um empréstimo de 10 mil. A garantia é 150% do empréstimo. O contrato tem uma regra: se a garantia valer menos de 120% do empréstimo, liquida."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `10000` `ENTER` `120` `%` | 🖥️ 12.000,00 | Valor-limite da garantia |
| 2 | ⌨️ `15000` `ENTER` `12000` `Δ%` | 🖥️ −20,00 | Queda da garantia que dispara a liquidação |

  - "Se os tokens caírem 20%, a garantia chega a 12 mil e o contrato liquida a posição sozinho. Ninguém telefona, ninguém avisa antes. O contrato cumpre a regra no momento em que a condição acontece."
  - 🔇 Valores e percentuais hipotéticos; cada protocolo define os seus. O contrato depende do **oráculo** para saber o preço da garantia.

| Vantagens | Limites |
| --- | --- |
| Menos intervenção manual | Rígido diante do imprevisto |
| Execução padronizada | Erro de código também é executado |
| Rastreável | Difícil de reverter |
| Liquidação programada | Depende do oráculo e de um **gatilho** (uma transação que chame a função) |

  - "Aqui mora o alerta: a execução é literal e inevitável. Um erro de programação pode ter consequências financeiras irreversíveis."
- **Erro comum:** achar que o contrato interrompe a execução se o resultado parecer injusto. Ele executa a regra literal.

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O smart contract executa a regra quando as condições predefinidas são cumpridas" | Certo | Autoexecução |
| "Se o resultado for injusto, o smart contract interrompe sozinho a execução" | Errado | Executa a regra **literal**, justa ou não |
| "A liquidação automática de garantias é um exemplo de contrato autoexecutável" | Certo | Se a condição acontece, a regra roda |

> **Autoexecutável cumpre a regra quando o gatilho chega; não julga se é justo.**

**🔗 Ponte:** "Em que redes esses contratos rodam?"

---

### 3.4 Plataformas de smart contracts — 4 min · CPA 4.4.3.4

> **Objetivo deste bloco:** ao fim, o aluno consegue separar plataforma, protocolo e smart contract, e dizer o que pesa na escolha de uma plataforma.

- **O que é plataforma**
  - "Plataforma é a blockchain que permite implantar e executar smart contracts. Ela define o consenso, o ambiente de execução, as taxas e as linguagens."

| Plataforma | Ponto de destaque |
| --- | --- |
| **Ethereum** | A principal plataforma de smart contracts; ambiente de execução **EVM**; taxas em gas |
| **Redes compatíveis com EVM** | Rodam contratos no padrão Ethereum, com **consenso e segurança próprios** |
| **Redes de segunda camada** | Processam operações fora da rede principal para reduzir custo e depois registram o resultado nela |
| **Outras redes** | Arquiteturas diferentes (como Solana e Cardano); o conceito de smart contract se adapta |

- **O que é EVM**
  - "EVM, Máquina Virtual do Ethereum, é o ambiente que executa o código dos contratos. Por ser um padrão, um contrato escrito para ele pode rodar em várias redes compatíveis."
- **Três camadas**

| Camada | O que é |
| --- | --- |
| **Plataforma** | A infraestrutura onde o código roda |
| **Protocolo DeFi** | A aplicação financeira |
| **Smart contract** | O código com as regras do protocolo |

- **O que olhar na escolha**
  - "Custo por operação, velocidade, segurança, quantidade de usuários e a maturidade da rede. Uma rede compatível com EVM pode cobrar menos taxa, mas ter menos participantes validando, o que muda o risco."
- **Atualização regulatória (fora destes subitens)**
  - 🔇 "Usar blockchain não afasta a lei. A Lei 14.478/2022 exclui do conceito de ativo virtual os valores mobiliários, que seguem com a CVM. E o Banco Central regulamentou as prestadoras de serviços de ativos virtuais nas Resoluções BCB 519, 520 e 521, de 2025, em vigor desde 02/02/2026." **Status: conferido em fontes secundárias; texto das resoluções não reaberto.**
- **Erro comum:** achar que, se a rede é compatível com EVM, ela é a própria Ethereum. Usa o padrão, mas tem consenso e segurança próprios.

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Rede compatível com EVM é a própria Ethereum" | Errado | Usa o padrão, mas tem **consenso e segurança próprios** |
| "Plataforma e protocolo DeFi são a mesma coisa" | Errado | Infraestrutura × aplicação |
| "Ethereum é a principal plataforma de smart contracts" | Certo | Plataforma de referência |
| "Um contrato escrito para a EVM pode rodar em redes compatíveis" | Certo | Padrão de execução |

> **Plataforma é a infraestrutura, protocolo é a aplicação, smart contract é a regra que a aplicação executa.**

- 🔇 **Fechamento:** "Smart contract é código que executa a regra combinada, com estado, oráculo e gas; roda numa plataforma; e o código não substitui a lei." Próxima aula do bloco: aplicações práticas (empréstimos, DEX, seguros e imóveis).

---

## Lista de pegadinhas com nome

1. **Pegadinha da IA** — "Smart contract é inteligência artificial." Errado: é código programado; executa, não pensa.
2. **Pegadinha do oráculo validador** — "O oráculo valida os blocos." Errado: traz dados externos; quem valida são os nós.
3. **Pegadinha do código acima da lei** — "Code is Law: o código não se submete à lei." Errado: juridicamente, a lei continua valendo.
4. **Pegadinha da rede EVM** — "Rede compatível com EVM é a própria Ethereum." Errado: tem consenso e segurança próprios.

---

## Nota de verificação

- Programa Detalhado CPA (v1.2): itens 4.4.3.1 a 4.4.3.4 lidos no texto do PD do repositório.
- Apostila CPA, p. 541–542: definição, características e princípio "Code is Law".
- **Roteiro 4.4-A** (35 min, do repositório): componentes, plataformas e correções, conferidos contra o roteiro em PDF e a aula do repositório. **Não reabertos nesta sessão:** Ethereum.org e NIST, citados nele.
- **Res. BCB 519, 520 e 521/2025:** publicadas em 10/11/2025, em vigor desde 02/02/2026, conforme fontes secundárias. **Fontes divergem sobre qual resolução trata de qual tema**, então a fala cita só as três em conjunto.
- **Lei 14.478/2022 e Parecer de Orientação CVM 40/2022:** conforme a aula do repositório. **Não reabertos nesta sessão.**
- **Conhecimento geral, sem fonte aberta nesta sessão:** EVM como padrão de execução; redes de segunda camada; Solana e Cardano como exemplos de outras redes; gas gasto não retorna se a transação falha.
- **Convenções sem força normativa:** o seguro de atraso de voo, o empréstimo com garantia de 150% e liquidação aos 120%, a tabela de componentes e a classificação de plataformas.
- **Cálculos conferidos em Python nesta revisão:** 10.000 × 120% = 12.000; (12.000 − 15.000) ÷ 15.000 = −20%.
- Revisão de estrutura: metáfora única (máquina de venda automática) com o ponto de falha, caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
