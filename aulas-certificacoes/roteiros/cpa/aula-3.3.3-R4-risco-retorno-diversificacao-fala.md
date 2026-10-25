# Roteiro de fala — Aula CPA: Avaliação de Risco e Retorno e Diversificação de Carteira

**Base:**
- **Programa Detalhado CPA** (ANBIMA, v1.2, rev. 04/06/2025, vigência 01/01/2026), itens 3.3.3 e 3.3.4;
- APOSTILA-CPA, p. 498–499;
- aulas **R1** (tolerância, capacidade e horizonte), **F13** (suitability) e roteiro **3.2.3-3.2.4** (gestão de investimentos e risco), para não repetir;
- aula do repositório `aulas/cpa/aula-1.2.7-riscos-liquidez-credito-mercado/aula.md`, que trata dos riscos de liquidez, crédito e mercado do ponto de vista do sistema.

CPA 3.3.3 · 3.3.4 · Módulo 3 · **15 min** · Aula R4 · **só a etapa de tópicos**

**Legenda:** **negrito** = marcador · "texto entre aspas" = fala · 🔇 = bastidor, sem fala · ✏️ = correção da fonte · ⌨️ = teclas da HP12C · 🖥️ = visor.

---

## Bastidor — antes de gravar

### 🔇 Metáfora única desta aula

**A cesta de ovos.** Não se coloca todos os ovos na mesma cesta: se ela cair, quebram todos. Ovos em cestas diferentes reduzem o estrago de um tombo isolado.

**Onde a metáfora falha:** em uma crise geral, todas as cestas caem juntas. A diversificação reduz o risco de um ativo ou empresa (específico), mas não protege de uma crise do mercado (sistemático). A metáfora também não mostra o peso que cada ovo tem: o que importa é a correlação entre as cestas.

### 🔇 Formato

- Direto aos tópicos do PD, sem as demais etapas.
- A cliente **Clara**, 40 anos, atravessa a aula: tem R$ 200.000 e **todo o dinheiro está em ações da empresa onde trabalha**. A aula mostra por que isso é risco que ela poderia evitar.
- O PD pede **conceitos**. Os cálculos servem para fixar a ideia, e não para serem cobrados.

### 🔇 Checagem de escopo (PD × materiais)

| Subitem do PD | Apostila | Tratamento |
| --- | --- | --- |
| 3.3.3 Avaliação de risco e retorno | p. 498 | Conferido; risco, relação com retorno, tipos e classificação (diversificável × sistemático) |
| 3.3.4 Diversificação de carteira | p. 498–499 | Conferido; objetivo, funcionamento e limite |

### ✏️ Correções e notas da fonte

| # | Fonte | O material diz | O correto |
| --- | --- | --- | --- |
| 1 | Apostila p. 498 | "Quanto maior o risco assumido, maior é a expectativa de retorno" | Correto, e a palavra é **expectativa**: retorno maior **não é garantido**. Risco maior significa que o resultado pode ser **melhor ou pior** |
| 2 | Apostila p. 498 | O risco "diversificável" se reduz "ao adicionar mais ativos à carteira" | Só reduz se os ativos **se comportam de forma distinta**. Adicionar ativos muito parecidos (ações do mesmo setor) quase não diversifica |
| 3 | Apostila p. 498 | Lista três riscos: mercado, crédito e liquidez | São os **principais**, e não os únicos. Outros riscos, como o operacional e o legal, existem e aparecem em outras aulas |
| 4 | Apostila p. 498–499 | Diversificação reduz o risco "sem necessariamente reduzir o retorno esperado" | Correto: reduz risco **sem reduzir** o retorno esperado médio (como no exemplo desta aula), mas **não elimina** o risco sistemático |
| 5 | Apostila p. 496–499 | Subitens numerados como "3.5" | Numeração do PD: 3.3.3 e 3.3.4 |

### 🔇 Dados dos exemplos

