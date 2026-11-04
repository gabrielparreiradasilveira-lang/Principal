# Design: roteiro e lousas numa skill só (`roteiro-lousa-aprofundado`, versão 4)

Data: 04/11/2026 · Autor: Claude, a partir da conversa com o professor Gabriel (X8 Educação)

## 1. Por quê

O professor grava videoaulas para certificações financeiras (ANBIMA CPA, C-Pro R, C-Pro I, CFG, CGA, CGE e CFP) assim:

- a **lousa pronta** (PNG 1920×1080, fundo preto) é o **fundo parado** de um slide no **Google Slides**;
- ele fala lendo o **roteiro** que a skill entrega;
- com a **Wacom**, ele só **circula, sublinha e puxa setas** sobre a lousa (a letra dele não é boa para escrever);
- as contas, ele faz **ao vivo** num emulador da HP12C no computador.

Hoje, o roteiro sai desta skill (`Skill Creator/roteiro-lousa-aprofundado/`, branch `claude/nice-thompson-i4lha9`), e as lousas saem de outra sessão, com a skill `lousa-manuscrita` (branch `claude/admiring-euler-76f74n`, pasta `.claude/skills/lousa-manuscrita/`), que relê o roteiro e resume. Resultado, nas lousas da R50 e da R60: metade da tela vazia, só palavras-chave, metáfora sem desenho, exercício com "?" e sem resposta.

O professor quer **uma skill só** que entregue o roteiro e as lousas, com lousas **mais completas**, salvas no GitHub, no Drive e direto no Google Slides.

## 2. Metas

1. **Um pedido, tudo pronto.** "Cria o roteiro da R62" entrega: o roteiro (Google Doc), as lousas (PNG e JSON no GitHub) e uma apresentação no Google Slides com uma lousa por slide, como fundo.
2. **Roteiro em 4 blocos por vídeo:** 1. Abertura (destruição de mito) · 2. Metáfora central · 3. Conteúdo técnico · 4. Resolução rápida (o antigo bloco 5). Sai o bloco de pegadinhas (lousa e fala) e sai a Nota de bastidor. A tabela de teclas da HP12C continua no bloco de resolução do roteiro.
3. **Uma lousa por bloco** (4 por vídeo). Só divide em (1/2) e (2/2) se não couber.
4. **A lousa complementa a fala, não a repete.** Fica ligada ao bloco (mesma metáfora, mesmos conceitos), mas traz o que a fala não mostra: condições de uso, caso-limite, números, um segundo exemplo, a metáfora desenhada, o erro de quem escolhe mal. Tudo verdadeiro e tirado do conteúdo da aula (Programa Detalhado, apostila, normas); nada inventado.
5. **Densidade:** a quantidade de informação das amostras da lousa "Duas rodovias", que o professor aprovou (seção 9). Tela útil ocupada, respeitando os cantos do logo e da webcam. Letra do corpo entre 30 e 34 px (o professor disse que não precisa de letra maior).
6. **Metáfora sempre desenhada.** Se a biblioteca não tiver o desenho, a skill cria um (como o `rodovia_pedagio` da amostra).
7. **Exercício resolvido na lousa:** os cenários, as contas resumidas e o resultado. As teclas da HP ficam só no roteiro.
8. **Padrão visual X8 mantido:** fundo preto chapado, letra de mão em caixa alta, título amarelo sublinhado, subtítulo ciano, texto branco, destaques laranja, verde (certo) e vermelho (errado), cantos livres (logo: x ≥ 1560 e y ≤ 190; webcam: x ≥ 1600 e y ≥ 760), mínimo de 28 px.
9. **Goodnotes sai do texto da skill.** O professor usa Google Slides (o Goodnotes veio da skill original `roteiro-validado-lousa`).

## 3. Fora do escopo

- Lousa em etapas (vários slides revelando partes): as marcas da Wacom somem ou ficam fora do lugar ao trocar de slide.
- Espaço em branco para o professor escrever.
- Reescrever o motor de desenho.
- Alterar a skill `lousa-manuscrita` ou a sessão que a usa.
- Mudar a pesquisa, o inventário de profundidade, o ritmo de 95 palavras por minuto ou a divisão em vídeos de 6 a 8 minutos.

## 4. O que seria fracasso mesmo funcionando

