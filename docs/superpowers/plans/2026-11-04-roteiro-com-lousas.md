# Skill única de roteiro e lousas: plano de implementação

> **Para agentes:** sub-skill obrigatória: superpowers:subagent-driven-development (recomendada) ou superpowers:executing-plans, tarefa por tarefa. Os passos usam caixas de seleção (`- [ ]`).

**Objetivo:** a skill `roteiro-lousa-aprofundado` passa a entregar o roteiro em 4 blocos, uma lousa X8 por bloco (PNG) e uma apresentação no Google Slides com as lousas como fundo.

**Arquitetura:**
- O motor de desenho da `lousa-manuscrita` é copiado sem mudanças para `scripts/` desta skill: `lousa.py`, `moldes.py`, `desenhos.py`, com as fontes em `assets/fontes/`. O `lousa.py` já procura as fontes em `<raiz>/assets/fontes`, então não precisa ser alterado.
- Novos moldes e um desenho novo produzem lousas mais completas.
- Dois scripts novos: `conferir_lousas.py` (avisos, ocupação e repetição da fala) e `slides.py` (pedidos de batchUpdate para o conector do Slides).
- O modelo escreve o JSON das lousas a partir do inventário; os scripts só desenham e conferem.

**Tecnologia:** Python 3 e Pillow; testes com `unittest` da biblioteca padrão (o `pytest` não está instalado); conectores do Google Drive e do Google Slides.

**Design:** `docs/superpowers/specs/2026-11-04-roteiro-com-lousas-design.md`

Pasta da skill (chamada de `S` abaixo): `Skill Creator/roteiro-lousa-aprofundado/`. Branch: `claude/nice-thompson-i4lha9`. Origem do motor: `origin/claude/admiring-euler-76f74n`, commit `42ac894`, pasta `.claude/skills/lousa-manuscrita/`.

## Restrições gerais

- **Lousa:**
  - PNG 1920×1080, fundo preto chapado (`"fundo": "preto"`), caixa alta.
  - Cores: título amarelo sublinhado; subtítulo ciano; texto branco; destaques laranja, verde (certo) e vermelho (errado).
- **Cantos livres:** logo em x ≥ 1560 e y ≤ 190; webcam em x ≥ 1600 e y ≥ 760.
- **Letra:** corpo entre 30 e 34 px; mínimo absoluto de 28 px.
- **Uma lousa por bloco:** 4 por vídeo. Só se divide em (1/2) e (2/2) se não couber.
- **Roteiro:**
  - 4 blocos: 1. Abertura (destruição de mito), 2. Metáfora central, 3. Conteúdo técnico, 4. Resolução rápida.
  - Sem bloco de pegadinhas, sem "Nota de bastidor"; a tabela de teclas da HP12C fica no bloco 4.
- **Fala:** 95 palavras por minuto; de 570 a 760 palavras por vídeo, com alvo de 665. Alvo por bloco: 70 / 100 / 370 / 125.
- **Lousa complementa a fala:** nenhuma sequência de 8 palavras idênticas entre a lousa e a fala do mesmo bloco, depois de normalizar maiúsculas, acentos de caixa, pontuação e marcações `{cor:…}` e `[TECLA]`.
- **Ocupação:** o conteúdo da lousa cobre pelo menos 70% da altura útil.
- **Nomes dos PNG:** `{video}_{bloco}_{slug}.png`, em que `{video}` é o id do vídeo em minúsculas (`r60a`, `r50-1`).
- **Drive:**
  - Nomes: `Rxx · skill nova · Tema (itens do PD)` para o roteiro e `Rxx · skill nova · Tema (itens do PD) · lousas` para a apresentação.
  - Uma apresentação por aula.
  - Pasta: a do Rxx−1.
  - Refação ganha sufixo (2), (3)…; nunca se apaga a versão anterior.
- **Slides:** a URL da imagem usa o SHA de um commit já enviado (`https://raw.githubusercontent.com/<dono>/<repo>/<sha>/<caminho>`, com cada trecho do caminho codificado).
- **Texto da skill:** sem "Goodnotes"; o professor usa Google Slides. SKILL.md com menos de 500 linhas.

## Foco da revisão

