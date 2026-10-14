# Roteiro de fala — Aula CPA: Princípios do Crédito, Rating, Score e Comprovação de Renda (versão aprofundada)

**Base:**
- documento "14-10- GRAVARPrincípios de crédito" (Google Docs), guia 1 "Princípios de crédito, rating, score e comprovação";
- aula do repositório `aulas/cpa/aula-2.3.1-A-principios-credito-rating-score-renda/aula.md`.

O documento original não foi alterado. As guias 2 a 4 (Contas e FGC; Boleto e Pix; Tarifas) não fazem parte desta entrega.

CPA 2.3 · 2.3.1 · 2.3.1.1 · Módulo 2 · **50 min** (passou de 40 para 50 min por causa dos cálculos na HP12C) · Aula A de 4 do item 2.3

**Legenda:**
- **negrito** = marcador do conteúdo;
- "texto entre aspas" = fala;
- 🔇 = bastidor, sem fala;
- ✏️ = complemento da guia mantido;
- ➕ = acréscimo desta versão;
- 🔗 = ponte para o próximo tópico;
- ⌨️ = teclas da HP12C;
- 🖥️ = o que aparece no visor.

---

## Bastidor — antes de gravar

> 🔇 **A guia está incompleta.**
> - Ela começa na etapa 2 (metáfora) e termina no tópico 3.4.
> - Faltam a abertura, "Por que cai na prova", o case, a questão e a revisão final.
> - Faltam também a frase de fixação do 3.4 e qualquer cálculo na HP12C.
>
> As falas da guia foram mantidas e revisadas. O que faltava veio da aula do repositório ou é acréscimo (➕).
>
> A apostila **não traz** os itens 2.3 a 2.3.1.1. A fonte é o roteiro de origem mais as normas.

### 🔇 Correções e checagens da fonte

| # | Ponto | Situação | Base |
| --- | --- | --- | --- |
| 1 | Mínimo existencial de R$ 600 | Confere (art. 3º do Decreto 11.150/2022, com a redação do Decreto 11.567/2023). Vale para prevenção e tratamento do superendividamento; **não é limite de concessão**. É objeto de ADPFs no STF: status pode mudar | Decreto 11.150/2022 |
| 2 | Validade mínima da oferta de 2 dias | Confere (CDC, art. 54-B). A oferta também exige CET e taxa efetiva mensal | CDC |
| 3 | Score Serasa de 0 a 1.000 | Descrição do produto comercial; **não é norma** | Roteiro de origem |
| 4 | Questão do roteiro de origem com 5 alternativas | Substituída por questões inéditas com 4 alternativas | Prompt mestre |
| 5 | MP 1.393/2026 (art. 28-A da Lei 14.690/2023) | Só como nota de atualização, fora do PD; MP em tramitação | Lei 14.690 compilada |

### ➕ Kit HP12C (mostrar na tela uma vez)

| O que fazer | Teclas | Por quê |
| --- | --- | --- |
| Limpar tudo | ⌨️ `f` `REG` | Apaga cálculos anteriores |
| Duas casas decimais | ⌨️ `f` `2` | Reais e centavos |
| Parcela no fim do mês | ⌨️ `g` `END` | Padrão dos empréstimos: 1ª parcela 30 dias depois |
| Sinal | Quem recebe o dinheiro põe o valor positivo; a parcela que sai do bolso entra com ⌨️ `CHS` | Convenção de fluxo de caixa da HP |

- "Pegue a HP: f REG, f 2 e g END. Hoje o dinheiro do empréstimo entra no seu bolso, então é positivo. A parcela sai do bolso: negativa, com CHS."

---

## 1. ➕ Fala de abertura — 3 min

- **Duas pessoas, mesma renda**
  - "Duas pessoas ganham exatamente o mesmo salário. Uma recebe limite de 8 mil reais no cartão; a outra, 2 mil. Uma paga a fatura inteira todo mês; a outra paga só uma parte. Qual delas é o melhor risco de crédito?"

- **Nenhum sinal decide sozinho**
  - "Não dá para responder só com a renda. Nem só com o score. Nem só com uma garantia. O banco olha um conjunto de sinais: o produto, a finalidade, o custo, a capacidade de pagar e os dados da pessoa. E nenhum desses sinais decide sozinho."

- **A promessa da aula**
  - "Nesta aula você vai entender as regras que todo banco precisa seguir antes de emprestar, a diferença entre rating e score, o que a lei proíbe na oferta de crédito e como medir se uma parcela cabe no bolso. E vamos fazer as contas na HP12C: parcela, custo efetivo, quitação antecipada e portabilidade."

**🔗 Ponte:** "Para organizar tudo isso, vamos usar uma imagem: uma ponte."

---

## 2. Metáfora central — 3 min

### Metáfora: a ponte com pedágio e painel de segurança

- **Ponte: o crédito traz um recurso do futuro para o presente**
  - "Pense no crédito como uma ponte. Ela traz para hoje um dinheiro que você só teria no futuro. Você atravessa agora e paga a travessia depois, com a renda dos próximos meses. Repare: quem pega crédito está gastando hoje a renda de amanhã."

- **Pedágio: os custos da travessia**
  - "Toda ponte tem pedágio. No crédito, o pedágio são os juros, que são o preço do dinheiro no tempo; as tarifas, que o banco cobra pelos serviços; os tributos, como o IOF; e os seguros, quando o contrato exige."

- **Painel de segurança: os sinais da análise**
  - "E a ponte tem um painel de segurança, como o painel de um carro. Ele mostra a renda, as dívidas que a pessoa já tem, o histórico de pagamento e o score. Ele indica se a travessia é suportável ou se o carro vai ficar sem combustível no meio do caminho."

- **O painel não é o motorista**
  - "Mas o painel não dirige. Quem decide atravessar é o cliente; quem decide abrir a cancela é a instituição financeira. Guarde essa imagem, porque ela vai voltar em todos os tópicos."

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Ponte | Produto de crédito |
| Destino | Finalidade: livre (empréstimo), vinculada (financiamento) ou uso do bem (leasing) |
| Painel | Análise de risco: renda, dívidas, histórico, score, SCR, política interna |
| Combustível | Capacidade de pagamento |
| Barreira lateral | Garantia: reduz a perda, não evita a queda |
| Pedágio somado | CET: juros + tarifas + tributos + seguros |
| Quem abre a cancela | A instituição financeira |

