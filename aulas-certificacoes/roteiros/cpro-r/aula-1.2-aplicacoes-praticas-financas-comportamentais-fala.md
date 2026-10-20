# Roteiro de fala — Aula C-Pro R: Aplicações Práticas das Finanças Comportamentais

**Base:**
- **Programa Detalhado C-Pro R** (ANBIMA, v1.2, rev. 04/06/2025, vigência 01/01/2026), itens 1.2.1 a 1.2.5;
- APOSTILA-C-PRO-R (Top Invest, rev. mar/2026), p. 43–47;
- slides X8 **A5107** (Aplicações práticas das finanças comportamentais);
- **Caderno de Roteiros C-Pro R**, aula 002 (analogia da cozinha profissional e caso da Bianca);
- fontes conferidas em 20/10/2026: Resolução CVM 30/2021 (texto consolidado, arts. 2º, 6º e 7º), Lei 11.033/2004 (tabela regressiva do IR em renda fixa; MP 1.303/2025 caducou), Lei 9.250/1995, art. 23, e Lei 11.196/2005, art. 39 (isenções no ganho de capital de imóvel).

C-Pro R 1.2 · 1.2.1 · 1.2.2 · 1.2.3 · 1.2.4 · 1.2.5 · Módulo 1 · **45 min** · Aula única do item 1.2

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ✏️ = correção da fonte · ➕ = acréscimo desta versão · 🔗 = ponte · ⌨️ = teclas da HP12C · 🖥️ = visor.

---

## Bastidor — antes de gravar

### 🔇 Checagem de escopo (PD × materiais)

| Subitem do PD | Slides X8 | Apostila | Tratamento |
| --- | --- | --- | --- |
| 1.2 Aplicações práticas das finanças comportamentais | A5107, slide 1 | p. 43 | Conferido |
| 1.2.1 Estratégias de investimento baseadas em finanças comportamentais | A5107, slide 2 | p. 44 | Conferido |
| 1.2.2 Gestão de risco e finanças comportamentais | A5107, slide 3 | p. 44–45 | Conferido; definição de aversão à perda do slide corrigida (correção 3); conduta da CVM 30 acrescida |
| 1.2.3 Estratégias para mitigação das heurísticas e vieses | A5107, slide 4 | p. 45 | Conferido; "evite comparações" qualificado (correção 4); tabela viés → ferramenta acrescida |
| 1.2.4 Investimentos reais (imóveis, bens móveis, obras de arte, eletrônicos) × investimentos | A5107, slide 5 | p. 46 | Conferido; acrescidos os três atritos e a tributação do imóvel |
| 1.2.5 Financeiros (moedas, títulos de renda fixa, ativos da bolsa) | A5107, slide 6 | p. 46–47 | Conferido |

**Cobertura PD × material:** todos os subitens de 1.2.1 a 1.2.5 estão nos slides e na apostila. Os slides são curtos (6 telas); o conteúdo de aplicação vem da apostila e do caderno, aula 002.

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto | Base |
| --- | --- | --- | --- | --- |
| 1 | Apostila p. 43–47 | Todos os subitens numerados como "1.8" | Numeração do PD: 1.2.1 a 1.2.5. Na fala, usamos a do PD | PD C-Pro R |
| 2 | Apostila p. 46 | "Para o planejador financeiro…" | **Especialista de relacionamento** certificado. Ajustado na fala | PD C-Pro R |
| 3 | Slide A5107-3 | "Pessoas superestimam perdas e **subestimam ganhos** (aversão à perda)" | Aversão à perda é a **perda pesar mais** que um ganho de mesmo valor (cerca de 2,25 vezes na estimativa de Tversky e Kahneman). Não é "subestimar ganhos" | Tversky e Kahneman (1992); aula 1.1-A |
| 4 | Slide A5107-4 | "Evite comparações" | Evitar a comparação **com o vizinho, o amigo ou a rentabilidade passada de outro ativo**. A comparação com um **benchmark adequado ao objetivo** é necessária e faz parte do acompanhamento | Apostila p. 44 ("avaliação periódica e disciplinada") |
| 5 | Slide A5107-2 | Quem aplica todo mês "tende a obter resultados mais consistentes" | O ganho é de **processo**: menos decisões por impulso. Não é garantia de retorno maior. A fala diz "decisões mais consistentes" | Apostila p. 44 |
| 6 | Apostila p. 46 | Lista automóveis e eletrônicos como "investimentos reais" | A própria apostila ressalva: em geral, são **bens de consumo**, que se depreciam. A fala separa ativo de uso, bem de consumo e investimento real | Apostila p. 46 |

### 🔇 Nota de atualização (fora do PD)

- A **MP 1.303/2025**, que trocava a tabela regressiva do IR em renda fixa por alíquota única de 17,5%, **caducou** em outubro de 2025. Em 2026 vale a tabela da **Lei 11.033/2004**: 22,5% até 180 dias, 20% de 181 a 360, 17,5% de 361 a 720 e 15% acima de 720 dias. A tabela aparece só no exemplo da HP12C; a tributação é tema do Módulo 3.
- As isenções do ganho de capital do imóvel (R$ 440 mil, único imóvel; reaplicação em 180 dias) aparecem só como exemplo de custo de transação. **Não são cobradas no PD 1.2.**

### ➕ Kit HP12C

