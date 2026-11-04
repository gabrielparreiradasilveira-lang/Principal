# C-PRO R · Aula 4 · Como montar a carteira e o que entra nela

**Escopo (Programa Detalhado ANBIMA C-Pro R, v1.2, revisado em 04/06/2025, vigência 01/01/2026):**
item 3.1 inteiro (asset allocation: 3.1.1 a 3.1.6) e itens 3.2.1.1 a 3.2.1.4 (renda fixa: definição e
características; títulos públicos; emissões bancárias; emissões corporativas). O macrotema 3 pesa 40% da prova.

**Duração:** 60 minutos (o pedido traz "1h" no cabeçalho e "90 minutos" na seção de organização; o deck foi
dimensionado para 60, no mesmo ritmo do deck de referência das Aulas 2 e 3, cerca de 2,4 min por slide).
A coluna "Se 90 min" mostra onde o tempo extra rende mais.

**Fio condutor:** Marina (cliente das Aulas 2 e 3: CLT, um filho, perfil moderado, acumulação, reserva agora
completa) pergunta se pode pôr tudo no CDB de 110% do CDI. A aula responde em três camadas: quanto vai em cada
classe (3.1), por que a renda fixa oscila (3.2.1.1 e 3.2.1.2) e o que distingue cada papel (3.2.1.3 e 3.2.1.4).

**Objetivo terminal:** ao final, o aluno consegue, diante de um caso, (1) montar e justificar uma alocação por
objetivo, perfil e fase de vida; (2) explicar o que oscila no extrato de renda fixa e escolher entre pré, pós e
híbrido; (3) classificar um papel bancário ou corporativo por emissor, garantia, FGC, tributação e risco, e decidir
se cabe na recomendação.

## Distribuição do tempo

| Bloco | Itens do PD | Slides | 60 min | Se 90 min | O que acontece |
|---|---|---|---|---|---|
| Abertura | — | 1–2 | 3 | 5 | Ponte com a Aula 3, pergunta da Marina, objetivos |
| Bloco 1 · Asset allocation | 3.1.1 a 3.1.6 | 3–8 | 14 | 20 | Fatores do retorno, processo, estratégica × tática, diversificação, classes, exemplo resolvido |
| Bloco 2 · Renda fixa: definição e dinâmica | 3.2.1.1 | 9–12 | 10 | 15 | Riscos, pré/pós/híbrido, primário × secundário, marcação a mercado e duration, exemplo resolvido |
| Bloco 3 · Títulos públicos | 3.2.1.2 | 13–15 | 7 | 11 | Família Tesouro, dívida pública e riscos, exemplo resolvido |
| Bloco 4 · Emissões bancárias | 3.2.1.3 | 16–19 | 11 | 17 | Treze papéis, FGC, ficha técnica, exemplo resolvido |
| Bloco 5 · Emissões corporativas | 3.2.1.4 | 20–23 | 11 | 17 | Debêntures e oferta pública, garantias e covenants, tributação e líquido, exemplo resolvido |
| Fechamento | — | 24–25 | 4 | 5 | Cinco ideias, checagem V/F, ponte para a Aula 5 |
| **Total** | | **25** | **60** | **90** | |

Com 90 minutos, o tempo extra vai para: resolver as seis questões autorais em sala (hoje estão nas notas, para
usar como quiser), fazer as contas de HP12C com a turma nos slides 11, 15 e 22 e abrir discussão nos "Pare e
pergunte" de cada bloco.

## Ciclo de cada bloco

Cada bloco segue ATIVAR (pergunta de abertura nas notas) → DEMONSTRAR (slides de conceito, com "Na fala do
cliente" e "Como agir") → APLICAR (exemplo resolvido em quatro passos) → VERIFICAR (questão autoral nas notas do
exemplo resolvido e checagem final no slide 25).

## Questões autorais (gabarito comentado nas notas)

| Nº | Slide | Item do PD | Dificuldade | Tema |
|---|---|---|---|---|
| 1 | 8 | 3.1.2 / 3.1.3 | Média | Estratégica × tática com Selic alta |
| 2 | 12 | 3.2.1.1.3 | Média | O que oscila no extrato em ciclo de alta da Selic |
| 3 | 15 | 3.2.1.1.5 / 3.2.1.2 | Difícil | Prefixado marcado a mercado: perda realizada ou não |
| 4 | 19 | 3.2.1.3.2 | Média | FGC: mesmo conglomerado e papel sem cobertura |
| 5 | 23 | 3.2.1.4.5 | Fácil | CDB 110% × LCA 95%: comparar pelo líquido |
| 6 | 21 | 3.2.1.4.7 / 3.2.1.4.8 | Difícil | Quebra de covenant em debênture com garantia flutuante |

---

# Slide a slide


## Slide 1 · Como montar a carteira e o que entra nela

**Marcador:** C-PRO R  ·  AULA 4  
**Tempo:** 1 min

**Conteúdo visível:**

- Blocos 1 a 5: alocação e renda fixa Asset allocation (3.1) e instrumentos de renda fixa: definição, títulos públicos, emissões bancárias e corporativas (3.2.1.1 a 3.2.1.4)
- O foco é aprender. A aprovação é consequência.

**Recurso visual:** Capa X8 (fundo navy, logo à direita, kicker dourado, título Cambria).

**Notas do professor:**

> PONTE COM A AULA 3: fechamos com a Marina (CLT, um filho, renda R$ 12.000, despesas R$ 9.600, perfil moderado, fase de acumulação) decidindo completar a reserva antes de comprar ações. Hoje a reserva está completa (R$ 57.600) e a pergunta muda: o que entra na carteira e em que proporção.
>
> ESCOPO (Programa Detalhado C-Pro R v1.2, vigência 01/01/2026): 3.1 inteiro (asset allocation) e 3.2.1.1 a 3.2.1.4 (renda fixa: definição e características, títulos públicos, emissões bancárias, emissões corporativas). Peso do macrotema 3 na prova: 40%.
>
> CONDUÇÃO: diga em uma frase a espinha dorsal da aula: primeiro decide-se QUANTO vai em cada classe (3.1); só depois escolhe-se O QUE comprar dentro da renda fixa (3.2).

## Slide 2 · Marina pergunta: "Tudo no CDB de 110% do CDI?"

**Marcador:** ABERTURA · O QUE VOCÊ VAI CONSEGUIR FAZER  
**Tempo:** 2 min

**Conteúdo visível:**

- A SITUAÇÃO
- Reserva completa: R$ 57.600 em liquidez diária. Dinheiro novo: R$ 36.000 e mais R$ 2.400 por mês. Perfil: moderado, fase de acumulação. Objetivos: carro em 3 anos, faculdade do filho em 15, aposentadoria em 25 ou mais. "O gerente disse que o CDB de 110% do CDI é o melhor. Coloco tudo lá?"
- 1 · Alocar
- Montar e justificar uma alocação por objetivo, perfil e fase de vida (3.1).
- 2 · Explicar o extrato
- Dizer por que a renda fixa oscila e escolher entre pré, pós e IPCA+ (3.2.1.1 e 3.2.1.2).
- 3 · Classificar papéis
- Separar emissões bancárias e corporativas por garantia, FGC, tributação e risco (3.2.1.3 e 3.2.1.4).
- NA PROVA
- A banca cobra decisão, não definição: situação do cliente, recomendação adequada e o porquê. A resposta certa quase sempre começa pelo objetivo, não pelo produto.

**Recurso visual:** Card de situação à esquerda (dados da Marina + fala do cliente em itálico) e três cards de objetivo à direita, o terceiro em azul de destaque. Barra NA PROVA.

**Notas do professor:**

> GANCHO: deixe a pergunta da Marina no ar. Quase todo aluno já ouviu isso de um cliente. Não responda agora: a resposta fecha a aula (slide 23).
>
> OBJETIVOS (Backward Design): os três cartões da direita são o que vai ser verificado no fim. Se o aluno sair sabendo (1) distribuir por classe antes de escolher produto, (2) explicar por que o extrato oscila e (3) separar isento de garantido, a aula cumpriu o objetivo.
>
> PREMISSAS DA MARINA (continuidade da Aula 3): reserva de 6 meses × R$ 9.600 = R$ 57.600, completa. Dinheiro novo de R$ 36.000 é premissa desta aula (bônus + poupança acumulada).
>
> PARE E PERGUNTE: 'O que está errado na frase do gerente?'. Respostas esperadas: 'melhor para quem?', 'para qual objetivo?', 'de que banco?'. Anote no quadro: as três perguntas voltam nos Blocos 1, 2 e 4.

## Slide 3 · O retorno nasce da alocação, não do timing

**Marcador:** BLOCO 1 · 3.1.6 E 3.1.4  
**Tempo:** 2 min

**Conteúdo visível:**

- Três decisões explicam o resultado de uma carteira. Só uma delas pesa de verdade.
- ASSET ALLOCATION
- cerca de 90%
- da variabilidade do retorno vem de quanto vai em cada classe (Brinson, Hood e Beebower, 1986: 93,6%)
- MARKET TIMING
- parcela pequena
- entrar e sair conforme o momento. Errar o dia custa caro e o acerto não se repete
- SELEÇÃO DE ATIVOS
- parcela pequena
- qual CDB, qual ação, qual fundo. Importa, mas depois de definir a classe
- NA PROVA
- Entre "escolher o melhor fundo" e "definir quanto vai em cada classe", a segunda explica a maior parte do resultado. Timing é o fator menos confiável: a prova pune quem o trata como estratégia.

**Recurso visual:** Três cards comparativos com número grande; o primeiro (asset allocation) em azul de destaque. Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.1.6): o programa lista três fatores determinantes do retorno no longo prazo: asset allocation (política de alocação entre classes), market timing (mudar a exposição conforme a expectativa de mercado) e escolha de ativos (seleção dentro da classe). O estudo clássico de Brinson, Hood e Beebower (Financial Analysts Journal, 1986), com fundos de pensão americanos, encontrou que 93,6% da VARIABILIDADE dos retornos ao longo do tempo era explicada pela política de alocação. Diga 'variabilidade', não 'nível': é a leitura correta do estudo e evita contestação.
>
> EXEMPLO: dois clientes com o mesmo gestor de ações: um tem 10% em ações, outro tem 60%. A diferença entre as carteiras em um ano de queda de 30% na bolsa vem da alocação (−3% contra −18%), não da habilidade do gestor.
>
> ANALOGIA: a alocação é o leme; timing e seleção são os remos. Remar forte com o leme errado leva longe do destino. Onde a analogia quebra: no barco, o leme é uma decisão só; na carteira, a alocação é revisada quando a vida muda.
>
> NA PROVA: enunciado típico: cliente quer 'esperar o melhor momento' para investir. A resposta adequada ignora o timing e volta ao plano (objetivo, prazo, perfil).