1. **Caminho com espaço** (`Skill Creator/...` ou `aulas-certificacoes/...` com acento) na URL do GitHub: precisa sair codificado (`%20`), ou o Google não baixa a imagem. Teste na Tarefa 5.
2. **Slug com acento ou longo virando `objectId` do Slides:** o id precisa ter de 5 a 50 caracteres em `[A-Za-z0-9_-]`. Teste na Tarefa 5.
3. **Repetição da fala escondida por acento, caixa ou marcação** (`{laranja:CARGA INTEIRA}` × "carga inteira"): precisa ser detectada. Teste na Tarefa 4.
4. **Id de vídeo nos dois formatos** (`R60A` e `R50-1`), no roteiro e no nome do PNG: os dois são aceitos. Testes nas Tarefas 4 e 6.
5. **Tinta só no canto da webcam ou do logo não conta como ocupação.** Teste na Tarefa 4.

---

### Task 1: Copiar o motor e provar que ele reproduz as lousas

**Arquivos:**
- Criar (cópia exata da origem): `S/scripts/lousa.py`, `S/scripts/moldes.py`, `S/scripts/desenhos.py`, `S/assets/fontes/` (PermanentMarker-Regular.ttf, Pangolin-Regular.ttf, LICENSE-PermanentMarker.txt, LICENSE-Pangolin-OFL.txt).
- Criar: `S/tests/fixtures/mito-x-verdade.json` e `.png` (de `assets/exemplos/` da origem) e `S/tests/test_motor.py`.

**Interfaces:**
- Produz: o CLI `python3 S/scripts/lousa.py roteiro.json -o pasta [--grade] [--pptx arq]`, a classe `lousa.Lousa(spec, pasta_roteiro, avisos)` e `lousa.main(argv) -> int`, sem mudança em relação à origem.

- [ ] **Passo 1:** copiar os arquivos com `git show origin/claude/admiring-euler-76f74n:<caminho> > destino` (para as fontes, `git show` redirecionado ao arquivo binário funciona).
- [ ] **Passo 2:** escrever `test_motor.py::TesteMotor.test_reproduz_exemplo`: renderiza a fixture numa pasta temporária, chamando `lousa.main([json, "-o", tmp])`, e compara os bytes do PNG com a fixture (`assertEqual`).
- [ ] **Passo 3:** rodar `python3 -m unittest discover -s "S/tests" -v` e esperar OK. Se falhar, a cópia está errada; não "conserte" o teste.
- [ ] **Passo 4:** commit `Copia o motor de lousas para a skill roteiro-lousa-aprofundado`.

### Task 2: Desenho `rodovia_pedagio` e molde `comparacao`

**Arquivos:**
- Modificar: `S/scripts/desenhos.py` (nova entrada em `DESENHOS`) e `S/scripts/moldes.py` (função `comparacao` e registro em `MOLDES`).
- Teste: `S/tests/test_moldes.py`.

**Interfaces:**
- Produz o molde `"molde": "comparacao"`, com os campos:
  - `titulo: str`;
  - `colunas: [{titulo: str, desenho: str | {nome, largura}, rotulos: [str, str] (opcional; ficam embaixo do desenho, à esquerda e à direita, em laranja, 28 px), texto: str}]` (exatamente 2);
  - `faixas: [str]` (linhas de largura total abaixo das colunas);
  - `destaque: str | {texto, cor, moldura}` (frase emoldurada na base).

