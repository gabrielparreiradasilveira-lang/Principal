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

---

## 2. Uso no dia a dia (3 passos)

1. Coloque os vídeos na pasta **`entrada/`**.
2. Dê dois cliques em **`transcrever_windows.bat`** (ou `transcrever_mac.command`).
3. Pegue os arquivos na pasta **`saida/`**.

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
| Frases que você não falou ("Legendas pela comunidade Amara.org") | Alucinação do Whisper em silêncio/música. O script já remove as mais comuns. |
| Muito lento | Use `--modo rapido` para rascunho, ou rode à noite com a pasta cheia. |
| Erro de GPU / CUDA | Rode com `--dispositivo cpu`. |
| `MemoryError`, `cannot allocate AudioFrame buffer`, `mkl_malloc` | Faltou RAM durante a execução. Arraste o vídeo em cima do `diagnosticar_windows.bat` e olhe **livre** e **pico deste programa**. Se o "livre" já estiver baixo antes de começar, outro programa ocupou a memória (OBS, navegador, editor de vídeo). |

---

## 7. Próximos passos (fora do MVP)

1. **Interface com arrastar-e-soltar** (janela no navegador, sem terminal).
2. **Motor nativo do Mac** (mlx-whisper), que usa a GPU dos chips M (hoje o MVP usa só a CPU no Mac).
3. **Revisão com IA**: pontuação, parágrafos e títulos de seção, sem mudar o conteúdo.
4. **Saídas pedagógicas**: resumo, capítulos para YouTube, questões no padrão ANBIMA a partir da transcrição.
5. **Pasta vigiada**: transcreve sozinho quando um vídeo novo aparece.
