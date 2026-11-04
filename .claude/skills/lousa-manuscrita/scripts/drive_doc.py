# -*- coding: utf-8 -*-
"""
Monta o HTML que vira um Google Doc com as lousas EMBUTIDAS (PNG 1920x1080) no Google Drive.

Por que assim: o conector do Drive só recebe o conteúdo do arquivo dentro do próprio comando, e um
PNG de ~300 KB não cabe ali. Um HTML com <img src="https://raw.githubusercontent.com/..."> cabe, e o
Google, ao converter o HTML em Doc, baixa e guarda cada imagem dentro do documento (conferido: as
imagens exportadas saem em PNG 1920x1080, sem depender do GitHub depois).

Uso (o commit já precisa estar no GitHub, e o repositório é público):
    python3 scripts/drive_doc.py <pasta-das-lousas> <sha-do-commit>
Copie a saída para o create_file do Drive: contentMimeType "text/html", title = 1ª linha impressa
(sem o "TITULO: "), parentId = pasta "Lousas — C-PRO R" no Drive.
"""
import json
import os
import subprocess
import sys

REPO = "https://raw.githubusercontent.com/gabrielparreiradasilveira-lang/Principal"


def main():
    pasta, sha = os.path.abspath(sys.argv[1]), sys.argv[2]
    raiz = subprocess.run(["git", "-C", pasta, "rev-parse", "--show-toplevel"], capture_output=True,
                          text=True, check=True).stdout.strip()
    rel = os.path.relpath(pasta, raiz)
    pngs = subprocess.run(["git", "-C", raiz, "ls-tree", "--name-only", sha, rel + "/"], capture_output=True,
                          text=True, check=True).stdout.split()
    pngs = sorted(p for p in pngs if p.endswith(".png") and not p.endswith("_grade.png"))
    if not pngs:
        sys.exit(f"nenhuma lousa .png em {rel} no commit {sha} (o commit já foi enviado?)")
    codigo = os.path.basename(pasta).split("-")[0].upper()
    spec = next((os.path.join(pasta, f) for f in os.listdir(pasta) if f.endswith("-lousas.json")), None)
    primeiro = json.load(open(spec, encoding="utf-8"))["slides"][0] if spec else {}
    tit = primeiro.get("titulo") or next((e.get("texto", "") for e in primeiro.get("elementos", [])
                                          if e.get("tipo") == "titulo"), "")
    tit = tit.replace(" ", " ").replace("\n", " ")
    print(f"TITULO: Lousas {codigo} — {tit} · {len(pngs)} lousas")
    print('<html><head><meta charset="utf-8"></head><body>')
    print(f"<p>Lousas {codigo} · {len(pngs)} lousas (PNG 1920×1080). Para baixar os PNGs: Arquivo → Fazer "
          "download → Página da Web (.html, compactado).</p>")
    for p in pngs:
        nome = os.path.basename(p)[:-4]
        print(f'<p><b>{nome}</b><br><img src="{REPO}/{sha}/{p}" width="624" height="351"></p>')
    print("</body></html>")


if __name__ == "__main__":
    main()