## Slide 4 · Alocar tem quatro passos; o produto é o terceiro

**Marcador:** BLOCO 1 · 3.1.3  
**Tempo:** 2,5 min

**Conteúdo visível:**

- REGRA  Quem começa pelo produto ("qual CDB?") inverte o processo. O produto só aparece depois que o perfil, os objetivos e os pesos por classe já estão definidos.
- Conhecer
- Perfil (Aula 3), objetivos com valor e prazo, horizonte, restrições: liquidez, tributação, regras internas
- Definir pesos
- Alocação estratégica: classes, pesos-alvo e bandas de tolerância (ex.: 25% em ações, ±5 p.p.)
- Implementar
- Escolher os produtos dentro de cada classe. Aqui entra "qual CDB", "qual fundo"
- Monitorar
- Rebalancear ao sair da banda; rever a estratégia quando a vida do cliente mudar
- NA PROVA
- Rebalancear é vender o que subiu e comprar o que caiu para voltar ao peso-alvo. Não é market timing: é disciplina de voltar ao plano. O gatilho é a banda ou a data, não a notícia.

**Recurso visual:** Barra REGRA no topo e fluxo de quatro passos com chevrons dourados; o quarto passo em azul. Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.1.3): os pilares do processo de alocação. (1) Conhecer: tudo o que a Aula 3 construiu (suitability, objetivos, horizonte, tolerância e capacidade, fase de vida) mais as restrições: necessidade de liquidez, situação tributária (quem declara no modelo completo valoriza isentos), limites regulatórios ou da instituição. (2) Definir a alocação estratégica: pesos-alvo por classe e bandas. (3) Implementar: seleção dos produtos. (4) Monitorar e rebalancear.
>
> EXEMPLO (rebalanceamento): carteira de R$ 100.000 com alvo de 25% em ações (banda ±5 p.p.). Ações sobem 40%: passam a R$ 35.000 de R$ 110.000 = 31,8%. Saiu da banda (30%): vende R$ 7.500 de ações e compra renda fixa até voltar a 25%. HP12C: 110000 ENTER 25 % → 27.500 (alvo); 35000 ENTER 27500 − → 7.500.
>
> PARE E PERGUNTE: 'Rebalancear depois de uma alta é vender na alta. E depois de uma queda?'. Resposta: comprar o que caiu. É o oposto do que o cliente quer fazer por instinto (finanças comportamentais, Aula 1).
>
> NA PROVA: distrator comum: 'alterar a alocação estratégica porque o mercado caiu'. A estratégica muda com a vida; o mercado só autoriza ajuste tático dentro da banda (próximo slide).

## Slide 5 · A estratégica segue a vida; a tática segue o mercado

**Marcador:** BLOCO 1 · 3.1.1 E 3.1.2  
**Tempo:** 2,5 min

**Conteúdo visível:**

- Alocação estratégica
- Quanto vai em cada classe no longo prazo?
- NATUREZA
- Deriva do perfil, dos objetivos e da fase de vida. Pesos-alvo com bandas.
- SINAL
- Muda quando a VIDA muda
- Marina: 60% renda fixa · 25% ações · 15% multimercado e FII, bandas de ±5 p.p.
- Alocação tática
- Onde ficar dentro da banda, agora?
- NATUREZA
- Desvio temporário a partir do momento de mercado: juros, inflação, preços.
- SINAL
- Muda quando o MERCADO muda
- Juro alto: Marina vai a 65% de renda fixa, mais pós-fixado. Nunca a 80%.
- NA PROVA
- Aderência (3.1.1): a carteira tem de caber no perfil E na fase de vida ao mesmo tempo. Juros altos justificam tática em pós-fixado dentro da banda; nunca justificam sair do perfil.

**Recurso visual:** Dois cards espelhados (estratégica × tática): pergunta, natureza, sinal em dourado e exemplo da Marina. Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.1.2): alocação estratégica é a política de longo prazo: pesos-alvo por classe que traduzem o perfil e os objetivos. Alocação tática é o desvio deliberado e temporário em relação ao alvo, motivado pelo momento de mercado, limitado pelas bandas. Pesos e bandas são convenção desta aula para a Marina (moderada, acumulação), não norma.
>
> EXPLICAÇÃO (3.1.1): aderência ao perfil e à fase de vida. O perfil (Aula 3, 2.4.6) dá o teto de risco; a fase de vida (2.4.8) ajusta a capacidade. Uma carteira pode caber no perfil e não caber na fase (aposentado moderado com 40% em ações ilíquidas) ou vice-versa.
>
> EXEMPLO: Selic alta. A tática manda elevar pós-fixado: Marina passa de 60% para 65% de renda fixa, dentro da banda. Quando o ciclo virar, volta ao alvo. O que não pode: ir a 80% 'porque o CDI está bom', porque isso rompe a banda e deixa o longo prazo sem renda variável.
>
> PARE E PERGUNTE: 'Marina ficou desempregada. Isso é mudança de vida ou de mercado?'. Vida: a estratégica muda (mais liquidez, menos risco) até a renda voltar.
>
> NA PROVA: caderno oficial traz caso de cliente que pode trocar de emprego e pede mais risco 'para aproveitar enquanto tem renda'. Resposta adequada: incerteza de renda reduz capacidade de risco; a alocação estratégica fica mais conservadora, não mais agressiva.

## Slide 6 · Diversificar funciona porque os ativos não caem juntos

**Marcador:** BLOCO 1 · 3.1.4  
**Tempo:** 2,5 min

**Conteúdo visível:**

- Retornos ilustrativos de um ano, para mostrar o mecanismo (não são projeções).
- Tabela:
    Cenário do ano | Só ações | Só Tesouro IPCA+ | Carteira 50% / 50%
    Recessão: bolsa cai, juro cai | −20% | +12% | −4%
    Expansão: bolsa sobe | +30% | +5% | +17,5%
    Ano morno | +8% | +7% | +7,5%
    Oscilação (pior ao melhor) | 50 pontos | 7 pontos | 21,5 pontos

- REDUZ: risco não sistemático: de um emissor, uma empresa, um setor.
- NÃO REDUZ: risco sistemático: juros, recessão, crise. Atinge todos.
- ANALOGIA
- Ovos em cestas diferentes funciona para o emissor. Quebra quando as cestas vão no mesmo caminhão: dez CDBs de bancos pequenos diversificam o crédito, não o risco de juros.

**Recurso visual:** Tabela de cenários (4 colunas) com a carteira 50/50 em dourado; dois mini-cards (reduz / não reduz); barra ANALOGIA.

**Notas do professor:**

> EXPLICAÇÃO (3.1.4): o poder da diversificação vem da correlação menor que 1 entre as classes. Quando um ativo cai e o outro sobe (ou cai menos), a carteira oscila menos do que a média das oscilações. Na tabela, a carteira 50/50 tem amplitude de 21,5 pontos contra 50 pontos das ações, com retorno médio próximo. Números ilustrativos: construídos para mostrar o mecanismo.
>
> CONTAS: recessão: 0,5 × (−20%) + 0,5 × 12% = −4%. Expansão: 0,5 × 30% + 0,5 × 5% = 17,5%. Morno: 0,5 × 8% + 0,5 × 7% = 7,5%.
>
> DOIS RISCOS: não sistemático (específico: um emissor quebra, um setor sofre) some com diversificação. Sistemático (juros, câmbio, recessão) não some: só se gerencia com a alocação e o horizonte.
>
> ANALOGIA, ONDE QUEBRA: 'não coloque todos os ovos na mesma cesta' trata apenas do emissor. Dez CDBs de dez bancos pequenos pós-fixados são a mesma cesta no mesmo caminhão: todos reagem igual à Selic. Diversificar de verdade é misturar o que move o preço (próximo slide).
>
> NA PROVA: 'diversificar elimina o risco' está errado; elimina o não sistemático. E diversificar demais (dezenas de produtos iguais) é custo sem benefício.

## Slide 7 · Classe: o que move o preço; subclasse: o detalhe

**Marcador:** BLOCO 1 · 3.1.5  
**Tempo:** 1,5 min

**Conteúdo visível:**

- Tabela:
    Classe | O que move o preço | Subclasses | Função na carteira
    Caixa e pós-fixado | Selic e CDI do dia | Tesouro Selic, CDB DI, fundos DI, compromissadas | Reserva, caixa dos objetivos, tática em juro alto
    Renda fixa pré e inflação | Juros futuros e inflação esperada | Prefixados, IPCA+, crédito privado (debênture, CRI, CRA) | Objetivos com data; proteção do poder de compra
    Renda variável | Lucros e risco de mercado | Ações Brasil, exterior, FII, small caps | Crescimento de longo prazo
    Multimercado e alternativos | Estratégia do gestor; ativos sem bolsa | Multimercados, câmbio, cripto, private equity | Descorrelação; exposição a outros fatores

- NA PROVA
- Subclasse se define por indexador, emissor (público ou privado), prazo e grau de crédito. CDB prefixado e Tesouro Selic são renda fixa, mas reagem ao juro de forma oposta.

**Recurso visual:** Tabela 4 × 4: classe, o que move o preço, subclasses, função. Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.1.5): classe de ativos é um conjunto de investimentos que reagem aos mesmos fatores de risco. A pergunta-chave para classificar é 'o que faz o preço se mover?'. Subclasse é o recorte dentro da classe: por indexador (pré, Selic/CDI, IPCA), por emissor (público, bancário, corporativo), por prazo (curto, longo), por qualidade de crédito (grau de investimento ou especulativo), por geografia (Brasil, exterior).
>
> EXEMPLO: para a Marina, 'renda fixa 60%' não basta como instrução. A subclasse decide: 20% pós-fixado (caixa dos objetivos de curto prazo), 25% IPCA+ longo (faculdade, aposentadoria), 15% crédito privado (incentivadas, CRI). Cada subclasse tem um papel.
>
> NA PROVA: a banca descreve dois produtos da mesma classe e pergunta qual se adequa a um objetivo. A resposta sai da subclasse: indexador e prazo casados com o objetivo (Bloco 2).
>
> PONTE: a partir daqui, a aula desce da classe para o produto: a renda fixa, que é o que a Marina mais compra.