- 🔇 A HP aparece no fechamento do 1.2.3: o **custo de resgatar no susto e voltar depois** (caso da Bianca, do caderno, aula 002).
- Preparar com ⌨️ `f` `REG` e ⌨️ `f` `2`.

| Recurso | Teclas | Para que serve aqui |
| --- | --- | --- |
| Limpar | ⌨️ `f` `REG` | Zera registradores entre as pernas da conta |
| 2 casas | ⌨️ `f` `2` | Reais e centavos |
| Valor presente | ⌨️ valor `CHS` `PV` | Dinheiro que sai do bolso: negativo |
| Taxa e prazo | ⌨️ `i` `n` | Sempre na **mesma periodicidade** (ao mês com meses) |
| Valor futuro | ⌨️ `FV` | Montante bruto de cada perna |

### 🔇 Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Abertura | 3 min |
| 2. Metáfora | 3 min |
| 3. Tópicos (3.1 Estratégias 7 · 3.2 Gestão de risco 7 · 3.3 Mitigação de vieses 9 · 3.4 Reais × financeiros 7) | 30 min |
| 4. Por que cai | 2 min |
| 5. Case | 2 min |
| 6. Questões | 4 min |
| 7. Revisão | 1 min |
| **Total** | **45 min** |

---

## 1. Fala de abertura — 3 min

- **Nomeou. E agora?**
  - "Nas duas aulas passadas você aprendeu a dar nome. Ancoragem, disponibilidade, aversão à perda, manada, nudge. O cliente fala, e você sabe o nome técnico do que ele está fazendo."
  - "Hoje é a pergunta seguinte, e é ela que cai na prova: nomeou, e agora?"

- **O erro que parece acerto**
  - "O cliente diz: 'só vendo quando a ação voltar ao preço que eu paguei'. Você responde: 'isso é ancoragem'. Ele concorda com a cabeça e mantém exatamente a mesma decisão."
  - "Nomear o viés não desliga o viés. Informação sozinha não muda comportamento. Se mudasse, ninguém fumaria."

- **O que a prova quer**
  - "Repare na palavra do programa: aplicações práticas. A banca já saiu do 'o que é'. Ela quer saber o que você faz na mesa, com o cliente na frente: a estratégia, a gestão de risco, a ferramenta para cada viés e a diferença entre investimento real e financeiro."

- 🔇 Conexão com o PD: C-Pro R 1.2.1 a 1.2.5. Depois do 1.1 (aulas 1.1-A e 1.1-B). Antes do 1.3 (características da pessoa investidora no Brasil).

**🔗 Ponte:** "Para isso, vamos entrar numa cozinha."

---

## 2. Metáfora central — 3 min

### Metáfora: a cozinha profissional

- **O mise en place**
  - "O jantar começa às sete da noite. O cozinheiro que se dá bem não é o que corta cebola mais rápido. É o que, às cinco da tarde, já cortou tudo, pesou tudo e deixou cada pote no lugar. Isso tem nome: mise en place, tudo no lugar."
  - "Às sete, com trinta pedidos e o fogo aceso, ninguém decide. Só executa o que foi decidido às cinco."

- **O termômetro e o timer**
  - "O cozinheiro amador põe o dedo na panela para ver se está quente. O profissional usa termômetro e timer. Ele não sente menos: só não deixa a sensação decidir."

- **A receita na parede**
  - "O chef não confia na memória às sete da noite. A receita está escrita na parede e um ajudante repete o pedido em voz alta antes de sair."

- **A geladeira e o freezer**
  - "E a comida fica guardada em dois lugares. Na geladeira, você abre e usa na hora. No freezer, ela dura muito mais, mas precisa descongelar."

### Correspondência técnica

| Na cozinha | Na assessoria |
| --- | --- |
| Mise en place às cinco da tarde | **Estratégia comportamental**: decisão escrita, com número e data, tomada a frio (1.2.1) |
| Termômetro e timer | **Gestão de risco**: risco medido e acompanhamento com periodicidade definida (1.2.2) |
| Receita na parede e ajudante que confere | **Mitigação de vieses**: regra escrita e segunda checagem antes da ordem (1.2.3) |
| Freezer | **Investimento real**: guarda bem, demora para servir (1.2.4) |
| Geladeira | **Investimento financeiro**: abre e usa (1.2.5) |

### Frase de fixação

> **Quem faz o mise en place decide com a panela fria; quem não faz decide com a panela pegando fogo.**

- "E o seu papel: montar o mise en place com o cliente. Não é comer o prato por ele."

**🔗 Ponte:** "Começando pela primeira estação: o mise en place."

---

## 3. Explicação dos tópicos — 30 min

### 3.1 Estratégias de investimento baseadas em finanças comportamentais — 7 min · C-Pro R 1.2.1 · Apostila p. 43–44 · Slide A5107 (2)

- **Para que servem**
  - "A apostila diz: as finanças comportamentais não servem só para explicar. Elas transformam o que a psicologia descobriu em ações concretas. O objetivo é reduzir vieses, melhorar a disciplina, deixar o ambiente de decisão mais claro e proteger o investidor da impulsividade."

- **A regra de ouro**
  - "Estratégia comportamental é decisão escrita, com número e data. Sem número e sem data, é intenção. E intenção não sobrevive ao fogo aceso."

