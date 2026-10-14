# Roteiro de fala — Aula CPA: PGBL, VGBL, Tributação e Portabilidade (versão aprofundada)

Base:
- documento "Gravar - PGBL, VGBL, Tributação e Portabilidade" (Google Docs);
- aula do repositório `aulas/cpa/aula-2.2-A-pgbl-vgbl-tributacao-portabilidade/aula.md`;
- APOSTILA-CPA, p. 441–449.

O documento original não foi alterado.

CPA 2.2.1 · 2.2.2 · 2.2.3.3 · Módulo 2 · **50 min** (passou de 40 para 50 min por causa dos cálculos na HP12C) · Aula A de 2. A Aula B cobre fases, taxas e renda: 2.2.3.1, 2.2.3.2 e 2.2.3.4.

**Legenda:** **negrito** = marcador do conteúdo · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ➕ = acréscimo desta versão · 🔗 = ponte para o próximo tópico · ⌨️ = teclas da HP12C · 🖥️ = o que aparece no visor.

---

## Bastidor — antes de gravar

> 🔇 **Valores perdidos no Google Docs:** no documento, o trecho entre dois cifrões ("R$ … $") virou equação e aparece vazio. Exemplo: "R 3.300" em vez de "R$ 12.000 × 27,5% = R$ 3.300". Neste roteiro, todos os valores vêm da aula do repositório. Conferi cada conta de novo.

### 🔇 Correções da fonte (resumo para quem grava)

| # | O material diz | O correto | Base |
| --- | --- | --- | --- |
| 1 | PGBL e VGBL são "seguro de pessoas" (PDF A0143) | Só o VGBL é seguro de pessoas; o PGBL é plano de previdência | SUSEP |
| 2 | PGBL: "diferimento de até 12% sobre o imposto" (PDF A0143) | 12% da **renda bruta anual tributável** | SUSEP; Lei 9.532/1997, art. 11 |
| 3 | Regime escolhido "no início do plano" (Apostila p. 447) e mudável "na portabilidade" (Apostila p. 449) | Desde a Lei 14.803/2024, a escolha é feita no 1º resgate ou benefício; o regressivo é irretratável | Lei 14.803/2024 |
| 4 | Progressivo: "alíquota será SEMPRE de 15%" (PDF A0148) | Os 15% são retenção antecipada no resgate; o imposto final sai na declaração anual | Lei 11.053/2004, art. 3º |
| 5 | Tabela progressiva e redutor do slide (PDF A0148) | Tabela mensal 2026 + redutor da Lei 15.270/2025: R$ 978,62 − 0,133145 × rendimento, até R$ 7.350 | Lei 15.270/2025; RFB |
| 6 | Portabilidade "entre planos tradicionais e fundos de pensão" (Apostila p. 450) | Aberta ↔ fechada só nas condições da Res. Conjunta SUSEP-PREVIC 1/2022; PGBL ↔ VGBL é proibida | Res. Conj. SUSEP-PREVIC 1/2022 |
| 7 | "Alíquota máxima em caso de falecimento é 25%" (PDF A0148) | Vale só no regressivo, para benefício de risco (morte/invalidez) com até 6 anos de acumulação | RFB (confirmado só em fonte secundária) |

### ➕ Kit HP12C — preparar a calculadora (mostrar na tela uma vez)

| O que fazer | Teclas | Por quê |
| --- | --- | --- |
| Limpar tudo | ⌨️ `f` `REG` | Apaga registros financeiros e memórias de contas anteriores |
| Duas casas decimais | ⌨️ `f` `2` | Formato de reais e centavos |
| Pagamentos no fim do período | ⌨️ `g` `END` | Padrão para aportes no fim de cada ano (o visor **não** mostra "BEGIN") |
| Vírgula como separador decimal (se a sua mostra ponto) | Desligar, segurar ⌨️ `.` e apertar ⌨️ `ON` | Visor no padrão brasileiro: 3.300,00 |
| Sinal do fluxo | Dinheiro que **sai** do bolso entra com ⌨️ `CHS` | Na HP, aporte é negativo e resgate é positivo |

- "Antes dos cálculos, pegue a HP12C e prepare a máquina comigo. Primeiro, f e REG, para limpar tudo. Depois, f e 2, para ficar com duas casas decimais. E g e END, para os aportes caírem no fim de cada período. Uma regra de ouro: dinheiro que sai do seu bolso entra negativo, com a tecla CHS."

---

## 1. Fala de abertura — 3 min

- **Ana × Bia: mesmo salário, mesmo aporte, planos diferentes**
  - "Duas amigas, Ana e Bia, ganham exatamente o mesmo salário: 100 mil reais por ano. As duas decidem guardar 12 mil reais para a aposentadoria. A Ana escolhe um PGBL e a Bia um VGBL. Mesma seguradora, mesmo fundo, mesma rentabilidade."

- **A restituição maior**
  - "Em abril, quando sai a restituição do Imposto de Renda, a Ana recebe 3.300 reais a mais do que a Bia. Parece que a Ana ganhou, certo?"

- **O resgate, vinte anos depois**
  - "Vinte anos depois, as duas resgatam. Agora é a Ana quem paga mais imposto que a Bia. E aí, quem ganhou?"

- **A promessa da aula**
  - "No fim desta aula, você vai fazer essa conta na HP12C e descobrir que a resposta depende de uma decisão que quase ninguém comenta: o que a Ana fez com aqueles 3.300 reais. No caminho, você vai aprender as três perguntas que resolvem qualquer questão de previdência. Como a pessoa declara o Imposto de Renda? Quando vai usar o dinheiro? Qual regime de tributação escolheu? E ainda uma quarta: dá para trocar de plano sem pagar imposto? Dá, e isso se chama portabilidade."

**🔗 Ponte:** "Para não se perder nessas perguntas, vamos usar uma imagem: uma estrada com pedágio."

---

## 2. Metáfora central — 3 min

### Metáfora: a estrada com pedágio do Leão

- **A estrada e o pedágio**
  - "Pense na previdência como uma estrada longa. No caminho tem um pedágio, cobrado pelo Imposto de Renda, o famoso Leão."

- **PGBL: passe livre na entrada**
  - "Quem entra pelo PGBL ganha um passe livre na entrada. O que você aporta sai da base do Imposto de Renda hoje, até 12% da sua renda. Base de cálculo é o valor sobre o qual o imposto é calculado. Só que, na saída, o Leão cobra sobre o carro inteiro: o que você aportou mais o que rendeu."

- **VGBL: sem passe livre**
  - "Quem entra pelo VGBL não tem passe livre, porque o dinheiro já pagou imposto antes de entrar. Por isso, na saída, o Leão só cobra sobre o que o carro ganhou na viagem: os rendimentos."

- **As duas cabines da saída**
  - "Na saída existem duas cabines. A regressiva funciona como um estacionamento com desconto por tempo: quanto mais tempo o carro ficou na estrada, menor a tarifa, de 35% até 10%. E cada carro tem o seu próprio tíquete, porque cada aporte conta o seu próprio prazo. A progressiva cobra pelo peso da carga: quanto maior a sua renda, maior a alíquota, com acerto na declaração anual."

