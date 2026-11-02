#!/usr/bin/env python3
"""
Transcritor de Videoaulas (PT-BR) - MVP local
Motor: faster-whisper (modelo Whisper rodando 100% no seu computador).

Uso:
  1. Coloque os vídeos/áudios na pasta "entrada"
  2. Rode:  python transcrever.py
  3. Pegue os arquivos na pasta "saida"  (.txt, .md, .srt, .vtt)

Opções úteis:
  python transcrever.py --modo maximo        # mais preciso, mais lento
  python transcrever.py --estilo limpo       # tira os "né", "tipo", "é..."
  python transcrever.py "C:/aulas/aula1.mp4" # arquivo específico
"""

from __future__ import annotations

import argparse
import csv
import gc
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path

PASTA = Path(__file__).resolve().parent

# Modo -> modelo Whisper
MODOS = {
    "rapido": "small",                # rascunho rápido, erra mais termos técnicos
    "equilibrado": "large-v3-turbo",  # padrão: quase a precisão do large-v3, bem mais rápido
    "maximo": "large-v3",             # mais preciso, mais lento
}

TAXA = 16000      # o Whisper trabalha com áudio em 16 kHz
BLOCO_SEG = 600   # transcreve em blocos de 10 min: RAM constante para qualquer duração

EXTENSOES = {
    ".mp4", ".mov", ".mkv", ".avi", ".webm", ".m4v", ".wmv",
    ".mp3", ".m4a", ".wav", ".flac", ".ogg", ".aac", ".opus",
}

# O Whisper imita o estilo do texto que recebe como "contexto anterior".
# Contexto com vícios de fala -> ele tende a manter os seus vícios de fala.
ESTILOS = {
    "fiel": "Então, né, é... a gente vai ver isso agora, tá? Tipo assim, beleza.",
    "limpo": "Olá, pessoal. Hoje vamos estudar este tema com calma.",
}

# Frases que o Whisper "inventa" em trechos de silêncio/música (vêm das legendas
# usadas no treino do modelo). Segmentos que batem com isso são descartados.
ALUCINACOES = re.compile(
    r"amara\.org|legendas? pela comunidade|legendado por|legendas? por \w+",
    re.IGNORECASE,
)


@dataclass
class Palavra:
    inicio: float
    fim: float
    texto: str


# ----------------------------------------------------------------------------
# Glossário e correções
# ----------------------------------------------------------------------------

def carregar_glossario(caminho: Path) -> list[str]:
    if not caminho.exists():
        return []
    termos = []
    for linha in caminho.read_text(encoding="utf-8-sig").splitlines():
        linha = linha.strip()
        if linha and not linha.startswith("#"):
            termos.append(linha)
    return termos


def carregar_correcoes(caminho: Path) -> list[tuple[re.Pattern, str]]:
    """CSV com separador ';' (padrão do Excel em PT-BR): errado;certo"""
    if not caminho.exists():
        return []
    regras = []
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        for linha in csv.reader(f, delimiter=";"):
            if len(linha) < 2 or not linha[0].strip() or linha[0].startswith("#"):
                continue
            errado, certo = linha[0].strip(), linha[1].strip()
            if errado.lower() == "errado":  # cabeçalho
                continue
            padrao = re.compile(r"(?<!\w)" + re.escape(errado) + r"(?!\w)", re.IGNORECASE)
            regras.append((padrao, certo))
    return regras


def corrigir(texto: str, regras: list[tuple[re.Pattern, str]]) -> str:
    for padrao, certo in regras:
        texto = padrao.sub(certo, texto)
    return re.sub(r"\s{2,}", " ", texto).strip()


def montar_contexto(estilo: str, termos: list[str], model) -> str:
    """Texto enviado ao Whisper em TODA janela de 30 s (parâmetro hotwords).
    Limite do modelo: ~223 tokens. Passou disso, o fim é cortado."""
    contexto = ESTILOS[estilo]
    if termos:
        contexto += " Termos da aula: " + ", ".join(termos) + "."
    n_tokens = len(model.hf_tokenizer.encode(" " + contexto).ids)
    limite = model.max_length // 2 - 1
    if n_tokens > limite:
        print(f"  ! Glossário longo demais ({n_tokens} tokens, limite {limite}). "
              f"Os últimos termos serão ignorados. Deixe só os que o modelo mais erra.")
    return contexto


# ----------------------------------------------------------------------------
# Formatação de tempo e saídas
# ----------------------------------------------------------------------------

