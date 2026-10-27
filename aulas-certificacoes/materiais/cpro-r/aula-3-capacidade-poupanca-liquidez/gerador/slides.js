// Conteúdo da Aula 3 da C-PRO R (itens 2.1 e 2.2 do PD ANBIMA v1.2): 60 minutos.
// Cada slide: tipo, bloco, tag, título, conteúdo, tempo (min), recurso visual e notas.
// Caso único da aula: Marina, 36 anos, CLT, um filho.
const S = [];
const add = (s) => S.push(s);

const B0 = "Abertura";
const B1 = "Bloco 1 · 2.1.1 a 2.1.4";
const B2 = "Bloco 2 · 2.1.5 a 2.1.7";
const B3 = "Bloco 3 · 2.2.1 a 2.2.4";
const B4 = "Revisão";

// ================= ABERTURA (5 min) =================
add({
  type: "capa", section: B0, time: 1,
  kicker: "C-PRO R  ·  AULA 3",
  title: "Quanto sobra, quanto dura e quão rápido vira dinheiro",
  titleSize: 30,
  sub: "Itens 2.1 e 2.2 do programa detalhado ANBIMA: capacidade de poupança e liquidez",
  sign: "O foco é aprender. A aprovação é consequência.",
  visual: "Capa com logo X8 e frase-assinatura.",
  notes: {
    conducao: "Boas-vindas. Aula de 60 minutos, começo do Módulo 2 (Análise de informações do cliente). Hoje a pergunta não é 'onde investir', e sim 'quanto o cliente consegue guardar, quanto tempo ele aguenta sem renda e quão rápido o dinheiro dele vira dinheiro de verdade'. Avise que haverá uma pergunta rápida e 4 questões autorais.",
  },
});

add({
  type: "flow", section: B0, time: 1.5,
  tag: "MAPA DA AULA",
  title: "Três perguntas guiam os 60 minutos",
  cards: [
    { t: "Quanto sobra?", d: "Renda, idade, padrão de vida, planejamento, poupança do país e reserva de emergência\n\nItens 2.1.1 a 2.1.4" },
    { t: "Quanto vale e quanto dura?", d: "Balanço pessoal, ativos de uso e não uso, cobertura de despesas e índice de poupança\n\nItens 2.1.5 a 2.1.7" },
    { t: "Quão rápido vira dinheiro?", d: "Liquidez, reserva, liquidez × rentabilidade, liquidez corrente e liquidez seca\n\nItens 2.2.1 a 2.2.4", hi: true },
  ],
  foot: "Módulo 2 do programa (Análise de informações do cliente) = 20% do programa da C-PRO R",
  visual: "Fluxo de 3 cartões numerados, um por bloco; o terceiro em destaque.",
  notes: {
    explicacao: "Segundo o programa detalhado vigente (v1.2, vigência a partir de 01/01/2026), o Módulo 2 representa 20% do programa. O programa não informa peso por subitem, então não diga que um tema 'cai mais' que outro.",
    conducao: "Mostre a lógica: primeiro o fluxo (quanto entra e quanto sobra), depois a foto (o que o cliente tem e deve), por fim a velocidade (o que vira dinheiro rápido). Os três se cruzam no caso da Marina.",
  },
});

add({
  type: "stats", section: B0, time: 2.5,
  tag: "CASO DA AULA · PERGUNTA RÁPIDA",
  title: "Marina, 36 anos, CLT, um filho",
  case: "Marina pergunta: \"Ganho bem. Posso colocar tudo o que tenho num fundo imobiliário para ter renda?\"",
  cards: [
    { k: "RENDA LÍQUIDA", big: "R$ 12.000", bfs: 30, sub: "por mês, salário estável" },
    { k: "DESPESAS", big: "R$ 9.600", bfs: 30, sub: "por mês: fixas R$ 6.600 e variáveis R$ 3.000" },
    { k: "SOBRA", big: "?", sub: "Quanto ela consegue poupar? E quanto tempo aguentaria sem salário?", hi: true },
  ],
  visual: "Faixa com a fala da cliente e três cartões de números; o terceiro com interrogação.",
  notes: {
    conducao: "Peça a resposta pelo chat: quanto sobra? (R$ 2.400.) Depois pergunte: 'Ela pode colocar tudo num fundo imobiliário?'. Deixe a pergunta aberta: a aula inteira responde.",
    explicacao: "Dados hipotéticos e didáticos. Marina volta em todos os blocos: índice de poupança, reserva, balanço, cobertura, liquidez corrente e seca.",
  },
});