- **Mudar de pista**
  - "E se a estrada estiver ruim, dá para mudar de pista sem passar pela cancela. Isso é a portabilidade: você troca de plano ou de seguradora sem pagar pedágio e sem perder o tempo já rodado. A condição é continuar no mesmo tipo de pista: PGBL com PGBL, VGBL com VGBL."

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Passe livre na entrada | Dedução do PGBL, até 12% da renda bruta tributável |
| Pedágio sobre o carro inteiro | PGBL: IR sobre aportes + rendimentos |
| Pedágio só sobre o ganho da viagem | VGBL: IR só sobre rendimentos |
| Cabine com desconto por tempo | Regime regressivo (35% → 10%), definitivo |
| Um tíquete por carro | Prazo contado aporte a aporte (PEPS) |
| Cabine que cobra pelo peso | Regime progressivo (tabela do IRPF), compensável na declaração |
| Mudar de pista sem cancela | Portabilidade, sem IR |
| Só entre pistas do mesmo tipo | PGBL → PGBL; VGBL → VGBL |

### Frase de fixação

> **PGBL: passe livre na entrada, pedágio no carro inteiro. VGBL: sem passe livre, pedágio só no ganho. Regressivo: desconto por tempo. Progressivo: cobrança pelo peso.**

- "Repita comigo. PGBL: passe livre na entrada, pedágio no carro inteiro. VGBL: pedágio só no ganho."

**🔗 Ponte:** "Antes de entrar nos dois planos, um minuto para entender por que a previdência complementar existe."

---

## 3. Explicação dos tópicos — 32 min

### 3.1 Previdência complementar em 1 minuto — 2 min · contexto do CPA 2.2 · Apostila p. 441–442

| | INSS | Previdência complementar |
| --- | --- | --- |
| Regime financeiro | Repartição simples | Capitalização |
| Participação | Obrigatória para quem trabalha com carteira ou contribui | Voluntária |
| Onde fica o dinheiro | Caixa único do sistema | Reserva individual, aplicada em FIE |
| Quem fiscaliza | — | Aberta: SUSEP · Fechada: PREVIC |

- **INSS: repartição simples**
  - "A previdência complementar existe para complementar o INSS. O INSS funciona por repartição simples. Imagine uma panela coletiva: quem trabalha hoje coloca dinheiro e quem está aposentado tira. Com a população envelhecendo, tem cada vez menos gente colocando e mais gente tirando."

- **Previdência complementar: capitalização**
  - "A previdência complementar funciona por capitalização. Em vez da panela coletiva, cada um tem o seu cofrinho com nome e sobrenome. O que você junta, mais o que rende, é seu. Esse dinheiro é aplicado num FIE, Fundo de Investimento Especialmente Constituído, um fundo criado só para receber dinheiro de previdência."

- **Aberta × fechada**
  - "PGBL e VGBL são planos abertos, ou seja, qualquer pessoa pode contratar. Quem vende são as seguradoras e as entidades abertas, as EAPC, e quem fiscaliza é a SUSEP. Os fundos de pensão de empresas formam a previdência fechada, as EFPC, só para empregados ou associados, e são fiscalizados pela PREVIC."

> **INSS é a panela coletiva; previdência complementar é o cofrinho com o seu nome.**

**🔗 Ponte:** "Dentro da previdência aberta, os dois produtos que caem na prova são o PGBL e o VGBL. Vamos colocar os dois lado a lado."

---

### 3.2 PGBL × VGBL — 10 min · CPA 2.2.1.1 e 2.2.1.2 · Apostila p. 442–443

#### O que é

| | PGBL — Plano Gerador de Benefício Livre | VGBL — Vida Gerador de Benefício Livre |
| --- | --- | --- |
| Natureza jurídica | Plano de previdência complementar aberta | Seguro de pessoas com cobertura por sobrevivência |
| Benefício fiscal na entrada | Dedução das contribuições da base do IR, até 12% da renda bruta anual tributável | Nenhum |
| Base do IR na saída | Total resgatado ou recebido (aportes + rendimentos) | Só os rendimentos |
| Declaração ideal | Completa | Simplificada, isento, ou quem já usou os 12% |
| Come-cotas | Não tem | Não tem |
| Fiscalização | SUSEP | SUSEP |

- **Natureza jurídica**
  - "O PGBL é um plano de previdência. O VGBL, juridicamente, é um seguro de pessoas com cobertura por sobrevivência: ele paga se você estiver vivo na data combinada. Cuidado: só o VGBL é seguro. Material que chama os dois de seguro está errado."

- **Entrada e saída**
  - "A grande diferença é o imposto. No PGBL, o que você aporta pode ser deduzido da base do Imposto de Renda, até 12% da renda bruta anual tributável. Renda bruta tributável é tudo o que você ganhou no ano e que paga imposto na tabela, como salário, pró-labore e aluguel, antes dos descontos. Rendimentos isentos, como o rendimento da poupança, não entram nessa conta. Em troca, no resgate, o imposto incide sobre tudo. No VGBL não há dedução, e por isso, no resgate, o imposto incide só sobre o rendimento."

- **Come-cotas**
  - "Nenhum dos dois tem come-cotas, aquela antecipação de imposto que os fundos comuns cobram em maio e novembro. Na previdência, o imposto só aparece no resgate ou no recebimento do benefício. Isso deixa o dinheiro render juros sobre juros sem interrupção."

#### Como funciona a dedução do PGBL

| Condição ou regra | Conteúdo |
| --- | --- |
| Tipo de declaração | Só na declaração **completa** |
| Contribuição à previdência básica | Contribuir para o INSS ou para um regime próprio (servidor público) |
| Limite | 12% da renda bruta anual tributável, somadas todas as contribuições a previdência complementar dedutíveis (Lei 9.532/1997, art. 11) |
| Ano da dedução | Conta o ano em que o aporte foi feito: quem quer deduzir em 2026 precisa aportar até 31/12/2026 |

- **As condições**
  - "Para aproveitar a dedução, você precisa de duas coisas: fazer a declaração completa e contribuir para o INSS ou para o regime próprio, como o dos servidores públicos. Declaração completa é aquela em que você lista as despesas dedutíveis, como saúde, educação e dependentes. Na simplificada, você troca tudo isso por um desconto padrão e o PGBL não ajuda em nada."

- **O limite é um só**
  - "Detalhe que pega muita gente: o limite de 12% é um só para tudo. Se você também contribui para um fundo de pensão da empresa, os dois somados não passam de 12%."

- **Prazo do aporte**
  - "Outro detalhe prático: a dedução vale no ano em que o aporte foi feito. Quem quer abater na declaração do ano que vem precisa aportar até 31 de dezembro. É por isso que o mercado faz campanha de PGBL todo fim de ano."

- **Diferimento, não isenção**
  - "Por que o PGBL tributa o total na saída? Porque o dinheiro entrou sem pagar imposto. A dedução é um diferimento: o imposto não desaparece, ele é adiado. O ganho tem duas fontes. A primeira é pagar mais tarde, talvez com alíquota menor, por exemplo 27,5% hoje e 10% lá na frente. A segunda é fazer render o dinheiro que iria para o Leão. É como um empréstimo sem juros que a Receita te faz."

#### Utilização típica

| Perfil | Escolha |
| --- | --- |
| Declaração completa, contribui para o INSS, quer investir até 12% da renda | PGBL |
| Declaração simplificada ou isento | VGBL |
| Declaração completa e quer investir acima de 12% | PGBL até 12% + VGBL no excedente |
| Autônomo que não contribui para o INSS | VGBL (sem a condição, a dedução do PGBL não vale) |