| Estratégia da apostila | Na prática | Viés que reduz |
| --- | --- | --- |
| **Simplificação das escolhas** | Menos opções, mais clareza | Sobrecarga, paralisia |
| **Metas específicas** | "R$ 300 mil em dezembro de 2034", e não "quero me aposentar bem" | Status quo, falta de foco |
| **Compartimentalização saudável** | Carteiras por objetivo: reserva, carro, aposentadoria | Contabilidade mental usada a favor |
| **Automatização** | Aporte automático em data fixa; rebalanceamento programado | Procrastinação, timing de mercado |
| **Regras pré-definidas de compra e venda** | Decididas na reunião calma | Aversão à perda, manada |
| **Avaliação periódica e disciplinada** | Revisão em data marcada, contra benchmark adequado | Excesso de confiança |

- **A virada de chave: a caixinha**
  - "Na aula 1.1-A, a contabilidade mental apareceu como viés: a pessoa trata o dinheiro de forma diferente conforme a origem. Agora repare: você não briga com a caixinha. Você usa a caixinha."
  - "Se ele separa o dinheiro na cabeça, dê nome e prazo a cada separação. 'Reserva: seis meses de despesa, liquidez diária.' 'Aposentadoria: vinte anos.' A separação sem objetivo é distorção. Com nome e prazo, vira organização."

- **Automatizar é cortar a cebola antes**
  - "Cada decisão que o cliente não precisa tomar é uma decisão que o viés não contamina. O aporte automático tira da mesa a pergunta 'será que aplico este mês?'. É a cebola já cortada."
  - ✏️ "O slide diz que quem aplica todo mês tem 'resultados mais consistentes'. O que fica mais consistente é a decisão. Retorno, ninguém garante."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Explicar o viés ao cliente é suficiente para corrigi-lo" | Errado | Nomear **não** muda a conduta; é preciso mudar o ambiente de decisão |
| "A compartimentalização por objetivo deve ser sempre combatida" | Errado | Com **nome e prazo**, ela vira organização |
| "Aporte automático garante retorno maior" | Errado | Reduz decisões impulsivas; **não** garante retorno |

> **Estratégia comportamental é decisão escrita, com número e data, tomada com a panela fria.**

**🔗 Ponte:** "Com o mise en place pronto, o fogo acende. Agora, a gestão de risco."

---

### 3.2 Gestão de risco e finanças comportamentais — 7 min · C-Pro R 1.2.2 · Apostila p. 44–45 · Slide A5107 (3)

- **Risco real × risco percebido**
  - "O slide resume numa frase: o risco não é só matemático, ele é percebido. O risco que a pessoa sente nem sempre corresponde ao risco real. Emoções e vieses distorcem essa percepção."

| Comportamento típico (apostila) | Distorção |
| --- | --- |
| Exagerar o risco depois de uma queda recente | Disponibilidade, aversão à perda |
| Ignorar riscos estruturais na euforia | Excesso de otimismo, manada |
| Concentrar demais a carteira | Excesso de confiança |
| Fugir completamente da volatilidade por medo | Aversão à perda |

  - ✏️ "Uma correção do slide: ele diz que aversão à perda é 'superestimar perdas e subestimar ganhos'. O correto é: a perda dói mais que um ganho do mesmo tamanho. Na estimativa clássica, cerca de 2,25 vezes. Ninguém está subestimando o ganho; a perda é que pesa mais."

- **Os instrumentos (o termômetro)**
  - "A apostila lista cinco: rebalanceamento regular, diversificação por classes de ativos, faixas-alvo para cada investimento, análise de correlação e comunicação clara sobre a volatilidade esperada. O slide acrescenta mais três: limites de perda definidos antes, simulação de cenários e educação emocional."

- **Traduzir percentual em reais**
  - "A comunicação clara da volatilidade é o instrumento mais forte na mesa. 'Perfil moderado, oscilação de até 12%' não diz nada a ninguém. 'Numa carteira de 250 mil, é ver 30 mil a menos no extrato de um mês para o outro' diz."
  - "Se a cara do cliente mudar, o risco que ele declarou está acima do que ele suporta. E isso é informação de suitability."

- **A reserva e o timer**
  - "A reserva de emergência também é ferramenta comportamental. Ela impede o resgate forçado no pior momento, porque o imprevisto costuma chegar junto com a crise."
  - "E a periodicidade de acompanhamento vai escrita no plano. Quem olha a carteira todo dia vê queda em quase metade dos dias. O ativo é o mesmo; o que muda é quantas vezes a pessoa se expõe ao susto. É o timer: você não abre o forno a cada trinta segundos."

- ➕ **Quando o cliente insiste fora do perfil**
  - "A gestão de risco tem um limite regulatório. A Resolução CVM 30, no artigo 2º, proíbe recomendar produto sem verificar a adequação ao perfil. E, no artigo 7º, quando o cliente ordena a operação com perfil inadequado, ausente ou desatualizado, você precisa, antes da primeira operação com aquela categoria de ativo, alertar o cliente indicando a causa da divergência e obter declaração expressa de que ele está ciente."
  - "Repare no que a norma não manda: ela não manda recusar a ordem, e não permite executar calado. É alerta com a causa, declaração e registro."

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Aversão à perda é subestimar ganhos" | Errado | É a **perda pesar mais** que o ganho equivalente |
| "Olhar a carteira todo dia reduz o risco" | Errado | A frequência muda a **percepção**, não o risco |
| "Cliente insiste em produto inadequado: o profissional deve recusar a ordem" | Errado | Deve **alertar com a causa** e obter **declaração expressa** (CVM 30, art. 7º) |

