// Conteúdo da Aula 2 da C-PRO R (itens 1.3, 1.5 e 1.6 do PD ANBIMA v1.2).
// Cada slide: tipo, bloco, tag, título, conteúdo, tempo (min), recurso visual e notas.
const S = [];
const add = (s) => S.push(s);

// ================= ABERTURA (5 min) =================
add({
  type: "capa", section: "Abertura", time: 1,
  kicker: "C-PRO R  ·  AULA 2",
  title: "Quem é o investidor, como conhecê-lo e que regras seguir",
  titleSize: 30,
  sub: "Itens 1.3, 1.5 e 1.6 do programa detalhado ANBIMA",
  sign: "O foco é aprender. A aprovação é consequência.",
  visual: "Capa com logo X8 e frase-assinatura.",
  notes: {
    conducao: "Boas-vindas. Objetivo da aula: sair do 'o que é' e chegar ao 'o que fazer' em três frentes: entender o investidor brasileiro (1.3), coletar as informações certas do cliente (1.5) e aplicar as regras de relacionamento e distribuição (1.6). Avise que haverá perguntas rápidas e 5 questões autorais no estilo da prova.",
  },
});

add({
  type: "flow", section: "Abertura", time: 2,
  tag: "MAPA DA AULA",
  title: "Três perguntas guiam os 90 minutos",
  cards: [
    { t: "Quem é o investidor brasileiro?", d: "Objetivos, destino do dinheiro, inflação, bancos digitais, aposentadoria, estresse, apostas e educação\n\nItem 1.3" },
    { t: "Como conhecer o meu cliente?", d: "Objetivos por prazo, liquidez, conhecimento, origem dos recursos e comprometimento da renda\n\nItem 1.5" },
    { t: "Que regras eu sigo?", d: "Código ANBIMA de Distribuição, CVM 30, CMN 4.949, BCB 155 e Res. Conjunta 8/2023\n\nItem 1.6", hi: true },
  ],
  foot: "Capítulo 1 do programa (Prospecção e relacionamento com a pessoa investidora) = 20% do programa da C-PRO R",
  visual: "Fluxo de 3 cartões numerados, um por item do programa; o terceiro em destaque.",
  notes: {
    explicacao: "Esta aula fecha o Capítulo 1 do programa: a Aula 1 tratou de 1.1, 1.2 e 1.4. Segundo o programa detalhado vigente (v1.2, vigência a partir de 01/01/2026), o Capítulo 1 representa 20% do programa. O programa não informa peso por subitem, então não diga à turma que um tema 'cai mais' que outro.",
    conducao: "Mostre a lógica da aula: primeiro o retrato do país (estatística), depois a entrevista com o cliente (coleta), por fim as regras que transformam a coleta em recomendação adequada.",
  },
});

add({
  type: "compare", section: "Abertura", time: 2,
  tag: "AQUECIMENTO · PERGUNTA RÁPIDA",
  title: "Avó e neto, a mesma pergunta",
  lead: "Os dois chegam juntos à agência e perguntam: \"Onde devo investir?\"",
  left: { t: "Dona Lúcia, 67 anos", items: ["R$ 40 mil na poupança \"porque é seguro\"", "Prefere falar com o gerente na agência", "Quer deixar uma reserva para a família"] },
  right: { t: "Kauã, 22 anos", items: ["Aplica tudo pelo app, seguindo vídeos", "Quer dar entrada num apartamento em 3 anos", "Nunca falou com um especialista"] },
  mid: "?",
  band: "Qual é a primeira pergunta que você faz a cada um? Responda antes de pensar em produto.",
  visual: "Dois cartões de perfil lado a lado com '?' central; faixa com a pergunta para a turma.",
  notes: {
    conducao: "Peça respostas rápidas (voz ou chat). Espera-se que a turma queira sugerir produto. Pare e mostre: antes de produto vêm objetivo, prazo, situação financeira e conhecimento. Essa é a espinha da aula.",
    explicacao: "Os dois cabem no retrato do investidor brasileiro da pesquisa Raio X (ANBIMA/Datafolha), mas cada um tem objetivo, prazo e conhecimento diferentes. A estatística diz onde procurar; a entrevista diz o que fazer.",
    prova: "Questões de conduta costumam trazer uma alternativa que já recomenda produto sem coletar informação. Ela tende a ser a errada.",
  },
});

// ================= BLOCO 1 · 1.3.1 a 1.3.4 (12 min) =================
add({
  type: "stats", section: "Bloco 1 · 1.3.1 a 1.3.4", time: 2,
  tag: "BLOCO 1 · 1.3",
  title: "O retrato do investidor brasileiro",
  cards: [
    { k: "INVESTEM", big: "36%", sub: "da população tem algum produto financeiro: 60,6 milhões de pessoas" },
    { k: "NÃO INVESTEM", big: "64%", sub: "107,7 milhões; 52% da população não guarda dinheiro de forma nenhuma" },
    { k: "SÓ NA POUPANÇA", big: "19%", sub: "da população investe apenas na caderneta: mais da metade dos investidores", hi: true },
  ],
  band: "Dado de pesquisa é ponto de partida. Na prova, a conduta correta é sempre individual.",
  visual: "Três cartões com números grandes; o terceiro em destaque azul.",
  notes: {
    explicacao: "Fonte: Raio X do Investidor Brasileiro, 9ª edição (ANBIMA/Datafolha; 5.832 entrevistas em novembro de 2025). Perfis da pesquisa: Caderneta 19%, Diversifica 17% (juntos, os 36% de investidores), Sem Reserva 52% e Economiza mas Não Investe 12%.",
    exemplo: "O cliente típico que chega à agência guarda dinheiro, mas na poupança. O traço que a apostila destaca é a preferência por segurança e liquidez, além da baixa educação financeira histórica e da desconfiança de produtos complexos.",
    conducao: "Pergunte: 'Quantos dos seus clientes estão só na poupança?'. Use a resposta para mostrar que o retrato bate com a prática.",
    prova: "A banca pode trazer o percentual no enunciado, mas a alternativa correta usa o dado para agir (perguntar o objetivo, calcular a perda real), e não apenas repete o número.",
  },
});

add({
  type: "compare", section: "Bloco 1 · 1.3.1 a 1.3.4", time: 2.5,
  tag: "BLOCO 1 · 1.3.1 E 1.3.2",
  title: "Por que poupa e o que faz com o que poupa",
  left: { t: "Objetivos para poupar (1.3.1)", items: ["Reserva de emergência", "Compra de bens: casa, carro, reforma, viagem", "Aposentadoria", "Educação e empreendedorismo"] },
  right: { t: "Destino da economia (1.3.2)", items: ["38% aplicaram em produtos financeiros", "19% guardaram sem aplicar", "7% compraram imóvel; 6% veículo", "Produto mais usado: poupança (22% da população)"] },
  band: "Não confunda: 'comprar imóvel' (32%) é o destino do RETORNO das aplicações, não do dinheiro economizado no ano.",
  visual: "Comparação lado a lado: objetivos (apostila) x destino do dinheiro (Raio X).",
  notes: {
    explicacao: "1.3.1: a apostila lista reserva de emergência, aquisição de bens, aposentadoria, educação, empreendedorismo e sonhos pessoais. 1.3.2: no Raio X, apenas 33% conseguiram economizar em 2025; desses, 38% aplicaram, 19% guardaram parado, 7% compraram imóvel e 6% veículo. Entre os investidores, a poupança caiu de 75% para 61% em cinco anos, e os títulos privados subiram de 8% para 20%.",
    exemplo: "Cliente diz 'quero só deixar rendendo'. 'Manter aplicado' (22% no destino do retorno) é objetivo sem finalidade: falta perguntar para quê e até quando.",
    conducao: "Pergunte: 'Qual a diferença entre o objetivo e o destino?'. Objetivo é o porquê; destino é onde o dinheiro foi parar.",
    prova: "A apostila resume a regra: a clareza do objetivo define o tipo de investimento, o prazo e o risco adequado.",
  },
});

