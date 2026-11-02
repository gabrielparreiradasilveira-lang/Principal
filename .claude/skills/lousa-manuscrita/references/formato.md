# Formato do roteiro (`lousa.py`)

Arquivo JSON em UTF-8. Coordenadas em pixels numa tela de 1920x1080 (origem no canto superior esquerdo).

## 1. Estrutura

Uma lousa:
```json
{"saida": "lousa.png", "fundo": "preto", "elementos": [ ... ]}
```

Várias lousas (gera `saida` de cada uma; sem `saida`, gera `<nome-do-json>_01.png`, `_02.png`…):
```json
{
  "padrao": {"fundo": "preto", "imperfeicao": 1.0},
  "slides": [
    {"saida": "aula_01.png", "elementos": [ ... ]},
    {"saida": "aula_02.png", "fundo": "lousa", "elementos": [ ... ]}
  ]
}
```
O que está em `padrao` vale para todos os slides; o slide pode sobrescrever.

## 2. Opções da lousa

| chave | padrão | o que faz |
|---|---|---|
| `saida` | nome do JSON + `.png` | arquivo de saída (relativo à pasta do JSON ou a `-o`) |
| `fundo` | `preto` | `preto` (molde), `grafite`, `lousa` (verde), `azul-noite` ou `#RRGGBB` |
| `giz` | só em `lousa` | falhas de giz no traço (o fundo aparece por dentro da letra) |
| `textura` | só em `lousa` | pó de giz apagado no fundo |
| `imperfeicao` | `1.0` | quanto treme: `0` = limpo, `0.6` = leve, `1` = molde, `1.6` = bem torto |
| `semente` | `7` | outra semente = outra "caligrafia" com o mesmo conteúdo; a mesma semente repete a imagem |
| `peso` | `1.0` | engrossa a letra (`0` = fonte pura, `2` = bem gorda) |
| `largura`, `altura` | `1920`, `1080` | tamanho da imagem |
| `fonte` | Permanent Marker | caminho de outra fonte `.ttf` (relativo ao JSON) |
| `endireitar` | `0.16` (fonte padrão) | corrige a inclinação da fonte (`0` = como a fonte vem) |

## 3. Elementos

Todo elemento aceita `id` (para ser alvo de outro), `imperfeicao` e `peso` próprios.
Cor: `amarelo`, `vermelho`, `verde`, `branco`, `azul`, `laranja`, `rosa`, `roxo`, `cinza` ou `#RRGGBB`.
`riscar`, `caixa`, `circular`, `sublinhar` e `seta` precisam vir **depois** do elemento que apontam.
Setas e linhas são sempre desenhadas por último (para encostarem nas caixas e nos riscos já feitos).

### `titulo`
Igual a `texto`, com outros padrões: `x` 40, `y` 24, `tamanho` 36, `cor` amarelo e sublinhado tremido embaixo
(`"sublinhado": false` tira; `espessura_sublinhado` 3.4).

### `texto`
| campo | padrão | |
|---|---|---|
| `texto` | — | `\n` quebra linha; `{cor:trecho}` pinta um trecho; `→ ← ↑ ↓ ↗ ↘` viram setinhas desenhadas; `≥ ≤ ≠` viram `>= <= =/=` |
| `x`, `y` | — | canto superior esquerdo do bloco (`y` = topo das maiúsculas). Aceitam `"centro"` |
| `largura` | sem quebra | largura máxima da linha; **sem ela o texto não quebra** |
| `tamanho` | 56 | tamanho da letra em px |
| `cor` | branco | |
| `alinhar` | esquerda | `esquerda`, `centro`, `direita` (dentro de `largura`) |
| `entrelinha` | 1.38 | distância entre linhas = tamanho x entrelinha (o molde usa ~1.6) |
| `espacamento` | 0.1 | espaço extra entre letras (fração da largura da letra) |

Minúsculas saem em versalete (maiúsculas menores) e maiúsculas saem grandes.

### `caixa`
Retângulo tremido em volta do `alvo` (ou da área `x`, `y`, `largura`, `altura`).
`margem` 30 · `espessura` 5.5 · `cor` = cor do alvo.

### `circular`
Contorno em volta do `alvo`: elipse em blocos curtos; "cápsula" (pílula) em frase comprida.
`margem` 22 · `espessura` 5 · `cor` = cor do alvo.

### `riscar`
`estilo` `"x"` (padrão: X grande passando do texto, como no molde) ou `"linha"` (um risco em cada linha).
`margem` 38 · `espessura` 4.2 · `cor` = cor do alvo.

### `sublinhar`
Traço tremido sob cada linha do alvo. `so_ultima_linha` false · `espessura` 4 · `cor` = cor do alvo.

