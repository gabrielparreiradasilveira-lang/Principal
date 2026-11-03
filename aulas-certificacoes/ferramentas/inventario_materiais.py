#!/usr/bin/env python3
"""Gera o inventário dos materiais de aula do repositório (JSON de linhas).

Uso:  python3 ferramentas/inventario_materiais.py > inventario.json
Roda a partir de aulas-certificacoes/. Lê só arquivos versionados no git
(aulas, roteiros, materiais e modelos) e ignora 00-fontes/.
Cada linha traz: certificação, tipo, código, item do PD, módulo, título,
duração declarada, palavras, pendências ("não confirmado"), data do último
commit, nº de commits, caminho e link no GitHub.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_URL = "https://github.com/gabrielparreiradasilveira-lang/Principal"
BRANCH = "claude/admiring-euler-76f74n"
PREFIXO = "aulas-certificacoes"

ITEM_RE = re.compile(r"\d\.\d+(?:\.\d+)*")
# itens de 2 níveis do Programa Detalhado ANBIMA v1.2 (vigência 01/01/2026)
PD_ITENS = {
    "CPA": {"1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "2.3", "2.4", "2.5", "3.1", "3.2", "3.3", "3.4",
            "4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7"},
    "C-PRO R": {"1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "2.1", "2.2", "2.3", "2.4", "3.1", "3.2", "3.3",
                "3.4", "3.5", "3.6", "3.7", "3.8", "4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "4.9"},
}
CERT_NOME = {"cpa": "CPA", "cpro-r": "C-PRO R", "c-pro-r": "C-PRO R", "c-pro-i": "C-PRO I", "geral": "Geral"}


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def classificar(p: Path):
    s = p.as_posix()
    nome = p.name
    if s.startswith("aulas/"):
        return s.split("/")[1], "Aula completa (7 etapas)", p.parent.name
    if s.startswith("roteiros/"):
        cert = s.split("/")[1]
        if nome == "PLANO-CALENDARIO.md":
            return cert, "Planejamento", nome
        if nome.startswith("revisao-modulo"):
            return cert, "Revisão de módulo", nome
        if "/guias-15-10/" in s:
            return cert, "Guia de fala", nome
        if nome.startswith("hp12c"):
            return cert, "Roteiro HP12C", nome
        if nome.startswith("roteiro-fala-comentado"):
            return cert, "Roteiro comentado", nome
        if nome.endswith("-lousa.md"):
            return cert, "Roteiro de lousa", nome
        return cert, "Roteiro de fala", nome
    if s.startswith("materiais/"):
        partes = s.split("/")
        cert, pasta = partes[1], partes[2]
        if pasta.startswith("manual-revisao"):
            return cert, "Manual de revisão (PDF)", pasta
        if pasta.startswith("slides-modulo"):
            return cert, "Slides de revisão (PDF)", pasta
        if nome.endswith(".pptx"):
            return cert, "Deck X8 (PPTX)", pasta
        return cert, "Roteiro + deck X8", pasta
    if s.startswith("modelos/"):
        return "geral", "Modelo", nome
    return None


def codigo_de(nome: str):
    for padrao, fmt in ((r"-(G\d+|F\d+|R\d+)-", "{}"), (r"aula-[\d.]+-([A-H])-", "{}"),
                        (r"revisao-modulo-(\d)", "M{}"), (r"aula-(\d+)-", "Aula {}")):
        m = re.search(padrao, nome)
        if m:
            return fmt.format(m.group(1))
    return ""


def main():
    linhas = []
    for p in sorted(Path(f) for f in git("ls-files").splitlines()):
        if p.suffix not in {".md", ".pdf", ".pptx"}:
            continue
        cls = classificar(p)
        if not cls:
            continue
        cert, tipo, chave = cls
        if tipo.endswith("(PDF)") and p.suffix != ".pdf":
            continue
        texto = p.read_text(encoding="utf-8", errors="ignore") if p.suffix == ".md" else ""
        cabeca = "\n".join(texto.splitlines()[:15])
        titulo = next((l.lstrip("# ").strip() for l in texto.splitlines() if l.startswith("# ")), p.stem)
        m = ITEM_RE.search(chave) or ITEM_RE.search(cabeca)
        item = m.group(0) if m else ""
        if tipo in {"Planejamento", "Modelo", "Roteiro comentado"}:
            item = ""
        elif tipo == "Deck X8 (PPTX)":
            irmao = next(p.parent.glob("roteiro-*.md"), None)
            mm = ITEM_RE.search("\n".join(irmao.read_text(encoding="utf-8").splitlines()[:5])) if irmao else None
            item = mm.group(0) if mm else ""
        elif tipo == "Revisão de módulo":
            item = "M" + re.search(r"modulo-(\d)", p.name).group(1)
        elif tipo.endswith("(PDF)"):
            mm = re.search(r"modulo-(\d)", chave)
            item = "M" + mm.group(1) if mm else item
        # itens de 2 níveis (ex.: 1.3) citados no cabeçalho, para medir a cobertura do PD
        limpo = re.sub(r"(v|vers[ãa]o\s*)1\.2|\d\.\d{3}\b|p\.\s*[\d.–-]+", " ", cabeca)
        validos = PD_ITENS.get(CERT_NOME.get(cert, cert), set())
        # o item principal; nas aulas com deck X8 o cabeçalho lista vários ("Itens 1.3, 1.5 e 1.6")
        # e o nome do arquivo pode trazer uma faixa ("aula-4.2.6-4.3-...")
        fonte_itens = (limpo + " " + item) if tipo in {"Roteiro + deck X8", "Deck X8 (PPTX)"} else item + " " + chave
        itens = sorted({".".join(i.split(".")[:2]) for i in ITEM_RE.findall(fonte_itens)} & validos,
                       key=lambda i: [int(n) for n in i.split(".")]) if item and not item.startswith("M") else []
        dur = re.search(r"(\d{1,3})\s*min", cabeca)
        datas = git("log", "--format=%cs", "--", p.as_posix()).split()
        linhas.append({
            "cert": CERT_NOME.get(cert, cert),
            "tipo": tipo,
            "codigo": codigo_de(p.name) if p.suffix == ".md" else "",
            "item": item,
            "itens": " ".join(itens),
            "modulo": item[1:] if item.startswith("M") else item[:1],
            "titulo": titulo[:160],
            "duracao_min": int(dur.group(1)) if dur else None,
            "palavras": len(texto.split()) if texto else None,
            "pendencias": len(re.findall(r"n[ãa]o confirmad", texto, re.I)),
            "ultimo_commit": datas[0] if datas else None,
            "commits": len(datas),
            "caminho": f"{PREFIXO}/{p.as_posix()}",
            "link": f"{REPO_URL}/blob/{BRANCH}/{PREFIXO}/{p.as_posix()}",
        })
    json.dump(linhas, sys.stdout, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
