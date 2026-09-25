# Aula CPA — COE: Certificado de Operações Estruturadas

Sep 25, 2026 · @Boss · Roteiro integrado · 40 min

## Identificação e alinhamento

Aula D de 4 do bloco **2.1.1.2.2.2 a 2.1.1.4** do Programa Detalhado CPA (ANBIMA, vigência 01/01/2026), Módulo 2. Esta aula cobre **2.1.1.4 Certificado de Operações Estruturadas (COE)**, com os subitens 2.1.1.4.1 a 2.1.1.4.3.

### Checagem de escopo

| Subitem do PD | Fonte de origem | Tratamento |
| --- | --- | --- |
| 2.1.1.4.1 Principais regras e estrutura via derivativos | PDF A3501 p. 3–5, 12 · APOSTILA-CPA p. 282–283 | Conferido, com correções e **nota de atualização** |
| 2.1.1.4.2 Níveis de risco e garantias (capital protegido ou em risco) | PDF A3501 p. 6–11 · APOSTILA-CPA p. 283 | Conferido, **completado com o risco de crédito do emissor** |
| 2.1.1.4.3 Tributação | PDF A3501 p. 13 · APOSTILA-CPA p. 284 | Conferido |

**Cobertura PD × PDFs:** todos os subitens têm material. A troca da norma do COE entra como **nota de atualização**, como você decidiu.

### Cronograma

| Etapa | Tempo |
| --- | --- |
| 1. Fala de abertura | 3 min |
| 2. Metáfora central | 3 min |
| 3. Tópicos (Estrutura via derivativos 5 · Regras principais 5 · Capital protegido × em risco 8 · Tributação 4) | 22 min |
| 4. Por que cai na prova | 4 min |
| 5. Case | 3 min |
| 6. Questão comentada | 3 min |
| 7. Revisão final | 2 min |
| **Total** | **40 min** |

### Correções feitas na fonte

| # | Fonte | O material diz | O correto | Fonte oficial |
| --- | --- | --- | --- | --- |
| 1 | PDF A3501 p. 5 · APOSTILA-CPA p. 283 | "Prazo determinado (não existe resgate antecipado pelo investidor)" | O COE tem **prazo determinado** e **não tem liquidez diária**, mas a norma exige que o registro traga as **condições de recompra ou resgate antecipado**, quando houver. O investidor **não tem direito** a resgatar a qualquer momento | Res. CMN 5.166/2024 |
| 2 | PDF A3501 p. 6–7 · APOSTILA-CPA p. 283 | "COE de capital garantido: o investidor recebe 100% do principal" | Nome normativo: **Valor Nominal Protegido**. A proteção depende de o **emissor honrar o pagamento**: há **risco de crédito do emissor** e o COE **não tem FGC** | Res. CMN 5.166/2024; FGC |
| 3 | PDF A3501 p. 8 · APOSTILA-CPA p. 283 | "COE de capital em risco" | Nome normativo: **Valor Nominal em Risco**: o pagamento mínimo cobre só uma **parcela** do valor investido, definida previamente | Res. CMN 5.166/2024 |
| 4 | PDF A3501 p. 5 | Emissor deve fornecer "probabilidade dos cenários (quando aplicável)" | Não reconferido → **retirado**. O documento obrigatório é o **DIE** (Documento de Informações Essenciais), com cenários, riscos e características | Res. CVM 8/2020 |

## 1. Fala de abertura — 3 min

> "Invista na bolsa americana sem risco de perder o que aplicou." Parece bom demais? É um **COE**.
>
> O COE é um **produto montado pelo banco**: junta um pedaço de **renda fixa** com **derivativos** para entregar um cenário combinado. Você sabe, antes de aplicar, **quanto ganha em cada cenário**.
>
> Mas há três perguntas que o investidor precisa fazer: **meu capital é protegido ou está em risco? Posso sair antes do prazo? E se o banco quebrar?**
>
> Nesta aula você vai responder as três e aprender como o COE é tributado.

### Objetivo da abertura

Apresentar o COE como produto estruturado com cenários conhecidos e antecipar os riscos que a prova cobra.

### Conexão com o Programa Detalhado

CPA 2.1.1.4.1 a 2.1.1.4.3.

## 2. Metáfora central — 3 min

### Metáfora: o pacote de viagem com seguro

> O COE é um **pacote de viagem montado pela agência (o banco)**.
>
> Parte do dinheiro vai para a **passagem garantida de volta**: é a **renda fixa**, que devolve o capital no fim. A outra parte compra os **passeios opcionais**: os **derivativos**, que só rendem se o **cenário** acontecer (se o dólar subir, se o índice subir...).
>
> Há pacotes **com volta garantida** (**valor nominal protegido**): no pior caso, você volta para casa com o que levou. E há pacotes **sem volta garantida** (**valor nominal em risco**): prometem passeios melhores, mas você pode voltar com menos.
>
> Dois alertas: o pacote tem **data marcada**, e você não desce do avião no meio do caminho. E a garantia de volta **depende da agência continuar existindo**: se ela quebrar, **não há seguro do FGC**.