- [ ] **Passo 1:** acrescentar `rodovia_pedagio` (aspecto 0,26; duas bordas de estrada, faixa central tracejada, cabine com cancela à esquerda e à direita), com os traços abaixo, que já foram testados na amostra:
  ```python
  ("linha", [(0.0, 0.17), (0.5, 0.168), (1.0, 0.172)]), ("linha", [(0.0, 0.25), (0.5, 0.252), (1.0, 0.248)]),
  ("linha", [(0.27, 0.21), (0.33, 0.21)]), ("linha", [(0.42, 0.21), (0.48, 0.21)]), ("linha", [(0.57, 0.21), (0.63, 0.21)]),
  ("fechada", [(0.05, 0.155), (0.05, 0.05), (0.16, 0.05), (0.16, 0.155)]),
  ("fechada", [(0.035, 0.05), (0.175, 0.05), (0.16, 0.015), (0.05, 0.015)]),
  ("fechada", [(0.08, 0.07), (0.13, 0.07), (0.13, 0.11), (0.08, 0.11)]), ("grossa", [(0.16, 0.13), (0.25, 0.13)]),
  ("fechada", [(0.84, 0.155), (0.84, 0.05), (0.95, 0.05), (0.95, 0.155)]),
  ("fechada", [(0.825, 0.05), (0.965, 0.05), (0.95, 0.015), (0.84, 0.015)]),
  ("fechada", [(0.87, 0.07), (0.92, 0.07), (0.92, 0.11), (0.87, 0.11)]), ("grossa", [(0.84, 0.13), (0.75, 0.13)]),
  ```
- [ ] **Passo 2:** escrever `test_moldes.py::test_comparacao_amostra_sem_avisos`, que monta a lousa "Duas rodovias" com o molde (textos da seção 9 do design: colunas VGBL e PGBL, faixas "TARIFA DA SAÍDA…" e "CARGA DE EXEMPLO…", destaque "RODOVIA ERRADA…" com moldura vermelha). Asserções:
  - `avisos == []`;
  - o PNG existe e tem 1920×1080;
  - `conferir_lousas.ocupacao(png) >= 0.70`. Esta asserção entra na Tarefa 4; até lá, fica marcada com `@unittest.skip("Tarefa 4")`.
- [ ] **Passo 3:** rodar o teste e esperar ERRO (`molde 'comparacao' não existe`).
- [ ] **Passo 4:** implementar `comparacao(L, spec, els)` em `moldes.py` com a geometria da amostra aprovada:
  - subtítulos em y 132 (x 80 e x 1000), sublinhados;
  - desenhos em y 196, largura 660, em x 130 e x 1050;
  - rótulos em y 380;
  - textos das colunas em y 432 (x 80 com largura 820; x 1000 com largura 860), no maior tamanho de [34, 33, 32, 31, 30] que termine até y 735;
  - linha vertical à mão em x ≈ 945;
  - faixas a partir de y 750, x 80, largura 1500, 30 px, empilhadas com 12 px de folga;
  - destaque com a mesma lógica de `_destaque`, com largura de 1440 e x 100, ancorado na base.

  Se as faixas invadirem o destaque, reduzir o tamanho das faixas até 28 px e, se ainda não couber, avisar (`L.avisos`).
- [ ] **Passo 5:** rodar e esperar OK. Abrir o PNG e comparar com a amostra 2: as duas devem ficar equivalentes.
- [ ] **Passo 6:** commit `Molde comparacao e desenho rodovia_pedagio`.

### Task 3: Moldes `exercicio` e `mito_verdade` com apoio

**Arquivos:**
- Modificar: `S/scripts/moldes.py`.
- Teste: `S/tests/test_moldes.py`.

**Interfaces:**
- Produz `"molde": "exercicio"`, com os campos:
  - `titulo: str`;
  - `dados: str` (enunciado em tópicos, largura total);
  - `cenarios: [{titulo: str, passos: str, resultado: str}]` (2 colunas; `resultado` em verde, emoldurado);
  - `conclusao: str | {texto, cor, moldura}` (destaque na base).
- `mito_verdade` ganha o campo opcional `apoio: str`: tópicos em largura total, abaixo do mito e da verdade, a partir de y ≥ 640, entre 30 e 34 px.

- [ ] **Passo 1:** escrever `test_exercicio_r50_1_sem_avisos`, com os dados do bloco 5 da R50-1:
  - saldo de R$ 150.000, com R$ 100.000 aportados, alíquota de 10% e resgate de R$ 30.000;
  - cenário VGBL: "20% DO SALDO → SAEM R$ 20.000 DE APORTE\nRENDIMENTO = R$ 10.000", resultado "IR = R$ 1.000";
  - cenário PGBL: "BASE = VALOR TOTAL = R$ 30.000", resultado "IR = R$ 3.000".

  Asserções: `avisos == []`, e "R$ 1.000" e "R$ 3.000" presentes no JSON expandido (os elementos gerados por `moldes.expandir`).
