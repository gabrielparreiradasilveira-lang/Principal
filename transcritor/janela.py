#!/usr/bin/env python3
"""
Janela do Transcritor de Videoaulas.

  1. Arraste os vídeos para a janela (ou clique para escolher)
  2. Escolha o modo
  3. Clique em Transcrever

Por baixo, a janela roda o mesmo transcrever.py, em um processo separado:
se algo der errado, a janela continua aberta, e "Cancelar" encerra na hora.
"""

from __future__ import annotations

import codecs
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
SAIDA = PASTA / "saida"

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
        self.modo = tk.StringVar(value="equilibrado")
        self.estilo = tk.StringVar(value="fiel")
        self.refazer = tk.BooleanVar(value=False)
        self._montar()
        self.raiz.protocol("WM_DELETE_WINDOW", self.fechar)
        self.raiz.after(100, self._ler_fila)

    # ------------------------------------------------------------------ tela
    def _montar(self):
        r = self.raiz
        r.title("Transcritor de Videoaulas")
        r.geometry("780x760")
        r.minsize(640, 600)
        font.nametofont("TkDefaultFont").configure(size=11)
        font.nametofont("TkTextFont").configure(size=10)
        estilo = ttk.Style()
        estilo.configure("Grande.TButton", font=("TkDefaultFont", 13, "bold"), padding=8)

        corpo = ttk.Frame(r, padding=14)
        corpo.pack(fill="both", expand=True)

        ttk.Label(corpo, text="Transcritor de Videoaulas",
                  font=("TkDefaultFont", 16, "bold")).pack(anchor="w")
        ttk.Label(corpo, text="1. Arraste os vídeos   →   2. Escolha o modo   →   "
                              "3. Clique em Transcrever").pack(anchor="w", pady=(2, 10))

        dica = ("Arraste os vídeos aqui\n(ou clique para escolher)" if TEM_ARRASTAR else
                "Clique aqui para escolher os vídeos\n(para arrastar e soltar, rode o "
                "instalador de novo)")
        self.zona = tk.Label(corpo, text=dica, relief="ridge", bd=2, height=4,
                             bg="#eef3fb", fg="#1f3b63", cursor="hand2",
                             font=("TkDefaultFont", 12, "bold"))
        self.zona.pack(fill="x")
        self.zona.bind("<Button-1>", lambda e: self.escolher())

        lista = ttk.Frame(corpo)
        lista.pack(fill="both", expand=True, pady=(10, 4))
        self.tabela = ttk.Treeview(lista, columns=("arquivo", "status"), show="headings",
                                   height=6, selectmode="extended")
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

        opcoes = ttk.Frame(corpo)
        opcoes.pack(fill="x", pady=10)
        quadro_modo = ttk.LabelFrame(opcoes, text="Modo", padding=8)
        quadro_modo.pack(side="left", fill="both", expand=True)
        for valor, nome, desc in MODOS:
            ttk.Radiobutton(quadro_modo, text=f"{nome} — {desc}", value=valor,
                            variable=self.modo).pack(anchor="w")
        quadro_estilo = ttk.LabelFrame(opcoes, text="Estilo do texto", padding=8)
        quadro_estilo.pack(side="left", fill="both", expand=True, padx=(10, 0))
        for valor, nome, desc in ESTILOS:
            ttk.Radiobutton(quadro_estilo, text=f"{nome} — {desc}", value=valor,
                            variable=self.estilo).pack(anchor="w")
        ttk.Checkbutton(quadro_estilo, text="Refazer vídeos já transcritos",
                        variable=self.refazer).pack(anchor="w", pady=(6, 0))

        acoes = ttk.Frame(corpo)
        acoes.pack(fill="x")
        self.bt_iniciar = ttk.Button(acoes, text="▶  Transcrever", style="Grande.TButton",
                                     command=self.iniciar)
        self.bt_iniciar.pack(side="left")
        self.bt_cancelar = ttk.Button(acoes, text="Cancelar", command=self.cancelar,
                                      state="disabled")
        self.bt_cancelar.pack(side="left", padx=8)
        ttk.Button(acoes, text="Abrir pasta de resultados",
                   command=self.abrir_pasta).pack(side="right")

        self.barra = ttk.Progressbar(corpo, maximum=100)
        self.barra.pack(fill="x", pady=(12, 2))
        self.situacao = ttk.Label(corpo, text="Pronto para começar.")
        self.situacao.pack(anchor="w")

        detalhes = ttk.LabelFrame(corpo, text="Detalhes (copie daqui se precisar de ajuda)",
                                  padding=4)
        detalhes.pack(fill="both", expand=True, pady=(10, 0))
        self.log = scrolledtext.ScrolledText(detalhes, height=7, state="disabled", wrap="word")
        self.log.pack(fill="both", expand=True)

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

    def _status_inicial(self, p: Path) -> str:
        feito = (SAIDA / f"{p.stem}.txt").exists()
        return JA_FEITO if feito and not self.refazer.get() else NA_FILA

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
    def iniciar(self):
        if self._ocupado():
            return
        if not self.arquivos:
            messagebox.showinfo("Transcritor", "Arraste ou escolha pelo menos um vídeo.")
            return
        for p in self.arquivos:
            self.tabela.set(str(p), "status", self._status_inicial(p))
        self.total = sum(1 for p in self.arquivos if self._status_inicial(p) == NA_FILA)
        if self.total == 0:
            messagebox.showinfo("Transcritor", "Todos esses vídeos já foram transcritos.\n"
                                "Para refazer, marque “Refazer vídeos já transcritos”.")
            return

        comando = [sys.executable, "-u", str(SCRIPT), "--modo", self.modo.get(),
                   "--estilo", self.estilo.get()]
        if self.refazer.get():
            comando.append("--forcar")
        comando += [str(p) for p in self.arquivos]
        ambiente = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUNBUFFERED="1")

        self.feitos = self.erros = 0
        self.atual, self.cancelado = None, False
        self.barra.config(value=0)
        self._escrever(f"\n=== Início: {self.total} vídeo(s), modo {self.modo.get()} ===")
        self.situacao.config(text="Iniciando...")
        self.processo = subprocess.Popen(
            comando, cwd=PASTA, env=ambiente, stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        threading.Thread(target=self._ler_saida, args=(self.processo,), daemon=True).start()
        self._botoes(rodando=True)

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
        if not self.cancelado and prontos and messagebox.askyesno(
                "Transcritor", f"{resumo}\n\nAbrir a pasta de resultados?"):
            self.abrir_pasta()

    def cancelar(self):
        if self.processo:
            self.cancelado = True
            self.processo.terminate()
            self.situacao.config(text="Cancelando...")

    # ------------------------------------------------------------- utilidades
    def abrir_pasta(self):
        SAIDA.mkdir(exist_ok=True)
        if sys.platform == "win32":
            os.startfile(SAIDA)  # noqa: S606 (abre a pasta no Explorer)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(SAIDA)])
        else:
            subprocess.Popen(["xdg-open", str(SAIDA)])

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
        for b in (self.bt_remover, self.bt_limpar):
            b.config(state="disabled" if rodando else "normal")

    def _escrever(self, texto: str):
        self.log.config(state="normal")
        self.log.insert("end", texto + "\n")
        self.log.see("end")
        self.log.config(state="disabled")


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