- **Traduzindo**
  - "Traduzindo. A ponte é o produto de crédito. O destino é a finalidade: dinheiro livre, como no empréstimo pessoal; crédito vinculado a uma compra, como no financiamento; ou uso de um bem, como no leasing."
  - "O painel é a análise de risco. Ela junta a renda, as dívidas, o histórico, o score, o SCR e a política interna do banco. O SCR é o sistema do Banco Central que mostra quanto a pessoa deve no sistema financeiro. A política interna é o conjunto de regras que cada instituição define para conceder crédito."
  - "O combustível é a capacidade de pagamento: quanto sobra no mês, depois das contas, para pagar a parcela."
  - "A barreira lateral é a garantia: um bem ou um direito que o banco pode usar para se pagar se o cliente não pagar, como o imóvel no financiamento imobiliário. Ela diminui o estrago se o carro sair da pista, mas não impede o acidente."
  - "E o pedágio inteiro, somado, tem nome: CET, o Custo Efetivo Total. Ele junta todos os custos numa taxa só. É o CET que você compara entre bancos, e não só a taxa de juros. Daqui a pouco vamos calcular um na HP."

### Frase de fixação

> **O painel ajuda a decidir; quem decide é a instituição.**

- "Repita comigo: o painel ajuda a decidir; quem decide é a instituição."

**🔗 Ponte:** "Só que uma ponte não pode ser oferecida de qualquer jeito. Quem oferece a travessia tem deveres: avisar o preço do pedágio, não empurrar a ponte para quem não precisa, não esconder buraco no caminho. Esses deveres são os princípios para disponibilizar crédito. É por onde começamos."

---

## 3. Explicação dos tópicos — 32 min

### 3.1 Princípios para disponibilização de crédito — 15 min · CPA 2.3 e 2.3.1

#### O que é

- **Definição**
  - "Disponibilizar crédito é colocar o crédito à disposição do cliente. E isso não é só emprestar: é oferecer com responsabilidade, informar direito e avaliar antes de liberar."

- **Os cinco produtos do item 2.3**
  - "No programa da prova, esse item cobre cinco produtos: empréstimo, financiamento, leasing, cartão de crédito e cheque especial. Cada um tem aula própria. Hoje vemos as regras que valem para todos eles."

| Produto | Finalidade | Exemplo |
| --- | --- | --- |
| Empréstimo | Livre: o cliente usa como quiser | Crédito pessoal |
| Financiamento | Vinculada a um bem ou serviço | Veículo, imóvel |
| Leasing | Uso do bem, com opção de compra | Frota de veículos |
| Cartão de crédito | Meio de pagamento com crédito embutido | Compra parcelada, rotativo |
| Cheque especial | Limite emergencial na conta | Saldo negativo de curtíssimo prazo |

#### Como funciona — Res. CMN 4.949/2021 (relacionamento com clientes)

- **A primeira fonte**
  - "As regras vêm de duas fontes. A primeira é do Conselho Monetário Nacional e vale para todas as instituições financeiras: a Resolução 4.949, de 2021, que trata do relacionamento com clientes."

| Princípio ou dever | Conteúdo |
| --- | --- |
| Princípios gerais | Ética, responsabilidade, transparência e diligência, com **convergência de interesses** |
| Tratamento | Justo e equitativo, considerando perfis e **vulnerabilidades** |
| Adequação | Produtos adequados às **necessidades, interesses e objetivos** do cliente |
| Informação | Clara e precisa: **direitos, deveres, custos, penalidades e riscos** |

- **Princípios gerais**
  - "Ela exige quatro atitudes do banco: ética, responsabilidade, transparência e diligência. Transparência é mostrar tudo de forma clara. Diligência é o cuidado de um profissional atento. E a resolução pede convergência de interesses: o que é bom para o banco precisa ser bom para o cliente também. Não vale ganhar à custa do cliente."

- **Tratamento justo**
  - "O tratamento tem de ser justo e equitativo, ou seja, adequado a cada cliente, levando em conta o perfil e as vulnerabilidades. Cliente vulnerável é quem tem mais dificuldade de entender ou de se defender, como o idoso, a pessoa com pouca escolaridade ou quem está em crise financeira."

- **Adequação**
  - "Adequação quer dizer que o produto precisa servir para aquele cliente, e não só para a meta de vendas do banco. Oferecer cheque especial para quem precisa de dinheiro por dois anos é inadequado, porque é um crédito caro, pensado para o curtíssimo prazo."

- **Informação**
  - "E a informação tem de ser clara e precisa: direitos, deveres, custos, multas e riscos. Tudo antes da contratação, e não depois."
  - 🔇 Validado: arts. 2º, 3º e 4º, I e III, da Res. CMN 4.949.

#### Como funciona — CDC, alterado pela Lei 14.181/2021 (crédito responsável)

- **A segunda fonte**
  - "A segunda fonte protege o cliente como consumidor: o Código de Defesa do Consumidor. Em 2021, a Lei 14.181, conhecida como Lei do Superendividamento, acrescentou ao Código regras específicas para a oferta de crédito."

- **Superendividamento (art. 54-A, § 1º)**
  - "Superendividamento, pela lei, é quando uma pessoa física, agindo de boa-fé, não consegue pagar todas as suas dívidas de consumo sem comprometer o mínimo necessário para viver. Não é quem deve muito: é quem não consegue mais pagar e continuar vivendo com dignidade."

**Na oferta (art. 54-B), o banco precisa informar:**

| # | Informação | O que é |
| --- | --- | --- |
| 1 | **CET** | Custo efetivo total: juros + tarifas + tributos + seguros, numa taxa só |
| 2 | **Taxa efetiva mensal** | A taxa real por mês, já com os juros compostos |
| 3 | **Encargos de atraso** | Juros de mora e multa |
| 4 | **Valor das prestações** | Quanto se paga por mês |
| 5 | **Validade da oferta** | Mínimo de **2 dias** |
| 6 | **Identificação do fornecedor** | Nome e endereço de quem oferece |
| 7 | **Liquidação antecipada** | Direito de quitar antes sem ônus |

