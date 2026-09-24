# Projeto aulas-certificacoes — regras para o agente

Toda aula criada nesta pasta segue **integralmente** o `PROMPT_MESTRE_CERTPASS.md` (Agente CertPass).
Leia esse arquivo antes de produzir qualquer aula, questão, roteiro ou slide.

## Regras críticas (resumo — o prompt mestre prevalece)

1. **Escopo:** tópicos só do Programa Detalhado ANBIMA da certificação + planilha de planejamento. Sem PD/planilha disponível → avisar; nunca declarar alinhamento não conferido.
2. **Sequência obrigatória:** 1. Abertura → 2. Metáfora → 3. Tópicos do PD → 4. Por que cai na prova → 5. Case → 6. Questão comentada → 7. Revisão final.
3. **Nada inventado:** números, percentuais, prazos, classificações, normas, links. Pendência → `Status: não confirmado — verificar na fonte oficial indicada.`
4. **Referência normativa:** `Órgão — tipo do ato — número — data — título resumido — link direto — último acesso: AAAA-MM-DD`, com status (em vigor / revogada / alterada / consulta pública / prática de mercado).
5. **Questões:** inéditas, nunca cópia de questão real; gabarito com justificativa de todas as alternativas.
6. **Não gerar artefatos não solicitados** (slides, roteiro, lousa só quando pedidos).
7. Português do Brasil; linguagem linear, previsível e visual (público inclui TEA/TDAH).

## Fontes de consulta disponíveis

- **Programas Detalhados ANBIMA** (versão 1.2, rev. 04/06/2025, vigência a partir de 01/01/2026):
  `00-fontes/programas-detalhados/` — CPA, C-PRO-I, C-PRO-R (PDF + `.txt` para busca + `INDICE.md`).
  São a **fonte de conhecimento base** de todo material criado (aulas, questões, roteiros, slides):
  - definem **escopo, ordem e redação dos tópicos** — títulos das seções 3.X seguem a redação do PD;
  - antes de escrever, ler no `.txt` o item completo até o último subitem e cobrir **todos** eles;
  - todo bloco da aula cita o item do PD (ex.: `CPA 1.2.4.2`);
  - o PD lista *o que* ensinar; o *conteúdo técnico* (definições, números, normas) vem das apostilas
    e de fontes oficiais (ANBIMA, CVM, BCB, CMN, RFB etc.), conforme a seção 4 do prompt mestre.
- **Apostilas CPA, C-PRO-I, C-PRO-R** (rev. mar–abr/2026): `00-fontes/apostilas/` (PDF + `.txt` + `INDICE.md`).
  São a **fonte de conhecimento principal do conteúdo técnico**: definições, mecanismos, exemplos e números.
  - localizar o trecho pelo `.txt` (`<<<PÁGINA N>>>` = página do PDF) e citar a página na aula;
  - apostila **não substitui** o PD: tópico fora do PD não entra; tópico do PD ausente da apostila → fonte oficial;
  - normas, alíquotas, limites e prazos: conferir vigência na fonte oficial (a apostila pode estar desatualizada);
    divergência apostila × norma → prevalece a norma e a divergência é registrada em "Pendências de verificação".

### Hierarquia das fontes
1. **Programa Detalhado** → o que ensinar e em que ordem.
2. **Apostila** → como explicar (conteúdo técnico base).
3. **Norma/órgão oficial** → validação de números, regras e vigência.

## Checagem obrigatória antes de cada entrega (pedido do professor)

1. Listar os subitens do PD informados no pedido (ou extraídos do `PD-*.txt`).
2. Conferir **subitem por subitem** se os PDFs enviados cobrem o conteúdo; conferir também a apostila.
3. **Informar ao professor** antes de escrever: o que falta nos PDFs, o que está desatualizado ou errado,
   e o que está no material mas fora do PD — e **perguntar como proceder** (completar pela norma/apostila,
   aguardar PDF, incluir como nota, retirar).
4. Novidades normativas ou de produto fora do PD (ex.: título novo) entram só como **nota de atualização**,
   salvo decisão contrária do professor.

## Formato de saída (padrão de entrega)

Toda aula entregue segue o formato de
`modelos/REFERENCIA-aula-cpa-1.1.4-1.1.5-autorreguladores-fgc-spb.md` (aula-referência aprovada),
com o esqueleto em `modelos/modelo-aula-7-etapas.md`. Em caso de dúvida de layout, tom ou densidade, **copie a referência**.

Características obrigatórias do padrão:
- Cabeçalho: `# Aula [CERT] — [Tema]` + linha `data · @Boss · Roteiro integrado · duração`.
- **Identificação e alinhamento** com: parágrafo de escopo (itens do PD + módulo), tabela **Checagem de escopo**
  (Subitem do PD | Fonte de origem | Tratamento), tabela **Cronograma** (tempo por etapa e por tópico)
  e tabela **Correções feitas na fonte** (# | Fonte | O material diz | O correto | Fonte oficial).
- Tempo em minutos no título de cada etapa e de cada tópico (`## 1. Fala de abertura — 3 min`).
- Abertura, metáfora e case em **blockquote** (`>`), como fala pronta.
- Metáfora com nome (`### Metáfora: o condomínio`) e tabela de correspondência técnica.
- Tópicos 3.X separados por `---`; subseções usadas: O que é · Como funciona · (Exemplo prático) ·
  O que a prova pode confundir · Frase de fixação · Alinhamento ao PD. Tabelas sempre que houver regras, números ou comparações.
- Frases de fixação em **negrito** dentro de blockquote.
- Questão: linha única `Certificação · Competência · Nível`; **4 alternativas (A–D)**; justificativa de cada incorreta.
- Revisão final com **Quadro de emergência em tabela** (Tema | Regra-chave).
- Fontes consolidadas no fim em **Referências oficiais e status** (lista numerada, `Último acesso`, status em negrito);
  o que não foi confirmado aparece como "não confirmado nesta sessão" — nunca inventado.
- Duração padrão: 30–40 min, salvo pedido diferente.

## Onde salvar

- Fontes recebidas (PDF, planilha, PD, normas): `00-fontes/`
- Aula: `aulas/<certificacao>/aula-NN-tema-curto/aula.md` (partir de `modelos/modelo-aula-7-etapas.md`)
- Questões adicionais: `questoes/<certificacao>/bateria-NN-tema-nivel.md`
- Roteiros de fala / lousa: `roteiros/<certificacao>/aula-NN-tema-curto-<fala|lousa>.md`
