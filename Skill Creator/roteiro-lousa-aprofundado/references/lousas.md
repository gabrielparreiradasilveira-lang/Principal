# Lousas: padrão X8, moldes e formato do JSON

Gerador: `scripts/lousa.py` (Python 3 + Pillow; `--pptx` precisa de `python-pptx`). Conferidor: `scripts/conferir_lousas.py`. Fontes em `assets/fontes/` (Permanent Marker e Pangolin, licença OFL).

## 1. Padrão visual X8 (definido pelo professor)

| Regra | Como o gerador cumpre |
|---|---|
| PNG 1920×1080, fundo preto chapado | `"padrao": {"fundo": "preto"}` |
| Letra de mão em CAIXA ALTA, reta | automático; escreva o texto normal |
| Cores chapadas, sem brilho | paleta fixa |
| Amarelo: títulos e molduras · ciano: subtítulos · branco: texto | `titulo`, `subtitulo`, `texto`; `caixa` sai amarela |
| Laranja: destaque · verde: certo · vermelho: errado ou alerta | `{laranja:trecho}`, `{verde:…}`, `{vermelho:…}`; `riscar` sai vermelho |
| **A cor nunca carrega o sentido sozinha** (quem não distingue verde de vermelho, ou vê a gravação comprimida, perde a informação) | verde vem com ✓ (ou ↑) ou uma palavra-rótulo (CERTO, REGRA, VERDADE) na mesma linha; vermelho, com ✗ (⚠ no alerta, ↓ na queda) ou ERRADO, FALSO, MITO, ALERTA; número com sinal (+15,90%, −29,90%) dispensa. Vale também para `destaque` e `conclusao`, que saem em verde se você não der outra `cor` (use `"cor": "branco"` quando a frase não for certo/errado), e para o resultado de cenário com `cor` própria. Número neutro vai em laranja |
| Marca do vídeo e do bloco no topo, à direita do título: `R58A · 2/4` | automática, tirada do nome do PNG; o título termina antes dela |
| Rodapé de linhas curtas, cada uma em uma linha: síntese, pergunta, legenda e fonte | campos `sintese`, `pergunta`, `legenda` e `referencia` (seção 4); o molde se acomoda acima |
| Números de lista em circulinhos; tópicos sem tabela com grade | linha que começa com `1. ` vira circulinho; `- ` tópico; 2 espaços + `- ` subtópico |
| Cantos livres: logo (x ≥ 1560 e y ≤ 190) e webcam (x ≥ 1600 e y ≥ 760) | aviso se algo invadir; `--grade` mostra as áreas em rosa |
| Letra mínima de 28 px; corpo entre 30 e 34 px | aviso abaixo de 28; os moldes escolhem o maior tamanho que cabe |
| Vírgula decimal, ponto de milhar | aviso para ponto decimal e número sem ponto de milhar |
| Teclas da HP12C em caixinhas | `[ENTER]`, `[÷]`, `[CHS]`... (só se a lousa pedir; o professor faz a conta ao vivo) |
| Sem LaTeX; emoji vira desenho | aviso para `\frac`, `$…$`; ✅ ❌ ⚠️ viram desenho |

## 2. A lousa de referência (aprovada pelo professor em 04/11/2026; regras de 07/11/2026)

Bloco 2 da R50-1 (VGBL), molde `comparacao`. A fala do bloco explica as duas rodovias e diz que a tarifa da saída depende do regime e do prazo. A lousa traz o mesmo mapa desenhado e mais o que a fala não detalha:

```json
{"saida": "r50-1_2_duas-rodovias.png", "semente": 502, "molde": "comparacao",
 "titulo": "DUAS RODOVIAS ATÉ A APOSENTADORIA",
 "colunas": [
  {"titulo": "RODOVIA VGBL", "desenho": "rodovia_pedagio", "rotulos": ["ENTRADA = APORTE", "SAÍDA = RESGATE"],
   "texto": "- ✗ ENTRADA: {vermelho:SEM VALE-PEDÁGIO}\n- ✓ SAÍDA: PEDÁGIO SÓ SOBRE O {verde:LUCRO DA VIAGEM} (OS RENDIMENTOS)\n- MESMA CARGA, BASE MENOR: SÓ O QUE A CARGA GANHOU NO CAMINHO"},
  {"titulo": "RODOVIA PGBL", "desenho": "rodovia_pedagio", "rotulos": ["ENTRADA = APORTE", "SAÍDA = RESGATE"],
   "texto": "- ✓ ENTRADA: {verde:VALE-PEDÁGIO} DE ATÉ {laranja:12% DA RENDA BRUTA TRIBUTÁVEL}\n  - SÓ NA {laranja:DECLARAÇÃO COMPLETA} E, EM REGRA, COM INSS OU REGIME PRÓPRIO\n- ✗ SAÍDA: PEDÁGIO SOBRE A {vermelho:CARGA INTEIRA} (VALOR TOTAL)"}],
 "faixas": [
  "{ciano:TARIFA DA SAÍDA, NAS DUAS:} REGRESSIVO {laranja:35% → 10%} PELO TEMPO DE CADA APORTE · PROGRESSIVO: {laranja:TABELA DO IR}",
  "{ciano:CARGA DE EXEMPLO:} APORTES DE R$ 50.000 QUE VIRARAM R$ 80.000 → BASE NO VGBL {laranja:R$ 30.000} · NO PGBL {laranja:R$ 80.000}"],
 "destaque": {"texto": "✗ {vermelho:RODOVIA ERRADA:} PGBL NA DECLARAÇÃO SIMPLIFICADA NÃO USA O VALE E AINDA PAGA PEDÁGIO SOBRE A CARGA INTEIRA", "cor": "branco", "moldura": "vermelho"},
 "referencia": ["IR DA PREVIDÊNCIA (LEI 11.053/2004)", "DEDUÇÃO DO PGBL (LEI 9.532/1997)"]}
```

O que essa lousa faz: desenha a metáfora; traz a condição de uso (declaração completa, INSS ou regime próprio); põe em números o que a fala só menciona (a tarifa); usa um exemplo diferente do exercício do Bloco 4; mostra o erro de quem escolhe mal. É essa a quantidade de informação esperada. Desde 07/11/2026: ✓ e ✗ junto do verde e do vermelho, os valores neutros do exemplo em laranja, o tópico longo dividido em subtópico e a fonte no rodapé.

## 3. Estrutura do JSON

```json
{"padrao": {"fundo": "preto"},
 "slides": [
  {"saida": "r60a_1_abertura.png", "semente": 601, "molde": "mito_verdade", ...},
  {"saida": "r60a_2_mar-mare-barcos.png", "semente": 602, "molde": "comparacao", ...}
 ]}
```

- `saida`: `{video}_{bloco}_{slug}.png`, com o vídeo em minúsculas (`r60a`, `r50-1`) e o bloco de 1 a 4. O conferidor usa o nome para achar a fala do bloco. Bloco dividido em duas lousas (só se não couber nem em 28 px): mesmo bloco, número no fim do slug e título com "(1/2)", "(2/2)": `r60a_3_conteudo-1.png`, `r60a_3_conteudo-2.png`.
- `semente`: uma por lousa (muda a "caligrafia"; a mesma semente repete a imagem).
- `molde`: o gerador calcula posição e tamanho. `elementos` extras (com x/y) são desenhados por cima.

## 4. Moldes (use sempre um molde)