- [ ] **Passo 2:** escrever `test_mito_verdade_com_apoio_sem_avisos`, com o mito e a verdade da R50-1 e o apoio "- VGBL: R$ 94,5 BILHÕES DE JAN. A AGO./2026 (CERCA DE 90% DOS APORTES)\n- ...". Asserções: `avisos == []` e, quando houver apoio, o maior `y` dos elementos do apoio deve ser maior que 640.
- [ ] **Passo 3:** rodar os testes e esperar falha nos dois.
- [ ] **Passo 4:** implementar `exercicio` e o campo `apoio`. Usar `_maior_que_cabe`, `_titulo` e `_destaque`, que já existem, e respeitar os cantos livres; o canto da webcam vale para tudo abaixo de y 760.
- [ ] **Passo 5:** rodar e esperar OK. Abrir os dois PNG.
- [ ] **Passo 6:** commit `Moldes exercicio e mito_verdade com apoio`.

### Task 4: `conferir_lousas.py`

**Arquivos:**
- Criar: `S/scripts/conferir_lousas.py`.
- Teste: `S/tests/test_conferir_lousas.py`.

**Interfaces:**
- Consome: `lousa.Lousa` e `lousa.main` (Tarefa 1).
- Produz:
  - `ocupacao(png: str) -> float`: (y da última linha com tinta − 120) ÷ (1040 − 120), entre 0 e 1. "Tinta" é um pixel com algum canal maior que 40, ignorando os retângulos do logo e da webcam.
  - `normalizar(texto: str) -> list[str]`: tira `{cor:` e `}`, troca `[TECLA]` por `TECLA`, passa para maiúsculas, tira a pontuação e devolve as palavras.
  - `repeticoes(lousa: str, fala: str, n: int = 8) -> list[str]`: as sequências de `n` palavras que aparecem nas duas.
  - `video_bloco(nome_png: str) -> tuple[str, int] | None`: lê `^(r\d{2,3}(?:-\d|[a-z]))_([1-4])_` no nome do arquivo.
  - CLI `python3 S/scripts/conferir_lousas.py roteiro.md lousas.json [-o pasta]`, que:
    - renderiza tudo;
    - lista os avisos do gerador, a ocupação abaixo de 0,70, as repetições contra a fala do mesmo vídeo e bloco (lida no roteiro com a mesma separação do `conferir_roteiro.py`), os PNG sem vídeo ou bloco reconhecido e os vídeos que não têm as 4 lousas (como aviso, não pendência, quando houver lousa (1/2));
    - sai com 1 se houver pendência.

- [ ] **Passo 1:** escrever os testes abaixo e vê-los falhar:
  - `test_ocupacao_meia_tela`: imagem preta com retângulo branco de y 140 a 500 em x 80–900 → valor entre 0,40 e 0,42;
  - `test_ocupacao_cheia`: retângulo até y 1000 → valor ≥ 0,95;
  - `test_ocupacao_ignora_webcam`: tinta só em x 1700, y 900 → 0,0;
  - `test_repeticao_com_marcacao`: lousa "PEDÁGIO SOBRE A {vermelho:CARGA INTEIRA} DO CAMINHÃO QUE SAI DA RODOVIA" × fala "o pedágio sobre a carga inteira do caminhão que sai da rodovia" → 1 repetição;
  - `test_sem_repeticao_com_7_palavras` → lista vazia;
  - `test_video_bloco`: "r50-1_2_metafora.png" → ("r50-1", 2); "r60a_4_resolucao.png" → ("r60a", 4); "abertura.png" → None.
- [ ] **Passo 2:** implementar as funções e o CLI.
- [ ] **Passo 3:** rodar e esperar OK. Tirar o `skip` da Tarefa 2 e rodar toda a pasta `tests`.
- [ ] **Passo 4:** commit `Conferidor de lousas: avisos, ocupação e repetição da fala`.

### Task 5: `slides.py`

**Arquivos:**
- Criar: `S/scripts/slides.py`.
- Teste: `S/tests/test_slides.py`.