// ================= BLOCO 1 · 2.1.1 a 2.1.4 (19 min) =================
add({
  type: "concept", section: B1, time: 2,
  tag: "BLOCO 1 · 2.1",
  title: "Capacidade de poupança: o pilar da análise",
  what: "Quanto a pessoa consegue poupar de forma recorrente e sustentável ao longo do tempo. Vem antes de produto, alocação ou risco.",
  say: "\"Quando sobra, eu guardo.\"",
  act: "Trocar a sobra eventual por decisão estrutural: um valor definido, todo mês, como se fosse despesa obrigatória.",
  band: "Poupar não é \"sobrar dinheiro\": é decisão influenciada por renda, idade, padrão de vida, obrigações e comportamento.",
  visual: "Cartão de definição, balão com a fala do cliente e cartão de ação em destaque.",
  notes: {
    explicacao: "Capacidade de poupança é a parte da renda que fica depois das despesas essenciais, dos compromissos financeiros e do consumo. Costuma ser lida em percentual da renda. Uma estratégia de investimentos sólida começa pela construção de uma poupança viável.",
    exemplo: "Marina: R$ 12.000 − R$ 9.600 = R$ 2.400 por mês. Ainda não é o índice (que vem no Bloco 2), mas já mostra que há espaço para poupar.",
    prova: "Alternativa que recomenda produto antes de saber quanto o cliente consegue poupar tende a ser a errada.",
  },
});

add({
  type: "table", section: B1, time: 2.5,
  tag: "BLOCO 1 · 2.1.1",
  title: "Renda, idade e padrão de vida",
  lead: "Renda alta não garante poupança alta. Renda modesta, com disciplina, pode gerar poupança relevante.",
  cols: ["Fase", "Renda", "Despesas", "Poupança típica"],
  colW: [1.9, 2.3, 2.5, 2.3],
  rows: [
    ["Jovem", "Em crescimento", "Despesas iniciais altas (casa, carro, família)", "Baixa"],
    ["Meia-idade", "No pico", "Compromissos familiares, menos dependência inicial", "Alta"],
    ["Mais velho", "Estabilizada ou em queda", "Consumo do patrimônio acumulado", "Decrescente"],
  ],
  rowH: 0.5,
  band: "Padrão de vida: quanto maior o consumo em relação à renda, menor a margem para poupar, em qualquer faixa de renda.",
  visual: "Tabela de três fases do ciclo de vida, com faixa de prova.",
  notes: {
    explicacao: "A renda precisa ser lida junto com a fase de vida e o padrão de consumo. Capacidade de renda é o potencial de gerar fluxo positivo: depende de profissão, estabilidade, crescimento esperado e fontes adicionais (aluguéis, dividendos).",
    exemplo: "Marina está na meia-idade: renda estável e em bom nível, mas com um filho. A margem dela depende mais do padrão de vida do que do salário.",
    prova: "Pegadinha clássica: 'quem ganha mais sempre poupa mais'. Errado: o padrão de vida pode consumir toda a renda.",
  },
});

add({
  type: "flow", section: B1, time: 2,
  tag: "BLOCO 1 · 2.1.1",
  title: "Estratégias que garantem a poupança",
  cards: [
    { t: "Ajustes graduais de consumo", d: "Cortar aos poucos, sem trocar de vida de uma vez: o que é sustentável se mantém" },
    { t: "Priorização de objetivos", d: "Reserva primeiro, depois os objetivos com data: nem tudo cabe ao mesmo tempo" },
    { t: "Automatização dos aportes", d: "Aplicação programada no dia do salário: a poupança sai antes do consumo", hi: true },
  ],
  band: "O papel do profissional é adequar o padrão de vida à realidade financeira, sem comprometer a qualidade de vida.",
  visual: "Três cartões em sequência; a automatização em destaque.",
  notes: {
    explicacao: "São as três estratégias da apostila para viabilizar a poupança. A automatização transforma a poupança em despesa obrigatória: ela acontece antes de o dinheiro ser gasto.",
    exemplo: "Marina programa R$ 2.400 para o dia do salário. O que sobra no mês é o que ela pode gastar, e não o contrário.",
    conducao: "Pergunte: 'Quem aqui tem aplicação automática no dia do salário?'. Use as respostas para mostrar que poupar é processo, e não força de vontade.",
  },
});

add({
  type: "flow", section: B1, time: 2,
  tag: "BLOCO 1 · 2.1.2",
  title: "Planejamento para formar poupança",
  cards: [
    { t: "Objetivos claros", d: "Para que é o dinheiro e quando será usado" },
    { t: "Receitas e despesas mapeadas", d: "Saber o que entra e o que sai, inclusive o que é anual" },
    { t: "Metas mensais realistas", d: "Um valor que caiba na renda, e não um desejo" },
    { t: "Mecanismos automáticos", d: "Aporte programado, tratado como despesa obrigatória", hi: true },
  ],
  band: "Poupar de forma esporádica tende a falhar; poupar de forma planejada tende a se sustentar.",
  visual: "Quatro cartões em sequência com setas; o último em destaque.",
  notes: {
    explicacao: "Planejar é transformar intenção em processo. Os quatro passos são da apostila. Quando a poupança é tratada como despesa obrigatória, e não como sobra eventual, a chance de sucesso aumenta.",
    prova: "Questões costumam trazer a alternativa 'poupar o que sobrar no fim do mês'. É o oposto do planejamento.",
  },
});