## Slide 8 · Marina tem R$ 36.000 novos. Onde cada real entra?

**Marcador:** EXEMPLO RESOLVIDO · 3.1  
**Tempo:** 3 min

**Conteúdo visível:**

- SITUAÇÃO  Reserva completa (R$ 57.600 em liquidez). Perfil moderado, fase de acumulação. Carro em 3 anos (R$ 40.000), faculdade do filho em 15 anos, aposentadoria em 25 ou mais. Poupa R$ 2.400 por mês.
- Por objetivo
- Carro: 3 anos, renda fixa com data. Faculdade e aposentadoria: longo prazo, aceitam oscilação
- Pesos-alvo
- 60 · 25 · 15
- Renda fixa, ações, multimercado e FII. Bandas de ±5 p.p.
- Implementar
- Carro: Tesouro IPCA+ 2029. Longo prazo: IPCA+ 2040, fundo de ações, FII. CDB 110% do CDI: só a parte de caixa
- Monitorar
- Revisar a cada 12 meses ou quando mudar emprego, renda ou família. Rebalancear fora da banda
- RESPOSTA
- A alocação sai do objetivo e do perfil, não do produto da semana. O CDB de 110% do CDI pode entrar na parte pós-fixada da carteira; nunca ser a carteira inteira.

**Recurso visual:** Card SITUAÇÃO + fluxo de quatro passos (número grande 60 · 25 · 15 no passo 2); passo 4 em azul. Barra RESPOSTA.

**Notas do professor:**

> EXEMPLO RESOLVIDO: percorra os quatro passos do Bloco 1 com a Marina. Os pesos (60/25/15) e as bandas são convenção desta aula para um perfil moderado em acumulação; o que importa é o método.
>
> CONTAS: R$ 36.000 × 60% = R$ 21.600 em renda fixa; × 25% = R$ 9.000 em ações; × 15% = R$ 5.400 em multimercado e FII. Dentro da renda fixa: o carro precisa de R$ 40.000 em 3 anos; com R$ 15.000 iniciais e aportes, HP12C: f REG · 36 n · 0,7 i (premissa, 0,7% a.m. real) · 15000 CHS PV · 40000 FV · PMT → cerca de −600. Ou seja, R$ 600 por mês dos R$ 2.400 vão para o carro; o resto, para o longo prazo.
>
> PARE E PERGUNTE (antes de revelar o passo 3): 'O CDB de 110% do CDI entra onde?'. Resposta: na subclasse pós-fixada, como caixa dos objetivos de curto prazo. Não é ruim; é parcial.
>
> — — —
>
> QUESTÃO 1 (autoral · 3.1 · dificuldade média · nível: aplicação)
> Rafael, profissional C-Pro R, atende Paula, 38 anos, perfil moderado, reserva de emergência completa, com dois objetivos: trocar de carro em 2 anos e aposentar-se em 27 anos. A Selic está alta e Paula pede para aplicar 100% do dinheiro novo em CDB pós-fixado "enquanto o juro estiver bom". A orientação mais adequada é:
> A) Atender ao pedido, porque juros altos justificam concentrar em pós-fixado até o cenário mudar.
> B) Definir primeiro a alocação estratégica por objetivo e perfil e, se couber, usar o pós-fixado como ajuste tático dentro das bandas.
> C) Aplicar tudo em renda variável, porque o horizonte de 27 anos exige o máximo de crescimento.
> D) Dividir em partes iguais entre todas as classes, para garantir diversificação.
>
> GABARITO: B. A estratégica vem do objetivo e do perfil; o momento de mercado só autoriza desvio tático dentro das bandas (3.1.2 e 3.1.3).
> A) troca estratégia por timing: concentra 100% com base no cenário, sem plano de volta.
> C) ignora o carro em 2 anos (dinheiro com data não vai para ativo volátil) e o perfil moderado.
> D) pesos iguais não são alocação: diversificação sem relação com objetivo, prazo ou perfil (3.1.4 e 3.1.5).
> Conceito-chave: estratégica define, tática ajusta. Pegadinha: 'juro alto' como justificativa para abandonar o plano.

## Slide 9 · Renda fixa: a regra é fixa; o resultado, nem sempre

**Marcador:** BLOCO 2 · 3.2.1.1.1 E 3.2.1.1.2  
**Tempo:** 2,5 min

**Conteúdo visível:**

- O QUE É
- Título de dívida: você empresta, o emissor promete devolver com juros por uma regra definida na emissão: pré, pós ou híbrida.
- NA FALA DO CLIENTE
- "É renda fixa, então não tem risco."
- COMO AGIR
- Perguntar quem deve (crédito), quando o dinheiro volta (liquidez) e o que acontece se vender antes (mercado).
- Risco de crédito
- O emissor não paga. Mitigantes: rating, garantias, FGC (só bancários), diversificar emissor.
- Risco de liquidez
- Não consegue vender a tempo ou só com deságio. Mitigantes: prazo casado com o objetivo, papel com mercado secundário.
- NA PROVA
- Vantagem por perfil: para o conservador é o núcleo (previsibilidade); para o arrojado, o lastro de liquidez e o redutor de volatilidade. Para todos: reserva, objetivo com data e proteção contra inflação.

**Recurso visual:** Card "O que é / Na fala do cliente / Como agir" à esquerda; dois cards de risco à direita (liquidez em azul). Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.1): renda fixa é o título em que a REGRA de remuneração é conhecida na compra (taxa fixa, percentual do CDI, IPCA + taxa). 'Fixa' é a regra, não o resultado: se vender antes do vencimento, o preço é o de mercado (Bloco 2, slide 11).
>
> RISCO DE CRÉDITO (3.2.1.1.1): o emissor deixa de pagar. Quanto pior o crédito, maior a taxa exigida. Mitigantes: rating, garantias (Bloco 5), FGC (só para emissões bancárias cobertas, Bloco 4), diversificação por emissor.
>
> RISCO DE LIQUIDEZ: não há comprador no prazo ou só com deságio relevante. Retome a definição da Aula 3 (2.2.1): liquidez é prazo E preço. CDB sem liquidez antes do vencimento, debênture pouco negociada, LCI com carência.
>
> VANTAGENS POR PERFIL (3.2.1.1.2): conservador: previsibilidade de fluxo e preservação; moderado: base da carteira e caixa dos objetivos com data; arrojado: reserva de liquidez para comprar risco na queda e redutor de volatilidade. O ponto da banca: renda fixa não é 'produto de conservador'; é classe que todo perfil usa com funções diferentes.
>
> NA PROVA: 'renda fixa não tem risco' é a afirmação errada mais frequente nos distratores. Tem crédito, liquidez e mercado.

## Slide 10 · Pré, pós ou híbrido: o que você quer travar?

**Marcador:** BLOCO 2 · 3.2.1.1.4 E 3.2.1.1.5  
**Tempo:** 2 min

**Conteúdo visível:**

- Tabela:
    Forma | Como rende | Ganha quando | Exemplos
    Prefixado | Taxa fixa na compra (ex.: 12% a.a.) | Juros caem depois da compra | LTN, NTN-F, CDB pré, LCI pré
    Pós-fixado | Índice diário: Selic ou CDI | Juros sobem ou cenário incerto | LFT, CDB CDI+, LCA % do CDI
    Híbrido | IPCA + taxa real (ex.: IPCA + 6%) | Inflação surpreende para cima | NTN-B, CDB IPCA+, debênture IPCA+

- MERCADO PRIMÁRIO
- Emissão: o dinheiro vai para o emissor (Tesouro, banco, empresa). Preço e taxa definidos na oferta.
- MERCADO SECUNDÁRIO
- Negociação entre investidores: o preço muda todo dia e o emissor não recebe nada. É onde nasce a marcação a mercado.
- NA PROVA
- Prefixado trava a TAXA, não o resultado se vender antes. Pós-fixado não protege da inflação; o híbrido protege. Quem compra no secundário com deságio ganha a taxa nova, não a da emissão.

**Recurso visual:** Tabela pré × pós × híbrido (como rende, ganha quando, exemplos) e dois cards: mercado primário × secundário (secundário em azul). Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.1.4): prefixado: o investidor sabe hoje quanto recebe no vencimento; aposta implícita em queda (ou estabilidade) dos juros. Pós-fixado: rende o índice do período (Selic, CDI); protege em alta de juros. Híbrido: parte pós (IPCA) + parte pré (taxa real); protege o poder de compra. Variações de convenção: '110% do CDI' (percentual) e 'CDI + 2%' (spread) são ambos pós-fixados.
>
> EXPLICAÇÃO (3.2.1.1.5): mercado primário é a emissão; secundário é a revenda entre investidores. O emissor só capta no primário. No secundário, o preço reflete a taxa de mercado do dia: por isso há marcação a mercado. CDB, RDB, LCI e LCA praticamente não têm secundário (ou o emissor recompra 'na curva'); títulos públicos, debêntures, CRI e CRA têm.
>
> EXEMPLO: cliente com objetivo em 3 anos e Selic alta. Se os juros caírem, o prefixado de 3 anos rende mais do que o pós; se subirem, o pós ganha. Quem não sabe (ninguém sabe) divide: metade pré, metade pós, ou escolhe o híbrido se o medo é a inflação.
>
> PARE E PERGUNTE: 'Um CDB IPCA+ 6% é pré ou pós?'. Híbrido: a taxa real é fixa, o IPCA é pós.
>
> NA PROVA: a banca descreve o cenário (Selic caindo, inflação subindo) e pergunta qual forma de remuneração se beneficia. Associe: queda de juros → pré; alta de juros → pós; inflação acima do esperado → híbrido.

## Slide 11 · Juro sobe, preço cai: a duration diz quanto

**Marcador:** BLOCO 2 · 3.2.1.1.3 E 3.2.1.1.5  
**Tempo:** 3 min

**Conteúdo visível:**