> **Gestão de risco comportamental é dimensionar antes o que vai doer, para que a dor não decida depois.**

**🔗 Ponte:** "Dimensionar ajuda. Mas cada viés tem a sua ferramenta própria. É a receita na parede."

---

### 3.3 Estratégias para mitigação das heurísticas e vieses comportamentais — 9 min · C-Pro R 1.2.3 · Apostila p. 45 · Slide A5107 (4)

- **Você não desliga o viés**
  - "O slide fecha com a frase certa: nenhum investidor é 100% racional, mas é possível criar mecanismos de proteção. Você não desliga o viés. Você desenha o ambiente para que ele custe menos."

- **Os quatro pilares da apostila**

| Pilar | O que fazer |
| --- | --- |
| **1. Criação de processos** | Checklist antes de decisões importantes; regras automáticas; separar análise de execução |
| **2. Informações diversificadas** | Consultar fontes diferentes; evitar bolhas informacionais; confrontar opiniões opostas |
| **3. Registro de decisões** | Anotar o motivo da escolha; acompanhar o resultado; identificar vieses recorrentes |
| **4. Educação financeira contínua** | Entender fundamentos, riscos, mercado e produtos |

- ✏️ "O slide diz 'evite comparações'. Atenção: a comparação que atrapalha é com o vizinho, com o amigo que ganhou na cripto, com a rentabilidade passada de outro ativo. A comparação com um benchmark adequado ao objetivo é obrigatória: é ela que diz se a estratégia está funcionando."

- ➕ **A receita na parede: cada viés com a sua ferramenta**
  - "Agora a tabela que a banca cobra em forma de caso. Coluna da esquerda, o viés. Coluna da direita, a ferramenta."

| Viés (aula 1.1-A) | Ferramenta | Como falar |
| --- | --- | --- |
| **Ancoragem** | Trocar a âncora | "O que essa posição faz pelo seu objetivo, no valor de hoje?" |
| **Disponibilidade** | Série longa no lugar da notícia | "Vamos ver dez anos, e não os três vídeos da semana" |
| **Excesso de confiança** | Registro datado de decisões | Data, o que esperava, o que fez; reler seis meses depois |
| **Autoatribuição** | O mesmo registro | Acertos e erros na mesma folha |
| **Confirmação** | Pedir o argumento contrário | "Me dê uma razão para essa decisão dar errado" |
| **Status quo** | Data marcada de revisão | O padrão passa a ser revisar, e não ficar parado |
| **Manada e FOMO** | Regra escrita antes da notícia | A regra na parede vale contra a manchete de hoje |
| **Framing** | Apresentar as duas leituras | "80% de chance de atingir é 20% de chance de não atingir" |
| **Aversão à perda** | Mostrar o custo em reais | É a conta da HP daqui a pouco |

- **O ajudante que confere**
  - "Repare que quase todas as ferramentas são uma segunda checagem: a folha, a pergunta contrária, a data marcada. Nenhuma depende de força de vontade."

- **Usar a heurística a favor**
  - "O slide também diz: use as heurísticas a seu favor. É o nudge da aula passada, do lado certo do balcão. Aporte automático já marcado, cancelável em uma tela. O cliente aceitaria se soubesse que existe: então é legítimo."

- **O limite**
  - "E o limite que a banca cobra: mitigar viés não é decidir pelo cliente. Você troca a âncora, mostra o dado, marca a data, pede o contra-argumento. Quem assina a ordem é ele. Se a ferramenta vira 'eu não deixo o cliente fazer', você saiu da mitigação e entrou na substituição da vontade dele."

- ➕ **Exemplo prático na HP12C: o custo de sair no susto**
  - "Bianca aplicou 120 mil reais num CDB de 36 meses que paga o equivalente a 1% ao mês. No oitavo mês, sai uma notícia ruim e ela resgata tudo. Fica dois meses com o dinheiro parado na conta e reaplica nas mesmas condições pelos 26 meses que faltam. Ela diz: 'não perdi nada, o dinheiro estava seguro'. Vamos à conta."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `120000` `CHS` `PV` `1` `i` `8` `n` `FV` | 🖥️ 129.942,80 | Montante bruto no mês 8 |