add({
  type: "concept", section: "Bloco 1 · 1.3.1 a 1.3.4", time: 2.5,
  tag: "BLOCO 1 · 1.3.3",
  title: "Inflação: o dinheiro parado encolhe",
  what: "Poder de compra = valor ÷ (1 + inflação).\n\nMarlene: R$ 30.000 parados 12 meses, IPCA de 4,58%.\n30.000 ÷ 1,0458 = R$ 28.686\n\nPerdeu R$ 1.314 sem ver nada sair.",
  wfs: 13.5,
  say: "\"Não perdi nada: o saldo continua o mesmo.\"",
  act: "Mostrar ganho nominal x real com a conta da cliente e o custo de não investir.",
  band: "Perda real se calcula DIVIDINDO pela inflação, não subtraindo. Real = (1 + nominal) ÷ (1 + inflação) − 1.",
  visual: "Cartão de conta + balão com a fala da cliente + cartão 'como agir' + faixa 'Na prova'.",
  notes: {
    explicacao: "A apostila chama a inflação de invisível: o saldo nominal fica 'intacto', mas compra menos. IPCA de setembro de 2026: 4,58% em 12 meses (IBGE, divulgado em 09/10/2026), acima do teto da meta contínua (3% ± 1,5 p.p.).",
    exemplo: "HP12C: 30000 ENTER 1,0458 ÷ → 28.686,17. Na poupança (0,5% a.m. + TR, com Selic acima de 8,5% a.a.), sem TR: f REG 30000 CHS PV 0,5 i 12 n FV → 31.850,33; ÷ 1,0458 → 30.455,47 em poder de compra.",
    conducao: "Faça a conta ao vivo. A frase do slide da X8 resume: 'não investir também é uma decisão'.",
    prova: "Distrator clássico: subtrair a inflação (30.000 − 5%). Outro: tratar o saldo nominal como poder de compra.",
  },
});

add({
  type: "compare", section: "Bloco 1 · 1.3.1 a 1.3.4", time: 2,
  tag: "BLOCO 1 · 1.3.4",
  title: "Bancos digitais: o acesso caiu, a decisão não",
  left: { t: "O que o digital trouxe", items: ["Acesso fácil e tarifas menores", "Aplicar online: de 48% para 63% dos investidores", "App do banco: de 33% para 46%", "Conhecimento de bancos digitais: de 24% para 46%"] },
  right: { t: "Riscos do digital", items: ["Decisões rápidas e impulsivas", "Apps gamificados e notificações (nudges)", "Exposição a produtos inadequados", "Dificuldade de filtrar informação"] },
  band: "Conta em banco tradicional ainda lidera: 73,7% x 38,9% em banco digital. O cliente chega com o app instalado, mas sem critério.",
  visual: "Comparação: benefícios x riscos do digital, com números do Raio X na coluna da esquerda.",
  notes: {
    explicacao: "Fontes: Raio X 9ª ed. (meios para aplicar: presencial de 43% para 32%, online de 48% para 63%, app de 33% para 46%, entre 2021 e 2025) e nota da ANBIMA de 12/05/2026 (conhecimento de bancos digitais de 23,9% em 2022 para 45,6% em 2025; conta em banco tradicional 73,67% e digital 38,87%, que recuou do pico de 43,78% em 2024).",
    conducao: "Frase para a turma: a barreira de acesso caiu; a barreira de decisão, não. O critério é o serviço do profissional.",
    prova: "Afirmação falsa típica: 'o banco digital já superou o tradicional como conta do brasileiro' ou 'o digital dispensa orientação profissional'.",
  },
});

add({
  type: "table", section: "Bloco 1 · 1.3.1 a 1.3.4", time: 2,
  tag: "BLOCO 1 · 1.3.4.1 A 1.3.4.3",
  title: "Geração, renda e canais de informação",
  cols: ["Recorte", "Como se comporta", "Dado da pesquisa"],
  colW: [1.8, 3.9, 3.3],
  rows: [
    ["Geração Z", "App, retorno, diversifica, ouve amigos e influenciadores", "84% aplicam online; 66% têm conta digital"],
    ["Boomers", "Agência, segurança, poupança, gerente", "66% aplicam presencialmente; 7% conta digital"],
    ["Baixa renda", "Digital como porta de entrada; poupança e caixinhas", "Classe DE: 2% aplicaram em produtos financeiros"],
    ["Alta renda", "Digital como complemento; mantém assessoria", "Classe AB: 24% aplicaram em produtos financeiros"],
    ["Canais", "Para se informar: YouTube lidera", "Para decidir: gerente ou assessor (26%)"],
  ],
  rowH: 0.47,
  fs: 11.5,
  visual: "Tabela de recortes com uma coluna de dado da pesquisa.",
  notes: {
    explicacao: "Faixas etárias do Raio X: Geração Z 16–29, Millennials 30–44, Geração X 45–64, Boomers 65+ (a apostila e os slides usam faixas ligeiramente diferentes; siga a do enunciado). Na Geração Z, 23% decidem com amigos e parentes e 11% com influenciadores. Influenciadores pesam 6% na média para decidir. Assistentes de IA já são usados por 9% dos investidores.",
    exemplo: "O slide da X8 diz que 'quanto maior a renda, mais racional a decisão'. Cuidado: maior renda dá mais acesso a assessoria, mas não imuniza contra vieses. A classe AB é a mais atingida por golpes (47%).",
    conducao: "Pergunte: 'Em que canal está o seu público?'. Ligue com a Aula 1 (canais de prospecção).",
    prova: "Diferencie canal para se INFORMAR (YouTube, Instagram) de meio para DECIDIR (gerente ou assessor). A banca pode trocar os dois.",
  },
});

add({
  type: "quiz", section: "Bloco 1 · 1.3.1 a 1.3.4", time: 1,
  tag: "BLOCO 1 · PERGUNTA RÁPIDA",
  title: "Certo ou errado?",
  items: [
    "\"A maioria dos brasileiros investe em produtos financeiros.\"",
    "\"Se o saldo nominal não caiu, não houve perda.\"",
    "\"Boomers aplicam principalmente pelo aplicativo.\"",
    "\"Para decidir, o gerente ainda é o meio mais citado.\"",
  ],
  foot: "Dez segundos para cada. Polegar para cima ou para baixo.",
  visual: "Grade 2x2 de afirmações numeradas.",
  notes: {
    conducao: "Ritmo de jogo. Se errarem a 2, volte ao slide da inflação.",
    gabarito: "1 = errado (36% investem). 2 = errado (o poder de compra cai). 3 = errado (66% dos Boomers aplicam presencialmente). 4 = certo (gerente ou assessor, 26%).",
  },
});

// ================= BLOCO 2 · 1.3.5 a 1.3.7 (9 min) =================
add({
  type: "compare", section: "Bloco 2 · 1.3.5 a 1.3.7", time: 2.5,
  tag: "BLOCO 2 · 1.3.5 E 1.3.6",
  title: "Por que investir e por que não investe",
  left: { t: "Vantagens de aplicar (1.3.5)", items: ["Rentabilidade real positiva", "Proteção contra a inflação", "Liquidez para diferentes horizontes", "Diversificação e renda futura"] },
  right: { t: "Por que não investe (1.3.6)", items: ["82%: condições financeiras desfavoráveis", "67%: falta de dinheiro", "Medo de perder e desconfiança", "Baixa educação financeira e falta de hábito"] },
  band: "A barreira mais declarada é orçamento, não produto. 33% guardaram em 2025, mas só 12% da população guarda e não investe.",
  visual: "Comparação vantagens x barreiras; números do Raio X na coluna da direita.",
  notes: {
    explicacao: "1.3.5: a apostila lista rentabilidade real, proteção contra inflação, construção de patrimônio, diversificação, liquidez, acesso a produtos e renda passiva. 1.3.6: no Raio X, entre os que não guardam dinheiro (55% dos não investidores), 82% citam condições financeiras desfavoráveis e 67% falta de dinheiro; desemprego, 6%. A apostila acrescenta medo, consumo imediato, desconfiança, experiências ruins, complexidade, influência de terceiros e falta de hábito.",
    exemplo: "Slide da X8: 'Investir é coisa de rico'. Mostre que um aporte automático pequeno quebra essa crença.",
    conducao: "Pergunte: 'Qual desses motivos vocês mais ouvem?'.",
    prova: "Em caso de cliente que 'não sobra nada', a alternativa correta trabalha o orçamento e a reserva antes do produto.",
  },
});

add({
  type: "dialog", section: "Bloco 2 · 1.3.5 a 1.3.7", time: 2,
  tag: "BLOCO 2 · SITUAÇÃO PRÁTICA",
  title: "\"Nunca sobra nada para investir\"",
  lines: [
    { who: "CLIENTE", t: "Já tentei investir duas vezes. Desisti: no fim do mês nunca sobra." },
    { who: "PROFISSIONAL", t: "Quanto sobra nos meses bons? E em que dia cai o seu pagamento?" },
    { who: "CLIENTE", t: "Uns R$ 90, às vezes. E acabo gastando antes do mês seguinte." },
    { who: "PROFISSIONAL", t: "Vamos programar R$ 90 automáticos no dia do pagamento, numa reserva com liquidez diária." },
  ],
  visual: "Diálogo em 4 balões alternados.",
  notes: {
    explicacao: "Caso que liga 1.3.6 (barreira de orçamento) a 1.2 (estratégias comportamentais, Aula 1): o aporte automático no dia do recebimento tira a decisão da força de vontade. A reserva vem antes de produto de prazo.",
    exemplo: "Aldenir, 29 anos, motorista de aplicativo, renda média de R$ 2.800, sem dívida em atraso.",
    conducao: "Peça a dois alunos que leiam o diálogo. Pergunte: 'Por que começar pela reserva e não por um fundo?'.",
    prova: "Distratores típicos: 'explicar que falta de dinheiro é um motivo comum e retomar depois' (só explica) ou 'registrar o cliente como não investidor' (só identifica).",
  },
});