- A gangorra do preço
- Preço hoje = valor de resgate trazido pela taxa de mercado. Taxa sobe, preço cai. Taxa cai, preço sobe. No vencimento, recebe o combinado.
- EXEMPLO
- R$ 1.000 daqui a 1 ano: a 10% vale R$ 909; a 12% vale R$ 893 (−1,8%).
- Duration
- Prazo médio dos fluxos do título. Mede a sensibilidade: variação do preço ≈ −duration × variação da taxa.
- EXEMPLO
- Duration de 7,8 e taxa +1 p.p.: preço cai cerca de 7,8%. Mais prazo e menos cupom: mais duration.
- SOFREM MAM: títulos públicos, debêntures, CRI, CRA (têm secundário; extrato marcado desde 2023).  FICAM NA CURVA: CDB, RDB, LCI, LCA.
- NA PROVA
- Pós-fixado Selic tem duration curtíssima: quase não oscila. Pré e IPCA+ longos oscilam muito. A marcação só vira resultado se vender antes do vencimento.

**Recurso visual:** Dois cards: "gangorra do preço" (com exemplo numérico em dourado) e "duration" (fórmula e exemplo). Faixa SOFREM MAM × FICAM NA CURVA. Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.1.3): marcação a mercado (MaM) é registrar o título pelo preço que ele teria se fosse vendido hoje. Como o preço de um título prefixado é o valor de resgate descontado pela taxa de mercado, taxa e preço andam em direções opostas. No vencimento, o preço converge para o valor de resgate: quem segura até o fim recebe a taxa contratada.
>
> CONTA DO EXEMPLO (HP12C): 1000 CHS FV · 1 n · 10 i · PV → 909,09. Depois 12 i · PV → 892,86. Queda de 1,8%. Para 5 anos: 5 n · 10 i · PV → 620,92; 12 i · PV → 567,43: queda de 8,6%. Mesmo choque, prazo maior, perda maior: isso é duration.
>
> DURATION: prazo médio ponderado dos fluxos (Macaulay). Título sem cupom: duration = prazo. Cupons antecipam fluxo e reduzem a duration. A duration modificada aproxima a variação percentual do preço para 1 p.p. de taxa. O caderno oficial da C-Pro R usa exatamente isso: CRI com duration 7,8 e choque de +1 p.p. → perda próxima de 7,8%.
>
> QUEM SOFRE MAM NO EXTRATO: pelas Regras e Procedimentos ANBIMA de marcação a mercado, desde 2 de janeiro de 2023 os distribuidores marcam a mercado títulos públicos, debêntures, CRI e CRA na posição do cliente. CDB, RDB, LCI e LCA, sem mercado secundário relevante, seguem 'na curva' (taxa contratada apropriada no tempo).
>
> NA PROVA: a banca descreve um cenário de juros (alta ou queda) e uma carteira com vários papéis e pergunta o que oscila e para que lado. Regra: tem secundário + taxa travada = oscila; pós-fixado = varia pouco; sem secundário = na curva (próximo slide).

## Slide 12 · Selic em queda: por que o extrato da Verônica mudou?

**Marcador:** EXEMPLO RESOLVIDO · 3.2.1.1  
**Tempo:** 2,5 min

**Conteúdo visível:**

- SITUAÇÃO  Carteira: Tesouro Prefixado (LTN), Tesouro Selic (LFT), CDB CDI+ e RDB prefixado. Nos últimos meses, inflação estável e Selic em queda. Verônica não entende as variações do extrato.
- LTN
- Subiu
- Pré com secundário: a taxa caiu, o preço subiu por marcação a mercado
- LFT
- Varia pouco
- Pós-fixada à Selic diária: duration curta, quase sem efeito de preço
- CDB CDI+
- Desacelera
- Rende o CDI do dia, agora menor. Sem efeito de preço: fica na curva
- RDB pré
- Igual
- Taxa contratada apropriada no tempo; sem secundário, sem marcação
- RESPOSTA
- Oscila o que tem mercado secundário e taxa travada. A LTN subiu porque a taxa caiu; os pós-fixados só passaram a render menos por dia; o RDB não muda de preço.

**Recurso visual:** Card SITUAÇÃO + quatro cards (um por papel) com o veredito em dourado: Subiu / Varia pouco / Desacelera / Igual. Barra RESPOSTA.

**Notas do professor:**

> EXEMPLO RESOLVIDO: baseado na Questão 12 do caderno oficial de questões da C-Pro R (PD 3.2.1.4, dificuldade fácil). A banca descreve a carteira, o cenário (Selic em queda, inflação estável) e pede a explicação correta para cada papel.
>
> CONDUÇÃO: mostre só a situação e pergunte, papel por papel: 'sobe, cai ou não muda?'. Revele os cartões depois das respostas. O erro mais comum é dizer que a LFT 'valoriza por marcação a mercado'. Ela acompanha a taxa diária e tem duration mínima.
>
> ERROS QUE A BANCA EXPLORA: (1) trocar LTN e LFT; (2) achar que o CDB CDI+ 'sobe' quando a Selic cai (ele rende menos); (3) achar que o RDB prefixado sofre marcação (não tem mercado secundário: é intransferível).
>
> — — —
>
> QUESTÃO 2 (autoral · 3.2.1.1 · dificuldade média · nível: aplicação)
> A carteira de um cliente tem Tesouro Prefixado 2032, Tesouro Selic 2029, CDB pós-fixado a 102% do CDI e LCI prefixada de 2 anos. O Banco Central inicia um ciclo de ALTA da Selic. O profissional deve explicar que o efeito imediato nos extratos tende a ser:
> A) O Tesouro Prefixado 2032 cai por marcação a mercado; o Tesouro Selic varia pouco; o CDB passa a render mais a cada dia; a LCI segue a taxa contratada, sem marcação.
> B) Todos os títulos caem, porque juro mais alto reduz o valor de qualquer renda fixa.
> C) A LCI prefixada cai por marcação a mercado, enquanto o Tesouro Prefixado é protegido pela garantia do Tesouro.
> D) O Tesouro Selic cai por marcação a mercado, por ter prazo longo.
>
> GABARITO: A. Alta de taxa derruba o preço do prefixado longo com secundário (duration alta); a LFT acompanha a Selic diária; o CDB pós rende mais; a LCI, sem secundário, fica na curva.
> B) generaliza: pós-fixados não caem de preço com alta de juros.
> C) inverte: LCI não é marcada a mercado no extrato; a garantia do Tesouro é de crédito, não de preço.
> D) prazo longo não importa para a LFT: ela é pós-fixada diária, duration próxima de zero.
> Conceito-chave: oscila quem tem secundário e taxa travada. Pegadinha: confundir garantia de crédito com proteção de preço.

## Slide 13 · Tesouro: seis nomes, três indexadores

**Marcador:** BLOCO 3 · 3.2.1.2  
**Tempo:** 2,5 min

**Conteúdo visível:**

- Tabela:
    Nome no Tesouro Direto | Título | Rende | Para quê
    Tesouro Selic | LFT | Selic diária | Reserva, caixa, tática em juro alto
    Tesouro Prefixado | LTN | Taxa fixa, sem cupom | Objetivo com data; queda de juros
    Tesouro Prefixado com juros semestrais | NTN-F | Taxa fixa + cupom semestral | Renda periódica; duration menor
    Tesouro IPCA+ | NTN-B Principal | IPCA + taxa real, sem cupom | Longo prazo; poder de compra
    Tesouro IPCA+ com juros semestrais | NTN-B | IPCA + cupom semestral | Renda real periódica
    Tesouro RendA+ e Educa+ | NTN-B1 | IPCA + taxa; renda mensal após carência | Aposentadoria e educação

- NA PROVA
- Cupom reduz a duration e cria risco de reinvestimento. Liquidez: o Tesouro recompra todo dia útil, a preço de mercado: liquidez alta, preço não garantido antes do vencimento.

**Recurso visual:** Tabela 6 × 4 da família Tesouro Direto (nome, título, rende, para quê). Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.2): principais títulos públicos federais e seus indexadores. LFT: pós-fixada à Selic. LTN: prefixada, sem cupom (zero cupom: paga tudo no vencimento). NTN-F: prefixada com cupom semestral. NTN-B Principal: IPCA + taxa real, sem cupom. NTN-B: IPCA + cupom semestral. NTN-B1 (RendA+ e Educa+): IPCA + taxa, com fase de acumulação e depois 240 (RendA+) ou 60 (Educa+) pagamentos mensais.
>
> CUPOM: antecipa parte do fluxo, por isso reduz a duration (menos sensível ao juro) e cria risco de reinvestimento (o cupom recebido será reaplicado à taxa do dia, que pode ser menor). Também gera IR a cada pagamento.
>
> LIQUIDEZ NO TESOURO DIRETO: o Tesouro Nacional garante a recompra em todo dia útil, pelo preço de mercado. Liquidez é alta; o preço antes do vencimento não é. Custódia dos títulos públicos: Selic (sistema do Banco Central), com a B3 como agente de custódia no Tesouro Direto.
>
> EXEMPLO: Marina, faculdade em 15 anos: Tesouro IPCA+ 2040 (NTN-B Principal) casa prazo e protege o poder de compra. Para o carro em 3 anos: Tesouro Prefixado ou IPCA+ com vencimento próximo de 2029.
>
> NA PROVA: 'Tesouro IPCA+' é pré ou pós? Híbrido. 'Tesouro Selic rende exatamente a Selic?' Rende Selic mais um pequeno ágio ou deságio, com taxa de custódia da B3 acima de R$ 10 mil. Detalhe de prova: cite, não aprofunde.

## Slide 14 · Dívida pública: grande, líquida e sensível ao juro

**Marcador:** BLOCO 3 · 3.2.1.2.1  
**Tempo:** 2 min

**Conteúdo visível:**

- ESTOQUE DA DPF · DEZ/2025
- R$ 8,6 trilhões
- dentro da faixa do PAF 2025 (R$ 8,5 a 8,8 tri). Custo médio perto de 12% a.a.
- COMPOSIÇÃO POR INDEXADOR
- 48% · 26% · 22%
- flutuante (Selic), índice de preços e prefixado; 4% câmbio. Juro alto puxa para a Selic
- TESOURO DIRETO
- R$ 213 bilhões
- 3,4 milhões de investidores ativos; Tesouro Selic é 37% do programa
- RISCO DE MERCADO
- Marcação a mercado nos prefixados e IPCA+. Quanto mais longo, maior.
- RISCO DE REINVESTIMENTO
- Cupons e vencimentos reaplicados a taxas menores quando o juro cai.
- RISCO SOBERANO
- Menor risco de crédito do país em moeda local: referência para todos os outros emissores.
- NA PROVA
- A trajetória da dívida afeta o prêmio exigido nos prefixados longos. "Título público não tem risco" é falso: não tem risco de crédito relevante, mas tem risco de mercado.