### Correspondência técnica

| Elemento da metáfora | Correspondência técnica |
| --- | --- |
| Agência que monta o pacote | Instituição financeira emissora |
| Passagem garantida de volta | Componente de renda fixa |
| Passeios opcionais | Derivativos (opções, swaps) |
| Roteiro conhecido antes | Cenários de retorno no DIE |
| Volta garantida | Valor nominal protegido |
| Volta sem garantia | Valor nominal em risco |
| Data marcada | Prazo determinado, sem liquidez diária |
| Agência quebrar | Risco de crédito do emissor, sem FGC |

### Frase de fixação

> **COE = renda fixa + derivativos, com cenários conhecidos, prazo marcado e risco do banco emissor.**

## 3. Explicação dos tópicos — 22 min

### 3.1 Estrutura via derivativos — 5 min

#### Como funciona

| Componente | Função |
| --- | --- |
| **Renda fixa** | Parte do valor aplicado em um título que, no vencimento, devolve **todo** (protegido) ou **parte** (em risco) do capital |
| **Derivativo** | A outra parte compra **opções** ou outros derivativos que geram o ganho variável ligado ao **ativo de referência** (índice, ação, moeda) |

**Elementos comuns:**

| Elemento | O que é |
| --- | --- |
| **Ativo de referência** | O que define o resultado (ex.: S&P 500, dólar, uma ação) |
| **Participação** | % da variação do ativo repassado ao investidor (ex.: 80% da alta) |
| **Cap (teto)** | Ganho máximo |
| **Barreira** | Nível de preço que liga ou desliga um ganho ou uma perda |
| **Estratégia** | **Direcional** (ganha com alta ou queda) ou **neutra** (ganha com estabilidade) |

#### Frase de fixação

> **A renda fixa segura o capital; o derivativo busca o ganho.**

#### Alinhamento ao PD

CPA 2.1.1.4.1.

---

### 3.2 Regras principais — 5 min

#### Como funciona

| Regra | Detalhe |
| --- | --- |
| Emissor | **Exclusivamente instituição financeira** autorizada pelo Banco Central |
| Registro | Em entidade registradora autorizada |
| Prazo | **Determinado**; **sem liquidez diária**. Recompra ou resgate antecipado só nas **condições previstas** pelo emissor |
| Informação ao investidor | **DIE (Documento de Informações Essenciais)**: cenários de retorno, ativo de referência, modalidade, riscos |
| FGC | **Não tem** |
| Adequação | Produto complexo: exige análise de **suitability** |

> **Nota de atualização:** a regulamentação do CMN sobre COE era a **Res. CMN 4.263/2013**, citada pelo material. Ela foi **revogada pela Res. CMN 5.166/2024**, que reformou o regime e criou também o **COE de risco de crédito**. A distribuição pública segue a **Res. CVM 8/2020**.

#### O que a prova pode confundir

- **COE não tem FGC.**
- **COE não tem liquidez diária.**

#### Frase de fixação

> **Emitido só por banco, com DIE, prazo marcado e sem FGC.**

#### Alinhamento ao PD

CPA 2.1.1.4.1.

---

### 3.3 Capital protegido × capital em risco — 8 min

#### Como funciona

| Critério | Valor nominal protegido | Valor nominal em risco |
| --- | --- | --- |
| Pagamento mínimo | **100%** do valor investido no vencimento | Só uma **parcela** do valor investido, definida antes (pode ser perda total) |
| Risco do investidor | **Custo de oportunidade** e perda do poder de compra; **risco de crédito do emissor** | **Perda de capital** + risco de crédito do emissor |
| Potencial de ganho | Menor (participação e teto) | Maior, como compensação |

#### Exemplo prático

**COE protegido (R$ 10.000, 3 anos):** S&P 500 como referência, participação de 80% na alta, teto de 15%.

| Cenário do S&P 500 | Cálculo | Resultado bruto |
| --- | --- | --- |
| +10% | 80% × 10% = 8% | **R$ 10.800** |
| +30% | 80% × 30% = 24% → teto de 15% | **R$ 11.500** |
| −20% | Capital protegido | **R$ 10.000** |

**COE em risco (R$ 10.000, 3 anos):** ação como referência, participação de 150% na alta, barreira de −40%.

| Cenário da ação | Resultado bruto |
| --- | --- |
| +30% | 150% × 30% = 45% → **R$ 14.500** |
| 0% | **R$ 10.000** |
| −20% (barreira não atingida) | Segue a queda → **R$ 8.000** |
| −50% (barreira atingida) | Segue a queda → **R$ 5.000** |

