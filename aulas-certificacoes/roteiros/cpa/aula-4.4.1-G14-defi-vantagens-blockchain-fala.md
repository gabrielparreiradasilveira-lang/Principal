# Roteiro de fala — Aula CPA: Finanças Tradicionais × DeFi, Vantagens e Blockchain

**Base:**
- **Programa Detalhado CPA** (ANBIMA, v1.2, rev. 04/06/2025, vigência 01/01/2026), itens 4.4.1, 4.4.2 e 4.4.2.1;
- APOSTILA-CPA, p. 539–541;
- roteiro **4.4-A** (DeFi, blockchain e smart contracts), do qual esta aula é a versão de 10 min só com tópicos;
- aula **G15** (smart contracts), que continua esta.

CPA 4.4.1 · 4.4.2 · 4.4.2.1 · Módulo 4 · **10 min** · Aula G14 do plano de gravação · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ✏️ = correção da fonte · ➕ = acréscimo desta versão · 🔗 = ponte · ⌨️ = teclas da HP12C · 🖥️ = visor.

---

## Bastidor — antes de gravar

### 🔇 Formato

- Direto aos tópicos do PD, sem as demais etapas.
- Fio condutor: um **empréstimo** feito no banco e o mesmo empréstimo feito por código, para comparar quem executa cada passo.

### 🔇 Checagem de escopo (PD × materiais)

| Subitem do PD | Apostila | Tratamento |
| --- | --- | --- |
| 4.4.1 Finanças tradicionais × descentralizadas | p. 539 | Conferido; a apostila só **define** e anuncia o contraste, então a tabela comparativa é acréscimo |
| 4.4.2 Vantagens do DeFi | **Ausente** | Coberto pelo roteiro 4.4-A; cada vantagem vem com seu limite |
| 4.4.2.1 Conceito de blockchain | p. 540–541 | Conferido; hash, nós e descentralização, com ressalva sobre "imutável" |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto | Base |
| --- | --- | --- | --- | --- |
| 1 | Apostila p. 539–542 | Subitens numerados como "4.3" | Numeração do PD: 4.4.1, 4.4.2 e 4.4.2.1. A fala usa a do PD | PD CPA |
| 2 | Apostila p. 539 e 542 | DeFi **elimina** a necessidade de intermediários | **Resposta de prova:** funciona sem intermediários centralizados. **Ressalva:** a dependência é reduzida, não zero (desenvolvedores, validadores, fornecedores de dados e governança continuam existindo) | Roteiro 4.4-A (BIS) |
| 3 | Apostila p. 541 | Blockchain é "quase impossível de ser alterada ou fraudada" | Muito difícil de **alterar**. Mas guarda bem **o que recebe**: não confere se o dado é verdadeiro | Roteiro 4.4-A (NIST) |
| 4 | Apostila p. 541 | Hash é "código criptográfico único que protege cada bloco" | Correto como resumo: o hash é a **impressão digital** do bloco, e não senha de usuário | Roteiro 4.4-A |

### 🔇 Dados do exemplo (taxa de rede)

| Item | Valor |
| --- | --- |
| Taxa de rede (gas) | R$ 15,00, hipótese em reais |
| Operação pequena | R$ 500,00 → taxa de **3%** |
| Operação grande | R$ 50.000,00 → taxa de **0,03%** |

### 🔇 Cronograma

| Tópico | Tempo |
| --- | --- |
| 3.1 Finanças tradicionais × DeFi | 3,5 min |
| 3.2 Vantagens do DeFi | 3 min |
| 3.3 Conceito de blockchain | 3,5 min |
| **Total** | **10 min** |

---

## 3. Explicação dos tópicos — 10 min

### 3.1 Finanças tradicionais × finanças descentralizadas — 3,5 min · CPA 4.4.1 · Apostila p. 539

- **O empréstimo de sempre**
  - "No banco, alguém analisa seu cadastro, aprova, registra o contrato e cobra as parcelas. Quem executa é uma instituição."