add({
  type: "stats", section: "Bloco 2 · 1.3.5 a 1.3.7", time: 2,
  tag: "BLOCO 2 · 1.3.7",
  title: "Aposentadoria: expectativa x realidade",
  cards: [
    { k: "CONTAM COM O INSS", big: "60%", sub: "dos não aposentados esperam viver da previdência pública" },
    { k: "JÁ DEPENDEM DO INSS", big: "93%", sub: "dos já aposentados dependem dele na prática" },
    { k: "JÁ COMEÇARAM", big: "16%", sub: "menor número da série histórica; 57% pretendem, 27% nem pretendem", hi: true },
  ],
  band: "O INSS tem teto. Quem ganha acima dele tem uma lacuna de renda que só a reserva de longo prazo cobre.",
  visual: "Três cartões numéricos: expectativa, realidade e preparo.",
  notes: {
    explicacao: "Raio X 9ª ed.: 60% dos não aposentados apontam a previdência pública como fonte principal (piso de 51% em 2022); 15% contam com o próprio salário, 13% com aplicações financeiras, 5% com previdência privada. 93% dos aposentados dependem do INSS. Teto do salário de contribuição em 2026: R$ 8.475,55 (Portaria Interministerial MPS/MF nº 13/2026; dado do Caderno de Roteiros C-Pro R, aula 003).",
    exemplo: "Rogério ganha R$ 12.000 e diz que vai se aposentar pelo INSS. A lacuna é de R$ 3.524,45 por mês (12.000 − 8.475,55), antes mesmo de o benefício ser calculado pela média.",
    conducao: "Pergunte: 'Quem aqui já calculou a própria lacuna?'.",
    prova: "A alternativa correta dimensiona a lacuna e a transforma em aporte; as erradas só explicam o teto ou citam o percentual da pesquisa.",
  },
});

add({
  type: "flow", section: "Bloco 2 · 1.3.5 a 1.3.7", time: 2.5,
  tag: "BLOCO 2 · 1.3.7.1 E 1.3.7.2",
  title: "Reserva de longo prazo e fontes de renda",
  cards: [
    { t: "INSS", d: "Benefício com teto e reajuste definido pelo governo" },
    { t: "Previdência complementar", d: "PGBL, VGBL, fundos de pensão: renda ou resgates" },
    { t: "Investimentos financeiros", d: "Renda fixa, ações, FII, dividendos, fundos" },
    { t: "Ativos reais", d: "Aluguéis, renda rural, negócio próprio", hi: true },
  ],
  noArrows: true,
  band: "O ideal é não depender de uma só fonte. Quanto mais cedo começa a reserva, menor o esforço mensal (juros compostos).",
  visual: "Quatro cartões das fontes de renda, lado a lado, sem setas (não é sequência).",
  notes: {
    explicacao: "1.3.7.1: a reserva de longo prazo exige aportes constantes, disciplina, produtos adequados, proteção contra inflação e gestão do risco conforme a idade (ciclo de vida). 1.3.7.2: a apostila lista as quatro fontes do slide. Slide da X8: 'INSS = Isso Não Será Suficiente' (frase de efeito, use com cuidado).",
    exemplo: "Rogério (slide anterior): lacuna de R$ 3.524,45; a 0,4% a.m. real, o capital que gera essa renda é 3.524,45 ÷ 0,004 = R$ 881.112,50; em 25 anos, f REG 881112,5 FV 0,4 i 300 n PMT → R$ 1.524,25 por mês (premissa didática).",
    conducao: "Mostre que a pergunta certa não é 'você precisa investir', e sim 'você precisa de R$ 1.524 por mês'.",
    prova: "Afirmação falsa típica: 'o INSS repõe o salário integral de quem ganha acima do teto'.",
  },
});

// ================= BLOCO 3 · 1.3.8 a 1.3.10 (11 min) =================
add({
  type: "flow", section: "Bloco 3 · 1.3.8 a 1.3.10", time: 2.5,
  tag: "BLOCO 3 · 1.3.8",
  title: "Estresse financeiro: motivos e impacto",
  cards: [
    { n: "47%", t: "Principais motivos", d: "Dívidas, inflação, emprego instável, renda irregular, falta de reserva" },
    { n: "+", t: "Investimentos", d: "Reduzem o estresse com plano, reserva e perfil; aumentam se o cliente não entende o produto" },
    { n: "≠", t: "Estrato social", d: "Baixa renda: sobreviver. Média: manter o padrão. Alta: proteger patrimônio e sucessão", hi: true },
  ],
  noArrows: true,
  band: "47% têm alto estresse financeiro. O estresse muda de forma com a renda, mas não desaparece.",
  visual: "Três cartões (motivos, impacto, estrato); o primeiro marcador mostra '47%'.",
  notes: {
    explicacao: "Raio X 9ª ed.: alto estresse em 47% e médio em 48%. Entre os de alto estresse, predominam mulheres (53%), Geração X (37%) e classe DE (39%); 82% não conseguiram economizar em 2025 e 41% têm dívidas em atraso. 1.3.8.2: a apostila lista quando o investimento reduz o estresse (diversificação, plano, entendimento dos riscos, carteira alinhada ao perfil, reserva) e quando aumenta (não entende o produto, volatilidade excessiva, expectativa irreal, decisões por medo ou euforia, falta de acompanhamento).",
    exemplo: "Cliente com perfil conservador que entrou em ações pela dica de um amigo e não dorme na queda: o investimento inadequado virou fonte de estresse.",
    conducao: "Pergunte: 'Um cliente rico pode ter estresse financeiro?'. Resposta: sim, ligado a patrimônio, status e sucessão.",
    prova: "Falsa típica: 'o estresse financeiro atinge apenas a baixa renda'.",
  },
});

add({
  type: "table", section: "Bloco 3 · 1.3.8 a 1.3.10", time: 3,
  tag: "BLOCO 3 · 1.3.9",
  title: "Apostas online: quem aposta e por quê",
  cols: ["Subitem", "O que a pesquisa mostra", "Leitura para o atendimento"],
  colW: [1.6, 4.0, 3.4],
  rows: [
    ["Público", "17% apostaram em 2025; 66% homens; idade média de 35 anos", "Gasto médio: R$ 195,15 por mês"],
    ["Geração", "Apostam 27% da Geração Z e 22% dos Millennials; 4% dos Boomers", "Público jovem e digital"],
    ["Motivação", "39%: dinheiro rápido; 32%: diversão; 20%: acham que é investimento", "Sinal de alerta para o orçamento"],
    ["Risco", "11% dos apostadores com alto risco de vício", "Investigar sem julgar"],
  ],
  rowH: 0.52,
  fs: 11.5,
  band: "Aposta é regulada (Lei 14.790/2023, Secretaria de Prêmios e Apostas), mas não é investimento: o resultado esperado é negativo.",
  visual: "Tabela por subitem do programa + faixa 'Na prova'.",
  notes: {
    explicacao: "Raio X 9ª ed.: 17% fizeram apostas online em 2025 (15% em 2024); renda média do apostador de R$ 5.402, contra R$ 4.627 na média. Quem acha que aposta é investimento gasta mais: R$ 284,81 por mês. Entre os apostadores problemáticos, 82% são da Geração Z ou Millennials e 56% estão na classe C. A apostila lista como motivações: ganhos rápidos, emoção, sensação de controle ('eu conheço esse time'), recuperar perdas, influência de amigos e influenciadores, publicidade e facilidade dos apps.",
    exemplo: "O slide da X8 cita '20 milhões de brasileiros (IBOPE, 2024)'; prefira os dados do Raio X 9ª edição, que são do programa de referência.",
    conducao: "Ligue com a Aula 1 (1.1.7, bets). Aqui o foco é QUEM aposta e POR QUÊ.",
    prova: "Falsa típica: 'por ser regulada, a aposta é uma forma de investimento'.",
  },
});