- **A regra prática**
  - "Na prova, a escolha sai de uma pergunta: como o cliente declara o Imposto de Renda? Completa e contribui para o INSS: PGBL até 12%. Simplificada ou isento: VGBL. Completa e quer investir mais de 12%: PGBL até o limite e VGBL no que passar."

- **➕ Sucessão: ponto em comum**
  - "Uma característica que os dois compartilham: o participante indica beneficiários. Se ele falecer, o dinheiro vai para essas pessoas sem precisar esperar o inventário. Por isso PGBL e VGBL também são usados em planejamento sucessório."
  - 🔇 Fora da fala: a cobrança de ITCMD sobre PGBL/VGBL teve decisão do STF (Tema 1214, 2024) e mudanças na reforma tributária. Status não confirmado nesta sessão. Não entra na aula.

#### ➕ Exemplo prático 1 — quanto o PGBL economiza hoje

| Item | Valor |
| --- | --- |
| Renda bruta tributável | R$ 100.000/ano · declaração completa · alíquota marginal 27,5% |
| Limite do PGBL (12%) | R$ 12.000 |
| Nova base de cálculo | R$ 88.000 |
| Economia de IR **neste ano** | R$ 12.000 × 27,5% = **R$ 3.300** |
| Se aportasse R$ 20.000 | Só R$ 12.000 dedutíveis; os R$ 8.000 restantes não reduzem nada e ainda são tributados pelo total no resgate → vão para o VGBL |

**Na HP12C**

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `100000` `ENTER` `12` `%` | 🖥️ 12.000,00 | Limite do PGBL: 12% da renda |
| 2 | ⌨️ `-` | 🖥️ 88.000,00 | Nova base de cálculo do IR |
| 3 | ⌨️ `12000` `ENTER` `27,5` `%` | 🖥️ 3.300,00 | Economia de IR no ano |
| 4 | ⌨️ `20000` `ENTER` `12000` `-` | 🖥️ 8.000,00 | Excedente que deve ir para o VGBL |

- "Vamos à HP. Digite 100 mil, ENTER, 12 e a tecla de porcentagem: aparecem 12 mil, o limite do PGBL. Aperte menos e o visor mostra 88 mil, a nova base do imposto. Agora a economia: 12 mil, ENTER, 27,5, porcentagem. Três mil e trezentos. Esse é o dinheiro que a Ana recebe a mais na restituição."
- "Por que 27,5%? Porque é a alíquota marginal, a que incide sobre a última fatia da renda. Os 12 mil deduzidos saem justamente dessa última fatia, a mais tributada."
- "E se ela aportasse 20 mil? Vinte mil menos doze mil dá oito mil. Esses 8 mil não reduzem o imposto agora e ainda vão pagar imposto sobre o valor total no resgate. Lugar deles é no VGBL."

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Deduz até 12% do imposto devido" | Errado | 12% da renda bruta tributável |
| "PGBL é isento de IR" | Errado | É diferimento: paga no resgate, sobre o total |
| "Quem faz declaração simplificada deve preferir PGBL" | Errado | Não aproveita a dedução → VGBL |
| "VGBL tributa só o rendimento" | Certo | O aporte já foi tributado |
| "PGBL e VGBL são seguros de pessoas" | Errado | Só o VGBL |

> **PGBL: deduz 12% hoje e paga sobre tudo amanhã, para quem faz declaração completa. VGBL: nada hoje e paga só sobre o ganho, para o resto.**

**🔗 Ponte:** "O plano define sobre quanto o imposto incide: o total ou só o rendimento. Falta saber com qual alíquota. Quem decide isso é o regime de tributação."

---

### 3.3 Regimes de tributação: progressivo × regressivo — 13 min · CPA 2.2.2.1 e 2.2.2.2 · Apostila p. 447–448

#### O que é

- **Base × alíquota**
  - "São dois regimes de Imposto de Renda para resgates e benefícios da previdência, criados pela Lei 11.053, de 2004. Grave a divisão de trabalho: o plano define a base, total no PGBL e rendimento no VGBL; o regime define a alíquota. Imposto é sempre base vezes alíquota."

| | Plano: define a **base** | Regime: define a **alíquota** |
| --- | --- | --- |
| Pergunta | Sobre quanto incide? | Quanto por cento? |
| Opções | PGBL (total) · VGBL (rendimento) | Regressivo (pelo tempo) · Progressivo (pela renda) |

#### Quando escolher o regime

- **Lei 14.803/2024**
  - "Até 2023, o regime era escolhido na contratação do plano, quando a pessoa ainda não sabia quanto tempo ia ficar nem quanto ia ganhar no futuro. Desde a Lei 14.803, de 2024, a escolha é feita no primeiro resgate ou quando começa o benefício, ou seja, já sabendo o prazo e a renda. Um cuidado: o regressivo é irretratável. Escolheu, não volta mais. A apostila ainda diz que a escolha é feita no início do plano, e essa informação está desatualizada."

#### Regime regressivo — definitivo ou exclusivo na fonte

| Prazo de acumulação (de cada aporte) | Alíquota de IR |
| --- | --- |
| Até 2 anos | 35% |
| Acima de 2 até 4 anos | 30% |
| Acima de 4 até 6 anos | 25% |
| Acima de 6 até 8 anos | 20% |
| Acima de 8 até 10 anos | 15% |
| Acima de 10 anos | 10% |

- **A tabela de cor**
  - "Esta tabela você precisa saber de cor: 35, 30, 25, 20, 15 e 10. Cai 5 pontos a cada 2 anos. Um macete: com 10 anos, você chega a 10%."

- **Definitivo**
  - "No regressivo, o imposto é retido na fonte e é definitivo. Ele não entra no acerto da declaração: nem restitui, nem cobra mais."

- **Cada aporte, um tíquete (PEPS)**
  - "E cada aporte tem o seu próprio prazo. Na hora do resgate, vale a regra PEPS: primeiro que entra, primeiro que sai. A seguradora tira primeiro o dinheiro mais antigo, que paga a menor alíquota. Um aporte de 11 anos atrás paga 10%; um aporte do ano passado paga 35%."

- **Benefício de risco**
  - "Uma exceção: nos benefícios pagos por morte ou invalidez, com até 6 anos de acumulação, a alíquota é de 25%, e não 35% ou 30%."
  - 🔇 Regra confirmada só por fontes secundárias. Verificar a instrução normativa da RFB.

- **Para quem**
  - "O regressivo serve para quem vai deixar o dinheiro por muito tempo, de preferência mais de 10 anos, ou para quem terá renda alta na aposentadoria."

#### Regime progressivo — compensável

Tabela mensal do IRPF vigente em 2026:

| Base de cálculo mensal | Alíquota | Parcela a deduzir |
| --- | --- | --- |
| Até R$ 2.428,80 | Isento | — |
| De R$ 2.428,81 a R$ 2.826,65 | 7,5% | R$ 182,16 |
| De R$ 2.826,66 a R$ 3.751,05 | 15% | R$ 394,16 |
| De R$ 3.751,06 a R$ 4.664,68 | 22,5% | R$ 675,49 |
| Acima de R$ 4.664,68 | 27,5% | R$ 908,73 |

