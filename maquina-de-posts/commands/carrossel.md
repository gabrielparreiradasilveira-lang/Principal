---
description: Gera um carrossel completo de Instagram (PNGs 1080x1350) a partir de um tema, ideia, link ou transcrição
argument-hint: [tema]
---

# /carrossel — Linha de Produção Estratégica

Este comando transforma um tema, ideia, link ou transcrição em um carrossel pronto para postar.

Tema recebido: $ARGUMENTS

Você segue uma sequência lógica de dependências. Não avance para uma fase sem concluir a anterior, verificar os arquivos no disco e respeitar as aprovações pedidas.

---

## FASE 1: Contexto e identidade

1. Leia obrigatoriamente:
   - `${CLAUDE_PLUGIN_ROOT}/skills/maquina-de-posts/SKILL.md`
   - `${CLAUDE_PLUGIN_ROOT}/skills/maquina-de-posts/references/direcao-de-arte.md`
   - `marca/perfil.md`
   - `pesquisa/instagram-framework.md` (se não existir no projeto, use `${CLAUDE_PLUGIN_ROOT}/skills/maquina-de-posts/references/instagram-framework.md`)
2. **Pergunte sempre qual identidade visual usar, antes de qualquer outra ação:**
   > Qual identidade você quer neste carrossel: **azul** (dark navy, Poppins, estilo educacional) ou **dourada** (preto e ouro, serifada editorial, estilo premium)?

   Use a ferramenta de perguntas, se disponível. Nunca assuma a escolha nem reaproveite a do carrossel anterior. Leia `marca/sistema-visual-azul.css` ou `marca/sistema-visual-dourado.css` conforme a resposta, e use só essa identidade do início ao fim.
3. Se a marca não estiver configurada, pare e conduza o usuário para `/começar`.

---

## FASE 2: Estratégia Editorial, Copy e Aprovação

Antes de criar qualquer HTML, defina a estratégia do carrossel.

### Decisões obrigatórias

- **Tese central:** o que este carrossel defende.
- **Tensão real:** qual dor, erro, desejo ou contradição merece ser explicada.
- **Promessa:** o que a pessoa entende ou ganha ao chegar no fim.
- **Público:** para quem o carrossel está falando.
- **Ângulo próprio:** qual leitura torna este conteúdo específico, humano ou original.
- **Arco:** como a ideia evolui do contexto para a aplicação.
- **CTA:** uma ação final clara, sem dispersão.
- **Ritmo visual:** quais slides são densos e quais sintetizam.

### Planejamento de slides

Monte um plano com 6 a 9 slides, salvo se o tema claramente pedir outro tamanho.

Cada slide precisa ter uma função editorial. Planeje a ideia que será desenvolvida, não só a frase que aparecerá em destaque.

Mostre ao usuário o planejamento neste formato:

```text
Tese:
Promessa:
Ângulo próprio:

Slide 1 — [função editorial] | [ideia-matriz] | [desenvolvimento em 2-4 linhas] | [layout]
Slide 2 — [função editorial] | [ideia-matriz] | [desenvolvimento em 2-4 linhas] | [layout]
...
Slide final — [síntese] | [CTA conectada à tese] | [layout]
```

Use o `pesquisa/instagram-framework.md` como metodologia editorial: carrossel denso, escaneável, útil, com ponto de vista e desenvolvimento real.
Use a skill `humanizer` como revisão de linguagem: aplique a lógica de humanização na copy dos slides antes de criar o HTML, mantendo apenas a versão final no carrossel.

**BLOQUEIO:** pergunte:

> Posso montar os slides a partir desse plano?

Aguarde aprovação antes de continuar.

---

## FASE 3: HTML e Renderização

1. Crie um HTML por slide em `output/carrossel-[slug]/`.
2. Use 1080x1350.
3. Mantenha o conteúdo crítico dentro da área central 1080x1080.
4. Nunca use emojis.
5. Se `marca/foto.*` existir, use `src="__FOTO_PERFIL__"` no slide 1 e no último.
6. Use as regras de `references/direcao-de-arte.md`.
7. A copy deve seguir o planejamento aprovado: frase-matriz em destaque, desenvolvimento escaneável e exemplos quando fizer sentido.

### Rota Tipográfica

- Use tipografia massiva, hierarquia clara e contraste forte.
- Use textura sutil, grid/dots e linhas de acento.
- Use geometria minimalista para representar conceitos.

Renderize cada slide:

```bash
node ${CLAUDE_PLUGIN_ROOT}/scripts/renderizar.js output/carrossel-[slug]/slide-0X.html output/carrossel-[slug]/slide-0X.png
```

Se o Puppeteer não estiver instalado no projeto, rode `/começar` primeiro (ou `npm install puppeteer@^22.15.0`).

---

## FASE 4: Verificação Final

Antes de finalizar, verifique:

1. PNGs existem em `output/carrossel-[slug]/`.
2. Todos os slides esperados foram renderizados.
3. O slide 1 tem impacto imediato.
4. O texto está legível em mobile.
5. A sequência tem ritmo: abertura, contexto, desenvolvimento, síntese e CTA.
6. Os slides do meio entregam conteúdo real, com exemplos, contexto ou aplicação.
7. A identidade da marca foi respeitada.

Finalize informando:

- pasta final
- quantidade de slides