add({
  type: "compare", section: "Bloco 3 · 1.3.8 a 1.3.10", time: 2.5,
  tag: "BLOCO 3 · 1.3.10",
  title: "Certificado x finfluencer",
  left: { t: "Profissional certificado", items: ["Orienta conforme o perfil do cliente", "Educa: riscos, volatilidade, custos", "Age no melhor interesse e comunica conflitos", "Responde pela recomendação"] },
  right: { t: "Finfluencer", items: ["Linguagem simples e alcance enorme", "Desperta interesse e o primeiro contato", "Não substitui orientação personalizada", "Se contratado: contrato e aviso de publicidade"] },
  band: "Opinião e conteúdo educativo são diferentes de recomendação personalizada. 34% da população já sofreu golpe ou fraude; entre investidores, 42%.",
  visual: "Comparação lado a lado; destaque no último item de cada coluna.",
  notes: {
    explicacao: "1.3.10.1: a apostila lista as responsabilidades do certificado: orientação alinhada ao perfil, educação contínua, proteção e transparência, responsabilidade ética (diligência, competência, honestidade, imparcialidade). 1.3.10.2: os finfluencers democratizam o acesso, mas não substituem profissionais. Quando um distribuidor contrata um influenciador, as Regras e Procedimentos ANBIMA de Distribuição (Cap. VIII, versão de 13/05/2025) exigem contrato com escopo e remuneração, aviso claro de publicidade (#parceria e nome da instituição) e relação mensal de influenciadores. 1.3.10.3: os riscos são excesso de informação, promessas de retorno rápido (pirâmides, golpes), subestimação de riscos, emoção, mistura de aposta com investimento e ausência de orientação.",
    exemplo: "Raio X: 21% da população já fez curso de educação financeira (33% dos investidores; 37% na classe AB e 8% na DE).",
    conducao: "Pergunte: 'O que vocês fazem quando o cliente chega com o print de um influenciador?'. Resposta: verificar quem indicou, confrontar com o perfil e refazer a recomendação pelo processo formal.",
    prova: "A alternativa correta não desqualifica o influenciador por princípio: leva a indicação para o processo de adequação.",
  },
});

add({
  type: "question", section: "Bloco 3 · 1.3.8 a 1.3.10", time: 3,
  tag: "QUESTÃO AUTORAL 1 · ESTRESSE E APOSTAS",
  title: "Qual é a ordem certa?",
  case: "Ubiratan, 34 anos, renda de R$ 5.400, quer aplicar R$ 500 por mês. Na conversa, conta que paga o rotativo do cartão há quatro meses e que aposta cerca de R$ 200 por mês \"para juntar dinheiro mais rápido\".",
  ch: 1.05,
  ask: "Qual é a conduta mais adequada do profissional?",
  alts: [
    "Recomendar um fundo de ações para que o retorno compense o custo do cartão",
    "Explicar que apostas são reguladas por lei e seguir com a aplicação de R$ 500",
    "Priorizar a quitação do rotativo e a reserva, mostrando que aposta não é investimento",
    "Registrar o cliente como apostador e retomar o contato quando a renda aumentar",
  ],
  visual: "Caso em cartão + 4 alternativas em grade 2x2.",
  notes: {
    conducao: "Dê 1 minuto para resposta individual; depois peça votos por letra.",
    gabarito: "C.\nA) Incorreta. Nenhuma aplicação compensa com segurança o custo do rotativo, e o perfil do cliente não foi avaliado.\nB) Incorreta. Ser regulada (Lei 14.790/2023) não torna a aposta investimento; a alternativa só explica e ignora a dívida cara.\nC) Correta. Ordem técnica: sanar dívida cara, formar reserva e só então definir produto. O dinheiro das apostas é fluxo que pode acelerar a quitação.\nD) Incorreta. Apenas identifica e adia; não muda a situação do cliente.",
  },
});

// ================= BLOCO 4 · 1.5 (13 min) =================
add({
  type: "flow", section: "Bloco 4 · 1.5", time: 2.5,
  tag: "BLOCO 4 · 1.5.1",
  title: "O prazo do objetivo manda",
  cards: [
    { t: "Curto prazo", d: "Até cerca de 2 anos\nLiquidez alta, risco muito baixo\nEx.: viagem, carro, reserva" },
    { t: "Médio prazo", d: "De 2 a 5 anos\nEquilíbrio entre segurança e retorno\nEx.: entrada do imóvel, pós" },
    { t: "Longo prazo", d: "Acima de 5 anos\nAceita mais volatilidade\nEx.: aposentadoria, sucessão", hi: true },
  ],
  band: "O mesmo cliente arrojado pode ter um objetivo de curto prazo: para esse dinheiro, o prazo pesa mais que o apetite.",
  visual: "Fluxo de 3 cartões por horizonte; o de longo prazo em destaque.",
  notes: {
    explicacao: "O programa pede objetivos de curto, médio e longo prazo, mas não fixa as faixas. As faixas do slide (até 2 anos; 2 a 5; acima de 5) são as do material X8 (convenção didática). A apostila e as Regras ANBIMA exigem considerar o período do investimento, as preferências de risco e a finalidade.",
    exemplo: "Investimentos típicos (material X8): curto, com Tesouro Selic, CDB com liquidez diária e fundo DI; médio, com CDB intermediário e previdência; longo, com títulos longos, ações, ETFs e previdência.",
    conducao: "Pergunte: 'Um cliente arrojado que vai comprar um carro em 8 meses deve pôr esse dinheiro em ações?'.",
    prova: "Se a banca der faixas, use as do enunciado. A ideia cobrada é a relação prazo → liquidez → risco tolerável.",
  },
});

add({
  type: "flow", section: "Bloco 4 · 1.5", time: 2,
  tag: "BLOCO 4 · 1.5.2",
  title: "Situação financeira em 4 perguntas",
  cards: [
    { t: "Liquidez", d: "Reserva atual x ideal (1.5.2.1)" },
    { t: "Conhecimento", d: "Produtos que conhece e experiência (1.5.2.2)" },
    { t: "Origem", d: "De onde vêm os recursos e a renda ativa (1.5.2.3)" },
    { t: "Compromissos", d: "Dependentes, custos, dívidas, previdência (1.5.2.4)", hi: true },
  ],
  band: "Sem essas quatro respostas não há perfil, e sem perfil não há recomendação.",
  visual: "Fluxo de 4 cartões, um por subitem do programa.",
  notes: {
    explicacao: "O programa detalha a definição da situação financeira e do conhecimento em quatro subitens. Eles conversam com a coleta exigida pelas Regras ANBIMA (art. 21, §§ 2º a 5º) e pela CVM 30: objetivo, situação financeira e conhecimento.",
    conducao: "Explique que os próximos slides abrem cada uma das quatro.",
    prova: "Questões podem pedir em qual dimensão se encaixa uma informação ('tem três filhos' = comprometimento da renda).",
  },
});

add({
  type: "stats", section: "Bloco 4 · 1.5", time: 2.5,
  tag: "BLOCO 4 · 1.5.2.1",
  title: "Reserva de emergência: atual x ideal",
  case: "Paula gasta R$ 6.000 por mês, é CLT há 6 anos e tem R$ 12.000 em conta remunerada.",
  cards: [
    { k: "IDEAL (6 MESES)", line: "6 × R$ 6.000", big: "R$ 36 mil", bfs: 30, sub: "regra prática do material: de 6 a 12 meses de despesas" },
    { k: "ATUAL", line: "R$ 12.000 ÷ R$ 6.000", big: "2 meses", bfs: 30, sub: "de cobertura de despesas" },
    { k: "LACUNA", line: "R$ 36.000 − R$ 12.000", big: "R$ 24 mil", bfs: 30, sub: "prioridade antes de qualquer produto de prazo", hi: true },
  ],
  visual: "Caso em cartão + três cartões de conta (ideal, atual, lacuna).",
  notes: {
    explicacao: "O programa pede 'reserva de emergência atual versus ideal'. O tamanho ideal depende de gastos fixos, estabilidade da renda e dependentes (slide X8). Autônomo ou renda irregular pede mais meses. Não há número legal: 6 a 12 meses é regra prática.",
    exemplo: "HP12C: 6000 ENTER 6 × → 36.000; 12000 ENTER 6000 ÷ → 2; 36000 ENTER 12000 − → 24.000.",
    conducao: "Pergunte: 'E se Paula fosse autônoma?'. Espera-se: aumentar a meta.",
    prova: "Falta de liquidez = risco de vender investimentos na hora errada. A alternativa correta trata a lacuna da reserva antes de produtos de prazo.",
  },
});

