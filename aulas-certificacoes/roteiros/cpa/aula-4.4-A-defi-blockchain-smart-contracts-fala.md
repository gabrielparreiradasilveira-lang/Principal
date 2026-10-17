# Roteiro de fala — Aula CPA: DeFi, Blockchain e Smart Contracts

**Base:**
- aula do repositório `aulas/cpa/aula-4.4-A-defi-blockchain-smart-contracts/aula.md`;
- roteiro em PDF `material-4.4-defi` (lote `topico-4.4-defi-blockchain-smart-contracts`);
- APOSTILA-CPA, p. 539–542;
- Lei 14.478/2022 e Parecer CVM 40/2022, conferidos na aula do repositório em 29/09/2026.

CPA 4.4 · 4.4.1 · 4.4.2 · 4.4.2.1 · 4.4.3 · 4.4.3.1 · 4.4.3.2 · 4.4.3.3 · 4.4.3.4 · Módulo 4 · **35 min** · Aula A de 3 do bloco 4.4

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ✏️ = correção da fonte · ➕ = acréscimo desta versão · 🔗 = ponte · ⌨️ = teclas da HP12C · 🖥️ = visor.

---

## Bastidor — antes de gravar

### 🔇 Checagem de escopo (PD × materiais)

| Subitem do PD | PDF do lote | Apostila | Tratamento |
| --- | --- | --- | --- |
| 4.4.1 Finanças tradicionais × descentralizadas | Roteiro p. 6–10 | p. 539 | Coberto; "elimina" intermediários com ressalva |
| 4.4.2 Vantagens do DeFi | Roteiro p. 10–13 | — | Coberto pelo PDF |
| 4.4.2.1 Conceito de blockchain | Roteiro p. 13–18 | p. 540–541 | Coberto; imutabilidade com ressalva |
| 4.4.3.1 Conceito de smart contracts | Roteiro p. 18–20 | p. 541 | Coberto; "Code is Law" com ressalva |
| 4.4.3.2 Componentes e funcionamento | Roteiro p. 20–26 | **Ausente** | Coberto pelo PDF |
| 4.4.3.3 Contratos autoexecutáveis | Roteiro p. 26–29 | p. 541 | Coberto |
| 4.4.3.4 Plataformas de smart contracts | Roteiro p. 29–33 | **Ausente** | Coberto pelo PDF, **simplificado** para o nível da CPA |

**Cobertura:** todos os itens da imagem têm material. Nada faltando nos PDFs.

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto | Base |
| --- | --- | --- | --- | --- |
| 1 | Apostila p. 539 e 542 | DeFi **elimina** intermediários | **Resposta de prova:** recria serviços **sem intermediários centralizados**. **Ressalva:** a dependência é **reduzida**; seguem existindo validadores, oráculos, desenvolvedores e governança | Roteiro em PDF (BIS) |
| 2 | Apostila p. 541 | Smart contract "não pode ser alterado" | **Resposta de prova:** imutável depois de implantado. **Ressalva:** é o **padrão**; há desenhos com atualização ou pausa por governança | Roteiro em PDF (Ethereum.org) |
| 3 | Apostila p. 541–542 | "Code is Law": autoridade final, **sem apelação** | Expressão de mercado sobre execução literal. **Juridicamente o código não substitui a lei** | Lei 14.478/2022; Parecer CVM 40/2022 |
| 4 | Apostila p. 541 | Blockchain é "quase impossível de ser alterada ou fraudada"; execução "garantida pela rede" | A rede **preserva o registro** e executa o código como escrito, mas **não garante** que o dado seja verdadeiro nem que o código esteja certo | Roteiro em PDF (NIST) |
| 5 | Roteiro p. 29–33 | Plataformas em nível técnico de engenharia | **Simplificado** para a CPA | — |

### ➕ Kit HP12C

- 🔇 A HP aparece uma vez: para mostrar quanto a **taxa da rede (gas)** pesa em uma operação pequena e em uma grande, com ⌨️ `%T`.
- Preparar com ⌨️ `f` `REG` e ⌨️ `f` `2`.

| Recurso | Teclas | Para que serve aqui |
| --- | --- | --- |
| Limpar | ⌨️ `f` `REG` | Zera a pilha |
| 2 casas | ⌨️ `f` `2` | Visor com centavos |
| Percentual do total | ⌨️ total `ENTER` parte `%T` | Quanto a taxa representa da operação |