add({
  type: "stats", section: B1, time: 2.5,
  tag: "BLOCO 1 · 2.1.3",
  title: "A poupança do país financia o investimento do país",
  cards: [
    { k: "TAXA DE POUPANÇA · 2025", big: "14,4%", sub: "do PIB: o que o Brasil poupou (IBGE)" },
    { k: "TAXA DE INVESTIMENTO · 2025", big: "16,8%", sub: "do PIB: o que o Brasil investiu (IBGE)" },
    { k: "A DIFERENÇA", big: "Poupança externa", bfs: 22, sub: "O país investe mais do que poupa e depende de capital de fora para fechar a conta", hi: true },
  ],
  band: "PIB = C + G + I + (X − M): sem poupança interna, o investimento depende de capital externo, que é mais caro e instável.",
  visual: "Três cartões de números: poupança, investimento e a diferença em destaque.",
  notes: {
    explicacao: "A poupança é tema macroeconômico também. Países com maior poupança interna têm mais recursos para investimento produtivo, menor dependência de capital externo e mais estabilidade. Em 2025, a taxa de poupança do Brasil foi de 14,4% do PIB, e a de investimento, de 16,8% (IBGE, Contas Nacionais Trimestrais).",
    exemplo: "Leitura simples: de cada R$ 100 produzidos, o país guardou R$ 14,40 e investiu cerca de R$ 16,80. A diferença veio de fora.",
    prova: "A prova cobra o conceito, e não o número. Guarde a lógica: pouca poupança interna significa crédito mais caro e juros mais altos.",
  },
});

add({
  type: "grid", section: B1, time: 2,
  tag: "BLOCO 1 · 2.1.3",
  title: "O que a baixa poupança custa ao Brasil",
  cols: 2,
  cards: [
    { t: "Custo do capital", d: "Dinheiro escasso é dinheiro caro: empresas pagam mais para se financiar" },
    { t: "Nível de juros", d: "Menos poupança disponível pressiona as taxas para cima" },
    { t: "Investimento de longo prazo", d: "Menor volume de obras, fábricas e infraestrutura" },
    { t: "Mercado de capitais", d: "Desenvolvimento mais lento: menos gente comprando ações e títulos de longo prazo", hi: true },
  ],
  band: "Conectar a decisão individual de poupar ao ambiente econômico é parte do trabalho do profissional.",
  visual: "Grade 2 × 2 com os quatro impactos da apostila.",
  notes: {
    explicacao: "Os quatro impactos são os da apostila: custo do capital, nível de juros, volume de investimentos de longo prazo e desenvolvimento do mercado de capitais.",
    exemplo: "Para o investidor, juros altos também têm outro lado: a renda fixa paga mais. Mas, para o país, o investimento produtivo fica mais caro.",
  },
});

add({
  type: "table", section: B1, time: 2.5,
  tag: "BLOCO 1 · 2.1.4",
  title: "Reserva de emergência: o tamanho depende do cliente",
  lead: "Reserva = despesa mensal × meses de segurança. Os meses dependem de quatro fatores:",
  cols: ["Fator", "Reserva menor", "Reserva maior"],
  colW: [2.6, 3.2, 3.2],
  rows: [
    ["Estabilidade da renda", "Salário estável (CLT, servidor)", "Renda variável, autônomo, comissionado"],
    ["Tipo de profissão", "Mercado com recolocação rápida", "Profissão sazonal ou de nicho"],
    ["Dependentes", "Nenhum", "Filhos, pais ou cônjuge dependentes"],
    ["Despesas fixas", "Baixas em relação à renda", "Altas e difíceis de cortar"],
  ],
  rowH: 0.42,
  band: "Prática de mercado: 3 a 6 meses de despesa para renda estável; até 12 meses para renda variável. Não é regra da norma.",
  visual: "Tabela de quatro fatores com as duas pontas, e faixa com as faixas de mercado.",
  notes: {
    explicacao: "A apostila lista os quatro fatores, sem número de meses. As faixas de 3 a 6 meses (renda estável) e até 12 meses (renda variável) são prática de mercado, e não norma. Medida em meses de DESPESA, e não de renda.",
    exemplo: "Marina é CLT, mas tem um filho: a meta razoável é 6 meses × R$ 9.600 = R$ 57.600. Hoje ela tem R$ 28.800 líquidos: falta R$ 28.800. Poupando R$ 2.400 por mês a 0,8% a.m., leva cerca de 11,5 meses (12 depósitos). HP12C: f REG · 0,8 i · 28800 FV · 2400 CHS PMT · n → 12,00 (a HP12C arredonda n para o inteiro de cima; a conta exata dá 11,50 meses).",
    prova: "Correção do material X8 (A5125-7): ele liga o tamanho da reserva ao perfil de suitability (conservador 12, moderado 6, arrojado 3 a 4 meses). A apostila liga a renda, profissão, dependentes e despesas, e não ao perfil de risco. Use os fatores.",
  },
});