- Lousa que contradiz a fala ou traz número ou regra sem fonte real.
- Lousa que é cópia da fala.
- Texto cortado ou dentro dos cantos do logo e da webcam.
- Dizer que salvou no Drive ou no Slides sem a ferramenta confirmar.

## 5. Restrições

- **Motor:** Python 3 e Pillow (`python-pptx` só para o `.pptx` de reserva). Fontes incluídas (Permanent Marker e Pangolin, licença OFL; os arquivos de licença vão junto).
- **Instalável como skill da conta** (zip): todos os caminhos relativos à pasta da skill.
- **Google Slides** (conector com a permissão "perguntar antes de alterar"): testado em 04/11/2026, `update_presentation` com `createSlide` (layout `BLANK`) e `updatePageProperties` → `pageBackgroundFill.stretchedPictureFill.contentUrl` põe o PNG como fundo; o Google copia a imagem no momento. A URL precisa ser pública: o PNG vai antes para o GitHub (repositório público) e é referenciado pelo SHA do commit (`raw.githubusercontent.com/<dono>/<repo>/<sha>/<caminho>`). Apresentação nova: `create_file` do Drive com `contentMimeType` `application/vnd.google-apps.presentation`, sem conteúdo; apagar o slide inicial (`p`).
- **O Drive não recebe PNG pelo conector:** o modelo teria de digitar o arquivo inteiro em base64.
- **Orçamento de fala:** sem o bloco de pegadinhas (cerca de 90 palavras), redistribuir para manter 570 a 760 palavras por vídeo.
- **O conferidor** (`scripts/conferir_roteiro.py`) passa a esperar 4 blocos e deixa de exigir a Nota de bastidor.
- **SKILL.md abaixo de 500 linhas;** as regras de lousa vão para `references/lousas.md`.

## 6. Abordagens

| | Abordagem | Situação |
|---|---|---|
| A | Copiar o motor da `lousa-manuscrita` (`lousa.py`, `moldes.py`, `desenhos.py`, fontes) para `scripts/lousa/` desta skill e evoluir aqui | **Escolhida** |
| B | Deixar duas skills e encadear | Descartada: contraria "uma skill só" e mantém a releitura do roteiro |
| C | Reescrever o motor | Descartada: o motor atual reproduz 35 de 35 lousas byte a byte |

Entrega: **direto no Google Slides** (escolhido; o professor ativou o conector). Se o conector não estiver disponível na sessão, a skill gera o `.pptx`, sobe para o GitHub e avisa que não criou a apresentação.

## 7. Decidido pelo professor

- Lousa pronta, fundo parado de slide no Google Slides; Wacom só para marcar; contas ao vivo na HP do computador; sem espaço em branco.
- Fundo preto como padrão.
- Uma skill só; lousas mais completas; motor de desenho mantido; metáfora desenhada; exercício com resolução.
- Lousa ligada à fala, mas sem repetir a fala; informação correta, do conteúdo, não inventada; a quantidade da amostra 2 está boa.
- Sem o bloco de pegadinhas (lousa e fala); sem Nota de bastidor; tabela da HP12C mantida no roteiro.
- Salvar no GitHub e no Drive; entregar no Google Slides.
- Uma apresentação por aula: a série inteira numa apresentação só (12 slides na R50), na ordem dos vídeos.

## 8. Decisões minhas (para o professor conferir)

1. **Tempo dos blocos** (total de cerca de 665 palavras, 7 min): abertura ~70 · metáfora ~100 · conteúdo ~370 · resolução ~125 palavras.
2. **Fontes sem Nota:** a checagem continua (fontes oficiais, contas recalculadas, contraexemplo). Ponto não confirmado fica marcado **[VERIFICAR]** no próprio texto e listado na mensagem de entrega.
3. **Bloco "[Ação na Lousa]" do roteiro** passa a trazer: o número do slide e de 1 a 3 marcações sugeridas, ligadas à fala ("ao dizer 'carga inteira', circule VALOR TOTAL"). O conteúdo da lousa fica só na lousa.
4. **Drive:** roteiro (Doc) e apresentação (Slides) na mesma pasta, com os nomes `Rxx · skill nova · Tema (itens do PD)` e `Rxx · skill nova · Tema (itens do PD) · lousas`. O Doc ganha o link da apresentação no topo. Não haverá Doc separado com as lousas.
5. **Repositório:** lousas em `aulas-certificacoes/materiais/{cert}/lousas/{rxx-tema}/` (JSON e PNG), a convenção que já existe.
6. **Primeiro teste:** refazer a série R50 (VGBL, 3 vídeos) com a skill nova, para comparar lado a lado com as lousas da outra sessão.
7. **A skill antiga:** depois da validação, aviso o professor de que a outra sessão pode parar de usar a `lousa-manuscrita`. Não mexo naquela sessão.