**Interfaces:**
- Produz:
  - `url_raw(dono: str, repo: str, sha: str, caminho: str) -> str`, com cada trecho do caminho passado por `urllib.parse.quote`;
  - `object_id(i: int, nome_png: str) -> str`, no formato `lousa_{i:02d}_{slug}`, só com `[A-Za-z0-9_-]` (acento removido) e cortado em 50 caracteres;
  - `requisicoes(caminhos: list[str], dono: str, repo: str, sha: str, slide_inicial: str | None = "p") -> list[dict]`, que devolve, para cada PNG:
    - `{"createSlide": {"objectId": id, "slideLayoutReference": {"predefinedLayout": "BLANK"}}}`;
    - `{"updatePageProperties": {"objectId": id, "pageProperties": {"pageBackgroundFill": {"stretchedPictureFill": {"contentUrl": url}}}, "fields": "pageBackgroundFill"}}`;
    - e, no fim, `{"deleteObject": {"objectId": slide_inicial}}` quando `slide_inicial` não for `None`;
  - CLI `python3 S/scripts/slides.py --dono D --repo R --sha X png1 png2 …` (caminhos relativos à raiz do repositório), que imprime o JSON.

- [ ] **Passo 1:** escrever os testes abaixo e vê-los falhar:
  - `test_url_codifica_espaco`: o caminho "Skill Creator/a b.png" vira `.../Skill%20Creator/a%20b.png`;
  - `test_object_id_limites`: o nome "r50-1_2_metáfora-das-duas-rodovias-até-a-aposentadoria-longa.png" gera um id com tamanho entre 5 e 50 e que casa com `^[A-Za-z0-9_-]+$`;
  - `test_requisicoes_dois_pngs`: 5 pedidos na ordem create, update, create, update, delete, com as URLs corretas;
  - `test_sem_slide_inicial`: com `slide_inicial=None`, não há delete.
- [ ] **Passo 2:** implementar.
- [ ] **Passo 3:** rodar e esperar OK.
- [ ] **Passo 4:** commit `Gerador dos pedidos do Google Slides`.

### Task 6: Conferidor do roteiro com 4 blocos e sem Nota

**Arquivos:**
- Modificar: `S/scripts/conferir_roteiro.py`.
- Teste: `S/tests/test_conferir_roteiro.py`.

**Interfaces:**
- A regex de vídeo aceita `R\d{2,3}(?:[A-Z]|-\d)`.
- `BLOCO` passa a casar de 1 a 4; o vídeo precisa ter os blocos `[1, 2, 3, 4]`, com pelo menos 4 "Ação na Lousa" e 4 "Locução Direta".
- A presença de "Nota de bastidor" vira pendência ("o roteiro não leva Nota de bastidor").
- Saem as regras que liam a Nota. A regra da data passa a ser: sem data e sem "hipotétic" na fala → pendência; sem data, mas com "hipotétic" na fala → aviso.
- Os limites de palavras (570, 665, 760; aviso acima de 720) continuam.

- [ ] **Passo 1:** escrever os testes abaixo, com um roteiro sintético gerado no teste (função `roteiro(blocos, palavras_por_bloco, nota=False, video="R50-1")`), e vê-los falhar:
  - `test_quatro_blocos_ok` (70/100/370/125, com "em 2026" na fala) → código 0;
  - `test_cinco_blocos_pendencia` → código 1, com "blocos" na saída;
  - `test_nota_pendencia` → código 1;
  - `test_id_r60a_aceito` → código 0.
- [ ] **Passo 2:** alterar o conferidor e a docstring.
- [ ] **Passo 3:** rodar e esperar OK.
- [ ] **Passo 4:** commit `Conferidor do roteiro: 4 blocos e sem Nota de bastidor`.

### Task 7: SKILL.md e referências

**Arquivos:**
- Modificar: `S/SKILL.md`, `S/references/exemplo-item.md`, `S/references/analogias.md`.
- Criar: `S/references/lousas.md`.