def tempo(segundos: float, sep: str = ",") -> str:
    ms = int(round(segundos * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def tempo_curto(segundos: float) -> str:
    return tempo(segundos)[:8]


FIM_FRASE = (".", "?", "!")
PAUSA_FRASE = FIM_FRASE + (",", ";", ":")


def _texto(palavras: list[Palavra]) -> str:
    return "".join(p.texto for p in palavras).strip()


def quebrar_linha(texto: str, max_linha: int = 42) -> str:
    """Divide a legenda em 2 linhas, perto do meio, de preferência após pontuação."""
    if len(texto) <= max_linha:
        return texto
    meio = len(texto) // 2
    espacos = [i for i, c in enumerate(texto) if c == " "]
    if not espacos:
        return texto
    cabem = [i for i in espacos if i <= max_linha and len(texto) - i - 1 <= max_linha]
    candidatos = cabem or espacos
    corte = min(candidatos,
                key=lambda i: abs(i - meio) - (8 if texto[i - 1] in ",.?!;:" else 0))
    return texto[:corte] + "\n" + texto[corte + 1:]


def montar_legendas(palavras: list[Palavra], regras, max_chars=84, max_dur=7.0,
                    max_pausa=1.0) -> list[tuple[float, float, str]]:
    """Agrupa palavras em legendas de até 2 linhas x 42 caracteres e 7 s,
    cortando de preferência em pontuação."""
    blocos, atual = [], []
    for p in palavras:
        if atual:
            pausa = p.inicio - atual[-1].fim
            if (len(_texto(atual + [p])) > max_chars
                    or p.fim - atual[0].inicio > max_dur or pausa > max_pausa):
                corte = len(atual)
                if pausa <= max_pausa:  # procura vírgula/ponto na metade final
                    for i in range(len(atual) - 1, len(atual) // 2 - 1, -1):
                        if atual[i].texto.strip().endswith(PAUSA_FRASE):
                            corte = i + 1
                            break
                blocos.append(atual[:corte])
                atual = atual[corte:]
        atual.append(p)
        if _texto(atual).endswith(FIM_FRASE) and len(_texto(atual)) >= 25:
            blocos.append(atual)
            atual = []
    if atual:
        blocos.append(atual)

    legendas = []
    for b in blocos:
        texto = corrigir(_texto(b), regras)
        if texto:
            legendas.append((b[0].inicio, b[-1].fim, quebrar_linha(texto)))
    return legendas


def montar_paragrafos(palavras: list[Palavra], regras, pausa=2.0, max_chars=700):
    """Novo parágrafo a cada pausa longa ou quando o texto passa do tamanho."""
    paragrafos, atual = [], []
    for p in palavras:
        if atual:
            fim_frase = atual[-1].texto.strip().endswith(FIM_FRASE)
            if p.inicio - atual[-1].fim >= pausa or (fim_frase and len(_texto(atual)) >= max_chars):
                # O alinhamento às vezes "puxa" 1-3 palavras para antes da pausa.
                # Se houver fim de frase logo antes, corta ali.
                corte = len(atual)
                if not fim_frase:
                    for i in range(len(atual) - 2, max(len(atual) - 5, -1), -1):
                        if atual[i].texto.strip().endswith(FIM_FRASE):
                            corte = i + 1
                            break
                paragrafos.append((atual[0].inicio, corrigir(_texto(atual[:corte]), regras)))
                atual = atual[corte:]
        atual.append(p)
    if atual:
        paragrafos.append((atual[0].inicio, corrigir(_texto(atual), regras)))
    return paragrafos


def salvar_saidas(destino: Path, nome: str, palavras: list[Palavra], regras):
    destino.mkdir(parents=True, exist_ok=True)
    saida = lambda ext: destino / f"{nome}{ext}"  # noqa: E731 (nomes com ponto: "Aula 1.2")

    paragrafos = montar_paragrafos(palavras, regras)
    saida(".txt").write_text("\n\n".join(t for _, t in paragrafos) + "\n", encoding="utf-8")
    saida(".md").write_text(
        f"# {nome}\n\n" + "\n\n".join(f"**[{tempo_curto(i)}]** {t}" for i, t in paragrafos)
        + "\n", encoding="utf-8")

    legendas = montar_legendas(palavras, regras)
    srt = [f"{n}\n{tempo(i)} --> {tempo(f)}\n{t}\n" for n, (i, f, t) in enumerate(legendas, 1)]
    saida(".srt").write_text("\n".join(srt), encoding="utf-8")
    vtt = [f"{tempo(i, '.')} --> {tempo(f, '.')}\n{t}\n" for i, f, t in legendas]
    saida(".vtt").write_text("WEBVTT\n\n" + "\n".join(vtt), encoding="utf-8")


# ----------------------------------------------------------------------------
# Transcrição
# ----------------------------------------------------------------------------

def escolher_dispositivo(pedido: str) -> str:
    if pedido != "auto":
        return pedido
    try:
        import ctranslate2
        if ctranslate2.get_cuda_device_count() > 0:
            return "cuda"
    except Exception:
        pass
    return "cpu"


def carregar_modelo(nome: str, dispositivo: str, threads: int):
    from faster_whisper import WhisperModel
    tipo = "float16" if dispositivo == "cuda" else "int8"
    print(f"Carregando modelo '{nome}' em {dispositivo.upper()} ({tipo})...")
    print("  (na primeira vez ele é baixado: 0,5 a 3 GB. Depois fica salvo na pasta 'modelos'.)")
    return WhisperModel(nome, device=dispositivo, compute_type=tipo,
                        cpu_threads=threads, download_root=str(PASTA / "modelos"))


def carregar_audio(arquivo: Path):
    """Extrai só o áudio, em 16 kHz mono int16 (~115 MB por hora de aula).
    O faster-whisper sozinho guardaria o áudio inteiro em float32 e calcularia o
    espectrograma de tudo de uma vez: ~3 GB de RAM por hora de vídeo."""
    import av
    import numpy as np
    dados = bytearray()
    with av.open(str(arquivo)) as cont:
        if not cont.streams.audio:
            raise ValueError("o arquivo não tem faixa de áudio")
        faixa = cont.streams.audio[0]  # OBS: faixa 1 = mixagem principal
        reamostrador = av.audio.resampler.AudioResampler(format="s16", layout="mono", rate=TAXA)
        for pacote in cont.demux(faixa):
            try:
                quadros = pacote.decode()
            except av.error.InvalidDataError:  # pedaço corrompido: pula
                continue
            for quadro in quadros:
                for q in reamostrador.resample(quadro):
                    dados += q.to_ndarray().tobytes()
        for q in reamostrador.resample(None):  # esvazia o que sobrou
            dados += q.to_ndarray().tobytes()
    return np.frombuffer(dados, dtype=np.int16)


def pontos_de_corte(audio, bloco_seg: int, busca_seg: int = 20) -> list[int]:
    """Divide o áudio em blocos de ~bloco_seg, cortando no trecho mais silencioso
    a até ±busca_seg do ponto ideal, para não partir uma palavra ao meio."""
    import numpy as np
    bloco, busca, quadro = bloco_seg * TAXA, busca_seg * TAXA, TAXA // 10  # quadro = 100 ms
    cortes, pos = [0], bloco
    while pos + busca < len(audio):
        ini = pos - busca
        trecho = audio[ini:pos + busca].astype(np.float32)
        n = len(trecho) // quadro
        energia = np.sqrt((trecho[:n * quadro].reshape(n, quadro) ** 2).mean(axis=1))
        energia = np.convolve(energia, np.ones(4) / 4, mode="same")  # janela de ~0,4 s
        corte = ini + int(np.argmin(energia)) * quadro + quadro // 2
        cortes.append(corte)
        pos = corte + bloco
    cortes.append(len(audio))
    return cortes


def transcrever(model, audio, contexto: str, bloco_seg: int = BLOCO_SEG):
    import numpy as np
    duracao = len(audio) / TAXA
    palavras, ultimo_texto = [], None
    cortes = pontos_de_corte(audio, bloco_seg)
    for a, b in zip(cortes, cortes[1:]):
        inicio = a / TAXA
        trecho = audio[a:b].astype(np.float32) / 32768.0
        segs_iter, _ = model.transcribe(
            trecho,
            language="pt",
            beam_size=5,
            vad_filter=True,                          # pula silêncios (menos alucinação)
            vad_parameters={"min_silence_duration_ms": 500},
            condition_on_previous_text=False,         # evita loops de repetição
            hotwords=contexto,                        # estilo + glossário em toda janela
            word_timestamps=True,                     # legendas bem cortadas
            hallucination_silence_threshold=2.0,
        )
        for seg in segs_iter:
            texto = seg.text.strip()
            fim = inicio + seg.end
            pct = min(100, fim / max(duracao, 1) * 100)
            print(f"\r  {pct:5.1f}%  [{tempo_curto(fim)} / {tempo_curto(duracao)}]",
                  end="", flush=True)
            if not texto or ALUCINACOES.search(texto):
                continue
            if texto == ultimo_texto and len(texto) > 20:  # frase longa repetida = loop
                continue
            ultimo_texto = texto
            palavras.extend(Palavra(inicio + w.start, inicio + w.end, w.word)
                            for w in (seg.words or []))
        del trecho
    print()
    return palavras, duracao


def erro_de_gpu(erro: Exception) -> bool:
    msg = str(erro).lower()
    return any(k in msg for k in ("cuda", "cublas", "cudnn", "cudart"))


def descrever_erro(erro: Exception) -> str:
    if isinstance(erro, MemoryError) or "allocate" in str(erro).lower():
        return ("memória RAM insuficiente. Feche OBS, navegador e editores de vídeo "
                "e rode de novo (ou use --modo rapido)")
    return f"{type(erro).__name__}: {erro}"


def listar_arquivos(alvos: list[str]) -> list[Path]:
    caminhos = [Path(a) for a in alvos] if alvos else [PASTA / "entrada"]
    arquivos = []
    for c in caminhos:
        if c.is_dir():
            arquivos += sorted(p for p in c.iterdir() if p.suffix.lower() in EXTENSOES)
        elif c.is_file() and c.suffix.lower() in EXTENSOES:
            arquivos.append(c)
        else:
            print(f"Ignorado (não encontrado ou formato não suportado): {c}")
    return arquivos


def main():
    ap = argparse.ArgumentParser(description="Transcritor de videoaulas PT-BR (local)")
    ap.add_argument("alvos", nargs="*", help="arquivos ou pastas (padrão: pasta 'entrada')")
    ap.add_argument("--modo", choices=MODOS, default="equilibrado")
    ap.add_argument("--estilo", choices=ESTILOS, default="fiel",
                    help="fiel = mantém seu jeito de falar; limpo = texto mais 'de apostila'")
    ap.add_argument("--saida", default=str(PASTA / "saida"))
    ap.add_argument("--dispositivo", choices=["auto", "cpu", "cuda"], default="auto")
    ap.add_argument("--threads", type=int, default=os.cpu_count() or 4)
    ap.add_argument("--forcar", action="store_true", help="refaz arquivos já transcritos")
    ap.add_argument("--bloco", type=int, default=BLOCO_SEG, help=argparse.SUPPRESS)  # testes
    args = ap.parse_args()

    arquivos = listar_arquivos(args.alvos)
    if not arquivos:
        print("Nenhum vídeo/áudio encontrado. Coloque os arquivos na pasta 'entrada'.")
        return 1

    destino = Path(args.saida)
    pendentes = [a for a in arquivos
                 if args.forcar or not (destino / f"{a.stem}.txt").exists()]
    if not pendentes:
        print("Tudo já transcrito. Use --forcar para refazer.")
        return 0
    print(f"{len(pendentes)} arquivo(s) para transcrever.\n")

    termos = carregar_glossario(PASTA / "glossario.txt")
    regras = carregar_correcoes(PASTA / "correcoes.csv")
    # Termos com maiúscula no glossário padronizam a grafia: SELIC/selic -> Selic
    regras += [(re.compile(r"(?<!\w)" + re.escape(t) + r"(?!\w)", re.IGNORECASE), t)
               for t in termos if any(c.isupper() for c in t)]
    dispositivo = escolher_dispositivo(args.dispositivo)
    try:
        model = carregar_modelo(MODOS[args.modo], dispositivo, args.threads)
    except Exception as erro:
        if dispositivo != "cuda":
            raise
        print(f"  GPU indisponível ({erro}). Usando a CPU.")
        dispositivo = "cpu"
        model = carregar_modelo(MODOS[args.modo], dispositivo, args.threads)
    contexto = montar_contexto(args.estilo, termos, model)

    for n, arquivo in enumerate(pendentes, 1):
        print(f"\n[{n}/{len(pendentes)}] {arquivo.name}")
        t0 = time.time()
        try:
            audio = carregar_audio(arquivo)
        except Exception as erro:
            print(f"  ERRO ao ler o áudio: {descrever_erro(erro)}  (arquivo pulado)")
            continue
        print(f"  Áudio extraído: {tempo_curto(len(audio) / TAXA)} de duração")

        resultado, falhou_na_gpu = None, False
        try:
            resultado = transcrever(model, audio, contexto, args.bloco)
        except Exception as erro:
            if dispositivo == "cuda" and erro_de_gpu(erro):
                falhou_na_gpu = True
                print(f"\n  GPU falhou ({erro}). Tentando de novo na CPU...")
            else:
                print(f"\n  ERRO: {descrever_erro(erro)}  (arquivo pulado)")
        if falhou_na_gpu:  # fora do except: a memória do erro já foi liberada
            del model
            gc.collect()
            dispositivo = "cpu"
            try:
                model = carregar_modelo(MODOS[args.modo], "cpu", args.threads)
                resultado = transcrever(model, audio, contexto, args.bloco)
            except Exception as erro:
                print(f"\n  ERRO na CPU: {descrever_erro(erro)}")
                return 1
        del audio
        if resultado is None:
            continue

        palavras, duracao = resultado
        salvar_saidas(destino, arquivo.stem, palavras, regras)
        gasto = time.time() - t0
        print(f"  OK: {tempo_curto(duracao)} de aula em {tempo_curto(gasto)} "
              f"({duracao / max(gasto, 0.01):.1f}x o tempo real) -> {destino / arquivo.stem}.*")

    print("\nPronto.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