8. **Onde a skill roda:** numa sessão do Claude Code com o repositório `gabrielparreiradasilveira-lang/Principal` (público) clonado. O motor gera os PNGs, a skill faz commit e push na branch da sessão e só depois cria os slides, porque a URL usa o SHA de um commit já enviado. Num chat sem git (só conectores), a skill gera os PNGs se puder executar Python, entrega como arquivo e avisa que eles não foram para o GitHub nem para o Slides.
9. **Quem escreve a lousa:** o modelo, a partir do inventário, escreve o JSON nos campos dos moldes; os scripts só desenham e conferem. Não há parser do roteiro.
10. **Pasta e refação:** a pasta do Drive segue a regra atual (a pasta do Rxx−1). Numa refação, cria-se uma apresentação nova com sufixo (2), (3)…; a anterior nunca é apagada.
11. **Insumos do teste da R50:**
    - o roteiro no Drive (id `1FDmX27LKOHffUCA2caZ9fiPN9uPToxHCAp05HTQiBJU`);
    - o PD e a apostila no Drive (busca da Etapa 0);
    - as lousas antigas em `origin/claude/admiring-euler-76f74n:aulas-certificacoes/materiais/cpro-r/lousas/r50-vgbl/`.

    As lousas novas vão para `aulas-certificacoes/materiais/cpro-r/lousas/r50-vgbl-skill-nova/`, para não colidir com a pasta da outra sessão.
12. **Limiares das conferências:**
    - "Área útil ocupada" significa que o conteúdo cobre pelo menos 70% da altura útil.
    - "Frase igual à fala" significa 8 palavras seguidas idênticas, depois de normalizar maiúsculas e pontuação.
13. **Alcance da mudança para 4 blocos:** SKILL.md, `references/exemplo-item.md`, `references/analogias.md`, a Etapa 3 (plano da série) e o conferidor.

## 9. Referência de densidade e de complemento (amostra 2)

O professor aprovou a quantidade de informação. O jeito de complementar a fala, mostrado abaixo, foi a proposta que levou à decisão "ligada à fala, mas sem repetir".

Lousa do bloco 2 da R50-1, "Duas rodovias até a aposentadoria", comparada com a fala do mesmo bloco:

| Na fala | Na lousa |
|---|---|
| As duas rodovias e o que é cada pedágio | O mesmo, desenhado (rodovia com cabine na entrada e na saída) |
| — | Condição do vale-pedágio do PGBL: declaração completa e, em regra, contribuição ao INSS ou a regime próprio |
| "A tarifa da saída depende do regime e do prazo" | A tarifa em números: regressivo de 35% a 10%; progressivo pela tabela do IR |
| Exemplo do bloco de resolução (saldo de R$ 150 mil) | Outro exemplo: R$ 50 mil aportados viraram R$ 80 mil; base de R$ 30 mil no VGBL e de R$ 80 mil no PGBL |
| — | "Rodovia errada": PGBL na declaração simplificada não usa o vale e paga pedágio sobre a carga inteira |

Arquivos da amostra (descartáveis): o JSON e o desenho `rodovia_pedagio` estão no scratchpad da sessão; o builder recria a partir desta descrição.

## 10. Deixado para quem constrói

- O código dos moldes novos ou ajustados (por exemplo, comparação com a metáfora desenhada e exercício resolvido) e o cálculo de enchimento da tela.
- Os desenhos novos.
- As conferências automáticas: avisos zerados, ocupação da área útil, cantos livres, e nenhuma frase da lousa igual a uma frase da fala.
- A conversão do plano da lousa (feito no inventário) em JSON para o motor.
- Os testes.

## 11. Como saber que deu certo

- A série R50 refeita: 3 vídeos × 4 lousas, zero aviso do gerador, área útil ocupada, metáfora desenhada, exercício resolvido.
- Apresentação no Google Slides com 12 slides, cada um com a lousa como fundo (miniatura conferida).
- Roteiro no Drive com 4 blocos, sem Nota de bastidor, e o conferidor sem pendência.
- O professor aprova a densidade e o jeito de complementar a fala.