- "Na hora da oferta, o Código obriga o banco a informar sete coisas. O CET. A taxa efetiva mensal. Os encargos de atraso. O valor das parcelas. O prazo de validade da oferta, que tem de ser de pelo menos dois dias, para você pensar com calma e comparar. Quem está oferecendo, com nome e endereço. E o direito de quitar antes sem pagar a mais."

**Vedações (art. 54-C):**

| É proibido | Por quê |
| --- | --- |
| Dizer que o crédito sai **sem consulta** aos cadastros ou **sem análise** da situação financeira | Estimula quem já está apertado a se endividar mais |
| **Ocultar** ônus e riscos | Impede a decisão informada |
| **Assediar ou pressionar**, principalmente idosos, analfabetos, doentes e vulneráveis | Explora quem tem menos defesa |

- "E há proibições. É proibido anunciar que o crédito sai sem consulta ou sem análise, porque isso estimula quem já está apertado a se endividar mais. É proibido esconder custos e riscos. E é proibido assediar ou pressionar o cliente, principalmente o idoso, o analfabeto, o doente ou qualquer pessoa vulnerável. Aquele anúncio 'dinheiro na hora, sem consulta ao SPC' é exatamente o que a lei proíbe."

#### ➕ Exemplo prático 1 — taxa de juros × CET (hipotético)

Empréstimo de R$ 10.000, em 12 parcelas mensais, a 3% a.m. O banco desconta R$ 500 de custos (tarifa, IOF e seguro, valor hipotético) do valor liberado. O cliente recebe R$ 9.500.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` | 🖥️ 0,00 | Limpa |
| 2 | ⌨️ `10000` `PV` · `3` `i` · `12` `n` · `PMT` | 🖥️ −1.004,62 | Parcela mensal |
| 3 | ⌨️ `9500` `PV` · `i` | 🖥️ 3,87 | **CET mensal**: a taxa com os custos |
| 4 | ⌨️ `100` `÷` `1` `+` `12` `yˣ` `1` `-` `100` `×` | 🖥️ 57,72 | CET anual (%) |
| 5 | ⌨️ `1,03` `ENTER` `12` `yˣ` `1` `-` `100` `×` | 🖥️ 42,58 | Taxa de juros anual (%), sem os custos |

- "Vamos ver por que o CET importa. Empréstimo de 10 mil a 3% ao mês em 12 parcelas. Na HP: 10 mil em PV, 3 em i, 12 em n, PMT. Parcela de 1.004,62."
- "Mas o banco descontou 500 reais de tarifa, IOF e seguro, e o cliente recebeu só 9.500. A parcela continua a mesma. Troque o PV para 9.500 e peça i: 3,87% ao mês. Esse é o custo efetivo. Para anualizar: divide por 100, soma 1, eleva a 12, tira 1 e multiplica por 100. CET de 57,72% ao ano, contra 42,58% da taxa de juros sozinha. É por isso que a lei manda informar o CET: dois bancos com a mesma taxa de juros podem ter custos totais bem diferentes."
- 🔇 Os R$ 500 de custos são hipotéticos. O cálculo real do IOF é tema da aula 2.3.3-D.

#### Mínimo existencial

- **O que é e quanto vale**
  - "Mínimo existencial é a parte da renda que fica protegida para a pessoa sobreviver: comida, moradia, contas básicas. Hoje, esse valor é de 600 reais por mês. Ele vem de um decreto de 2023, que alterou o decreto original, de 2022, em que o valor era de 25% do salário mínimo."

- **Para que serve, e para que não serve**
  - "Ele é usado para prevenir e tratar o superendividamento, por exemplo numa renegociação: o plano de pagamento não pode deixar a pessoa com menos do que isso. Atenção: isso não é limite para conceder crédito. O banco não está proibido de emprestar para quem ganha mil reais."

- **Status**
  - "Esse valor está sendo questionado no Supremo Tribunal Federal por meio de ADPFs, que são ações para proteger direitos fundamentais da Constituição. Então pode mudar: confira sempre o valor vigente antes da prova."

#### ➕ Exemplo prático 2 — o mínimo existencial foi preservado? (hipotético)

Renda mensal de R$ 1.500; parcelas de dívidas de consumo no mês: R$ 1.100.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `1500` `ENTER` `1100` `-` | 🖥️ 400,00 | O que sobra depois das parcelas |
| 2 | ⌨️ `600` `-` | 🖥️ −200,00 | Faltam R$ 200 para o mínimo existencial |

- "Uma pessoa ganha 1.500 e paga 1.100 de parcelas de dívidas de consumo no mês. Sobram 400. Menos os 600 do mínimo existencial: faltam 200. O mínimo não está preservado. É um sinal de superendividamento, e num processo de repactuação o plano teria de devolver a ela pelo menos esses 600 por mês."
- 🔇 O decreto faz a conta em base mensal: renda total menos as parcelas das dívidas do mês. Algumas dívidas ficam fora da conta, como financiamento imobiliário e crédito com garantia real. A lista exata (art. 4º do Decreto 11.150) não foi reaberta nesta sessão e fica fora da fala.

#### Como funciona — garantia ≠ análise de risco ≠ capacidade

- **Três perguntas diferentes**
  - "O Código proíbe dar crédito sem análise. Mas analisar o quê? Aqui entram três conceitos que a prova adora misturar. Cada um responde a uma pergunta diferente."

| Elemento | Pergunta que responde | O que **não** faz |
| --- | --- | --- |
| Análise de risco | Qual a chance de pagar? | Não é uma nota única |
| Garantia | Se não pagar, o que o banco recupera? | Não prova renda, não elimina o risco, não obriga a aprovar |
| Capacidade de pagamento | Sobra dinheiro para a parcela, todo mês? | Não é sinônimo de renda bruta |

- "A análise de risco responde: qual a chance de essa pessoa pagar? Ela junta renda, dívidas, histórico, cadastros e a política do banco. É o painel inteiro, não um ponteiro só."
- "A garantia responde: se a pessoa não pagar, o que o banco recupera? Ela diminui a perda, mas não prova que a pessoa tem renda, não elimina o risco e não obriga o banco a aprovar. Um imóvel em garantia não paga a parcela todo mês."
- "E a capacidade de pagamento responde: depois de pagar tudo, sobra dinheiro para a parcela, todo mês? Não é o salário bruto. É o que sobra de verdade."

#### Como funciona — liquidação antecipada e portabilidade

- **Sair antes ou trocar de ponte**
  - "Até agora falamos da entrada na ponte. Mas e se, no meio do caminho, o cliente quiser sair antes ou trocar de ponte? A lei garante dois direitos."

- **Liquidação antecipada (CDC, art. 52, § 2º)**
  - "O primeiro é a liquidação antecipada: quitar a dívida antes do prazo, toda ou em parte. Os juros e os demais acréscimos caem na proporção do tempo antecipado. A lógica é simples: juro é o aluguel do dinheiro. Se você devolveu antes, não paga aluguel do tempo em que não usou."

#### ➕ Exemplo prático 3 — quitar antes: quanto se economiza?

Mesmo empréstimo do exemplo 1 (parcela de R$ 1.004,62, 3% a.m.). Depois de pagar 6 parcelas, o cliente quer quitar as 6 restantes.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` | 🖥️ 0,00 | Limpa |
| 2 | ⌨️ `1004,62` `CHS` `PMT` · `3` `i` · `6` `n` · `PV` | 🖥️ 5.442,22 | Saldo devedor: valor para quitar hoje |
| 3 | ⌨️ `1004,62` `ENTER` `6` `×` | 🖥️ 6.027,72 | Soma das 6 parcelas restantes |
| 4 | ⌨️ `5442,22` `-` | 🖥️ 585,50 | Juros que deixam de ser pagos |