add({
  type: "compare", section: B1, time: 2,
  tag: "BLOCO 1 · 2.1.4",
  title: "Onde fica a reserva",
  left: { t: "Serve para a reserva", items: ["Alta liquidez: D+0 ou D+1", "Baixo risco de crédito e de mercado", "Tesouro Selic, fundo DI, CDB de liquidez diária", "Rentabilidade não é a prioridade"] },
  right: { t: "Não serve para a reserva", hi: true, items: ["Ações e fundos imobiliários: oscilam e liquidam em D+2", "CDB com carência ou vencimento longo", "Previdência: resgate demorado e com imposto", "Imóvel: venda leva meses"] },
  band: "Sem reserva, o investidor toma decisões forçadas e emocionalmente custosas: vende no pior momento.",
  visual: "Duas colunas: o que serve e o que não serve para a reserva; a segunda em destaque.",
  notes: {
    explicacao: "A reserva é a base da segurança financeira. O critério é liquidez e baixo risco; a rentabilidade vem depois. O FGC cobre depósitos e títulos bancários até um limite por CPF e instituição (conferir o valor vigente antes de citar).",
    exemplo: "Resposta parcial à Marina: os R$ 28.800 de liquidez imediata não podem ir para o fundo imobiliário, porque são a reserva dela, e ainda pequena.",
  },
});

add({
  type: "question", section: B1, time: 2.5,
  tag: "QUESTÃO 1 · 2.1.4",
  title: "Questão 1",
  case: "Carlos é dentista autônomo, com renda que varia muito ao longo do ano, dois filhos e despesas mensais de R$ 15.000. Ele não tem reserva de emergência e pede ao assessor uma recomendação para começar.",
  ask: "Qual orientação está mais adequada?",
  alts: [
    "Formar cerca de 3 meses de despesa em ações de primeira linha, que têm boa liquidez",
    "Formar uma reserva maior, de até 12 meses de despesa, em ativos de liquidez diária e baixo risco",
    "Formar 6 meses de despesa em CDB com vencimento em 2 anos, que rende mais",
    "Dispensar a reserva, porque a renda dele é alta",
  ],
  visual: "Caso, comando e quatro alternativas em grade 2 × 2.",
  notes: {
    gabarito: "Letra B. Renda variável e dependentes pedem reserva maior (até 12 meses, prática de mercado), em ativos líquidos e de baixo risco. A) ações oscilam e liquidam em D+2; não servem para reserva. C) CDB com vencimento longo não tem a liquidez necessária. D) renda alta não dispensa reserva; renda variável aumenta a necessidade.",
    conducao: "Dê 1 minuto. Peça a letra no chat antes de mostrar o gabarito.",
  },
});

// ================= BLOCO 2 · 2.1.5 a 2.1.7 (14,5 min) =================
add({
  type: "table", section: B2, time: 2.5,
  tag: "BLOCO 2 · 2.1.5",
  title: "O balanço patrimonial da Marina",
  lead: "Balanço é a foto: tudo o que a pessoa tem e tudo o que deve, numa data.",
  cols: ["Ativos", "R$", "Passivos", "R$"],
  colW: [3.2, 1.3, 3.2, 1.3],
  rows: [
    ["Conta, Tesouro Selic e CDB diário", "28.800", "Fatura do cartão", "6.000"],
    ["CDB que vence em 8 meses", "14.400", "Financiamento do carro", "30.000"],
    ["Ações", "20.000", "Financiamento do apartamento", "210.000"],
    ["Previdência privada", "40.000", "", ""],
    ["Apartamento de moradia · Carro", "450.000 · 60.000", "", ""],
    ["Total de ativos", "613.200", "Total de passivos", "246.000"],
  ],
  rowH: 0.38, fs: 11.5,
  visual: "Tabela do balanço com ativos à esquerda e passivos à direita.",
  notes: {
    explicacao: "O balanço organiza tudo o que a pessoa possui e tudo o que deve. Dá visão clara da saúde financeira e é a base de decisões. Os bens entram pelo valor de hoje.",
    exemplo: "Dos R$ 30.000 do carro, R$ 18.000 vencem nos próximos 12 meses: vão para o passivo de curto prazo junto com a fatura (R$ 6.000), somando R$ 24.000. Esse número volta na liquidez.",
    conducao: "Deixe a turma olhar 30 segundos e perguntar: 'Marina é rica?'. A resposta vem no próximo slide.",
  },
});

