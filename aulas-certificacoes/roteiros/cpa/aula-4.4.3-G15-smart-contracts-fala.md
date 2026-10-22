# Roteiro de fala — Aula CPA: Smart Contracts, Componentes, Autoexecução e Plataformas

**Base:**
- **Programa Detalhado CPA** (ANBIMA, v1.2, rev. 04/06/2025, vigência 01/01/2026), itens 4.4.3.1 a 4.4.3.4;
- APOSTILA-CPA, p. 541–542;
- roteiro **4.4-A** (DeFi, blockchain e smart contracts), do qual esta aula é a versão de 10 min só com tópicos;
- aula **G14** (finanças tradicionais × DeFi, vantagens e blockchain), que antecede esta.

CPA 4.4.3 · 4.4.3.1 · 4.4.3.2 · 4.4.3.3 · 4.4.3.4 · Módulo 4 · **10 min** · Aula G15 do plano de gravação · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ✏️ = correção da fonte · ➕ = acréscimo desta versão · 🔗 = ponte · ⌨️ = teclas da HP12C · 🖥️ = visor.

---

## Bastidor — antes de gravar

### 🔇 Formato

- Direto aos tópicos do PD, sem as demais etapas.
- Fio condutor: uma **máquina de venda automática**, para mostrar que o contrato executa a regra sem vendedor, e um **seguro de atraso de voo**, para mostrar o oráculo.

### 🔇 Checagem de escopo (PD × materiais)

| Subitem do PD | Apostila | Tratamento |
| --- | --- | --- |
| 4.4.3.1 Conceito de smart contracts | p. 541 | Conferido; imutabilidade e "Code is Law" com ressalva |
| 4.4.3.2 Componentes e funcionamento | **Ausente** | Coberto pelo roteiro 4.4-A (código, estado, endereço, transação, gas, oráculo, carteira) |
| 4.4.3.3 Contratos autoexecutáveis | p. 541 | Conferido; acrescido o limite do "gatilho" |
| 4.4.3.4 Plataformas de smart contracts | **Ausente** | Coberto pelo roteiro 4.4-A, **simplificado** para o nível da CPA |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto | Base |
| --- | --- | --- | --- | --- |
| 1 | Apostila p. 541 | Smart contract "não pode ser alterado" | **Resposta de prova:** imutável depois de implantado. **Ressalva:** é o padrão; há desenhos com atualização ou pausa por governança | Roteiro 4.4-A (Ethereum.org) |
| 2 | Apostila p. 541 | Segurança: "a execução é garantida pela rede" | A rede garante a **execução** como foi escrita. Não garante que o código esteja certo nem que o dado de entrada seja verdadeiro | Roteiro 4.4-A (NIST) |
| 3 | Apostila p. 541–542 | "Code is Law": o código é a autoridade final, "sem apelação" | Expressão de mercado sobre execução literal. **Juridicamente o código não está acima da lei** | Lei 14.478/2022; Parecer CVM 40/2022 |
| 4 | Apostila p. 541 | Smart contract elimina a necessidade de intermediário | Mesma ressalva da G14: reduz a dependência, não a zera | Roteiro 4.4-A |
| 5 | Apostila p. 539–542 | Subitens numerados como "4.3" | Numeração do PD: 4.4.3.1 a 4.4.3.4 | PD CPA |

### 🔇 Cronograma

| Tópico | Tempo |
| --- | --- |
| 3.1 Conceito de smart contracts | 2 min |
| 3.2 Componentes e funcionamento | 3 min |
| 3.3 Contratos autoexecutáveis | 2 min |
| 3.4 Plataformas de smart contracts | 3 min |
| **Total** | **10 min** |

---

## 3. Explicação dos tópicos — 10 min

### 3.1 Conceito de smart contracts — 2 min · CPA 4.4.3 e 4.4.3.1 · Apostila p. 541

- **A definição**
  - "Smart contract, ou contrato inteligente, é um contrato digital autoexecutável escrito em linhas de código. As regras e as consequências do acordo ficam programadas e são executadas automaticamente quando as condições predefinidas são cumpridas."

- **A máquina de venda automática**
  - "A máquina de venda não precisa de vendedor. Você escolhe, paga o valor certo e ela libera. O smart contract é essa máquina dentro de uma blockchain: a regra é o código, o estoque é o saldo registrado e o livro de vendas é a blockchain."

| Característica da apostila | Ressalva |
| --- | --- |
| **Imutabilidade** | É o padrão; alguns desenhos permitem atualização ou pausa por governança |
| **Transparência** | Público não significa compreensível nem seguro |
| **Segurança** | A rede garante a **execução**, não que o código esteja certo |
| **"Code is Law"** | Expressão de mercado; **não substitui a lei** |

- ✏️ **"Code is Law"**
  - "A apostila diz que o código é a autoridade final, sem apelação. É o que o mercado diz. Juridicamente, no Brasil, o código não está acima da lei: proteção do consumidor, lavagem de dinheiro, tributação e a competência da CVM continuam valendo."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Smart contract é uma inteligência artificial" | Errado | É **código programado**: não pensa, executa |
| "As regras de um smart contract são programadas no código" | Certo | Apostila p. 541 |

> **Smart contract é um contrato em código: não pensa, executa.**

**🔗 Ponte:** "De que ele é feito? Os componentes."

---

### 3.2 Componentes e funcionamento dos smart contracts — 3 min · CPA 4.4.3.2

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
  - "O código é implantado. O usuário assina uma transação na carteira. A rede executa o contrato. O consenso confirma. O estado é atualizado."

