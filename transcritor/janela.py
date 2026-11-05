#!/usr/bin/env python3
"""
Janela do Transcritor de Videoaulas.

  1. Arraste os vídeos para a janela (ou clique para escolher)
  2. Escolha o modo
  3. Clique em Transcrever

Ou, no quadro "Automático", escolha a pasta onde o OBS grava: cada gravação nova
é transcrita sozinha assim que o OBS termina de gravar.

Por baixo, a janela roda o mesmo transcrever.py, em um processo separado:
se algo der errado, a janela continua aberta, e "Cancelar" encerra na hora.
"""

from __future__ import annotations

import codecs
import json
import os
import queue
import re
import subprocess
import sys
import threading
import time
import traceback
from pathlib import Path

import tkinter as tk
from tkinter import filedialog, font, messagebox, scrolledtext, ttk

from transcrever import EXTENSOES

PASTA = Path(__file__).resolve().parent
SCRIPT = PASTA / "transcrever.py"
SAIDA = PASTA / "saida"             # pasta de resultados padrão
CONFIG = PASTA / "config.json"       # escolhas da janela (pastas, modo, estilo...)
REGISTRO = PASTA / "registro.txt"    # cópia de tudo o que aparece em "Detalhes"

ESTAVEL_SEG = 20      # vídeo "pronto" = tamanho parado por esse tempo (OBS terminou)
INTERVALO_VIGIA = 5   # segundos entre uma olhada e outra na pasta do OBS
MARGEM_SEG = 5        # folga ao separar vídeos novos dos que já estavam na pasta

try:  # arrastar e soltar (pacote tkinterdnd2); sem ele, só o botão de escolher
    from tkinterdnd2 import DND_FILES, TkinterDnD
    TEM_ARRASTAR = True
except Exception:
    TEM_ARRASTAR = False

MODOS = [
    ("rapido", "Rápido", "rascunho; erra mais siglas"),
    ("equilibrado", "Equilibrado", "recomendado"),
    ("maximo", "Máximo", "mais preciso, bem mais lento"),
]
ESTILOS = [
    ("fiel", "Fiel ao meu jeito de falar", "mantém “né”, “tá?”"),
    ("limpo", "Limpo", "texto de apostila"),
]

RE_ARQUIVO = re.compile(r"^\[(\d+)/(\d+)\] (.+)$")
RE_PROGRESSO = re.compile(r"^(\d+(?:\.\d+)?)%\s+\[")

NA_FILA, JA_FEITO, PRONTO = "Na fila", "Já transcrito", "Pronto ✓"