**Redução da Lei 15.270/2025 (desde 2026), para rendimentos tributáveis mensais:**
- até R$ 5.000: imposto zero;
- de R$ 5.000,01 a R$ 7.350: o imposto da tabela é reduzido em R$ 978,62 − (0,133145 × rendimento);
- acima de R$ 7.350: sem redução.

| Situação | Como o IR é retido | Quando fecha a conta |
| --- | --- | --- |
| **Resgate** | 15% na fonte, como antecipação | Na declaração anual, pela tabela progressiva |
| **Benefício (renda mensal)** | Tabela mensal acima (com a redução da Lei 15.270, se aplicável) | Também ajusta na declaração anual |

- **A tabela e a parcela a deduzir**
  - "O progressivo usa a mesma tabela do Imposto de Renda do salário. A alíquota vai de isento até 27,5%. A parcela a deduzir existe porque a alíquota cheia só vale para a parte da renda que está naquela faixa. Ela é um atalho para não precisar calcular faixa por faixa. Na prova, a tabela costuma vir no enunciado."

- **Resgate: 15% é adiantamento**
  - "Atenção ao resgate. A seguradora retém 15% na hora, mas isso é um adiantamento. Na declaração anual, o resgate se soma às outras rendas do ano e passa pela tabela. Se o imposto final for menor que os 15%, você recebe a diferença de volta; se for maior, paga o que falta. Por isso o regime se chama compensável."

- **Para quem**
  - "O progressivo serve para quem terá renda baixa na aposentadoria, para quem pode precisar resgatar cedo e para quem tem muitas deduções na declaração."

#### ➕ Exemplo prático 2 — regressivo: mesma alíquota, base diferente

Aporte de R$ 10.000 feito há 7 anos, hoje valendo R$ 16.000. Alíquota: 20% (acima de 6 até 8 anos).

| | VGBL | PGBL |
| --- | --- | --- |
| Base | Rendimento: R$ 6.000 | Total: R$ 16.000 |
| IR (20%) | **R$ 1.200** | **R$ 3.200** |
| Líquido | R$ 14.800 | R$ 12.800 |

**Na HP12C**

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `16000` `ENTER` `10000` `-` | 🖥️ 6.000,00 | Rendimento (base do VGBL) |
| 2 | ⌨️ `20` `%` | 🖥️ 1.200,00 | IR no VGBL |
| 3 | ⌨️ `16000` `ENTER` `20` `%` | 🖥️ 3.200,00 | IR no PGBL (base = total) |
| 4 | ⌨️ `-` | 🖥️ 12.800,00 | Líquido no PGBL |

- "Na HP: 16 mil, ENTER, 10 mil, menos. Seis mil é o rendimento. Vinte, porcentagem: 1.200 de imposto no VGBL. Agora o PGBL: 16 mil, ENTER, 20, porcentagem. 3.200, porque a base é o total. Aperte menos e você vê o líquido do PGBL: 12.800. Mesma alíquota, base diferente."
- "Mas lembre: quem tem PGBL deduziu os 10 mil lá atrás. A comparação justa inclui a economia de imposto na entrada. Vamos fazer essa conta completa no fim da aula, com a Ana e a Bia."

#### ➕ Exemplo prático 3 — regressivo com dois aportes (PEPS)

VGBL com dois aportes:
- Aporte 1: R$ 10.000 há 11 anos, hoje R$ 25.000. Alíquota 10%.
- Aporte 2: R$ 10.000 há 3 anos, hoje R$ 12.000. Alíquota 30%.

O cliente resgata tudo (R$ 37.000).

| Aporte | Rendimento | Alíquota | IR |
| --- | --- | --- | --- |
| 1 | R$ 15.000 | 10% | R$ 1.500 |
| 2 | R$ 2.000 | 30% | R$ 600 |
| **Total** | **R$ 17.000** | — | **R$ 2.100** |

**Na HP12C**

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `25000` `ENTER` `10000` `-` | 🖥️ 15.000,00 | Rendimento do aporte 1 |
| 2 | ⌨️ `10` `%` | 🖥️ 1.500,00 | IR do aporte 1 |
| 3 | ⌨️ `STO` `1` | 🖥️ 1.500,00 | Guarda na memória 1 |
| 4 | ⌨️ `12000` `ENTER` `10000` `-` | 🖥️ 2.000,00 | Rendimento do aporte 2 |
| 5 | ⌨️ `30` `%` | 🖥️ 600,00 | IR do aporte 2 |
| 6 | ⌨️ `RCL` `1` `+` | 🖥️ 2.100,00 | IR total do resgate |

- "Aqui está o tíquete por carro. O aporte antigo rendeu 15 mil e paga 10%: 1.500. Guardo na memória com STO 1. O aporte novo rendeu 2 mil e paga 30%: 600. RCL 1, mais: 2.100 de imposto. Repare que o aporte novo rendeu muito menos e mesmo assim pagou uma alíquota três vezes maior. Na prova, nunca use uma alíquota única para aportes de datas diferentes."

#### ➕ Exemplo prático 4 — progressivo: benefício mensal

**a) Benefício de R$ 8.000/mês (acima de R$ 7.350, sem redução):**
R$ 8.000 × 27,5% − R$ 908,73 = **R$ 1.291,27**

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `8000` `ENTER` `27,5` `%` | 🖥️ 2.200,00 | Alíquota cheia sobre o benefício |
| 2 | ⌨️ `908,73` `-` | 🖥️ 1.291,27 | IR retido no mês |

- "Benefício de 8 mil por mês no progressivo. Na HP: 8 mil, ENTER, 27,5, porcentagem, 2.200. Menos a parcela a deduzir, 908,73. Imposto do mês: 1.291,27. Como 8 mil passa de 7.350, a lei nova não dá desconto."

**b) Benefício de R$ 6.000/mês (faixa da redução da Lei 15.270):**

| Etapa | Conta | Resultado |
| --- | --- | --- |
| IR pela tabela | 6.000 × 27,5% − 908,73 | R$ 741,27 |
| Redução | 978,62 − 0,133145 × 6.000 | R$ 179,75 |
| IR retido | 741,27 − 179,75 | **R$ 561,52** |

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `6000` `ENTER` `27,5` `%` | 🖥️ 1.650,00 | Alíquota cheia |
| 2 | ⌨️ `908,73` `-` | 🖥️ 741,27 | IR pela tabela |
| 3 | ⌨️ `STO` `1` | 🖥️ 741,27 | Guarda na memória 1 |
| 4 | ⌨️ `0,133145` `ENTER` `6000` `×` | 🖥️ 798,87 | Parte variável do redutor |
| 5 | ⌨️ `978,62` `x≷y` `-` | 🖥️ 179,75 | Valor da redução |
| 6 | ⌨️ `RCL` `1` `x≷y` `-` | 🖥️ 561,52 | IR retido no mês |

- "Agora um benefício de 6 mil, que está dentro da faixa de redução. Primeiro o imposto pela tabela: 741,27, que guardo na memória. Depois a redução: 0,133145 vezes 6 mil dá 798,87. Digito 978,62, troco a ordem com x≷y e subtraio: 179,75 de desconto. RCL 1, troco de novo e subtraio: imposto de 561,52. A tecla x≷y troca os dois números de lugar para a subtração sair na ordem certa."
- 🔇 A aplicação da redução da Lei 15.270 especificamente aos benefícios de previdência não foi confirmada nesta sessão. Se for usar na aula, dizer "pela regra geral da tabela mensal".

