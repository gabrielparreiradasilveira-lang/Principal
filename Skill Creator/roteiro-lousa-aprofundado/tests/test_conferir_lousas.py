# -*- coding: utf-8 -*-
"""Conferidor de lousas: ocupação, repetição da fala e nome do arquivo."""
import json
import os
import subprocess
import sys
import tempfile
import unittest

from PIL import Image, ImageDraw

import util_lousa  # noqa: F401  (põe scripts/ no caminho)
import conferir_lousas as C

SCRIPT = os.path.join(util_lousa.RAIZ, "scripts", "conferir_lousas.py")


def png_com_retangulo(tmp, caixa):
    img = Image.new("RGB", (1920, 1080), "black")
    ImageDraw.Draw(img).rectangle(caixa, fill="white")
    caminho = os.path.join(tmp, "x.png")
    img.save(caminho)
    return caminho


class TesteOcupacao(unittest.TestCase):
    def test_ocupacao_meia_tela(self):
        with tempfile.TemporaryDirectory() as tmp:
            v = C.ocupacao(png_com_retangulo(tmp, (80, 140, 900, 500)))
            self.assertTrue(0.40 <= v <= 0.42, v)

    def test_ocupacao_cheia(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertGreaterEqual(C.ocupacao(png_com_retangulo(tmp, (80, 140, 900, 1000))), 0.95)

    def test_ocupacao_ignora_webcam(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(C.ocupacao(png_com_retangulo(tmp, (1700, 900, 1710, 910))), 0.0)


class TesteRepeticao(unittest.TestCase):
    def test_repeticao_com_marcacao(self):
        lousa = "PEDÁGIO SOBRE A {vermelho:CARGA INTEIRA} DO CAMINHÃO QUE SAI DA RODOVIA"
        fala = "o pedágio sobre a carga inteira do caminhão que sai da rodovia"
        self.assertEqual(len(C.repeticoes(lousa, fala)), 1)

    def test_sem_repeticao_com_7_palavras(self):
        lousa = "PEDÁGIO SOBRE A {vermelho:CARGA INTEIRA} DO CAMINHÃO"
        fala = "o pedágio sobre a carga inteira do caminhão que sai da rodovia"
        self.assertEqual(C.repeticoes(lousa, fala), [])


class TesteNome(unittest.TestCase):
    def test_video_bloco(self):
        self.assertEqual(C.video_bloco("r50-1_2_metafora.png"), ("r50-1", 2))
        self.assertEqual(C.video_bloco("r60a_4_resolucao.png"), ("r60a", 4))
        self.assertIsNone(C.video_bloco("abertura.png"))


class TesteCLI(unittest.TestCase):
    def test_cli_aponta_repeticao_da_fala(self):
        roteiro = ("# R60A · Teste (7 min)\n\n## 2. Metáfora Central de Fixação — [1 min]\n"
                   "**[Ação na Lousa - Google Slides]**\n- Slide 2\n**[Locução Direta]**\n"
                   "\"Na saída o pedágio cobra sobre a carga inteira do caminhão que sai da rodovia.\"\n")
        lousas = {"padrao": {"fundo": "preto"}, "slides": [{"saida": "r60a_2_metafora.png", "elementos": [
            {"tipo": "titulo", "texto": "METÁFORA"},
            {"tipo": "texto", "x": 80, "y": 200, "largura": 1400, "tamanho": 34,
             "texto": "PEDÁGIO SOBRE A CARGA INTEIRA DO CAMINHÃO QUE SAI DA RODOVIA"}]}]}
        with tempfile.TemporaryDirectory() as tmp:
            r, j = os.path.join(tmp, "r.md"), os.path.join(tmp, "l.json")
            open(r, "w", encoding="utf-8").write(roteiro)
            json.dump(lousas, open(j, "w", encoding="utf-8"), ensure_ascii=False)
            out = subprocess.run([sys.executable, "-I", SCRIPT, r, j, "-o", tmp], capture_output=True, text=True)
        self.assertEqual(out.returncode, 1, out.stdout + out.stderr)
        self.assertIn("repete a fala", out.stdout)


if __name__ == "__main__":
    unittest.main()