| molde | campos |
|---|---|
| `mito_verdade` | `titulo`, `mitos` (lista; saem em vermelho, riscados), `verdade` (verde, moldura), `desenho`, `apoio` (tópicos em largura total na parte de baixo: caso real em números, para quem vale) |
| `comparacao` | `titulo`, `colunas`: exatamente 2 `[{titulo, desenho, rotulos: [esquerda, direita], texto}]`, `faixas` (linhas de largura total abaixo das colunas), `destaque` (frase emoldurada na base) |
| `metafora` | `titulo`, `itens`: 2 a 4 `[{desenho, cor, extra, cor_extra, nome, legenda}]`, sobre uma estrada (`"estrada": false` tira) |
| `topicos` | `titulo`, `formula` ({antes, num, den}), `desenho`, `subtitulo`, `texto`, `destaque`, `largura_texto` |
| `colunas` | `titulo`, `formula`, `desenho`, `topo`, `colunas`: 2 ou 3 `[{titulo, texto}]`, `destaque` |
| `exercicio` | `titulo`, `dados` (enunciado em tópicos), `premissas` (obrigatório; sai logo abaixo dos dados), `cenarios`: exatamente 2 `[{titulo, passos, resultado, cor}]` (resultado emoldurado; em verde é a resposta certa da conta; no cenário que dá errado, `"cor": "vermelho"` e ✗ no resultado), `conclusao` (destaque na base, no formato regra → efeito) |
| `hp12c` | `titulo`, `passos`: `[{nome, teclas, visor, leitura}]` — só se o professor pedir as teclas na lousa |
| `pegadinhas` | `titulo`, `itens`: `[{frase, correcao, veredito}]` — fora do padrão atual (o professor tirou o bloco de pegadinhas) |

### Campos de toda lousa (com ou sem molde)

| campo | o que é | quando |
|---|---|---|
| `referencia` | a fonte do conceito técnico, da norma ou do dado: `"DESCRIÇÃO SIMPLES (IDENTIFICADOR)"`, ou uma lista delas. Sai no rodapé como "FONTE: …" | **toda lousa**. `false` só se a lousa não traz norma, dado nem conceito técnico (vira aviso) |
| `legenda` | `true` põe no rodapé a legenda das cores (✓ verde = certo · ✗ vermelho = errado ou alerta · laranja = destaque) | **primeira lousa da aula** |
| `pergunta` | a pergunta de recuperação, terminada em "?". Sai como "PAUSE E RESPONDA: …" | **Bloco 4 de cada vídeo** |
| `sintese` | a aula em uma linha, ligando os vídeos com → . Sai como "SÍNTESE: …" | **Bloco 4 do último vídeo da aula** |

A marca `R58A · 2/4` sai sozinha quando o nome do PNG segue o padrão. Cada linha do rodapé cabe em uma linha (cerca de 10 palavras na pergunta e na síntese); se quebrar, o gerador avisa.

**Referência que qualquer aluno entende:** primeiro o que é, em palavras simples; depois, entre parênteses, o identificador. Bom: `"IR DA PREVIDÊNCIA (LEI 11.053/2004)"`, `"GARANTIA DO FUNDO GARANTIDOR DE CRÉDITOS (FGC.ORG.BR, NOV./2026)"`, `"TEORIA MODERNA DE CARTEIRAS DE HARRY MARKOWITZ (ARTIGO DE 1952)"`. Ruim: `"IN RFB 1.585/2015, ART. 46"` (só o código). A referência é para conceito técnico, norma e dado; história ou caso ilustrativo não leva referência na lousa. Cite só o que você consultou (Etapa 0) e nunca a apostila.

No `exercicio`, os passos vão de 40 a 28 px e o resultado sai 4 px maior: a conta precisa ser lida de longe. `destaque` e `conclusao` aceitam texto ou `{texto, cor, moldura}`; `desenho` aceita nome ou `{nome, cor, largura}`. Nos moldes `comparacao`, `exercicio` e no `apoio`, "R$ 1.000" nunca quebra no meio da linha.

## 5. Texto

- **Tópico curto:** uma ideia por tópico, a palavra-chave na frente (`LIQUIDEZ → PRAZO CASADO COM O OBJETIVO`), no máximo **12 palavras** por tópico ou subtópico (números não contam). Passou disso, divida em subtópico (`  - `). Vale para linhas que começam com `- `, `• ` ou `1. `; faixas e destaques são uma frase cada.
- **Premissas à vista em todo exemplo com números:** no `exercicio`, o campo `premissas` diz se os valores são hipotéticos ou reais, se o retorno é bruto ou líquido e o que ficou de fora (IR, custos, inflação), e a condição que o cenário exige (ex.: bancos de conglomerados diferentes). Fora do exercício, escreva a condição na própria linha ("(HIPOTÉTICO)", "BRUTO").
- **Regra → efeito:** quando a lousa compara dois cenários, a conclusão diz qual regra produziu a diferença (`O LIMITE VALE POR CONGLOMERADO → DIVIDIR TIROU R$ 150.000 DO RISCO`), não só o resultado.
- **Frase absoluta** (SEMPRE, NUNCA, ISENTO, SÓ VALE…) passa pelo teste do contraexemplo da Etapa 4 também na lousa; o conferidor lista as que achar.
- `\n` quebra linha; `{cor:trecho}` pinta um trecho; `→ ← ↑ ↓` viram setinhas desenhadas; `≥ ≤ ≠` viram `>= <= =/=`.
- `σ`, `β`, `ρ`, `√` saem desenhados; `R_{f}` escreve índice; ` ` (espaço que não quebra) prende pedaços: `"20% A.A."`.
- Fração à mão: elemento `fracao` (`antes`, `num`, `den`) ou o campo `formula` dos moldes.