| Item | Valor |
| --- | --- |
| Retorno esperado por cenários | 30% de chance de +20%, 50% de +10% e 20% de −15% → **8,00%** |
| Ativo A | Retorno esperado de 12%; volatilidade (desvio-padrão) de 20% |
| Ativo B | Retorno esperado de 8%; volatilidade de 10% |
| Carteira 50% A + 50% B | Retorno esperado de **10%** (média ponderada) |
| Risco da carteira se os ativos andassem juntos (correlação 1) | **15%**, a média ponderada |
| Risco da carteira com correlação de 0,2 | **12,04%** |
| Risco da carteira com correlação de −0,3 | **9,75%** |

Valores hipotéticos. A fórmula do risco de uma carteira de dois ativos é σ² = w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·ρ·σ₁·σ₂, em que w é o peso, σ o desvio-padrão e ρ a correlação. O PD não cobra a fórmula.

### 🔇 Cronograma

| Tópico | Tempo |
| --- | --- |
| 3.1 Avaliação de risco e retorno | 8 min |
| 3.2 Diversificação de carteira | 7 min |
| **Total** | **15 min** |

---

## 3. Explicação dos tópicos — 15 min

### 3.1 Avaliação de risco e retorno — 8 min · CPA 3.3.3

> **Objetivo deste bloco:** ao fim, o aluno consegue calcular o retorno esperado por cenários e explicar por que o retorno esperado não mostra o risco.

- **O que é risco**
  - "Risco é a possibilidade de o resultado do investimento ser diferente do esperado, incluindo perdas. Repare: diferente do esperado. Risco não é só perder; é não saber ao certo quanto vai ganhar."
- **A relação com o retorno**
  - "De forma geral, quanto maior o risco assumido, maior é a expectativa de retorno. O investidor só aceita mais risco se espera ser recompensado."
  - ✏️ "A palavra importante é expectativa. Mais risco não garante mais retorno: significa que o resultado pode ser melhor, mas também pior."

| Perfil do ativo | Risco | Retorno esperado |
| --- | --- | --- |
| Título público pós-fixado | Baixo | Menor |
| CDB de banco médio | Médio | Intermediário |
| Ações | Alto | Maior |

  - 🔇 Tabela ilustrativa, sem números; os retornos variam por cenário.
- **Os principais tipos de risco**

| Risco | O que é | Exemplo |
| --- | --- | --- |
| **De mercado** | Oscilação dos preços dos ativos | A bolsa cai e a ação perde valor |
| **De crédito** | O emissor deixa de pagar | O banco emissor do CDB quebra |
| **De liquidez** | Dificuldade de vender sem perda relevante de valor | Cotas de um fundo fechado sem negociação |

  - "Cada produto tem um mix desses riscos. O Tesouro Selic tem baixíssimo risco de crédito, mas oscila um pouco. O CDB tem risco do emissor. A ação tem risco de mercado alto."
  - ✏️ "São os principais riscos, não os únicos. Há também o risco operacional e o legal, vistos em outras aulas."
- **Risco diversificável e não diversificável**
  - "O risco se divide em dois grupos."

| | **Diversificável** (específico) | **Não diversificável** (sistemático) |
| --- | --- | --- |
| **O que é** | Risco ligado a um ativo, empresa ou setor | Risco que afeta o mercado como um todo |
| **Exemplo** | Fraude na empresa em que se investiu | Crise econômica, choque de juros |
| **Dá para reduzir?** | **Sim**, com diversificação | **Não** pode ser eliminado |

- **Retorno esperado: média ponderada pelas chances**
  - "Retorno esperado é o retorno médio, ponderado pela chance de cada cenário. Veja um exemplo: uma ação tem 30% de chance de subir 20%, 50% de chance de subir 10% e 20% de chance de cair 15%."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `0,3` `ENTER` `20` `×` | 🖥️ 6,00 | Contribuição do cenário otimista |
| 2 | ⌨️ `0,5` `ENTER` `10` `×` `+` | 🖥️ 11,00 | Soma o cenário base |
| 3 | ⌨️ `0,2` `ENTER` `15` `CHS` `×` `+` | 🖥️ 8,00 | Soma o cenário de perda: retorno esperado de 8% |

  - "O retorno esperado é de 8%. Mas repare que há 20% de chance de perder 15%. O retorno esperado não mostra o risco: é a dispersão dos resultados que mostra."
  - 🔇 Probabilidades hipotéticas.