### 🔇 Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Abertura | 3 min |
| 2. Metáfora | 3 min |
| 3. Tópicos (3.1 Tradicional × DeFi 4 · 3.2 Vantagens 3 · 3.3 Blockchain 5 · 3.4 Smart contracts 5 · 3.5 Autoexecutáveis 2 · 3.6 Plataformas 3) | 22 min |
| 4. Por que cai | 2 min |
| 5. Case | 2 min |
| 6. Questões | 2 min |
| 7. Revisão | 1 min |
| **Total** | **35 min** |

---

## 1. Fala de abertura — 3 min

- **O empréstimo de sempre**
  - "Você quer um empréstimo. No banco, alguém analisa seu cadastro, aprova, registra o contrato e cobra as parcelas."

- **O empréstimo em código**
  - "Agora imagine que as regras desse empréstimo estão escritas em um programa. Você deposita uma garantia digital, o programa confere e libera o dinheiro. Se a garantia perder valor, o programa executa sozinho a regra combinada."

- **A pergunta**
  - "Onde está o banco? O gerente? O cartório? É isso que a gente vai entender hoje: DeFi, a blockchain que registra tudo e os smart contracts que executam as regras."

- 🔇 Conexão com o PD: CPA 4.4.1 a 4.4.3.4. A aula seguinte, 4.4-B, trata das aplicações: empréstimos, DEX, seguros, imóveis e DAOs.

**🔗 Ponte:** "Para entender, vamos a uma máquina de venda automática."

---

## 2. Metáfora central — 3 min

### Metáfora: a máquina de venda automática

- **Sem vendedor**
  - "A máquina de venda não precisa de vendedor. Você escolhe o produto, paga o valor certo e ela libera. As regras estão programadas."

- **A máquina dentro da blockchain**
  - "O smart contract é essa máquina, só que dentro de uma blockchain. A regra é o código. O estoque é o saldo registrado na rede. O pagamento é uma transação assinada. E o livro de vendas, que todos podem conferir e ninguém consegue apagar, é a blockchain."

- **O shopping**
  - "E DeFi é o shopping inteiro dessas máquinas: empréstimo, troca de ativos, seguro, tudo em máquinas programadas."

### Correspondência técnica

| Máquina de venda | DeFi |
| --- | --- |
| Máquina | **Smart contract** |
| Regra programada | **Código** |
| Estoque | **Estado** (saldos e dados) |
| Pagamento | **Transação assinada** com chave privada |
| Livro de vendas público | **Blockchain** |
| Shopping de máquinas | **Ecossistema DeFi** |
| Energia que a máquina consome | **Gas** (taxa da rede) |
| Máquina que dá defeito e engole a moeda | **Erro de código**: também é executado |

### Frase de fixação

> **Blockchain é o livro; smart contract é a máquina; DeFi é o shopping de máquinas.**

**🔗 Ponte:** "Primeiro, a comparação que a prova mais cobra: tradicional contra descentralizado."

---

## 3. Explicação dos tópicos — 22 min

### 3.1 Finanças tradicionais × finanças descentralizadas — 4 min · CPA 4.4.1 · Apostila p. 539

- **O que é DeFi**
  - "DeFi, de *Decentralized Finance*, é o ecossistema que recria serviços financeiros, como empréstimos, pagamentos e negociações, sobre blockchain, de forma aberta e programável, sem intermediários centralizados como bancos e corretoras."

| Critério | Finanças tradicionais | DeFi |
| --- | --- | --- |
| Quem executa | **Instituições** (bancos, corretoras) | **Protocolos e smart contracts** |
| Acesso | Conta, cadastro, aprovação | Carteira digital e conexão à rede |
| Registro | Sistemas da instituição | **Blockchain** (registro distribuído) |
| Custódia | Banco, corretora, custodiante | O próprio usuário (chave privada) ou o contrato |
| Horário | Horário de funcionamento | **24 horas, 7 dias** |
| Erro | Contestação, estorno | Transação confirmada é **difícil ou impossível** de reverter |
| Responsável | Entidade identificável | Difuso entre participantes |

- ✏️ **"Elimina" ou "reduz"?**
  - "A apostila diz que o DeFi 'elimina' os intermediários. Na prova, aceite: DeFi funciona sem intermediários centralizados. Mas, na vida real, descentralizado não quer dizer sem ninguém: há desenvolvedores, validadores, fornecedores de dados e votações de governança. A dependência é menor, não zero."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Blockchain e DeFi são sinônimos" | Errado | Blockchain é a **tecnologia**; DeFi é a **aplicação financeira** |