**Recurso visual:** Três cards de números (estoque, composição em azul, Tesouro Direto) e três cards de risco (mercado, reinvestimento, soberano). Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.2.1): volumes de emissão, trajetória da dívida e riscos. Fonte dos números: Tesouro Nacional, Relatório Mensal da Dívida de dezembro de 2025 (divulgação em janeiro de 2026): estoque da Dívida Pública Federal de R$ 8,635 trilhões; composição: flutuantes 48,3%, índice de preços 25,9%, prefixados 22,0%, câmbio 3,8%; Selic média de 14,33% em 2025 e custo médio próximo de 12%. Tesouro Direto: estoque de R$ 213,2 bilhões e 3,436 milhões de investidores ativos; Tesouro Selic com 37,2% do programa. Atualize os números antes de cada turma; o raciocínio não muda.
>
> POR QUE IMPORTA PARA O RELACIONAMENTO: (1) juro alto aumenta a parcela flutuante da dívida, porque o Tesouro evita travar prefixado caro; (2) quanto maior e mais incerta a trajetória da dívida, maior o prêmio que o mercado exige nos prefixados longos (inclinação da curva); (3) o Tesouro é a referência de crédito: todo CDB, debênture e CRI é precificado como 'Tesouro + spread'.
>
> RISCOS: mercado (MaM), reinvestimento (cupons) e soberano (teoricamente o menor do país em reais; não é zero, mas é a referência). Risco de liquidez no Tesouro Direto é baixo pela recompra diária.
>
> NA PROVA: enunciado com 'título público livre de risco'. Marque mentalmente: livre de risco de crédito relevante; não livre de risco de mercado.

## Slide 15 · Prefixado 2029: quem comprou a R$ 772 perdeu?

**Marcador:** EXEMPLO RESOLVIDO · 3.2.1.2  
**Tempo:** 2,5 min

**Conteúdo visível:**

- SITUAÇÃO  Tesouro Prefixado 2029, 3 anos, valor de face R$ 1.000, sem cupom. Na emissão, a taxa era 9% a.a. Depois de um ciclo de alta, os prefixados novos pagam 12% a.a. Dois clientes: um comprou na emissão; o outro quer comprar agora.
- Preço a 9%
- 1.000 ÷ 1,09³
- = R$ 772,18 (primário)
- Preço a 12%
- 1.000 ÷ 1,12³
- = R$ 711,78: queda de 7,8% (marcação a mercado)
- Quem já tinha
- Só perde se vender agora. Levando até 2029, recebe R$ 1.000: os 9% a.a. contratados
- Quem compra agora
- Paga R$ 711,78 e recebe R$ 1.000: trava 12% a.a. O deságio é a taxa nova
- RESPOSTA
- Comprar com deságio no secundário rende mais que a taxa da emissão. Quem já tinha o papel só perde se vender antes do vencimento. A perda no extrato é marcação, não resultado.

**Recurso visual:** Card SITUAÇÃO + fluxo de quatro passos com as contas em dourado (1.000 ÷ 1,09³; 1.000 ÷ 1,12³). Barra RESPOSTA.

**Notas do professor:**

> EXEMPLO RESOLVIDO: versão com contas fechadas da Questão 13 do caderno oficial (PD 3.2.1.4, dificuldade difícil), que trata de prefixado comprado no primário a R$ 1.000 e negociado no secundário a R$ 850 após alta de juros. Aqui usamos 3 anos sem cupom para a conta fechar na HP12C.
>
> HP12C: f REG · 1000 CHS FV · 3 n · 9 i · PV → 772,18. Depois 12 i · PV → 711,78. Variação: 711,78 ENTER 772,18 ÷ 1 − → −7,82%. Conferindo a taxa de quem compra agora: 711,78 CHS PV · 1000 FV · 3 n · i → 12,00.
>
> CONDUÇÃO: pergunte antes de revelar os cartões 3 e 4: 'o cliente que comprou a R$ 772 perdeu dinheiro?'. A resposta 'depende de vender ou não' é o aprendizado do bloco.
>
> — — —
>
> QUESTÃO 3 (autoral · 3.2.1.2 · dificuldade difícil · nível: análise)
> Um cliente comprou Tesouro Prefixado 2029 (3 anos, sem cupom, valor de face R$ 1.000) a R$ 772,18, quando a taxa era 9% a.a. As taxas subiram para 12% a.a. e o título está marcado a R$ 711,78. O profissional deve explicar que o cliente:
> A) perdeu 7,8% e deve vender para interromper a perda antes que as taxas subam mais.
> B) só realiza a perda se vender antes de 2029; levando ao vencimento, recebe R$ 1.000 e obtém os 9% a.a. contratados.
> C) passará a render 12% a.a. até o vencimento, porque a taxa de mercado subiu.
> D) não é afetado, porque títulos públicos não sofrem marcação a mercado.
>
> GABARITO: B. Título prefixado levado ao vencimento paga a taxa contratada na compra; a queda de preço é marcação a mercado, que só vira resultado na venda (3.2.1.1.3 e 3.2.1.1.5).
> A) transforma marcação em prejuízo realizado e ainda embute market timing (vender porque 'pode subir mais').
> C) a taxa de 12% é de quem compra agora a R$ 711,78; quem comprou a R$ 772,18 tem 9% a.a. travados.
> D) títulos públicos têm mercado secundário e são marcados a mercado; o que não têm é risco de crédito relevante.
> Conceito-chave: a taxa é definida pelo preço de compra. Pegadinha: confundir a taxa de mercado atual com a taxa contratada.

## Slide 16 · Treze papéis, três perguntas: emissor, FGC e IR

**Marcador:** BLOCO 4 · 3.2.1.3.1  
**Tempo:** 3 min

**Conteúdo visível:**

- Tabela:
    Papel | Quem emite e lastro | FGC | IR pessoa física
    CDB · RDB | Bancos; depósito a prazo. RDB é intransferível | Sim | Tabela regressiva
    LC · LH | LC: financeiras. LH: bancos, lastro imobiliário | Sim | LC tributada; LH isenta
    LCI · LCA · LCD | Bancos; lastro imobiliário, agro e desenvolvimento | Sim | Isentas
    LF | Bancos; mínimo R$ 50 mil, prazo ≥ 24 meses, sem resgate antecipado | Não | Tributada
    DPGE | Bancos; depósito a prazo com garantia especial | Especial: até R$ 40 milhões | Tributado
    CRI · CRA · CDCA · CCI | Securitizadoras e empresas do agro: não são bancos. CCI é o lastro | Não | Isentos
    RDC | Cooperativas de crédito | FGCoop, não FGC | Tributado

- NA PROVA
- Isento não é garantido: CRI e CRA são isentos e não têm FGC; CDB tem FGC e paga IR. LF não tem FGC nem resgate antecipado. Banco não emite debênture: emite LF.

**Recurso visual:** Tabela 7 × 4 (papel, emissor e lastro, FGC, IR); linha CRI/CRA/CDCA/CCI destacada. Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.3.1): os papéis que o programa lista: CDB, RDB, RDC, LCA, LCI, LCD, LF, LC, LH, CRA, CRI, CCI, CDCA e DPGE. Organize pelas três perguntas da prova: quem emite (e com que lastro), tem FGC, paga IR.
>
> DETALHES QUE CAEM:
> - CDB: transferível (pode ser negociado); RDB: intransferível e inegociável (resgate só no emissor). Ambos com FGC e IR.
> - LCI e LCA: lastro imobiliário e do agronegócio; isentas de IR para PF (Lei 11.033/2004, art. 3º); FGC; prazo mínimo hoje de 6 meses sem índice de preços e 36 meses com índice de preços (Res. CMN 5.215/2025, vigente desde 1º/8/2025). A MP 1.303/2025, que previa 5% de IR, caducou em outubro de 2025: isenção mantida.
> - LCD: Letra de Crédito do Desenvolvimento (Lei 14.937/2024), emitida por bancos de desenvolvimento (BNDES e congêneres); isenta para PF; FGC.
> - LH: emitida por instituições com crédito imobiliário; isenta para PF; FGC.
> - LF: Letra Financeira: captação longa dos bancos; valor mínimo R$ 50 mil (R$ 300 mil se subordinada); prazo mínimo 24 meses; sem resgate antecipado; sem FGC; IR.
> - LC: Letra de Câmbio, emitida por financeiras (sociedades de crédito, financiamento e investimento); FGC; IR.
> - DPGE: depósito a prazo com garantia especial do FGC até R$ 40 milhões por CPF/CNPJ e conglomerado; prazo de 6 a 36 meses; sem resgate antecipado.
> - CRI e CRA: emitidos por companhias securitizadoras (não são bancos, embora o programa os liste aqui); isentos para PF; sem FGC. CDCA: emitido por cooperativas e empresas do agro; isento; sem FGC. CCI: cédula que representa o crédito imobiliário; serve de lastro ao CRI.
> - RDC: Recibo de Depósito Cooperativo: cooperativas de crédito; coberto pelo FGCoop (fundo próprio do cooperativismo, limite também de R$ 250 mil), não pelo FGC.
>
> NA PROVA: a confusão mais lucrativa para a banca é 'isento = seguro'. Separe as duas colunas da tabela.

## Slide 17 · FGC: R$ 250 mil por conglomerado, R$ 1 milhão em 4 anos

**Marcador:** BLOCO 4 · 3.2.1.3.2  
**Tempo:** 3 min

**Conteúdo visível:**

- POR CPF OU CNPJ
- R$ 250 mil
- por instituição ou conglomerado; soma principal e juros
- TETO GLOBAL
- R$ 1 milhão
- a cada período de 4 anos, contado do primeiro pagamento de garantia
- DPGE
- R$ 40 milhões
- garantia especial: prazo de 6 a 36 meses, sem resgate antecipado
- COBERTOS
- Conta corrente e poupança; CDB, RDB, LC, LH, LCI, LCA, LCD; operações compromissadas com título de empresa ligada. Conta conjunta: R$ 250 mil divididos entre os titulares.
- FORA DA GARANTIA
- Tesouro, debêntures, CRI, CRA, CDCA, LF, LIG, fundos, previdência, depósitos judiciais, recursos captados no exterior e créditos de instituições financeiras e fundos.
- NA PROVA
- Dois bancos do mesmo conglomerado = um limite. Fato gerador: decretação de intervenção ou liquidação pelo BC. Sobre o rendimento pago incide IR. Já recebeu R$ 1 milhão? Só volta a ter cobertura após 4 anos.