add({
  type: "compare", section: B2, time: 2,
  tag: "BLOCO 2 · 2.1.5.1",
  title: "Ativos de uso e de não uso",
  left: { t: "Uso: mora com você", items: ["Moradia, veículos, bens pessoais", "Não geram renda direta", "Geram custo: IPTU, condomínio, seguro, manutenção", "Marina: R$ 510.000"] },
  right: { t: "Não uso: trabalha para você", hi: true, items: ["Investimentos, imóveis para renda, participações", "Geram renda ou valorização", "Pagam os objetivos futuros", "Marina: R$ 103.200"] },
  band: "A distinção evita superestimar o patrimônio: só o não uso contribui diretamente para os objetivos financeiros.",
  visual: "Duas colunas comparando uso e não uso, com os números da Marina.",
  notes: {
    explicacao: "O que decide é o uso, e não o tipo de bem: o mesmo apartamento é de uso se a família mora nele e de não uso se está alugado.",
    exemplo: "Marina: uso = apartamento (450.000) + carro (60.000) = 510.000, ou 83% do ativo. Não uso = 28.800 + 14.400 + 20.000 + 40.000 = 103.200. A casa enche o balanço, mas não paga a aposentadoria.",
    prova: "Pegadinha: 'imóvel alugado é ativo de uso'. Errado: gera renda, então é não uso.",
  },
});

add({
  type: "stats", section: B2, time: 2,
  tag: "BLOCO 2 · 2.1.5",
  title: "O que o balanço revela",
  cards: [
    { k: "PATRIMÔNIO LÍQUIDO", line: "613.200 − 246.000", big: "R$ 367.200", bfs: 26, sub: "Ativos menos passivos: a riqueza efetiva" },
    { k: "PESO DOS ATIVOS DE USO", line: "510.000 ÷ 613.200", big: "83%", sub: "Mais de quatro quintos do que ela tem é casa e carro" },
    { k: "O QUE TRABALHA", line: "não uso", big: "R$ 103.200", bfs: 26, sub: "É daqui que saem reserva, objetivos e aposentadoria", hi: true },
  ],
  band: "Patrimônio grande não é patrimônio disponível. Antes de recomendar, separe o que é uso do que é não uso.",
  visual: "Três cartões de números calculados a partir do balanço; o terceiro em destaque.",
  notes: {
    explicacao: "PL = ativos − passivos. Não confundir com o total de ativos.",
    exemplo: "HP12C: f REG · 613200 ENTER 246000 − → 367.200,00 · 613200 ENTER 510000 %T → 83,17.",
    conducao: "Volte à pergunta: 'Marina é rica?'. Ela tem R$ 367 mil de patrimônio, mas só R$ 103 mil trabalham, e só R$ 28,8 mil são de acesso imediato.",
  },
});

add({
  type: "stats", section: B2, time: 2.5,
  tag: "BLOCO 2 · 2.1.6",
  title: "Cobertura de despesas mensais",
  case: "Por quantos meses a Marina mantém o padrão de vida se o salário parar amanhã?",
  cards: [
    { k: "FÓRMULA", big: "Ativos líquidos ÷ despesa mensal", bfs: 17, sub: "Só o que vira dinheiro rápido, sem perda" },
    { k: "MARINA", line: "28.800 ÷ 9.600", big: "3 meses", sub: "No piso da faixa de renda estável" },
    { k: "META", line: "6 meses × 9.600", big: "R$ 57.600", bfs: 26, sub: "Com um filho, dobrar a cobertura", hi: true },
  ],
  band: "Cobertura mostra a resiliência do cliente a imprevistos e orienta as decisões de liquidez e risco.",
  visual: "Faixa com a pergunta e três cartões: fórmula, resultado e meta.",
  notes: {
    explicacao: "A apostila define a cobertura como o tempo que o patrimônio disponível cobre as despesas mensais, sem fórmula. A fórmula usada aqui é a do material X8 (A5126): ativos líquidos ÷ despesas mensais. Convenção de mercado, não norma.",
    exemplo: "HP12C: 28800 ENTER 9600 ÷ → 3,00. Ações e previdência ficam fora: não viram dinheiro rápido sem risco de perda.",
    prova: "Erro comum: dividir pela RENDA. A cobertura usa a DESPESA, porque é o que precisa ser pago sem salário.",
  },
});

add({
  type: "stats", section: B2, time: 2,
  tag: "BLOCO 2 · 2.1.7",
  title: "Índice de poupança",
  cards: [
    { k: "FÓRMULA", big: "Valor poupado ÷ renda do período", bfs: 17, sub: "Proporção da renda que vira poupança" },
    { k: "MARINA", line: "2.400 ÷ 12.000", big: "20%", sub: "De cada R$ 100 que entram, R$ 20 são poupados" },
    { k: "PARA QUE SERVE", big: "Acompanhar", bfs: 24, sub: "A evolução ao longo do tempo e as metas de acumulação", hi: true },
  ],
  band: "Mesmo período nos dois lados: poupança do mês sobre renda do mês, ou do ano sobre o ano.",
  visual: "Três cartões: fórmula, resultado da Marina e uso do indicador.",
  notes: {
    explicacao: "Índice de poupança = valor poupado no período ÷ renda total do período (apostila, p. 88). Ajuda a acompanhar a evolução e a fixar metas consistentes.",
    exemplo: "HP12C: 12000 ENTER 2400 %T → 20,00. Se o 13º salário entrar no ano, o cálculo anual muda; compare sempre períodos iguais.",
    prova: "Pegadinha: usar a despesa no denominador. O índice é sobre a RENDA.",
  },
});