| 2 | ⌨️ `120000` `−` | 🖥️ 9.942,80 | Rendimento; 240 dias → IR de **20%** = 1.988,56 |
| 3 | ⌨️ `f` `REG` `127954,24` `CHS` `PV` `1` `i` `26` `n` `FV` | 🖥️ 165.733,54 | Reaplicação do líquido por 26 meses (780 dias → IR de 15% sobre 37.779,30 = 5.666,89) |
| 4 | — | 🖥️ 160.066,65 | **Líquido do caminho com o susto** |
| 5 | ⌨️ `f` `REG` `120000` `CHS` `PV` `1` `i` `36` `n` `FV` | 🖥️ 171.692,25 | Ficou os 36 meses (1.080 dias → IR de 15% sobre 51.692,25 = 7.753,84) |
| 6 | — | 🖥️ 163.938,42 | **Líquido de quem ficou** |

  - "Narrando o primeiro: f REG. Cento e vinte mil, CHS, PV. Um, i. Oito, n. FV: cento e vinte e nove mil, novecentos e quarenta e dois e oitenta. Menos cento e vinte mil: nove mil, novecentos e quarenta e dois e oitenta de rendimento. Com 240 dias, a alíquota é 20%."
  - "Resultado: com o susto, 160.066,65. Sem o susto, 163.938,42. Diferença de 3.871,77 reais: 3,2% do capital, numa decisão tomada com a panela pegando fogo."
  - "E de onde veio o prejuízo? Boa parte foi imposto antecipado na faixa mais alta. O resgate zerou a contagem do prazo, e a tabela regressiva recomeçou do zero."
  - 🔇 Regra da HP: `i` e `n` na mesma periodicidade e `PV` negativo. Taxa de 1% ao mês é hipótese didática; tabela regressiva da Lei 11.033/2004, art. 1º.
  - "E como dizer para a Bianca: 'Não estou dizendo que sair foi errado. Estou dizendo que custou 3.871 reais. Então, hoje, com a panela fria, vamos escrever o que a gente faz da próxima vez que a notícia aparecer.'"

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Viés de confirmação se mitiga reunindo mais materiais sobre a tese" | Errado | Mitiga-se buscando o **argumento contrário** |
| "Status quo se combate com data marcada de revisão" | Certo | O padrão passa a ser **revisar** |
| "Para proteger o cliente, o profissional pode impedir a ordem" | Errado | Mitigar **não** é decidir por ele |
| "Toda comparação deve ser evitada" | Errado | A comparação com **benchmark adequado** é necessária |

> **Você não desliga o viés; desenha o ambiente para que ele custe menos.**

**🔗 Ponte:** "Falta a última estação: onde a comida fica guardada. Geladeira ou freezer."

---

### 3.4 Investimentos reais × investimentos financeiros — 7 min · C-Pro R 1.2.4 e 1.2.5 · Apostila p. 46–47 · Slides A5107 (5 e 6)

- **As definições**
  - "Investimento real é o bem físico e tangível: imóvel, terreno, obra de arte, joia, bens móveis. Investimento financeiro é um direito sobre um fluxo de caixa: título de renda fixa, ação, cota de fundo, ETF, moeda, derivativo."
  - "A diferença de fundo: no financeiro existe intermediário e infraestrutura: registro, custódia, liquidação padronizada e preço todo dia. No real, é você e o bem."

- **O apego ao tangível (slide A5107-5)**
  - "O bem físico dá sensação de controle e de segurança. 'Quem compra terra não erra.' O slide chama isso de ilusão de segurança e de apego ao patrimônio físico: a dificuldade de vender."
  - "E o financeiro, diz o slide 6, desperta mais ansiedade, porque a volatilidade é visível: gráfico, notícia, cotação na tela."

- **As características do investimento real (apostila p. 46)**

| Característica | O que significa |
| --- | --- |
| **Menor liquidez** | Prazo de venda incerto, e ele piora quando muitos querem vender |
| **Maior custo de manutenção** | IPTU, condomínio, seguro, conservação |
| **Risco de obsolescência** | O bem envelhece ou sai de moda |
| **Dificuldade de precificação** | Só há preço quando alguém faz proposta |
| **Baixa diversificação** | Um imóvel concentra muito patrimônio em um só ativo |

  - "Some o custo de transação. No financeiro, são taxas e imposto em pontos percentuais pequenos. No imóvel, há ITBI na compra, que em São Paulo é de 3%, mais escritura, registro, corretagem e imposto sobre o ganho de capital na venda."

- **A frase da aula**
  - "O imóvel não oscila menos. Ele é observado menos."
  - "A falta de preço diário cria a sensação de estabilidade. É a comida no freezer: parece intacta porque você não abriu a porta. O cliente que diz 'imóvel nunca cai' está descrevendo a frequência com que olha o preço, e não o preço."
  - "Repare na simetria com o 3.2: lá, olhar demais aumenta a percepção de risco. Aqui, não olhar cria uma segurança que o ativo não tem."

- **Consumo não é investimento**
  - ✏️ "A apostila lista carro e eletrônicos entre os bens reais, mas faz a ressalva: muitos são consumidos. Carro e celular perdem valor com o uso. São bens de consumo, e não investimento. E a casa onde o cliente mora é ativo de uso: ela economiza aluguel, mas não paga a aposentadoria enquanto ele morar nela."

- **As vantagens do financeiro (apostila p. 46–47)**
  - "Maior liquidez, diversificação, acompanhamento, preço transparente e capacidade de gerar renda e valorização. Exemplos: títulos públicos, CDB, debêntures, ações, fundos, ETFs, moedas e derivativos. A combinação deles equilibra risco, retorno, horizonte, objetivos e necessidade de liquidez."

- **Nenhum é o certo**
  - "O freezer é bom. Investimento real combina com objetivo longo, valor alto e uso definido. O erro é o descasamento: guardar no freezer o que o jantar de hoje precisa. Objetivo de dezoito meses dentro de um imóvel que pode levar um ano para vender."