**Recurso visual:** Três cards de números (R$ 250 mil em azul, R$ 1 milhão, R$ 40 milhões) e dois cards: cobertos × fora da garantia. Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.3.2): Fundo Garantidor de Créditos, entidade privada mantida pelas instituições associadas (associação obrigatória), regida pelo Regulamento anexo à Resolução CMN 4.222/2013 (com alterações). Garantia ordinária: até R$ 250 mil por CPF ou CNPJ, por instituição ou conglomerado financeiro, somando principal e rendimentos. Teto global de R$ 1 milhão a cada 4 anos, contado a partir do primeiro pagamento de garantia. DPGE: garantia especial até R$ 40 milhões.
>
> COBERTOS: depósitos à vista, poupança, depósitos a prazo (CDB, RDB), letras de câmbio, hipotecárias, LCI, LCA, LCD, operações compromissadas com títulos de empresa ligada (emitidos após 8/3/2012). Não cobertos: fundos, previdência, Tesouro, debêntures, CRI, CRA, CDCA, LF, LIG, depósitos judiciais, recursos no exterior, créditos de instituições financeiras e de fundos.
>
> MECÂNICA: o fato gerador é a decretação de intervenção ou liquidação extrajudicial pelo Banco Central. O saldo na data (principal + juros) é limitado a R$ 250 mil; sobre o rendimento pago há retenção de IR pela tabela regressiva (e IOF se menos de 30 dias). Conta conjunta: o limite de R$ 250 mil é dividido em partes iguais entre os titulares. Instituições do mesmo conglomerado compartilham um único limite.
>
> ATUALIZAÇÃO 2025/2026: após as liquidações do Banco Master e do Will Bank, o CMN endureceu regras prudenciais para os bancos (Res. CMN 5.238/2025 e normas de 2026: contribuição adicional maior e ativo de referência em títulos públicos). Os limites para o investidor NÃO mudaram. Fonte: FGC, material para corretoras, dez/2025. Confirme antes da aula se houver nova resolução.
>
> NA PROVA: o caderno oficial traz investidor que já recebeu R$ 500 mil do FGC em duas liquidações: o limite remanescente nos 4 anos é R$ 500 mil, e a orientação é reduzir a exposição coberta a esse valor e realocar o excedente em soberano ou grau de investimento.

## Slide 18 · Ficha técnica: cinco campos antes de assinar

**Marcador:** BLOCO 4 · 3.2.1.3.3  
**Tempo:** 2 min

**Conteúdo visível:**

- Custódia
- Onde o papel fica registrado: B3 para bancários e privados; Selic para títulos públicos. Prova que o título existe e é seu. Não é garantia de crédito.
- Remuneração
- Pré, pós (% do CDI, CDI +) ou híbrida (IPCA +). "110% do CDI" é só a regra, não um selo de segurança.
- Prazo e carência
- Vencimento é quando acaba; carência é a partir de quando pode resgatar. Antes da carência, nem com perda.
- Liquidez
- Diária, após a carência ou só no vencimento. "Liquidez diária" com deságio não é liquidez plena (prazo e preço).
- Risco e rating
- Nota do emissor. Grau de investimento: BBB− (ou Baa3) ou melhor. BB+ para baixo é especulativo: taxa maior é prêmio por risco.
- NA FALA DO CLIENTE
- "Esse CDB paga 130% do CDI, é melhor que o Tesouro." Pergunte: de que banco, com que rating, com que carência e liquidez; e quanto desse valor o FGC cobre.
- NA PROVA
- Rating BB+ é grau especulativo (risco elevado), mesmo em "banco médio". Remuneração IPCA + taxa é híbrida. Custódia na B3 confirma registro, não solvência.

**Recurso visual:** Grade 3 × 2 com os cinco campos da ficha técnica e um sexto card azul "Na fala do cliente". Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.3.3): custódia, tipos de remuneração, prazos e carências, liquidez, riscos e rating. É a leitura da ficha técnica de qualquer emissão bancária. O caderno oficial (Questão 15) descreve um CDB 'IPCA + 5,2% a.a., 5 anos, carência de 180 dias, liquidez só no vencimento, rating BB+, custódia B3' e pede a validação: remuneração híbrida, liquidez restrita, risco de crédito elevado, registro em sistema de custódia privada operado pela B3. Os distratores dizem 'prefixada', 'custódia no Selic' e 'BB+ é baixo risco'.
>
> RATING: escala de longo prazo das agências: AAA, AA, A, BBB (grau de investimento) e BB, B, CCC e abaixo (grau especulativo). Fronteira: BBB− (S&P, Fitch) ou Baa3 (Moody's). Rating nacional (brAAA) compara emissores dentro do Brasil.
>
> LIQUIDEZ E CARÊNCIA: 'liquidez diária após 90 dias' significa carência de 90 dias e depois resgate antecipado, geralmente com remuneração menor ou deságio. Retome a Aula 3: liquidez é prazo E preço.
>
> PARE E PERGUNTE: 'Quanto maior a taxa, melhor o produto?'. Não: a taxa remunera risco de crédito, prazo e falta de liquidez. Taxa alta é um sintoma a investigar.
>
> NA PROVA: enunciado com ficha técnica e pedido de 'validar'. Marque cada campo: pré/pós/híbrido, carência × prazo, custódia B3 × Selic, rating e o que ele significa.

## Slide 19 · Seu Antônio: R$ 600 mil em CDBs de um banco só

**Marcador:** EXEMPLO RESOLVIDO · 3.2.1.3  
**Tempo:** 3 min

**Conteúdo visível:**

- SITUAÇÃO  Aposentado, conservador. R$ 600 mil em CDBs a 125% do CDI do Banco Beta (rating BB), vencendo em 2 anos, em conta conjunta com a esposa. Diz: "tem FGC, está tudo garantido". Nunca recebeu pagamento do FGC.
- Coberto
- R$ 250 mil
- por conglomerado, dividido entre os dois. Fora: R$ 350 mil
- Por que 125%
- Rating BB: grau especulativo. A taxa remunera o risco do banco, não a fidelidade do cliente
- Redistribuir
- Até R$ 250 mil por conglomerado, em bancos de grupos diferentes; excedente em Tesouro Selic e IPCA+
- Como fazer
- Acompanhar os vencimentos: resgatar antes pode custar deságio ou nem ser possível. Sem venda forçada
- RESPOSTA
- Garantido é até R$ 250 mil por conglomerado; o teto de R$ 1 milhão em 4 anos é do investidor, não do banco. O excedente vai para soberano ou grau de investimento, no ritmo dos vencimentos.

**Recurso visual:** Card SITUAÇÃO + fluxo de quatro passos (R$ 250 mil em dourado no passo 1); passo 4 em azul. Barra RESPOSTA.

**Notas do professor:**

> EXEMPLO RESOLVIDO: aplica o slide anterior. Conta conjunta: o FGC garante R$ 250 mil divididos em partes iguais entre os titulares (R$ 125 mil para cada um), não R$ 250 mil por titular. Mesmo que fossem contas separadas, o limite é por CPF e por conglomerado: R$ 250 mil cada, R$ 500 mil no total, ainda abaixo dos R$ 600 mil.
>
> CONDUÇÃO: pergunte antes do cartão 1: 'quanto está garantido?'. Muitos dirão R$ 500 mil (dois titulares). Corrija com a regra da conta conjunta.
>
> POR QUE NÃO VENDER TUDO HOJE: o CDB pode não ter liquidez antes do vencimento ou ter deságio. A orientação adequada é escalonar: a cada vencimento, realocar. O caderno oficial (Questão 14) usa a mesma lógica: 'acompanhar os vencimentos a fim de evitar perdas nos resgates e, gradativamente, reduzir a exposição'.
>
> PERFIL: conservador e aposentado (fase de usufruto, Aula 3). Concentração em banco BB contradiz o perfil, mesmo com FGC. Para o excedente: Tesouro Selic (liquidez e renda) e IPCA+ de prazo curto a médio (renda real).
>
> — — —
>
> QUESTÃO 4 (autoral · 3.2.1.3.2 · dificuldade média · nível: aplicação)
> Um cliente mantém R$ 300 mil em CDB do Banco X, R$ 200 mil em LCI do Banco Y, que integra o mesmo conglomerado financeiro do Banco X, e R$ 150 mil em Letra Financeira do Banco Z. Se X e Y sofrerem liquidação extrajudicial decretada pelo Banco Central, o FGC pagará a esse cliente:
> A) R$ 500 mil, correspondentes a R$ 250 mil por instituição.
> B) R$ 250 mil no total, porque X e Y compartilham um único limite; a LF do Banco Z não teria cobertura em nenhuma hipótese.
> C) R$ 650 mil, porque LCI e LF são títulos isentos e garantidos.
> D) R$ 450 mil: R$ 250 mil do CDB e R$ 200 mil da LCI.
>
> GABARITO: B. Instituições do mesmo conglomerado compartilham o limite de R$ 250 mil por CPF; CDB e LCI são cobertos, mas somados; a LF não é coberta pelo FGC.
> A) trata cada banco como limite separado; no mesmo conglomerado o limite é um só.
> C) confunde isenção de IR com garantia; LF é tributada e não tem FGC.
> D) soma CDB e LCI como se fossem limites independentes.
> Conceito-chave: limite por CPF e por conglomerado. Pegadinha: 'bancos diferentes' do mesmo grupo.

## Slide 20 · Debênture: a empresa toma emprestado do mercado

**Marcador:** BLOCO 5 · 3.2.1.4.1 A 3.2.1.4.3  
**Tempo:** 2,5 min

**Conteúdo visível:**

- O QUE É
- Título de dívida de sociedade anônima não financeira. Sem FGC. Remuneração pré, CDI +, % do CDI ou IPCA +, com ou sem cupom. Prazos de 3 a 15 anos ou mais.
- O QUE DEFINE O RISCO
- Prazo e cupom (duration e marcação a mercado); crédito do emissor (rating, garantias, covenants); liquidez (poucos negócios no secundário: deságio para sair).
- Oferta pública (Res. CVM 160/2022)
- Rito automático ou ordinário; público-alvo: geral, qualificados ou profissionais; prospecto ou lâmina; reserva, bookbuilding define a taxa; rateio se a demanda supera a oferta.
- Variações
- Simples, conversível em ações ou permutável. Incentivada (Lei 12.431: infraestrutura, isenta para PF). De infraestrutura (Lei 14.801/2024: benefício fiscal no emissor; PF paga IR).
- NA PROVA
- Banco não emite debênture (emite LF); por isso debênture nunca tem FGC. Prazo longo com cupom baixo é duration alta: marcação a mercado forte. "Incentivada" e "de infraestrutura" não são a mesma coisa.