- **O empréstimo em código**
  - "No DeFi, as regras estão escritas em um programa. Você deposita uma garantia digital, o programa confere e libera o dinheiro. Quem executa é o código."

- **O que é DeFi**
  - "DeFi, do inglês *Decentralized Finance*, é um ecossistema financeiro construído sobre blockchain. Ele recria empréstimos, pagamentos e negociações de forma aberta e programável, sem intermediários centralizados, como bancos e corretoras."

| Critério | Finanças tradicionais | DeFi |
| --- | --- | --- |
| **Quem executa** | Instituições (bancos, corretoras) | Protocolos e smart contracts |
| **Acesso** | Conta, cadastro, aprovação | Carteira digital e conexão à rede |
| **Registro** | Sistemas da instituição | Blockchain |
| **Custódia** | Banco, corretora ou custodiante | O próprio usuário (chave privada) ou o contrato |
| **Horário** | Horário de funcionamento | 24 horas, 7 dias |
| **Erro** | Contestação e estorno | Transação confirmada é **difícil ou impossível** de reverter |
| **Responsável** | Entidade identificável | Difuso entre os participantes |

- ✏️ **Eliminar ou reduzir?**
  - "A apostila diz que o DeFi elimina os intermediários. Na prova, aceite: sem intermediários centralizados. Na vida real, descentralizado não quer dizer sem ninguém: há desenvolvedores, validadores e votações de governança. A dependência é menor, não zero."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Blockchain e DeFi são sinônimos" | Errado | Blockchain é a **tecnologia**; DeFi é a **aplicação financeira** |
| "No DeFi, o usuário pede estorno ao protocolo como faz com o banco" | Errado | Transação confirmada é **difícil de reverter** |
| "DeFi recria serviços financeiros em blockchain, sem intermediários centralizados" | Certo | Apostila p. 539 |

> **No tradicional, a instituição executa; no DeFi, o código executa.**

**🔗 Ponte:** "Por que alguém usaria isso? As vantagens."

---

### 3.2 Vantagens do DeFi — 3 min · CPA 4.4.2

- **Cada vantagem tem um preço**
  - "Vou listar as vantagens, sempre com o risco que vem junto. É isso que um profissional certificado precisa saber explicar ao cliente."

| Vantagem | O que significa | Limite |
| --- | --- | --- |
| **Acesso ampliado** | Qualquer pessoa com carteira e internet | Exige conhecimento; há fraudes |
| **Funcionamento 24/7** | Sem horário de agência | A rede congestiona e as taxas sobem |
| **Transparência** | Regras e transações visíveis | Código aberto não é código seguro |
| **Programabilidade** | Regras financeiras viram código | Erro de código também é executado |
| **Composabilidade** | Protocolos se encaixam como blocos de montar | A falha de um contamina os outros |
| **Autocustódia** | O usuário controla os próprios ativos | Perdeu a chave, perdeu o ativo |
| **Menos etapas e custos** | A automação reduz conciliações | Não elimina risco de mercado nem de governança |

- **Quanto a taxa da rede pesa**
  - "Uma operação paga 15 reais de taxa de rede, o gas. Compare uma operação de 500 reais com outra de 50 mil."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `500` `ENTER` `15` `%T` | 🖥️ 3,00 | A taxa é 3% da operação pequena |
| 2 | ⌨️ `f` `REG` `50000` `ENTER` `15` `%T` | 🖥️ 0,03 | A mesma taxa é 0,03% da operação grande |

  - "A taxa não depende do valor da operação, e sim do processamento. Em 500 reais, pesa 3%. Em 50 mil, pesa 0,03%. E, se a rede congestionar, sobe. Por isso 'custo menor' não vale para qualquer operação."
  - 🔇 Valores hipotéticos, em reais para simplificar. Na prática o gas é pago na moeda da rede e varia com o congestionamento. Gas **não é juros**.

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "No DeFi, o usuário pode ter a custódia dos próprios ativos" | Certo | Autocustódia |
| "A transparência do código garante que o protocolo seja seguro" | Errado | Código aberto pode ter erro |
| "Gas é a taxa de juros do empréstimo DeFi" | Errado | É o **custo de processamento** da rede |