def ler_config() -> dict:
    """Escolhas salvas; arquivo ausente ou estragado = valores padrão."""
    try:
        dados = json.loads(CONFIG.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return dados if isinstance(dados, dict) else {}


def livre(p: Path) -> bool:
    """No Windows o OBS deixa o vídeo travado enquanto grava: renomear falha."""
    if sys.platform != "win32":
        return True
    try:
        os.rename(p, p)
        return True
    except OSError:
        return False


class Janela:
    def __init__(self, raiz: tk.Tk):
        self.raiz = raiz
        self.arquivos: list[Path] = []
        self.processo: subprocess.Popen | None = None
        self.fila: queue.Queue = queue.Queue()
        self.atual: str | None = None      # nome do arquivo em andamento
        self.inicio_arquivo = 0.0
        self.feitos = self.erros = self.total = 0
        self.cancelado = False
        self.automatico = False            # rodada iniciada pela pasta vigiada
        self.pendente_auto = False         # vídeo novo chegou durante uma rodada
        self.tamanhos: dict[Path, tuple[int, float]] = {}  # tamanho e quando mudou
        self.vistos_auto: set[Path] = set()  # já entregues à lista pela pasta vigiada
        self.vigia_desde = time.time()

        conf = ler_config()
        texto = lambda chave, padrao: (conf[chave] if isinstance(conf.get(chave), str)  # noqa: E731
                                       else padrao)
        modo, estilo = texto("modo", "equilibrado"), texto("estilo", "fiel")
        self.modo = tk.StringVar(value=modo if modo in {m[0] for m in MODOS} else "equilibrado")
        self.estilo = tk.StringVar(value=estilo if estilo in {e[0] for e in ESTILOS} else "fiel")
        self.padronizar = tk.BooleanVar(value=texto("numeros", "padrao") != "original")
        self.refazer = tk.BooleanVar(value=False)
        self.pasta_obs = tk.StringVar(value=texto("pasta_obs", ""))
        self.vigiar = tk.BooleanVar(value=conf.get("vigiar") is True)
        self.saida = tk.StringVar(value=texto("saida", "") or str(SAIDA))
        for var in (self.modo, self.estilo, self.padronizar, self.pasta_obs, self.vigiar,
                    self.saida):
            var.trace_add("write", lambda *_: self._salvar_config())
        self.vigiar.trace_add("write", lambda *_: self._ao_mudar_vigia())

        self._montar()
        self.raiz.protocol("WM_DELETE_WINDOW", self.fechar)
        self.raiz.after(100, self._ler_fila)
        self.raiz.after(1000, self._vigiar)

    # ------------------------------------------------------------------ tela
    def _montar(self):
        r = self.raiz
        r.title("Transcritor de Videoaulas")
        r.minsize(720, 560)  # o tamanho final é calculado em _ajustar_tamanho()
        font.nametofont("TkDefaultFont").configure(size=11)
        font.nametofont("TkTextFont").configure(size=10)
        estilo = ttk.Style()
        estilo.configure("Grande.TButton", font=("TkDefaultFont", 13, "bold"), padding=8)

        corpo = ttk.Frame(r, padding=(14, 10))
        corpo.pack(fill="both", expand=True)

        ttk.Label(corpo, text="Transcritor de Videoaulas",
                  font=("TkDefaultFont", 16, "bold")).pack(anchor="w")
        ttk.Label(corpo, text="1. Arraste os vídeos   →   2. Escolha o modo   →   "
                              "3. Clique em Transcrever").pack(anchor="w", pady=(2, 8))

        dica = ("Arraste os vídeos aqui\n(ou clique para escolher)" if TEM_ARRASTAR else
                "Clique aqui para escolher os vídeos\n(para arrastar e soltar, rode o "
                "instalador de novo)")
        self.zona = tk.Label(corpo, text=dica, relief="ridge", bd=2, height=2,
                             bg="#eef3fb", fg="#1f3b63", cursor="hand2",
                             font=("TkDefaultFont", 12, "bold"))
        self.zona.pack(fill="x")
        self.zona.bind("<Button-1>", lambda e: self.escolher())

        lista = ttk.Frame(corpo)
        lista.pack(fill="both", expand=True, pady=(8, 4))
        self.tabela = ttk.Treeview(lista, columns=("arquivo", "status"), show="headings",
                                   height=3, selectmode="extended")
        self.tabela.heading("arquivo", text="Arquivo")
        self.tabela.heading("status", text="Situação")
        self.tabela.column("arquivo", width=480)
        self.tabela.column("status", width=200)
        rolagem = ttk.Scrollbar(lista, orient="vertical", command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=rolagem.set)
        self.tabela.pack(side="left", fill="both", expand=True)
        rolagem.pack(side="right", fill="y")

        if TEM_ARRASTAR:
            for alvo in (self.zona, self.tabela):
                alvo.drop_target_register(DND_FILES)
                alvo.dnd_bind("<<Drop>>", self._ao_soltar)

        botoes_lista = ttk.Frame(corpo)
        botoes_lista.pack(fill="x")
        self.bt_remover = ttk.Button(botoes_lista, text="Remover selecionados",
                                     command=self.remover)
        self.bt_remover.pack(side="left")
        self.bt_limpar = ttk.Button(botoes_lista, text="Limpar lista", command=self.limpar)
        self.bt_limpar.pack(side="left", padx=6)

        pastas = ttk.Frame(corpo)
        pastas.pack(fill="x", pady=(8, 0))
        quadro_auto = ttk.LabelFrame(pastas, text="Automático (pasta do OBS)", padding=(8, 4))
        quadro_auto.pack(side="left", fill="both", expand=True)
        linha = ttk.Frame(quadro_auto)
        linha.pack(fill="x")
        ttk.Entry(linha, textvariable=self.pasta_obs, state="readonly").pack(
            side="left", fill="x", expand=True)
        ttk.Button(linha, text="Escolher pasta do OBS…", command=self.escolher_obs).pack(
            side="left", padx=(6, 0))
        ttk.Checkbutton(quadro_auto, text="Transcrever sozinho os vídeos novos desta pasta",
                        variable=self.vigiar).pack(anchor="w", pady=(4, 0))
        quadro_saida = ttk.LabelFrame(pastas, text="Pasta de resultados", padding=(8, 4))
        quadro_saida.pack(side="left", fill="both", expand=True, padx=(10, 0))
        linha = ttk.Frame(quadro_saida)
        linha.pack(fill="x")
        ttk.Entry(linha, textvariable=self.saida, state="readonly").pack(
            side="left", fill="x", expand=True)
        self.bt_saida = ttk.Button(linha, text="Escolher…", command=self.escolher_saida)
        self.bt_saida.pack(side="left", padx=(6, 0))
        ttk.Button(quadro_saida, text="Abrir pasta de resultados",
                   command=self.abrir_pasta).pack(anchor="w", pady=(4, 0))

        opcoes = ttk.Frame(corpo)
        opcoes.pack(fill="x", pady=8)
        quadro_modo = ttk.LabelFrame(opcoes, text="Modo", padding=(8, 4))
        quadro_modo.pack(side="left", fill="both", expand=True)
        for valor, nome, desc in MODOS:
            ttk.Radiobutton(quadro_modo, text=f"{nome} — {desc}", value=valor,
                            variable=self.modo).pack(anchor="w")
        quadro_estilo = ttk.LabelFrame(opcoes, text="Estilo do texto", padding=(8, 4))
        quadro_estilo.pack(side="left", fill="both", expand=True, padx=(10, 0))
        for valor, nome, desc in ESTILOS:
            ttk.Radiobutton(quadro_estilo, text=f"{nome} — {desc}", value=valor,
                            variable=self.estilo).pack(anchor="w")
        ttk.Checkbutton(quadro_estilo, text="Padronizar números (R$, %, D+2)",
                        variable=self.padronizar).pack(anchor="w", pady=(4, 0))
        ttk.Checkbutton(quadro_estilo, text="Refazer vídeos já transcritos",
                        variable=self.refazer).pack(anchor="w")

        acoes = ttk.Frame(corpo)
        acoes.pack(fill="x")
        self.bt_iniciar = ttk.Button(acoes, text="▶  Transcrever", style="Grande.TButton",
                                     command=self.iniciar)
        self.bt_iniciar.pack(side="left")
        self.bt_cancelar = ttk.Button(acoes, text="Cancelar", command=self.cancelar,
                                      state="disabled")
        self.bt_cancelar.pack(side="left", padx=8)

        self.barra = ttk.Progressbar(corpo, maximum=100)
        self.barra.pack(fill="x", pady=(8, 2))
        self.situacao = ttk.Label(corpo, text="Pronto para começar.")
        self.situacao.pack(anchor="w")

        detalhes = ttk.LabelFrame(corpo, text="Detalhes (copie daqui se precisar de ajuda)",
                                  padding=4)
        detalhes.pack(fill="both", expand=True, pady=(6, 0))
        self.log = scrolledtext.ScrolledText(detalhes, height=3, state="disabled", wrap="word")
        self.log.pack(fill="both", expand=True)
        self._ajustar_tamanho()

    def _ajustar_tamanho(self):
        """Tamanho pelo que o conteúdo pede: com zoom de 125%/150% no Windows as letras
        crescem e uma altura fixa cortaria o rodapé. Limitado à tela (menos a barra
        de tarefas); se ainda faltar espaço, só a caixa Detalhes encolhe."""
        r = self.raiz
        r.update_idletasks()
        largura = min(max(900, r.winfo_reqwidth()), r.winfo_screenwidth() - 20)
        altura = min(r.winfo_reqheight() + 4, r.winfo_screenheight() - 80)
        r.geometry(f"{largura}x{altura}")

    # -------------------------------------------------------------- arquivos
    def escolher(self):
        if self._ocupado():
            return
        tipos = " ".join(f"*{e}" for e in sorted(EXTENSOES))
        caminhos = filedialog.askopenfilenames(
            title="Escolha os vídeos", filetypes=[("Vídeos e áudios", tipos), ("Todos", "*.*")])
        self.adicionar([Path(c) for c in caminhos])

    def _ao_soltar(self, evento):
        if not self._ocupado():
            self.adicionar([Path(c) for c in self.raiz.tk.splitlist(evento.data)])
        return evento.action

    def adicionar(self, caminhos: list[Path]):
        novos, ignorados = [], []
        for c in caminhos:
            itens = sorted(c.iterdir()) if c.is_dir() else [c]
            for p in itens:
                if p.is_file() and p.suffix.lower() in EXTENSOES:
                    novos.append(p.resolve())
                elif not c.is_dir():
                    ignorados.append(p.name)
        for p in novos:
            if p in self.arquivos:
                continue
            self.arquivos.append(p)
            self.tabela.insert("", "end", iid=str(p), values=(p.name, self._status_inicial(p)))
        if ignorados:
            self._escrever(f"Ignorados (formato não suportado): {', '.join(ignorados)}")
        self.situacao.config(text=f"{len(self.arquivos)} vídeo(s) na lista.")

    def _status_inicial(self, p: Path, refazer: bool | None = None) -> str:
        feito = (self._pasta_saida() / f"{p.stem}.txt").exists()
        refazer = self.refazer.get() if refazer is None else refazer
        return JA_FEITO if feito and not refazer else NA_FILA

    def remover(self):
        if self._ocupado():
            return
        for iid in self.tabela.selection():
            self.tabela.delete(iid)
            self.arquivos.remove(Path(iid))

    def limpar(self):
        if self._ocupado():
            return
        self.tabela.delete(*self.tabela.get_children())
        self.arquivos.clear()
        self.situacao.config(text="Lista vazia.")

    def _marcar(self, nome: str, status: str):
        for p in self.arquivos:
            if p.name == nome:
                self.tabela.set(str(p), "status", status)

    # ------------------------------------------------------------- execução
    def iniciar(self, automatico: bool = False):
        """Manual: transcreve a lista toda. Automático (pasta do OBS): só o que está
        "Na fila", sem refazer nada e sem caixas de mensagem."""
        if self.processo if automatico else self._ocupado():
            return
        if not self.arquivos:
            if not automatico:
                messagebox.showinfo("Transcritor", "Arraste ou escolha pelo menos um vídeo.")
            return
        refazer = self.refazer.get() and not automatico
        candidatos = [p for p in self.arquivos
                      if not automatico or self.tabela.set(str(p), "status") == NA_FILA]
        for p in candidatos:
            self.tabela.set(str(p), "status", self._status_inicial(p, refazer))
        pendentes = [p for p in candidatos if self._status_inicial(p, refazer) == NA_FILA]
        self.total = len(pendentes)
        if self.total == 0:
            if automatico:
                aviso = "Vídeo novo da pasta do OBS já estava transcrito: nada a fazer."
                self.situacao.config(text=aviso)
                self._escrever(aviso)
            else:
                messagebox.showinfo("Transcritor", "Todos esses vídeos já foram transcritos.\n"
                                    "Para refazer, marque “Refazer vídeos já transcritos”.")
            return

        comando = self._comando(pendentes, refazer)
        ambiente = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUNBUFFERED="1")

        self.feitos = self.erros = 0
        self.atual, self.cancelado, self.automatico = None, False, automatico
        self.barra.config(value=0)
        quando = time.strftime("%d/%m/%Y %H:%M:%S")
        self._escrever(f"\n=== {quando} — Início{' automático' if automatico else ''}: "
                       f"{self.total} vídeo(s), modo {self.modo.get()} ===")
        self.situacao.config(text="Iniciando...")
        self.processo = subprocess.Popen(
            comando, cwd=PASTA, env=ambiente, stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        threading.Thread(target=self._ler_saida, args=(self.processo,), daemon=True).start()
        self._botoes(rodando=True)

    def _comando(self, arquivos: list[Path], refazer: bool) -> list[str]:
        comando = [sys.executable, "-u", str(SCRIPT), "--modo", self.modo.get(),
                   "--estilo", self.estilo.get(), "--saida", str(self._pasta_saida())]
        if not self.padronizar.get():
            comando += ["--numeros", "original"]
        if refazer:
            comando.append("--forcar")
        return comando + [str(p) for p in arquivos]

    def _ler_saida(self, processo: subprocess.Popen):
        """Lê a saída do transcrever.py; as linhas de progresso terminam em \\r."""
        decodificador = codecs.getincrementaldecoder("utf-8")(errors="replace")
        resto = ""
        while True:
            pedaco = processo.stdout.read1(4096)
            if not pedaco:
                break
            resto += decodificador.decode(pedaco)
            *linhas, resto = re.split(r"[\r\n]", resto)
            for linha in linhas:
                if linha.strip():
                    self.fila.put(("linha", linha))
        if resto.strip():
            self.fila.put(("linha", resto))
        self.fila.put(("fim", processo.wait()))

    def _ler_fila(self):
        try:
            while True:
                tipo, valor = self.fila.get_nowait()
                if tipo == "linha":
                    self._tratar(valor)
                else:
                    self._terminou(valor)
        except queue.Empty:
            pass
        self.raiz.after(100, self._ler_fila)

    def _tratar(self, linha: str):
        texto = linha.strip()
        progresso = RE_PROGRESSO.match(texto)
        if progresso and self.atual:
            pct = float(progresso.group(1))
            self._marcar(self.atual, f"Transcrevendo {pct:.0f}%")
            self.barra.config(value=(self.feitos + pct / 100) / max(self.total, 1) * 100)
            gasto = time.time() - self.inicio_arquivo
            falta = f" — faltam ~{max(1, round(gasto * (100 / pct - 1) / 60))} min" if pct > 3 else ""
            self.situacao.config(text=f"Vídeo {self.feitos + 1} de {self.total}: "
                                      f"{self.atual} — {pct:.0f}%{falta}")
            return  # progresso não vai para os detalhes (seria uma linha por segundo)

        self._escrever(texto)
        novo = RE_ARQUIVO.match(texto)
        if novo:
            self.atual, self.inicio_arquivo = novo.group(3), time.time()
            self._marcar(self.atual, "Lendo o áudio...")
            self.situacao.config(text=f"Vídeo {self.feitos + 1} de {self.total}: {self.atual}")
        elif texto.startswith("Carregando modelo"):
            self.situacao.config(text="Carregando o modelo de IA... (na 1ª vez ele é baixado "
                                      "da internet: pode levar alguns minutos)")
        elif texto.startswith("OK:") and self.atual:
            self._marcar(self.atual, PRONTO)
            self.feitos += 1
            self.barra.config(value=self.feitos / max(self.total, 1) * 100)
        elif texto.startswith("ERRO") and self.atual:
            self._marcar(self.atual, "Erro (veja Detalhes)")
            self.feitos += 1
            self.erros += 1
        elif texto.startswith("GPU falhou") and self.atual:
            self._marcar(self.atual, "Repetindo...")

    def _terminou(self, codigo: int):
        self.processo = None
        self._botoes(rodando=False)
        prontos = self.feitos - self.erros
        if self.cancelado:
            if self.atual:
                self._marcar(self.atual, "Cancelado")
            resumo = f"Cancelado. {prontos} vídeo(s) prontos antes de cancelar."
        elif codigo != 0 and self.feitos < self.total:
            if self.atual:
                self._marcar(self.atual, "Erro (veja Detalhes)")
            resumo = "Parou por um erro. Copie o texto de Detalhes e me envie."
        else:
            self.barra.config(value=100)
            resumo = f"Concluído: {prontos} pronto(s)" + (f", {self.erros} com erro." if self.erros
                                                          else ".")
        self.situacao.config(text=resumo)
        self._escrever(f"=== {resumo} ===")
        if self.pendente_auto and not self.cancelado:  # chegou vídeo novo no meio da rodada
            self.raiz.after(300, lambda: self.iniciar(automatico=True))
        self.pendente_auto = False
        if not self.automatico and not self.cancelado and prontos and messagebox.askyesno(
                "Transcritor", f"{resumo}\n\nAbrir a pasta de resultados?"):
            self.abrir_pasta()

    def cancelar(self):
        if self.processo:
            self.cancelado = True
            self.processo.terminate()
            self.situacao.config(text="Cancelando...")

    # ------------------------------------------------------ pasta do OBS
    def escolher_obs(self):
        pasta = filedialog.askdirectory(title="Escolha a pasta onde o OBS grava os vídeos",
                                        initialdir=self.pasta_obs.get() or None)
        if pasta:
            self.pasta_obs.set(str(Path(pasta)))
            self.tamanhos.clear()

    def _ao_mudar_vigia(self):
        if self.vigiar.get():  # só valem os vídeos gravados a partir de agora
            self.vigia_desde = time.time()
            self.tamanhos.clear()
            if not self.processo:
                self.situacao.config(text="Vigiando a pasta do OBS: cada vídeo novo será "
                                          "transcrito quando a gravação terminar.")

    def _vigiar(self):
        try:
            self._olhar_pasta()
        finally:
            self.raiz.after(INTERVALO_VIGIA * 1000, self._vigiar)

    def _olhar_pasta(self):
        if not self.vigiar.get():
            return
        texto = self.pasta_obs.get().strip()
        pasta = Path(texto) if texto else None
        if pasta is None or not pasta.is_dir():
            if not self.processo:
                self.situacao.config(text="Escolha a pasta do OBS no quadro “Automático”."
                                     if pasta is None else
                                     f"Pasta do OBS não encontrada: {pasta}  (continuo procurando)")
            return
        agora, terminados = time.time(), []
        try:
            with os.scandir(pasta) as itens:
                for item in itens:
                    p = Path(item.path).resolve()
                    if (not item.is_file() or p.suffix.lower() not in EXTENSOES
                            or p in self.vistos_auto or p in self.arquivos):
                        continue
                    info = item.stat()
                    if info.st_mtime < self.vigia_desde - MARGEM_SEG:
                        continue  # gravação antiga, de antes de ligar o automático
                    anterior = self.tamanhos.get(p)
                    if anterior is None or anterior[0] != info.st_size:
                        self.tamanhos[p] = (info.st_size, agora)  # ainda crescendo
                    elif info.st_size and agora - anterior[1] >= ESTAVEL_SEG and livre(p):
                        terminados.append(p)
        except OSError as erro:
            self._escrever(f"Não consegui olhar a pasta do OBS: {erro}")
            return
        if not terminados:
            return
        for p in terminados:
            self.vistos_auto.add(p)
            self.tamanhos.pop(p, None)
            self._escrever(f"Vídeo novo na pasta do OBS: {p.name}")
        self.adicionar(sorted(terminados))
        if self.processo:
            self.pendente_auto = True  # espera "Na fila"; começa quando a rodada acabar
        else:
            self.iniciar(automatico=True)

    # ------------------------------------------------------------- utilidades
    def escolher_saida(self):
        if self._ocupado():
            return
        pasta = filedialog.askdirectory(title="Escolha onde salvar as transcrições",
                                        initialdir=self.saida.get() or None)
        if pasta:
            self.saida.set(str(Path(pasta)))
            for p in self.arquivos:
                self.tabela.set(str(p), "status", self._status_inicial(p))

    def _pasta_saida(self) -> Path:
        return Path(self.saida.get().strip() or SAIDA)

    def _salvar_config(self):
        dados = {"pasta_obs": self.pasta_obs.get(), "vigiar": self.vigiar.get(),
                 "saida": self.saida.get(), "modo": self.modo.get(),
                 "estilo": self.estilo.get(),
                 "numeros": "padrao" if self.padronizar.get() else "original"}
        try:
            CONFIG.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
                              encoding="utf-8")
        except OSError as erro:
            self._escrever(f"Não consegui salvar as escolhas ({CONFIG.name}): {erro}")

    def abrir_pasta(self):
        saida = self._pasta_saida()
        saida.mkdir(parents=True, exist_ok=True)
        if sys.platform == "win32":
            os.startfile(saida)  # noqa: S606 (abre a pasta no Explorer)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(saida)])
        else:
            subprocess.Popen(["xdg-open", str(saida)])

    def fechar(self):
        if self.processo and not messagebox.askyesno(
                "Transcritor", "Uma transcrição está em andamento. Cancelar e fechar?"):
            return
        if self.processo:
            self.processo.terminate()
        self.raiz.destroy()

    def _ocupado(self) -> bool:
        if self.processo:
            messagebox.showinfo("Transcritor", "Espere terminar (ou clique em Cancelar) "
                                               "para mexer na lista.")
            return True
        return False

    def _botoes(self, rodando: bool):
        self.bt_iniciar.config(state="disabled" if rodando else "normal")
        self.bt_cancelar.config(state="normal" if rodando else "disabled")
        for b in (self.bt_remover, self.bt_limpar, self.bt_saida):
            b.config(state="disabled" if rodando else "normal")

    def _escrever(self, texto: str):
        self.log.config(state="normal")
        self.log.insert("end", texto + "\n")
        self.log.see("end")
        self.log.config(state="disabled")
        try:  # registro.txt: os detalhes ficam guardados mesmo depois de fechar a janela
            with REGISTRO.open("a", encoding="utf-8") as registro:
                registro.write(texto + "\n")
        except OSError:
            pass


def main():
    if sys.platform == "win32":
        try:  # texto nítido em telas com zoom (125%, 150%)
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass
    raiz = TkinterDnD.Tk() if TEM_ARRASTAR else tk.Tk()
    Janela(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Aberta sem terminal (pythonw), um erro sumiria: grava num arquivo e avisa.
        (PASTA / "janela_erro.log").write_text(traceback.format_exc(), encoding="utf-8")
        try:
            messagebox.showerror("Transcritor", "A janela não abriu. O motivo está em "
                                 "janela_erro.log, na pasta do transcritor.")
        except Exception:
            pass
        raise
