# -*- coding: utf-8 -*-
"""
Monta os pedidos (batchUpdate) que põem cada lousa como fundo de um slide no Google Slides.

Uso: python3 slides.py --dono D --repo R --sha SHA [--slide-inicial p] caminho1.png caminho2.png ...
Os caminhos são relativos à raiz do repositório e o commit (SHA) já precisa estar no GitHub:
o Google baixa cada imagem da URL raw do GitHub e guarda uma cópia na apresentação.
Imprime o JSON da lista "requests" para o update_presentation do conector do Google Slides.
"""
import argparse
import json
import os
import re
import sys
import unicodedata
from urllib.parse import quote


def url_raw(dono, repo, sha, caminho):
    trechos = [quote(t) for t in caminho.strip("/").split("/")]
    return f"https://raw.githubusercontent.com/{dono}/{repo}/{sha}/" + "/".join(trechos)


def object_id(i, nome_png):
    base = os.path.splitext(os.path.basename(nome_png))[0]
    base = unicodedata.normalize("NFKD", base).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^A-Za-z0-9_-]+", "-", base).strip("-")
    return f"lousa_{i:02d}_{slug}"[:50]


def requisicoes(caminhos, dono, repo, sha, slide_inicial="p"):
    out = []
    for i, c in enumerate(caminhos, 1):
        oid = object_id(i, c)
        out.append({"createSlide": {"objectId": oid, "slideLayoutReference": {"predefinedLayout": "BLANK"}}})
        out.append({"updatePageProperties": {
            "objectId": oid,
            "pageProperties": {"pageBackgroundFill": {"stretchedPictureFill": {"contentUrl": url_raw(dono, repo, sha, c)}}},
            "fields": "pageBackgroundFill"}})
    if slide_inicial is not None:
        out.append({"deleteObject": {"objectId": slide_inicial}})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="Pedidos do Google Slides com as lousas como fundo.")
    ap.add_argument("--dono", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--sha", required=True)
    ap.add_argument("--slide-inicial", default="p", help="id do slide em branco a apagar ('' para não apagar)")
    ap.add_argument("pngs", nargs="+")
    a = ap.parse_args(argv)
    print(json.dumps(requisicoes(a.pngs, a.dono, a.repo, a.sha, a.slide_inicial or None), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
