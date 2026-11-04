---
name: lousa-manuscrita
description: Gera as LOUSAS das aulas do professor Gabriel (X8 Educação) no PADRÃO VISUAL X8 — PNG 1920x1080, fundo preto chapado, letra de mão em caixa alta reta, título amarelo sublinhado à mão, subtítulos ciano, números de lista em circulinhos, caixas/setas/desenhos com traço cru e imperfeito, teclas da HP12C em caixinhas, cantos livres para o logo e a webcam — a partir do roteiro da aula (Google Docs, arquivo do repositório ou texto colado). Use sempre que o professor pedir "lousa", "lousas da aula", "gerar as lousas do roteiro", "fundo de slide estilo lousa", "slide escrito à mão", "quadro", ou mandar um roteiro com blocos [Ação na Lousa] — mesmo sem usar a palavra "lousa". Também junta tudo num .pptx.
---

# Lousas da aula no padrão visual X8

Entrega: um PNG 1920x1080 por lousa (+ `.pptx` com uma lousa por slide, se pedido) e o roteiro `.json`
usado para gerar (para ajustes depois). Gerador: `scripts/lousa.py` (só precisa de Python 3 + Pillow;
`--pptx` precisa de `python-pptx`). Caminhos relativos à pasta desta skill (`.claude/skills/lousa-manuscrita/`).

## Padrão visual X8 (obrigatório — definido pelo professor)

| Regra | Como a skill cumpre |
|---|---|
| PNG 1920×1080, fundo preto chapado | padrão do gerador (`"fundo": "preto"`); não use `lousa`/`grafite` sem pedido |
| Letra de mão toda em CAIXA ALTA, reta e alinhada, sem ondular | automático (`maiusculas` e `tremor_texto: 0`); escreva o texto normal, ele sai em caixa alta |
| Cores chapadas, sem brilho/neon/sombra | paleta chapada; nada de efeito |
| Amarelo: títulos e molduras | `titulo` é amarelo; `caixa` e `circular` saem amarelos |
| Ciano: subtítulos | elemento `subtitulo` |
| Branco: texto corrido | `texto` é branco |
| Laranja, verde, vermelho: destaques (verde = certo, vermelho = errado/alerta) | `{laranja:trecho}`, `{verde:…}`, `{vermelho:…}`; `riscar` sai vermelho |
| Títulos com sublinhado à mão | automático no `titulo` |
| Números de lista em circulinhos | linha do `texto` que começa com `1. ` vira circulinho |
| Caixas, setas e desenhos com traço cru e imperfeito | automático (`imperfeicao` 1.0) |
| Fonte mínima 28 px | aviso abaixo de 28; teclas nunca abaixo de 28 |
| Cantos livres: logo X8 (x ≥ 1560 e y ≤ 190) e webcam (x ≥ 1600 e y ≥ 760) | aviso se algo invadir; `--grade` mostra as duas áreas em rosa |
| Sem tabela com grade: tópicos, subtópicos, subitens | `- ` tópico (bolinha); 2 espaços + `- ` subtópico (tracinho); 4 espaços subitem |
| Teclas da HP12C em caixinhas, vírgula decimal, ponto de milhar | `[ENTER]` vira tecla; aviso para ponto decimal e número sem ponto de milhar |
| Emojis viram desenho; sem sobras de LaTeX | ✅ → check verde, ❌ → X vermelho, ⚠️ → triângulo; aviso se aparecer `\frac`, `$…$` etc. |
| Títulos curtos, os do roteiro; só criar título quando o roteiro não tem | regra de processo (Passo 2) |
| Nenhum texto de lousa do roteiro pode ser cortado | regra de processo (Passo 2): se não couber, divida em mais lousas |

## Passo 1. Ler o roteiro

- Google Docs: ler pelo conector do Google Drive (`read_file_content` com o id do link). Arquivo do repositório:
  ler direto. Texto colado: usar como está.
- Cada bloco **[Ação na Lousa]** vira uma lousa (ou mais, se não couber). Liste para o professor o plano:
  lousa → bloco do roteiro → título.
- Tabela de teclas da HP12C (mesmo se estiver na locução): vira lousa(s) em tópicos, passo a passo, com as
  teclas em caixinhas — sem grade. Avise o professor que essas lousas foram montadas a partir da tabela.
- Projeto `aulas-certificacoes/`: as regras do `aulas-certificacoes/CLAUDE.md` valem (nada inventado). A lousa
  só usa o texto e os números do roteiro.

## Passo 2. Montar cada lousa (regras de conteúdo)

- **Texto integral.** Todo texto que o roteiro manda escrever entra, palavra por palavra (pode virar tópicos:
  itens separados por `·` podem virar `- ` um embaixo do outro). Não resumir, não abreviar, não trocar palavras.
  Instruções para o professor ("Escreva no topo:", "Em vermelho:", "Duas colunas:", "Embaixo:") não são texto
  da lousa: viram cor, posição ou forma.
- **Títulos do roteiro.** Use o título que o roteiro manda escrever, como está. Só crie um título (curto) quando o
  bloco não tiver; se dividir um bloco em duas lousas, repita o título com `(1/2)`, `(2/2)`.
