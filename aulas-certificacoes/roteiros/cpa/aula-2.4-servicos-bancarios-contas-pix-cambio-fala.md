# Roteiro de fala — Aula CPA: Serviços Bancários, Contas, FGC, Compulsório, Boleto, Pix, Tarifas, Atendimento, Conta Internacional e Câmbio (versão refinada)

**Base:**
- texto enviado pelo professor (tópicos 3.2 a 3.13.3, corte normativo de 10/09/2026);
- aulas do repositório `aulas/cpa/aula-2.4.1-A`, `-B` e `-C`.

O texto original foi mantido na essência: falas revisadas, termos soltos explicados dentro da fala, pontes entre tópicos, tabelas, cálculos na HP12C e checagens.

CPA 2.4.1 a 2.4.1.7.1 · 2.4.2 a 2.4.2.3 · 2.4.3 a 2.4.3.3 · Módulo 2

**Legenda:**
- **negrito** = marcador do conteúdo;
- "texto entre aspas" = fala;
- 🔇 = bastidor, sem fala;
- ✏️ = ajuste ou correção no texto enviado;
- ➕ = acréscimo desta versão;
- 🔗 = ponte para o próximo tópico;
- ⌨️ = teclas da HP12C;
- 🖥️ = o que aparece no visor.

---

## Bastidor — antes de gravar

> 🔇 **Como ler este roteiro**
> - O texto começa no 3.2. O 3.1 (visão geral do item 2.4) não veio no envio e continua como estava.
> - Cada tópico termina com uma ponte (🔗). O texto enviado não tinha pontes.
> - Os números normativos foram mantidos como no texto enviado (corte de 10/09/2026). O que conferi está na nota de verificação no fim. O que mudou de status depois do corte está marcado com ✏️.

### ✏️ Ajustes feitos no texto enviado

| # | Tópico | O texto diz | Ajuste | Motivo |
| --- | --- | --- | --- | --- |
| 1 | 3.9.4 Pix PJ | "MEI e empresário individual = regra de PF; **EIRELI = PJ**" | Retirada a EIRELI da fala | A EIRELI deixou de existir: a Lei 14.195/2021 converteu as EIRELIs em sociedades limitadas unipessoais (SLU). Citar EIRELI como categoria atual confunde |
| 2 | 3.12.1 eFX | Res. BCB 561/2026 "ainda não estava valendo" na data de corte | Mantido o corte, com aviso de que a norma **passou a valer em 01/10/2026** | A gravação é posterior a 01/10/2026 |
| 3 | 3.6 Compulsório | "21% não é taxa da sua conta" | Mantido; ➕ exemplo numérico na HP | Mostrar que a base é o VSR do banco, não o saldo do cliente |
| 4 | 3.5 FGC | Exemplo de R$ 300.000 | Mantido; ➕ conta conjunta e limite de R$ 1 milhão com HP | O texto citava as regras, mas não as calculava |
| 5 | Vários | Siglas soltas (VSR, PSP, SPI, DICT, VET, CBE, DAA, ERP, API) | Explicadas dentro da fala | Público TEA/TDAH: nenhuma sigla sem tradução |

### ➕ Kit HP12C (mostrar uma vez)

| O que fazer | Teclas | Por quê |
| --- | --- | --- |
| Limpar tudo | ⌨️ `f` `REG` | Apaga cálculos anteriores |
| Duas casas decimais | ⌨️ `f` `2` | Reais e centavos |
| Percentual | Valor ⌨️ `ENTER` taxa ⌨️ `%` | Calcula a parte; o valor original continua na pilha |
| Memória | ⌨️ `STO` `1` / ⌨️ `RCL` `1` | Guarda e recupera resultados intermediários |

- "Hoje a HP aparece em contas curtas: limite do FGC, compulsório, boleto vencido, câmbio e imposto. Prepare a máquina: f REG e f 2."

---

## 3.2 Conta corrente — CPA 2.4.1

### O que é

- **Definição**
  - "Conta corrente é o nome do dia a dia para a conta de depósitos à vista. É um contrato entre você e o banco. O dinheiro fica, em regra, disponível para movimentar ou sacar quando você quiser."

- **Deveres na abertura**
  - "Para abrir a conta, o banco precisa confirmar quem você é e conhecer o seu perfil. É o 'conheça seu cliente' que vimos na aula de lavagem de dinheiro. Se houver representante, como um procurador ou o responsável por um menor, o banco também precisa validar quem é. E o contrato precisa dizer: como você movimenta a conta, quanto custa, que cuidados de segurança existem, quais são os seus direitos e deveres, quais são os limites e como encerrar."

| No contrato da conta deve constar | Exemplo |
| --- | --- |
| Meios de movimentação | Cartão, app, cheque, internet banking |
| Tarifas | Tabela e pacote, se contratado |
| Segurança | Senha, biometria, limites |
| Direitos e deveres | Informação, sigilo, guarda do cartão |
| Limites | De transação, de saque |
| Encerramento | Como pedir e o que acontece com o saldo |

### Função e objetivo

- "A conta serve para receber, pagar, transferir e sacar, dentro do que o contrato prevê. É a porta de entrada para quase todos os outros serviços do banco."

### Como funciona

- **Abertura**
  - "Quem decide abrir é você. Pode ser na agência ou pelo aplicativo, sempre com as checagens de segurança, como foto do documento e reconhecimento facial."

- **Encerramento**
  - "Para encerrar, você diz para onde vai o saldo. O banco avisa se ainda há algum produto ativo, como um investimento ou um débito automático, ou algum impedimento, como uma dívida em aberto."

### Aplicação: saldo ≠ disponível ≠ coberto

| Conceito | O que é |
| --- | --- |
| Saldo exibido | Soma de créditos e débitos, que pode incluir valores bloqueados ou a liberar |
| Saldo disponível | O que pode ser usado agora |
| Valor coberto pelo FGC | Só os créditos elegíveis, até o limite (tópico 3.5) |

- "O número que aparece como saldo pode incluir dinheiro bloqueado por ordem judicial ou ainda a liberar, como um depósito em cheque esperando compensação. Então saldo exibido não é automaticamente dinheiro disponível, e nem dinheiro coberto pelo FGC."

### O que a prova pode confundir: conta corrente × conta-salário

| Ponto | Conta corrente | Conta-salário |
| --- | --- | --- |
| Quem pede a abertura | O interessado | O **empregador** |
| Créditos aceitos | De qualquer origem | Só do empregador (pagador) |
| Cheque | Pode ter | **Não** pode |
| Gratuidades | Cesta de serviços essenciais | Lista própria |
| Vínculo | Nenhum | Com o empregador |

- "A conta corrente você abre; a conta-salário quem pede é o empregador. Na corrente entra dinheiro de qualquer origem; na salário, só do empregador. A corrente pode ter cheque; a salário, não. E cada uma tem a sua lista de serviços gratuitos."

> **Conta corrente = depósitos à vista que você escolhe abrir. Conta-salário = conta especial que o empregador abre para pagar o salário.**

**🔗 Ponte:** "Já que apareceu a conta-salário, vamos entender como ela funciona e qual é o direito mais importante dela: a portabilidade do salário."

---

## 3.3 Recebimento de salários — CPA 2.4.1.1

### O que é

- **Conta-salário**
  - "A conta-salário existe para receber salários e verbas parecidas: proventos, soldos, vencimentos, aposentadorias e pensões pagas pelo empregador. Quem pede a abertura é o empregador: ele escolhe o banco e informa quem são os funcionários."

- **Restrições**
  - "O titular é sempre pessoa física, e não existe cheque nessa conta."

### Função e objetivo

- "A ideia é proteger o trabalhador. O empregador paga pelo banco que escolheu, mas o funcionário não é obrigado a virar cliente de conta corrente desse banco."

### Como funciona

- **Entradas e saídas**
  - "Só entra dinheiro do empregador. Para sair, o funcionário pode sacar, usar cartão de débito, pagar contas, pagar parcelas de empréstimos que ele autorizou e transferir."

- **Portabilidade salarial**
  - "A portabilidade salarial é uma ordem permanente: todo mês, o salário vai automaticamente para outra conta sua. Pode ser conta de banco ou conta de pagamento pré-paga, aquela de carteira digital, desde que você seja o titular."

| Regra da portabilidade salarial | Conteúdo |
| --- | --- |
| Onde pedir | No banco pagador **ou** no banco que vai receber |
| Prazo para começar | Até **10 dias úteis** |
| Custo | **Gratuita** |
| Quanto é transferido | O **valor total**, salvo parcelas de crédito ou leasing **autorizadas** pelo titular |
| Horário da transferência | Por TED ou TEC até **12h** do dia do crédito (Res. BCB 284/2023) |
| Cancelamento | Vale no mês seguinte se pedido com **5 dias úteis** de antecedência |

- "Você pode pedir no banco do empregador ou no banco que vai receber. O prazo é de até 10 dias úteis, não custa nada e transfere o valor total. A única coisa que pode ser descontada antes é parcela de empréstimo ou de leasing que você mesmo autorizou."
- "O dinheiro tem de ser transferido até o meio-dia do dia em que o salário cai. TED é a Transferência Eletrônica Disponível; TEC é a Transferência Especial de Crédito, usada em pagamentos como o de salário. E, se quiser cancelar, peça com pelo menos 5 dias úteis de antecedência para valer no mês seguinte."

### Aplicação

- **Conta de pagamento ≠ conta-salário**
  - "Se o salário já cai numa conta de pagamento comum, que não é conta-salário, não existe portabilidade salarial regulada. Pode haver transferência comum, e ela pode ser tarifada."

- **INSS**
  - "Aposentadoria do INSS tem regra própria. Não trate como conta-salário de emprego."

### Gratuidades da conta-salário

| Não se cobra | Detalhe |
| --- | --- |
| Manutenção | — |
| Portabilidade e transferência total do salário | — |
| Saques | Até **5 por crédito** de salário |
| Cartão de débito | Salvo reposição por perda ou dano causado pelo titular |
| Consultas de saldo | **2 por mês** |
| Extratos | **2 por mês** |

- "Na conta-salário, o banco não pode cobrar a manutenção, a portabilidade, a transferência do salário, até cinco saques a cada salário, o cartão de débito, salvo se você perder ou estragar, duas consultas de saldo e dois extratos por mês."

### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Conta-salário é um tipo de conta corrente" | Errado | É conta especial, aberta pelo empregador |
| "O próprio empregado abre a conta-salário" | Errado | Quem pede é o empregador |
| "A portabilidade só vai para conta corrente" | Errado | Também para conta de pagamento pré-paga do titular |
| "A portabilidade salarial é tarifada como uma TED" | Errado | É gratuita |
| "Nenhum valor pode ser descontado antes da portabilidade" | Errado | Parcelas de crédito ou leasing autorizadas ficam |

> **➕ Conta-salário: o empregador abre, o trabalhador escolhe para onde o salário vai, de graça.**

**🔗 Ponte:** "Voltemos à conta corrente. O dinheiro que fica nela tem um nome técnico: depósito à vista. Vamos entender o que ele é do ponto de vista do banco."

---

## 3.4 Depósitos à vista — CPA 2.4.1.2

### O que é

- **Uma dívida do banco com você**
  - "Depósito à vista é uma dívida do banco com você, que você pode cobrar a qualquer momento. 'À vista' quer dizer exatamente isso: disponível agora. Do ponto de vista contábil, o seu dinheiro na conta é um passivo do banco, uma obrigação que ele tem com você."

- **Saldo × saldo negativo**
  - "O saldo é a fotografia do momento. E saldo negativo não é depósito: é dinheiro que você pegou emprestado no cheque especial."

### Função e objetivo

- "Serve para ter liquidez imediata, ou seja, dinheiro pronto para usar."

### Como funciona

**Cliente deposita → banco registra a obrigação → cliente pode exigir, conforme regras de liquidação, bloqueios e contrato**

- "Você deposita, o banco registra que deve a você, e você pode pedir de volta, respeitando bloqueios e prazos de compensação."

- **Base do compulsório**
  - "No quadro geral da economia, esses depósitos entram na base de cálculo do compulsório do banco. Mas isso não cria uma reserva com o seu nome no Banco Central. Vamos ver isso em detalhe daqui a pouco."

### Aplicação

- "Antes de dizer se um saldo tem FGC ou entra no compulsório, descubra qual é o produto de verdade. O nome no aplicativo não basta. 'Saldo na conta' pode ser depósito à vista num banco ou saldo de conta de pagamento numa instituição de pagamento, e as regras são diferentes."

### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O limite do cheque especial é depósito à vista" | Errado | É crédito, não depósito |
| "Todo saldo exibido está disponível" | Errado | Pode haver bloqueio ou valor a liberar |
| "O compulsório separa uma parte do saldo de cada cliente" | Errado | Incide sobre a base do banco, sem conta individual |
| "Todo depósito tem FGC" | Errado | Depende do instrumento, da instituição, do titular e do evento |

> **➕ Depósito à vista: o banco deve, você cobra quando quiser.**

**🔗 Ponte:** "E se o banco que te deve quebrar? É aí que entra a garantia dos depósitos à vista: o FGC."

---

## 3.5 Garantias para depósitos à vista — CPA 2.4.1.2.1

### O que é

- **Garantia ordinária do FGC**
  - "A principal garantia é a do FGC, o Fundo Garantidor de Créditos, uma entidade privada mantida pelas próprias instituições associadas. Ela só é acionada quando o Banco Central decreta intervenção ou liquidação extrajudicial, que são as formas de o BC assumir ou encerrar um banco em crise."

### Função e objetivo

- "O FGC protege contra perda, mas com limite. Não cobre qualquer produto, nem um aplicativo fora do ar por algumas horas. App fora do ar é indisponibilidade, não quebra."

### Como funciona (corte de 10/09/2026)

| Regra | Conteúdo |
| --- | --- |
| Limite por instituição | **R$ 250.000** por CPF ou CNPJ, por instituição ou **conglomerado**, somando os créditos elegíveis |
| Teto global | **R$ 1.000.000** a cada **4 anos** por CPF ou CNPJ, no conjunto das associadas |
| Data de referência | Limite vigente na **data do evento** |
| Conta conjunta | Os R$ 250.000 são **divididos** entre os titulares |
| Podem ser elegíveis | Depósitos à vista, depósitos com aviso prévio (entre outros) |
| Ficam fora | Depósitos judiciais, captações no exterior, cotas de fundos, créditos de instituições financeiras, instrumentos subordinados |
| Conta de pagamento | **Sem FGC**: proteção por segregação patrimonial (Lei 12.865/2013) |

- **Por instituição ou conglomerado**
  - "O limite é de 250 mil reais por CPF ou CNPJ, somando tudo o que você tem na mesma instituição ou no mesmo conglomerado, que é o grupo de empresas do banco. Ter conta no banco e na financeira do mesmo grupo não dobra a garantia."

- **Teto global**
  - "Existe também um teto geral: 1 milhão de reais a cada quatro anos, por pessoa, somando todas as instituições que quebrarem nesse período."

- **Data e conta conjunta**
  - "Vale o limite da data em que o banco quebrou. E, na conta conjunta, o limite não dobra: os 250 mil são divididos entre os titulares."

- **Quem fica de fora**
  - "Depósito à vista pode estar coberto. Já cota de fundo, depósito judicial, dinheiro captado no exterior e títulos subordinados ficam fora. Subordinados são dívidas que, se o banco quebrar, recebem por último."

- **Conta de pagamento**
  - "Conta de pagamento de instituição de pagamento não tem FGC. Ela tem outra proteção: o dinheiro do cliente fica separado do patrimônio da empresa e não pode ser usado para pagar as dívidas dela."

### ➕ Exemplo prático 1 — quanto o FGC cobre

| Situação | Cobertura de referência |
| --- | --- |
| R$ 300.000 no mesmo conglomerado | R$ 250.000 (R$ 50.000 descobertos) |
| Conta conjunta com 2 titulares e R$ 400.000 | R$ 250.000 no total: R$ 125.000 para cada titular |
| R$ 200.000 no banco A e R$ 200.000 no banco B, de grupos diferentes | Até R$ 250.000 em cada um: tudo coberto, dentro do teto de R$ 1 milhão em 4 anos |

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `300000` `ENTER` `250000` `-` | 🖥️ 50.000,00 | Parte sem garantia |
| 2 | ⌨️ `250000` `ENTER` `2` `÷` | 🖥️ 125.000,00 | Cobertura de cada titular na conta conjunta |

- "Quem tem 300 mil no mesmo grupo não deve contar com 300 mil de garantia. A referência é 250 mil: na HP, 300 mil menos 250 mil, e sobram 50 mil descobertos. Na conta conjunta de dois titulares com 400 mil, o limite continua 250 mil para a conta: 250 mil dividido por 2 dá 125 mil para cada um."
- 🔇 Conta conjunta: a regra geral do FGC divide o limite em partes iguais entre os titulares, salvo indicação diferente. O estatuto não foi reaberto nesta sessão.

### O que a prova pode confundir: FGC × compulsório

| | FGC | Compulsório |
| --- | --- | --- |
| Quando age | **Depois** da quebra (intervenção ou liquidação) | **Antes**, enquanto o banco funciona |
| Quem protege | O credor (cliente) | O sistema (liquidez e política monetária) |
| Natureza | Garantia com limites | Exigência do BC sobre o banco |
| Conta individual | Sim, por titular | Não |

- "O FGC age depois que o banco quebra e protege você, com limite. O compulsório age antes, enquanto o banco funciona, e é uma obrigação do banco com o Banco Central. Um não é o outro, e nenhum dos dois é garantia ilimitada do governo."

> **➕ FGC: R$ 250 mil por CPF por conglomerado, R$ 1 milhão a cada 4 anos, só depois da quebra.**

**🔗 Ponte:** "Já que comparamos, vamos abrir o compulsório."

---

## 3.6 Depósito compulsório — CPA 2.4.1.2.2

### O que é

- "Compulsório é a parte dos depósitos que o banco é obrigado a deixar parada no Banco Central. É regra de segurança e de política monetária, não um seguro para o cliente."

### Função e objetivo

- "Ele tem três funções: dar liquidez e segurança ao sistema, e ajudar o Banco Central a controlar quanto dinheiro circula. Quando o BC aumenta o compulsório, sobra menos dinheiro para os bancos emprestarem; quando reduz, sobra mais."
- "Existe compulsório sobre depósitos à vista, poupança e depósitos a prazo. E não confunda com direcionamento obrigatório, que é a obrigação de emprestar parte dos recursos para setores específicos, como o crédito rural."

### Como funciona no corte (recursos à vista)

| Regra | Conteúdo |
| --- | --- |
| Alíquota | **21%** sobre o VSR, após dedução de **R$ 500 milhões** (quadro oficial de 20/08/2026) |
| Período de cálculo | **Duas semanas** |
| Cumprimento | Média de **100%** da exigência no período |
| Posição diária mínima | **65%** da exigência |
| Dispensa | Exigência de até **R$ 500.000** |
| Forma | Em espécie e **sem remuneração** |
| Deficiência | Custo de **Selic + 4% a.a.** |
| Novidade | Res. BCB 551/2026: dedução ligada a antecipações de contribuições ao FGC |

- "Para recursos à vista, a alíquota é de 21% sobre o VSR, o Valor Sujeito a Recolhimento, que é a base de cálculo: o total desses depósitos no banco. Antes de aplicar os 21%, desconta-se uma parcela de 500 milhões de reais."
- "Na prática, o cálculo é feito em períodos de duas semanas. Na média, o banco tem de cumprir 100% da exigência e, em nenhum dia, pode ficar abaixo de 65%. Exigência de até 500 mil é dispensada. O dinheiro fica parado sem render, e quem não cumpre paga um custo de Selic mais 4% ao ano."
- "Uma novidade de 2026: o banco pode deduzir da exigência valores que antecipou ao FGC, dentro das condições da norma."

### ➕ Exemplo prático 2 — o compulsório de um banco (hipotético)

Banco com VSR de recursos à vista de R$ 2 bilhões.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `2000` `ENTER` `500` `-` | 🖥️ 1.500,00 | Base após a dedução (R$ milhões) |
| 2 | ⌨️ `21` `%` | 🖥️ 315,00 | Exigência: R$ 315 milhões |
| 3 | ⌨️ `65` `%` | 🖥️ 204,75 | Mínimo em qualquer dia: R$ 204,75 milhões |

