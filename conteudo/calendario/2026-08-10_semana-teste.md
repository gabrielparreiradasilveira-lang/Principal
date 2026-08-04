# Calendário — semana de teste (10 a 16/08/2026)

Modelo B (diário, 7 posts/semana, formato livre por ideia). Gerado para validar o fluxo ponta a ponta do workflow.

| Data | Dia | Pilar | Categoria | Formato | Hook | Ideia (motivo de existir) |
|---|---|---|---|---|---|---|
| 10/08 | Seg | EDU | Tradução de Jargão | Carrossel | "Come-cotas não é imposto extra. É antecipação." | Termo mais mal-entendido por quem começa em fundos — mata a objeção nº1 contra investir em fundos de renda fixa. |
| 11/08 | Ter | ENT | Mito vs. Verdade do Mercado | Reel | "Quem tem CPA-20 sabe mais que quem tem CFP. Mito." | Desmonta a crença de que certificação mais avançada = mais completa; gera discordância nos comentários. |
| 12/08 | Qua | EDU | Questão Comentada | Carrossel | "Essa questão reprovou 6 em cada 10 no simulado." | Questão padrão FGV sobre suitability, gabarito comentado alternativa por alternativa. |
| 13/08 | Qui | CONF | Economia no Dia a Dia | Story | "Selic subiu. Isso muda sua reserva de emergência." | Traduz a notícia da semana (Selic) para decisão prática do seguidor — CTA para DM. |
| 14/08 | Sex | VEN | Comparativo de Certificações | Carrossel | "CPA-10 ou CPA-20: uma te deixa estagnado." | Conteúdo de decisão para quem está escolhendo por qual certificação começar — puxa para mentoria/simulado. |
| 15/08 | Sáb | ENT | Números que Ninguém Te Conta | Reel | "Só 12% de quem presta CPA-20 estuda mais de 1h/dia." | Estatística que gera compartilhamento e comparação entre seguidores nos comentários. |
| 16/08 | Dom | CONF | Bastidores da Carreira de Gestor | Imagem estática | "O dia que quase saí da gestora por um erro de marcação." | Humaniza, mostra erro real já cometido — constrói credibilidade sem parecer perfeito. |

## Checagem da regra dos 3 dias
Sequência de pilares: EDU, ENT, EDU, CONF, VEN, ENT, CONF — nenhum pilar se repete em mais de 1 dia seguido. ✅ Dentro da regra.

## Observação de rigor técnico
O post de 12/08 (Questão Comentada, suitability) precisa de revisão do Gabriel antes de publicar — norma sensível, conforme regra de qualidade da skill.

## Status de produção

| Data | Material | Status |
|---|---|---|
| 10/08 | Copy + 10 slides de carrossel | ✅ Pronto |
| 11/08 | Roteiro de reel | ✅ Pronto |
| 12/08 | Copy + 10 slides de carrossel | ⚠️ Pronto, **bloqueado para revisão técnica** (suitability) |
| 13/08 | Copy + 1 imagem de story | ✅ Pronto (conferir Selic vigente antes de postar) |
| 14/08 | Copy + 10 slides de carrossel | ✅ Pronto |
| 15/08 | Roteiro de reel | ⚠️ **Bloqueado**: estatística do hook é ilustrativa, precisa de dado real com fonte antes de publicar |
| 16/08 | Copy + 1 imagem estática | ✅ Pronto — ângulo institucional/geral, sem usar o Gabriel como case pessoal |

Todos os assets ficam em `conteudo/posts/AAAA-MM-DD/`. Pipeline de geração de imagem em `conteudo/scripts/` (`base.py` + um script por post).
