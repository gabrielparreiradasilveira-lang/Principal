# Aulas para Certificações Financeiras — Projeto CertPass

Aulas prontas para ensinar, alinhadas ao **Programa Detalhado ANBIMA**, para as certificações
CPA, C-PRO-I, C-PRO-R, CPA-20, CEA, CFP, CFG, CGA e CGE.

Regras completas: [`PROMPT_MESTRE_CERTPASS.md`](PROMPT_MESTRE_CERTPASS.md).
Modelo de aula: [`modelos/modelo-aula-7-etapas.md`](modelos/modelo-aula-7-etapas.md).

## Estrutura

```
aulas-certificacoes/
├── CLAUDE.md                  # regras carregadas automaticamente pelo agente
├── PROMPT_MESTRE_CERTPASS.md  # prompt mestre (fonte da verdade do projeto)
├── modelos/                   # esqueleto da aula em 7 etapas
├── 00-fontes/                 # Programas Detalhados, planilhas, PDFs, normas
├── aulas/                     # aulas/<certificacao>/aula-NN-tema-curto/aula.md
├── questoes/                  # baterias adicionais (quando solicitadas)
└── roteiros/                  # roteiros de fala / lousa (quando solicitados)
```

## Sequência obrigatória de toda aula

> **1. Fala de abertura → 2. Metáfora central → 3. Explicação dos tópicos → 4. Por que cai na prova? → 5. Case/Storytelling → 6. Questão final comentada → 7. Revisão final**

## Fluxo por aula

1. **Fontes** — salvar PD, planilha e anexos em `00-fontes/`.
2. **Identificação** — certificação, módulo, item e subitem do Programa Detalhado.
3. **Matriz** — cada tópico oficial ↔ seção da aula.
4. **Pesquisa normativa** — ANBIMA, CVM, BCB, CMN, RFB, B3, SUSEP, PREVIC, Tesouro; registrar status e data de acesso.
5. **Aula** — copiar o modelo para `aulas/<certificacao>/aula-NN-tema-curto/aula.md` e preencher as 7 etapas.
6. **Checklist final** (seção 7 do prompt mestre) — cobertura, case usa os conceitos ensinados, gabarito conferido, números/datas revisados, fontes e pendências sinalizadas.

## Convenções de nome

- Pasta de certificação: `cpa`, `c-pro-i`, `c-pro-r`, `cpa-20`, `cea`, `cfp`, `cfg`, `cga`, `cge`
- Aula: `aula-NN-tema-curto` (ex.: `aula-01-sistema-financeiro-nacional`)
- Bateria de questões: `bateria-NN-tema-nivel` (ex.: `bateria-01-sfn-medio.md`)
- Roteiro: `aula-NN-tema-curto-fala.md` / `aula-NN-tema-curto-lousa.md`
