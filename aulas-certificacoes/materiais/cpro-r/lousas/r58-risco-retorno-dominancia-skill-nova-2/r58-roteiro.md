# R58 · skill nova · Risco de ativos, ativo livre de risco e dominância entre ativos (4.5 a 4.6) (2)

Apresentação das lousas (2), no Google Slides: https://docs.google.com/presentation/d/1L7tjOQlXVCNpGevvKNod4Web4EcDBlBPfBpuhOAXCFc/edit

## Plano da série

| Vídeo | Itens do PD | Minutagem (conferidor) | Mito da abertura |
|---|---|---|---|
| R58A | 4.5 (risco de ativos) | ~7,3 min | "Risco é a chance de perder dinheiro" |
| R58B | 4.5.1 (ativos livres de risco e ativos com risco de crédito) | ~7,2 min | "CDB com FGC é ativo livre de risco" |
| R58C | 4.6 (relação entre risco, retorno e dominância entre ativos) | ~7,2 min | "Com o mesmo retorno, tanto faz o ativo" |

Metáfora central da série (do rascunho do professor): as estradas. O ganho da viagem é o retorno; os buracos são o risco; o asfalto liso é o ativo livre de risco.

# R58A · Risco de ativos: o que é e de onde vem (7 min)

**Base:** PD C-PRO R v1.2, item 4.5 · Resolução CMN 4.557/2017 (definições de risco de crédito, de mercado, de liquidez e operacional, com o legal) · Ibovespa em 2020 (B3, dados mensais divulgados pela imprensa). **Escopo:** o conceito de risco, a medida (volatilidade) e as cinco fontes de risco de um ativo. O ativo livre de risco e o risco de crédito estão no R58B; a relação risco-retorno e a dominância, no R58C; o risco de uma carteira, na aula R59.

## 1. Abertura Instigante (Destruição de Mito) — [45 s]

**[Ação na Lousa - Google Slides]**
- Slide 1 · ao dizer "Afirmação falsa", circule o mito riscado · ao dizer "para cima ou para baixo", sublinhe os dois números de 2020

**[Locução Direta]**
"Em março de 2020, o Ibovespa caiu 29,9% num único mês. Em novembro do mesmo ano, subiu 15,9%. E fechou 2020 com alta de 2,92%. Afirmação falsa: risco é a chance de perder dinheiro. Parece verdade porque a perda é o que dói. A regra: risco é a incerteza, a chance de o retorno sair diferente do esperado, para cima ou para baixo. Neste vídeo, o que é risco, como se mede e de onde ele vem."

## 2. Metáfora Central de Fixação — [1 min]

**[Ação na Lousa - Google Slides]**
- Slide 2 · ao dizer "a chuva", circule MERCADO · ao dizer "Onde a analogia quebra", sublinhe a moldura

**[Locução Direta]**
"Para guardar, imagine uma estrada até o objetivo do cliente. O ganho da viagem é o retorno. Os buracos são o risco: eles fazem a chegada ser diferente do previsto. E cada buraco tem uma origem. A chuva que muda o asfalto é o risco de mercado. A ponte que pode cair é o risco de crédito. O trecho sem saída para desviar é o risco de liquidez. A falha do GPS é o risco operacional. E a placa que muda de regra no meio da viagem é o risco legal. Onde a analogia quebra: buraco só atrasa, e no mercado a incerteza também pode adiantar a chegada. O termo técnico para o tamanho dos buracos é volatilidade."

## 3. Conteúdo Técnico e Roteiro Visual — [4 min]

**[Ação na Lousa - Google Slides]**
- Slide 3 · ao dizer "Como se mede?", sublinhe a fórmula · ao dizer "Não confunda volatilidade com risco de crédito", circule a moldura de baixo

**[Locução Direta]**
"Em finanças, risco é a probabilidade de o retorno efetivo ser diferente do retorno esperado. A banca também chama de incerteza. Repare: a definição não fala em perda. Um ativo que você esperava render 10% e rendeu 25% também mostrou risco, porque o resultado fugiu do esperado.