| | Real (freezer) | Financeiro (geladeira) |
| --- | --- | --- |
| Exemplo | Imóvel, terra, arte, joia | Título, ação, cota, ETF, moeda |
| Liquidez | Baixa, prazo incerto | Maior, prazo conhecido |
| Preço | Só na proposta | Diário, transparente |
| Custo de entrada e saída | Alto | Baixo |
| Diversificação | Difícil | Fácil |
| Sensação | Segurança (ilusão) | Ansiedade (volatilidade visível) |

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O imóvel tem risco baixo porque o valor não oscila" | Errado | Não há **marcação**; isso não é ausência de risco |
| "Carro e smartphone são investimentos reais típicos" | Errado | Em geral, são **bens de consumo**, que se depreciam |
| "A residência do cliente compõe o patrimônio para a aposentadoria" | Errado | É **ativo de uso** enquanto for moradia |
| "Investimentos financeiros têm, em geral, maior liquidez e preço transparente" | Certo | Apostila p. 46–47 |

> **O freezer guarda bem e demora para servir; o erro é guardar no freezer o jantar de hoje.**

**🔗 Ponte:** "Agora, como isso aparece na prova."

---

## 4. Por que isso cai na prova? — 2 min

- **Como a banca pergunta**
  - "A banca descreve um cliente com um comportamento e pergunta a conduta do profissional. Nas alternativas, quase sempre há uma que só explica o conceito ao cliente. Ela parece certa, mas demonstra explicar, e o comando pede aplicar."

### Pontos de atenção

1. Estratégia comportamental = decisão **escrita, com número e data**; automatizar, simplificar, compartimentalizar por objetivo.
2. Gestão de risco = risco **percebido** × real; traduzir percentual em **reais**; reserva e periodicidade de acompanhamento.
3. Cliente insiste fora do perfil: **alerta com a causa** + **declaração expressa** (CVM 30, art. 7º); não é recusa, nem execução calada.
4. Cada viés tem a sua ferramenta: confirmação → **contra-argumento**; status quo → **data de revisão**; ancoragem → **troca de âncora**.
5. Mitigar **não** é decidir pelo cliente.
6. Investimento real: **liquidez baixa, custo alto, sem marcação**. Estabilidade aparente ≠ risco baixo.

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Explicar o viés | Aplicar a ferramenta | Informação × mudança no ambiente de decisão |
| Risco declarado | Risco suportado | O que diz × o que aguenta na queda |
| Alerta + declaração | Recusa da ordem | O que a CVM 30 exige × o que ela não manda |
| Compartimentalização solta | Com nome e prazo | Distorção × organização |
| Investimento real | Financeiro | Tangível, ilíquido, sem preço diário × direito, líquido, preço diário |
| Ativo de uso | Ativo de investimento | Economiza despesa × gera fluxo para o objetivo |

### Pegadinhas (todas erradas)

- "Basta explicar o viés ao cliente para que ele mude a decisão."
- "Diante da insistência do cliente, o profissional deve recusar a ordem."
- "Se o cliente pediu, a ordem pode ser executada sem alerta."
- "O imóvel é investimento de baixo risco porque seu preço é estável."
- "Aversão à perda significa subestimar os ganhos."

> **Nomear é o começo; a prova cobra a ferramenta.**

**🔗 Ponte:** "Vamos aplicar num caso."

---

## 5. Case — 2 min

- "Seu Jorge, 58 anos, perfil moderado, chega com três falas. Primeira: 'Eu sei que tenho viés de status quo, você me explicou, mas faz dois anos que meu dinheiro está parado na conta'. Segunda: 'Li cinco artigos dizendo que o setor de energia vai disparar, quero pôr metade da carteira nele'. Terceira: 'Para a aposentadoria, em três anos, eu conto com a casa de praia; imóvel não cai'."

| Fala | Leitura técnica | Ferramenta |
| --- | --- | --- |
| "Faz dois anos que está parado" | **Status quo**; explicar não bastou (1.2.1 e 1.2.3) | Objetivo com valor e data, aporte automático, data marcada de revisão |
| "Cinco artigos a favor" | **Confirmação** e **excesso de confiança** (1.2.3) | Pedir o argumento contrário; registro datado; se mantiver fora do perfil, alerta e declaração (1.2.2) |
| "Conto com a casa de praia" | **Ilusão de segurança** do real; descasamento de prazo (1.2.4) | Mostrar os três atritos: liquidez, custo de transação e ausência de marcação |

- "Repare: em nenhuma das três você decide por ele. Você muda o ambiente, mostra o número e registra."

> **Explicar não basta: escreva a regra, peça o contra-argumento e mostre quanto tempo o freezer leva para descongelar.**

**🔗 Ponte:** "Agora, as questões."

---

## 6. Questões comentadas — 4 min

### Questão 1 — Fácil

**C-Pro R · 1.2.3 Mitigação de vieses · Fácil**

Ao preparar uma decisão de investimento, um cliente reúne apenas reportagens favoráveis à tese que já havia escolhido e admite não ter procurado opiniões contrárias. A ferramenta de mitigação mais adequada a esse comportamento é:

A) marcar uma data fixa de revisão da carteira, para combater a inércia.
B) solicitar que o cliente formule razões pelas quais a tese poderia não se confirmar, registrando-as antes da decisão.
C) explicar ao cliente o conceito de viés de confirmação e executar a decisão como foi trazida.
D) recomendar que o cliente reúna mais reportagens sobre o mesmo setor antes de decidir.