- "Um banco tem 2 bilhões de depósitos à vista na base. Na HP, em milhões: 2.000 menos 500 de dedução dá 1.500. 21% disso são 315 milhões: essa é a exigência média. E 65% dos 315 dão 204,75 milhões: em nenhum dia o saldo no BC pode ficar abaixo disso. Repare que em nenhum momento entrou o saldo de um cliente. Os 21% são sobre a base do banco."
- 🔇 Valores hipotéticos, em R$ milhões, para ilustrar a mecânica. A dedução e a alíquota seguem o texto enviado (quadro oficial de 20/08/2026), sem reconferência nesta sessão.

### Aplicação

- "E o que sobra depois do compulsório não vira empréstimo automaticamente. Para emprestar, o banco precisa de capital, precisa avaliar o risco e precisa ter quem queira tomar crédito."

### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O compulsório garante o depósito do cliente" | Errado | Isso é o FGC |
| "Compulsório e direcionamento são a mesma coisa" | Errado | Recolher ao BC × emprestar a setores específicos |
| "21% do saldo de cada cliente vai para o BC" | Errado | Incide sobre a base do banco |
| "Todo recurso livre vira empréstimo" | Errado | O multiplicador é modelo teórico, não promessa |

- "Compulsório não é FGC, não é direcionamento e não é uma taxa sobre a sua conta. E o multiplicador de depósitos, aquela ideia de que o dinheiro se multiplica quando é reemprestado, é uma explicação da economia, não uma garantia de que todo depósito vira empréstimo."

> **➕ Compulsório: o banco recolhe, o BC controla a liquidez, e o cliente nem aparece na conta.**

**🔗 Ponte:** "Saímos do dinheiro parado e vamos para o dinheiro em movimento. O primeiro meio de pagamento do programa é o boleto."

---

## 3.7 Boleto bancário — CPA 2.4.1.3

### O que é

- "Boleto é um documento padronizado que serve para cobrar uma dívida, fazer uma proposta ou depositar na sua própria conta."

| Espécie | Para que serve | Detalhe |
| --- | --- | --- |
| Cobrança comum | Cobrar uma dívida | O credor original recebe |
| Cobrança dinâmico | Cobrar uma dívida que pode ser vendida | O recebedor pode mudar, por exemplo para um fundo que comprou a dívida |
| Proposta | Fazer uma oferta | Pagar é **opcional** e significa **aceitar** |
| Depósito e aporte | Pôr dinheiro na sua própria conta | Pagador e beneficiário são a mesma pessoa |

- "São quatro tipos. O de cobrança comum, em que o credor original recebe. O de cobrança dinâmico, em que o recebedor pode mudar quando a dívida é vendida, por exemplo a um fundo. O de proposta, em que pagar é opcional e quer dizer aceitar a oferta. E o de depósito, para colocar dinheiro na sua própria conta."

### Função e objetivo

- "O boleto padroniza a cobrança, registra a dívida numa base central e encaminha o pagamento até o banco do recebedor."

### Como funciona

**Beneficiário pede a emissão → dados registrados na base centralizada → boleto apresentado → pagador confere → pagamento liquidado**

- "Quem vai receber, chamado beneficiário, pede o boleto ao banco. Os dados vão para uma base central do sistema. Você recebe o boleto, confere e paga, e o pagamento segue para o banco de quem recebe."

- **A base prevalece sobre o papel**
  - "Se o PDF diz uma coisa e a base registrada diz outra, vale a base. A exceção é quando o sistema está fora do ar."

- **Boleto de proposta**
  - "O boleto de proposta tem de deixar claro três coisas: pagar é opcional, não pagar não gera protesto, cobrança nem nome sujo, e pagar significa aceitar a oferta."

- **Vencido e dia não útil**
  - "Boleto vencido pode ser pago sem pedir outro, porque a base calcula os juros e a multa. Se ele vence num feriado ou fim de semana, em regra dá para pagar no próximo dia útil sem encargos. Mas guias de imposto, como DARF, DAS, GPS e DAE, têm regras próprias."

#### ➕ Exemplo prático 3 — boleto pago com atraso (hipotético)

Boleto de R$ 1.000, multa de 2% e juros de mora de 1% ao mês, pro rata, pago com 10 dias de atraso.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `1000` `ENTER` `2` `%` | 🖥️ 20,00 | Multa |
| 2 | ⌨️ `STO` `1` | 🖥️ 20,00 | Guarda a multa |
| 3 | ⌨️ `1000` `ENTER` `1` `%` `30` `÷` `10` `×` | 🖥️ 3,33 | Juros de 10 dias (1% a.m. ÷ 30 × 10) |
| 4 | ⌨️ `RCL` `1` `+` `1000` `+` | 🖥️ 1.023,33 | Valor a pagar |

- "Um boleto de mil reais, multa de 2% e juros de 1% ao mês, pago com 10 dias de atraso. Na HP: mil, ENTER, 2, porcentagem, 20 de multa. Guardo na memória. Juros: mil, ENTER, 1, porcentagem, dá 10 reais por mês; divido por 30 e multiplico por 10 dias, 3,33. Somo a multa e o principal: 1.023,33. É essa conta que a base centralizada faz por você quando você paga o boleto vencido."
- 🔇 Multa e juros são hipotéticos e definidos no título. Nas relações de consumo, o CDC (art. 52, § 1º) limita a multa a 2%. Os juros pro rata em base 30 são convenção didática.

- **Valores**
  - "Os 250 mil reais do VR-Boleto mudam só a forma como o pagamento é liquidado entre os bancos. Não são valor máximo do boleto. E boleto de 10 mil reais ou mais não pode ser pago em dinheiro vivo, nem fracionado para driblar a regra. Isso ajuda a prevenir lavagem de dinheiro."

### Aplicação e segurança

- **Antes de pagar**
  - "Antes de pagar, confira no aplicativo quem vai receber, o banco, o valor e o vencimento. Boleto registrado não quer dizer cobrança verdadeira: o golpista também consegue registrar um boleto."

- **Boleto falso e QR Code Pix**
  - "Caiu num boleto falso? Avise o banco na hora, guarde os comprovantes e registre ocorrência. E, se o boleto tiver QR Code Pix, ao ler o código você está fazendo um Pix, com as regras do Pix, e não pagando o boleto pela compensação."

### O que a prova pode confundir: boleto × Pix × débito automático × DDA

| Instrumento | Como funciona | Quem autoriza |
| --- | --- | --- |
| Boleto | Cobrança registrada, liquidada pela compensação | Você, a cada pagamento |
| Pix (inclusive Pix Cobrança) | Pagamento instantâneo pelo SPI | Você, no canal Pix |
| Débito automático | Banco debita na data | Você autorizou antes, uma vez |
| DDA (Débito Direto Autorizado) | **Só apresenta** os boletos no app | Não paga sozinho |

- "No boleto, você confere e autoriza cada pagamento. No Pix, o pagamento é instantâneo, e até o Pix Cobrança com vencimento liquida como Pix. No débito automático, você autorizou antes e o banco debita na data. E o DDA, o Débito Direto Autorizado, só mostra no aplicativo os boletos emitidos no seu CPF. Apesar do nome, ele não paga sozinho."

> **➕ Boleto: a base registrada manda, o pagador confere e autoriza cada pagamento.**

**🔗 Ponte:** "Boleto, Pix e consulta de conta: quase tudo isso hoje acontece pelo celular. Vamos aos serviços digitais."

---

## 3.8 Serviços digitais — CPA 2.4.1.4

### O que é

- "Serviço digital é tudo o que o banco oferece por internet banking, aplicativo ou API. API é a sigla de Interface de Programação de Aplicações: a conexão direta entre dois sistemas, sem tela no meio."
- "Conta digital não é categoria da lei, é nome de mercado. E 'banco digital' pode ser banco de verdade ou instituição de pagamento. O que vale é a licença do Banco Central, não o nome no anúncio."

### Função e objetivo

- "Permite consultar, movimentar, contratar, pagar e compartilhar dados sem ir à agência, com segurança e informação."

### Como funciona

- **Segurança: os quatro pilares**
  - "O banco tem de confirmar que é você e proteger os dados. São quatro pilares. Integridade: os dados não podem ser alterados. Autenticidade: precisam ser verdadeiros e vir de quem diz que mandou. Confidencialidade: ficam em sigilo. Disponibilidade: o serviço precisa estar no ar. Para confirmar a sua identidade, usa senha, biometria ou token, aquele código temporário."

| Papel no Open Finance | O que faz |
| --- | --- |
| Transmissora | Envia os dados do cliente |
| Receptora | Recebe os dados |
| Detentora | Mantém a conta do cliente |
| Iniciadora | Dispara o pagamento sem guardar o dinheiro |
| Cliente | Dá o **consentimento**: livre, informado, prévio e com finalidade definida |

- **Open Finance**
  - "No Open Finance, o sistema de compartilhamento de dados e serviços entre instituições, cada um tem um papel. A transmissora envia os dados, a receptora recebe, a detentora é onde está a conta, e a iniciadora dispara um pagamento sem nunca segurar o dinheiro. Nada acontece sem o seu consentimento, que tem de ser livre, informado, prévio e para uma finalidade definida."

- **Autenticação na origem**
  - "Quando outro aplicativo inicia um pagamento da sua conta, você confirma no seu próprio banco. O app iniciador nunca recebe a sua senha."

- **Instituição de pagamento**
  - "A instituição de pagamento pode cuidar da sua conta de pagamento e fazer transações. Mas, só como instituição de pagamento, não pode emprestar dinheiro. Para emprestar, precisa de outra licença."

### Aplicação

- "Ser digital não tira os seus direitos de informação, segurança e atendimento. Pode haver custo, se estiver no contrato. E consultar a conta pela internet é serviço essencial gratuito para pessoa física na conta corrente."

### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Serviço digital só existe em banco digital" | Errado | Banco tradicional também oferece |
| "Open Finance é um aplicativo" | Errado | É um sistema de compartilhamento, com regras do BC |
| "A senha do cliente garante a segurança cibernética do banco" | Errado | Autenticação é uma parte; a segurança do sistema é dever do banco |
| "Instituição de pagamento é instituição financeira" | Errado | Licenças e regras diferentes |
| "O limite da conta simplificada é o limite do Pix" | Errado | São regras diferentes |

> **➕ Digital é o canal, não a licença. E nada no Open Finance acontece sem o seu consentimento.**

**🔗 Ponte:** "O serviço digital mais usado do país é o Pix. Vamos a ele, em quatro partes."

---

## 3.9 Pix — CPA 2.4.1.5