add({
  type: "dialog", section: "Bloco 4 · 1.5", time: 2,
  tag: "BLOCO 4 · 1.5.2.2 A 1.5.2.4",
  title: "Conhecimento, origem e compromissos",
  lines: [
    { who: "PROFISSIONAL", t: "Com quais investimentos você já teve experiência?" },
    { who: "CLIENTE", t: "Só poupança. Mas recebi R$ 400 mil da venda da minha empresa." },
    { who: "PROFISSIONAL", t: "Hoje, qual é sua renda e quem depende dela? Há dívidas ou previdência?" },
    { who: "CLIENTE", t: "Sou consultor, renda variável. Tenho dois filhos e o financiamento da casa." },
  ],
  bh: 0.6,
  defs: [
    { k: "Conhecimento", v: "baixo (só poupança): limita produtos complexos" },
    { k: "Origem e renda", v: "venda de empresa (comprovar: PLD); renda irregular" },
  ],
  visual: "Diálogo em 4 balões + dois cartões de leitura técnica.",
  notes: {
    explicacao: "1.5.2.2: conhecimento = tipos de produto que conhece e experiência. 1.5.2.3: origem dos recursos é também requisito de prevenção à lavagem de dinheiro (slide X8); fonte atual de renda ativa e sua estabilidade. 1.5.2.4: comprometimento = dependentes, custos fixos e variáveis, dívidas e contribuição para previdência, para chegar à capacidade de poupança real.",
    exemplo: "Leitura do caso: muito patrimônio, pouco conhecimento, renda irregular e dois dependentes. Patrimônio alto não é sinônimo de perfil arrojado.",
    conducao: "Pergunte: 'Que perfil vocês dariam? Por quê?'. Mostre que conhecimento e situação financeira entram juntos.",
    prova: "Falsa típica: 'quem tem patrimônio elevado pode ser classificado como arrojado sem avaliar conhecimento'.",
  },
});

add({
  type: "quiz", section: "Bloco 4 · 1.5", time: 1.5,
  tag: "BLOCO 4 · PERGUNTA RÁPIDA",
  title: "Em qual dimensão entra cada fala?",
  items: [
    "\"Tenho três filhos e pago a escola deles.\"",
    "\"Nunca investi em ações nem em fundos.\"",
    "\"Esse dinheiro veio de uma herança.\"",
    "\"Tenho dois meses de despesas guardados.\"",
  ],
  foot: "Liquidez, conhecimento, origem ou comprometimento da renda?",
  visual: "Grade 2x2 de falas de cliente.",
  notes: {
    conducao: "Respostas rápidas em voz alta.",
    gabarito: "1 = comprometimento da renda (dependentes e custos). 2 = conhecimento e experiência. 3 = origem dos recursos. 4 = liquidez (reserva atual).",
  },
});

add({
  type: "question", section: "Bloco 4 · 1.5", time: 2.5,
  tag: "QUESTÃO AUTORAL 2 · COLETA DE INFORMAÇÕES",
  title: "O que pesa mais nessa decisão?",
  case: "Renato, perfil arrojado, quer aplicar R$ 40 mil em ações. Na coleta, conta que esse dinheiro é para trocar de carro daqui a 10 meses. Ele tem reserva de emergência completa.",
  ch: 1.0,
  ask: "Qual é a leitura técnica correta?",
  alts: [
    "Como o perfil é arrojado, ações são adequadas para qualquer objetivo do cliente",
    "A reserva completa autoriza aplicar esse valor em produtos de maior volatilidade",
    "O cliente deve primeiro refazer o perfil, que ficou arrojado por engano",
    "O prazo curto do objetivo exige liquidez e baixa volatilidade para esse recurso",
  ],
  visual: "Caso em cartão + 4 alternativas em grade 2x2.",
  notes: {
    conducao: "Peça que a turma identifique o prazo antes de olhar as alternativas.",
    gabarito: "D.\nA) Incorreta. O perfil não dispensa a análise do objetivo: a adequação considera objetivo, situação financeira e conhecimento.\nB) Incorreta. A reserva protege contra imprevistos, mas não muda a data do objetivo do carro.\nC) Incorreta. Nada indica erro no perfil; o cliente pode ser arrojado e ter um objetivo de curto prazo.\nD) Correta. Objetivo de curto prazo pede liquidez e previsibilidade, independentemente do apetite a risco.",
  },
});

// ================= BLOCO 5 · 1.6.1 (20 min) =================
add({
  type: "concept", section: "Bloco 5 · 1.6.1", time: 2,
  tag: "BLOCO 5 · 1.6.1 E 1.6.1.1",
  title: "Código ANBIMA: objetivo e abrangência",
  l1: "O QUE É",
  what: "Regras e Procedimentos que complementam os princípios do Código de Distribuição.\n\nValem para TODOS os produtos de investimento e para todos os distribuidores associados ou aderentes.",
  l2: "ANEXOS COMPLEMENTARES",
  say: "I. Private  ·  II. Fundos  ·  III. Modelos de transferência",
  l3: "SE HOUVER DIVERGÊNCIA",
  act: "O Anexo Complementar prevalece sobre a Parte Geral. Só o Fórum de Distribuição altera as regras.",
  band: "A numeração dos capítulos muda entre versões do documento. Estude o conteúdo, não o número do capítulo.",
  visual: "Cartão 'o que é' + cartão dos anexos + cartão de prevalência + faixa 'Na prova'.",
  notes: {
    explicacao: "Regras e Procedimentos do Código de Distribuição, versão de 13/05/2025 (conferida na ANBIMA), Cap. I, art. 1º: complementam o Código; a Parte Geral vale para a distribuição de todos os produtos; os Anexos trazem regras específicas (I private, II fundos, III modelos de transferência); só o Fórum de Distribuição modifica; em divergência, prevalecem os Anexos.",
    exemplo: "Atenção à numeração: o programa (elaborado em 2024) cita Conheça seu Cliente no Cap. III, Suitability no Cap. IV e Transferência no Cap. IX. Na versão de 2025 eles estão nos Caps. IV, V e X, porque foi incluído um capítulo sobre a divulgação da remuneração.",
    conducao: "Diga à turma que, na prova, o enunciado costuma citar o tema, e não o número do capítulo.",
    prova: "Pegadinha possível: 'a Parte Geral prevalece sobre os Anexos'. É o contrário.",
  },
});

add({
  type: "grid", section: "Bloco 5 · 1.6.1", time: 2.5,
  tag: "BLOCO 5 · 1.6.1.2",
  title: "Regras gerais da atividade de distribuição",
  cols: 2,
  cards: [
    { n: "I", t: "Regras gerais", d: "Não induzir o cliente a pensar que o distribuidor é consultor independente" },
    { n: "II", t: "Meios eletrônicos", d: "Seção no site com objetivo, público-alvo, carência, emissor, tributação, classificação, riscos e aviso de remuneração" },
    { n: "III", t: "Canais digitais", d: "Senha individual, operações criptografadas, uma sessão por usuário, trilha de auditoria por 5 anos" },
    { n: "IV", t: "Remuneração", d: "Divulgar a remuneração recebida pela distribuição: informações qualitativas e quantitativas", hi: true },
  ],
  dfs: 12,
  visual: "Grade 2x2, um cartão por seção (I a IV).",
  notes: {
    explicacao: "Cap. II das Regras ANBIMA (versão de 13/05/2025): art. 2º (seção I), art. 3º (conteúdo mínimo do site: objetivo/estratégia, público-alvo, carência e prazo, emissor, tributação, classificação do produto, principais riscos de liquidez, mercado e crédito, aviso de remuneração), art. 4º (canais de atendimento compatíveis com o porte), art. 5º (canais digitais; trilhas de auditoria retidas por no mínimo 5 anos), art. 6º (remuneração, detalhada no Cap. III: informe de investimento e extrato trimestral).",
    exemplo: "Aviso obrigatório no site: 'A instituição é remunerada pela Distribuição do produto. Para mais informações, consulte o documento disponível em...'.",
    conducao: "Pergunte: 'Por que a regra proíbe o distribuidor de se apresentar como consultor independente?'. Resposta: conflito de interesses, porque ele é remunerado pelo produto.",
    prova: "Números que podem aparecer: retenção da trilha de auditoria por no mínimo 5 anos.",
  },
});