add({
  type: "quiz", section: B2, time: 1.5,
  tag: "PERGUNTA RÁPIDA · CERTO OU ERRADO",
  title: "Quatro frases em 90 segundos",
  items: [
    "Patrimônio líquido é o total de ativos da família.",
    "Imóvel alugado a terceiros é ativo de não uso.",
    "A cobertura de despesas divide os ativos líquidos pela renda mensal.",
    "O índice de poupança divide o valor poupado pela renda do período.",
  ],
  foot: "Respostas: 1 errado (ativos − passivos) · 2 certo · 3 errado (é pela despesa) · 4 certo",
  visual: "Quatro frases numeradas em grade 2 × 2 e a linha de respostas.",
  notes: {
    conducao: "Leia as quatro frases e peça 'C' ou 'E' no chat para cada uma. Revele as respostas no rodapé ao final.",
  },
});

add({
  type: "question", section: B2, time: 2.5,
  tag: "QUESTÃO 2 · 2.1.6 E 2.1.7",
  title: "Questão 2",
  case: "Um cliente tem renda líquida de R$ 20.000 por mês, despesas mensais de R$ 16.000 e R$ 48.000 em ativos de liquidez diária. Ele não tem outras aplicações.",
  ask: "O índice de poupança e a cobertura de despesas mensais são, respectivamente:",
  alts: [
    "20% e 3 meses",
    "25% e 2,4 meses",
    "20% e 2,4 meses",
    "80% e 3 meses",
  ],
  visual: "Caso, comando e quatro alternativas em grade 2 × 2.",
  notes: {
    gabarito: "Letra A. Poupança = 20.000 − 16.000 = 4.000; índice = 4.000 ÷ 20.000 = 20%. Cobertura = 48.000 ÷ 16.000 = 3 meses. B) 25% usa a despesa no denominador (4.000 ÷ 16.000). C) 2,4 meses divide pela renda (48.000 ÷ 20.000). D) 80% é a parcela gasta, e não a poupada.",
  },
});

// ================= BLOCO 3 · 2.2.1 a 2.2.4 (14 min) =================
add({
  type: "concept", section: B3, time: 2,
  tag: "BLOCO 3 · 2.2.1",
  title: "Liquidez: virar dinheiro sem perder valor",
  what: "Facilidade com que um ativo vira dinheiro, sem perda relevante de valor. Quanto maior a liquidez, menor o risco de vender em condições desfavoráveis.",
  say: "\"Posso vender quando eu quiser, então é líquido.\"",
  act: "Perguntar duas coisas: em quanto tempo o dinheiro cai na conta e por quanto o ativo seria vendido naquele dia.",
  band: "Liquidez tem duas dimensões: prazo e preço. Vender rápido com perda grande não é liquidez.",
  visual: "Cartão de definição, balão com a fala do cliente e cartão de ação.",
  notes: {
    explicacao: "Definição da apostila (p. 88). O ponto que mais se perde: liquidez não é só velocidade; é velocidade sem perda relevante de valor.",
    exemplo: "As ações da Marina podem ser vendidas hoje, mas, numa queda de 20%, ela venderia com prejuízo. Rapidez sem preço não protege.",
  },
});

add({
  type: "compare", section: B3, time: 2,
  tag: "BLOCO 3 · 2.2.2",
  title: "Liquidez e reserva de emergência",
  left: { t: "Reserva em ativo líquido", items: ["Dinheiro disponível no dia do imprevisto", "Sem vender nada com prejuízo", "Sem pagar juros de cheque especial", "Cumpre a função da reserva"] },
  right: { t: "Reserva em ativo ilíquido", hi: true, items: ["Dinheiro preso quando mais se precisa", "Venda forçada, no pior preço", "Recurso a crédito caro", "A reserva deixa de ser reserva"] },
  band: "A reserva exige liquidez imediata. Alocá-la em ativos ilíquidos compromete a função principal dela.",
  visual: "Duas colunas: reserva líquida e reserva ilíquida; a segunda em destaque.",
  notes: {
    explicacao: "Apostila, p. 88: a reserva de emergência exige liquidez imediata. Por isso a necessidade de ativos líquidos é calculada a partir da reserva: quanto maior a reserva necessária, maior a parcela da carteira em liquidez.",
    exemplo: "Resposta à Marina: se ela puser os R$ 28.800 no fundo imobiliário, um imprevisto a obriga a vender as cotas no preço do dia, que pode estar em queda.",
  },
});

