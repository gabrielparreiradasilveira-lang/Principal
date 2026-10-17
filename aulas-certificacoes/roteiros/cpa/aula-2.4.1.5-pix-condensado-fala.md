# Roteiro de fala condensado — Aula CPA: Pix (2.4.1.5)

**Base:**
- documento "j" (Google Docs, seções 3.9 a 3.9.4), reescrito de forma condensada; o original não foi alterado;
- roteiro do repositório `roteiros/cpa/aula-2.4-servicos-bancarios-contas-pix-cambio-fala.md` (bloco Pix);
- **Resolução BCB 19/2020** (tarifas do Pix, com a Res. BCB 136/2021), conferida em 17/10/2026.

CPA 2.4.1.5 · 2.4.1.5.1 · 2.4.1.5.2 · 2.4.1.5.3 · 2.4.1.5.4 · Módulo 2 · **18 min** (o original rendia cerca de 35)

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ✏️ = correção · 🔗 = ponte.

---

## Bastidor — antes de gravar

### 🔇 O que foi condensado

| Mantido (essencial para a prova) | Cortado ou encurtado |
| --- | --- |
| Pix = arranjo do BC; DICT acha, SPI liquida | Falas que repetiam a mesma ideia do bullet técnico |
| 5 formas de iniciar · 4 tipos de chave · 5/20 chaves | Descrição longa dos 6 objetivos (virou uma linha) |
| Irrevogável após liquidar | Narração passo a passo duplicada do fluxo |
| Noturno R$ 1.000 · dispositivo novo R$ 200/R$ 1.000 · bloqueio 72 h · MED 80 dias | Explicações de ERP, API e conciliação (viraram uma frase) |
| Tarifas: PF grátis + 3 exceções · 8 Pix Saque/Troco · PJ pode pagar | Listas de "prova pode confundir" repetidas entre tópicos (unificadas) |
| QR estático × dinâmico · Pix Cobrança · Copia e Cola · Pix × TED × DOC | Pontes longas entre tópicos |

### ✏️ Correções feitas no texto original

| # | O original diz | O correto | Base |
| --- | --- | --- | --- |
| 1 | Título "3.90" | **3.9** | — |
| 2 | Sociedades "SLU/antiga EIRELI" | A EIRELI **foi extinta** (transformada em SLU). Fica só "Ltda., S.A., SLU" | Lei 14.195/2021 |
| 3 | Recebimento comercial por PF caracterizado por "mais de 30 Pix por mês" | A Res. BCB 19 só diz "recebimento com **finalidade de compra**" e manda seguir as definições do **Regulamento do Pix**. O número "30" **não foi conferido**: saiu da fala | Res. BCB 19/2020, arts. 4º, I, a, e 7º-A |
| 4 | Gratuidade da PF "inclusive MEI e Empresário Individual" | Confere: a norma fala em "pessoa natural, **inclusive empresários individuais**" (o MEI é empresário individual) | Res. BCB 19/2020, art. 3º |

### 🔇 Notas de atualização (fora da fala)

- O limite para **dispositivo não cadastrado** (R$ 200 por transação e R$ 1.000 por dia) veio da **Res. BCB 403/2024**, prevista para 01/11/2024.
- O **Pix Automático** (pagamentos recorrentes com autorização prévia) foi marcado pela **Res. BCB 402/2024** para **16/06/2025**. Fonte secundária; não está no PD.

### 🔇 HP12C

- Este bloco **não tem cálculo**.

---

## 3.9 Pix: visão geral — 2 min · CPA 2.4.1.5

- **O que é**
  - "O Pix não é aplicativo nem moeda. É um **arranjo de pagamentos** criado e regulado pelo Banco Central: um conjunto de regras para o dinheiro passar de uma instituição para outra em segundos. Você usa o Pix dentro do app do seu banco."

- **As duas engrenagens**
  - "Por trás da tela há duas engrenagens do Banco Central. O **DICT** é a lista telefônica: descobre de quem é a chave e em que conta a pessoa recebe. O **SPI** é o trilho do dinheiro: tira da instituição de quem paga e põe na de quem recebe."

| Sigla | Nome | Função |
| --- | --- | --- |
| **DICT** | Diretório de Identificadores de Contas Transacionais | **Acha** a conta pela chave |
| **SPI** | Sistema de Pagamentos Instantâneos | **Liquida**: move o dinheiro entre as Contas PI das instituições no BC |

> **O DICT acha; o SPI paga.**

---

## 3.9.1 Definição e objetivos — 3 min · CPA 2.4.1.5.1

- **Definição**
  - "Pix tem dois sentidos: é o **arranjo**, o conjunto de regras, e é a própria **transação** instantânea. Instantâneo quer dizer que a ordem e o dinheiro chegam em segundos, **24 horas, 7 dias por semana**, inclusive feriados, respeitadas as travas antifraude."

