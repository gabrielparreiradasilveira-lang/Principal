# Roteiro de fala — Aula CPA: Fundos de Investimento — Responsabilidade Ilimitada, Patrimônio Líquido Negativo e Insolvência da Classe

**Base:** PD CPA v1.2 (rev. 04/06/2025, vigência 01/01/2026), itens **2.1.2.2.25.2**, **2.1.2.2.25.3** e **2.1.2.2.25.4** (com o 2.1.2.2.25.1 como contexto); APOSTILA-CPA p. 342–344; aula do repositório `aula-2.1.2-E-vedacoes-encargos-pl-negativo` (seção 3.5), conferida contra a Res. CVM 175, arts. 6º, § 3º, 18, 29 e 122 a 125.

CPA 2.1.2.2.25.2 · 2.1.2.2.25.3 · 2.1.2.2.25.4 · Módulo 2 · **10 min** · Aula F1 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor · ✏️ = correção da fonte (só no bastidor) · ⌨️ = HP12C · 🖥️ = visor.

---

## Bastidor

### 🔇 Metáfora única desta aula

**Freio de emergência.** Quando o patrimônio fica negativo, o administrador aciona o freio: tranca resgates e aportes, avisa todos e apresenta um plano. O freio para o fundo, para ouvir o diagnóstico antes de seguir.

**Onde a metáfora falha:** um freio de carro para o carro na hora. O freio do fundo não resolve o problema, só o põe em pausa, e há prazos legais para o plano e a assembleia. Além disso, o freio não decide quem paga a conta: isso depende da responsabilidade do cotista.

### 🔇 Caso

Um **fundo multimercado** perde com derivativos. A classe tem R$ 8.000.000 em ativos e R$ 9.200.000 em obrigações: patrimônio líquido de **−R$ 1.200.000**. Um cotista tem 10% das cotas.

### 🔇 Checagem de escopo

| Subitem do PD | Fonte | Tratamento |
| --- | --- | --- |
| 2.1.2.2.25.1 Responsabilidade limitada (contexto) | Material A0083 p. 4; Res. CVM 175, arts. 6º, § 3º, 18 e 29 | Só como contraste |
| 2.1.2.2.25.2 Responsabilidade ilimitada de cotistas | Idem | Conferido |
| 2.1.2.2.25.3 Patrimônio líquido negativo | Apostila p. 342–343; A0095; art. 122 | Conferido |
| 2.1.2.2.25.4 Insolvência da classe | Apostila p. 343–344; A0095; arts. 123 a 125 | Conferido; **cancelamento corrigido** |

### ✏️ Correções da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | A0095 p. 8 | "Se o administrador não adotar o plano em até 20 dias, a Superintendência pode cancelar o registro" | A Superintendência cancela **depois da declaração judicial de insolvência**, se o administrador não cancelar o registro a tempo (art. 125, § 1º) |
| 2 | Apostila p. 342 | PL = "investimentos − contas a pagar + contas a receber" | O PL é **ativos − passivos**; é negativo quando as obrigações superam os ativos (art. 122) |
| 3 | Apostila p. 342–343 | "Dar um tempo" como termo oficial | Expressão didática. A norma fala em fechar para resgates, não amortizar, não aceitar subscrições, comunicar o gestor, divulgar fato relevante e cancelar resgates pendentes |
| 4 | Apostila p. 343 | Plano em "até 20 dias" e assembleia em "até dois dias úteis" | Correto. Os 2 dias úteis contam **da conclusão do plano**; a prova costuma trocar os dois prazos |
| 5 | Apostila p. 342–344 | Ilimitada tratada só no PL negativo | Na ilimitada, os cotistas podem ter de **aportar**; isso consta do **termo de adesão**. O prestador responde por dolo ou má-fé |

### 🔇 Dados

| Item | Valor |
| --- | --- |
| PL da classe | 8.000.000 − 9.200.000 = **−R$ 1.200.000** |
| Parte do cotista com 10% das cotas (ilimitada, hipótese) | 10% × 1.200.000 = **R$ 120.000** |

Valores hipotéticos. O rateio segue o regulamento e o termo de adesão.

### 🔇 Cronograma

| Bloco | Tempo |
| --- | --- |
| 1. Caso do fundo: quanto o cotista pode perder | 3 min |
| 2. Patrimônio negativo: o freio e os prazos | 4 min |
| 3. Insolvência: quando e quem pede | 3 min |
| **Total** | **10 min** |

---

## 3. Explicação em três blocos

### Bloco 1 — Caso do fundo: quanto o cotista pode perder — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue dizer quanto um cotista pode perder, conforme a responsabilidade seja limitada ou ilimitada.

- "Um fundo multimercado perdeu com derivativos. Ele tem oito milhões em ativos e deve nove milhões e duzentos mil. O patrimônio está em menos um milhão e duzentos mil reais."
- "Antes de seguir, duas palavras. **Patrimônio líquido** é o que sobra quando se tira o que se deve do que se tem. **Responsabilidade do cotista** é o limite do que ele pode perder."
- "Na responsabilidade **limitada**, o cotista perde no máximo o que aplicou. Na **ilimitada**, pode ter de colocar mais dinheiro, e isso consta do termo de adesão que ele assinou."
- "Se o cotista tiver dez por cento das cotas, a parte dele na cobertura seria de cento e vinte mil reais, além do que já aplicou."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `8000000` `ENTER` `9200000` `−` | 🖥️ −1.200.000,00 | PL da classe |
| 2 | ⌨️ `CHS` `ENTER` `10` `%` | 🖥️ 120.000,00 | Parte de 10% da cobertura |