#### ➕ Exemplo prático 5 — prazo curto: por que o regressivo pode ser pior

Dona Lúcia aplica R$ 50.000 num VGBL a 7% a.a. e resgata tudo em 3 anos.

| Item | Regressivo | Progressivo |
| --- | --- | --- |
| Saldo (50.000 × 1,07³) | R$ 61.252,15 | R$ 61.252,15 |
| Rendimento (base VGBL) | R$ 11.252,15 | R$ 11.252,15 |
| Retenção no resgate | 30% = **R$ 3.375,65** (definitivo) | 15% = **R$ 1.687,82** (antecipação) |
| Depois | Fim da história | Ajuste na declaração: se a renda anual dela for baixa, parte ou tudo pode voltar como restituição |

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` | 🖥️ 0,00 | Limpa |
| 2 | ⌨️ `50000` `CHS` `PV` | 🖥️ −50.000,00 | Aplicação (sai do bolso) |
| 3 | ⌨️ `7` `i` · `3` `n` · `FV` | 🖥️ 61.252,15 | Saldo em 3 anos |
| 4 | ⌨️ `50000` `-` | 🖥️ 11.252,15 | Rendimento |
| 5 | ⌨️ `30` `%` | 🖥️ 3.375,65 | IR no regressivo |
| 6 | ⌨️ `x≷y` `15` `%` | 🖥️ 1.687,82 | Retenção no progressivo |

- "Dona Lúcia aplica 50 mil e vai precisar do dinheiro em 3 anos. Na HP: 50 mil, CHS, PV, porque o dinheiro sai do bolso; 7 na taxa, i; 3 em n; FV. Saldo de 61.252,15. Menos 50 mil: 11.252,15 de rendimento. No regressivo, 3 anos caem na faixa de 30%: 3.375,65, e acabou. Aperto x≷y para trazer o rendimento de volta e calculo 15%: no progressivo, a retenção é de 1.687,82, e ainda pode voltar na declaração. Para prazo curto e renda baixa, o progressivo tende a ganhar."

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Regressivo permite ajuste na declaração" | Errado | É definitivo |
| "No regressivo, o prazo conta da adesão ao plano" | Errado | Conta por aporte (PEPS) |
| "No progressivo, os 15% do resgate são o imposto final" | Errado | São antecipação |
| "Previdência sofre come-cotas" | Errado | IR só no resgate ou no benefício |
| "O regime é escolhido na contratação" | Errado | No 1º resgate ou benefício (Lei 14.803/2024) |

> **O plano define a base (PGBL total, VGBL rendimento). O regime define a alíquota (regressivo pelo tempo, progressivo pela renda).**

**🔗 Ponte:** "Você já sabe escolher o plano e o regime. E se, no meio do caminho, o plano se mostrar ruim, com taxa alta ou fundo fraco? Resgatar custa imposto. A saída é a portabilidade."

---

### 3.4 Portabilidade: interna e externa — 7 min · CPA 2.2.3.3 · Apostila p. 449–450

#### O que é

- **Transferência sem resgate**
  - "Portabilidade é levar o dinheiro acumulado de um plano para outro sem resgatar. Como o dinheiro não passa pela sua conta, não há Imposto de Renda na transferência. É o carro mudando de pista sem passar pela cancela."

#### Tipos

| Tipo | O que é | Exemplo |
| --- | --- | --- |
| Interna | Para outro plano da mesma entidade (seguradora ou EAPC) | Trocar um plano com FIE de renda fixa por um de multimercado, na mesma seguradora |
| Externa | Para plano de outra entidade | Levar o PGBL do Banco A para uma seguradora independente |

- **Interna × externa**
  - "A portabilidade interna é dentro da mesma casa: por exemplo, trocar o fundo de renda fixa por um multimercado na mesma seguradora. A externa leva o dinheiro para outra casa, como sair do banco e ir para uma seguradora independente."
  - 🔇 A norma fala só em "portabilidade entre planos". "Interna" e "externa" são termos do mercado e do Programa Detalhado.

#### Regras

| Regra | Conteúdo |
| --- | --- |
| Mesma natureza | PGBL → PGBL e VGBL → VGBL. PGBL ↔ VGBL é proibido |
| Aberta ↔ fechada | Permitida nas condições da Resolução Conjunta SUSEP-PREVIC nº 1/2022 |
| Sem IR | O dinheiro vai direto de entidade para entidade; o participante não pode receber o recurso na mão |
| Prazo do regressivo preservado | As datas dos aportes acompanham os recursos |
| Carregamento | A receptora não pode cobrar carregamento sobre o valor portado; a cedente pode cobrar o carregamento de saída previsto no plano (Res. CNSP 463/2024, art. 57) |
| Carência | Mínimo de 60 dias para a portabilidade; intervalo mínimo de 60 dias entre portabilidades; recursos vindos de EFPC não têm carência |
| Resgate × portabilidade | O resgate também tem carência mínima de 60 dias; o prazo máximo segue o regulamento de cada plano |
| Regime tributário | A portabilidade **não** é o momento de escolher o regime; a escolha é feita no 1º resgate ou benefício (Lei 14.803/2024) |

- **Por que PGBL não vira VGBL**
  - "A primeira regra é a mais cobrada: só entre planos da mesma natureza. Por quê? Pense na base do imposto. No PGBL, o aporte nunca pagou imposto; no VGBL, o aporte já pagou. Se o PGBL virasse VGBL, o imposto sobre os aportes simplesmente sumiria. Por isso é proibido."

- **Aberta ↔ fechada**
  - "Entre previdência aberta e fundo de pensão a portabilidade é permitida, nas condições de uma resolução conjunta da SUSEP e da PREVIC, de 2022."

- **Sem IR, prazo preservado**
  - "O dinheiro vai direto de uma entidade para a outra. Se passasse pela sua conta, seria resgate, com imposto. E as datas dos aportes vão junto. Quem tinha um aporte de 9 anos continua com 9 anos no plano novo, a caminho dos 10%."

- **Carregamento**
  - "Carregamento é uma taxa comercial, cobrada na entrada ou na saída do plano. Na portabilidade, a seguradora que recebe o dinheiro não pode cobrar carregamento sobre ele. A que você está deixando pode cobrar o carregamento de saída, se ele estiver previsto no contrato. Leia o regulamento antes de pedir."

- **Carência**
  - "Carência é o prazo mínimo de espera: 60 dias para pedir a portabilidade e 60 dias entre uma portabilidade e outra. Dinheiro vindo de fundo de pensão, as EFPC, não tem carência. O resgate também tem carência mínima de 60 dias."

- **Regime não muda na portabilidade**
  - "Um erro da apostila: ela diz que dá para mudar o regime tributário na portabilidade. Desde 2024, quem ainda não escolheu o regime escolhe no primeiro resgate ou benefício. Portabilidade é trocar de pista, não de cabine de pedágio."

#### ➕ Exemplo prático 6 — portabilidade × resgate

Ana tem R$ 80.000 num PGBL, com R$ 50.000 de aportes antigos (todos com mais de 10 anos), e quer trocar de seguradora.

| Caminho | O que acontece | IR |
| --- | --- | --- |
| Resgatar e aplicar em outro PGBL | Paga imposto sobre o total (PGBL) e recomeça os prazos do zero | 10% × 80.000 = **R$ 8.000** |
| Portabilidade externa | Dinheiro vai direto, prazos preservados | **R$ 0** |

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `80000` `ENTER` `10` `%` | 🖥️ 8.000,00 | IR que o resgate custaria |
| 2 | ⌨️ `-` | 🖥️ 72.000,00 | O que sobraria para reaplicar |

- "Se a Ana resgatar 80 mil do PGBL, mesmo com a menor alíquota do regressivo ela paga 10% sobre tudo: 8 mil reais. Na HP: 80 mil, ENTER, 10, porcentagem, 8 mil; menos, 72 mil. Ela reaplicaria só 72 mil, e os prazos voltariam para zero, com o dinheiro novo pagando 35% se precisar sair cedo. Pela portabilidade, os 80 mil chegam inteiros e mantêm os prazos. Quem resgata para trocar de plano joga dinheiro fora."

#### O que a prova pode confundir

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Portabilidade gera IR" | Errado | Não há resgate |
| "É possível portar PGBL para VGBL" | Errado | Só entre planos da mesma natureza |
| "Na portabilidade, os prazos do regressivo recomeçam" | Errado | As datas dos aportes acompanham o recurso |
| "A receptora pode cobrar carregamento sobre o valor portado" | Errado | Vedado |
| "Portabilidade interna = mesma entidade" | Certo | Externa = outra entidade |

> **Portabilidade: muda de pista sem passar pela cancela. Sem IR, sem perder o tempo rodado, só entre pistas do mesmo tipo.**

**🔗 Ponte:** "Fechamos o conteúdo. Agora vamos ver como a CPA cobra tudo isso, para você reconhecer a questão já no enunciado."

---

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

- **Três formatos de questão**
  - "A CPA cobra previdência de três jeitos. O primeiro é o caso de cliente: o enunciado descreve renda, declaração, prazo e objetivo, e pergunta qual plano ou regime indicar. O segundo é o cálculo: base vezes alíquota, ou o limite de 12%. O terceiro é a regra seca: portabilidade, carência, quando escolher o regime. A tabela regressiva você precisa saber de cor; a progressiva costuma vir no enunciado."

### Roteiro de resolução em 4 passos

| Passo | Pergunta | Leva a |
| --- | --- | --- |
| 1 | Como o cliente declara? Contribui para o INSS? | PGBL ou VGBL (base) |
| 2 | Quanto é 12% da renda bruta tributável? | Divisão PGBL + VGBL |
| 3 | Por quanto tempo fica? Renda futura alta ou baixa? | Regressivo ou progressivo (alíquota) |
| 4 | Quer trocar de plano? | Portabilidade, nunca resgate |

- "Siga sempre estes quatro passos, nesta ordem. Eles resolvem praticamente todas as questões de previdência."

### Pontos de atenção

1. **PGBL:** declaração completa + contribuição ao INSS ou regime próprio; deduz até 12% da renda bruta tributável.
2. **VGBL:** simplificada, isento ou excedente aos 12%.
3. **PGBL tributa o total; VGBL, só o rendimento.**
4. **Regressivo:** 35% → 10%, de 2 em 2 anos, definitivo, prazo por aporte (PEPS).
5. **Progressivo:** tabela do IRPF, 15% retidos no resgate como antecipação, ajuste na declaração.
6. **Escolha do regime:** no primeiro resgate ou benefício (Lei 14.803/2024); regressivo é irretratável.
7. **Portabilidade:** sem IR, mesma natureza, prazos preservados, carência mínima de 60 dias, sem carregamento na receptora.

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| PGBL | VGBL | Deduz na entrada e tributa o total × não deduz e tributa só o rendimento |
| Regressivo | Progressivo | Alíquota pelo tempo, definitivo × alíquota pela renda, compensável |
| Diferimento | Isenção | Imposto adiado × imposto que não existe |
| Portabilidade | Resgate | Sem IR × com IR |
| Interna | Externa | Mesma entidade × outra entidade |
| Base | Alíquota | Definida pelo plano × definida pelo regime |

### Palavras-chave da prova

| Expressão no enunciado | Resposta |
| --- | --- |
| "Declaração completa", "deduzir" | PGBL |
| "Declaração simplificada", "isento", "acima de 12%" | VGBL |
| "Longo prazo", "mais de 10 anos" | Regressivo |
| "Ajuste na declaração", "compensável" | Progressivo |
| "Sem incidência de IR na transferência" | Portabilidade |

### Pegadinhas (todas erradas)

- "O PGBL permite deduzir até 12% do imposto devido."
- "No VGBL, o IR incide sobre o valor total resgatado."
- "É possível fazer portabilidade de um PGBL para um VGBL, sem IR."
- "No regressivo, o prazo é contado a partir da data de adesão ao plano."
- "O regime progressivo retém 15% e esse é o imposto definitivo."
- "A opção pelo regime tributário deve ser feita na contratação do plano."
  - "Leia cada frase, diga 'errado' em voz alta e explique por quê. Se você consegue explicar as seis, está pronto."

> **Primeiro o plano (pela declaração), depois o regime (pelo prazo e pela renda futura). E troque de pista pela portabilidade, nunca pelo resgate.**

**🔗 Ponte:** "Agora vamos aplicar tudo numa família."

---

## 5. Case — 4 min

### Situação

- **Carlos**
  - "O Carlos tem 40 anos, é engenheiro, tem renda bruta tributável de 200 mil reais por ano, faz declaração completa e contribui para o INSS. Ele quer guardar 30 mil por ano para se aposentar aos 60."
- **Dona Lúcia**
  - "A mãe dele, Dona Lúcia, tem 68 anos, é aposentada e faz declaração simplificada. Ela quer aplicar 50 mil reais que vai usar daqui a 3 anos para reformar a casa."
- **O PGBL antigo**
  - "O Carlos também tem um PGBL antigo no banco, com taxa alta, e está pensando em 'resgatar e aplicar em outro lugar'. Antes de eu responder, pense: o que você indicaria para cada um?"

### Conceitos aplicados

| Situação | Decisão | Por quê |
| --- | --- | --- |
| Carlos, R$ 30 mil/ano | **R$ 24 mil no PGBL** (12% de R$ 200 mil) + **R$ 6 mil no VGBL** | Aproveita a dedução no limite; o excedente iria para a base total do PGBL sem ter sido deduzido |
| Economia anual de Carlos | R$ 24.000 × 27,5% = **R$ 6.600** | Alíquota marginal de 27,5% |
| Regime de Carlos | Tendência ao **regressivo** na hora do benefício (20 anos → 10%) | Horizonte longo; escolha no 1º resgate ou benefício |
| Dona Lúcia, R$ 50 mil por 3 anos | **VGBL**; regime **progressivo** tende a ser melhor | Declaração simplificada; prazo curto (no regressivo seriam 30%); renda de aposentada pode ficar em faixa baixa (exemplo prático 5) |
| PGBL antigo de Carlos | **Portabilidade externa** para outro PGBL, não resgate | Sem IR, prazos preservados, receptora sem carregamento (exemplo prático 6) |

### Cálculo do Carlos na HP12C

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `200000` `ENTER` `12` `%` | 🖥️ 24.000,00 | Teto do PGBL |
| 2 | ⌨️ `STO` `1` | 🖥️ 24.000,00 | Guarda o valor do PGBL |
| 3 | ⌨️ `30000` `ENTER` `RCL` `1` `-` | 🖥️ 6.000,00 | Parte que vai para o VGBL |
| 4 | ⌨️ `RCL` `1` `27,5` `%` | 🖥️ 6.600,00 | Economia de IR no ano |

- "Doze por cento de 200 mil dá 24 mil, o teto do PGBL. Guardo na memória. Trinta mil menos 24 mil: 6 mil vão para o VGBL. E a economia de imposto, 24 mil vezes 27,5%, dá 6.600 por ano. Se o Carlos reinvestir esse dinheiro, a vantagem cresce ano a ano."

### Análise passo a passo

- **1. Plano pela declaração**
  - "O Carlos faz declaração completa e contribui para o INSS, então usa o PGBL até 24 mil e o VGBL no resto. A Dona Lúcia faz a simplificada: VGBL."
- **2. Regime pelo prazo e pela renda**
  - "O Carlos tem 20 anos pela frente: tende ao regressivo, chegando a 10%. A Dona Lúcia tem 3 anos: no regressivo pagaria 30% e definitivo. Com renda de aposentada, o progressivo tende a ser melhor."
- **3. Trocar de plano pela portabilidade**
  - "O PGBL antigo vai para outro PGBL por portabilidade externa. Resgatar seria pagar imposto à toa e zerar os prazos."

### Síntese do case

- "Mesma família, planos e regimes diferentes. A escolha sai de três dados: tipo de declaração, prazo e renda esperada no resgate."

> **A declaração escolhe o plano; o prazo e a renda escolhem o regime; a portabilidade troca de plano sem pedágio.**

**🔗 Ponte:** "Agora, as questões no estilo da prova."

---

## 6. Questões comentadas — 5 min

### Questão 1 — Médio

**CPA · 2.2.1 Modalidades de planos (PGBL e VGBL) · Médio**

Um cliente com renda bruta anual tributável de R$ 150.000,00 faz declaração completa do Imposto de Renda, contribui regularmente para o INSS e deseja investir R$ 25.000,00 por ano em previdência complementar, buscando a maior eficiência tributária. A alocação mais adequada é:

A) R$ 25.000,00 em PGBL, pois todo o valor aportado poderá ser deduzido da base de cálculo do IR.
B) R$ 18.000,00 em PGBL e R$ 7.000,00 em VGBL.
C) R$ 25.000,00 em VGBL, pois o VGBL tributa apenas os rendimentos no resgate.
D) R$ 12.000,00 em PGBL e R$ 13.000,00 em VGBL, pois a dedução do PGBL está limitada a R$ 12.000,00 por ano.

**Gabarito: B**

| Passo | Teclas | Visor |
| --- | --- | --- |
| 1 | ⌨️ `150000` `ENTER` `12` `%` | 🖥️ 18.000,00 |
| 2 | ⌨️ `25000` `x≷y` `-` | 🖥️ 7.000,00 |

- **B (correta):** 12% × R$ 150.000 = R$ 18.000 dedutíveis no PGBL. O excedente de R$ 7.000 vai para o VGBL, tributado só sobre o rendimento.
- **A:** só R$ 18.000 são dedutíveis; os R$ 7.000 restantes seriam tributados sobre o total no resgate sem nenhum benefício na entrada.
- **C:** desperdiça a dedução de R$ 18.000 a que o cliente tem direito.
- **D:** confunde o limite: são 12% da renda, não R$ 12.000 fixos.
  - "Na HP: 150 mil, ENTER, 12, porcentagem: 18 mil. Digito 25 mil, troco a ordem com x≷y e subtraio: 7 mil. Resposta B. A D é a mais traiçoeira, porque usa o 12 como se fosse 12 mil reais."

### ➕ Questão 2 — Difícil

**CPA · 2.2.2.2 Regime regressivo · Difícil**

Um participante de VGBL, optante pelo regime regressivo, fez dois aportes: R$ 20.000,00 há 9 anos, que hoje valem R$ 34.000,00, e R$ 10.000,00 há 1 ano, que hoje valem R$ 10.800,00. Ele solicita o resgate de R$ 34.000,00. Considerando a forma de apuração do prazo no regime regressivo, o Imposto de Renda retido será de:

A) R$ 1.480,00.
B) R$ 2.100,00.
C) R$ 2.220,00.
D) R$ 5.100,00.

**Gabarito: B**

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `34000` `ENTER` `20000` `-` | 🖥️ 14.000,00 | Rendimento do aporte mais antigo (PEPS) |
| 2 | ⌨️ `15` `%` | 🖥️ 2.100,00 | IR: 9 anos → faixa de 15% |

- **B (correta):** pela regra PEPS, o resgate de R$ 34.000 consome o aporte mais antigo. Rendimento de R$ 14.000 (VGBL) × 15% (acima de 8 até 10 anos) = R$ 2.100.
- **A:** aplica 10% sobre todo o rendimento (R$ 14.800). Nove anos não chegam à faixa de 10%, e o aporte novo não foi resgatado.
- **C:** aplica 15% sobre o rendimento dos dois aportes (R$ 14.800), mas o resgate consumiu só o aporte antigo.
- **D:** usa a base de PGBL (R$ 34.000 × 15%); no VGBL, a base é só o rendimento.
  - "Três armadilhas numa questão só: a base, que no VGBL é o rendimento; a faixa, já que 9 anos dão 15% e não 10%; e a regra PEPS, pela qual sai primeiro o aporte mais antigo. Resposta B."

### ➕ Questão 3 — Fácil

**CPA · 2.2.3.3 Portabilidade · Fácil**

Sobre a portabilidade em planos de previdência complementar aberta, é correto afirmar que:

A) permite transferir recursos de um PGBL para um VGBL sem incidência de Imposto de Renda.
B) gera incidência de Imposto de Renda sobre os rendimentos no momento da transferência.
C) transfere os recursos entre planos da mesma natureza sem incidência de Imposto de Renda, preservando os prazos dos aportes.
D) exige que o participante resgate os recursos e os reaplique no novo plano em até 60 dias.

**Gabarito: C**

- **C (correta):** portabilidade é transferência direta entre planos da mesma natureza, sem IR, e as datas dos aportes acompanham os recursos.
- **A:** PGBL ↔ VGBL é proibido.
- **B:** não há IR, porque não há resgate.
- **D:** o recurso não passa pelas mãos do participante; os 60 dias são carência, não prazo de reaplicação.
  - "Resposta C. Se o dinheiro passa pela mão do cliente, deixou de ser portabilidade e virou resgate."

**🔗 Ponte:** "Para fechar, vamos voltar à pergunta do começo: Ana ou Bia?"

---

## 7. Revisão final — 4 min

### ➕ Fechamento da abertura: quem ganhou, Ana ou Bia? (com HP12C)

Simplificação didática: só o **primeiro aporte** de R$ 12.000, rendendo 8% a.a. por **20 anos**, no regime **regressivo** (mais de 10 anos → 10%). Ana recebeu R$ 3.300 de restituição.

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` | 🖥️ 0,00 | Limpa |
| 2 | ⌨️ `12000` `CHS` `PV` | 🖥️ −12.000,00 | Aporte |
| 3 | ⌨️ `8` `i` · `20` `n` · `FV` | 🖥️ 55.931,49 | Saldo das duas em 20 anos |
| 4 | ⌨️ `ENTER` `12000` `-` `10` `%` | 🖥️ 4.393,15 | IR da Bia (VGBL: 10% do rendimento) |
| 5 | ⌨️ `CHS` `RCL` `FV` `+` | 🖥️ 51.538,34 | **Líquido da Bia** |
| 6 | ⌨️ `RCL` `FV` `10` `%` | 🖥️ 5.593,15 | IR da Ana (PGBL: 10% do total) |
| 7 | ⌨️ `-` | 🖥️ 50.338,34 | **Líquido da Ana, se gastou a restituição** |
| 8 | ⌨️ `STO` `1` | 🖥️ 50.338,34 | Guarda |
| 9 | ⌨️ `3300` `CHS` `PV` `FV` | 🖥️ 15.381,16 | Restituição reinvestida (VGBL) em 20 anos |
| 10 | ⌨️ `ENTER` `3300` `-` `10` `%` | 🖥️ 1.208,12 | IR sobre o rendimento da restituição |
| 11 | ⌨️ `CHS` `RCL` `FV` `+` | 🖥️ 14.173,04 | Líquido da restituição |
| 12 | ⌨️ `RCL` `1` `+` | 🖥️ 64.511,38 | **Líquido da Ana, se reinvestiu a restituição** |

