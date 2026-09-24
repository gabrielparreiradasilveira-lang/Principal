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
- **Apostilas** (fonte de conteúdo): `00-fontes/apostilas/`.

## Onde salvar

- Fontes recebidas (PDF, planilha, PD, normas): `00-fontes/`
- Aula: `aulas/<certificacao>/aula-NN-tema-curto/aula.md` (partir de `modelos/modelo-aula-7-etapas.md`)
- Questões adicionais: `questoes/<certificacao>/bateria-NN-tema-nivel.md`
- Roteiros de fala / lousa: `roteiros/<certificacao>/aula-NN-tema-curto-<fala|lousa>.md`