| "No DeFi, o usuário pode pedir estorno ao protocolo como pede ao banco" | Errado | Transação confirmada é **difícil de reverter** |
| "No DeFi, quem executa o empréstimo é um gerente do protocolo" | Errado | Quem executa é o **código** |

> **No tradicional, a instituição executa; no DeFi, o código executa.**

**🔗 Ponte:** "Por que alguém usaria isso? As vantagens."

---

### 3.2 Vantagens do DeFi — 3 min · CPA 4.4.2

- **Cada vantagem tem um preço**
  - "Vou listar as vantagens, mas sempre com o risco que vem junto. É isso que um profissional certificado precisa saber explicar ao cliente."

| Vantagem | O que significa | Limite |
| --- | --- | --- |
| **Acesso ampliado** | Qualquer pessoa com carteira e internet | Exige conhecimento; fraudes |
| **24/7** | Sem horário de agência | Rede congestiona; taxas sobem |
| **Transparência** | Regras e transações visíveis | Código aberto não é código seguro |
| **Programabilidade** | Regras financeiras viram código | Erro de código também é executado |
| **Composabilidade** | Protocolos se encaixam como "blocos de montar" | Falha de um contamina os outros |
| **Autocustódia** | O usuário controla os próprios ativos | Perdeu a chave, perdeu o ativo |
| **Menos etapas e custos** | Automação reduz conciliações | Não elimina risco de mercado nem de governança |

#### ➕ Exemplo prático — quanto a taxa da rede pesa