**Recurso visual:** Card "O que é / O que define o risco" à esquerda; dois cards à direita: oferta pública (Res. CVM 160) e variações (em azul). Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.4.1 e 3.2.1.4.3): debênture é o título de dívida de médio e longo prazo emitido por sociedades anônimas (Lei 6.404/1976). Instituições financeiras não podem emitir debêntures (exceção: sociedades de arrendamento mercantil); bancos captam por LF. Não há FGC. Características: prazo, remuneração (pré, CDI +, % do CDI, IPCA +), cupom (periodicidade de juros), amortizações, garantias (próximo slide), repactuação. Risco de crédito, marcação a mercado e duration seguem a lógica do Bloco 2, com um agravante: liquidez menor no secundário, o que abre o spread em momentos de estresse.
>
> OFERTA PÚBLICA (3.2.1.4.2): Resolução CVM 160/2022 unificou o regime. Rito de registro automático (sem análise prévia) ou ordinário (com análise da CVM), conforme o emissor e o público-alvo. Público-alvo define quem pode comprar: investidores em geral, qualificados ou profissionais. Documentos: prospecto e lâmina (quando exigidos). Processo: período de reserva, bookbuilding (a taxa final sai da demanda), alocação com rateio se houver excesso de demanda; depois, negociação no secundário.
>
> VARIAÇÕES: simples (só dívida), conversível (pode virar ação da emissora), permutável (troca por ação de outra empresa). Debênture incentivada (Lei 12.431/2011, art. 2º): projetos de infraestrutura prioritários; rendimento isento de IR para pessoa física. Debênture de infraestrutura (Lei 14.801/2024): o benefício fiscal é do emissor (dedução), e o investidor PF paga IR normalmente. A banca pode cobrar a diferença.
>
> NA PROVA: 'debênture de banco com FGC' é distrator duplo: banco não emite e debênture não tem FGC.

## Slide 21 · Garantias definem a fila; covenants, o gatilho

**Marcador:** BLOCO 5 · 3.2.1.4.7 E 3.2.1.4.8  
**Tempo:** 2,5 min

**Conteúdo visível:**

- Lei 6.404/76, art. 58: a espécie da debênture define a fila numa recuperação ou falência. Fidejussória (fiança ou aval de terceiro, como a controladora) é garantia pessoal que se soma a qualquer espécie.
- Real
- Bem específico vinculado (imóvel, máquina, recebível). Recebe primeiro, com o produto do bem
- Flutuante
- Privilégio geral sobre o ativo da empresa, sem bem fixo: ela pode vender e substituir bens
- Quirografária
- Sem garantia. Concorre em igualdade com os demais credores comuns
- Subordinada
- Recebe depois de todos os outros credores; só tem preferência sobre os acionistas
- COVENANTS  Compromissos do emissor na escritura: financeiros (ex.: dívida líquida ÷ EBITDA ≤ 3×) e não financeiros (limite a dividendos, manter rating). Quebrou, vence antecipado, salvo perdão (waiver) da assembleia de debenturistas.
- NA PROVA
- Ordem na fila: real, flutuante, quirografária, subordinada. Covenant quebrado não dá garantia nova: dá o direito de cobrar antes. Flutuante não impede a empresa de vender ativos.

**Recurso visual:** Linha de contexto (Lei 6.404, art. 58) + fila de quatro cards (real → flutuante → quirografária → subordinada) com chevrons; card COVENANTS com borda dourada. Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.4.7): espécies de debênture pela garantia (Lei 6.404/1976, art. 58): com garantia real (bem específico gravado, como hipoteca ou alienação fiduciária), com garantia flutuante (privilégio geral sobre o ativo da companhia, que continua livre para dispor dos bens), quirografária (sem preferência: credor comum) e subordinada (prefere apenas aos acionistas). Garantia fidejussória é a pessoal, por fiança ou aval de terceiro (normalmente a controladora ou os sócios); não é espécie de debênture, é reforço que pode acompanhar qualquer espécie.
>
> ANALOGIA: fila do caixa na falência. Real tem senha preferencial com o bem reservado; flutuante entra na frente dos comuns, mas sem bem reservado; quirografária é a fila comum; subordinada entra depois de todos, antes só dos donos. Onde quebra: na falência real, há créditos trabalhistas e tributários antes de todos esses.
>
> EXPLICAÇÃO (3.2.1.4.8): covenants são cláusulas da escritura que impõem obrigações ao emissor para proteger o credor. Financeiros: índices (alavancagem, cobertura de juros). Não financeiros: restrições a dividendos, venda de ativos, mudança de controle, manutenção de rating. O descumprimento é evento de vencimento antecipado (o agente fiduciário convoca assembleia); os debenturistas podem conceder waiver, muitas vezes em troca de taxa maior ou garantia adicional.
>
> NA PROVA: 'covenant quebrado transforma a debênture em garantia real' é falso. 'Garantia flutuante impede a venda de ativos' é falso. 'Subordinada recebe antes dos acionistas' é verdadeiro.
>
> — — —
>
> QUESTÃO 6 (autoral · 3.2.1.4.7 e 3.2.1.4.8 · dificuldade difícil · nível: análise)
> Uma debênture com garantia flutuante tem covenant financeiro de dívida líquida ÷ EBITDA de no máximo 3,0×. A emissora fecha o ano em 3,4×. O profissional deve explicar ao cliente que:
> A) os debenturistas passam a ter garantia real sobre os imóveis da emissora.
> B) o descumprimento pode levar ao vencimento antecipado, salvo se a assembleia de debenturistas aprovar o perdão (waiver).
> C) o FGC cobrirá os debenturistas até R$ 250 mil.
> D) a garantia flutuante impede a emissora de vender qualquer ativo até regularizar o índice.
>
> GABARITO: B. Quebra de covenant é evento de vencimento antecipado, sujeito a deliberação dos debenturistas, que podem conceder waiver.
> A) a espécie da garantia não muda por quebra de covenant; real exige bem gravado na escritura.
> C) debênture não tem FGC.
> D) garantia flutuante não vincula bens específicos; a empresa pode dispor dos ativos.
> Conceito-chave: covenant protege por antecipação, não por garantia. Pegadinha: misturar garantia (fila) com covenant (gatilho).

## Slide 22 · Isento ou tributado: compare pelo líquido

**Marcador:** BLOCO 5 · 3.2.1.4.4 E 3.2.1.4.5  
**Tempo:** 3 min

**Conteúdo visível:**

- TABELA REGRESSIVA DO IR (SOBRE O RENDIMENTO)
- Tabela:
    Prazo da aplicação | Alíquota
    Até 180 dias | 22,5%
    181 a 360 dias | 20%
    361 a 720 dias | 17,5%
    Acima de 720 dias | 15%

- QUEM PAGA E QUEM NÃO PAGA (PESSOA FÍSICA)
- Isentos: LCI, LCA, LCD, LH, CRI, CRA, CDCA, debêntures incentivadas (Lei 12.431), poupança. Tributados: Tesouro, CDB, RDB, LC, LF, debêntures comuns e de infraestrutura. IOF regressivo até o 29º dia.
- A CONTA
- Líquido do tributado = taxa × (1 − IR).  CDB 110% do CDI, 2 anos: 110% × 0,85 = 93,5% do CDI líquido.  Equivalente bruto do isento = taxa ÷ (1 − IR): LCA 95% do CDI ÷ 0,85 = 111,8%. A LCA ganha.
- NA PROVA
- Prazo curto piora o tributado (22,5%) e valoriza o isento. MP 1.303/2025 (5% sobre LCI e LCA) caducou: isenção mantida. No híbrido, o IR incide sobre o ganho nominal, inflação incluída.

**Recurso visual:** Card com tabela regressiva do IR; card "quem paga e quem não paga"; card "A conta" com o exemplo 110% × 0,85 em dourado. Barra NA PROVA.

**Notas do professor:**

> EXPLICAÇÃO (3.2.1.4.4): renda fixa tributada segue a tabela regressiva do IR sobre o rendimento: 22,5% até 180 dias, 20% de 181 a 360, 17,5% de 361 a 720 e 15% acima de 720 dias (Lei 11.033/2004). IOF regressivo sobre o rendimento nos primeiros 29 dias (zera no 30º). Retenção na fonte pela instituição. Isentos para pessoa física (Lei 11.033, art. 3º, e Lei 12.431, art. 2º): LCI, LCA, LH, CRI, CRA, CDCA, debêntures incentivadas; LCD pela Lei 14.937/2024; poupança. Pessoa jurídica paga IR nesses papéis.
>
> EXPLICAÇÃO (3.2.1.4.5): rentabilidade líquida. Tributado: multiplique por (1 − alíquota). Para comparar com isento, ou leva o tributado ao líquido, ou leva o isento ao bruto equivalente dividindo por (1 − alíquota). HP12C: 110 ENTER 0,85 × → 93,5. 95 ENTER 0,85 ÷ → 111,76.
>
> PEGADINHA DO HÍBRIDO: no Tesouro IPCA+ e no CDB IPCA+, o IR incide sobre o rendimento nominal total (IPCA + taxa real). Com IPCA de 4% e taxa real de 6%, o ganho nominal é cerca de 10,24% e o IR de 15% leva 1,54 p.p.; a taxa real líquida fica em torno de 4,5%, não 5,1% (6% × 0,85). A isenção da incentivada vale sobre o total: por isso a diferença líquida entre uma incentivada IPCA + 7% e um Tesouro IPCA+ 6% é maior do que 1 p.p.
>
> ATUALIZAÇÃO: a MP 1.303/2025 previa alíquota de 5% sobre LCI, LCA, CRI, CRA e incentivadas emitidas a partir de 2026 e caducou em 8/10/2025 sem conversão em lei. Isenção mantida. Avise a turma: se houver nova lei, a regra muda; a lógica da comparação, não.
>
> NA PROVA: 'LCA de 95% rende menos que CDB de 110%' é o distrator clássico. Converta sempre.

## Slide 23 · Marina quer a debênture "que paga mais". Recomenda?

