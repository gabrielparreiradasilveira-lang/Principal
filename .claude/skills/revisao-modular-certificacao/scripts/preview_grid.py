"""Gera grades de miniaturas (8 páginas por imagem) de um PDF, para revisão visual.

Uso: python3 preview_grid.py manual.pdf [pasta_saida]
Imprime o caminho de cada grade; abra-as com a ferramenta de leitura de imagem.
Para checar uma página em detalhe: pymupdf.open(pdf)[i].get_pixmap(dpi=110).save(...)
"""
import os
import sys

import pymupdf
from PIL import Image

pdf = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(pdf))
doc = pymupdf.open(pdf)
pages = []
for i in range(doc.page_count):
    p = os.path.join(out, f"_prev_p{i + 1:02d}.png")
    doc[i].get_pixmap(dpi=60).save(p)
    pages.append(p)
for g in range(0, len(pages), 8):
    imgs = [Image.open(p) for p in pages[g:g + 8]]
    w, h = imgs[0].size
    grid = Image.new("RGB", (w * 4, h * 2), "white")
    for k, im in enumerate(imgs):
        grid.paste(im, ((k % 4) * w, (k // 4) * h))
    path = os.path.join(out, f"_prev_grid{g // 8 + 1}.png")
    grid.save(path)
    print(path)
for p in pages:
    os.remove(p)
print(f"{doc.page_count} páginas")