**Gabarito: B**

- **B (correta):** busca seletiva de informação favorável é **viés de confirmação**; a ferramenta é produzir o **argumento contrário** e registrá-lo.
- **A:** data de revisão é a ferramenta para o **status quo**.
- **C:** explicar o conceito não muda a decisão; o comando pede a ferramenta.
- **D:** mais material na mesma direção **reforça** o viés.
  - "Resposta B. Confirmação se mitiga com o contra-argumento."

### ➕ Questão 2 — Médio

**C-Pro R · 1.2.2 Gestão de risco e finanças comportamentais · Médio**

Uma cliente de perfil conservador solicita a aplicação em um produto de risco elevado após assistir a um vídeo. O profissional verifica que o produto é inadequado ao perfil dela e informa o resultado, mas a cliente mantém a ordem. De acordo com a Resolução CVM 30, antes da primeira operação com essa categoria de produto, o profissional deve:

A) alertá-la sobre a inadequação, indicando as causas da divergência, e obter declaração expressa de que está ciente.
B) recusar a ordem enquanto o perfil registrado for incompatível com o produto.
C) executar a ordem sem formalidades, pois a iniciativa partiu da própria cliente.
D) reclassificar o perfil da cliente para a categoria compatível com o produto e executar a ordem.

**Gabarito: A**

- **A (correta):** é o que exige o **art. 7º da CVM 30**: alerta com indicação das causas e declaração expressa de ciência.
- **B:** a norma **não** manda recusar automaticamente a ordem do cliente.
- **C:** a iniciativa do cliente não dispensa o alerta e a declaração.
- **D:** o perfil decorre das informações do cliente; mudá-lo para acomodar uma ordem desvirtua o suitability.
  - "Resposta A. Nem recusa, nem execução calada: alerta, declaração e registro."

### ➕ Questão 3 — Médio

**C-Pro R · 1.2.4 e 1.2.5 Investimentos reais × financeiros · Médio**

Um cliente afirma que seu imóvel de aluguel é o investimento mais seguro que possui, porque "o valor nunca caiu", embora a última avaliação formal tenha sido feita há três anos. Ele pretende vendê-lo para cobrir uma despesa daqui a oito meses. A leitura técnica correta é que:

A) o imóvel tem risco reduzido, já que seu valor permaneceu estável no período.
B) o imóvel tem liquidez equivalente à de um título público, por ser um bem de alto valor.
C) a ausência de oscilação demonstra que investimentos reais são mais adequados a objetivos de curto prazo.
D) a estabilidade aparente decorre da ausência de preço observado, e o prazo de venda incerto e o custo de transação podem comprometer o objetivo de curto prazo.

**Gabarito: D**

- **D (correta):** sem marcação diária, o imóvel **parece** estável; os atritos de **liquidez** e **custo de transação** tornam arriscado usá-lo num objetivo de oito meses.
- **A:** confunde ausência de marcação com ausência de risco.
- **B:** imóvel tem **liquidez menor** e prazo de venda incerto.
- **C:** inverte a conclusão: investimento real casa com objetivos **longos**.
  - "Resposta D. O imóvel não oscila menos; é observado menos."

### ➕ Questão 4 — Difícil (cálculo)

**C-Pro R · 1.2.2 e 1.2.3 Gestão de risco e mitigação de vieses · Difícil**

Um cliente aplicou R$ 80.000 em um título de renda fixa de 30 meses que rende o equivalente a 1% ao mês. No 5º mês (150 dias), assustado com uma notícia, resgatou tudo, deixou o dinheiro parado em conta por 2 meses e reaplicou o valor líquido nas mesmas condições pelos 23 meses restantes (690 dias). Considerando a tabela regressiva do IR em renda fixa (22,5% até 180 dias; 20% de 181 a 360; 17,5% de 361 a 720; 15% acima de 720 dias), o custo dessa decisão, em relação a manter a aplicação pelos 30 meses, foi de aproximadamente:

A) zero, pois o capital permaneceu em conta durante o período de instabilidade.
B) R$ 2.124,64.
C) R$ 2.847,36.
D) R$ 4.174,19.

**Gabarito: C**

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `80000` `CHS` `PV` `1` `i` `5` `n` `FV` | 🖥️ 84.080,80 | Rendimento 4.080,80; IR 22,5% = 918,18; líquido **83.162,62** |
| 2 | ⌨️ `f` `REG` `83162,62` `CHS` `PV` `1` `i` `23` `n` `FV` | 🖥️ 104.548,97 | Rendimento 21.386,35; IR 17,5% = 3.742,61; líquido **100.806,36** |
| 3 | ⌨️ `f` `REG` `80000` `CHS` `PV` `1` `i` `30` `n` `FV` | 🖥️ 107.827,91 | Rendimento 27.827,91; IR 15% = 4.174,19; líquido **103.653,73** |
| 4 | ⌨️ `103653,73` `ENTER` `100806,36` `−` | 🖥️ 2.847,36 | Custo da ida e volta |

