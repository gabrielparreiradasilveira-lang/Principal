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
| `fundo` | `preto` | padrão X8 = `preto` chapado. Outros (`grafite`, `lousa`, `azul-noite`, `#RRGGBB`) só se pedido |
| `maiusculas` | `true` | todo texto sai em caixa alta (padrão X8); `false` mantém minúsculas (viram versalete) |
| `tremor_texto` | `0` | padrão X8: letra reta e alinhada. Valores > 0 fazem a letra tremer/ondular |
| `areas_livres` | logo + webcam | cantos que não podem ter nada: `[["logo X8", 1560, 0, 1920, 190], ["webcam", 1600, 760, 1920, 1080]]`; `[]` desliga |
| `giz` | só em `lousa` | falhas de giz no traço (o fundo aparece por dentro da letra) |
| `textura` | só em `lousa` | pó de giz apagado no fundo |
| `imperfeicao` | `1.0` | quanto tremem caixas, setas, riscos e desenhos: `0` = limpo, `1` = padrão, `1.6` = bem torto |
| `semente` | `7` | outra semente = outra "caligrafia" com o mesmo conteúdo; a mesma semente repete a imagem |
| `peso` | `1.0` | engrossa a letra (`0` = fonte pura, `2` = bem gorda) |
| `largura`, `altura` | `1920`, `1080` | tamanho da imagem |
| `fonte` | Permanent Marker | caminho de outra fonte `.ttf` (relativo ao JSON) |
| `endireitar` | `0.16` (fonte padrão) | corrige a inclinação da fonte (`0` = como a fonte vem) |

## 3. Elementos

Todo elemento aceita `id` (para ser alvo de outro), `imperfeicao` e `peso` próprios.
Cor: `amarelo`, `ciano`, `branco`, `laranja`, `verde`, `vermelho` (as do padrão X8), mais `azul`, `rosa`, `roxo`,
`cinza` ou `#RRGGBB`.
`riscar`, `caixa`, `circular`, `sublinhar` e `seta` precisam vir **depois** do elemento que apontam.
Setas e linhas são sempre desenhadas por último (para encostarem nas caixas e nos riscos já feitos).

### `titulo`
Igual a `texto`, com outros padrões: `x` 40, `y` 24, `tamanho` 44, `cor` amarelo e sublinhado à mão embaixo
(`"sublinhado": false` tira; `espessura_sublinhado` 3.4). Não detecta lista (um título "1. …" fica como está).

### `subtitulo`
Igual a `texto`, com `tamanho` 40 e `cor` ciano, sem sublinhado (`"sublinhado": true` põe).

### `texto`
| campo | padrão | |
|---|---|---|
| `texto` | — | `\n` quebra linha; `{cor:trecho}` pinta um trecho; `[ENTER]` = tecla da HP12C em caixinha; `→ ← ↑ ↓ ↗ ↘` viram setinhas desenhadas; ✅ ❌ ⚠️ viram desenho; `≥ ≤ ≠` viram `>= <= =/=` |
| `x`, `y` | — | canto superior esquerdo do bloco (`y` = topo das maiúsculas). Aceitam `"centro"` |
| `largura` | sem quebra | largura máxima da linha; **sem ela o texto não quebra** |
| `tamanho` | 36 | tamanho da letra em px (mínimo 28) |
| `cor` | branco | |
| `alinhar` | esquerda | `esquerda`, `centro`, `direita` (dentro de `largura`) |
| `entrelinha` | 1.38 | distância entre linhas = tamanho x entrelinha (o molde usa ~1.6) |
| `espacamento` | 0.1 | espaço extra entre letras (fração da largura da letra) |

| `lista` | `true` | detecta os marcadores de lista abaixo; `false` desliga |
| `maiusculas` | da lousa | caixa alta neste elemento |

**Listas (padrão X8, sem tabela):** cada linha (parágrafo) pode começar com:
- `1. ` (ou `1) `) → número dentro de circulinho desenhado; as linhas seguintes ficam recuadas;
- `- ` ou `• ` → tópico com bolinha;
- 2 espaços antes do marcador → subtópico (tracinho); 4 espaços → subitem.

**Teclas da HP12C:** `[f] [REG] [ENTER] [÷] [×] [−] [CHS] [Σ+] [g] [x̄] [s]` viram caixinhas com o rótulo em caixa
alta numa letra de mão mais limpa (Pangolin), para G e S não parecerem 6 e 5. Números digitados (1,10; 100) ficam
fora da caixinha; o dígito depois de `f` (casas decimais) vai em caixinha: `[f] [2]`. Use `entrelinha` ~1.55
nas linhas com teclas.

### `caixa`
Moldura tremida em volta do `alvo` (ou da área `x`, `y`, `largura`, `altura`).
`margem` 30 · `espessura` 5.5 · `cor` amarelo (padrão X8; "quadro vermelho" do roteiro → `"cor": "vermelho"`).

### `circular`
Contorno em volta do `alvo`: elipse em blocos curtos; "cápsula" (pílula) em frase comprida.
`margem` 22 · `espessura` 5 · `cor` amarelo.

### `riscar`
`estilo` `"x"` (padrão: X grande passando do texto, como no molde) ou `"linha"` (um risco em cada linha).
`margem` 38 · `espessura` 4.2 · `cor` vermelho (errado).

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
Nomes (lista com desenho: `assets/exemplos/desenhos.png`): alvo, ampulheta, balanca, balanca_peso, balao, banco, carro, casa, check, cofrinho, dinheiro, estrela,
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

- **Cantos livres (padrão X8):** nada em x ≥ 1560 com y ≤ 190 (logo X8) nem em x ≥ 1600 com y ≥ 760 (webcam).
  O `--grade` desenha as duas áreas em rosa e o gerador avisa quem invadir.
- Título em y 24–90. Conteúdo de y ~140 a 1040; acima de y 190 só até x 1560; abaixo de y 760 só até x 1600.
- Duas colunas: x 80–900 e x 1060–1840 (comece a coluna da direita em y ≥ 200 se ela passar de x 1560).
- Tamanhos: título 40–46 · subtítulo 36–42 · texto 30–38 · **mínimo 28**.
- Regra de bolso em caixa alta (`espacamento` 0.1), caracteres por 800 px de largura:

| tamanho | caracteres / 800 px | altura da linha (1.38) |
|---|---|---|
| 28 | 42 | 39 |
| 32 | 37 | 44 |
| 36 | 33 | 50 |
| 44 | 27 | 61 |
| 56 | 21 | 77 |

- Altura do bloco ≈ 0.75 x tamanho + (linhas − 1) x tamanho x entrelinha + 0.2 x tamanho.

## 6. Moldes de layout

Use como ponto de partida e ajuste as coordenadas ao tamanho real do texto (confira com `--grade`).
Exemplo completo no padrão X8, uma aula inteira: `aulas-certificacoes/materiais/cpro-r/lousas/r53-perfil-carteira-indicadores/r53-lousas.json`
(abertura mito × verdade, metáfora em 4 estações, lista com circulinhos + quadro, 2 colunas, laudo → receita,
pegadinhas em quadro vermelho, dados do exercício e 3 lousas de HP12C com teclas).

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
