# Transcritor de Videoaulas (PT-BR) — MVP local

Transforma seus vídeos de aula em texto e legenda, **no seu computador**, sem internet e sem custo por minuto.

```
entrada/  →  [ transcrever ]  →  saida/
Aula 01.mp4                       Aula 01.txt   texto corrido, em parágrafos
                                  Aula 01.md    texto com marcação de tempo [00:12:34]
                                  Aula 01.srt   legenda (YouTube, Hotmart, editores)
                                  Aula 01.vtt   legenda (players web)
```

Motor: **Whisper** (modelo aberto da OpenAI), na versão otimizada **faster-whisper**.

---

## 1. Instalação (só uma vez)

### Windows
1. Instale o **Python 3.12** em [python.org](https://www.python.org/downloads/).
   Na primeira tela, marque **"Add python.exe to PATH"**.
2. Dê dois cliques em **`instalar_windows.bat`**. Espere terminar.

### Mac (chip M1/M2/M3/M4)
1. Instale o **Python 3.12** em [python.org](https://www.python.org/downloads/).
2. Dê dois cliques em **`instalar_mac.command`**.
   Se o Mac bloquear: botão direito → **Abrir** → **Abrir**.

> Na **primeira transcrição** o modelo é baixado (~1,6 GB no modo padrão).
> Ele fica salvo na pasta `modelos/`. Depois disso, funciona offline.

### Placa de vídeo NVIDIA (opcional, Windows)
Sem este passo o transcritor funciona, mas só pela CPU (mais lento).

1. Feche a janela do transcritor.
2. Dê dois cliques em **`instalar_gpu_windows.bat`**. Ele baixa duas bibliotecas da NVIDIA (cuBLAS e cuDNN, ~1,3 GB, uma única vez) e testa a placa no final.
3. Tem que aparecer **`GPU OK: a placa de vídeo está transcrevendo`**. Se aparecer `GPU FALHOU`, copie a mensagem e envie.

Placas com pouca memória (ex.: GTX 1650, 4 GB) funcionam: o script usa um formato compacto (`int8_float16`) e, se a placa encher, divide o lote pela metade antes de voltar para a CPU.

---

## 2. Uso no dia a dia (3 passos)

**Pela janela (recomendado):**

1. Dê dois cliques em **`abrir_janela_windows.bat`** (ou `abrir_janela_mac.command`).
2. **Arraste os vídeos** para a janela, escolha o modo e clique em **▶ Transcrever**.
3. No fim, clique em **Abrir pasta de resultados**.

A janela mostra a situação de cada vídeo, a porcentagem e o tempo restante. Ela também tem um botão **Cancelar**.

**Automático (pasta do OBS):** na janela, clique em **Escolher pasta do OBS…**, aponte para a pasta onde o OBS grava e marque **"Transcrever sozinho os vídeos novos desta pasta"**. A partir daí:
- quando você para a gravação, a transcrição começa sozinha, sem clique (o OBS solta o arquivo e a janela espera ~20 s para confirmar);
- só vídeos gravados **depois** de ligar a opção entram, e vídeos antigos da pasta são ignorados. Gravações feitas com a janela fechada também não entram: arraste-as para a janela;
- se o OBS gerar `aula.mp4` depois de `aula.mkv`, ele não transcreve duas vezes;
- **a janela precisa estar aberta** (pode ficar minimizada).

**Pasta de resultados:** clique em **Escolher…** para mandar os textos direto para outra pasta, por exemplo a de outro projeto. A janela lembra das suas escolhas (`config.json`).

**Registro:** tudo o que aparece em "Detalhes" também fica salvo em **`registro.txt`**, na pasta do transcritor. Se der problema, é só mandar esse arquivo.

> **Já tinha instalado antes desta versão?** Feche a janela e rode o `instalar_windows.bat` de novo, uma vez, para ganhar o arrastar e soltar. Sem isso a janela funciona, mas só pelo clique na área azul. Se o ambiente antigo estiver incompatível, o instalador apaga e refaz sozinho; os modelos já baixados ficam.

**Pela pasta (alternativa):** coloque os vídeos em `entrada/` e dê dois cliques em `transcrever_windows.bat`. Os resultados saem em `saida/`.

- Vídeo que já tem `.txt` na `saida/` é **pulado** (pode jogar a pasta inteira de novo sem medo).
- No Windows, dá para **arrastar um vídeo em cima** do `transcrever_windows.bat`.
- **Deu erro?** Arraste o vídeo em cima do `diagnosticar_windows.bat`. Ele não transcreve, só mede (versões, RAM e faixas de áudio) e salva tudo em `diagnostico.txt`.

---

## 3. Modos e estilos

Pelo terminal: `python transcrever.py --modo maximo --estilo limpo`

| Modo | Modelo | Quando usar |
|---|---|---|
| `rapido` | small | Rascunho. Erra mais siglas e termos técnicos. |
| **`equilibrado`** (padrão) | large-v3-turbo | Uso normal. Boa precisão, velocidade boa. |
| `maximo` | large-v3 | Aula importante, áudio ruim, muito termo técnico. |

| Estilo | Resultado |
|---|---|
| **`fiel`** (padrão) | Tenta manter seu jeito de falar ("né", "tá?", "então"). |
| `limpo` | Texto mais "de apostila". Bom para virar material escrito. |

> O estilo é um **empurrão**, não uma garantia. O Whisper por natureza
> limpa parte dos vícios de fala ("é...", "hã") mesmo no modo `fiel`.

**Números padronizados** (ligado por padrão; na janela: "Padronizar números"; no terminal: `--numeros original` desliga):

| O modelo escreve | Fica |
|---|---|
| 250 mil reais / R$250 mil | R$ 250 mil |
| 1,5 milhão de reais | R$ 1,5 milhão |
| 10 por cento / dez por cento | 10% |
| 13.75% | 13,75% |
| 2 pontos percentuais | 2 p.p. |
| D mais 2 / D + 2 | D+2 |

O padronizador só mexe quando o contexto é claramente numérico. "Juros reais", "dois anos" e "CPA-20" ficam como estão. Limitação: em legenda, um valor partido entre duas linhas pode escapar da padronização. O `.txt` e o `.md` não têm esse problema.

---

## 4. Ensinando o vocabulário (o diferencial deste MVP)

Dois arquivos, duas funções diferentes:

| Arquivo | O que faz | Quando age |
|---|---|---|
| `glossario.txt` | Diz ao modelo quais termos esperar (CDB, NTN-B, come-cotas…). Termos com maiúscula também padronizam a grafia (SELIC → Selic). | **Durante** a transcrição |
| `correcoes.csv` | Troca erros que se repetem: `selique;Selic`. Abre no Excel (separador `;`). | **Depois** da transcrição |

**Rotina recomendada:** revisou uma aula e achou um erro repetido? Adicione uma linha no `correcoes.csv`. Em poucas semanas o texto sai quase limpo.

**Cuidado:** não coloque no `correcoes.csv` palavras comuns que viram sigla (ex.: `ir;IR` estragaria o verbo "ir").

---

## 5. O que esperar (medido)

Teste feito em servidor de **4 núcleos, sem placa de vídeo**, com áudio sintético de 1min43s:

| Modo | Velocidade | 1 h de aula levaria |
|---|---|---|
| rapido | 6,1× o tempo real | ~10 min |
| equilibrado | 5,2× o tempo real | ~12 min |
| maximo | 0,8× o tempo real* | ~75 min |

\* `rapido` e `equilibrado` medidos num vídeo de 5 min (03/11/2026). `maximo` vem de um teste anterior de 1min43s, que superestima o tempo.

- Notebook com 8+ núcleos tende a ser mais rápido. Placa NVIDIA (GPU) costuma acelerar várias vezes (ordem de 5–10×).
- **Lote (`--lote`):** processa vários trechos de 30 s de uma vez. O padrão é automático: **8 na placa de vídeo, 1 no processador**.
  - Na CPU o lote deixou o turbo **mais lento** (5,2× → 4,1×) e o modelo `rapido` mais rápido (6,1× → 9,7×).
  - Na GPU, o benchmark oficial do faster-whisper mostra o lote 3,7× mais rápido.
  - Para testar no seu PC: rode o mesmo vídeo com `--lote 1` e sem a opção, e compare o "x o tempo real".
- O script detecta GPU NVIDIA sozinho. Se der erro na GPU, ele refaz na CPU.
- **Memória (RAM):** o áudio é transcrito em blocos de 10 min, cortados num silêncio. Num vídeo de 2 h o pico foi de ~0,9 GB além do modelo, e esse valor quase não cresce com a duração.
- **OBS com várias faixas de áudio:** o script usa a **faixa 1** (a mixagem principal).
- **Precisão real só se mede com a SUA voz e o SEU microfone.** Antes de confiar, transcreva 1 aula e revise.

---

## 6. Problemas comuns

| Sintoma | Causa / solução |
|---|---|
| `metadata_errors` | Versão nova da biblioteca `av`. Rode o instalador de novo (o `requirements.txt` já trava a versão certa). |
| `Importing the numpy C-extensions failed` (com `cp312` e "Python 3.11" na mensagem) | O ambiente `.venv` misturou duas versões do Python. Feche a janela e rode o `instalar_windows.bat` (versão de 04/11/2026), que detecta e refaz o ambiente. Com instalador antigo: apague a pasta `.venv` e rode o instalador. |
| Frases que você não falou ("Legendas pela comunidade Amara.org") | Alucinação do Whisper em silêncio/música. O script já remove as mais comuns. |
| Muito lento | Use `--modo rapido` para rascunho, ou rode à noite com a pasta cheia. |
| `Library cublas64_12.dll is not found` (ou `cudnn…dll`) | Faltam as bibliotecas da NVIDIA. Rode o `instalar_gpu_windows.bat`. Enquanto isso, o script transcreve pela CPU sozinho. |
| Outro erro de GPU / CUDA | O script já refaz na CPU. Para forçar a CPU: `--dispositivo cpu`. |
| `MemoryError`, `cannot allocate AudioFrame buffer`, `mkl_malloc` | Faltou RAM durante a execução. Arraste o vídeo em cima do `diagnosticar_windows.bat` e olhe **livre** e **pico deste programa**. Se o "livre" já estiver baixo antes de começar, outro programa ocupou a memória (OBS, navegador, editor de vídeo). |

---

## 7. Próximos passos (fora do MVP)

1. **Motor nativo do Mac** (mlx-whisper), que usa a GPU dos chips M (hoje o MVP usa só a CPU no Mac).
2. **Revisão com IA**: pontuação, parágrafos e títulos de seção, sem mudar o conteúdo.
3. **Saídas pedagógicas**: resumo, capítulos para YouTube, questões no padrão ANBIMA a partir da transcrição.