- **Objetivos (uma linha)**
  - "O BC criou o Pix para melhorar a experiência de pagamento, aumentar a competição, baratear custos, incluir mais pessoas no sistema financeiro e reduzir o uso de dinheiro em espécie."

- **As 5 formas de iniciar um Pix**

| # | Forma |
| --- | --- |
| 1 | **Chave Pix** |
| 2 | **Dados da conta** digitados (sem chave) |
| 3 | **QR Code** (estático ou dinâmico) |
| 4 | **Pix Copia e Cola** |
| 5 | **Iniciador de pagamento** (Open Finance) |

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Pix, SPI, DICT e chave são a mesma coisa" | Errado | Arranjo × liquidação × diretório × apelido |
| "24/7 significa sem limite e sem bloqueio" | Errado | Há limites e antifraude |

> **Pix é regra do BC, não aplicativo.**

**🔗 Ponte:** "Agora, o que acontece nos três segundos de um Pix."

---

## 3.9.2 Funcionamento, chaves, custos, tarifas e liquidação — 6 min · CPA 2.4.1.5.2

### O caminho do Pix

| # | Etapa | Quem faz |
| --- | --- | --- |
| 1 | Informa a chave ou lê o QR Code | Pagador |
| 2 | Consulta o DICT e mostra o nome do recebedor | Instituição do pagador (PSP) |
| 3 | Confere e autentica (senha ou biometria) | Pagador |
| 4 | Checa saldo, limite e antifraude | PSP do pagador |
| 5 | Move o dinheiro entre as Contas PI | SPI (BC) |
| 6 | Credita o recebedor | PSP do recebedor |

- "Você informa a chave, o seu banco consulta o DICT e mostra o nome. Você confere e autentica. O banco checa saldo, limite e fraude. O SPI move o dinheiro e o banco de quem recebe credita. Liquidado no SPI, o Pix é **irrevogável**: não existe cancelar por arrependimento. O dinheiro só volta por devolução voluntária de quem recebeu ou pelo MED, em caso de fraude ou falha."

### Chaves

| Regra | Conteúdo |
| --- | --- |
| Tipos | CPF/CNPJ · celular · e-mail · **aleatória** |
| Natureza | Apelido da conta: **não guarda dinheiro** e **não é obrigatória** |
| Limite | **5 por conta PF** · **20 por conta PJ** |

### Limites e segurança

| Mecanismo | Regra |
| --- | --- |
| **Limite noturno** (PF → PF) | **R$ 1.000** entre **20h e 6h** (ou 22h–6h, se o banco oferecer). Aumento: 24 a 48 h; redução: imediata |
| **Dispositivo novo** (PF) | **R$ 200 por Pix** e **R$ 1.000 por dia** até o aparelho ser cadastrado |
| **Bloqueio cautelar** | Banco do recebedor segura o valor por até **72 h** se houver suspeita de fraude |
| **MED** (Mecanismo Especial de Devolução) | Pedido em até **80 dias**, para **fraude ou falha operacional**. **Não** é seguro e **não** cobre erro de digitação, arrependimento ou briga comercial |

- "Grave os quatro números: mil à noite, 200 e mil no celular novo, 72 horas de bloqueio, 80 dias de MED. E o MED só devolve se ainda houver saldo na conta do golpista."

### Tarifas (Res. BCB 19/2020)

| Cliente | Regra |
| --- | --- |
| **PF, inclusive empresário individual (MEI)** | **Grátis** para enviar (transferência ou compra) e receber transferência |
| Exceções da PF | 1) Pix feito **no guichê ou por telefone** com o app disponível · 2) **recebimento com finalidade de compra** (venda) · 3) **Pix Saque/Troco** além de **8 por mês** |
| **PJ** | Pode ser tarifada no **envio e no recebimento**, sem preço único nacional |

- "Para a pessoa física, Pix é grátis, com três exceções: pedir para o funcionário fazer quando o app funciona, receber como venda, e passar de 8 Pix Saque ou Troco no mês. Empresa pode pagar para enviar e para receber."
- 🔇 Franquia de 8 Pix Saque/Troco: vale por conta, não acumula para o mês seguinte (Res. BCB 19, art. 3º, § 2º).

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A chave Pix é a conta" | Errado | É apelido |
| "O SPI procura a chave" | Errado | O DICT procura; o SPI liquida |
| "O MED devolve Pix mandado para a chave errada" | Errado | Só fraude ou falha operacional |
| "O limite noturno de R$ 1.000 vale para empresas" | Errado | É regra PF → PF |

> **O DICT acha, o SPI liquida, e o MED tenta devolver, mas não garante.**

**🔗 Ponte:** "Para que o Pix serve no dia a dia?"

