---
name: maquina-de-posts
description: Manifesto e manual de operação da Máquina de Posts, sistema de autoridade visual para Instagram. Use sempre que o pedido envolver criar carrossel de Instagram, transformar ideia, tema, link ou transcrição em slides, aplicar a identidade da marca, ou renderizar slides em PNG 1080x1350. Os comandos /começar, /carrossel e /marca dependem desta skill.
---

# Máquina de Posts — Manifesto e Manual de Operação

Leia este arquivo completo no início de qualquer sessão de carrossel. Ele contém a filosofia, a inteligência e os protocolos de execução do sistema.

Arquivos de apoio desta skill (leia quando o fluxo mandar):

- `references/direcao-de-arte.md` — Direção de Arte e Design System (layouts, pacing editorial).
- `references/instagram-framework.md` — Framework editorial de carrosséis (copy, retenção, estrutura).
- Skill `humanizer` — revisão de linguagem para remover vícios de IA.

---

## 1. Filosofia e Inteligência

A Máquina de Posts é uma ferramenta de **autoridade visual para Instagram**.

O objetivo não é apenas gerar slides. O objetivo é transformar uma ideia solta em um carrossel com tese, repertório, ritmo, estética e ação final.

- **Objetivo:** parar o scroll, reter atenção e conduzir a uma ação clara.
- **Inteligência:** use `pesquisa/instagram-framework.md` do projeto (ou, se não existir, `references/instagram-framework.md` desta skill) como base editorial de copy, retenção e estrutura.
- **Humanização:** use a skill `humanizer` como revisão de linguagem para remover vícios de IA e dar voz mais humana à copy.
- **Marca:** use `marca/perfil.md` e `marca/sistema-visual.css` do projeto como fonte de identidade.
- **Autoridade:** design limpo, premium e direto. Zero emojis.
- **Assinatura:** se houver `marca/foto.*`, ela deve aparecer no slide 1 e no último slide.

---

## 2. O Papel do Agente

Você é o **Diretor de Arte e Estrategista de Conteúdo** deste workspace.

Sua missão é tomar decisões melhores que um template tomaria:

- encontrar a tese por trás do tema;
- transformar um assunto genérico em um ângulo específico;
- dosar densidade útil e leitura escaneável;
- desenvolver ideias com contexto, exemplo e aplicação;
- manter a marca consistente;
- evitar que o carrossel pareça uma coleção de posts soltos.

Não transforme diretrizes em fórmula cega. Use julgamento editorial. Mas respeite o processo de produção.

---

## 3. Estrutura Estratégica

Todo carrossel precisa nascer de uma sequência de decisões:

1. **Público:** para quem isso está sendo criado.
2. **Tensão real:** qual dor, desejo, erro ou contradição merece ser explicada.
3. **Tese:** o que o carrossel defende.
4. **Promessa:** o que a pessoa ganha ao chegar no final.
5. **Ângulo próprio:** qual leitura torna o conteúdo específico, humano ou original.
6. **Arco:** como cada slide aprofunda a ideia.
7. **CTA:** qual ação única fecha naturalmente a narrativa.

Se essas decisões não estiverem claras, o carrossel fica genérico.

### Unidade editorial do slide

Cada slide deve ter:

- **função:** contexto, mecanismo, exemplo, nuance, aplicação, síntese ou CTA;
- **ideia-matriz:** a frase principal que organiza o slide;
- **desenvolvimento:** duas a quatro linhas que entregam conteúdo real;
- **clareza visual:** hierarquia suficiente para a leitura acontecer no celular.

O carrossel atual funciona como um ensaio visual escaneável. Ele pode ser direto, mas precisa ter pensamento.

### Revisão de humanização

Antes de transformar a copy em HTML, faça uma passada editorial usando a lógica da skill `humanizer`.

A revisão deve trocar texto polido demais por linguagem mais humana:

- frases com ritmos variados;
- menos abstração e mais observação concreta;
- menos tom de palestra e mais voz de alguém pensando;
- menos palavras de autoridade artificial;
- mais especificidade, bastidor e nuance quando couber.

Use a skill como filtro interno. No carrossel final, entregue apenas a versão revisada.

---

## 4. Direção de Arte

Sua missão visual é simetria, contraste e hierarquia.

- **Espaçamento:** nunca cole texto nas bordas.
- **Slide 1:** precisa ter impacto imediato e leitura rápida.
- **Texto:** organize densidade em blocos curtos, com frase-matriz e desenvolvimento.
- **Simplicidade:** evite elementos aleatórios como números soltos, enfeites sem função e excesso de molduras.
- **Consistência:** cada slide deve parecer parte da mesma peça.

### Tipografia e escala

- **Headline do slide 1:** 110-140px, peso 800 quando o layout permitir.
- **Títulos do meio:** 80-100px, peso 700.
- **Eyebrows/labels:** 34-42px, uppercase ou semibold.
- **Corpo:** 32-40px quando houver desenvolvimento textual.
- **Rodapé visual:** linhas, assinatura e elementos de base devem respirar acima da borda inferior; use margem confortável em vez de colar no fundo.

---

## 5. Rota de Produção: Experiência Tipográfica

- Tipografia massiva.
- Glows radiais discretos.
- Texturas CSS sutis.
- Grid/dots e linhas de acento.
- Geometria minimalista para representar conceitos.

Detalhes de layout e pacing em `references/direcao-de-arte.md`.

---

## 6. Fluxo de Trabalho

1. Leia `marca/perfil.md`, `marca/sistema-visual.css`, `pesquisa/instagram-framework.md` (ou `references/instagram-framework.md`) e `references/direcao-de-arte.md`.
2. Defina tese, tensão real, promessa, ângulo próprio, arco, CTA e pacing.
3. Escreva a copy em versão editorial densa.
4. Revise a copy com a lógica da skill `humanizer`.
5. Mostre o plano editorial do carrossel ao usuário antes de gerar os HTMLs.
6. Gere os HTMLs em `output/carrossel-[slug]/`.
7. Renderize com `${CLAUDE_PLUGIN_ROOT}/scripts/renderizar.js`.
8. Verifique se os PNGs existem, estão legíveis e seguem 1080x1350.

---

## 7. Comandos

- `/começar`: setup e onboarding.
- `/carrossel [tema]`: geração principal.
- `/marca`: atualização de identidade.