- "Depois de 6 parcelas, o cliente quer quitar tudo. Na HP: a parcela de 1.004,62 negativa em PMT, 3 em i, 6 em n, PV: 5.442,22. É isso que ele paga hoje. Se continuasse, pagaria 6 vezes 1.004,62, ou seja, 6.027,72. A diferença, 585,50, são os juros do tempo que ele não vai mais usar. Esse é o direito da liquidação antecipada."
- 🔇 Trazer as parcelas a valor presente pela taxa do contrato é a prática para contratos prefixados (Res. CMN 3.516/2007). A resolução não foi reaberta nesta sessão.

- **Portabilidade**
  - "O segundo direito é a portabilidade: levar a dívida para outro banco que ofereça condição melhor. O banco novo quita a dívida no banco antigo, e você passa a pagar o novo. Isso não é renegociar com o banco atual, é trocar de credor. E, em regra, a dívida nova não pode passar do saldo devedor, que é o que falta pagar hoje, nem do prazo que ainda resta. Portabilidade serve para melhorar a dívida que já existe, não para pegar dinheiro novo."

#### ➕ Exemplo prático 4 — portabilidade para uma taxa menor

O saldo de R$ 5.442,22 vai para outro banco, a 2% a.m., pelos mesmos 6 meses que faltam.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` | 🖥️ 0,00 | Limpa |
| 2 | ⌨️ `5442,22` `PV` · `2` `i` · `6` `n` · `PMT` | 🖥️ −971,58 | Nova parcela |
| 3 | ⌨️ `1004,62` `ENTER` `971,58` `-` | 🖥️ 33,04 | Economia por mês |
| 4 | ⌨️ `6` `×` | 🖥️ 198,24 | Economia nos 6 meses |

- "Agora a portabilidade. O saldo de 5.442,22 vai para um banco que cobra 2% ao mês, pelo mesmo prazo. Na HP: 5.442,22 em PV, 2 em i, 6 em n, PMT: parcela nova de 971,58. São 33,04 a menos por mês, e cerca de 198 reais em seis meses. Repare: o saldo e o prazo são os mesmos. Mudou só a taxa. Se o banco novo oferecesse dinheiro extra ou mais prazo, já não seria portabilidade pura."
- 🔇 33,04 × 6 = 198,24 com a parcela arredondada. Sem arredondar, 198,26.

- **📌 Nota de atualização (fora do PD)**
  - "Uma atualização recente, fora do programa da prova. Em setembro de 2026, uma medida provisória criou o Desenrola 3.0, um programa do governo para renegociar dívidas de pessoas físicas, e mandou o Conselho Monetário reforçar as regras de crédito responsável. Medida provisória é uma norma editada pelo Presidente que já vale quando é publicada, mas que precisa ser aprovada pelo Congresso para continuar valendo. Por isso, ainda pode mudar."
  - 🔇 MP 1.393, de 25/09/2026: art. 28-A da Lei 14.690/2023, vigência até 30/06/2028. Mantido como na guia; não reconferido.

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A garantia comprova a capacidade de pagamento" | Errado | Garantia reduz a perda; capacidade é folga mensal |
| "Crédito responsável significa aprovação garantida" | Errado | Às vezes, o responsável é negar |
| "O mínimo existencial é o limite máximo de crédito" | Errado | Serve à prevenção e ao tratamento do superendividamento |
| "Portabilidade é renegociar com o banco atual" | Errado | É trocar de credor |
| "Basta informar a taxa de juros na oferta" | Errado | O CDC exige o CET e a taxa efetiva mensal, entre outros |
| "Na quitação antecipada, o cliente paga todos os juros do contrato" | Errado | Redução proporcional dos juros |

> **Crédito responsável: adequar, informar com clareza e nunca prometer aprovação.**

**🔗 Ponte:** "Voltemos ao painel de segurança. Ele tem vários ponteiros, e o primeiro que vamos estudar não mede pessoas: mede empresas e países que pegam dinheiro emprestado no mercado. É o rating."

---

### 3.2 Rating de crédito — 4 min · CPA 2.3.1.1

#### O que é

- **Definição**
  - "Rating é a nota que uma agência especializada dá a um emissor de dívida. Emissor é quem pega dinheiro emprestado no mercado vendendo títulos: um país, que emite títulos públicos, ou uma empresa, que emite debêntures, por exemplo. A nota é uma opinião sobre duas coisas: se o emissor consegue pagar e se está disposto a pagar, no prazo e por inteiro."

#### Como funciona

| Pergunta | Resposta |
| --- | --- |
| Quem é avaliado? | O **emissor** como um todo ou uma **emissão específica** |
| Quem avalia? | **Agência de classificação de risco** (S&P, Moody's, Fitch), registrada e supervisionada pela **CVM** |
| Para que serve? | Medir o **risco de crédito**: a chance de o emissor não pagar |
| Efeito | Nota melhor → risco percebido menor → em geral, **taxa menor** para captar |
| É score? | **Não**: rating é do atacado (emissores); score é do varejo (pessoas físicas) |

- **Emissor ou emissão**
  - "A nota pode ser do emissor como um todo ou de uma emissão específica, que é um lote de títulos com regras próprias. A mesma empresa pode ter emissões com notas diferentes, porque uma tem garantia e a outra não."

- ✏️ **Quem avalia**
  - "Quem dá a nota é a agência de classificação de risco. As mais conhecidas são S&P, Moody's e Fitch. No Brasil, elas precisam de registro na CVM e são supervisionadas por ela."

- **Para que serve**
  - "Serve para medir o risco de crédito, que é a chance de o emissor não pagar. Quanto melhor a nota, menor o risco percebido e, em geral, menor a taxa que o emissor precisa oferecer para captar."

- **➕ Grau de investimento × grau especulativo**
  - "No mercado, as notas se dividem em dois grandes grupos. O grau de investimento, que nas escalas de S&P e Fitch vai de AAA até BBB−, indica risco mais baixo. Abaixo disso é o grau especulativo, com risco maior. É por isso que se ouve no noticiário que um país 'perdeu o grau de investimento'."
  - 🔇 Convenção das agências, não norma. Na Moody's, o equivalente a BBB− é Baa3.

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Rating é a nota de crédito da pessoa física" | Errado | Isso é score; rating é de emissor de dívida |
| "Rating é garantia de pagamento" | Errado | É opinião sobre o risco |
| "Toda emissão de uma empresa tem o mesmo rating" | Errado | Emissões com garantias diferentes podem ter notas diferentes |

> **Rating é a nota do emissor de dívida.**

**🔗 Ponte:** "E quando quem pede crédito é você, pessoa física? Não existe agência de rating para cada cidadão. Existe outro ponteiro no painel: o score."

---

### 3.3 Score, cadastro positivo e dados do cliente — 7 min · CPA 2.3.1.1

#### O que é

- **Credit scoring**
  - "Credit scoring, ou pontuação de crédito, é um modelo estatístico. O modelo olha milhões de pessoas no passado, vê quem pagou e quem não pagou e descobre quais características aparecem em cada grupo. Depois, usa dados permitidos por lei sobre você para estimar, numa nota, a sua chance de pagar em dia."

- **Serasa Score**
  - "O Serasa Score, citado no programa da prova, vai de zero a mil. Quanto maior, maior a chance estimada de pagar em dia. Mas atenção: essa escala é um produto comercial de uma empresa. Não é regra do Conselho Monetário, nem do Banco Central, nem da ANBIMA. Cada birô tem a sua escala."

#### Como funciona — quem faz o quê

| Peça | Quem é | O que faz | Decide? |
| --- | --- | --- | --- |
| Rating | Agência de classificação | Opinião sobre emissor de dívida | Não |
| Score | Modelo estatístico (birô) | Nota de probabilidade de pagar em dia | Não: é insumo |
| Cadastro positivo | Banco de dados de adimplemento (Lei 12.414/2011) | Histórico de contas pagas em dia | Não |
| Cadastro negativo | Birôs (Serasa, SPC, Boa Vista) | Registro de dívidas em atraso ("nome sujo") | Não |
| SCR | Banco Central (público) | Dívidas no sistema financeiro, em dia e em atraso | Não |
| Decisão de crédito | **Instituição financeira** | Aprovar, negar, limitar, precificar | **Sim** |

- **Score**
  - "O score entra na análise como insumo, ou seja, como um dos ingredientes. Sozinho, não decide nada."

- **Cadastro positivo**
  - "O cadastro positivo é o histórico das contas que você pagou em dia, como luz, telefone, financiamento e cartão. Adimplemento é isso, pagar em dia. Ele foi criado pela Lei 12.414, de 2011, e, desde 2019, a inclusão é automática; quem não quiser pode pedir para sair. É ele que ajuda quem paga em dia a ter um score melhor."

- **Birôs e SCR**
  - "Birôs de crédito são empresas privadas que reúnem dados de crédito e vendem produtos com eles, como o score e a consulta de negativação. Serasa, SPC e Boa Vista são exemplos. Já o SCR é público, do Banco Central, e mostra quanto cada pessoa deve no sistema financeiro, inclusive as dívidas em dia."

- **Quem decide**
  - "E quem decide aprovar, negar, limitar o valor ou precificar, que é definir a taxa de juros conforme o risco, é a instituição. Sempre ela. O painel ajuda; quem decide é a instituição."

#### Como funciona — transparência e dados

- **Score é legal?**
  - "Se um modelo dá nota para as pessoas, surge uma pergunta justa: isso é legal? E o cliente tem direito de saber como foi avaliado?"

- ✏️ **STJ**
  - "O Superior Tribunal de Justiça, o STJ, que uniformiza a interpretação das leis federais, julgou um recurso especial sobre isso e depois consolidou o entendimento na Súmula 550. A conclusão: o score é uma prática legal. Mas o consumidor tem o direito de saber quais dados pessoais foram considerados e de onde vieram. A fórmula, o birô pode manter em segredo, porque é segredo do negócio."

- ✏️ **LGPD**
  - "A LGPD, Lei Geral de Proteção de Dados, reforça esses direitos. Você pode acessar e corrigir os seus dados. E, se uma decisão foi tomada só por um sistema automático, sem participação humana, como uma negativa de crédito, você pode pedir a revisão dessa decisão. Dois cuidados: a lei garante a revisão, mas não exige que ela seja feita por uma pessoa. E revisar não é o mesmo que aprovar."
  - 🔇 REsp 1.419.697/RS e Súmula 550 do STJ: citados pelo roteiro de origem, não reabertos nesta sessão.

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Score alto obriga a aprovar" | Errado | Score é insumo |
| "Score baixo impede legalmente a concessão" | Errado | Nenhuma lei veta |
| "Cadastro positivo é a lista de devedores" | Errado | Lista de atraso é o cadastro negativo |
| "SCR, Serasa Score e SPC são a mesma coisa" | Errado | Um sistema público e dois produtos privados |
| "O birô deve revelar a fórmula do score" | Errado | Revela dados e fontes; a fórmula é segredo de negócio |

> **➕ Score é insumo; a decisão é da instituição.**

**🔗 Ponte:** "O score é um sinal indireto: ele olha o passado e o comportamento de pessoas parecidas com você. O sinal mais direto do painel é outro: quanto você ganha e quanto sobra no fim do mês. É o combustível da nossa metáfora: comprovação de renda e capacidade de pagamento."

---

### 3.4 Comprovação de renda e capacidade de pagamento — 6 min · CPA 2.3.1.1

#### O que é

- **Comprovação de renda**
  - "Comprovar renda é mostrar, com documentos, quanto dinheiro entra. Os mais comuns são o holerite, que é o contracheque do assalariado, a declaração do Imposto de Renda e o extrato bancário, que mostra o dinheiro entrando de fato na conta."

- **Capacidade de pagamento**
  - "Capacidade é outra coisa: é o que sobra depois de pagar tudo, e se essa sobra se repete todo mês. Renda estável, como salário de servidor, pesa diferente de renda que varia muito, como a de um autônomo, com mês bom e mês ruim."

#### Como funciona

**Fórmula didática (não é percentual legal):**

**Folga = renda líquida validada − despesas essenciais − dívidas existentes − nova parcela**

- "Uma conta simples para a lousa, que não é regra legal, é só para entender. Pegue a renda líquida, que é o que cai na conta depois dos descontos de imposto e previdência. Tire as despesas essenciais, aquelas sem as quais não se vive: moradia, alimentação, transporte, saúde. Tire as dívidas que já existem. E tire a parcela nova. O que sobra é a folga."

#### ➕ Exemplo prático 5 — folga e comprometimento da renda

Renda líquida de R$ 5.000; despesas essenciais de R$ 2.800; dívidas atuais de R$ 1.200; nova parcela de R$ 700.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `5000` `ENTER` `2800` `-` `1200` `-` `700` `-` | 🖥️ 300,00 | Folga mensal |
| 2 | ⌨️ `1200` `ENTER` `700` `+` | 🖥️ 1.900,00 | Total de parcelas com o novo crédito |
| 3 | ⌨️ `5000` `x≷y` `%T` | 🖥️ 38,00 | % da renda comprometida com dívidas |

- "Na HP: 5 mil, ENTER, menos 2.800, menos 1.200, menos 700. Sobram 300 reais. A renda está comprovada, mas a folga é pequena. Qualquer imprevisto, uma conta de farmácia, um conserto, e a parcela atrasa."
- "E quanto da renda vai para dívidas? 1.200 mais 700 dá 1.900. Digito 5 mil, troco a ordem com x≷y e aperto %T, porcentagem do total: 38% da renda comprometida. Por isso renda comprovada não é o mesmo que capacidade."
- 🔇 A tecla `%T` calcula que percentual o número no visor (X) representa do número acima (Y). Depois de `x≷y`, Y = 5.000 e X = 1.900.

- ✏️ **Não existe regra única**
  - "Não existe na lei um documento único, uma renda mínima ou um percentual de comprometimento da renda que valha para todo produto. Existem limites específicos de alguns produtos. O principal é a margem consignável do crédito consignado, que é o percentual máximo do salário ou do benefício que pode ser descontado em folha. Mas ela vale para aquele produto, e não para todos. Os 38% do exemplo são só uma medida para a conversa, não um limite legal."

- **Documentos conforme o caso**
  - "Cada banco decide quais documentos aceita conforme o produto, o canal, o perfil do cliente e a sua política interna. Canal é o meio de contratação, como agência, aplicativo ou correspondente. Um financiamento imobiliário pede muito mais papel que um cartão com limite baixo."

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Renda comprovada garante capacidade de pagamento" | Errado | Capacidade é a folga depois de despesas e dívidas |
| "Existe um percentual legal máximo de comprometimento para todo crédito" | Errado | Só limites específicos, como a margem do consignado |
| "Há uma renda mínima legal para obter crédito" | Errado | Não existe |
| "O documento de renda é o mesmo para qualquer produto" | Errado | Depende do produto, do canal, do perfil e da política interna |

> **➕ Renda é o que entra; capacidade é o que sobra.**

**🔗 Ponte:** "Vamos fechar o painel. Os princípios dizem como a ponte deve ser oferecida. O rating mede o emissor de dívida. O score e os cadastros mostram o histórico da pessoa. A renda e a capacidade mostram se há combustível para a travessia. Agora vamos ver como tudo isso vira questão de prova."

---

## 4. ➕ Por que isso cai na prova? — 4 min

### Explicação estratégica

- **A palavra que define o objeto**
  - "A banca troca conceitos parecidos. A resposta quase sempre está na palavra que define o objeto. Emissor? Rating. Pessoa? Score. Histórico em dia? Cadastro positivo. Entrada? Renda. Folga? Capacidade. Perda se não pagar? Garantia."

### Pontos de atenção

1. **Rating** → emissor de dívida, agência registrada na CVM.
2. **Score** → modelo estatístico; é insumo, não decisão.
3. **Renda** → entrada; **capacidade** → folga.
4. **Garantia** → reduz a perda; não substitui a análise.
5. **CDC, na oferta:** CET, taxa efetiva mensal, encargos de atraso, prestações e validade mínima de 2 dias.
6. **Vedado:** prometer crédito sem consulta e sem avaliação; ocultar riscos; assediar.
7. **Mínimo existencial:** R$ 600, para tratar superendividamento; não é limite de concessão.
8. **Direitos:** liquidação antecipada com redução proporcional dos juros; portabilidade para outro credor.

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Rating | Score | Opinião sobre emissor × modelo de risco da pessoa |
| Renda comprovada | Capacidade | Entrada × folga |
| Garantia | Análise de risco | Perda potencial × probabilidade de pagar |
| Cadastro positivo | Cadastro negativo | Contas pagas em dia × dívidas em atraso |
| Cadastro positivo | SCR | Histórico de adimplemento (privado) × dívidas no sistema financeiro (BC) |
| Taxa de juros | CET | Só juros × juros + tarifas + tributos + seguros |
| Portabilidade | Renegociação | Novo credor × mesmo credor |

### Palavras-chave da prova

| Expressão no enunciado | Resposta |
| --- | --- |
| "Emissor de dívida", "agência" | Rating |
| "Modelo estatístico", "0 a 1.000" | Score |
| "Folga após as parcelas" | Capacidade de pagamento |
| "Custo total da operação" | CET |
| "Sem consulta ao SPC/Serasa" | Prática vedada (CDC, art. 54-C) |
| "Transferir a dívida para outra instituição" | Portabilidade |

### Pegadinhas (todas erradas)

- "Score alto obriga a instituição a conceder o crédito."
- "Quem tem renda comprovada tem capacidade de pagar a nova parcela."
- "Garantia dispensa a avaliação de risco."
- "O mínimo existencial de R$ 600 é o valor máximo de parcela permitido."
- "A oferta de crédito pode ter validade de apenas 24 horas."
- "Basta informar a taxa de juros mensal na oferta."
  - "Leia cada frase, diga 'errado' em voz alta e explique por quê."

> **Nenhum sinal decide sozinho.**

**🔗 Ponte:** "Vamos ver isso numa agência de verdade."

---

## 5. ➕ Case — 4 min

### Situação

- "Marina é autônoma. Apresenta extratos e declaração de renda de 5 mil reais por mês. O score dela é alto. Ela já paga 1.200 em parcelas e tem 2.800 de despesas essenciais. Quer um empréstimo com parcela de 700. O gerente promete: 'Com esse score, está aprovado, nem precisa olhar o resto.' O que está certo e o que está errado nessa história?"

### Conceitos aplicados

| Fato | Conceito | Item |
| --- | --- | --- |
| Extratos e declaração | **Comprovação de renda** (entradas) | 2.3.1.1 |
| Sobram R$ 300; 38% da renda em dívidas (exemplo 5) | **Capacidade de pagamento** limitada | 2.3.1.1 |
| Autônoma | Renda **variável**: pesa na estabilidade da folga | 2.3.1.1 |
| Score alto | **Insumo** estatístico favorável, não decisão | 2.3.1.1 |
| "Está aprovado, nem precisa olhar o resto" | **Prática vedada** (CDC, art. 54-C) e falha de **adequação** (Res. CMN 4.949) | 2.3.1 |

### Análise passo a passo

- **1. A renda está comprovada**
  - "Os extratos e a declaração mostram 5 mil de entrada. Isso está certo."
- **2. A capacidade é apertada**
  - "Fazendo a conta da HP, sobram 300 reais por mês e 38% da renda vai para dívidas. Como ela é autônoma, num mês ruim a folga some."
- **3. O score não decide**
  - "O score alto é um bom sinal, mas é só um ponteiro do painel."
- **4. A fala do gerente é o problema**
  - "Prometer aprovação sem olhar renda e dívidas viola o dever de análise do Código de Defesa do Consumidor e o dever de adequação da Resolução 4.949. O correto é analisar o conjunto e, talvez, oferecer uma parcela menor, um prazo maior ou simplesmente não oferecer."

> **Score alto abre a conversa; a análise fecha a decisão.**

**🔗 Ponte:** "Agora, as questões no estilo da prova."

---

## 6. ➕ Questões comentadas — 5 min

### Questão 1 — Médio

**CPA · 2.3.1.1 Rating, score e renda · Médio**

Uma instituição analisa o pedido de crédito de um cliente que comprovou renda mensal de R$ 6.000 e possui score elevado, mas já compromete boa parte da renda com outras parcelas. A respeito dessa análise, é correto afirmar que:

A) o score elevado obriga a instituição a aprovar o crédito, pois é o indicador oficial de risco.
B) a renda comprovada demonstra as entradas do cliente, mas a capacidade de pagamento depende da folga após despesas e obrigações existentes.
C) o rating do cliente, atribuído por uma agência, substitui a análise de renda e de dívidas.
D) a existência de garantia dispensa a instituição de avaliar a capacidade de pagamento.

**Gabarito: B**

- **B (correta):** renda mostra quanto entra; capacidade mede quanto sobra depois de despesas, dívidas e nova parcela.
- **A:** o score é insumo de modelo estatístico, não indicador oficial; a decisão é da instituição.
- **C:** rating avalia emissores de dívida e não substitui a análise do cliente.
- **D:** a garantia reduz a perda potencial, mas não elimina a análise de capacidade.
  - "Resposta B. Renda é entrada; capacidade é folga."

### ➕ Questão 2 — Difícil

**CPA · 2.3.1 Princípios para disponibilização de crédito · Difícil**

Um banco oferece empréstimo de R$ 10.000,00 em 12 parcelas mensais de R$ 1.004,62, à taxa de juros de 3% a.m. Do valor contratado, são descontados R$ 500,00 de tarifa, IOF e seguro, e o cliente recebe R$ 9.500,00. Considerando as regras do Código de Defesa do Consumidor sobre a oferta de crédito, é correto afirmar que:

A) basta ao banco informar a taxa de juros de 3% a.m., pois tarifas e tributos não integram o custo da operação.
B) o custo efetivo da operação é superior a 3% a.m., e o banco deve informar o CET, a taxa efetiva mensal, o valor das prestações e a validade mínima de 2 dias da oferta.
C) o CET é igual à taxa de juros sempre que as parcelas são fixas.
D) a oferta pode ter validade de 24 horas, desde que o CET seja informado.

**Gabarito: B**

| Passo | Teclas | Visor |
| --- | --- | --- |
| 1 | ⌨️ `f` `REG` · `9500` `PV` · `1004,62` `CHS` `PMT` · `12` `n` · `i` | 🖥️ 3,87 |

- **B (correta):** com o valor líquido de R$ 9.500, a taxa efetiva sobe para cerca de 3,87% a.m. O CDC (art. 54-B) exige o CET, a taxa efetiva mensal, as prestações e a validade mínima de 2 dias.
- **A:** o CET existe justamente para somar juros, tarifas, tributos e seguros.
- **C:** parcelas fixas não tornam o CET igual à taxa; os custos descontados elevam o custo efetivo.
- **D:** a validade mínima é de 2 dias.
  - "Resposta B. Na HP, com 9.500 no PV e a mesma parcela, a taxa vai a 3,87% ao mês."

### ➕ Questão 3 — Fácil

**CPA · 2.3.1.1 Rating de crédito · Fácil**

O rating de crédito é:

A) a pontuação de 0 a 1.000 atribuída por birôs às pessoas físicas.
B) a opinião de uma agência de classificação de risco sobre a capacidade e a disposição de um emissor de dívida de pagar suas obrigações.
C) o registro das dívidas das pessoas físicas no sistema do Banco Central.
D) a garantia de que o emissor pagará os títulos no vencimento.

**Gabarito: B**

- **B (correta):** rating é a opinião sobre o emissor de dívida ou sobre uma emissão.
- **A:** essa é a descrição do score.
- **C:** isso é o SCR.
- **D:** rating é opinião sobre risco, não garantia.
  - "Resposta B. Rating é a nota do emissor de dívida."

**🔗 Ponte:** "Para fechar, a revisão."

---

## 7. ➕ Revisão final — 3 min

### Resumo em cinco pontos

1. **Produtos do item 2.3:** empréstimo, financiamento, leasing, cartão e cheque especial. O crédito deve ser adequado, transparente e responsável (Res. CMN 4.949; CDC, arts. 54-B e 54-C).
2. **Na oferta:** CET, taxa efetiva mensal, encargos do atraso, prestações e validade mínima de 2 dias. É vedado prometer crédito sem consulta e sem avaliação.
3. **Rating** classifica o emissor de dívida. **Score** é modelo estatístico e insumo. **Cadastro positivo** é o histórico de adimplemento.
4. **Renda** comprova entradas; **capacidade** é a folga. Não há renda mínima nem percentual universal de comprometimento. O **mínimo existencial** (R$ 600) serve para tratar o superendividamento.
5. **Garantia** reduz a perda, mas não substitui a análise. A decisão é sempre da instituição. O cliente tem direito à **liquidação antecipada** com redução proporcional dos juros e à **portabilidade**.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Rating | Emissor de dívida · agência registrada na CVM |
| Score | Modelo estatístico · insumo · não decide |
| Cadastro positivo | Histórico de adimplemento (Lei 12.414) |
| Renda × capacidade | Entrada × folga |
| Garantia | Reduz perda; não substitui análise |
| Oferta (CDC 54-B) | CET + taxa efetiva mensal + prestações + validade de 2 dias |
| Vedações (CDC 54-C) | Sem consulta/análise · ocultar riscos · assédio |
| Mínimo existencial | R$ 600 (superendividamento); não é limite de crédito |
| Liquidação antecipada | Redução proporcional dos juros (CDC, art. 52, § 2º) |
| HP12C | Parcela: `PV` `i` `n` `PMT` · CET: trocar o `PV` pelo valor líquido e pedir `i` · % da renda: `%T` |

### Cadeia lógica

**Necessidade → produto adequado → análise (renda, capacidade, risco, dados) → informação de custo (CET) → decisão da instituição → direitos durante o contrato (quitação antecipada, portabilidade)**

### Diferenças que não podem ser confundidas

- **Rating ≠ score · renda ≠ capacidade · garantia ≠ análise de risco · taxa de juros ≠ CET · portabilidade ≠ renegociação · mínimo existencial ≠ limite de crédito.**

### Frase central da aula

> **Crédito não é só dinheiro disponível: é uma decisão sobre finalidade, capacidade, risco, custo e consequência. O painel ajuda; quem decide é a instituição.**

- "Voltando às duas pessoas do começo: a renda era igual, mas o histórico, as dívidas e a folga não. Por isso os limites eram diferentes. Nenhum sinal decide sozinho."

### Próximo passo de estudo

- "Refaça na HP os exemplos do CET, da quitação antecipada e da portabilidade. Na próxima aula: empréstimo, financiamento, leasing e SCR."

---

## Nota de verificação

- **Contas conferidas por script e pela sequência da HP12C:**
  - parcela de 1.004,62; CET de 3,87% a.m. (57,72% a.a.) contra juros de 42,58% a.a.;
  - quitação antecipada: saldo de 5.442,22 e economia de 585,50;
  - portabilidade: nova parcela de 971,58, economia de 33,04 por mês e 198,24 em 6 meses (198,26 sem arredondar a parcela);
  - folga de 300 e comprometimento de 38%;
  - mínimo existencial: faltam 200.
- **Normas:** vêm da aula do repositório, conferida em 01/10/2026: Res. CMN 4.949; CDC, arts. 52, 54-B e 54-C; Decreto 11.150. Não foram reabertas nesta sessão.
- **Não confirmados nesta sessão:**
  - Lei 12.414 e LGPD;
  - STJ (REsp 1.419.697/RS e Súmula 550);
  - Res. CMN 3.516/2007 (desconto pela taxa do contrato);
  - lista de dívidas excluídas do cálculo do mínimo existencial (art. 4º do Decreto 11.150);
  - MP 1.393/2026;
  - faixas de grau de investimento das agências (convenção de mercado).
- **Valores hipotéticos:** os R$ 500 de custos do exemplo do CET e os valores do exemplo do mínimo existencial.
- **Acréscimos (➕):**
  - abertura;
  - kit HP12C;
  - exemplos 1 a 5 com teclas;
  - tabela dos cinco produtos e tabela "quem faz o quê";
  - grau de investimento;
  - etapas 4 a 7 completas, com as questões 2 e 3.