#### O que a prova pode confundir

- **"Protegido" não é "sem risco"**: se o emissor quebrar, o investidor pode perder, e não há FGC.
- **Protegido tem teto e participação**: o ganho costuma ser limitado.

#### Frase de fixação

> **Protegido devolve o capital se o banco pagar; em risco pode devolver menos — e nenhum dos dois tem FGC.**

#### Alinhamento ao PD

CPA 2.1.1.4.2.

---

### 3.4 Tributação — 4 min

#### Como funciona

| Ponto | Regra (material e apostila) |
| --- | --- |
| IR | **Tabela regressiva da renda fixa**: 22,5% (até 180 dias), 20% (181 a 360), 17,5% (361 a 720), 15% (acima de 720) |
| Momento | **Retido na fonte no vencimento** (ou na liquidação) |
| Come-cotas | **Não há** (não é fundo) |
| IOF | O material informa que não incide IOF regressivo, porque não há resgate antes de 30 dias |

#### Exemplo prático

COE protegido do exemplo, 3 anos (acima de 720 dias), ganho de R$ 1.500: IR 15% = **R$ 225** → líquido **R$ 11.275**.

#### O que a prova pode confundir

- **COE segue a tabela da renda fixa**, mesmo quando o ativo de referência é de renda variável.

#### Frase de fixação

> **COE paga IR como renda fixa: tabela regressiva, retido na fonte, sem come-cotas.**

#### Alinhamento ao PD

CPA 2.1.1.4.3.

## 4. Por que isso cai na prova? — 4 min

### Explicação estratégica

A CPA cobra o COE por **características** (quem emite, FGC, liquidez, DIE), pelas **modalidades** (protegido × em risco) e pela **tributação**. As pegadinhas exploram a palavra "protegido" e o FGC.

### Pontos de atenção

1. **Estrutura:** renda fixa + derivativos.
2. **Emissor:** só instituição financeira.
3. **DIE** obrigatório, com os cenários.
4. **Sem FGC, sem liquidez diária, prazo determinado.**
5. **Protegido:** 100% do capital no vencimento, sujeito ao risco do emissor. **Em risco:** pode perder parte ou todo o capital.
6. **Tributação:** tabela regressiva, IR retido na fonte, sem come-cotas.

### Comparações que a prova pode explorar

| Conceito A | Conceito B | Diferença decisiva |
| --- | --- | --- |
| Valor nominal protegido | Valor nominal em risco | Devolve 100% × devolve parcela definida |
| COE | CDB | Sem FGC × com FGC |
| COE | Fundo | Sem come-cotas × com come-cotas |
| Participação | Cap | % da alta repassada × ganho máximo |

### Palavras-chave da prova

- **"Estrutura com derivativos"**: COE.
- **"Documento de Informações Essenciais"**: DIE.
- **"Emissor"**: instituição financeira.
- **"Barreira"**: nível que muda o resultado.

### Pegadinhas

- "O COE de capital protegido é garantido pelo FGC." **Errado.**
- "O COE pode ser emitido por qualquer companhia aberta." **Errado.**
- "O COE sofre come-cotas." **Errado.**
- "O COE protegido não tem nenhum risco." **Errado.**

### Frase de fixação

> **Protegido pelo banco, não pelo FGC.**

## 5. Case — 3 min

### Situação

> Seu Antônio, 68 anos, perfil conservador, tem R$ 50 mil. O gerente oferece um COE de 4 anos atrelado a ações de tecnologia, com participação de 150% e barreira de −30%, capital em risco. Seu Antônio diz: "Se é de banco, é garantido pelo FGC, então tudo bem." Ele pode precisar do dinheiro em 1 ano.

### Conceitos aplicados

| Ponto | Conceito | Problema |
| --- | --- | --- |
| Capital em risco | Pode perder parte ou todo o capital | Incompatível com perfil conservador |
| "Garantido pelo FGC" | COE não tem FGC | Informação errada |
| Precisa em 1 ano, prazo de 4 | Sem liquidez diária | Descasamento de prazo |
| Produto complexo | Suitability | Oferta inadequada |

### Análise passo a passo

1. **Perfil:** conservador × capital em risco → inadequado.
2. **FGC:** não cobre COE.
3. **Liquidez:** prazo maior que a necessidade.

### Síntese do case

O COE certo para Seu Antônio, se algum, seria **protegido**, com prazo compatível e explicação clara do **risco do emissor**.

### Frase de fixação

> **COE certo = perfil certo + prazo certo + risco do emissor explicado.**

## 6. Questão final comentada — 3 min