- **Medindo o risco**
  - "A medida mais comum é a volatilidade, o desvio-padrão dos retornos. Quanto maior, mais o resultado se afasta da média. Um ativo com média de 10% e volatilidade de 20% é mais arriscado que outro com a mesma média e volatilidade de 5%."
- **A conexão com o cliente**
  - "A decisão final cruza o risco do produto com o que o cliente tolera, o que pode perder e o prazo que tem. É o suitability, visto na F13."
- **Erro comum:** achar que maior risco garante maior retorno. Ele dá maior expectativa de retorno, sem garantia.

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "Risco é a possibilidade de o resultado ser diferente do esperado, incluindo perdas" | Certo | Definição do risco |
| "Maior risco garante maior retorno" | Errado | Maior **expectativa** de retorno, sem garantia |
| "Risco de crédito é a possibilidade de inadimplência do emissor" | Certo | Definição do risco de crédito |
| "Risco de liquidez é a dificuldade de vender um ativo sem perda relevante de valor" | Certo | Definição do risco de liquidez |
| "O risco sistemático pode ser eliminado com diversificação" | Errado | Não é diversificável |

> **Risco é a chance de o resultado fugir do esperado; quanto maior, maior a expectativa de retorno, mas nunca a garantia.**

**🔗 Ponte:** "Se parte do risco pode ser reduzida, como?"

---

### 3.2 Diversificação de carteira — 7 min · CPA 3.3.4

> **Objetivo deste bloco:** ao fim, o aluno consegue explicar por que a correlação decide quanto a diversificação reduz o risco, e calcular o risco de uma carteira de dois ativos.

- **O que é**
  - "Diversificação é distribuir os investimentos entre diferentes ativos, setores ou classes. O objetivo é reduzir o risco da carteira sem necessariamente reduzir o retorno esperado."
- **Como funciona**
  - "Ao combinar ativos que se comportam de forma distinta, o impacto de um evento negativo específico diminui. Quando um cai, outro pode subir ou cair menos. É a ideia da cesta de ovos."

| Dimensão | Exemplo |
| --- | --- |
| **Classes de ativos** | Renda fixa, ações, multimercado, imóveis |
| **Setores** | Bancos, energia, varejo |
| **Emissores** | Vários bancos, e não um só |
| **Prazos** | Vencimentos escalonados |
| **Geografia** | Brasil e exterior |

- **O caso da Clara**
  - "Clara tem 200 mil reais, todos em ações da empresa onde trabalha. Se a empresa tiver um problema, ela perde o emprego e o patrimônio ao mesmo tempo. Esse é um risco específico, diversificável, que ela não precisa correr."
- **O número por trás da ideia**
  - "Dois ativos. O A tem retorno esperado de 12% e volatilidade de 20%. O B tem retorno esperado de 8% e volatilidade de 10%. Uma carteira meio a meio tem retorno esperado de 10%, a média ponderada."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `2` `0,5` `ENTER` `12` `×` `0,5` `ENTER` `8` `×` `+` | 🖥️ 10,00 | Retorno esperado da carteira (%) |

  - "Se os dois ativos andassem sempre juntos, o risco da carteira seria a média ponderada: 15%. Mas eles não andam juntos: a correlação entre eles é de 0,2. Calculando o risco da carteira..."

| Passo | Teclas | Visor | O que significa |
| --- | --- | --- | --- |
| 1 | ⌨️ `f` `REG` `f` `4` `0,25` `ENTER` `0,04` `×` | 🖥️ 0,0100 | Parcela do ativo A: peso² × variância |
| 2 | ⌨️ `0,25` `ENTER` `0,01` `×` `+` | 🖥️ 0,0125 | Soma a parcela do ativo B |
| 3 | ⌨️ `2` `ENTER` `0,25` `×` `0,2` `×` `0,2` `×` `0,1` `×` `+` | 🖥️ 0,0145 | Soma o termo da correlação: variância da carteira |
| 4 | ⌨️ `g` `√x` `100` `×` | 🖥️ 12,04 | Risco da carteira: **12,04%** |

  - "O retorno esperado continua em 10%, a média dos dois, mas o risco caiu de 15% para 12%. Menos risco para o mesmo retorno esperado: esse é o ganho da diversificação. E, se a correlação fosse negativa, de menos 0,3, o risco cairia para cerca de 9,75%."
  - 🔇 Valores hipotéticos. A fórmula do risco da carteira (σ² = w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·ρ·σ₁·σ₂) não é cobrada pelo PD; serve para mostrar que diversificar depende da **correlação**.