- **O oráculo, peça-chave**
  - "O contrato não enxerga o mundo de fora. Imagine um seguro que paga a indenização se o voo atrasar. Quem avisa o contrato que o voo atrasou? O oráculo. Se o oráculo errar, o contrato executa certo com o dado errado."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O oráculo valida os blocos da rede" | Errado | Oráculo **traz dados externos**; quem valida são os nós |
| "A carteira executa as regras do contrato" | Errado | A carteira **assina**; a rede executa |
| "Gas é o custo de processamento da operação na rede" | Certo | Roteiro 4.4-A |

> **Código mais estado, na blockchain; o oráculo traz o mundo de fora.**

**🔗 Ponte:** "Com os dados certos, o contrato roda sozinho. É a autoexecução."

---

### 3.3 Contratos autoexecutáveis — 2 min · CPA 4.4.3.3 · Apostila p. 541

- **A lógica "se… então…"**
  - "Se as condições programadas forem cumpridas, então o resultado é executado automaticamente, sem alguém interpretar e fazer cada etapa à mão. Garantia suficiente mais transação válida: empréstimo liberado."

| Vantagens | Limites |
| --- | --- |
| Menos intervenção manual | Rígido diante do imprevisto |
| Execução padronizada | Erro de código também é executado |
| Rastreável | Difícil de reverter |
| Liquidação programada | Depende do oráculo e de um **gatilho** (uma transação que chame a função) |

  - "Aqui mora o alerta da apostila: a execução é literal e inevitável. Um erro de programação pode ter consequências financeiras irreversíveis."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O smart contract executa a regra quando as condições predefinidas são cumpridas" | Certo | Apostila p. 541 |
| "Se o resultado for injusto, o smart contract interrompe sozinho a execução" | Errado | Executa a regra **literal**, justa ou não |

> **Autoexecutável cumpre a regra quando o gatilho chega; não julga se é justo.**

**🔗 Ponte:** "Em que redes esses contratos rodam?"

---

### 3.4 Plataformas de smart contracts — 3 min · CPA 4.4.3.4

- **O que é plataforma**
  - "Plataforma é a blockchain que permite implantar e executar smart contracts. Ela define o consenso, o ambiente de execução, as taxas e as linguagens."

| Plataforma | Ponto de destaque |
| --- | --- |
| **Ethereum** | A principal plataforma de smart contracts; ambiente de execução **EVM**; taxas em gas |
| **Redes compatíveis com EVM** | Rodam contratos no padrão Ethereum, com **consenso e segurança próprios** |
| **Outras redes** | Arquiteturas diferentes; o conceito de smart contract se adapta |

- **Três camadas**

| Camada | O que é | Na metáfora |
| --- | --- | --- |
| **Plataforma** | A infraestrutura onde o código roda | O terreno do shopping |
| **Protocolo DeFi** | A aplicação financeira | A loja |
| **Smart contract** | O código com as regras do protocolo | A regra da loja |

  - "Escolher a plataforma é escolher o terreno: custo, velocidade, segurança e quem já usa."

- **Atualização regulatória (fora destes subitens)**
  - 🔇 "Usar blockchain não afasta a lei. A Lei 14.478/2022 exclui do conceito de ativo virtual os valores mobiliários, que seguem com a CVM. E o Banco Central regulamentou as prestadoras de serviços de ativos virtuais nas Resoluções BCB 519, 520 e 521, de 2025, em vigor desde 02/02/2026." **Status: conferido em fontes secundárias; texto das resoluções não reaberto.**

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Rede compatível com EVM é a própria Ethereum" | Errado | Usa o padrão, mas tem **consenso e segurança próprios** |
| "Plataforma e protocolo DeFi são a mesma coisa" | Errado | Infraestrutura × aplicação |
| "Ethereum é a principal plataforma de smart contracts" | Certo | Roteiro 4.4-A |

> **Plataforma é o terreno, protocolo é a loja, smart contract é a regra da loja.**

- 🔇 Fechamento em uma frase (sem etapa de revisão): "Smart contract é código que executa a regra combinada, com estado, oráculo e gas; roda numa plataforma; e o código não substitui a lei." Próxima aula do bloco: aplicações práticas (empréstimos, DEX, seguros e imóveis).

---

## Nota de verificação

- **Programa Detalhado CPA** (v1.2, rev. 04/06/2025, vigência 01/01/2026): itens 4.4.3.1 a 4.4.3.4 lidos no texto do PD do repositório.
- **Apostila CPA**, p. 541–542: definição, características e princípio "Code is Law".
- **Roteiro 4.4-A** (35 min, do repositório): componentes, plataformas e correções, conferidos em 29/09/2026 contra o roteiro em PDF e a aula do repositório. **Não reabertos nesta sessão:** Ethereum.org e NIST, citados nele.
- **Res. BCB 519, 520 e 521/2025:** publicadas em 10/11/2025, em vigor desde 02/02/2026, conforme fontes secundárias (Chambers, Felsberg, Machado Meyer). **Fontes divergem sobre qual resolução trata de qual tema**, então a fala cita só as três em conjunto.
- **Lei 14.478/2022 e Parecer de Orientação CVM 40/2022:** conforme a aula do repositório. **Não reabertos nesta sessão.**
- **Convenções sem força normativa:** o seguro de atraso de voo (exemplo didático), a tabela de componentes e a classificação de plataformas.
- **Acréscimos (➕):** exemplo do seguro de voo para o oráculo, tabela de vantagens e limites da autoexecução e as três camadas.