### Visão geral

- "Pix não é um aplicativo. É um arranjo de pagamentos: um conjunto de regras criado e regulado pelo Banco Central. Você usa pelo app do seu banco ou de um iniciador autorizado."
- 🔇 [ESCREVA na lousa] **PIX = ARRANJO + TRANSAÇÃO INSTANTÂNEA** · [MANTENHA] **SPI = liquidação** · **DICT = diretório de chaves e contas**
- "Deixe duas siglas no quadro. SPI é o Sistema de Pagamentos Instantâneos, do Banco Central, onde o dinheiro passa de um banco para o outro. DICT é o Diretório de Identificadores de Contas Transacionais, que guarda as chaves e diz a qual conta cada chave pertence."

---

### 3.9.1 Pix: definição e objetivos — CPA 2.4.1.5.1

- **Definição**
  - "Pelo regulamento, Pix é ao mesmo tempo o arranjo, ou seja, as regras, e a transação em si."

- **Pagamento instantâneo**
  - "Instantâneo quer dizer que a ordem sai e o dinheiro fica disponível para quem recebe em tempo real, a qualquer hora, todo dia. Mas com controles, manutenção e bloqueios de segurança."

| Objetivos do Pix |
| --- |
| Melhor experiência para quem paga e recebe |
| Mais competição entre instituições |
| Menor custo |
| Inclusão financeira |
| Digitalização dos pagamentos |
| Disponibilidade 24/7 |

- "O Pix nasceu para melhorar a experiência de quem paga e recebe, aumentar a concorrência, baixar custos, incluir mais gente no sistema financeiro e digitalizar os pagamentos, a qualquer hora."

- **Formas de iniciar**
  - "Você pode fazer um Pix pela chave, digitando os dados da conta, lendo um QR Code, colando o código do Copia e Cola ou por um app via Open Finance."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Pix, SPI e DICT são a mesma coisa" | Errado | Arranjo × liquidação × diretório |
| "Funcionar 24/7 significa não ter limite nem bloqueio" | Errado | Há limites e controles |
| "Pix instantâneo pode ser cancelado pelo pagador" | Errado | É irrevogável após a liquidação |

> **➕ Pix é regra do BC, não aplicativo.**

**🔗 Ponte:** "Agora, o caminho do Pix por dentro."

---

### 3.9.2 Pix: funcionamento, chaves, custos, tarifas e liquidação — CPA 2.4.1.5.2

#### O caminho do Pix

| # | Etapa | Quem faz |
| --- | --- | --- |
| 1 | Informa a chave | Pagador |
| 2 | Consulta o DICT e mostra o nome do recebedor | PSP do pagador |
| 3 | Confere e autoriza | Pagador |
| 4 | Autenticação, saldo, limite e antifraude | PSP do pagador |
| 5 | Liquidação nas Contas PI (se os PSPs forem diferentes) | SPI (BC) |
| 6 | Crédito na conta do recebedor | PSP do recebedor |

- "Você informa a chave. O seu banco, que aqui se chama PSP, prestador de serviço de pagamento, consulta o DICT e mostra o nome de quem vai receber. Você confere e autoriza. O banco checa senha, saldo, limite e fraude. Se os bancos forem diferentes, o SPI liquida na hora, nas Contas PI, que são as contas dos bancos no Banco Central. E o banco de quem recebe credita o valor."

- **Irrevogável**
  - "Depois que o SPI liquidou, o Pix é irrevogável. Pode haver devolução voluntária, o MED ou um novo Pix no sentido contrário, mas não existe cancelar por conta própria."

#### Chave Pix ≠ conta

| Regra | Conteúdo |
| --- | --- |
| Tipos | CPF, CNPJ, telefone, e-mail, aleatória |
| Natureza | Apelido da conta: não guarda dinheiro |
| Obrigatoriedade | Não é obrigatória: dá para fazer Pix pelos dados da conta |
| Quantidade | Até **5 por conta PF** e **20 por conta PJ** |

- "A chave pode ser CPF, CNPJ, telefone, e-mail ou um código aleatório. É só um apelido da conta: não guarda dinheiro, e você pode fazer Pix sem chave, usando os dados da conta. Pessoa física pode ter até 5 chaves por conta; empresa, até 20."

#### Limites e segurança

| Regra | Conteúdo |
| --- | --- |
| Limite noturno PF → PF | **R$ 1.000** entre **20h e 6h** (ou 22h–6h, se o banco oferecer), salvo pedido do usuário |
| Recebedor PJ | Limite definido pela instituição |
| Dispositivo não cadastrado (pessoa natural) | Até **R$ 200 por transação** e **R$ 1.000 por dia**, salvo exceções |
| Bloqueio cautelar | Até **72 horas**, por suspeita de fraude |
| MED (Mecanismo Especial de Devolução) | Pedido em até **80 dias**; sem garantia; não cobre erro ou arrependimento |

- "À noite, das 20h às 6h, ou das 22h às 6h se o banco oferecer, o Pix de pessoa física para pessoa física tem limite de mil reais, a não ser que você peça para mudar. Para pagar empresa, quem define o limite é o banco."
- "Num celular novo, ainda não cadastrado, o limite é de 200 reais por Pix e mil por dia. Não transporte esse número para empresa ou para outras situações sem conferir."
- "Se houver suspeita de fraude, o banco pode segurar o dinheiro por até 72 horas. O MED, Mecanismo Especial de Devolução, pode ser pedido em até 80 dias. Mas ele não é seguro: depende de análise e de ainda haver saldo na conta do golpista, e não vale para erro de digitação, arrependimento ou briga comercial."

#### Custos e tarifas

| Situação | Regra |
| --- | --- |
| PF enviando ou recebendo por transferência | Em regra, **grátis** |
| Exceções para PF | Pix por canal presencial ou telefone com meio eletrônico disponível · recebimento com finalidade comercial em certos casos · Pix Saque/Troco além da franquia |
| Pix Saque e Pix Troco | **8 por mês grátis** para PF; PJ pode pagar desde o primeiro |

- "Para pessoa física, em regra, enviar e receber Pix é de graça. As exceções: fazer pelo caixa ou pelo telefone tendo o app disponível, receber como venda comercial em certos casos, e passar da franquia de Pix Saque ou Troco. Pix Saque e Pix Troco são formas de sacar dinheiro numa loja: até 8 por mês grátis para pessoa física; empresa pode pagar desde o primeiro."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A chave Pix é a conta" | Errado | É apelido da conta |
| "O SPI procura a chave" | Errado | O DICT procura; o SPI liquida |
| "O MED é um seguro contra golpe" | Errado | Depende de análise e de saldo |
| "O limite noturno de R$ 1.000 vale para empresas" | Errado | Vale para PF → PF |
| "Pix instantâneo dispensa controles" | Errado | Há limites, autenticação e bloqueio cautelar |

> **➕ O DICT acha, o SPI liquida, e o MED tenta devolver, mas não garante.**

**🔗 Ponte:** "Sabendo como o Pix funciona, vamos ver para que ele serve no dia a dia."

---

### 3.9.3 Pix: aplicações, transferências e pagamentos — CPA 2.4.1.5.3

- **Usos**
  - "O Pix serve para quase tudo: mandar dinheiro, comprar, pagar fornecedor, imposto, multa, fatura e até FGTS, desde que quem recebe aceite Pix."

- **A finalidade importa**
  - "A finalidade faz diferença. Transferir é mover dinheiro entre contas. Comprar é pagar um produto ou serviço. Isso pode mudar a tarifa e os controles."

| Modalidade | Como funciona |
| --- | --- |
| Pix Cobrança imediato | Cobrança para pagar na hora |
| Pix Cobrança com vencimento | Com data, juros, multa e desconto |
| QR Code estático | Reutilizável, serve para vários pagamentos (ex.: padaria) |
| QR Code dinâmico | Identifica uma cobrança só, facilita a conferência |
| Pix Copia e Cola | O conteúdo do QR Code, colado em vez de lido |

- "O Pix Cobrança pode ser imediato ou com vencimento, com juros e multa. O QR Code estático serve para vários pagamentos, como o da padaria. O dinâmico é de uma cobrança só, o que facilita a conferência. E o Copia e Cola é o mesmo código, só que colado em vez de lido pela câmera."

| | Pix | TED | DOC |
| --- | --- | --- | --- |
| Velocidade | Instantâneo | No mesmo dia, dentro do horário | Extinto |
| Disponibilidade | 24/7 | Horário e regras próprias | — |
| Usa chave/DICT | Sim | Não | — |

- "Pix é instantâneo e funciona sempre. A TED tem horário e regras próprias e não usa chave. E o DOC é coisa do passado: deixou de existir. Não traga regra do DOC para o Pix."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Pix Cobrança com vencimento é um boleto" | Errado | Liquida como Pix |
| "Ler o QR Pix de um boleto é pagar pela compensação" | Errado | É um Pix |
| "A tarifa do Pix é um imposto" | Errado | Tarifa é preço do serviço do banco |
| "Devolver um Pix voluntariamente é usar o MED" | Errado | O MED é mecanismo específico de fraude |

> **➕ Pix Cobrança tem cara de boleto, mas é Pix.**

**🔗 Ponte:** "E na empresa? O Pix vira ferramenta de caixa, com regras próprias."

---

### 3.9.4 Pix na pessoa jurídica — CPA 2.4.1.5.4

- **Ferramenta de caixa**
  - "Para a empresa, o Pix é ferramenta de caixa. Com a API Pix, a conexão direta com o sistema do banco, ela gera cobranças, confirma recebimentos e faz a conciliação, que é bater o que vendeu com o que recebeu."

- **Aplicações**
  - "A empresa recebe vendas por chave ou QR Code, paga fornecedores e impostos, pode pagar salários, se o banco oferecer, e integrar tudo ao ERP. ERP é o sistema de gestão da empresa, que junta estoque, vendas e financeiro."

| Tema | Regra para PJ |
| --- | --- |
| Tarifa | Pode ser cobrada no envio e no recebimento (Res. BCB 19/2020), sem preço nacional único |
| MEI e empresário individual | Seguem a regra da **pessoa física** |
| Limite noturno | Não há o limite universal de R$ 1.000: limites definidos pela instituição |
| API, QR dinâmico, lote | Variam de banco para banco |