add({
  type: "concept", section: "Bloco 5 · 1.6.1", time: 2,
  tag: "BLOCO 5 · 1.6.1.3",
  title: "Conheça seu cliente (KYC)",
  what: "Conhecer o cliente no início, no cadastro e durante todo o relacionamento.\n\nDocumento formal com: aceitação de clientes, visitas, sistemas de controle, atualização cadastral, beneficiário final e veto por risco.",
  wfs: 13.5,
  say: "\"Já sou cliente há 10 anos. Para que atualizar o cadastro?\"",
  act: "Explicar que o cadastro atualizado é condição para identificar o cliente e registrar todas as aplicações e resgates.",
  band: "KYC é sobre QUEM é o cliente (identificação e risco do relacionamento). Suitability é sobre O QUE é adequado a ele.",
  visual: "Layout padrão de conceito (o que é, fala do cliente, como agir) + faixa 'Na prova'.",
  notes: {
    explicacao: "Regras ANBIMA, Cap. IV (versão 2025; Cap. III no programa), arts. 18 e 19: documento escrito ou eletrônico, compatível com natureza, porte, complexidade e perfil de risco, com no mínimo os seis itens do slide; cadastro atualizado permite identificar o cliente e registrar todas as aplicações e resgates.",
    exemplo: "Beneficiário final: a pessoa natural por trás de uma empresa cliente.",
    conducao: "Pergunte a diferença entre KYC e suitability; use a faixa.",
    prova: "Distrator: tratar KYC e suitability como sinônimos.",
  },
});

add({
  type: "compare", section: "Bloco 5 · 1.6.1", time: 2.5,
  tag: "BLOCO 5 · 1.6.1.4",
  title: "Suitability: regra geral e dispensas",
  left: { t: "Regra geral", items: ["Distribuidor é responsável pelo suitability", "Só recomenda após verificar a adequação", "Coleta: objetivo, situação financeira e conhecimento", "Documento formal com critérios e controles"] },
  right: { t: "Dispensados (ANBIMA)", items: ["Fundos de renda fixa classificados como simples", "LFT (Tesouro Selic)", "CDB/RDB com emissor no nível do risco Brasil, liquidez diária ou até 6 meses e pós-fixado", "Produtos automáticos: suitability simplificado"] },
  fs: 12.5,
  band: "Para o CDB ser dispensado, os três critérios valem ao mesmo tempo (cumulativos).",
  visual: "Comparação: regra geral x dispensas.",
  notes: {
    explicacao: "Regras ANBIMA, Cap. V (versão 2025; Cap. IV no programa), art. 20 e parágrafo único; art. 21 (documento com mecanismo de coleta, critérios de perfil e de produto, comunicação do perfil e do desenquadramento, aferição periódica, atualização e controles). Coleta (art. 21, §§ 3º a 5º): período do investimento, preferências de risco e finalidade; receitas, patrimônio e necessidade futura de recursos; produtos conhecidos, volume e frequência das operações, formação e experiência. Art. 22: produtos automáticos têm suitability simplificado por declaração assinada, salvo se baseados em valor mobiliário.",
    exemplo: "CDB pós-fixado de banco grande com liquidez diária: dispensado. CDB prefixado de 3 anos: precisa de suitability.",
    conducao: "Teste: 'CDB pós-fixado, liquidez diária, emissor de rating baixo: está dispensado?'. Não: falha o critério do emissor.",
    prova: "A banca pode trocar um dos três critérios do CDB/RDB.",
  },
});

add({
  type: "flow", section: "Bloco 5 · 1.6.1", time: 2.5,
  tag: "BLOCO 5 · 1.6.1.4",
  title: "Cliente fora do perfil: o que fazer",
  cards: [
    { t: "Vedado recomendar", d: "Perfil inadequado, ausente ou desatualizado" },
    { t: "Cliente insiste", d: "Antes da 1ª aplicação naquela categoria de ativo" },
    { t: "Alertar", d: "Indicar as causas da divergência" },
    { t: "Declaração expressa", d: "Por categoria de ativo; atualizar em até 5 anos", hi: true },
  ],
  band: "Não é recusar a ordem nem executar calado: é alerta com a causa, declaração expressa e registro.",
  visual: "Fluxo de 4 etapas com a declaração em destaque.",
  notes: {
    explicacao: "Regras ANBIMA, art. 23 (versão 2025): vedada a recomendação nos três casos; antes da primeira aplicação com a categoria de ativo, alertar com as causas e obter declaração expressa, exclusiva para cada categoria; as declarações têm prazo máximo de 5 anos para atualização. Cliente que se recusa a fazer o perfil é tratado como 'sem perfil identificado' (art. 21, § 7º). A Res. CVM 30, arts. 6º e 7º, traz a mesma lógica.",
    exemplo: "Cliente conservadora quer um fundo multimercado indicado num vídeo: alerta, causa da divergência, declaração para a categoria 'FIF multimercado'.",
    conducao: "Pergunte: 'Se ela aplicar de novo no mesmo tipo de fundo no mês seguinte, precisa de nova declaração?'. Pela regra, a declaração é por categoria e antes da primeira aplicação nela.",
    prova: "Distratores: recusar automaticamente a ordem; executar sem alerta; reclassificar o perfil para acomodar o pedido.",
  },
});

add({
  type: "table", section: "Bloco 5 · 1.6.1", time: 2.5,
  tag: "BLOCO 5 · 1.6.1.5",
  title: "Três perfis, uma escala de risco",
  cols: ["Perfil", "Como o cliente se declara", "Pontuação máxima do produto"],
  colW: [1.9, 4.8, 2.3],
  rows: [
    ["Perfil 1 (conservador)", "Baixa tolerância a risco, baixo conhecimento, prioriza liquidez", "Até 1,5"],
    ["Perfil 2 (moderado)", "Média tolerância; preserva capital, aceita parte em mais risco", "Até 3"],
    ["Perfil 3 (arrojado)", "Tolera risco e aceita perdas em busca de retorno", "Até 5"],
  ],
  rowH: 0.62,
  fs: 12,
  band: "Escala de 0,5 (menor risco) a 5 (maior). Por portfólio, vale a média ponderada da carteira dentro do limite do perfil.",
  visual: "Tabela de 3 perfis com o limite de pontuação em destaque.",
  notes: {
    explicacao: "Regras ANBIMA, art. 24 (versão 2025): mínimo de três perfis; limites de 1,5, 3 e 5 quando a adequação é por produto (§ 1º); por portfólio, a média ponderada da carteira deve respeitar os mesmos limites (§ 2º). Classificação automática no Perfil 1 (§§ 3º a 5º): cadastro atualizado, sem investimento prévio incompatível e sem perfil concluído; o cliente deve ser comunicado e instruído a completar o processo, antes de qualquer recomendação. Art. 28: escala contínua de 0,5 a 5, considerando no mínimo os riscos de crédito, mercado e liquidez.",
    exemplo: "Pontuação mínima (art. 29): CDB de emissor grau de investimento, pós-fixado, até 2 anos = 0,75; prefixado = 1,00.",
    conducao: "Mostre que o perfil 'conservador' aceita produto de até 1,5: não é só renda fixa pós-fixada.",
    prova: "Questões de cálculo podem pedir a média ponderada da carteira (veja a questão 3).",
  },
});

add({
  type: "compare", section: "Bloco 5 · 1.6.1", time: 1.5,
  tag: "BLOCO 5 · 1.6.1.5.1 A 1.6.1.5.3",
  title: "Como o produto é classificado",
  left: { t: "Critérios mínimos", items: ["Riscos do produto e dos ativos subjacentes", "Perfil dos emissores e prestadores de serviço", "Existência de garantias", "Prazos de carência"] },
  right: { t: "Categorias mínimas", items: ["Ações · Derivativos", "Renda fixa crédito privado · Títulos públicos", "Classes de FII · Classes de FIP", "FIF cambial · FIF multimercado"] },
  fs: 13,
  band: "A classificação dos produtos é revista em prazo não superior ao da regulação: até 24 meses (CVM 30).",
  visual: "Comparação: critérios x categorias.",
  notes: {
    explicacao: "Regras ANBIMA, art. 25 (critérios), art. 26 (atualização em prazo não superior ao da regulação), arts. 28 e 29 (escala e pontuações mínimas obrigatórias) e art. 31 (categorias mínimas). A CVM 30, art. 9º, II, fixa a reclassificação das categorias em até 24 meses. As categorias são a base da declaração 'por categoria de ativo' do slide anterior.",
    exemplo: "Produtos complexos têm regras específicas (Subseção III), que ressaltam os riscos da estrutura e a dificuldade de precificação.",
    conducao: "Ligue as categorias à declaração expressa: a declaração vale por categoria.",
    prova: "Não confunda os 24 meses dos PRODUTOS com o prazo do PERFIL do cliente (até 5 anos, conforme o cadastro).",
  },
});