Como se mede? O mais comum é a volatilidade, calculada pelo desvio padrão dos retornos. Quanto mais os retornos se espalham em volta da média, maior o risco. Por isso, dois ativos podem ter a mesma média e riscos muito diferentes.

E de onde vem o risco? São cinco fontes principais. O risco de mercado é a variação de preços, juros, inflação e câmbio: a ação que oscila, o prefixado que perde valor quando os juros sobem. O risco de crédito é a chance de o emissor não pagar: a empresa da debênture ou o banco do CDB. O risco de liquidez é não conseguir vender rápido sem aceitar um preço pior, como numa ação pouco negociada ou num imóvel. O risco operacional são falhas de processos, pessoas ou sistemas. E o risco legal ou regulatório é a mudança de leis e normas. Um exemplo recente: em 2025, uma medida provisória propôs tributar as LCI e LCA novas. Ela perdeu a validade em outubro, mas mostrou que a regra do jogo pode mudar.

Não confunda volatilidade com risco de crédito. Um CDB quase não oscila e, mesmo assim, tem risco de crédito. A volatilidade baixa não mostra a chance de o banco quebrar: esse risco só aparece quando o problema acontece.

E daí, para o profissional? Antes de recomendar, você responde duas perguntas. O retorno esperado compensa a incerteza? E o cliente aguenta ver a oscilação sem vender no pior momento? A segunda pergunta é o perfil de risco.

*Pergunta-gatilho:* um investimento que rendeu muito acima do esperado não teve risco, já que o cliente ganhou? **Não.** Risco é a diferença entre o efetivo e o esperado, para cima ou para baixo; um ganho inesperado também é sinal de incerteza."

## 4. Resolução Rápida de Fixação — [1,3 min]

**[Ação na Lousa - Google Slides]**
- Slide 4 · ao dizer "a mesma média", circule as duas médias · ao dizer "cinco vezes", circule o resultado do ativo B · ao dizer "pause", aponte a pergunta do rodapé e espere 3 segundos

| Passo | Teclas na HP12C | Visor | O que significa |
|---|---|---|---|
| 1 | f REG f 2 | 0,00 | Memórias zeradas, 2 casas decimais |
| 2 | 8 Σ+ 10 Σ+ 12 Σ+ | 3,00 | Três anos do ativo A lançados |
| 3 | g x̄ | 10,00 | Retorno médio de A: 10% ao ano |
| 4 | g s | 2,00 | Desvio padrão de A: 2 pontos percentuais |
| 5 | f REG 0 Σ+ 10 Σ+ 20 Σ+ | 3,00 | Três anos do ativo B lançados |
| 6 | g x̄ | 10,00 | Retorno médio de B: também 10% ao ano |
| 7 | g s | 10,00 | Desvio padrão de B: 10 pontos percentuais |

**[Locução Direta]**
"Leia o visor. São dois ativos com números hipotéticos de três anos. O ativo A rendeu 8, 10 e 12%. O ativo B rendeu zero, 10 e 20%. Os dois têm a mesma média, 10% ao ano. Mas o desvio padrão de A é 2, e o de B é 10. O B tem cinco vezes mais risco com o mesmo retorno médio. Quem esperava 10% no B pode ter recebido zero. Resumo para a prova: risco é a incerteza, a chance de o retorno efetivo ser diferente do esperado, para cima ou para baixo. Ele se mede pela volatilidade, o desvio padrão dos retornos. E vem de cinco fontes: mercado, crédito, liquidez, operacional e legal. Agora, pause o vídeo e responda a pergunta da tela. A resposta: desvio padrão zero, porque nenhum retorno se afasta da média. Mas volatilidade zero no passado não apaga o risco de crédito. No próximo vídeo: o ativo livre de risco e os ativos com risco de crédito."

# R58B · Ativo livre de risco × ativos com risco de crédito (7 min)

**Base:** PD C-PRO R v1.2, item 4.5.1 · Fundo Garantidor de Créditos (limites de cobertura, fgc.org.br) · liquidação do Banco Master pelo Banco Central, 18/11/2025. **Escopo:** o que é ativo livre de risco, por que o Tesouro Selic é a referência no Brasil, quais ativos têm risco de crédito, o rating, o prêmio de crédito e o papel do FGC. Os limites completos do FGC estão na aula do item 3.2.1.3.2; a relação risco-retorno e a dominância, no R58C.