- 🔇 O sinal negativo do passo 1 é o PL negativo. O `CHS` o inverte para calcular a parte.
- **Erro comum:** achar que, na responsabilidade ilimitada, o cotista nunca perde mais do que aplicou. Ele pode perder mais e ser chamado a aportar.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Na responsabilidade ilimitada, o cotista nunca perde mais do que o valor aplicado" | Errado | Pode perder mais e ser chamado a aportar |
| "A responsabilidade ilimitada deve constar do termo de adesão" | Certo | O cotista precisa saber |

> **Limitada: perde no máximo o que aplicou. Ilimitada: pode ter de aportar mais.**

**🔗 Ponte:** "E quando o patrimônio fica negativo? Entra o freio de emergência."

---

### Bloco 2 — Patrimônio negativo: o freio e os prazos — 4 min

> **Objetivo deste bloco:** ao fim, o aluno consegue listar as medidas do administrador e os prazos do plano e da assembleia.

- "Quando o patrimônio fica negativo, na responsabilidade limitada, o administrador aciona o freio. Ele faz cinco coisas, logo de início: fecha a classe para resgates e amortizações, não aceita novas aplicações, avisa o gestor, divulga fato relevante e cancela os resgates pendentes."
- "Em até vinte dias, ele prepara com o gestor um plano de resolução: as causas, o balancete e uma proposta. Em até dois dias úteis depois do plano, convoca a assembleia de cotistas."

| Quando | O administrador deve |
| --- | --- |
| **Imediatamente** | Fechar para resgates; não aceitar subscrições; comunicar o gestor; divulgar fato relevante; cancelar resgates pendentes |
| **Em até 20 dias** | Plano de resolução com o gestor: causas, balancete e proposta |
| **Em até 2 dias úteis** depois do plano | Convocar a assembleia |

- "Se o cotista pediu resgate ontem, com pagamento em cinco dias, o pedido não será processado. Por isso o fato relevante é indispensável."
- "Se os prestadores essenciais avaliarem, por escrito, que o patrimônio negativo não coloca a solvência em risco, o plano e a assembleia ficam facultativos."
- **Erro comum:** achar que o administrador mantém os resgates abertos para não assustar os cotistas. Ele fecha, e é isso que a norma exige.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "O administrador mantém os resgates abertos para não alarmar os cotistas" | Errado | Fecha para resgates e divulga fato relevante |
| "O plano de resolução é elaborado em até 20 dias, com o gestor" | Certo | Prazo de 20 dias do plano, feito com o gestor |
| "A assembleia é convocada em até 20 dias após o plano" | Errado | São 2 dias úteis |

> **PL negativo: tranca resgates e aportes, avisa, plano em 20 dias, assembleia em 2 dias úteis.**

**🔗 Ponte:** "E se os cotistas não aprovarem o plano? Vem a insolvência."

---

### Bloco 3 — Insolvência: quando e quem pede — 3 min

> **Objetivo deste bloco:** ao fim, o aluno consegue dizer quem pede a insolvência e o que acontece depois da declaração.

- "A insolvência acontece quando o plano não é aprovado e os cotistas escolhem esse caminho. Ou quando a assembleia não se instala, por falta de quórum, ou não decide. Nesses casos, o administrador pede a declaração judicial de insolvência da classe."
- "A CVM também pode pedir, se o patrimônio negativo puser em risco o mercado ou o sistema financeiro."
- "Declarada a insolvência, o administrador divulga fato relevante e cancela o registro da classe na CVM. Se não cancelar a tempo, a Superintendência cancela."
- **Erro comum:** achar que o cancelamento apaga as infrações anteriores. Ele não apaga.

| Frase de prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Declarada a insolvência, o registro é cancelado e as infrações anteriores deixam de existir" | Errado | O cancelamento não apaga infrações |
| "Se a assembleia não for instalada por falta de quórum, o administrador pede a insolvência" | Certo | Sem decisão possível, o caminho é a insolvência |

> **Sem decisão, insolvência: o administrador pede, divulga fato relevante e, declarada, cancela o registro.**

- 🔇 **Fechamento:** "Na responsabilidade ilimitada, o cotista pode ter de aportar. Com patrimônio negativo, o administrador tranca, avisa e apresenta um plano em vinte dias. Sem solução, o caminho é a insolvência." Próxima aula: F2, o Anexo I dos FIF.

---

## Lista de pegadinhas com nome

1. **Pegadinha do "nunca perde mais"** — "Na ilimitada, o cotista nunca perde mais do que aplicou." Errado: pode perder mais e ser chamado a aportar.
2. **Pegadinha da troca de prazos** — "A assembleia é convocada em até 20 dias após o plano." Errado: são 2 dias úteis; os 20 dias são do plano.
3. **Pegadinha do resgate aberto** — "O administrador mantém os resgates abertos." Errado: fecha para resgates.
4. **Pegadinha da infração apagada** — "O cancelamento apaga as infrações." Errado: não apaga.

---

## Nota de verificação

- PD 2.1.2.2.25.1 a 2.1.2.2.25.4 lido no texto do repositório. Apostila p. 342–344 lida nesta sessão.
- Aula do repositório 2.1.2-E e Res. CVM 175, arts. 6º, § 3º, 18, 29 e 122 a 125: conferidos ali. **Textos legais não reabertos nesta sessão.**
- Cálculos conferidos em Python: 8.000.000 − 9.200.000 = −1.200.000; 10% de 1.200.000 = 120.000.
- Convenções: valores do exemplo e rateio proporcional (dependem do regulamento).
- Revisão de estrutura: metáfora única (freio de emergência), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