| Cenário | Líquido em 20 anos |
| --- | --- |
| Bia (VGBL) | R$ 51.538,34 |
| Ana (PGBL) **gastou** a restituição | R$ 50.338,34 → perde R$ 1.200 |
| Ana (PGBL) **reinvestiu** a restituição | R$ 64.511,38 → ganha R$ 12.973,04 |

- "Vamos resolver o mistério do começo. As duas aplicaram 12 mil por 20 anos a 8% ao ano: na HP, 12 mil, CHS, PV; 8, i; 20, n; FV. Cada uma tem 55.931,49."
- "A Bia, no VGBL, paga 10% só sobre o rendimento: 4.393,15 de imposto e 51.538,34 líquidos. A Ana, no PGBL, paga 10% sobre tudo: 5.593,15 de imposto e 50.338,34 líquidos. Se a Ana gastou a restituição, perdeu: ficou 1.200 reais atrás. E 1.200 é exatamente 10% dos 12 mil aportados, o imposto que ela adiou."
- "Agora, se a Ana reinvestiu os 3.300 da restituição: 3.300, CHS, PV, FV, e a HP mostra 15.381,16. Tirando o imposto, sobram 14.173,04. Somando, a Ana chega a 64.511,38, quase 13 mil a mais do que a Bia. O PGBL só vence quando a restituição é reinvestida. A vantagem vem de deduzir a 27,5% hoje e pagar 10% amanhã."
- 🔇 Simplificação assumida: um único aporte, sem taxas e com rentabilidade constante, com a restituição reinvestida num VGBL de mesma rentabilidade. Aportes mais recentes teriam alíquotas maiores no regressivo.

