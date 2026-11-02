---
name: lousa-manuscrita
description: Gera imagens de LOUSA ESCRITA À MÃO (PNG 1920x1080, fundo preto ou lousa verde com giz) para usar como fundo de slide, no molde do professor Gabriel — título amarelo sublinhado, texto em letra de pincel com tremor e imperfeições, mito em vermelho riscado com X, verdade em verde dentro de caixa tremida, setas e desenhos-âncora (carro, balão, termômetro, alvo, cofrinho, balança…). Use sempre que o professor pedir "lousa", "imagem de lousa", "quadro", "fundo de slide estilo lousa", "slide escrito à mão", "desenho à mão", "estilo Excalidraw/quadro-negro", "mito x verdade em imagem", ou quiser transformar um tópico, roteiro ou fala de aula em lousas prontas — mesmo sem usar a palavra "lousa". Também gera várias lousas de uma vez e junta num .pptx.
---

# Lousa manuscrita → imagem de fundo de slide

Entrega: PNG(s) 1920x1080 que parecem escritos à mão (de propósito imperfeitos: letras tortas, linhas que tremem,
cantos que passam do ponto, círculos que não fecham). Opcional: um `.pptx` com uma imagem por slide.

Molde aprovado pelo professor: `assets/exemplos/mito-x-verdade.json` → `assets/exemplos/mito-x-verdade.png`.
Desenhos prontos: `assets/exemplos/desenhos.png` (ou `python3 scripts/lousa.py --desenhos`).

Requisito: Python 3 + Pillow (`pip install pillow`; para `--pptx`, também `python-pptx`).
Todos os caminhos abaixo são relativos à pasta desta skill (no repositório: `.claude/skills/lousa-manuscrita/`).

## Passo 1. Entender o conteúdo

- Tema, item do Programa Detalhado (se for aula de certificação), quantas lousas e o que vai em cada uma.
- Se o professor só deu o tema, proponha o conteúdo de cada lousa em 1 linha e siga; pergunte só se faltar
  algo que mude o resultado (ex.: qual é o mito a ser derrubado).
- **No projeto `aulas-certificacoes/`, as regras de `aulas-certificacoes/CLAUDE.md` valem também na lousa:**
  nada de número, prazo, alíquota ou norma de memória — use o que já foi conferido na aula/roteiro ou na fonte
  oficial; banca de referência Cesgranrio/ANBIMA. Se o dado não estiver confirmado, deixe-o fora da lousa e avise.

## Passo 2. Planejar cada lousa (didática para TEA/TDAH)

- **Uma ideia por lousa.** No máximo ~35 palavras. Lousa é fundo de fala, não apostila.
- **Código de cores fixo** (previsibilidade ajuda TEA):
  | cor | uso |
  |---|---|
  | `amarelo` | título (com item do PD) e destaque de 1–2 palavras |
  | `vermelho` | mito, erro, pegadinha — vem riscado (`riscar`) |
  | `verde` | regra certa, verdade, frase de fixação — vem em `caixa` |
  | `branco` | setas, conectores, texto neutro |
  | `azul` | definição técnica |
  | `laranja` | analogia do cotidiano |
  | `rosa` | alerta de prova (com o desenho `exclamacao`) |
- **Um desenho-âncora por lousa** que materialize a analogia (juros = freio → `carro`; inflação = balão → `balao`;
  meta de inflação → `alvo`; reserva → `cofrinho`; equilíbrio → `balanca`; prazo → `ampulheta`).
- Escolha o molde de layout em `references/formato.md` (seção "Moldes de layout"): mito × verdade, causa → efeito,
  comparação em 2 colunas, conceito + analogia, pegadinha de prova.

## Passo 3. Escrever o roteiro JSON

Formato completo, tamanhos recomendados e grade da tela em `references/formato.md`. O essencial:

```json
{
  "saida": "lousa-01.png",
  "fundo": "preto",
  "elementos": [
    {"tipo": "titulo", "texto": "POLÍTICA MONETÁRIA (cpa 1.2.4)"},
    {"tipo": "texto", "id": "mito", "texto": "\"Selic alta ajuda o crédito\"", "x": 80, "y": 340, "largura": 760, "cor": "vermelho"},
    {"tipo": "riscar", "alvo": "mito"},
    {"tipo": "texto", "id": "certo", "texto": "Selic alta {amarelo:encarece} o crédito", "x": 1030, "y": 350, "largura": 520, "cor": "verde"},
    {"tipo": "caixa", "alvo": "certo"},
    {"tipo": "desenho", "nome": "carro", "abaixo_de": "certo", "distancia": 50, "largura": 210, "cor": "verde"},
    {"tipo": "seta", "de": "mito", "para": "certo"}
  ]
}
```

- Letra minúscula sai em **versalete** (caixa-alta menor); maiúscula sai maior — "Cenário" fica com o C grande,
  como no molde. Use isso para dar ênfase sem mudar de cor.
- `{amarelo:palavra}` muda a cor de um trecho. `→ ← ↑ ↓` viram setinhas desenhadas. `\n` quebra a linha.
- Posicione por `x`/`y` ou relativo a outro elemento (`abaixo_de`, `direita_de`…); `"x": "centro"` centraliza.
- Um elemento que aponta para outro (`riscar`, `caixa`, `seta`…) precisa vir **depois** dele.
- Onde salvar no repositório: `aulas-certificacoes/materiais/{cert}/lousas/{aula-ou-tema}/` (roteiro `.json` + PNGs
  juntos). Fora do repositório: a pasta de trabalho atual.

## Passo 4. Gerar e conferir (obrigatório antes de entregar)

```bash
python3 scripts/lousa.py caminho/roteiro.json --grade
```

1. Leia a saída: cada elemento com sua caixa (x, y) e os avisos `⚠` (sai da borda, sobreposição, letra pequena,
   caractere que a fonte não tem, texto demais).
2. **Abra o PNG gerado** (ferramenta de leitura de imagem) e o `*_grade.png` (grade de 100 px + caixa de cada id).
   Procure: texto cortado ou encostado na borda, seta atravessando texto, desenho em cima de texto, quebra de linha
   feia, lousa poluída.
3. Corrija no JSON e gere de novo até não sobrar aviso de borda/sobreposição. Apague os `*_grade.png` antes de
   entregar (são só para conferência).

## Passo 5. Entregar

- PNG(s) + o roteiro `.json` (para o professor pedir ajustes depois). Com várias lousas, use um único JSON com
  `"slides": [...]` e, se ele quiser, `--pptx aula.pptx`.
- Como usar como fundo: PowerPoint → Design → Formatar Plano de Fundo → Preenchimento com imagem → Inserir
  (o nome do menu varia por versão); Google Slides → Slide → Alterar plano de fundo → Escolher imagem.
- Variações sem mudar o conteúdo: `"semente"` diferente = outra "caligrafia"; `"imperfeicao"` 0.6 (mais limpa)
  a 1.6 (mais torta); `"fundo": "lousa"` = lousa verde com falhas de giz; `"peso"` 0 a 2 = letra mais fina/grossa.

## Erros comuns

- `id 'x' não existe` → o alvo está depois no roteiro ou o id foi digitado diferente.
- Texto saindo da tela → falta `largura` (sem ela o texto não quebra linha) ou `x` grande demais.
- Frase muito comprida dentro de `circular` → vira "cápsula" automaticamente; se ainda poluir, prefira `caixa`.
- Precisa de um desenho que não existe → use `livre` (pontos do traço) ou acrescente em `scripts/desenhos.py`
  (instruções no topo do arquivo).