## 6. Desenhos

Lista: `python3 scripts/lousa.py --desenhos`. Hoje: alvo, ampulheta, balanca, balanca_peso, balao, banco, caminhao, carro, casa, check, cofrinho, combustivel, dinheiro, diversificacao, estrada, estrada_buracos, estrela, exclamacao, fronteira_eficiente, grafico_alta, grafico_baixa, lampada, mar, moeda, onibus, pessoa, placa, prancheta, receita, rodovia_pedagio, serra, termometro, tubo_ensaio, xis.

**Metáfora sem desenho? Crie.** Acrescente uma entrada em `DESENHOS` (`scripts/desenhos.py`): `"aspecto"` (altura ÷ largura), `"descricao"` e `"tracos"` numa caixa de largura 1, com as primitivas `("linha", pontos)`, `("fechada", pontos)`, `("elipse", cx, cy, rx, ry)`, `("arco", cx, cy, rx, ry, a0, a1)`, `("grossa", pontos)`, `("ponto", cx, cy, r)`. Poucos traços: rabisco de professor, não ilustração. Renderize, abra o PNG e ajuste. Se o desenho servir a outras aulas, faça commit dele junto com as lousas.

## 7. Conferências (`conferir_lousas.py`)

| Reprova | Por quê |
|---|---|
| aviso do gerador | texto cortado, canto do logo ou da webcam invadido, letra abaixo de 28 px, sobreposição, LaTeX |
| ocupação abaixo de 70% da altura útil (y 120 a 1040) | lousa com a parte de baixo vazia |
| faixa sem tinta de mais de 120 px | buraco no meio ou pé vazio da lousa (a de referência tem até 38 px) |
| 8 palavras seguidas iguais à fala do mesmo vídeo e bloco | a lousa complementa, não copia (compara sem maiúsculas, acentos, pontuação e `{cor:}`) |
| lousa sem fala correspondente no roteiro | roteiro errado ou cabeçalho do vídeo fora do padrão: sem a fala, a repetição não seria conferida |
| menção à apostila | a apostila é fonte interna: nunca aparece na lousa |
| verde ou vermelho sem ✓/✗ ou palavra-rótulo na mesma linha (no texto, no destaque e na conclusão verdes e no resultado com cor própria) | a cor nunca carrega o sentido sozinha |
| tópico com mais de 12 palavras (números não contam) | uma ideia por tópico, palavra-chave na frente |
| lousa sem `referencia`, ou referência sem a descrição simples antes do identificador entre parênteses | conceito técnico, norma e dado têm fonte que o aluno entende |
| primeira lousa sem `legenda` · Bloco 4 sem `pergunta` (terminada em "?") · último vídeo sem `sintese` | legenda uma vez; recuperação no fim de cada vídeo; síntese no fim da aula |
| `exercicio` sem `premissas`, ou com `conclusao` sem → (ou "porque") | o aluno precisa ver o que o exemplo supõe e qual regra gerou a diferença |
| nome fora de `{video}_{bloco}_{slug}.png` | o conferidor não acha a fala do bloco |

Saem como aviso: vídeo sem as 4 lousas, `referencia: false` e frase absoluta na lousa (faça o teste do contraexemplo e registre no checklist). Depois de zerar, **abra cada PNG**: o conferidor não vê seta invertida, desenho mal escolhido nem número diferente do da fala.