### Resumo em cinco pontos

1. **PGBL é plano de previdência:** deduz até 12% da renda bruta tributável (declaração completa + INSS ou regime próprio) e tributa o total na saída.
2. **VGBL é seguro de pessoas:** não deduz e tributa só o rendimento; serve para declaração simplificada, isentos ou excedente aos 12%.
3. **Regressivo:** 35% → 10% pelo prazo de cada aporte (PEPS), definitivo. **Progressivo:** tabela do IRPF, 15% retidos no resgate como antecipação, compensável.
4. **Escolha do regime:** no primeiro resgate ou benefício (Lei 14.803/2024); o regressivo é irretratável.
5. **Portabilidade** (interna ou externa): sem IR, só entre planos da mesma natureza, prazos preservados, carência mínima de 60 dias, sem carregamento na receptora.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| PGBL | Completa + INSS · deduz 12% da renda bruta · IR sobre o total |
| VGBL | Simplificada/isento/excedente · sem dedução · IR sobre o rendimento |
| Regressivo | 35 · 30 · 25 · 20 · 15 · 10 (a cada 2 anos) · definitivo · por aporte (PEPS) |
| Progressivo | Tabela IRPF · 15% na fonte no resgate · ajuste anual |
| Escolha do regime | No 1º resgate/benefício · regressivo irretratável |
| Portabilidade | Sem IR · PGBL→PGBL, VGBL→VGBL · prazos preservados · carência 60 dias · receptora sem carregamento |
| HP12C | `%` para alíquota · `CHS PV`, `i`, `n`, `FV` para saldo · `STO`/`RCL` para guardar |

