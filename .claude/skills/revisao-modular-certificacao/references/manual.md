# Manual do aluno a partir da revisão — design X8 e produção do PDF

Modelo aprovado: `aulas-certificacoes/materiais/cpa/manual-revisao-modulo-2/`
(`manual.html` = fonte; `manual-revisao-cpa-modulo-2-x8.pdf` = entrega, 25 páginas A4).
Abra o `manual.html` do modelo para ver todos os componentes em uso real.

## Sumário
1. Do roteiro ao manual: o que entra e o que sai
2. Estrutura de páginas
3. Design X8 (tokens, fonte, ícones)
4. Usar outro design (PPTX anexado)
5. Produção e QA
6. Problemas conhecidos do ambiente

---

## 1. Do roteiro ao manual

O roteiro é para o **professor**; o manual é para o **aluno**. Transforme, não copie.

| Sai | Entra / vira |
|---|---|
| Tempos, cronograma, "[TELA]/[FALE]" | — |
| Tabela "Correções e ressalvas (para o professor)" | Só o que muda a resposta do aluno vira quadro **Fique de olho** |
| Notas internas "não confirmado nesta sessão" | Sai do texto; se o dado não é confiável, o dado também sai |
| [FALE] (fala corrida) | Bullets curtos, tabelas, cards e exemplos numéricos |
| [PEGADINHA] / Frase de fixação | Quadros **Pegadinha** e **Frase de fixação** |
| Quadro de emergência | Página "O módulo em uma página" |
| Questões + gabarito | Duas páginas: questões, depois gabarito (aluno responde antes de virar) |

**Reconfira os números ao transformar.** Na primeira vez, a conferência pegou erros do roteiro (ex.: "sem mínimo relevante" no Tesouro Direto → "sem valor mínimo desde 18/11/2024"; ETF/BDR com alíquota confusa). Compare cada número do manual com o quadro de emergência / correções da aula correspondente e corrija. Frases sem fonte ("o progressivo favorece renda baixa") saem ou viram a regra verificada.

## 2. Estrutura de páginas (≈24–25 páginas para um módulo de 40%)

1. Capa (logo grande, kicker, título, subtítulo, pílulas dos temas)
2. Como usar: 2 cards de número (peso do módulo, nº de temas), tabela-sumário (item · pergunta do cliente · páginas), legenda dos 3 quadros, método de estudo
3…n. Uma página por tema; temas grandes (fundos, renda variável, previdência, crédito) em 2 páginas
n+1. Quadro de emergência
n+2. Questões · n+3. Gabarito + cards Formação/Certificação/Carreira + nota de conferência

Cada página de conteúdo: header (logo + seção) · kicker com os itens do PD · h1-afirmação · lead · 1–2 tabelas · grid de cards · Pegadinha · Frase de fixação · rodapé.
Varie os componentes entre páginas (tabela, grid2/grid3, stat `.big`, `.flow`, chips, exemplo `.card.dark`).

**Sumário:** depois do PDF pronto, confira se as páginas da tabela batem com as páginas reais.

## 3. Design X8

Kit em `assets/manual-x8/`: `manual.css`, `template.html` (componentes com `{{placeholders}}`), `fonts/` (Poppins 300–800, woff2), `img/` (logo e ícones extraídos do PPTX X8).

| Token | Cor | Uso |
|---|---|---|
| `--bg` | #071020 | fundo de todas as páginas |
| `--bg2` | #0A1628 | cards escuros, notas |
| `--card` / `--card2` | #132A4E / #1A3260 | cards e linhas alternadas |
| `--line` | #22406E | bordas |
| `--blue` / `--blue2` | #2563EB / #3B82F6 | cabeçalho de tabela, bullets, ícones |
| `--gold` | #D4AF6A | kicker, pegadinha, gabarito |
| `--muted` / `--light` | #94A3B8 / #E8EDF5 | texto secundário / corpo |

| Ícone (`img/`) | Significado |
|---|---|
| image1 | logo X8 Educação (header e capa) |
| image2 | pessoa/executivo |
| image3 | cérebro → Frase de fixação |
| image4 | alvo |
| image5 | banco/instituição |
| image6 | moedas |
| image7 | gráfico de alta |
| image8 | maleta (carreira) |
| image9 | selo |
| image10 | foguete |
| image11 | medalha |
| image12 | roseta dourada (certificação) |
| image13 | capelo (formação) |
| image22 | montanha |
| image23 | bússola → Fique de olho |
| image28 | olho → Pegadinha |
| image29 | balança (tributação/regra) |

Rodapé padrão: `X8 Educação · Revisão {CERT} — Módulo {N}` + número da página. Não use os @ do PPTX original (havia possível erro de digitação "@x8.educao5"), salvo pedido.

## 4. Usar outro design (PPTX anexado)

1. `cp` o upload para o scratchpad e `chmod 644` (uploads vêm com permissão 600).
2. Texto: `pip install -q "markitdown[pptx]" defusedxml lxml` e `markitdown arquivo.pptx`.
3. Extrair o zip; em `ppt/slides/slideN.xml` coletar cores (`srgbClr val=`), fontes (`typeface=`), tamanhos (`sz=`) e fundo (`<p:bg>`); em `ppt/media/` ver logo e ícones (montar uma grade com PIL para enxergar).
4. Criar novo kit (css + img + fontes) copiando a estrutura de `assets/manual-x8/` e trocando os tokens. Fontes Google: `https://cdn.jsdelivr.net/npm/@fontsource/{familia}@5/files/{familia}-latin-{peso}-normal.woff2`.
5. Imagens com pessoas, QR codes e dados de contato do PPTX **não** entram no manual.

## 5. Produção e QA

```bash
SK=<pasta desta skill>; OUT=aulas-certificacoes/materiais/{cert}/manual-revisao-modulo-{N}
mkdir -p $OUT && cp -r $SK/assets/manual-x8/{manual.css,fonts,img} $OUT/
# escrever $OUT/manual.html a partir de template.html (link para manual.css)
NODE_PATH=$(npm root -g) node $SK/scripts/render_pdf.js $OUT/manual.html $OUT/manual-revisao-{cert}-modulo-{N}-x8.pdf
python3 $SK/scripts/preview_grid.py $OUT/manual-revisao-{cert}-modulo-{N}-x8.pdf <scratchpad>
```

- `render_pdf.js` sai com código 1 se alguma página transborda (folga < 0). Corrija: enxugue texto, divida em 2 páginas ou use `class="page tight"`.
- Folga muito grande (> ~230px em várias páginas) = páginas vazias demais; aumente fonte/espaçamento no CSS ou junte conteúdo.
- Olhe **todas** as grades geradas e uma página em 110 dpi: quebra feia de linha (ex.: chip "10%" caindo sozinho), ícone invisível, texto sem contraste.
- Antes do commit: `grep` no diff por e-mail/CPF; nunca commitar o PPTX do cliente.

## 6. Problemas conhecidos do ambiente

- LibreOffice (`soffice`) falha no sandbox com "source file could not be loaded" → não use para PDF; use Chromium/Playwright (`NODE_PATH=$(npm root -g)`, browsers em `/opt/pw-browsers`).
- `pptxgenjs` pode não estar instalado globalmente; o manual em HTML→PDF não precisa dele.
- GitHub raw dá 403 pelo proxy; jsDelivr funciona.