## 1. Abertura Instigante (Destruição de Mito) — [45 s]

**[Ação na Lousa - Google Slides]**
- Slide 5 · ao dizer "Afirmação falsa", circule o mito · ao dizer "não o elimina", sublinhe a verdade

**[Locução Direta]**
"Em 18 de novembro de 2025, o Banco Central decretou a liquidação extrajudicial do Banco Master. O FGC estimou cerca de 41 bilhões de reais em garantias a pagar. Afirmação falsa: CDB com FGC é ativo livre de risco. Parece verdade porque o FGC devolve o dinheiro. A regra: o FGC reduz o risco de crédito, mas não o elimina, e a referência de ativo livre de risco no Brasil é o Tesouro Selic. Neste vídeo, a diferença entre os dois."

## 2. Metáfora Central de Fixação — [1 min]

**[Ação na Lousa - Google Slides]**
- Slide 6 · ao dizer "asfalto liso", circule a coluna da esquerda · ao dizer "até um limite", sublinhe a moldura

**[Locução Direta]**
"Volte à estrada. O ativo livre de risco é o asfalto liso: você sabe quanto vai ganhar e quase não há buraco. As outras estradas passam por pontes construídas por terceiros, um banco ou uma empresa. Se a ponte cair, é o risco de crédito. Em algumas delas, o FGC funciona como uma rede embaixo da ponte: segura quem cai, mas só até um limite. Onde a analogia quebra: o asfalto liso também treme um pouco, porque o Tesouro Selic tem pequenas oscilações de preço. O termo técnico é ativo sem risco de crédito e com baixa volatilidade."

## 3. Conteúdo Técnico e Roteiro Visual — [4 min]

**[Ação na Lousa - Google Slides]**
- Slide 7 · ao dizer "três motivos", sublinhe TESOURO SELIC · ao dizer "prêmio de crédito", circule a escada de rating

**[Locução Direta]**
"Na teoria, o ativo livre de risco é aquele que não tem risco de crédito e tem retorno conhecido, com volatilidade muito baixa. A banca também usa o nome taxa livre de risco, que você vai reencontrar no índice de Sharpe.

No Brasil, a referência é o Tesouro Selic, por três motivos. O emissor é soberano: o governo federal deve em reais, a moeda que ele mesmo emite e arrecada, e por isso tem o menor risco de crédito da economia. O título tem alta liquidez. E o retorno é previsível, porque acompanha a Selic.

Atenção ao caso-limite. O Tesouro Prefixado e o Tesouro IPCA também são do governo e têm o mesmo risco de crédito. Mas oscilam bastante com os juros, pela marcação a mercado. Por isso não servem como referência de ativo livre de risco.

Do outro lado estão os ativos com risco de crédito: CDB, LCI, LCA, debêntures, CRI, CRA e fundos de crédito. Neles, o retorno depende da capacidade do emissor de pagar juros e principal. As agências medem esse risco com o rating. E quanto pior o rating, maior o retorno que o investidor exige: é o prêmio de crédito, também chamado de spread.

O FGC entra só nos produtos bancários cobertos, como CDB, LCI e LCA. Ele cobre até 250 mil reais por CPF e por instituição, somando as instituições do mesmo conglomerado financeiro, com teto de 1 milhão a cada quatro anos. Debêntures, CRI e CRA não têm FGC.

Não confunda risco de crédito com risco de liquidez. Uma debênture de empresa sólida pode pagar tudo em dia e, mesmo assim, ser difícil de vender antes do vencimento.

E daí, para o cliente? Quem coloca 400 mil reais num único banco tem 150 mil sem cobertura do FGC. Dividir entre bancos de conglomerados diferentes reduz essa exposição.

*Pergunta-gatilho:* por ter FGC, o CDB vira ativo livre de risco? **Não.** O FGC tem limite e demora para pagar; a referência continua sendo o Tesouro Selic."

## 4. Resolução Rápida de Fixação — [1,3 min]

