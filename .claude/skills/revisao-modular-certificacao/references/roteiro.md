# Roteiro de revisão ao vivo — estrutura e regras

Modelo aprovado: `aulas-certificacoes/roteiros/cpa/revisao-modulo-2-produtos-fala.md`.
Em dúvida de tom, densidade ou layout, abra o modelo e copie o padrão.

## Sumário
1. Esqueleto do arquivo
2. Como montar cada bloco
3. Distribuição de tempo
4. Questões
5. Fontes oficiais e como consultá-las
6. Checklist antes de salvar

---

## 1. Esqueleto do arquivo

```markdown
# Revisão ao vivo {CERT} — Módulo {N}: {Título do módulo no PD}

{Mon D, AAAA} · @Boss · Roteiro de fala ao vivo · {duração} min

## Identificação e alinhamento
Revisão do **Módulo {N} inteiro** do Programa Detalhado {CERT} (ANBIMA, vigência ...), que vale **{peso}% da prova**: {lista dos itens de 2º nível}.

**Como usar:** cada bloco tem **[TELA]** (o que escrever ou projetar), **[FALE]** (fala pronta e curta) e **[PEGADINHA]** (o erro que a banca usa). Siga a ordem; os tempos somam {duração} min.

**Bases:** aulas já conferidas ({lista}); APOSTILA-{CERT} p. {x–y} para itens sem aula; normas reabertas nesta sessão ({lista}).

### Cronograma
| Bloco | Tema | PD | Tempo |   ← soma exata = duração
### Correções e ressalvas (para o professor)
| # | Fonte | O material diz | O correto | Fonte oficial |

---
## 0. Abertura — 1 min
## 1. {Tema} — {n} min
...
## {k}. Questões rápidas — {n} min
## {k+1}. Fechamento — 1 min   (quadro de emergência do módulo inteiro + frase central)
## Referências oficiais e status
```

## 2. Como montar cada bloco

Ordem fixa dentro do bloco:

1. **[TELA]** — tabela ou bloco de código curto com os números e regras. É o que o aluno copia.
2. **[FALE]** — 3 a 6 frases em blockquote (`>`), fala pronta, linguagem simples, uma ideia por frase.
3. **[PEGADINHA]** — uma frase entre aspas como a banca escreveria + **Errado:** + motivo.
4. **Frase de fixação** — blockquote com o texto em negrito.
5. Opcional: **Nota de atualização (fora do PD)** em blockquote, para novidade normativa.

Agrupe os itens do PD em blocos por afinidade (ex.: 2.1.1.1.3 a 2.1.1.1.7 = "títulos bancários e crédito privado"). Um módulo costuma render 8 a 12 blocos.

Prioridade de conteúdo: o que mais cai = números (alíquotas, limites, prazos, percentuais), distinções (A × B), quem faz o quê, e frases absolutas da banca ("sempre", "todo", "garantido").

## 3. Distribuição de tempo

- 15 min: uma regra-chave por item, sem fala longa; 1 questão.
- 20 min: blocos de 1–2 min; temas de maior peso com mais tempo; 2–3 questões.
- 30 min (padrão do modelo): abertura 1 + blocos 1–3 min + questões 3 + fechamento 1.

Dê mais tempo aos temas com mais subitens no PD e mais números.

## 4. Questões

Inéditas (nunca copiar questão real), 4 alternativas A–D, níveis Fácil / Médio / Difícil, linha `**Certificação:** · **Competência:** · **Nível:**`, gabarito com justificativa de **todas** as alternativas (correta e erradas) citando a regra. A difícil deve exigir cálculo ou combinação de duas regras (ex.: 12% de dedução + regime regressivo).

## 5. Fontes oficiais e como consultá-las

Hierarquia (CLAUDE.md do projeto): PD → o que ensinar; apostila → como explicar; norma oficial → valida números e vigência. Divergência apostila × norma: ensina a norma; se o professor já decidiu "apostila como resposta de prova + ressalva" para aquele ponto, mantenha a decisão.

| Fonte | Como acessar |
|---|---|
| Programa Detalhado | `aulas-certificacoes/00-fontes/programas-detalhados/PD-{CERT}.txt` — localizar o módulo: `grep -n -E "^{N}\.[0-9]+\. " PD-{CERT}.txt` |
| Apostila | `00-fontes/apostilas/APOSTILA-{CERT}.txt` (`<<<PÁGINA N>>>`); mapa de módulos em `00-fontes/apostilas/INDICE.md` |
| Aulas já feitas | `aulas/{cert}/aula-{N}.*/aula.md` — o "Quadro de emergência" e a tabela "Correções feitas na fonte" já trazem números conferidos |
| Normas BCB/CMN | `curl -s -A "Mozilla/5.0" "https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20CMN&p2=5058"` (tipos: `Resolu%C3%A7%C3%A3o%20CMN`, `Resolu%C3%A7%C3%A3o%20BCB`, `Resolu%C3%A7%C3%A3o` para antigas, `Circular`). JSON: `conteudo[0].Texto` (HTML), `Revogado`, `Atualizacoes` |
| Leis/decretos | `curl -s -A "Mozilla/5.0" https://www.planalto.gov.br/ccivil_03/...` (latin-1); remover `<strike>` antes de ler — é texto revogado. "Vigência encerrada" ao lado de redação de MP = MP caducou |
| CVM | `https://conteudo.cvm.gov.br/legislacao/resolucoes/...` (PDF/HTML) |
| Confirmação secundária | WebSearch — marcar "não confirmado em fonte primária" |

Extrair os quadros de emergência de todas as aulas do módulo de uma vez:
```bash
cd aulas-certificacoes/aulas/{cert}; for d in aula-{N}.*; do echo "## $d"; awk '/### Quadro de emergência/{f=1;next} /^### /{if(f)exit} f' $d/aula.md | grep "^|"; done
```

## 6. Checklist antes de salvar

- [ ] Todos os itens de 2º nível do PD do módulo aparecem no cronograma.
- [ ] Soma dos tempos = duração pedida.
- [ ] Todo número veio de aula conferida, apostila conferida na norma, ou está marcado "não confirmado".
- [ ] Nomes comerciais de instituições trocados por exemplos genéricos.
- [ ] Tabela "Correções e ressalvas" preenchida (apostila × norma, MP caducada, ponto em disputa).
- [ ] Questões com 4 alternativas e todas justificadas.
- [ ] "Referências oficiais e status" com `Último acesso`, status em negrito e link.
- [ ] Salvo em `aulas-certificacoes/roteiros/{cert}/revisao-modulo-{N}-{tema-curto}-fala.md`.