add({
  type: "table", section: B3, time: 2.5,
  tag: "BLOCO 3 · 2.2.2.1",
  title: "Liquidez × rentabilidade: a troca",
  lead: "Em geral, a relação é inversa: quem abre mão da liquidez cobra por isso.",
  cols: ["Ativo (exemplo)", "Liquidez", "Retorno esperado", "Uso típico"],
  colW: [2.6, 1.9, 2.0, 2.5],
  rows: [
    ["Tesouro Selic, CDB diário", "D+0 a D+1", "Menor", "Reserva de emergência"],
    ["CDB com vencimento em 2 anos", "No vencimento", "Maior", "Objetivo com data"],
    ["Previdência, fundos de prazo longo", "Baixa", "Maior no longo prazo", "Aposentadoria"],
  ],
  rowH: 0.48,
  band: "O desafio é equilibrar: cada parte do dinheiro tem o seu objetivo, e o objetivo define quanta liquidez ele precisa.",
  visual: "Tabela de três linhas, da maior para a menor liquidez.",
  notes: {
    explicacao: "Apostila, p. 88: existe, em geral, relação inversa entre liquidez e rentabilidade. A tabela é ilustrativa, sem taxas: as taxas mudam com o cenário. O material X8 (A5127-5) traz taxas de exemplo, que não usamos porque envelhecem.",
    exemplo: "Marina: os R$ 28.800 ficam em liquidez (reserva); os R$ 14.400 do CDB que vence em 8 meses podem ir para a reserva no vencimento; a previdência é dinheiro de longo prazo. Cada parte no seu lugar.",
    prova: "Pegadinha: 'o investidor deve sempre buscar a maior liquidez'. Errado: liquidez em excesso custa retorno. O equilíbrio depende do objetivo.",
  },
});

add({
  type: "stats", section: B3, time: 2.5,
  tag: "BLOCO 3 · 2.2.3",
  title: "Liquidez corrente",
  case: "Ativos de curto prazo ÷ passivos de curto prazo. Curto prazo = o que vence ou se resgata em até 12 meses.",
  cards: [
    { k: "ATIVOS DE CURTO PRAZO", line: "28.800 + 14.400", big: "R$ 43.200", bfs: 26, sub: "Diária mais CDB de 8 meses" },
    { k: "PASSIVOS DE CURTO PRAZO", line: "6.000 + 18.000", big: "R$ 24.000", bfs: 26, sub: "Fatura mais carro em 12 meses" },
    { k: "LIQUIDEZ CORRENTE", line: "43.200 ÷ 24.000", big: "1,80", sub: "Acima de 1: folga no ano", hi: true },
  ],
  band: "Acima de 1: folga. Igual a 1: equilíbrio sem margem. Abaixo de 1: o que vence no curto prazo é maior que o que vira dinheiro.",
  visual: "Faixa com a fórmula e três cartões: numerador, denominador e resultado.",
  notes: {
    explicacao: "Fórmula da apostila (p. 89). Valores acima de 1 indicam folga no curto prazo. A janela de 12 meses é a convenção adotada (material X8, A5127-9).",
    exemplo: "HP12C: f REG f 2 · 28800 ENTER 14400 + → 43.200 · 6000 ENTER 18000 + → 24.000 · ÷ → 1,80. Ações e previdência ficam fora: não são ativos de curto prazo.",
    prova: "Erro comum: colocar o financiamento inteiro do carro (R$ 30.000) no passivo de curto prazo. Só entra o que vence em até 12 meses.",
  },
});

add({
  type: "stats", section: B3, time: 2.5,
  tag: "BLOCO 3 · 2.2.4",
  title: "Liquidez seca: só o que vira dinheiro agora",
  case: "Ativos de resgate imediato ÷ passivos de curto prazo. Sai o que depende de prazo, venda de bens ou vencimento.",
  cards: [
    { k: "LIQUIDEZ CORRENTE", line: "43.200 ÷ 24.000", big: "1,80", sub: "Pagar o que vence no ano" },
    { k: "LIQUIDEZ SECA", line: "28.800 ÷ 24.000", big: "1,20", sub: "Pagar agora, sem esperar", hi: true },
    { k: "LEITURA", big: "Mais conservadora", bfs: 20, sub: "Sempre menor ou igual à corrente" },
  ],
  band: "Seca acima de 1: fluxo tranquilo mesmo sem esperar nada vencer. Abaixo de 1: vulnerável no curtíssimo prazo.",
  visual: "Três cartões comparando corrente e seca; a seca em destaque.",
  notes: {
    explicacao: "A apostila diz só que a liquidez seca exclui ativos de menor liquidez e dá uma visão mais conservadora, sem fórmula. Adotamos a convenção do material X8 (A5127-8): apenas caixa e aplicações de resgate imediato no numerador. Convenção de mercado, e não norma.",
    exemplo: "HP12C: 28800 ENTER 24000 ÷ → 1,20. Marina paga tudo o que vence no ano mesmo antes de o CDB vencer, com sobra de 20%.",
    prova: "Correção do material X8 (A5127): um slide diz que a corrente usa só o que se acessa rápido, e o quadro comparativo diz 'todos os ativos de curto prazo'. A regra coerente: corrente = todo o curto prazo; seca = só o imediato.",
  },
});