**[Ação na Lousa - Google Slides]**
- Slide 8 · ao dizer "150 mil reais", circule o resultado do cenário A · ao dizer "inteiramente cobertos", circule o resultado do cenário B · ao dizer "pause", aponte a pergunta do rodapé e espere 3 segundos

| Passo | Teclas na HP12C | Visor | O que significa |
|---|---|---|---|
| 1 | f REG f 2 | 0,00 | Memórias zeradas, 2 casas decimais |
| 2 | 400000 ENTER 250000 − | 150.000,00 | Cenário A: R$ 150 mil acima do limite do FGC |
| 3 | 400000 ÷ 100 × | 37,50 | 37,5% do dinheiro fica sem cobertura |

**[Locução Direta]**
"Leia o visor. O cliente tem 400 mil reais em CDB, já com os rendimentos. Números hipotéticos. No cenário A, tudo está num só banco: 150 mil reais, 37,5% do dinheiro, ficam fora do FGC. Se o banco quebrar, essa parte entra na fila da liquidação, sem prazo definido e sem garantia de recebimento. No cenário B, os mesmos 400 mil estão divididos em dois bancos de conglomerados diferentes, 200 mil em cada, e ficam inteiramente cobertos. Resumo para a prova: o ativo livre de risco não tem risco de crédito e tem baixa volatilidade; no Brasil, a referência é o Tesouro Selic; CDB, LCI, LCA, debêntures, CRI e CRA têm risco de crédito, medido pelo rating, e pagam mais por isso; e o FGC reduz, mas não elimina, o risco dos produtos bancários. Pause o vídeo e responda a pergunta da tela. A resposta: o limite seria um só para os dois bancos, 250 mil, e os mesmos 150 mil ficariam de fora. No próximo vídeo: risco, retorno e o princípio da dominância."

# R58C · Risco, retorno e o princípio da dominância entre ativos (7 min)

**Base:** PD C-PRO R v1.2, item 4.6 · teoria moderna de carteiras (Markowitz, 1952). **Escopo:** a relação entre risco e retorno, o prêmio de risco e o princípio da dominância entre ativos (forte, fraca e os casos sem dominância). A dominância entre carteiras e a fronteira eficiente estão na aula R60.

## 1. Abertura Instigante (Destruição de Mito) — [45 s]

**[Ação na Lousa - Google Slides]**
- Slide 9 · ao dizer "Afirmação falsa", circule o mito · ao dizer "é dominado", sublinhe a verdade

**[Locução Direta]**
"Um cliente recebe duas ofertas: um CDB de banco médio e o Tesouro Selic. Números hipotéticos: os dois prometem o mesmo retorno no ano. Afirmação falsa: com o mesmo retorno, tanto faz. Parece verdade porque o extrato vai mostrar quase o mesmo número. A regra: com o mesmo retorno e mais risco, o CDB é dominado, e um ativo dominado não deveria ser escolhido. Neste vídeo, a relação entre risco e retorno e o princípio da dominância."

## 2. Metáfora Central de Fixação — [1 min]

**[Ação na Lousa - Google Slides]**
- Slide 10 · ao dizer "Ninguém escolhe a B", circule o ponto B · ao dizer "quem decide é o motorista", circule A e C

**[Locução Direta]**
"Na estrada, cada caminho tem uma placa com duas informações: o ganho da viagem, que é o retorno esperado, e a quantidade de buracos, que é o risco. A estrada A dá 10 e tem poucos buracos. A B dá os mesmos 10 com muitos buracos. A C dá 12, também com muitos buracos. Ninguém escolhe a B: a A entrega o mesmo com menos buraco, e a C entrega mais com o mesmo buraco. Já entre A e C, quem decide é o motorista. Onde a analogia quebra: a placa mostra o esperado, e não o que vai acontecer na viagem. O termo técnico para a estrada B é ativo dominado."

## 3. Conteúdo Técnico e Roteiro Visual — [4 min]

**[Ação na Lousa - Google Slides]**
- Slide 11 · ao dizer "prêmio de risco", sublinhe a fórmula do topo · ao dizer "ninguém domina", circule a terceira coluna

