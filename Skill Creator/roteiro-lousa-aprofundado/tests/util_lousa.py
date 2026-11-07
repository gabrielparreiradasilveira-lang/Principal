# -*- coding: utf-8 -*-
"""Utilitário dos testes: desenha uma lousa (dict) e devolve avisos, imagem e lousa."""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
sys.dont_write_bytecode = True

import lousa as LOUSA  # noqa: E402
import moldes as MOLDES  # noqa: E402


def renderizar(spec, salvar=None):
    spec = dict({"fundo": "preto"}, **spec)
    avisos = []
    L = LOUSA.Lousa(spec, RAIZ, avisos)
    elementos = MOLDES.montar(L, spec)
    L.desenhar(elementos)
    L.conferir()
    img = L.finalizar()
    if salvar:
        img.save(salvar)
    return avisos, img, elementos