---

## 3.9.3 Aplicações: transferências e pagamentos — 4 min · CPA 2.4.1.5.3

- **Usos**
  - "Pix serve para transferir entre pessoas, pagar lojas, fornecedores, impostos, contas de consumo, boletos com QR Code Pix e até o FGTS, sempre que quem recebe aceitar. A finalidade importa: transferência e compra têm regras de tarifa diferentes para quem recebe."

| Modalidade | Como funciona |
| --- | --- |
| **QR Code estático** | Fixo e reutilizável (ex.: plaquinha da padaria) |
| **QR Code dinâmico** | Único por cobrança, valor travado, facilita a conciliação |
| **Pix Cobrança** | Imediato ou **com vencimento** (juros, multa e desconto), mas liquida como Pix |
| **Pix Copia e Cola** | O código do QR em texto, colado em vez de lido |

| | Pix | TED | DOC |
| --- | --- | --- | --- |
| Velocidade | Segundos | Mesmo dia | — |
| Disponibilidade | 24/7 | Dias úteis, horário bancário | **Extinto em 2024** |
| Usa chave/DICT | Sim | Não | — |

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Pix Cobrança com vencimento é um boleto" | Errado | Parece, mas liquida no SPI |
| "Pagar boleto lendo o QR Pix é compensação de boleto" | Errado | É um Pix |
| "Existe imposto sobre o Pix" | Errado | Pode haver **tarifa** do banco, não tributo |
| "Devolução voluntária é o MED" | Errado | O MED é mecanismo antifraude |

> **Pix Cobrança tem cara de boleto, mas é Pix.**

**🔗 Ponte:** "E na empresa?"

---

## 3.9.4 Pix na pessoa jurídica — 3 min · CPA 2.4.1.5.4

- **Ferramenta de caixa**
  - "Para a empresa, o Pix é ferramenta de caixa. Pela **API Pix**, o sistema da empresa fala direto com o banco: gera cobranças, confirma o pagamento na hora e faz a conciliação sozinho. A empresa recebe vendas, paga fornecedores e impostos e pode pagar salários, se o banco oferecer."

| Tema | Regra para PJ |
| --- | --- |
| Tarifa | **Pode** cobrar envio e recebimento; cada banco define o preço |
| MEI e empresário individual | Seguem a regra da **PF** (gratuidade, salvo recebimento de vendas) |
| Ltda., S.A., SLU | Regra de **PJ**: tarifa desde o primeiro Pix, se o banco cobrar |
| Limite noturno | **Não** há o teto de R$ 1.000: limites definidos com o banco |
| Chave | **Não** é obrigatório usar o CNPJ |

- "Empresa pode pagar tarifa no Pix, não tem o limite noturno da pessoa física e não precisa usar o CNPJ como chave. E receber por Pix não muda nada nas obrigações fiscais: a nota fiscal continua obrigatória."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Pix de empresa é sempre grátis" | Errado | Pode ser tarifado |
| "Receber por Pix dispensa nota fiscal" | Errado | O meio de pagamento não muda o dever fiscal |
| "Todo valor recebido por Pix é receita tributável" | Errado | Depende da natureza da operação |

> **Pix na empresa: pode ter tarifa, não tem o limite noturno da PF e não muda a obrigação fiscal.**

**🔗 Ponte:** "Falamos muito de tarifa. Vamos às regras gerais de tarifas bancárias (3.10)."

---

## Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Natureza | Arranjo do BC · DICT acha · SPI liquida |
| Iniciar | Chave · dados da conta · QR · Copia e Cola · iniciador |
| Chaves | 4 tipos · 5 (PF) / 20 (PJ) por conta · não obrigatória |
| Liquidado | Irrevogável |
| Segurança | Noturno R$ 1.000 · dispositivo novo R$ 200/R$ 1.000 · bloqueio 72 h · MED 80 dias |
| Tarifa PF | Grátis · exceções: guichê/telefone, recebimento de venda, Saque/Troco após 8 |
| Tarifa PJ | Envio e recebimento podem ser cobrados |
| Pix × TED × DOC | 24/7 · dias úteis · DOC extinto |

---

## Nota de verificação

- **Conferido na fonte oficial em 17/10/2026:** Res. BCB 19/2020 consolidada (arts. 3º, 4º e 7º-A).
- **Vindos do roteiro 2.4 do repositório, não reabertos:** limites e prazos de segurança (noturno, dispositivo novo, 72 h, MED 80 dias) e 5/20 chaves.
- **Conferido só em fonte secundária (fora da fala):** Res. BCB 402/2024 (Pix Automático, 16/06/2025) e Res. BCB 403/2024 (dispositivo novo).
- **Não confirmado (retirado):** critério de "mais de 30 Pix por mês" para recebimento comercial.