### `seta` e `linha`
| campo | padrão | |
|---|---|---|
| `de`, `para` | — | id, ponto `[x, y]` ou área `[x0, y0, x1, y1]`. Com ids, a seta sai da borda certa sozinha |
| `pontos` | — | alternativa: caminho `[[x, y], ...]` (a ponta fica no último ponto) |
| `curva` | aleatória pequena | `0` = reta; `0.15` curva para um lado, `-0.15` para o outro |
| `folga` | 28 | distância entre a seta e as bordas de `de`/`para` |
| `cor` / `espessura` | branco / 5 | |
| `tamanho_ponta` | automático | |
| `duas_pontas` | false | ponta nas duas extremidades (só `seta`) |

### `desenho`
`nome` (lista: `python3 scripts/lousa.py --desenhos` ou `assets/exemplos/desenhos.png`), `largura` 200
(a altura vem do formato do desenho), `cor` branco, `espessura` automática.
Nomes: alvo, ampulheta, balanca, balanca_peso, balao, banco, carro, casa, check, cofrinho, dinheiro, estrela,
exclamacao, grafico_alta, grafico_baixa, lampada, moeda, pessoa, prancheta, receita, termometro, tubo_ensaio, xis.

### `livre`
Traço à mão por pontos: `pontos` `[[x, y], ...]`, `fechado` false, `cor`, `espessura` 4.5.
Serve para chave, colchete, curva de gráfico, flecha torta etc.

## 4. Posição relativa

Em vez de `x`/`y`, qualquer `texto`, `titulo` ou `desenho` aceita `abaixo_de`, `acima_de`, `direita_de` ou
`esquerda_de` (id ou área) + `distancia` (40). O elemento fica centralizado em relação ao outro no eixo
que sobra; se você também der `x` (ou `y`), ele prevalece.
Ex.: `{"tipo": "desenho", "nome": "carro", "abaixo_de": "verdade", "distancia": 50}`.

## 5. Grade da tela e tamanhos

- Margem segura: 40 px nas laterais, 24 no topo, 40 embaixo. O título ocupa y 20–75; a área útil é y 140–1040.
- Duas colunas: x 80–900 e x 1020–1840 (divisória em x ~960). Três colunas: x 80, 700, 1320 (largura ~520).
- Tamanhos: título 32–40 · texto principal 50–64 · texto de apoio 40–46 · mínimo para slide 34.
- Regra de bolso (com `espacamento` 0.1), caracteres por 800 px de largura:

| tamanho | minúsculas (versalete) | MAIÚSCULAS | altura da linha (1.38) |
|---|---|---|---|
| 36 | 39 | 33 | 50 |
| 44 | 32 | 27 | 61 |
| 50 | 28 | 24 | 69 |
| 56 | 25 | 21 | 77 |
| 64 | 22 | 18 | 88 |

- Altura do bloco ≈ 0.75 x tamanho + (linhas − 1) x tamanho x entrelinha + 0.2 x tamanho.

## 6. Moldes de layout

Use como ponto de partida e ajuste as coordenadas ao tamanho real do texto (confira com `--grade`).

**A. Mito × Verdade** (o molde do professor) — `assets/exemplos/mito-x-verdade.json`.
Mito à esquerda (x 80, y ~340, largura ~800, vermelho) + `riscar`; verdade à direita (x ~1030, largura ~500,
verde) + `caixa`; `seta` branca do mito para a verdade; desenho-âncora `abaixo_de` a verdade.

**B. Causa → efeito** — `assets/exemplos/monetaria-x-fiscal.json`, slide 1.
Uma frase com setinhas no próprio texto (`"Selic sobe → crédito caro → consumo cai"`) em x 80, y ~190,
largura ~1150; abaixo, a analogia em laranja + `sublinhar` + desenho `direita_de`; frase de fixação centralizada
embaixo (`"x": "centro"`, y ~870) com `circular`.

**C. Comparação em 2 colunas** — `assets/exemplos/monetaria-x-fiscal.json`, slide 2.
Cabeçalhos coloridos em x 120 e x 1080 (y 170) + `sublinhar`; itens com `\n` em y 300; `linha` vertical em
x ~960 com 3 pontos levemente desalinhados; um desenho por coluna embaixo.

**D. Conceito + analogia.**
Termo grande em amarelo (x 80, y 200, tamanho 72) + `circular`; definição técnica em azul abaixo (largura ~900,
tamanho 46); à direita (x ~1250) o desenho da analogia (largura ~380) com a legenda em laranja `abaixo_de` ele;
`seta` da definição para o desenho.

**E. Pegadinha de prova.**
Enunciado errado em rosa/vermelho + `riscar` com `"estilo": "linha"`; desenho `exclamacao` `esquerda_de` ele;
forma correta em verde abaixo + `caixa`; uma palavra-chave em `{amarelo:...}`.