**Marcador:** EXEMPLO RESOLVIDO · 3.2.1.4  
**Tempo:** 3 min

**Conteúdo visível:**

- SITUAÇÃO  Longo prazo (faculdade em 15 anos). Marina compara: debênture incentivada IPCA + 7,5% (rating A, 12 anos, quirografária, pouco negociada) e Tesouro IPCA+ 2040 a IPCA + 6,5%. Reserva completa, perfil moderado.
- Líquido
- 7,5% × 6,5%
- Isenta: 7,5% real. Tesouro com IR: perto de 5% real
- Crédito
- Rating A: grau de investimento. Sem FGC. Quirografária: fila comum. O 1 p.p. a mais é prêmio por risco e iliquidez
- Liquidez e prazo
- Pouco negociada: sair antes custa deságio. Mas 12 anos cabem no objetivo de 15: não precisa sair
- Decisão
- Entra como PARTE da subclasse de crédito privado (ex.: até 20% da renda fixa), com outros emissores. Nunca o todo
- RESPOSTA
- Sim, com dose. O líquido maior compensa, o objetivo é longo e o perfil aceita. O que impediria: prazo do objetivo curto, reserva incompleta ou concentração em um emissor.

**Recurso visual:** Card SITUAÇÃO + fluxo de quatro passos (líquido, crédito, liquidez e prazo, decisão em azul). Barra RESPOSTA.

**Notas do professor:**

> EXEMPLO RESOLVIDO: fecha a pergunta de abertura. 'Paga mais' precisa virar: líquido de quanto, com que risco, com que liquidez e para qual objetivo.
>
> CONTAS: incentivada isenta: IPCA + 7,5% líquido. Tesouro IPCA+ 6,5% com IR de 15% sobre o ganho nominal: com IPCA de 4%, nominal = 1,04 × 1,065 − 1 = 10,76%; IR = 1,61 p.p.; líquido nominal 9,15%; real líquido = 1,0915 ÷ 1,04 − 1 = 4,95%. A diferença líquida é de cerca de 2,5 p.p. ao ano, não 1 p.p. HP12C: 1,04 ENTER 1,065 × 1 − → 0,1076; 0,85 × → 0,0915; 1 + 1,04 ÷ 1 − → 0,0495.
>
> RISCO DE CRÉDITO E LIQUIDEZ NA RECOMENDAÇÃO (3.2.1.4.6): o prêmio compensa quando (1) o objetivo é longo o bastante para não precisar vender, (2) a posição é diluída entre emissores, (3) o rating é grau de investimento e acompanhado, (4) a reserva está completa (não será a fonte de emergência). Convenção desta aula: crédito privado até 20% da renda fixa, com no máximo 5% por emissor.
>
> PARE E PERGUNTE: 'E se fosse para o carro em 3 anos?'. Não: prazo de 12 anos não casa; vender antes exigiria deságio.
>
> RESPOSTA À MARINA (slide 2): o CDB de 110% do CDI entra na parte pós-fixada; a incentivada, na parte de crédito privado de longo prazo; o Tesouro IPCA+, no núcleo. 'Tudo em um produto' nunca é a resposta.
>
> — — —
>
> QUESTÃO 5 (autoral · 3.2.1.4.5 · dificuldade fácil · nível: aplicação)
> Cliente pessoa física, horizonte de 2 anos, compara um CDB a 110% do CDI (IR de 15% no prazo) e uma LCA a 95% do CDI, do mesmo banco, ambos sem liquidez antes do vencimento. Qual rende mais, líquido de IR?
> A) O CDB, porque 110% é maior que 95%.
> B) A LCA, porque 110% × 0,85 = 93,5% do CDI, menor que os 95% isentos.
> C) Empatam, porque o FGC iguala os dois produtos.
> D) O CDB, porque a LCA também paga 15% de IR.
>
> GABARITO: B. Líquido do CDB = 110% × (1 − 0,15) = 93,5% do CDI; a LCA é isenta para PF e rende 95% do CDI.
> A) compara bruto com líquido.
> C) FGC é garantia de crédito; não altera rentabilidade.
> D) LCA é isenta de IR para pessoa física (Lei 11.033/2004).
> Conceito-chave: compare pelo líquido. Pegadinha: taxa 'de cara' maior.

## Slide 24 · Cinco ideias para levar: alocação e renda fixa

**Marcador:** REVISÃO  
**Tempo:** 1,5 min

**Conteúdo visível:**

- A alocação entre classes explica a maior parte do resultado. Produto é o terceiro passo, depois de perfil e pesos.
- Estratégica segue a vida; tática segue o mercado, dentro das bandas e do perfil. Rebalancear não é timing.
- Juro sobe, preço cai: oscila quem tem secundário e taxa travada. Duration mede o quanto; pós-fixado quase não oscila.
- FGC: R$ 250 mil por CPF e conglomerado, R$ 1 milhão em 4 anos, só emissões bancárias. Isento não é garantido.
- Debênture: a garantia define a fila (real, flutuante, quirografária, subordinada); o covenant, o gatilho. Compare pelo líquido.

**Recurso visual:** Lista numerada de cinco ideias (marcadores azuis, o último dourado).

**Notas do professor:**

> CONDUÇÃO: leia em voz alta e peça à turma que repita: (1) os três números do FGC (R$ 250 mil, R$ 1 milhão, 4 anos) e (2) a ordem da fila das garantias (real, flutuante, quirografária, subordinada).
>
> REPETIÇÃO-CHAVE (fixação): 'juro sobe, preço cai' e 'isento não é garantido'. Diga duas vezes.
>
> PONTE PARA A PRÓXIMA AULA: a renda variável (3.3) é o que entra nos 25% de ações da Marina: ações, IPO e OPA, dividendos e JCP, tributação e compensação de perdas, derivativos.

## Slide 25 · Verdadeiro ou falso?

**Marcador:** CHECAGEM RÁPIDA · 60 SEGUNDOS  
**Tempo:** 2,5 min

**Conteúdo visível:**

- Rebalancear a carteira depois de uma alta da bolsa é uma forma de market timing.
- Com a Selic em queda, o Tesouro Selic valoriza por marcação a mercado.
- CRI é isento de IR para pessoa física e, por isso, coberto pelo FGC.
- PRÓXIMA AULA
- Aula 5 · Renda variável (3.3) Ações, IPO e OPA, dividendos e JCP, tributação e compensação de perdas, derivativos.
- DICA
- Responda antes de ver o gabarito. Cada afirmação errada aponta o bloco da aula para revisar: 1 é o Bloco 1, 2 é o Bloco 2, 3 é o Bloco 4.

**Recurso visual:** Três cards de afirmação V/F numeradas à esquerda e card azul "Próxima aula" à direita. Barra DICA.

**Notas do professor:**

> GABARITO DA CHECAGEM:
> 01 · FALSO. Rebalancear é voltar ao peso-alvo por regra (banda ou data), não por expectativa de mercado (3.1.3). Se metade da turma errar, retome o slide 4.
> 02 · FALSO. O Tesouro Selic é pós-fixado diário, com duration próxima de zero: passa a render menos, mas não valoriza por marcação. Quem valoriza é o prefixado (3.2.1.1.3). Retome o slide 12.
> 03 · FALSO. CRI é isento para PF, mas é emitido por securitizadora e não tem FGC. Isento e garantido são colunas diferentes (3.2.1.3). Retome o slide 16.
>
> FECHAMENTO: volte à pergunta da Marina: 'posso pôr tudo no CDB de 110% do CDI?'. Resposta da turma em uma frase: 'uma parte, na subclasse pós-fixada, depois de definir a alocação'.
>
> CONDUÇÃO FINAL: anote os temas em que a turma hesitou e abra a próxima aula com uma pergunta de recuperação sobre eles (espaçamento).

---

# Fontes e normas usadas

- ANBIMA, *Programa Detalhado C-Pro R*, v1.2 (revisado em 04/06/2025, vigência 01/01/2026). Itens 3.1 e 3.2.1.
- ANBIMA, *Caderno de questões C-Pro R* (questões 12 a 16: marcação a mercado, primário × secundário, FGC, ficha técnica, duration).
- Brinson, Hood e Beebower, "Determinants of Portfolio Performance", *Financial Analysts Journal*, 1986 (93,6% da variabilidade explicada pela política de alocação).
- Resolução CVM 160/2022 (ofertas públicas: ritos, público-alvo, documentos).
- Lei 6.404/1976, art. 58 (espécies de debênture pela garantia).
- Lei 12.431/2011, art. 2º (debêntures incentivadas) e Lei 14.801/2024 (debêntures de infraestrutura).
- Lei 11.033/2004, art. 1º (tabela regressiva do IR) e art. 3º (isenções de PF: LCI, LCA, LH, CRI, CRA, CDCA).
- Lei 14.937/2024 (LCD). Resolução CMN 4.733/2019 (Letra Financeira). Resolução CMN 5.215/2025 (prazo mínimo de LCI e LCA: 6 meses sem índice de preços; 36 meses com índice).
- MP 1.303/2025: caducou em 08/10/2025 sem conversão em lei; isenções mantidas.
- FGC, *Regulamento* (Resolução CMN 4.222/2013 e alterações) e *Material para corretoras*, dez/2025: R$ 250 mil por CPF/CNPJ e conglomerado; R$ 1 milhão a cada 4 anos; DPGE até R$ 40 milhões; lista de produtos cobertos e não cobertos; conta conjunta; fato gerador; retenção de IR.
- Regras e Procedimentos ANBIMA de marcação a mercado na distribuição (vigência 02/01/2023: títulos públicos, debêntures, CRI e CRA).
- Tesouro Nacional, *Relatório Mensal da Dívida*, dezembro/2025 (DPF de R$ 8,635 trilhões; flutuantes 48,3%, índice de preços 25,9%, prefixados 22,0%, câmbio 3,8%; Tesouro Direto R$ 213,2 bilhões e 3,436 milhões de investidores ativos).

# Materiais não disponíveis nesta produção (sinalização)

- Apostila ANBIMA Edu do macrotema 3 e o material X8 correspondente (códigos A51xx usados nas Aulas 2 e 3): não estavam na sessão. Por isso as notas não trazem referência de página da apostila; se quiser, envie o PDF e eu insiro as páginas e alinho a terminologia.
- A "imagem em anexo" com os temas da Aula 4 não chegou junto com o PPTX; o escopo seguiu o texto do pedido (3.1 inteiro e 3.2.1.1 a 3.2.1.4).