**Conteúdo que cada arquivo precisa ter:**
- **SKILL.md:**
  - A descrição cita as lousas e a apresentação no Google Slides, aciona com "lousa" ou "lousas", tem no máximo 1024 caracteres e nenhum ": " fora de aspas.
  - Etapa 5 com o esqueleto de 4 blocos, e o bloco "[Ação na Lousa]" do roteiro com "Slide N" mais de 1 a 3 marcações para a Wacom ("ao dizer '…', circule …").
  - Etapa nova **"Lousas"**:
    - planejar no inventário uma lousa por bloco;
    - aplicar a regra "a lousa mostra o que a fala não mostra", com a tabela da seção 9 do design como exemplo;
    - escrever o JSON com os moldes;
    - rodar `conferir_lousas.py` e abrir cada PNG.
  - Etapa **"Entrega"**:
    - commit e push dos PNG e do JSON em `aulas-certificacoes/materiais/{cert}/lousas/{rxx-tema}/`;
    - `create_file` da apresentação na pasta do Rxx−1;
    - `read_presentation` para obter o id do slide inicial;
    - `slides.py` e `update_presentation`;
    - conferir a miniatura do primeiro e do último slide;
    - colocar o link da apresentação no topo do Doc;
    - plano de reserva (`.pptx` e aviso) quando faltar o conector ou o git;
    - nunca dizer que salvou sem a ferramenta confirmar.
  - Sem "Goodnotes", sem bloco de pegadinhas e sem Nota de bastidor (a checagem de fontes continua; o que não for confirmado vai como `[VERIFICAR]` no texto e na mensagem de entrega).
  - Menos de 500 linhas.
- **lousas.md:**
  - o padrão X8 (restrições gerais acima);
  - os moldes e os campos (`mito_verdade`+`apoio`, `metafora`, `topicos`, `colunas`, `comparacao`, `exercicio`);
  - a lista de desenhos e como criar um novo;
  - os limites de tamanho;
  - o que cada bloco costuma levar na lousa;
  - as conferências.
- **exemplo-item.md:** o exemplo passa a ter o bloco de conteúdo com a lousa complementar (sem a seção da Nota).
- **analogias.md:** cada analogia do banco ganha o nome do desenho que a representa (`rodovia_pedagio`, `carro`, `balanca`...).

- [ ] **Passo 1:** escrever as alterações.
- [ ] **Passo 2:** verificar:
  - `python3 <skill-creator>/scripts/quick_validate.py "S"` deve responder `Skill is valid!`;
  - `grep -ci goodnotes -r "S"` deve dar 0;
  - `grep -c "Nota de bastidor" "S/SKILL.md"` só pode aparecer na frase que proíbe a Nota;
  - `wc -l "S/SKILL.md"` deve ficar abaixo de 500.
- [ ] **Passo 3:** commit `Skill: 4 blocos, lousas complementares e entrega no Google Slides`.

### Task 8: Pacote e teste de ponta a ponta com a R50

**Arquivos:**
- Recriar: `Skill Creator/roteiro-lousa-aprofundado.zip`, sem a pasta `tests/`.
- Criar: `aulas-certificacoes/materiais/cpro-r/lousas/r50-vgbl-skill-nova/` (JSON e 12 PNG) e o roteiro `r50-roteiro.md`.

- [ ] **Passo 1:** seguir a skill do começo ao fim para a R50 (itens 3.7.4 a 3.7.4.2), partindo do roteiro do Drive (`1FDmX27LKOHffUCA2caZ9fiPN9uPToxHCAp05HTQiBJU`).
- [ ] **Passo 2:** rodar os dois conferidores:
  - `python3 S/scripts/conferir_roteiro.py r50-roteiro.md --pd …` → zero pendência;
  - `python3 S/scripts/conferir_lousas.py r50-roteiro.md r50-lousas.json` → zero pendência.
- [ ] **Passo 3:** abrir os 12 PNG e comparar com as lousas antigas da R50 (outra branch).
- [ ] **Passo 4:** commit e push. Depois, criar a apresentação `R50 · skill nova · … · lousas` e o Doc do roteiro. O professor aprova cada alteração no Slides.
- [ ] **Passo 5:** conferir as miniaturas do slide 1 e do slide 12 e anotar os links.
- [ ] **Passo 6:** rodar todos os testes (`python3 -m unittest discover -s "S/tests"`), reempacotar o zip e fazer commit e push.