- ✏️ "Para empresa, o banco pode cobrar para enviar e receber Pix, conforme contrato e tabela. Não existe preço único no país. Já o MEI, o microempreendedor individual, e o empresário individual seguem a regra da pessoa física."
- "A empresa não tem aquele limite noturno de mil reais da pessoa física: quem define é o banco, conforme o risco. E nem todo banco oferece API ou pagamento em lote do mesmo jeito."
- 🔇 Retirada a menção à EIRELI: a modalidade foi extinta (Lei 14.195/2021, transformação em SLU).

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Pix de empresa é sempre grátis" | Errado | Pode ser tarifado |
| "A empresa é obrigada a usar o CNPJ como chave" | Errado | Pode usar outras chaves |
| "A API Pix é gratuita em todos os bancos" | Errado | Depende do contrato |
| "Receber por Pix dispensa nota fiscal" | Errado | O meio de pagamento não muda as obrigações fiscais |
| "Todo valor recebido por Pix é renda tributável" | Errado | O que importa é a natureza da operação |

> **➕ Pix na empresa: pode ter tarifa, não tem o limite noturno da PF e não muda nenhuma obrigação fiscal.**

**🔗 Ponte:** "Falamos várias vezes de tarifa. Vamos organizar as regras."

---

## 3.10 Tarifas — CPA 2.4.1.6

### O que é

- "Tarifa é o preço do serviço do banco. Não é imposto. E só pode ser cobrada se estiver dentro da regra, prevista no contrato, se você pediu ou autorizou o serviço e se ele foi de fato prestado."

### Função e objetivo

- "O banco é remunerado, mas não pode cobrar o que quiser. A transparência deixa você comparar o serviço avulso com o pacote."

### Como funciona (Res. CMN 3.919, pessoa física)

| Grupo | Regra |
| --- | --- |
| **Essenciais** | Gratuitos até a quantidade da norma |
| **Prioritários** | Cobrados com nome e regra padronizados |
| **Especiais** | Seguem lei própria (ex.: crédito rural, microcrédito) |
| **Diferenciados** | Contratados à parte, com condições claras |

- "Para pessoa física, a Resolução 3.919 divide os serviços em quatro grupos. Essenciais: gratuitos até a quantidade da norma. Prioritários: cobrados com nome e regra padronizados, para facilitar a comparação entre bancos. Especiais: seguem lei própria. Diferenciados: contratados à parte, com condições claras."
- "O banco tem de divulgar a tabela de preços, e ninguém é obrigado a contratar pacote."

### Aplicação

- "Confira o contrato, o extrato e a tabela. Se cobraram algo que você não contratou, não usou ou que deveria ser grátis, peça explicação ou reembolso ao banco."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Tarifa bancária é um tributo" | Errado | É preço de serviço |
| "O cliente é obrigado a contratar pacote" | Errado | Pacote é opcional |
| "Serviço essencial é ilimitado" | Errado | Gratuito até a quantidade da norma |
| "A tarifa tem preço nacional único" | Errado | Cada banco define o seu |
| "Todas as contas têm a mesma lista de gratuidades" | Errado | Conta corrente, salário, de pagamento e Pix têm regras próprias |

> **➕ Tarifa é preço: precisa de regra, contrato, pedido e serviço prestado.**

**🔗 Ponte:** "Quais serviços são gratuitos e como se conta a franquia? É o próximo item."

---

### 3.10.1 Critérios para cobrança e gratuidades — CPA 2.4.1.6.1

#### Serviços essenciais gratuitos na conta corrente PF

| Serviço | Quantidade gratuita |
| --- | --- |
| Cartão de débito | 1 (fornecimento) |
| Saques | **4 por mês** |
| Transferências entre contas da mesma instituição | **2 por mês** |
| Extratos | **2 por mês** |
| Consultas pela internet | Sem limite |
| Compensação de cheques | Sem limite |
| Folhas de cheque | **10 por mês**, se cumprir os requisitos |
| Extrato anual de tarifas | 1 por ano |
| Conta exclusivamente eletrônica | Serviços pelos canais eletrônicos |

- "A cesta gratuita da conta corrente de pessoa física tem: cartão de débito, quatro saques por mês, duas transferências para contas do mesmo banco, dois extratos, consultas pela internet, compensação de cheques, até dez folhas de cheque, se você cumprir os requisitos, e o extrato anual de tarifas. E, se a conta é só eletrônica, os serviços pelos canais eletrônicos."

#### Regras de contagem

- "A quota é da conta, e não de cada titular, e não passa para o mês seguinte. Saques no caixa eletrônico feitos em até 30 minutos contam como um só. E, se a conta é eletrônica e você escolhe o guichê, o banco pode cobrar já da primeira vez, a não ser que o canal eletrônico esteja fora do ar."

#### Conta-salário e conta de pagamento

| Conta | Regra |
| --- | --- |
| Conta-salário | Gratuidades próprias (tópico 3.3) |
| Conta de pagamento pós-paga (ex.: cartão) | Serviços prioritários padronizados |
| Conta de pagamento pré-paga (carteira digital) | Serviços diferenciados, com mais flexibilidade |

- "A conta-salário tem a sua própria lista grátis, que já vimos. A conta de pagamento pós-paga, como a do cartão de crédito, tem serviços padronizados. A pré-paga, de carteira digital, tem mais liberdade. Não copie a cesta da conta corrente para todas."

#### Pacotes e aviso de aumento

| Regra | Conteúdo |
| --- | --- |
| Pacote | Opcional, com contrato específico; preço **não pode ser maior** que a soma das tarifas avulsas |
| Aviso de criação ou aumento | **45 dias** para cartão de crédito; **30 dias** para os demais |
| Intervalos | Certas mudanças só depois de **180** ou **365 dias** |

- "O pacote é opcional, precisa de contrato próprio e não pode custar mais do que a soma dos serviços avulsos que estão nele. Para criar ou aumentar tarifa, o banco avisa com 45 dias de antecedência no cartão de crédito e 30 dias nos demais. E alguns aumentos só podem acontecer depois de 180 ou 365 dias."

#### ➕ Exemplo prático 4 — o pacote compensa? (hipotético)

Uso mensal: 6 saques e 4 transferências para outros bancos. Tarifas avulsas: saque R$ 2,50 (acima dos 4 grátis) e transferência R$ 9,00. Pacote oferecido: R$ 39,90.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `6` `ENTER` `4` `-` `2,5` `×` | 🖥️ 5,00 | Saques acima da franquia |
| 2 | ⌨️ `STO` `1` | 🖥️ 5,00 | Guarda |
| 3 | ⌨️ `4` `ENTER` `9` `×` | 🖥️ 36,00 | Transferências para outros bancos |
| 4 | ⌨️ `RCL` `1` `+` | 🖥️ 41,00 | Custo avulso no mês |
| 5 | ⌨️ `39,9` `-` | 🖥️ 1,10 | Economia mensal com o pacote |

- "Um cliente faz 6 saques e 4 transferências para outros bancos por mês. Os 4 primeiros saques são grátis: sobram 2 pagos, a 2,50, 5 reais. As 4 transferências, a 9 reais, dão 36. Somando, 41 reais avulsos. O pacote custa 39,90: compensa por 1,10. Mas, se num mês ele sacar menos, a vantagem some. Pacote só vale a pena para quem usa."
- 🔇 Preços hipotéticos. Cada banco tem a sua tabela.

#### Pix

- "O Pix tem regra própria, a que já vimos: pessoa física, MEI e empresário individual, em regra, não pagam. Empresa pode pagar desde o primeiro."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A conta corrente dá 5 saques grátis por mês" | Errado | 4 na conta corrente; 5 **por crédito** na conta-salário |
| "Essencial é qualquer serviço que o cliente queira" | Errado | É a lista da norma |
| "Cada titular de conta conjunta tem a própria franquia" | Errado | A franquia é por conta |
| "30 dias é o prazo da portabilidade salarial" | Errado | 30 dias é aviso de tarifa; a portabilidade leva até 10 dias úteis |
| "A gratuidade do Pix PF vale para empresa" | Errado | PJ pode ser tarifada |

> **➕ Quatro saques na conta corrente, cinco por salário na conta-salário, oito Pix Saque por mês.**

**🔗 Ponte:** "Se houver problema com tarifa ou serviço, onde o cliente reclama e como deve ser atendido? Vamos ao atendimento bancário."

---

## 3.11 Atendimento bancário — CPA 2.4.1.7

### O que é

- "Atendimento bancário é tudo o que o banco oferece em agência, caixa, terminal e canais remotos, como telefone e aplicativo."

### Função e objetivo

- "O objetivo é atender de forma justa, clara, segura e acessível, sem criar obstáculo sem motivo."

### Como funciona

- **Res. CMN 4.949**
  - "A Resolução 4.949 pede transparência, cuidado, sigilo e tratamento justo, e manda informar direitos, custos, riscos e prazos."

| Canal | Papel | Regra |
| --- | --- | --- |
| SAC | Primeira porta | Atendimento inicial |
| **Ouvidoria** (Res. CMN 4.860) | Segunda instância dentro do banco | Gratuita, com protocolo, resposta em até **10 dias úteis**, prorrogáveis **uma vez** por igual período, com justificativa |

- "A ouvidoria é a segunda instância dentro do banco, para quando o SAC não resolve. É gratuita, dá protocolo e responde em até 10 dias úteis, podendo prorrogar uma vez, com justificativa."

### Atendimento presencial

- "Nenhum banco é obrigado a ter agência. Mas, se tem uma aberta ao público, não pode recusar ou dificultar o atendimento no balcão ou no caixa, mesmo tendo aplicativo."
- "Isso vale até para quem não é cliente. O banco não pode exigir valor mínimo ou máximo, limitar quantos boletos você paga ou recusar dinheiro vivo, salvo exceção legal, como o boleto de 10 mil reais ou mais que vimos."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Todo banco é obrigado a ter agência" | Errado | Não há obrigação geral |
| "Quem tem app pode ser recusado no caixa" | Errado | Vedado dificultar o atendimento presencial |
| "Lei de fila define o horário da agência" | Errado | Fila é municipal; horário é norma do CMN |
| "SAC e ouvidoria são o mesmo canal" | Errado | Primeira e segunda instância |

> **➕ SAC é a primeira porta, ouvidoria é a segunda, e ter app não fecha o caixa.**

**🔗 Ponte:** "Quanto tempo a agência precisa ficar aberta, quanto se espera na fila e quem tem prioridade? Vamos aos detalhes."

