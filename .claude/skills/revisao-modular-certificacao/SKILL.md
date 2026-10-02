---
name: revisao-modular-certificacao
description: Cria a revisão de um MÓDULO INTEIRO de certificação financeira (CPA, C-PRO-R, C-PRO-I, CFP, CGA, CGE etc.) como roteiro de aula ao vivo de 15–30 min com os pontos que mais caem na prova, conferindo números nas aulas já feitas, na apostila e nas normas oficiais; depois pergunta se deve transformar a revisão em manual do aluno em PDF A4 com a identidade visual da X8 Educação (ou de um PPTX anexado). Use sempre que o professor pedir "revisão do módulo", "resumo do módulo para aula ao vivo", "aulão de revisão", "o que mais cai no módulo X", "manual de revisão", "apostila resumo do módulo" ou quiser revisar vários itens do Programa Detalhado de uma vez, mesmo sem usar a palavra "revisão".
---

# Revisão modular de certificação → roteiro ao vivo → manual do aluno

Duas entregas, nesta ordem:
1. **Roteiro de fala ao vivo** do módulo inteiro (para o professor).
2. **Manual do aluno** em PDF, **só se o professor aceitar** quando você perguntar ao fim da fase 1.

O processo nasceu da revisão do Módulo 2 da CPA. Os modelos aprovados estão no repositório:
- roteiro: `aulas-certificacoes/roteiros/cpa/revisao-modulo-2-produtos-fala.md`
- manual: `aulas-certificacoes/materiais/cpa/manual-revisao-modulo-2/` (`manual.html` + PDF)

Antes de tudo, leia `aulas-certificacoes/CLAUDE.md` (regras do projeto: escopo pelo PD, nada inventado, referências com status, questões inéditas). Esta skill não substitui essas regras; ela as aplica a uma revisão de módulo.

---

## Fase 1 — Roteiro de revisão do módulo

### Passo 1. Mapear o módulo

- Identifique certificação e módulo (pergunte se faltar).
- Liste no `PD-{CERT}.txt` **todos** os itens de 2º e 3º nível do módulo e o peso do módulo na prova (`00-fontes/apostilas/INDICE.md` tem o peso e as páginas da apostila).
- Inventarie o que já existe em `aulas/{cert}/aula-{N}.*`: cada aula pronta já tem números conferidos (quadro de emergência e tabela "Correções feitas na fonte"). Extraia os quadros de uma vez (comando em `references/roteiro.md`, seção 5).
- Separe os itens em **cobertos por aula** e **sem aula** (estes virão da apostila + norma).

Por que: a revisão herda a conferência já feita; o esforço novo vai só para o que nunca foi conferido.

### Passo 2. Perguntar antes de escrever (AskUserQuestion, uma rodada)

Pergunte, com a opção recomendada primeiro:
- **Duração:** 30 min (recomendado) · 20 · 15.
- **Itens sem aula conferida** (cite quais): apostila + conferir números na norma (recomendado) · só o já conferido · aguardar PDFs do professor.
- **Formato:** roteiro de fala ao vivo com [TELA]/[FALE]/[PEGADINHA] (recomendado) · padrão 7 etapas condensado · quadro de revisão.
- **Questões:** 3 rápidas, uma por nível (recomendado) · 1 · nenhuma.

Se o professor já decidiu algo antes na conversa (ex.: "IOF câmbio: apostila como resposta de prova + ressalva"), aplique a decisão sem perguntar de novo.

### Passo 3. Conferir o que não foi conferido

Para cada item sem aula: leia o trecho da apostila e confira **todo número, prazo, alíquota e percentual** na fonte oficial (BCB/CMN via API, Planalto, CVM — como acessar em `references/roteiro.md`, seção 5). Registre:
- divergência apostila × norma → tabela "Correções e ressalvas";
- norma alterada recentemente (ex.: prazos de LCI/LCA de 2025, MP que caducou) → nota de atualização;
- o que não conseguiu abrir → "não confirmado nesta sessão" (nunca preencher de memória).

Se aparecer uma divergência que muda a resposta de prova e não há decisão anterior, pergunte ao professor antes de escolher.

### Passo 4. Escrever o roteiro

Siga o esqueleto e as regras de `references/roteiro.md`. O essencial:
- cabeçalho, identificação, cronograma (soma = duração), tabela de correções;
- blocos por afinidade de itens do PD, cada um com **[TELA]** (tabela com números) → **[FALE]** (fala curta) → **[PEGADINHA]** → **Frase de fixação**;
- questões inéditas A–D com gabarito de todas as alternativas;
- fechamento com quadro de emergência do módulo e frase central;
- referências oficiais com `Último acesso` e status.

Salve em `aulas-certificacoes/roteiros/{cert}/revisao-modulo-{N}-{tema-curto}-fala.md`.

### Passo 5. Entregar a fase 1

1. `git add` só o roteiro; `git diff --cached` com grep de e-mail/CPF; commit com a mensagem em português e as linhas de atribuição da sessão; push para o branch de trabalho.
2. Envie o arquivo com SendUserFile.
3. Resposta curta: o que cobre, o que foi conferido e onde, correções encontradas, o que ficou "não confirmado".

### Passo 6. Perguntar sobre o manual

Termine a fase 1 perguntando (AskUserQuestion) se quer transformar a revisão em **manual do aluno**, nos moldes do manual do Módulo 2 da CPA. Se a resposta for sim, faça na mesma pergunta (ou na seguinte) as escolhas de produção:
- **Formato:** PDF A4 retrato (o modelo aprovado) · PPTX 16:9 · Canva (exige conector autorizado).
- **Conteúdo:** só o que serve ao aluno (recomendado) · também as ressalvas · questões em arquivo separado.
- **Marca:** X8 com rodapé "X8 Educação · Revisão {CERT} — Módulo {N}" (recomendado) · X8 com os @ · outro design (pedir o PPTX).
- **Tamanho:** ~24 páginas (um tema por página, temas grandes em duas) · ~16 · ~10.

Se não quiser, encerre.

---

## Fase 2 — Manual do aluno

Leia `references/manual.md` e siga-o. Em resumo:

1. **Transformar, não copiar:** tire tempos, [TELA]/[FALE] e notas internas; ressalvas só viram "Fique de olho" se mudam a resposta do aluno; dado incerto sai.
2. **Reconferir números** contra as aulas e normas ao reescrever — o roteiro pode ter imprecisões (na primeira vez apareceram três).
3. **Montar o HTML** a partir de `assets/manual-x8/template.html` + `manual.css` (Poppins e ícones X8 já inclusos). Se houver PPTX novo, extraia o design como descrito na seção 4 do reference.
4. **Renderizar e checar:** `scripts/render_pdf.js` (falha se algo transborda) e `scripts/preview_grid.py` (grades para olhar todas as páginas). Corrija e renderize de novo até não haver transbordo nem quebra feia. Confira o sumário com as páginas reais.
5. **Entregar:** salvar em `aulas-certificacoes/materiais/{cert}/manual-revisao-modulo-{N}/` (HTML, css, fonts, img, PDF), commit + push, SendUserFile com `display: render`, e resumo do que foi corrigido na conferência e do que ficou para decisão do professor.

---

## Tom das respostas ao professor

Português, direto, sem formalidades (preferência do Gabriel). Liste correções e pendências em tópicos; não repita o conteúdo inteiro do arquivo na conversa.