Uma operação paga **R$ 15,00 de taxa de rede (gas)**. Compare uma operação de **R$ 500,00** com outra de **R$ 50.000,00**.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` | 🖥️ 0,00 | Pilha limpa |
| 2 | ⌨️ `500` `ENTER` `15` `%T` | 🖥️ 3,00 | A taxa é **3%** da operação pequena |
| 3 | ⌨️ `f` `REG` | 🖥️ 0,00 | Pilha limpa |
| 4 | ⌨️ `50000` `ENTER` `15` `%T` | 🖥️ 0,03 | A mesma taxa é **0,03%** da operação grande |

- "A taxa da rede não depende do valor da operação, depende do processamento. Em uma operação de 500 reais, 15 de taxa são 3%. Em 50 mil, são 0,03%. E, se a rede congestionar, essa taxa sobe. Por isso 'custo menor' não vale para qualquer operação."
- 🔇 Valores hipotéticos e em reais para simplificar. Na prática, o gas é pago na moeda da rede e varia com o congestionamento. Gas **não é juros**.

> **Cada vantagem do DeFi vem com um risco na mesma medida.**

**🔗 Ponte:** "Tudo isso só funciona por causa de uma tecnologia: a blockchain."

---

### 3.3 Conceito de blockchain — 5 min · CPA 4.4.2.1 · Apostila p. 540–541

- **A definição**
  - "Blockchain, 'corrente de blocos', é um livro-razão digital distribuído. Ela registra transações em blocos ligados em sequência, com cópias em muitos computadores da rede."

| Componente | Função |
| --- | --- |
| **Bloco** | Agrupa um conjunto de transações |
| **Hash** | "Impressão digital" criptográfica do bloco; mudar o conteúdo muda o hash e **quebra a corrente** |
| **Nós** | Computadores que guardam cópias, validam e propagam transações |
| **Consenso** | Regra pela qual a rede aceita um novo bloco (ex.: prova de trabalho, prova de participação) |
| **Chave privada** | Assina as transações; quem tem a chave controla o ativo |

- **Como uma transação entra**
  - "O usuário assina. A transação vai para a rede. Os nós verificam. Ela entra num bloco. A rede chega a um consenso. O bloco é acrescentado à corrente. Os saldos são atualizados."

| Tipo de rede | Quem participa |
| --- | --- |
| **Pública** (não permissionada) | Qualquer um que siga as regras |
| **Privada** (permissionada) | Só participantes autorizados |
| **Consórcio** | Um grupo de entidades |

- ✏️ **Registro íntegro não é informação verdadeira**
  - "A apostila diz que a blockchain é 'quase impossível de ser alterada ou fraudada'. Ela é muito difícil de alterar, sim. Mas a blockchain guarda bem o que recebe: se alguém registrar um dado falso, ele fica guardado, falso, para sempre."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Toda blockchain é pública" | Errado | Há redes **privadas** e **de consórcio** |
| "O hash é uma senha que protege a conta do usuário" | Errado | É a **impressão digital** do bloco |
| "A blockchain garante que todo dado registrado é verdadeiro" | Errado | Garante a **integridade do registro**, não a verdade da origem |

> **Blockchain guarda bem o que recebe; não confere se é verdade.**

**🔗 Ponte:** "Na blockchain também rodam programas. São os smart contracts."

---

### 3.4 Smart contracts: conceito, componentes e funcionamento — 5 min · CPA 4.4.3, 4.4.3.1 e 4.4.3.2 · Apostila p. 541

- **A definição**
  - "Smart contract, ou contrato inteligente, é um contrato digital autoexecutável escrito em código. As regras e as consequências do acordo ficam programadas e são executadas automaticamente quando as condições são cumpridas."

| Característica (apostila) | Ressalva |
| --- | --- |
| **Imutabilidade** | É o **padrão**; alguns desenhos permitem atualização ou pausa por governança |
| **Transparência** | Público não significa compreensível nem seguro |
| **Segurança** | A rede garante a **execução**, não que o código esteja certo |
| **"Code is Law"** | Expressão de mercado; **não substitui a lei** |

- **Os componentes**

| Componente | Função |
| --- | --- |
| **Código** | As regras (depositar, sacar, trocar, liquidar) |
| **Estado** | Os dados guardados (saldos, garantias, dívidas) |
| **Endereço** | Onde o contrato "mora" na blockchain |
| **Transação** | Mensagem assinada que aciona uma função |
| **Gas** | Custo de processamento pago à rede (≠ juros) |
| **Oráculo** | Traz **dados do mundo real** (preço, índice, clima) para o contrato |
| **Carteira** | Guarda a chave e **assina**; não executa a regra |

- **O fluxo**
  - "O código é implantado. O usuário assina uma transação na carteira. A rede executa o contrato. O consenso confirma. O estado é atualizado."

- **O oráculo, peça-chave**
  - "O contrato não enxerga o mundo de fora. Se ele precisa saber o preço de um ativo ou se choveu numa cidade, alguém tem de levar essa informação: é o oráculo. Se o oráculo errar, o contrato executa certo com o dado errado."

- ✏️ **"Code is Law"**
  - "A apostila diz que o código é a autoridade final, sem apelação. É o que o mercado diz. Juridicamente, no Brasil, o código não está acima da lei: proteção do consumidor, lavagem de dinheiro, tributação e a competência da CVM continuam valendo."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Smart contract é uma inteligência artificial" | Errado | É **código programado**: não pensa, executa |
| "O oráculo valida os blocos da rede" | Errado | O oráculo **traz dados externos**; quem valida são os nós |
| "Gas é a taxa de juros do empréstimo DeFi" | Errado | É o **custo de processamento** da rede |

> **Smart contract é código + estado na blockchain: não pensa, executa.**

**🔗 Ponte:** "Executar sozinho é o que define um contrato autoexecutável."

---

### 3.5 Contratos autoexecutáveis — 2 min · CPA 4.4.3.3 · Apostila p. 541

- **A lógica "se… então…"**
  - "Se as condições programadas forem cumpridas, então o resultado é executado automaticamente, sem alguém interpretar e fazer cada etapa à mão. Garantia suficiente mais transação válida: empréstimo liberado."

| Vantagens | Limites |
| --- | --- |
| Menos intervenção manual | Rígido diante do imprevisto |
| Execução padronizada | Erro de código também é executado |
| Rastreável | Difícil de reverter |
| Liquidação programada | Depende de oráculo e de um **gatilho** (uma transação que chame a função) |

> **Autoexecutável cumpre a regra quando o gatilho chega; não julga se é justo.**

**🔗 Ponte:** "Em que redes esses contratos rodam?"

---

### 3.6 Plataformas de smart contracts — 3 min · CPA 4.4.3.4

- **O que é plataforma**
  - "Plataforma é a blockchain que permite implantar e executar smart contracts. Ela define o consenso, o ambiente de execução, as taxas e as linguagens."

| Plataforma | Ponto de destaque |
| --- | --- |
| **Ethereum** | A principal plataforma de smart contracts; ambiente de execução **EVM**; taxas em **gas** |
| **Redes compatíveis com EVM** | Rodam contratos no padrão Ethereum, com **consenso e segurança próprios** |
| **Outras redes** | Arquiteturas diferentes; o conceito de smart contract se adapta |

- **Três camadas**

| Camada | O que é | Na metáfora |
| --- | --- | --- |
| Plataforma | A **infraestrutura** onde o código roda | O terreno do shopping |
| Protocolo DeFi | A **aplicação financeira** | A loja |
| Smart contract | O **código** com as regras do protocolo | A regra da loja |

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Rede compatível com EVM é a própria Ethereum" | Errado | Usa o padrão, mas tem **consenso e segurança próprios** |
| "Plataforma e protocolo são a mesma coisa" | Errado | Infraestrutura × aplicação |

> **Plataforma é o terreno, protocolo é a loja, smart contract é a regra da loja.**

- 🔇 **Nota de atualização (fora destes subitens):** usar blockchain não afasta a lei. A Lei 14.478/2022 exclui do conceito de ativo virtual os **valores mobiliários**, que seguem com a **CVM** (Parecer CVM 40/2022). O BCB regulamentou as prestadoras de serviços de ativos virtuais pelas Res. BCB 519, 520 e 521/2025, em vigor desde 02/02/2026 (conferido na aula do repositório; texto não reaberto nesta sessão).

**🔗 Ponte:** "Agora, por que isso cai."

---

## 4. Por que isso cai na prova? — 2 min

- **Como a banca pergunta**
  - "A CPA cobra definições curtas e diferenças: tradicional contra DeFi, blockchain contra smart contract, e as características do smart contract."

### Pontos de atenção

1. **DeFi:** serviços financeiros em blockchain, sem intermediários centralizados.
2. **Blockchain:** livro-razão distribuído; blocos ligados por hash; validado por nós.
3. **Smart contract:** contrato autoexecutável em código; imutável, transparente, "Code is Law".
4. **Oráculo** traz dados externos; **gas** é taxa da rede.
5. **Ethereum** é a principal plataforma; **EVM** é seu ambiente de execução.

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Finanças tradicionais | DeFi | Instituição executa × código executa |
| Blockchain | DeFi | Tecnologia × aplicação |
| Blockchain | Smart contract | Livro-razão × código que roda nele |
| Smart contract | Contrato jurídico | Execução literal × interpretação humana e lei |
| Gas | Juros | Taxa da rede × remuneração do crédito |

### Pegadinhas (todas erradas)

- "Smart contract é uma inteligência artificial."
- "Blockchain garante que toda informação registrada é verdadeira."
- "Gas é a taxa de juros do empréstimo DeFi."
- "DeFi dispensa qualquer regra jurídica, porque o código é a lei."

> **Livro, máquina e shopping: blockchain, smart contract e DeFi.**

**🔗 Ponte:** "Vamos ver tudo junto num caso."

---

## 5. Case — 2 min

- "Uma investidora conecta sua carteira digital a um protocolo de empréstimos numa blockchain pública, deposita tokens como garantia e assina a transação. O contrato consulta o preço da garantia por um oráculo e libera o empréstimo. Semanas depois, o preço da garantia cai abaixo do limite, e o contrato liquida a posição automaticamente. Depois, os participantes do protocolo votam para mudar uma taxa."

| Fato | Conceito |
| --- | --- |
| Carteira e assinatura | Chave privada; autocustódia |
| Protocolo de empréstimos | **DeFi** |
| Regras de garantia e liberação | **Smart contract** |
| Preço trazido de fora | **Oráculo** |
| Liquidação ao romper o limite | **Contrato autoexecutável** |
| Registro de tudo | **Blockchain** |
| Votação da taxa | **Governança**: DeFi não é "sem ninguém" |

- "Nenhum gerente aprovou nada, mas houve código, oráculo, rede e governança."

> **Sem gerente não quer dizer sem regras nem sem risco.**

**🔗 Ponte:** "Agora, as questões."

---

## 6. Questões comentadas — 2 min

### Questão 1 — Médio

**CPA · 4.4.2.1 e 4.4.3 Blockchain e smart contracts · Médio**

Sobre blockchain e smart contracts no contexto das finanças descentralizadas (DeFi), é correto afirmar que:

A) o smart contract é um sistema de inteligência artificial que interpreta a intenção das partes antes de executar o acordo.
B) a blockchain é um livro-razão digital distribuído em que os blocos são encadeados por hash, e o smart contract é um contrato autoexecutável escrito em código, cumprido automaticamente quando as condições predefinidas são atendidas.
C) a blockchain garante que qualquer informação registrada é verdadeira, dispensando a verificação da fonte dos dados.
D) no DeFi, a taxa de gas corresponde aos juros pagos pelo tomador ao credor em um empréstimo.

**Gabarito: B**

- **B (correta):** definições de blockchain e smart contract (Apostila p. 540–541).
- **A:** smart contract não é IA; executa regras programadas.
- **C:** preserva o registro, mas não verifica a verdade da origem.
- **D:** gas é custo de processamento da rede.
  - "Resposta B. Smart contract não pensa, blockchain não confere a verdade, gas não é juros."

### ➕ Questão 2 — Difícil

**CPA · 4.4.3.2 Componentes dos smart contracts · Difícil**

Um smart contract de seguro precisa saber se houve atraso de um voo para pagar a indenização. A informação sobre o voo chega ao contrato por meio de:

A) um nó validador, que confirma os blocos da rede.
B) um oráculo, que leva dados do mundo externo para a blockchain.
C) a carteira digital do segurado, que executa a regra do contrato.
D) o hash do bloco, que registra o horário do voo.

**Gabarito: B**

- **B (correta):** o oráculo traz dados externos.
- **A:** o nó valida e propaga transações; não busca dados de fora.
- **C:** a carteira só assina; não executa a regra.
- **D:** o hash é a impressão digital do bloco.
  - "Resposta B. O contrato é cego para fora; o oráculo é o olho."

### ➕ Questão 3 — Fácil

**CPA · 4.4.1 Tradicional × DeFi · Fácil**

Em comparação às finanças tradicionais, as finanças descentralizadas (DeFi) caracterizam-se por:

A) depender de autorização de um banco para cada operação.
B) funcionar apenas em horário comercial.
C) recriar serviços financeiros em blockchain, com regras executadas por smart contracts, sem intermediários centralizados.
D) permitir o estorno de qualquer transação mediante pedido ao protocolo.

**Gabarito: C**

- **C (correta):** definição de DeFi (Apostila p. 539).
- **A:** quem executa é o código.
- **B:** funciona 24/7.
- **D:** transações confirmadas são difíceis de reverter.
  - "Resposta C. Código no lugar da instituição."

**🔗 Ponte:** "Para fechar, a revisão."

---

## 7. Revisão final — 1 min

### Resumo em cinco pontos

1. DeFi recria serviços financeiros em blockchain, de forma aberta e programável, sem intermediários centralizados (na prática, reduz a dependência deles).
2. Vantagens: acesso, 24/7, transparência, programabilidade, composabilidade e autocustódia, cada uma com um risco.
3. Blockchain: livro-razão distribuído, blocos ligados por hash, nós e consenso; registro íntegro, mas não necessariamente verdadeiro.
4. Smart contract: contrato autoexecutável em código; imutável, transparente, "Code is Law" sem substituir a lei; componentes: código, estado, transação, gas, oráculo e carteira.
5. Plataformas: Ethereum (EVM, gas) e outras redes; plataforma ≠ protocolo ≠ contrato.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| DeFi | Serviços financeiros em blockchain sem intermediário central |
| Blockchain | Livro-razão distribuído · blocos + hash · nós · consenso |
| Smart contract | Contrato autoexecutável em código · imutável · transparente |
| Code is Law | Execução literal (não substitui a lei) |
| Oráculo | Leva dado externo ao contrato |
| Gas | Taxa de processamento (≠ juros); pesa mais em operação pequena |
| Plataforma | Ethereum/EVM e outras redes |

### Cadeia lógica

**Blockchain (infraestrutura) → smart contract (código) → execução automática → protocolo DeFi (serviço financeiro)**

### Frase central da aula

> **Blockchain é o livro, smart contract é a máquina, DeFi é o shopping de máquinas, e o código não substitui a lei.**

- "Voltando ao empréstimo do começo: o banco virou código, o gerente virou regra programada e o cartório virou blockchain. Na próxima aula: o que dá para fazer com essas máquinas."

---

## Nota de verificação

- **Base:** aula do repositório (fontes conferidas em 29/09/2026), roteiro em PDF do lote e APOSTILA-CPA p. 539–542. Textos legais **não reabertos nesta sessão**.
- **Acréscimos (➕):**
  - exemplo HP12C do peso da taxa de rede (`%T`), hipotético;
  - linha "máquina que engole a moeda" na metáfora;
  - tabela de três camadas com a metáfora;
  - questões 2 e 3;
  - tabelas de certo × errado.