> **Cada vantagem do DeFi vem com um risco na mesma medida.**

**🔗 Ponte:** "Tudo isso funciona sobre uma tecnologia: a blockchain."

---

### 3.3 Conceito de blockchain — 3,5 min · CPA 4.4.2.1 · Apostila p. 540–541

- **A definição**
  - "Blockchain, ou corrente de blocos, é um livro-razão digital distribuído. Ela registra transações em blocos ligados em sequência, com cópias em muitos computadores da rede."

| Componente | Função |
| --- | --- |
| **Bloco** | Agrupa um conjunto de informações: transações, contratos ou documentos |
| **Hash** | Código criptográfico do bloco; mudar o conteúdo muda o hash e **quebra a corrente** |
| **Nós** | Computadores da rede: validam, guardam e propagam transações |
| **Consenso** | Regra pela qual a rede aceita um novo bloco |
| **Chave privada** | Assina a transação; quem a tem controla o ativo |

- **Como uma transação entra**
  - "O usuário assina. A transação vai para a rede. Os nós verificam. Ela entra num bloco. A rede chega a um consenso. O bloco é acrescentado à corrente. Os saldos são atualizados."

- **Descentralizada**
  - "Os registros não ficam em um único servidor. Ficam distribuídos em milhares de computadores. Isso dá resiliência: para fraudar, seria preciso alterar a maioria das cópias."

| Tipo de rede | Quem participa |
| --- | --- |
| **Pública** (não permissionada) | Qualquer um que siga as regras |
| **Privada** (permissionada) | Só participantes autorizados |
| **De consórcio** | Um grupo de entidades |

- ✏️ **Registro íntegro não é informação verdadeira**
  - "A apostila diz 'quase impossível de ser alterada ou fraudada'. Alterar é muito difícil. Mas a blockchain guarda bem o que recebe: se alguém registrar um dado falso, ele fica guardado, falso, para sempre."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Toda blockchain é pública" | Errado | Há redes privadas e de consórcio |
| "O hash é a senha da conta do usuário" | Errado | É a impressão digital do **bloco** |
| "Alterar um bloco muda o hash e quebra a corrente" | Certo | Apostila p. 541 |
| "A blockchain garante que todo dado registrado é verdadeiro" | Errado | Garante a **integridade do registro**, não a verdade da origem |

> **Blockchain guarda bem o que recebe; não confere se é verdade.**

- 🔇 Fechamento em uma frase (sem etapa de revisão): "DeFi é o serviço financeiro, a blockchain é o livro que sustenta o serviço, e cada vantagem vem com um risco." Próxima aula: G15, smart contracts.

---

## Nota de verificação

- **Programa Detalhado CPA** (v1.2, rev. 04/06/2025, vigência 01/01/2026): itens 4.4.1 a 4.4.2.1 lidos no texto do PD do repositório.
- **Apostila CPA**, p. 539–541: definição de DeFi, blockchain (bloco, hash, nós, descentralização).
- **Roteiro 4.4-A** (35 min, do repositório): tabela comparativa, vantagens com limites e correções, já conferidos em 29/09/2026 contra o roteiro em PDF e a aula do repositório. **Não reabertos nesta sessão:** as fontes originais citadas nele (BIS, NIST).
- **Convenções sem força normativa:** a tabela comparativa tradicional × DeFi, a lista de vantagens e limites, a classificação das redes (pública, privada, consórcio) e os valores do exemplo de gas.
- **Cálculos conferidos em Python:** 15 ÷ 500 = 3%; 15 ÷ 50.000 = 0,03%.
- **Acréscimos (➕):** o empréstimo no banco e em código, a tabela de vantagens com limites e o exemplo do peso do gas.