- **O limite**
  - "A diversificação atua sobre o risco diversificável, que é o específico de um ativo ou empresa. Ela não elimina o risco sistêmico, como uma crise econômica ou um choque de mercado. Em uma crise, quase tudo cai junto."
  - ✏️ "Diversificar não é ter muitos ativos, é ter ativos diferentes. Dez ações do mesmo setor sofrem juntas."
- **Na prática**
  - "Para o cliente de varejo, a diversificação costuma vir por fundos, que reúnem vários ativos. E, no crédito bancário, vale espalhar a aplicação em mais de uma instituição, para não concentrar o risco de crédito de um único emissor."
  - 🔇 O FGC cobre depósitos e títulos de emissão bancária até um limite por CPF e instituição (Res. CMN 4.222/2013, de memória); conferir os valores vigentes antes de citar.
- **A solução para a Clara**
  - "Clara pode vender parte das ações da empresa, distribuir o dinheiro entre classes de ativos e manter um percentual pequeno, se quiser, no papel da empresa. Assim, o risco específico cai, e o seu retorno esperado fica no mesmo patamar."
- **Erro comum:** achar que dez ações do mesmo setor formam uma carteira diversificada.

| Frase da prova | Certo ou errado | Por quê |
| --- | --- | --- |
| "A diversificação busca reduzir o risco da carteira sem necessariamente reduzir o retorno esperado" | Certo | Função da diversificação |
| "A diversificação elimina o risco sistemático" | Errado | Atua sobre o risco **diversificável** |
| "Combinar ativos com comportamentos distintos diminui o impacto de eventos negativos específicos" | Certo | Base da diversificação |
| "Investir em dez ações do mesmo setor é uma carteira bem diversificada" | Errado | Ativos muito parecidos diversificam pouco |

> **Diversificar é combinar ativos diferentes: reduz o risco específico, mas não protege de uma crise geral.**

- 🔇 **Fechamento:** "Risco é a chance de fugir do esperado; mais risco significa maior expectativa de retorno, sem garantia; parte do risco, a específica, se reduz diversificando; a sistemática, não."

---

## Lista de pegadinhas com nome

1. **Pegadinha do risco que garante** — "Maior risco garante maior retorno." Errado: dá maior expectativa, sem garantia.
2. **Pegadinha da diversificação total** — "A diversificação elimina o risco sistemático." Errado: atua só sobre o risco específico.
3. **Pegadinha das dez ações** — "Dez ações do mesmo setor formam carteira diversificada." Errado: ativos parecidos sofrem juntos.
4. **Pegadinha do retorno médio** — "O retorno esperado mostra o risco da carteira." Errado: é a dispersão dos cenários que mostra o risco.

---

## Nota de verificação

- Programa Detalhado CPA (v1.2): itens 3.3.3 e 3.3.4 lidos no texto do PD do repositório.
- Apostila CPA, p. 498–499: lida em sessão anterior.
- **Citado de memória, sem reabrir o texto:** cobertura do FGC (Res. CMN 4.222/2013). **Conferir antes de gravar.**
- **Conceitos de finanças, sem fonte aberta nesta sessão:** desvio-padrão como medida de risco, correlação e a fórmula do risco da carteira de dois ativos.
- **Convenções sem força normativa:** a tabela ilustrativa de risco × retorno, os cenários e as probabilidades, os ativos A e B, os pesos e as correlações do exemplo e a dimensão "geografia" da diversificação.
- **Cálculos conferidos em Python nesta revisão:** 0,3 × 20 + 0,5 × 10 + 0,2 × (−15) = 8; retorno da carteira = 0,5 × 12 + 0,5 × 8 = 10; variância com correlação 0,2 = 0,0145 → desvio-padrão de 12,04%; com correlação −0,3, variância = 0,0095 → 9,75%; com correlação 1, 15%.
- Revisão de estrutura: metáfora única (cesta de ovos), caso antes da regra, objetivo e erro comum por bloco, fonte removida da fala, lista de pegadinhas com nome.