add({
  type: "question", section: B3, time: 2.5,
  tag: "QUESTÃO 3 · 2.2.3 E 2.2.4",
  title: "Questão 3",
  case: "Um cliente tem R$ 60.000 em ativos de curto prazo, dos quais R$ 25.000 em aplicações de resgate imediato. Suas obrigações com vencimento nos próximos 12 meses somam R$ 40.000.",
  ask: "Sobre a liquidez desse cliente, é correto afirmar que:",
  alts: [
    "A liquidez corrente é 1,5 e a seca é 0,63: há folga no ano, mas aperto imediato",
    "A liquidez corrente é 0,67 e a seca é 1,6: há aperto no ano, mas folga imediata",
    "As duas são 1,5, porque usam os mesmos ativos",
    "A liquidez seca é maior que a corrente, porque considera só ativos seguros",
  ],
  afs: 11.5,
  visual: "Caso, comando e quatro alternativas em grade 2 × 2.",
  notes: {
    gabarito: "Letra A. Corrente = 60.000 ÷ 40.000 = 1,5. Seca = 25.000 ÷ 40.000 = 0,625 ≈ 0,63. O cliente cobre o que vence no ano, mas não consegue pagar tudo agora sem esperar vencimentos. B) inverte numerador e denominador. C) a seca exclui os ativos menos líquidos. D) a seca é sempre menor ou igual à corrente.",
  },
});

// ================= REVISÃO (6 min) =================
add({
  type: "review", section: B4, time: 1.5,
  tag: "REVISÃO",
  title: "Cinco ideias para levar",
  items: [
    "Capacidade de poupança vem antes de produto: poupar é decisão estrutural, e não sobra",
    "O país poupa pouco (14,4% do PIB em 2025): crédito caro e juros altos",
    "Reserva em meses de despesa, pelos fatores do cliente, sempre em ativos líquidos",
    "Balanço: separe uso de não uso. Cobertura = líquidos ÷ despesa. Índice = poupado ÷ renda",
    "Liquidez é prazo e preço. Corrente usa todo o curto prazo; seca, só o imediato",
  ],
  visual: "Lista numerada de cinco ideias; a última com marcador dourado.",
  notes: {
    conducao: "Leia em voz alta e peça à turma que repita a fórmula da cobertura e a da liquidez seca.",
  },
});

add({
  type: "question", section: B4, time: 3.5,
  tag: "QUESTÃO INTEGRADORA · 2.1 E 2.2",
  title: "Questão integradora",
  case: "Marina, CLT com um filho, tem despesas de R$ 9.600 por mês, R$ 28.800 em aplicações de liquidez diária, liquidez seca de 1,20 e índice de poupança de 20%. Ela quer aplicar os R$ 28.800 num fundo imobiliário para ter renda mensal.",
  ask: "Qual é a orientação mais adequada?",
  alts: [
    "Aplicar tudo, porque a liquidez seca acima de 1 mostra folga",
    "Manter os R$ 28.800 como reserva (3 meses), completar 6 meses com a poupança mensal e só depois buscar renda",
    "Aplicar tudo, porque o índice de 20% repõe a reserva em poucos meses",
    "Trocar a reserva por previdência, que rende mais no longo prazo",
  ],
  afs: 11.5, cfs: 12.5, ch: 1.15,
  visual: "Caso da Marina, comando e quatro alternativas em grade 2 × 2.",
  notes: {
    gabarito: "Letra B. Os R$ 28.800 são a reserva dela e cobrem só 3 meses; com um filho, a meta razoável é 6 meses (R$ 57.600). Poupando R$ 2.400 por mês, ela completa em cerca de 12 depósitos; depois disso, pode direcionar a poupança para renda. A) a liquidez seca mede o curto prazo, mas o dinheiro que dá folga é justamente a reserva: aplicá-lo em fundo imobiliário derruba a seca. C) repor R$ 28.800 levaria cerca de 12 meses, e ela ficaria sem reserva nesse tempo. D) previdência não tem a liquidez exigida pela reserva.",
    conducao: "Feche o caso aberto no slide 3: esta é a resposta à pergunta da Marina.",
  },
});

add({
  type: "capa", section: B4, time: 1,
  kicker: "C-PRO R  ·  AULA 3",
  title: "Próxima aula: endividamento e perfil do investidor",
  titleSize: 28,
  sub: "Itens 2.3 e 2.4 do programa detalhado ANBIMA",
  sign: "O foco é aprender. A aprovação é consequência.",
  visual: "Capa de encerramento com logo X8 e a próxima aula.",
  notes: {
    conducao: "Agradeça, lembre que o passivo de curto prazo da Marina volta na próxima aula, quando falarmos de comprometimento de renda e endividamento (2.3).",
  },
});

module.exports = S;
