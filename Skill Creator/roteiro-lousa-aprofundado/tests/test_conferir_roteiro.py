# -*- coding: utf-8 -*-
"""Conferidor do roteiro: 4 blocos, sem Nota de bastidor, ids R60A e R50-1."""
import os
import subprocess
import sys
import tempfile
import unittest

import util_lousa

SCRIPT = os.path.join(util_lousa.RAIZ, "scripts", "conferir_roteiro.py")
NOMES = {1: "Abertura Instigante (Destruição de Mito)", 2: "Metáfora Central de Fixação",
         3: "Conteúdo Técnico e Roteiro Visual", 4: "Resolução Rápida de Fixação",
         5: "Alerta de Prova e Pegadinha da Banca"}


def roteiro(blocos=(1, 2, 3, 4), palavras=(70, 100, 370, 125), nota=False, video="R50-1"):
    partes = [f"# {video} · Tema de teste (7 min)", "**Base:** item 3.7.4 · apostila p. 150", ""]
    for b, n in zip(blocos, palavras):
        fala = " ".join(["termo"] * (n - 2)) + (" em 2026" if b == 1 else " fim.")
        partes += [f"## {b}. {NOMES[b]} — [1 min]", "**[Ação na Lousa - Google Slides]**", f"- Slide {b}",
                   "**[Locução Direta]**", f"\"{fala}\"", ""]
    if nota:
        partes += ["### Nota de bastidor (fora do teleprompter)", "- Fonte: apostila."]
    return "\n".join(partes) + "\n"


def conferir(texto):
    with tempfile.TemporaryDirectory() as tmp:
        caminho = os.path.join(tmp, "r.md")
        open(caminho, "w", encoding="utf-8").write(texto)
        return subprocess.run([sys.executable, "-I", SCRIPT, caminho], capture_output=True, text=True)


class TesteConferirRoteiro(unittest.TestCase):
    def test_quatro_blocos_ok(self):
        r = conferir(roteiro())
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_cinco_blocos_pendencia(self):
        r = conferir(roteiro(blocos=(1, 2, 3, 5, 4), palavras=(70, 100, 300, 70, 125)))
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("blocos", r.stdout)

    def test_nota_pendencia(self):
        r = conferir(roteiro(nota=True))
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("Nota de bastidor", r.stdout)

    def test_id_r60a_aceito(self):
        r = conferir(roteiro(video="R60A"))
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("R60A", r.stdout)


if __name__ == "__main__":
    unittest.main()
