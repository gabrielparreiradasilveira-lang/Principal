# Máquina de Posts (plugin)

Plugin do Claude Code baseado no repositório `lukspit/CarrosseisAutom-ticos`, **sem** as partes de Telegram e Fal.ai.
Transforma tema, ideia, link ou transcrição em carrossel de Instagram: tese, copy editorial, identidade da marca e PNGs 1080x1350.

## Instalação

```bash
claude --plugin-dir /caminho/para/maquina-de-posts
```

Requisitos: Claude Code, Node.js 18+. O Puppeteer é instalado na pasta do seu projeto pelo `/começar`.

## Comandos

| Comando | O que faz |
|---|---|
| `/começar` (ou `/comecar`) | Instala o Puppeteer, coleta a marca (3 rodadas), gera `marca/perfil.md` e `marca/sistema-visual.css`, pesquisa de Instagram, foto de perfil |
| `/carrossel [tema]` | Estratégia, plano de slides com aprovação, HTMLs e PNGs 1080x1350 |
| `/marca` | Atualiza identidade, tom, nicho ou CTA sem refazer o setup |

Dentro do plugin, os comandos aparecem como `/maquina-de-posts:carrossel` etc. Se não houver conflito de nome, `/carrossel` também funciona.

## Skills

- `maquina-de-posts`: manifesto e manual de operação (CLAUDE.md original), com `references/direcao-de-arte.md` (AGENTS.md original) e `references/instagram-framework.md`.
- `humanizer`: revisão de linguagem para remover vícios de IA (v2.5.1, idêntica à original).

## Scripts

- `scripts/renderizar.js`: HTML para PNG 1080x1350. Injeta `marca/foto.*` no placeholder `__FOTO_PERFIL__` e embute imagens locais em base64.
- `scripts/renderizar-banner.js`: HTML para PNG com largura e altura customizadas.

Os dois leem `marca/` e o `node_modules` da pasta onde você roda o Claude Code (o projeto), não da pasta do plugin.

## O que foi removido em relação ao original

- `/entregar`, `scripts/entregar.js`, `scripts/bot.js` e a Fase de Telegram do `/começar`.
- `scripts/gerar-imagens-carrossel.js`, `FAL_KEY`, a Rota A (fotografia com Hero Fade, Split Lateral, Split Horizontal, Detalhe Editorial) e a engenharia de prompts de imagem. Resta a Rota Tipográfica (antiga Rota B).
- `config/.env.example` e `.claude/settings.json` (plugins não distribuem permissões).

## O que foi adaptado

- Caminhos `scripts/...` viraram `${CLAUDE_PLUGIN_ROOT}/scripts/...`; `CLAUDE.md` e `AGENTS.md` viraram skill e referência.
- Os scripts resolvem `marca/` e `puppeteer` a partir do diretório atual.
- Se o projeto não tiver `pesquisa/instagram-framework.md`, o `/carrossel` usa a cópia embutida no plugin.
- O "log" de checklist que o `/começar` gravava no `CLAUDE.md` foi removido; o estado continua sendo detectado pelos arquivos.

## Crédito e licença

Conteúdo derivado de https://github.com/lukspit/CarrosseisAutom-ticos, que não declara licença. Uso pessoal é seguro; para redistribuir, peça autorização ao autor. O `humanizer` é MIT (ver cabeçalho do SKILL.md).