add({
  type: "question", section: "Bloco 5 · 1.6.1", time: 2.5,
  tag: "QUESTÃO AUTORAL 3 · CLASSIFICAÇÃO DE RISCO",
  title: "A carteira cabe no perfil?",
  case: "Um distribuidor usa a adequação por portfólio. Cliente de Perfil 2 (moderado) tem: 50% em um produto de pontuação 1,0; 30% em um de 3,5; e 20% em um de 4,0.",
  ch: 0.95,
  ask: "Qual é a conclusão correta?",
  alts: [
    "Inadequada, porque há produtos com pontuação acima de 3",
    "Adequada: a média ponderada é 2,35, abaixo do limite de 3",
    "Adequada: a média simples é 2,83, abaixo do limite de 3",
    "Inadequada: a média ponderada é 3,5, acima do limite de 3",
  ],
  visual: "Caso numérico + 4 alternativas.",
  notes: {
    conducao: "Peça a conta antes de olhar as alternativas: 0,5 × 1,0 + 0,3 × 3,5 + 0,2 × 4,0. HP12C: 0,5 ENTER 1 × 0,3 ENTER 3,5 × + 0,2 ENTER 4 × + → 2,35.",
    gabarito: "B.\nA) Incorreta. Esse raciocínio vale para a adequação produto a produto, mas o enunciado diz que a metodologia é por portfólio.\nB) Correta. 0,50 + 1,05 + 0,80 = 2,35 ≤ 3 (Regras ANBIMA, art. 24, § 2º).\nC) Incorreta. A média simples ignora os pesos: (1,0 + 3,5 + 4,0) ÷ 3 = 2,83.\nD) Incorreta. 3,5 é a pontuação de um produto, e não a média da carteira.",
  },
});

add({
  type: "flow", section: "Bloco 5 · 1.6.1", time: 2,
  tag: "BLOCO 5 · 1.6.1.5.4",
  title: "Transferência de produtos de investimento",
  cards: [
    { t: "Pedido", d: "Investidor formaliza no distribuidor CEDENTE (de preferência, por meio eletrônico)" },
    { t: "Verificação", d: "Titularidade correta e bloqueios judiciais, de crédito ou de garantia" },
    { t: "Comunicação", d: "Informa o custodiante de origem e justifica eventual impossibilidade" },
    { t: "Transferência", d: "Ativos vão ao CESSIONÁRIO, sem venda e com a mesma titularidade", hi: true },
  ],
  band: "Recusa só em casos previstos: bloqueio, desistência, cadastro inconsistente, posição não reconhecida, resgate pendente, sem contrato com o administrador.",
  visual: "Fluxo de 4 etapas do cedente ao cessionário.",
  notes: {
    explicacao: "Regras ANBIMA, Cap. X (versão 2025; Cap. IX no programa), arts. 52 a 54: transferência de cotas de classes de fundos e de custódia dos demais produtos, de mesma titularidade; pedido ao cedente; site e canal de atendimento sobre o processo; obrigações do cedente; seis hipóteses de recusa. Cedente = de onde sai; cessionário = para onde vai.",
    exemplo: "Cliente quer levar CDBs e cotas de fundo para outra corretora: pede ao cedente; se houver resgate ainda não liquidado, a transferência pode ser recusada até a liquidação.",
    conducao: "Ligue com a Aula 1 (portabilidade e desintermediação).",
    prova: "Pegadinha: trocar cedente por cessionário, ou dizer que a transferência exige vender os ativos.",
  },
});

// ================= BLOCO 6 · 1.6.2 a 1.6.5 (12 min) =================
add({
  type: "concept", section: "Bloco 6 · 1.6.2 a 1.6.5", time: 3,
  tag: "BLOCO 6 · 1.6.2",
  title: "CVM 30: o dever de verificar a adequação",
  l1: "VERIFICAR SE O PRODUTO",
  what: "1. É adequado aos OBJETIVOS do cliente\n2. É compatível com a SITUAÇÃO FINANCEIRA\n3. É compreendido: o cliente tem o CONHECIMENTO necessário\n\nVale para distribuidores e consultores, em qualquer canal.",
  wfs: 13.5,
  l2: "PRAZOS QUE CONFUNDEM",
  say: "Perfil do cliente: conforme o cadastro, no máximo 5 anos.\nClassificação dos produtos: até 24 meses.",
  l3: "DISPENSAS",
  act: "Investidor qualificado ou profissional (com exceções), carteira administrada, recomendação de consultor CVM.",
  band: "Sem perfil, perfil desatualizado ou inadequado: alerta com as causas + declaração expressa antes da 1ª operação na categoria.",
  visual: "Cartão dos três testes + cartão de prazos + cartão de dispensas + faixa 'Na prova'.",
  notes: {
    explicacao: "Res. CVM 30/2021 (texto consolidado conferido): art. 2º (não recomendar sem verificar a adequação); art. 3º (objetivos, situação financeira, conhecimento); art. 6º (vedações); art. 7º (alerta com causas e declaração expressa antes da primeira operação com a categoria; dispensado se o cliente segue consultor CVM); art. 9º (perfil atualizado na periodicidade do cadastro de PLD, intervalo máximo de 5 anos; reclassificação das categorias em até 24 meses); art. 10 (dispensas).",
    exemplo: "O slide X8 sobre KYC diz 'atualizar o perfil em até 24 meses'. Isso está errado: os 24 meses são da classificação dos produtos. As próprias Regras ANBIMA mandam atualizar o perfil 'em prazo não superior ao permitido pela regulação'.",
    conducao: "Escreva na lousa: PERFIL ≤ 5 anos | PRODUTO ≤ 24 meses.",
    prova: "Investidor qualificado (CVM 30): investimentos acima de R$ 1 milhão com declaração, ou aprovado em exames e certificações aceitos pela CVM. Profissional: acima de R$ 10 milhões com declaração. Esse tema é aprofundado no item 2.4.7.",
  },
});

add({
  type: "table", section: "Bloco 6 · 1.6.2 a 1.6.5", time: 2,
  tag: "BLOCO 6 · SÍNTESE",
  title: "Quem regula o quê no relacionamento",
  cols: ["Norma", "Quem edita", "A quem se aplica", "Foco"],
  colW: [2.0, 1.6, 2.9, 2.5],
  rows: [
    ["Código ANBIMA", "ANBIMA (autorregulação)", "Distribuidores associados ou aderentes", "Distribuição e suitability"],
    ["Res. CVM 30/2021", "CVM", "Distribuidores e consultores de valores mobiliários", "Adequação ao perfil"],
    ["Res. CMN 4.949/2021", "CMN", "Instituições financeiras", "Princípios e procedimentos no relacionamento"],
    ["Res. BCB 155/2021", "Banco Central", "Consórcios, instituições de pagamento e outras", "Mesmos princípios, outro público"],
    ["Res. Conjunta 8/2023", "CMN e BCB", "IFs e demais autorizadas pelo BCB", "Educação financeira"],
  ],
  rowH: 0.47,
  fs: 11,
  visual: "Tabela-síntese das cinco normas do item 1.6.",
  notes: {
    explicacao: "A tabela é o mapa do bloco. CMN 4.949/2021 e BCB 155/2021 têm a mesma espinha (ética, responsabilidade, transparência, diligência), mas públicos diferentes: a BCB 155 nasceu para administradoras de consórcio e instituições de pagamento e, pelo texto atualizado (alterações de 2024 e 2026, conferidas em fonte secundária), alcança também corretoras, distribuidoras, corretoras de câmbio e prestadoras de serviços de ativos virtuais.",
    conducao: "Peça à turma que diga, para cada caso, qual norma se aplica: um banco, uma instituição de pagamento, uma corretora recomendando ações.",
    prova: "A banca pode trocar o órgão (ex.: 'Resolução CVM 4.949'). CMN 4.949 é do Conselho Monetário Nacional.",
  },
});

add({
  type: "flow", section: "Bloco 6 · 1.6.2 a 1.6.5", time: 2.5,
  tag: "BLOCO 6 · 1.6.3",
  title: "Res. CMN 4.949/2021 no dia a dia",
  cards: [
    { t: "Princípios", d: "Ética, responsabilidade, transparência e diligência; tratamento justo e equitativo" },
    { t: "Contratação", d: "Adequação às necessidades, informação clara sobre custos e riscos, cancelar sem barreiras" },
    { t: "Política", d: "Política institucional de relacionamento aprovada pela alta administração" },
    { t: "Metas", d: "Metas e incentivos alinhados à política de relacionamento", hi: true },
  ],
  band: "Meta comercial não pode empurrar produto inadequado: a norma exige incentivos coerentes com o interesse do cliente.",
  visual: "Fluxo de 4 cartões com 'metas' em destaque.",
  notes: {
    explicacao: "Resolução CMN 4.949/2021 (princípios e procedimentos no relacionamento com clientes e usuários): princípios (art. 2º); cultura organizacional e tratamento justo, considerando perfis e vulnerabilidades; procedimentos de contratação e prestação de serviços (art. 4º: adequação, integridade, informação clara sobre direitos, deveres, custos, riscos e penalidades, redação compreensível, atendimento sem barreiras para cancelar e transferir); política institucional de relacionamento (art. 6º); gerenciamento da política (art. 7º); metas e incentivos alinhados (art. 8º), conforme o material X8. Texto integral não reaberto nesta sessão.",
    exemplo: "Banco que paga bônus só pelo volume de um produto de risco, para qualquer cliente, cria incentivo desalinhado.",
    conducao: "Pergunte: 'Já viram campanha de vendas que conflita com o perfil do cliente?'.",
    prova: "A CVM 30 trata da adequação ao perfil; a CMN 4.949, da conduta e da estrutura do relacionamento. As duas se complementam.",
  },
});