**[Locução Direta]**
"A relação entre risco e retorno é um princípio básico das finanças: quanto maior o risco, maior o retorno esperado que o investidor exige. A diferença entre o retorno esperado de um ativo arriscado e o retorno do ativo livre de risco é o prêmio de risco.

Por que é assim? Porque o investidor é avesso ao risco. Se dois ativos prometessem o mesmo retorno, todos comprariam o mais seguro. O preço do mais arriscado cairia até o retorno esperado dele ficar maior. É o que o mercado resume como não existe almoço grátis.

Atenção à palavra esperado. Mais risco não garante mais retorno. Garante que o investidor exige mais para aceitar a incerteza. Num ano ruim, o ativo arriscado pode render bem menos que o seguro.

Agora, o princípio da dominância. Um ativo domina outro quando é melhor em pelo menos uma das duas dimensões, retorno e risco, sem ser pior na outra. Há dois tipos. A dominância forte: retorno maior e risco menor ao mesmo tempo. A dominância fraca: mesmo retorno com menos risco, ou mesmo risco com mais retorno.

E há dois casos em que ninguém domina. Quando um ativo tem mais retorno e também mais risco, a escolha depende do perfil do cliente. E quando os dois são iguais nas duas dimensões, eles são indiferentes.

Não confunda dominância entre ativos com dominância entre carteiras. Aqui comparamos ativos isolados. Quando a comparação é entre carteiras, entra a fronteira eficiente, tema da aula R60.

E daí, para o profissional? Primeiro, elimine os ativos dominados. Só depois discuta o perfil, entre os que sobraram.

*Pergunta-gatilho:* entre dois ativos, o de maior retorno esperado sempre domina o outro? **Não.** Se ele também tiver mais risco, não há dominância, e quem decide é o perfil."

## 4. Resolução Rápida de Fixação — [1,3 min]

**[Ação na Lousa - Google Slides]**
- Slide 12 · ao dizer "dominado duas vezes", circule B na conclusão · ao dizer "pause", aponte a pergunta do rodapé e espere 3 segundos · ao dizer "Para fechar a aula", sublinhe a síntese

| Passo | Teclas na HP12C | Visor | O que significa |
|---|---|---|---|
| 1 | f REG f 2 6 Σ+ 10 Σ+ 14 Σ+ | 3,00 | Três anos do ativo A lançados |
| 2 | g x̄ | 10,00 | Retorno médio de A: 10% ao ano |
| 3 | g s | 4,00 | Desvio padrão de A: 4 pontos percentuais |
| 4 | f REG 2 Σ+ 10 Σ+ 18 Σ+ | 3,00 | Três anos do ativo B lançados |
| 5 | g x̄ | 10,00 | Retorno médio de B: também 10% ao ano |
| 6 | g s | 8,00 | Desvio padrão de B: 8 pontos, o dobro de A |
| 7 | f REG 4 Σ+ 12 Σ+ 20 Σ+ | 3,00 | Três anos do ativo C lançados |
| 8 | g x̄ | 12,00 | Retorno médio de C: 12% ao ano |
| 9 | g s | 8,00 | Desvio padrão de C: 8 pontos, o mesmo de B |

**[Locução Direta]**
"Leia o visor. São três ativos com números hipotéticos de três anos. O A rende 10% com desvio padrão de 4. O B rende os mesmos 10% com desvio de 8. O C rende 12% com desvio de 8. A contra B: mesmo retorno, metade do risco. A domina B, com dominância fraca. C contra B: mesmo risco, mais retorno. C também domina B. O B é dominado duas vezes. E A contra C? Ninguém domina: quem decide é o perfil. Resumo para a prova: quanto maior o risco, maior o retorno esperado exigido, sem garantia de ganho. Dominância forte é ser melhor nas duas dimensões; fraca é ser melhor em uma e igual na outra; melhor em uma e pior na outra, decide o perfil. Pause o vídeo e responda a pergunta da tela. A resposta: com 13% e desvio de 8, o B passa a dominar o C, com o mesmo risco e mais retorno; contra o A, ninguém domina. Para fechar a aula: risco é incerteza, o Tesouro Selic é a régua, e quem corre mais risco exige mais retorno esperado. Na próxima aula, a R59: o risco de uma carteira e a diversificação."