- **Não coube?** Diminua até o mínimo de 28 px ou divida em mais lousas. Nunca corte texto.
- **Cores com sentido:** subtítulo ciano; destaque laranja; certo verde; errado/alerta vermelho (mito riscado).
- **Desenho-âncora** só quando ajudar (a metáfora do roteiro primeiro); nada nos cantos livres.
- Layout útil: título em y 24–90; conteúdo de x 60 a 1880, mas **acima de y 190 só até x 1560** e **abaixo de
  y 760 só até x 1600**. Moldes de layout e tamanhos em `references/formato.md`.

## Passo 3. Escrever o roteiro JSON

Um único arquivo com `"slides": [...]`, uma lousa por item. Formato completo em `references/formato.md`.

```json
{"slides": [{"saida": "r53_03_perfil.png", "elementos": [
  {"tipo": "titulo", "texto": "1. O PERFIL NÃO É ESTÁTICO"},
  {"tipo": "subtitulo", "texto": "Sete gatilhos de mudança:", "x": 80, "y": 140},
  {"tipo": "texto", "id": "lista", "x": 80, "y": 215, "largura": 840, "tamanho": 34,
   "texto": "1. Fase de vida.\n2. Evolução do patrimônio."},
  {"tipo": "texto", "id": "regra", "x": 1010, "y": 240, "largura": 600, "tamanho": 32,
   "texto": "- {laranja:Perfil do cliente:} no máximo a cada {laranja:5 anos}"},
  {"tipo": "caixa", "alvo": "regra"},
  {"tipo": "texto", "id": "hp", "x": 80, "y": 700, "largura": 1400, "tamanho": 34,
   "texto": "- 1,10 [ENTER] 1,05 [÷] 1 [−] 100 [×] → visor {laranja:4,76}"}
]}]}
```

Onde salvar no repositório: `aulas-certificacoes/materiais/{cert}/lousas/{aula}/` (JSON + PNGs + PPTX).

## Passo 4. Gerar e conferir (obrigatório)

```bash
python3 scripts/lousa.py caminho/roteiro.json --grade
```

1. Zero aviso `⚠` antes de entregar (borda, sobreposição, canto livre, menos de 28 px, ponto decimal, LaTeX,
   glifo ausente). Avisos de ponto decimal em número de item do PD podem ser ignorados.
2. **Abra cada PNG** e o `*_grade.png`: texto cortado, seta invertida ou minúscula, desenho em cima de texto,
   quebra de linha no meio de expressão, algo nas áreas rosa.
3. **Confira o texto contra o roteiro**, bloco por bloco: nada faltando, nada resumido.
4. Apague os `*_grade.png`. Se pedido, gere o `.pptx`: `python3 scripts/lousa.py roteiro.json --pptx aula.pptx`.

## Passo 5. Entregar

PNGs + `.pptx` (se pedido) + o `.json`. No relato: quantas lousas, onde cada bloco foi parar, o que foi
dividido, os títulos criados e as lousas montadas a partir de tabela da HP12C.

## Erros comuns

- `id 'x' não existe` → o alvo vem depois no roteiro ou o id está diferente.
- Texto saindo da tela → falta `largura` (sem ela o texto não quebra).
- Seta invertida/minúscula entre dois blocos → falta espaço entre eles; afaste os blocos ou quebre o texto.
- Desenho novo → `livre` (pontos do traço) ou acrescente em `scripts/desenhos.py` (instruções no topo).

## Decisões do professor (03/11/2026) — valem para todo roteiro
1. **Uma lousa por bloco [Ação na Lousa].** Só divide em (1/2), (2/2) se nem 28 px couber depois de condensar.
2. **Palavras-chave, não texto corrido:** condensar o texto do roteiro em termos-chave e frases curtas, mantendo
   todo conceito, número e fórmula; a explicação fica na fala. No relatório, listar o que foi condensado.
3. **HP12C só se o [Ação na Lousa] pedir** (tabela de teclas que está só na locução não vira lousa).
4. **Montar com `molde`** (references/formato.md, seção 7): sem coordenadas à mão; uma renderização, conferência
   da prancha, entrega.
5. **Antes de desenhar, conferir o roteiro na apostila** e devolver uma lista curta de alertas técnicos.
6. **Sempre subir as lousas para o Drive ao concluir** (pedido de 04/11/2026). Depois do commit enviado:
   `python3 scripts/drive_doc.py <pasta-das-lousas> <sha>` gera o HTML; criar com o `create_file` do
   Google Drive (`contentMimeType` "text/html", título = linha `TITULO:`, `parentId` = pasta
   **Lousas — C-PRO R**, id `1lPnWusDWmEeJD0V2crINux4SAwPqTNLf`). O Google baixa cada PNG do GitHub
   (repositório público) e guarda dentro do Doc em 1920×1080. Conferir com `get_file_metadata`: o
   Doc pronto tem mais de 1 MB. Se a aula for refeita, criar um Doc novo e apagar o antigo só com o
   ok do professor. Motivo: o conector só recebe o arquivo dentro do comando, e um PNG não cabe.
7. **Não gerar `.pptx`** (pedido de 04/11/2026): a entrega é o Doc do Drive com as lousas embutidas (item 6),
   mais os PNGs e o `.json` no repositório. Só fazer `.pptx` se o professor pedir de novo, explicitamente.
8. **Roteiro em série (R49-1, R49-2…)**: uma pasta e um `.json` por aula, PNGs com o prefixo do vídeo
   (`r49-1_01_…`, `r49-2_01_…`), um Doc do Drive para a série inteira. As pegadinhas usam o título do roteiro
   ("⚠️ PEGADINHAS") e o número de itens que ele traz.