---

### 3.11.1 Horários, filas, atendimento presencial e dias sem atendimento — CPA 2.4.1.7.1

#### Horário mínimo (Res. CMN 4.880/2020)

| Situação | Regra |
| --- | --- |
| Bancos múltiplos com carteira comercial, bancos comerciais e Caixa | Mínimo de **5 horas ininterruptas**, cobrindo **12h–15h** de Brasília |
| Quarta-Feira de Cinzas, 24/12 e casos excepcionais | Mínimo de **2 horas** |
| Mudança de horário | Aviso com **30 dias**, salvo ampliação |
| Último dia útil do ano | **Sem atendimento ao público**; só operações entre instituições |

- "Agência de banco comercial, de banco múltiplo com carteira comercial e da Caixa tem de abrir pelo menos 5 horas seguidas, sempre cobrindo das 12h às 15h, horário de Brasília. Na Quarta-Feira de Cinzas, na véspera de Natal e em casos especiais, o mínimo é de 2 horas. Mudança de horário tem de ser avisada com 30 dias, a não ser que seja para ampliar. E, no último dia útil do ano, a agência não abre para o público: só funcionam as operações entre os bancos."

#### Dias não úteis

- "Para o mercado financeiro, não são dias úteis: sábados, domingos, feriados nacionais, segunda e terça de Carnaval e Corpus Christi. Feriado estadual ou municipal depende da lei local. E o calendário da Febraban é orientação do setor, não substitui a regra do Conselho Monetário."

#### Filas

- "Não existe um tempo de fila nacional. Quem define é o município, e o Supremo confirmou isso no Tema 272. Não use o número de uma cidade para outra."
- "E o STJ decidiu, no Tema 1.156, que só esperar além do prazo não dá direito automático a indenização por dano moral. É preciso provar o prejuízo. A multa da lei local continua valendo."

#### Prioridade legal

| Quem tem prioridade |
| --- |
| Pessoas com deficiência |
| Pessoas com transtorno do espectro autista (TEA) |
| Idosos a partir de 60 anos |
| Gestantes e lactantes |
| Pessoas com criança de colo |
| Pessoas obesas ou com mobilidade reduzida |
| Doadores de sangue (depois dos demais prioritários, com comprovante de até 120 dias) |

- "Têm prioridade: pessoas com deficiência, pessoas com autismo, idosos a partir de 60 anos, gestantes, lactantes, quem está com criança de colo, pessoas obesas ou com mobilidade reduzida e doadores de sangue. Os doadores vêm depois dos demais prioritários e precisam de comprovante de doação de até 120 dias."

#### O que a prova pode confundir: horário × fila

| | Horário bancário | Tempo de fila |
| --- | --- | --- |
| Quem define | **CMN** (Res. 4.880), regra nacional | **Município** (Tema 272 do STF) |
| Conteúdo | 5h ininterruptas, incluindo 12h–15h | Tempo máximo, aferição e multa |

- "Horário de agência é regra nacional do Conselho Monetário. Tempo de fila é regra do município. Uma não substitui a outra."

> **➕ Horário é nacional, fila é municipal.**

**🔗 Ponte:** "Fechamos as contas no Brasil. Agora vamos atravessar a fronteira: conta internacional."

---

## 3.12 Conta internacional — CPA 2.4.2

### O que é

- "Conta internacional, conta global, conta em dólar: são nomes de marketing. Sozinhos, não dizem o que o produto é."

| As quatro perguntas | Por quê |
| --- | --- |
| 1. Onde está o saldo: no Brasil ou no exterior? | Define a lei aplicável e a proteção |
| 2. Em qual moeda? | Define se há câmbio e risco cambial |
| 3. Quem mantém a conta: banco brasileiro, instituição de pagamento ou banco estrangeiro? | Define a licença e se há FGC |
| 4. Houve câmbio, eFX, cartão, remessa ou investimento? | Define IOF e IR |

- "Para descobrir o que é, faça quatro perguntas. O dinheiro está no Brasil ou fora? Em que moeda? Quem guarda a conta: banco brasileiro, instituição de pagamento ou banco estrangeiro? E houve troca de moeda, cartão, remessa ou investimento?"

| Estrutura possível | Exemplo |
| --- | --- |
| Conta em reais com serviços internacionais | Conta brasileira com cartão internacional |
| Conta em moeda estrangeira no Brasil | Só nas hipóteses que a regra permite |
| Conta no exterior | Conta num banco estrangeiro |
| Serviço eFX | Empresa de pagamentos e transferências internacionais |

- "Atrás do nome pode estar uma conta em reais no Brasil com cartão internacional, uma conta em moeda estrangeira no Brasil, nos casos que a regra permite, uma conta de verdade no exterior ou um serviço eFX. eFX é o serviço de pagamento ou transferência internacional prestado por empresas autorizadas, sem que você abra conta lá fora."

### Função e objetivo

- "Facilita pagar, receber e guardar valor em outra moeda. Mas não tira o risco de câmbio, os custos nem os impostos."

### Como funciona

- "Conta em reais não guarda dólar. Quando você usa o cartão lá fora, há conversão e custo. Conta no exterior segue as regras do outro país, mas, se você mora no Brasil, continua tendo que declarar e pagar imposto aqui. E conta de pagamento não tem FGC: tem a proteção da Lei 12.865, que separa o seu dinheiro do patrimônio da empresa."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Conta internacional está sempre no exterior" | Errado | Pode ser conta em reais no Brasil |
| "Conta em reais com cartão internacional guarda dólares" | Errado | Converte no uso |
| "Conta de pagamento é conta de depósito" | Errado | Regras e proteções diferentes |
| "Supervisão do BC garante saldo e rendimento" | Errado | Supervisão não é garantia |
| "O nome do produto prova onde está o dinheiro" | Errado | Valem as quatro perguntas |

> **➕ Conta internacional: o nome não diz nada; as quatro perguntas dizem tudo.**

**🔗 Ponte:** "Que facilidades essas contas oferecem, e como comparar o custo de verdade?"

---

### 3.12.1 Principais facilidades e inovações — CPA 2.4.2.1

- "São recursos que podem vir junto com a conta. Cada um depende do produto, da instituição, do país e do contrato. Exemplos: cartão para compras lá fora, envio e recebimento de dinheiro, transferência para a sua conta no exterior, saques, conta com várias moedas, meios de pagamento locais e acompanhamento pelo aplicativo."

- ✏️ **Res. BCB 561/2026**
  - "Uma novidade: a Resolução BCB 561 amplia o que o eFX pode fazer, incluindo transferências para investimento de até 10 mil dólares por operação. Na data de corte deste material ela ainda não estava valendo, mas passou a valer em 1º de outubro de 2026."
  - 🔇 Mantido o conteúdo do texto enviado. A vigência de 01/10/2026 já passou na data desta gravação; o texto da resolução não foi reaberto.

#### VET — Valor Efetivo Total

**VET = [(valor em moeda estrangeira × taxa de câmbio) + IOF + tarifas] ÷ valor em moeda estrangeira**

- "O VET, Valor Efetivo Total, junta a taxa de câmbio, o IOF e as tarifas num número só, em reais por unidade de moeda estrangeira. É ele que você compara entre instituições, e não só a cotação do anúncio."

#### ➕ Exemplo prático 5 — calculando o VET (hipotético)

Compra de US$ 1.000 em espécie, taxa de R$ 5,40, IOF de 3,5% e tarifa de R$ 20.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `1000` `ENTER` `5,4` `×` | 🖥️ 5.400,00 | Valor em reais pela taxa |
| 2 | ⌨️ `3,5` `%` | 🖥️ 189,00 | IOF |
| 3 | ⌨️ `+` `20` `+` | 🖥️ 5.609,00 | Total pago |
| 4 | ⌨️ `1000` `÷` | 🖥️ 5,61 | VET: R$ 5,609 por dólar |

- "Comprar mil dólares a 5,40: na HP, mil vezes 5,4 dá 5.400. IOF de 3,5% sobre os reais: 189. Somo o IOF e mais 20 de tarifa: 5.609. Divido por mil: o VET é 5,609 por dólar. A cotação anunciada era 5,40, mas o custo real é quase 21 centavos mais caro por dólar. Por isso se compara o VET."
- 🔇 Com f 2, o visor mostra 5,61; com f 3, 5,609.

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "VET é a taxa de câmbio anunciada" | Errado | Inclui IOF e tarifas |
| "eFX é conta no exterior" | Errado | É serviço de pagamento internacional |
| "Toda facilidade do app é direito do cliente" | Errado | Depende do contrato |
| "US$ 10.000 é limite geral do câmbio" | Errado | Vale só para aquela modalidade de eFX |

> **➕ Compare VET, não cotação.**

**🔗 Ponte:** "O IOF apareceu dentro do VET. Mas ele não tem uma alíquota única. Vamos às diferenças."

---

### 3.12.2 Cobrança de IOF com diferentes alíquotas — CPA 2.4.2.2

- "O IOF-câmbio é o imposto sobre a troca de moeda. Não existe uma alíquota única para 'conta internacional': ela depende da operação, da finalidade e da data."
- "As alíquotas vêm do Decreto 6.306, de 2007, com as mudanças recentes que passaram pelo Supremo, na ADC 96 e nas ADIs 7827 e 7839."

| Operação | Alíquota na data de corte |
| --- | --- |
| Remessa para **disponibilidade** no exterior | **3,5%** |
| Cartão de crédito/débito no exterior, saque no exterior, compra de **espécie**, cartão **pré-pago** de viagem | **3,5%** |
| Remessa para **investimento** | **1,10%** |
| Demais entradas de recursos | **0,38%** |
| Hipóteses específicas (ex.: receitas de exportação) | **0%** |

- "Mandar dinheiro para ficar disponível lá fora: 3,5%. Cartão de crédito no exterior, saque no exterior, dólar em espécie e cartão pré-pago de viagem: 3,5%. Para investir: 1,10%. Dinheiro que entra do exterior, em geral: 0,38%. E algumas operações, como receitas de exportação, podem ter alíquota zero."
- "Atenção: mandar para uma conta sua no exterior não faz a remessa virar investimento automaticamente."

#### ➕ Exemplo prático 6 — mesma remessa, finalidades diferentes (hipotético)