- **C (correta):** 103.653,73 − 100.806,36 = **R$ 2.847,36** (3,56% do capital).
- **A:** ignora os juros dos 2 meses parados e o imposto antecipado em faixa mais alta.
- **B:** é só a diferença **bruta** dos juros (30 meses × 28 meses), sem considerar o IR nas faixas mais altas.
- **D:** é o IR do cenário em que o cliente **manteve** a aplicação, e não o custo da decisão.
  - "Resposta C. O susto custa os meses parados e o imposto na faixa errada."

**🔗 Ponte:** "Para fechar, a revisão."

---

## 7. Revisão final — 1 min

### Resumo em cinco pontos

1. Nomear o viés não muda a decisão; a prova cobra a aplicação: mudar o ambiente de decisão.
2. Estratégia comportamental é decisão escrita, com número e data: metas específicas, carteiras por objetivo, aporte automático, regras de compra e venda e avaliação periódica.
3. Gestão de risco separa risco percebido de risco real: percentual traduzido em reais, reserva, periodicidade de acompanhamento e, fora do perfil, alerta com a causa e declaração expressa (CVM 30, art. 7º).
4. Cada viés tem a sua ferramenta: processos, fontes diversificadas, registro de decisões e educação contínua. Mitigar não é decidir pelo cliente.
5. Investimento real tem baixa liquidez, custo alto e falta de marcação; parece estável porque é observado menos. O financeiro tem liquidez, preço transparente e diversificação.

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Estratégias (1.2.1) | Simplificar · metas · carteiras por objetivo · automatizar · regras prévias · revisão periódica |
| Gestão de risco (1.2.2) | Risco percebido ≠ real · rebalancear · diversificar · faixas-alvo · correlação · volatilidade em reais |
| Fora do perfil | CVM 30, art. 7º: alerta com a causa + declaração expressa, antes da 1ª operação na categoria |
| Mitigação (1.2.3) | Processos · fontes diversas · registro de decisões · educação contínua |
| Confirmação | Argumento contrário |
| Status quo | Data de revisão |
| Ancoragem | Trocar a âncora |
| Excesso de confiança | Registro datado |
| Real (1.2.4) | Baixa liquidez · manutenção · obsolescência · difícil precificar · pouca diversificação |
| Financeiro (1.2.5) | Liquidez · diversificação · acompanhamento · preço transparente · renda e valorização |
| Limite | Mitigar ≠ decidir pelo cliente |

### Cadeia lógica

**Viés nomeado → regra escrita a frio (mise en place) → risco medido e acompanhado (termômetro e timer) → ferramenta para cada viés (receita na parede) → ativo certo para o prazo certo (geladeira ou freezer)**

### Frase central da aula

> **Quem faz o mise en place decide com a panela fria; o seu papel é montar o mise en place com o cliente, e não comer o prato por ele.**

- "Voltando ao começo: o cliente que só vende quando a ação voltar ao preço pago. Você não diz 'isso é ancoragem'. Você pergunta: 'o que essa posição faz pelo seu objetivo, no valor de hoje?'. Na próxima aula, 1.3: quem é a pessoa do outro lado da mesa, com os dados das pesquisas sobre o investidor brasileiro."

---

## Nota de verificação

- **Programa Detalhado C-Pro R** (v1.2, rev. 04/06/2025, vigência 01/01/2026): itens 1.2 a 1.2.5 lidos no texto do PD do repositório.
- **Apostila C-Pro R** (Top Invest, rev. mar/2026), p. 43–47, e **slides X8 A5107** (6 telas): todos os subitens conferidos contra o PD.
- **Conferido em 20/10/2026:**
  - Resolução CVM 30/2021, texto consolidado (alterada pelas Res. 162/22 e 179/23), lido no PDF da CVM: art. 2º (vedação de recomendar sem verificar adequação), art. 6º (vedação quando o perfil é inadequado, ausente ou desatualizado) e art. 7º (alerta com indicação das causas da divergência e declaração expressa, antes da primeira operação com a categoria de valor mobiliário; dispensa quando o cliente segue recomendação de consultor autorizado);
  - Tabela regressiva do IR em renda fixa (Lei 11.033/2004, art. 1º) em vigor em 2026, após a **caducidade da MP 1.303/2025**, rejeitada pela Câmara em 08/10/2025 (fontes jornalísticas e de mercado);
  - Isenções do ganho de capital do imóvel: único imóvel até R$ 440 mil, sem outra venda em 5 anos (Lei 9.250/1995, art. 23) e reaplicação em imóvel residencial em 180 dias (Lei 11.196/2005, art. 39) (fontes secundárias; Receita Federal não lida diretamente). **Ficaram fora da fala.**
- **Não reaberto nesta sessão:** ITBI de 3% no município de São Paulo (conforme o caderno, aula 002); λ = 2,25 (Tversky e Kahneman, 1992), já usado na aula 1.1-A.
- **Cálculos conferidos em Python:** caso da Bianca (R$ 160.066,65 × R$ 163.938,42; diferença de R$ 3.871,77) e questão 4 (R$ 100.806,36 × R$ 103.653,73; diferença de R$ 2.847,36).
- **Acréscimos (➕):**
  - kit HP12C e caso da Bianca (do Caderno de Roteiros C-Pro R, aula 002; taxa hipotética);
  - conduta da CVM 30 diante da insistência do cliente;
  - tabela viés → ferramenta;
  - case do seu Jorge;
  - questões 2, 3 e 4 (inéditas, 4 alternativas).