### Cadeia lógica

**Tipo de declaração → PGBL ou VGBL (base) → prazo e renda futura → regressivo ou progressivo (alíquota) → portabilidade para trocar de plano sem IR**

- "Se a questão parecer confusa, siga essa corrente: declaração, plano, prazo e renda, regime. Para trocar de plano, portabilidade."

### Frase central da aula

> **Na estrada da previdência, o PGBL dá passe livre na entrada e cobra o carro inteiro na saída; o VGBL cobra só o que o carro ganhou. A cabine regressiva premia o tempo; a progressiva cobra pelo peso. A portabilidade troca de pista sem pedágio. E o passe livre só vale a pena se você reinvestir o que economizou.**

### Próximo passo de estudo

- "Decore a tabela regressiva, de 35 a 10, de 2 em 2 anos. Refaça na HP os exemplos 1, 3 e o da Ana e da Bia. Na próxima aula: fases do plano, taxas e transformação da reserva em renda."

---

## Nota de verificação

- **Valores recuperados:** no Google Docs, os trechos entre "R$" viraram equações vazias. Todos os valores vêm de `aulas/cpa/aula-2.2-A-pgbl-vgbl-tributacao-portabilidade/aula.md`.
- **Contas conferidas por script e pela sequência da HP12C:**
  - 3.300; 1.200 e 3.200; 2.100;
  - 1.291,27; 561,52 (redução de 179,75);
  - 61.252,15, com IR de 3.375,65 e retenção de 1.687,82;
  - 8.000 e 72.000; 24.000, 6.000 e 6.600; 18.000 e 7.000; 14.000 e 2.100;
  - 55.931,49, com líquidos de 51.538,34 e 50.338,34; 15.381,16 e 14.173,04; total de 64.511,38.
- **Acréscimos (➕):**
  - kit HP12C;
  - exemplos 1 a 6 com teclas;
  - limite conjunto de 12% (Lei 9.532/1997, art. 11) e dedução no ano do aporte;
  - beneficiários e sucessão;
  - roteiro de resolução em 4 passos;
  - questões 2 e 3;
  - fechamento Ana × Bia.
- **Pendências sem nova conferência nesta sessão:**
  - a alíquota de 25% em benefícios de risco, confirmada só por fonte secundária;
  - a aplicação da redução da Lei 15.270/2025 aos benefícios de previdência;
  - os prazos máximos de carência depois das Circulares SUSEP 698 e 699/2024;
  - o ITCMD sobre PGBL/VGBL (fora da fala).
- **Erros da apostila acrescentados nesta versão:**
  - p. 447: diz que o regime é escolhido "no início do plano";
  - p. 449: diz que o regime pode ser mudado na portabilidade.