Remessa de R$ 50.000.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `50000` `ENTER` `3,5` `%` | 🖥️ 1.750,00 | IOF se for para disponibilidade |
| 2 | ⌨️ `x≷y` `1,1` `%` | 🖥️ 550,00 | IOF se for para investimento |
| 3 | ⌨️ `500` `ENTER` `5,4` `×` `3,5` `%` | 🖥️ 94,50 | IOF numa compra de US$ 500 no cartão, a R$ 5,40 |

- "Remessa de 50 mil reais. Se for para disponibilidade, 3,5%: 1.750 de IOF. Troco a ordem com x≷y para trazer os 50 mil de volta e calculo 1,1%: se for investimento, 550. A finalidade declarada muda o imposto em 1.200 reais. E uma compra de 500 dólares no cartão lá fora, a 5,40, gera 2.700 reais e 94,50 de IOF."

#### Como funciona

- "O imposto nasce quando a troca de moeda é liquidada. O banco cobra e repassa ao governo, e você informa a finalidade. Ter saldo parado na conta internacional não gera IOF por si só: o que gera é a operação de câmbio."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "IOF é tarifa do banco" | Errado | É imposto federal |
| "IOF-câmbio e IR são o mesmo imposto" | Errado | Troca de moeda × ganho |
| "Remessa para disponibilidade paga 1,10%" | Errado | 3,5%; 1,10% é investimento |
| "Exemplo antigo de 1,1% vale para qualquer remessa hoje" | Errado | Conferir a regra da data |
| "Comprar dólar em espécie é remessa para investimento" | Errado | 3,5% |

> **➕ IOF-câmbio: 3,5% para gastar ou guardar lá fora, 1,10% para investir, 0,38% para entrar.**

**🔗 Ponte:** "O IOF é sobre a troca de moeda. E o ganho do investimento lá fora? Aí entra o Imposto de Renda."

---

### 3.12.3 Investimento internacional e imposto de renda — CPA 2.4.2.3

- **O que é**
  - "Investimento internacional é aplicar dinheiro lá fora para render: fundo, ação, título ou participação numa empresa. Ter uma conta no exterior não é, sozinho, investimento."

| Situação | Tratamento no IR |
| --- | --- |
| Depósito **não remunerado** em instituição estrangeira autorizada | Variação cambial **isenta**, inclusive no uso ou saque |
| Conta com juros, *sweep*, fundo, título, ação, derivativo ou cripto | Pode ser **aplicação financeira** → tributada |
| Aplicação financeira direta (Lei 14.754/2023) | **15%** sobre a parcela anual líquida, **regime de caixa** |
| Juros e dividendos | Tributados quando **recebidos** |
| Ganho de capital, inclusive variação cambial do principal | Tributado na **venda ou resgate** |
| Valorização não realizada | Em regra, **não** tributada |
| Isenção de pequeno valor | **Não existe** desde 01/01/2024 (reafirmado na Solução de Consulta Cosit 130/2026) |

- "Se o dinheiro está parado numa conta lá fora, sem render juros, num banco autorizado no país dele, a valorização do dólar não paga Imposto de Renda, nem quando você usa ou saca."
- "Mas, se a conta rende juros ou aplica automaticamente o saldo num fundo, o chamado *sweep*, aí pode virar aplicação financeira, com imposto."
- "A Lei 14.754, de 2023, cobra 15% sobre o ganho líquido do ano. E vale o regime de caixa: o imposto aparece quando o dinheiro é recebido ou o ganho é realizado. Juros e dividendos pagam quando caem na conta. Ganho de capital, inclusive a variação do dólar sobre o valor investido, paga quando você vende ou resgata. Se só valorizou e você não vendeu, em regra ainda não paga."
- "E não existe mais isenção para ganhos pequenos lá fora: ela acabou em janeiro de 2024, e a Receita reafirmou isso em 2026."

#### ➕ Exemplo prático 7 — IR sobre a aplicação no exterior (hipotético)

No ano, o investidor recebeu o equivalente a R$ 4.000 em dividendos e teve R$ 6.000 de ganho realizado na venda de ações no exterior, sem perdas.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `4000` `ENTER` `6000` `+` | 🖥️ 10.000,00 | Parcela anual líquida |
| 2 | ⌨️ `15` `%` | 🖥️ 1.500,00 | IR devido na declaração anual |

- "Dividendos de 4 mil mais 6 mil de ganho realizado: 10 mil de parcela anual. 15%: 1.500 reais de imposto, apurados na declaração anual. Se ele tivesse ações que só valorizaram e não foram vendidas, essa valorização ainda não entraria na conta."
- 🔇 Simplificação: valores já convertidos para reais pela regra de conversão da lei, sem compensação de perdas e sem imposto pago no exterior.

#### Controladas no exterior

- "Se você controla uma empresa lá fora, o lucro dela pode ser tributado todo 31 de dezembro, mesmo sem você receber, a 15% sobre a sua parte. Depois, quando esse lucro for distribuído, não paga de novo."
- "Se a controlada não se enquadra nesse regime anual, o imposto vem quando o lucro é pago ou remetido. E existe a opção de transparência fiscal, que trata os bens da empresa como se fossem seus, mas ela é irrevogável enquanto você for dono."

#### Perdas e imposto pago no exterior

- "Prejuízo lá fora, comprovado, compensa ganho lá fora. E imposto pago no outro país só pode ser descontado aqui se houver tratado ou reciprocidade, e só até o limite da lei."

#### CBE × DAA

| | DAA | CBE |
| --- | --- | --- |
| O que é | Declaração de Ajuste Anual do IR | Declaração de Capitais Brasileiros no Exterior |
| Para quem | Receita Federal | **Banco Central** |
| Gera imposto? | Sim (apuração) | **Não** |
| Obrigatoriedade | Regras do IR | **Anual** a partir de **US$ 1 milhão** em 31/12; **trimestral** a partir de **US$ 100 milhões** |

- "A DAA é a sua declaração de Imposto de Renda. A CBE é outra coisa: uma declaração ao Banco Central sobre capitais brasileiros no exterior, que não cobra imposto nenhum. Ela é anual para quem tem 1 milhão de dólares ou mais em 31 de dezembro, e trimestral a partir de 100 milhões."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "IOF e IR incidem sobre a mesma coisa" | Errado | Troca de moeda × ganho |
| "Depósito parado no exterior é aplicação financeira" | Errado | Se não remunerado, a variação cambial é isenta |
| "A CBE é declaração de imposto" | Errado | É declaração ao BC |
| "O lucro anual da controlada é dividendo recebido" | Errado | É tributação do lucro apurado, mesmo sem distribuição |
| "O FGC protege investimento no exterior" | Errado | FGC é brasileiro e só cobre associadas |
| "Existe isenção para ganhos pequenos no exterior" | Errado | Acabou em 01/01/2024 |

> **➕ No exterior: 15% sobre o ganho realizado no ano; parado e sem juros, a variação do dólar é isenta; CBE é para o BC, não para a Receita.**

**🔗 Ponte:** "Para mandar dinheiro para fora, é preciso trocar moeda. Vamos ao mercado de câmbio."

---

## 3.13 Compra e venda de moeda estrangeira — CPA 2.4.3

### O que é

- **Câmbio e a regra de ouro**
  - "Câmbio é trocar uma moeda por outra. E a regra de ouro: compra e venda se olham pelo lado do banco. Quando o banco compra os seus dólares, é compra. Quando o banco vende dólares para você, é venda."

| Você quer... | Para o banco, é... |
| --- | --- |
| Levar dólares para viajar | **Venda** de moeda estrangeira |
| Trocar os dólares que sobraram por reais | **Compra** de moeda estrangeira |

- "A taxa é negociada entre você e a instituição, dentro das regras e dos controles contra lavagem de dinheiro."

### Como funciona

**Identificação → finalidade → documentos e risco → informar taxa, tributos, tarifas e VET → consentimento e registro → liquidação**

- "O banco identifica você, pergunta a finalidade, avalia documentos e risco, informa a taxa e o VET, registra o seu consentimento e liquida, entregando uma moeda e recebendo a outra."

| Regra | Conteúdo |
| --- | --- |
| Operação pronta | Liquidada em até **2 dias úteis** |
| Espécie, cheque de viagem e carga de cartão internacional | Liquidação no **mesmo dia** |
| Estoque | A instituição não é obrigada a ter espécie nem a aceitar qualquer cédula |
| Limite geral para o cliente | **Não existe** |
| Até R$ 10.000 de contravalor | Pagamento por **qualquer meio**, inclusive espécie |

- "Operação pronta é liquidada em até dois dias úteis. Dólar em espécie, cheque de viagem e carga de cartão internacional, no mesmo dia. E o banco não é obrigado a ter dólar em espécie disponível nem a aceitar qualquer cédula."
- "Não existe um valor máximo geral para comprar moeda. Até 10 mil reais, você pode pagar de qualquer jeito, inclusive em dinheiro vivo. Esse número não é limite da operação, e também não é o limite para declarar dinheiro na alfândega."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Quando o cliente compra dólar, a operação é de compra" | Errado | Para a instituição, é venda |
| "Taxa de câmbio e VET são a mesma coisa" | Errado | VET inclui IOF e tarifas |
| "R$ 10.000 é o limite de declaração na alfândega" | Errado | A alfândega usa US$ 10.000; os R$ 10.000 são do meio de pagamento |
| "Câmbio turismo e câmbio comercial são mercados juridicamente distintos" | Errado | São rótulos de mercado; o mercado de câmbio é um só |

> **➕ No câmbio, quem dá nome à operação é o banco.**

**🔗 Ponte:** "Quem pode fazer essa troca? Pode ser o banco direto ou alguém em nome dele: o correspondente."

---

### 3.13.1 Correspondente bancário/cambial — CPA 2.4.3.1

- **O que é**
  - "O correspondente é uma empresa contratada pelo banco para atender em nome dele, como uma lotérica ou uma agência de turismo. Ele não vira banco por causa disso. Podem ser empresas, empresários, associações, cartórios e até empresas públicas."

| Regra | Conteúdo |
| --- | --- |
| Escopo | O que o contrato permitir: compra e venda de espécie, cheque de viagem, carga de cartão pré-pago, transferências unilaterais, propostas de câmbio |
| Limite por operação | **US$ 3.000** |
| Se as duas moedas forem em espécie | **US$ 1.000** |
| VET e comprovante | Informados e entregues **na hora, sem custo** |
| Cobrança própria | **Vedada** |
| Substabelecer (repassar a outro) | **Vedado** |
| Responsabilidade | **Integral** da instituição contratante |