add({
  type: "compare", section: "Bloco 6 · 1.6.2 a 1.6.5", time: 2,
  tag: "BLOCO 6 · 1.6.4 E 1.6.5",
  title: "BCB 155 e educação financeira",
  left: { t: "Res. BCB 155/2021 (1.6.4)", items: ["Mesmos princípios da CMN 4.949", "Para consórcios, instituições de pagamento e outras autorizadas", "Política de relacionamento, controles e responsável", "Atendimento sem barreiras para cancelar e transferir"] },
  right: { t: "Res. Conjunta 8/2023 (1.6.5)", items: ["Educação financeira para clientes pessoa física e empresário individual", "Orçamento, poupança e prevenção ao superendividamento", "Valor para o cliente, amplo alcance, personalização", "Política com governança e indicadores"] },
  fs: 12.5,
  band: "Educar o cliente passou a ser dever institucional, não ação de marketing.",
  visual: "Comparação: BCB 155 x Resolução Conjunta 8/2023.",
  notes: {
    explicacao: "1.6.4: Res. BCB 155, de 14/10/2021, sobre princípios e procedimentos no relacionamento; vigência a partir de 01/03/2022 (com efeitos em 01/10/2022 para parte das instituições). 1.6.5: o programa cita a 'Resolução Conjunta BCB e CMN de 08/2023'; trata-se da Resolução Conjunta nº 8, de 21/12/2023, sobre educação financeira (instituições financeiras, de pagamento e demais autorizadas pelo BCB, para clientes pessoa natural e empresário individual), em vigor desde 01/07/2024 (fonte secundária). O '08/2023' do programa é o número da norma, e não um mês.",
    exemplo: "Uma instituição que só oferece educação financeira como anúncio de produto não cumpre o princípio de 'valor para o cliente'.",
    conducao: "Ligue com 1.3.10: a norma institucionaliza o papel educativo que vimos no bloco 3.",
    prova: "Pegadinha: atribuir a educação financeira obrigatória à CVM ou à ANBIMA.",
  },
});

add({
  type: "question", section: "Bloco 6 · 1.6.2 a 1.6.5", time: 2.5,
  tag: "QUESTÃO AUTORAL 4 · RELACIONAMENTO",
  title: "Meta x política de relacionamento",
  case: "Um banco lança campanha que paga bônus aos gerentes apenas pelo volume captado em um fundo de maior risco, sem distinção de perfil dos clientes. A área de controles aponta conflito com a Res. CMN 4.949/2021.",
  ch: 1.0,
  ask: "Qual providência atende à norma?",
  alts: [
    "Alinhar metas e incentivos à política institucional de relacionamento",
    "Manter a campanha, pois metas comerciais não são tratadas pela norma",
    "Transferir a responsabilidade pela adequação para o próprio cliente",
    "Suspender a distribuição do fundo para todos os perfis de clientes",
  ],
  visual: "Caso em cartão + 4 alternativas em grade 2x2.",
  notes: {
    conducao: "Pergunte primeiro: 'Qual é o problema da campanha?' (incentivo desalinhado do interesse do cliente).",
    gabarito: "A.\nA) Correta. A norma exige que metas e incentivos sejam compatíveis com a política institucional de relacionamento, que tem a adequação e o tratamento justo como base.\nB) Incorreta. A norma trata expressamente de incentivos e metas.\nC) Incorreta. A adequação é dever da instituição (e, na distribuição de valores mobiliários, também da CVM 30).\nD) Incorreta. Exagero: o fundo pode ser adequado a parte dos clientes; o problema é o incentivo, não o produto.",
  },
});

// ================= REVISÃO (8 min) =================
add({
  type: "review", section: "Revisão", time: 2,
  tag: "REVISÃO",
  title: "Cinco ideias para levar da aula",
  items: [
    "O retrato do país (Raio X) diz onde procurar; a entrevista com o cliente diz o que fazer.",
    "Dinheiro parado encolhe: o poder de compra se calcula dividindo pela inflação.",
    "Objetivo define prazo; prazo define liquidez e risco. Coleta: objetivo, situação financeira, conhecimento.",
    "Fora do perfil: alerta com a causa + declaração por categoria. Perfil até 5 anos; produtos até 24 meses.",
    "ANBIMA, CVM 30, CMN 4.949, BCB 155 e Res. Conjunta 8: interesse do cliente acima da meta.",
  ],
  visual: "Lista numerada de 5 aprendizados.",
  notes: { conducao: "Leia rapidamente e peça um exemplo de cliente para cada ideia. Reforce o ponto 4 como estratégia de prova." },
});

add({
  type: "quiz", section: "Revisão", time: 2,
  tag: "QUIZ RELÂMPAGO",
  title: "Qual norma ou regra resolve?",
  items: [
    "Instituição de pagamento precisa de política de relacionamento.",
    "Cliente insiste em produto acima do perfil.",
    "Banco cria programa de educação financeira para clientes.",
    "CDB pós-fixado, liquidez diária, emissor de primeira linha.",
  ],
  foot: "Trinta segundos para cada. Responda antes de virar o slide.",
  visual: "Grade 2x2 de situações numeradas.",
  notes: {
    conducao: "Ritmo de jogo; se houver erro, volte à tabela 'Quem regula o quê'.",
    gabarito: "1 = Res. BCB 155/2021. 2 = alerta com causas + declaração expressa (CVM 30, art. 7º; ANBIMA, art. 23). 3 = Res. Conjunta 8/2023. 4 = dispensado de suitability pelas Regras ANBIMA (critérios cumulativos atendidos).",
  },
});

add({
  type: "question", section: "Revisão", time: 3,
  tag: "QUESTÃO AUTORAL 5 · INTEGRADORA",
  title: "Coleta, perfil e conduta no mesmo caso",
  case: "Helena, 52 anos, tem perfil feito há 6 anos e o cadastro desatualizado. Herdou R$ 800 mil e pede para aplicar metade em um produto estruturado complexo que viu num vídeo. Diz que nunca investiu além da poupança.",
  ch: 1.1,
  cfs: 12.5,
  ask: "Qual é a conduta mais adequada?",
  alts: [
    "Aplicar, pois a herança a torna investidora qualificada automaticamente",
    "Recusar a aplicação e encerrar o atendimento até nova solicitação",
    "Atualizar cadastro e perfil (objetivos, situação e conhecimento, inclusive a origem) antes de recomendar",
    "Aplicar sem alerta, pois o pedido partiu da própria cliente",
  ],
  afs: 11.5,
  visual: "Caso longo em cartão + 4 alternativas.",
  notes: {
    conducao: "Peça primeiro que a turma liste os problemas do caso: perfil desatualizado (mais de 5 anos), baixo conhecimento, recurso novo de origem específica, produto complexo vindo de vídeo.",
    gabarito: "C.\nA) Incorreta. Investidor qualificado exige investimentos acima de R$ 1 milhão e declaração por escrito (CVM 30); herança de R$ 800 mil não basta, e a condição não é automática.\nB) Incorreta. A norma não manda recusar e encerrar: manda atualizar o perfil ou, se a cliente insistir, alertar e obter declaração.\nC) Correta. Com perfil desatualizado é vedado recomendar (CVM 30, art. 6º; ANBIMA, art. 23). A coleta inclui objetivos, situação financeira (inclusive a origem dos recursos, item 1.5.2.3) e conhecimento (1.5.2.2), decisivo num produto complexo.\nD) Incorreta. A iniciativa da cliente não dispensa o alerta e a declaração exigidos para ordens fora do perfil ou sem perfil atualizado.",
  },
});

add({
  type: "capa", section: "Revisão", time: 1,
  kicker: "ATÉ A PRÓXIMA AULA",
  title: "O foco é aprender.\nA aprovação é consequência.",
  titleSize: 30,
  sub: "Para fixar: resolva a lista de exercícios da X8 sobre características do investidor, coleta de informações e regras de distribuição.",
  sign: " ",
  visual: "Encerramento no layout da capa.",
  notes: { conducao: "Agradeça, indique os exercícios de fixação e abra espaço para dúvidas, se houver tempo." },
});

module.exports = S;