**Certificação:** CPA · **Competência:** 2.1.1.4.2 Níveis de risco e garantias · **Nível:** Médio

### Questão

Um investidor aplicou R$ 20.000,00 em um COE de valor nominal protegido, com prazo de 2 anos, participação de 70% na alta de um índice e teto de ganho de 10% sobre o valor aplicado. No vencimento, o índice subiu 20%. Desconsiderando tributos, o valor bruto recebido será de:

A) R$ 24.000,00.

B) R$ 22.800,00.

C) R$ 22.000,00.

D) R$ 20.000,00.

### Ponto-chave do enunciado

Participação de **70%** e **teto de 10%**.

### Gabarito

**Alternativa C.**

### Comentário da alternativa correta

A participação daria 70% × 20% = **14%**, mas o **teto é de 10%**. Ganho: 10% × 20.000 = R$ 2.000 → **R$ 22.000,00**.

### Por que as demais estão incorretas?

- **A:** repassou 100% da alta (20%), ignorando participação e teto.
- **B:** aplicou a participação (14%), mas ignorou o **teto**.
- **D:** seria o resultado com o índice em queda ou estável; aqui o índice subiu.

### Armadilhas e macetes

- **Primeiro a participação, depois compare com o teto.**

### Referência

Res. CMN 5.166/2024; Res. CVM 8/2020; APOSTILA-CPA p. 282–284; Programa Detalhado CPA, item 2.1.1.4.

## 7. Revisão final — 2 min

### Resumo em cinco pontos

1. COE: renda fixa + derivativos, emitido só por instituição financeira, com cenários conhecidos antes.
2. Regras: DIE obrigatório, prazo determinado, sem liquidez diária, sem FGC; resgate antecipado só nas condições do emissor.
3. Valor nominal protegido: devolve 100% no vencimento, sujeito ao risco do emissor. Valor nominal em risco: devolve só a parcela definida.
4. Elementos: ativo de referência, participação, cap e barreira; estratégias direcionais ou neutras.
5. Tributação: tabela regressiva da renda fixa, IR retido na fonte, sem come-cotas. Norma atual: Res. CMN 5.166/2024 (nota).

### Quadro de emergência

| Tema | Regra-chave |
| --- | --- |
| Estrutura | Renda fixa + derivativos |
| Emissor | Só instituição financeira |
| Informação | DIE com cenários |
| Liquidez | Prazo determinado · sem liquidez diária |
| FGC | Não tem |
| Protegido × em risco | 100% no vencimento × parcela definida |
| Tributação | Tabela regressiva · sem come-cotas |
| Norma | Res. CMN 5.166/2024 (revogou 4.263) · Res. CVM 8/2020 |

### Cadeia lógica

> banco monta a estrutura → DIE mostra os cenários → investidor escolhe protegido ou em risco → vencimento → IR pela tabela regressiva

### Diferenças que não podem ser confundidas

- **Protegido ≠ sem risco** (risco do emissor).
- **COE ≠ CDB** (sem FGC).
- **Participação ≠ cap.**

### Frase central da aula

> **O pacote tem volta garantida só enquanto a agência existir — e não há FGC para o COE.**

### Próximo passo de estudo

Resolver 10 questões de cenários de COE (participação, teto, barreira). Próximo item do PD: 2.1.2 Introdução aos fundos de investimento.

## Referências oficiais e status

Último acesso: 2026-09-25.

1. ANBIMA — Programa Detalhado CPA — vigência 01/01/2026 — item 2.1.1.4 — [Programas Detalhados ANBIMA](https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm). **Em vigor.**
2. CMN — Resolução CMN 5.166/2024 — COE (revogou a Res. CMN 4.263/2013) — [LegisWeb](https://www.legisweb.com.br/legislacao/?id=463540) · [ANBIMA — informe de legislação](https://www.anbima.com.br/pt_br/informar/regulacao/informe-de-legislacao/certificados-de-operacoes-estruturadas-coe.htm). **Em vigor.** Texto oficial **não reaberto nesta sessão**.
3. CVM — Resolução CVM 8/2020 — oferta pública de COE e DIE. **Em vigor.** **Texto não reaberto nesta sessão.**
4. FGC — produtos cobertos (COE fora da cobertura) — [fgc.org.br](https://www.fgc.org.br/garantia-fgc/sobre-a-garantia-fgc). **Em vigor.** **Não reaberto nesta sessão.**
5. Tributação do COE (tabela regressiva; IOF): conforme material e apostila; norma específica **não confirmada nesta sessão**.

Fontes de origem (não oficiais): PDF A3501 "COE — Certificado de Operações Estruturadas" (`00-fontes/materiais-aula/topico-2.1.1.2.2.2-eventos-indices-governanca-tributacao-rv-coe/`); APOSTILA-CPA, p. 282–284.