- "O contrato diz o que ele pode fazer: trocar dinheiro em espécie, vender cheque de viagem, carregar cartão pré-pago, mandar transferências e receber propostas de câmbio. Transferência unilateral é aquela sem contrapartida, como mandar dinheiro para um parente."
- "No correspondente, o limite é de 3 mil dólares por operação. Se tanto o dólar quanto o real forem em dinheiro vivo, cai para mil dólares."
- "Ele tem de informar o VET e entregar o comprovante na hora, sem custo. Não pode cobrar nada para si nem repassar o atendimento a outro. Quem responde por tudo é o banco que contratou. Por isso, confira sempre o nome desse banco."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O correspondente cambial é uma instituição autorizada" | Errado | É contratado; quem é autorizada é a instituição |
| "US$ 3.000 é o limite geral do câmbio" | Errado | É limite do correspondente |
| "O correspondente pode cobrar tarifa própria" | Errado | Vedado |
| "O correspondente responde sozinho pelos erros" | Errado | A instituição responde integralmente |

> **➕ Correspondente: atende em nome do banco, até US$ 3.000 (US$ 1.000 em espécie dos dois lados), sem tarifa própria.**

**🔗 Ponte:** "E quem é o banco por trás do correspondente? As instituições autorizadas a operar câmbio."

---

### 3.13.2 Instituições financeiras — CPA 2.4.3.2

- "Para operar câmbio, a instituição precisa de autorização do Banco Central. Bancos e Caixa podem fazer todas as operações. Corretoras, distribuidoras, corretoras de câmbio, financeiras e agências de fomento têm um escopo menor, definido na regra."

| Dever da instituição | Conteúdo |
| --- | --- |
| Identificar | Conhecer o cliente |
| Verificar a finalidade | Para classificar a operação corretamente |
| Orientar a classificação | Ajudar o cliente a declarar a natureza certa |
| Monitorar | Prevenção à lavagem de dinheiro e ao financiamento do terrorismo (PLD/FT) |
| Informar | Taxa, VET, tributos e tarifas |
| Guardar registros | Por pelo menos **10 anos** |

- "A instituição identifica o cliente, confere a finalidade, orienta a classificação, monitora para prevenir lavagem de dinheiro e financiamento do terrorismo, informa a taxa e o VET e guarda a documentação por pelo menos 10 anos."
- "Nem toda operação exige contrato assinado, mas o seu consentimento tem de poder ser provado. E o banco pode pedir mais ou menos documentos conforme o risco, a mesma abordagem baseada em risco que vimos em PLD."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Autorização do BC garante rentabilidade" | Errado | Autorização não é garantia |
| "Toda instituição autorizada faz qualquer operação de câmbio" | Errado | Escopo varia |
| "Fracionar operações para fugir de limite é permitido" | Errado | Vedado, e é sinal de alerta de lavagem |

> **➕ Autorizada responde; escopo varia; nunca fracionar.**

**🔗 Ponte:** "Último ponto: e o dólar que sobrou da viagem? O banco é obrigado a comprar de volta?"

---

### 3.13.3 Recompra de moeda estrangeira — CPA 2.4.3.3

- **Não há regra universal**
  - "Não existe regra que obrigue o banco a recomprar o dólar que sobrou da sua viagem, nem pela mesma cotação, nem num prazo fixo, nem como estorno."

- **É uma operação nova**
  - "Quando você devolve as cédulas, é uma operação nova: agora você vende e o banco compra, pela cotação do dia, com VET, impostos e controles."

| | Ida (viagem) | Volta (sobrou dólar) |
| --- | --- | --- |
| Para a instituição | **Venda** | **Compra** |
| Taxa | Do dia da ida | Do dia da volta, possivelmente diferente |
| Recusa de cédulas | — | Possível: falsidade, má conservação, falta de estoque, política própria |

- "Na ida, o banco vendeu dólar para você. Na volta, o banco compra de você. A taxa da volta pode ser diferente, e o banco pode recusar cédulas por falsidade, má conservação, falta de estoque ou política própria."

#### ➕ Exemplo prático 8 — o custo da ida e volta (hipotético)

Comprou US$ 1.000 com VET de R$ 5,609 (exemplo 5). Voltou com US$ 300 e vendeu ao banco a R$ 5,20.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `300` `ENTER` `5,609` `×` | 🖥️ 1.682,70 | Quanto custaram, na ida, os US$ 300 que sobraram |
| 2 | ⌨️ `300` `ENTER` `5,2` `×` | 🖥️ 1.560,00 | Quanto o banco paga na volta |
| 3 | ⌨️ `-` | 🖥️ 122,70 | Perda na ida e volta (custo da ida − valor da volta) |

- "Dos mil dólares que custaram 5,609 cada, sobraram 300. Na ida, esses 300 custaram 1.682,70. Na volta, o banco compra a 5,20: 1.560. Subtraindo, perda de 122,70. Essa é a diferença entre a taxa de venda e a de compra, mais o IOF e a tarifa da ida. Recompra não é estorno."
- 🔇 Valores hipotéticos. Na operação de volta, a entrada de recursos pode ter IOF próprio; o exemplo o ignora.

#### Cancelamento e devolução

- "Cancelar é desfazer a operação de comum acordo. Baixa é só um registro contábil. E aquela regra antiga do RMCCI, o antigo Regulamento do Mercado de Câmbio e Capitais Internacionais, sobre a sobra de dinheiro, era para empresas de transporte estrangeiras e foi revogada em 2014. Não vale para o turista."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O banco é obrigado a recomprar a moeda que vendeu" | Errado | Não há regra universal |
| "A recompra é feita pela mesma cotação da venda" | Errado | Nova operação, nova taxa |
| "Recompra é estorno da operação original" | Errado | É nova operação |
| "US$ 3.000, R$ 10.000 e US$ 10.000 são limites de recompra" | Errado | Correspondente, meio de pagamento e alfândega |

> **➕ Recompra é operação nova: nova taxa, novo VET, sem obrigação de aceitar.**

**🔗 Ponte (fecha o bloco):** "Fechamos o item 2.4. Você saiu da conta corrente, passou pelo salário, pelo depósito, pelo FGC e pelo compulsório, aprendeu a pagar com boleto e Pix, a ler tarifas e direitos de atendimento, e atravessou a fronteira com conta internacional e câmbio. A regra que amarra tudo: descubra qual é o produto de verdade antes de aplicar qualquer regra."

---

## ➕ Quadro de emergência do bloco 2.4

| Tema | Regra-chave |
| --- | --- |
| Conta corrente × salário | Cliente abre × empregador abre · cheque × sem cheque |
| Portabilidade salarial | Grátis · até 10 dias úteis · até 12h do dia do crédito · parcelas autorizadas ficam |
| Gratuidades | CC: 4 saques, 2 transf., 2 extratos · Salário: 5 saques por crédito · Pix Saque: 8/mês |
| FGC | R$ 250 mil por CPF/conglomerado · R$ 1 mi/4 anos · conjunta divide |
| Compulsório à vista | 21% do VSR após R$ 500 mi · média 100% · mínimo diário 65% |
| Boleto | Base prevalece · proposta é opcional · ≥ R$ 10 mil não em espécie |
| Pix | Arranjo do BC · DICT acha, SPI liquida · noturno PF R$ 1.000 · MED 80 dias · bloqueio 72h |
| Chaves | 5 PF · 20 PJ |
| Tarifas | Essenciais, prioritários, especiais, diferenciados · aviso 45 dias (cartão) / 30 dias |
| Ouvidoria | 10 dias úteis, prorrogável uma vez |
| Horário | 5h seguidas incluindo 12h–15h · fila é municipal |
| IOF-câmbio | 3,5% disponibilidade/cartão/espécie · 1,10% investimento · 0,38% entradas |
| IR no exterior | 15% sobre a parcela anual líquida · regime de caixa · sem isenção de pequeno valor |
| CBE | BC · anual ≥ US$ 1 mi · trimestral ≥ US$ 100 mi |
| Câmbio | Ponto de vista do banco · pronta até D+2 · até R$ 10 mil qualquer meio |
| Correspondente | US$ 3.000 · US$ 1.000 em espécie dos dois lados |
| Recompra | Sem obrigação · nova taxa |

---

## Nota de verificação

- **Contas conferidas por script e pela sequência da HP12C:**
  - FGC: 50.000 descobertos; 125.000 por titular;
  - compulsório: 315 e 204,75 (R$ milhões);
  - boleto vencido: 20,00 + 3,33 → 1.023,33;
  - pacote: 41,00 contra 39,90;
  - VET: 5.400 + 189 + 20 = 5.609 → 5,609;
  - IOF: 1.750, 550 e 94,50;
  - IR no exterior: 1.500;
  - recompra: 1.682,70 − 1.560,00 = 122,70.
- **Itens que conferem com o meu conhecimento das normas e não foram reabertos nesta sessão:**
  - FGC (R$ 250 mil e R$ 1 milhão em 4 anos);
  - Pix: limite noturno, dispositivo novo, MED de 80 dias, bloqueio de 72h, 5/20 chaves, 8 Pix Saque/Troco;
  - Res. CMN 3.919 (cesta essencial) e prazos de aviso de 45/30 dias;
  - ouvidoria (Res. CMN 4.860);
  - horário (Res. CMN 4.880);
  - Tema 272 do STF e Tema 1.156 do STJ;
  - IOF-câmbio (3,5% / 1,10% / 0,38%);
  - Lei 14.754/2023 (15%);
  - CBE (US$ 1 mi e US$ 100 mi);
  - extinção do DOC e da EIRELI.
- **Mantidos como no texto enviado, sem reconferência:**
  - Res. BCB 284/2023 (portabilidade até 12h);
  - quadro do compulsório de 20/08/2026 (21%, R$ 500 mi, 65%, Selic + 4%);
  - Res. BCB 551/2026;
  - VR-Boleto de R$ 250 mil e vedação de espécie a partir de R$ 10 mil;
  - Res. BCB 561/2026;
  - Cosit 130/2026;
  - limites do correspondente cambial (US$ 3.000/1.000);
  - guarda de 10 anos no câmbio;
  - prazo de 120 dias do comprovante de doação de sangue.
- **Exemplos hipotéticos:** todos os exemplos numéricos (➕). Estão marcados na fala ou no bastidor.
