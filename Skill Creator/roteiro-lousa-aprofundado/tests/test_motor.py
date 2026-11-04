# -*- coding: utf-8 -*-
"""O motor copiado da lousa-manuscrita desenha exatamente a mesma lousa."""
import os
import sys
import tempfile
import unittest

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), "scripts"))
FIX = os.path.join(AQUI, "fixtures")


class TesteMotor(unittest.TestCase):
    def test_reproduz_exemplo(self):
        import lousa
        with tempfile.TemporaryDirectory() as tmp:
            lousa.main([os.path.join(FIX, "mito-x-verdade.json"), "-o", tmp])
            pngs = [f for f in os.listdir(tmp) if f.endswith(".png")]
            self.assertEqual(len(pngs), 1)
            with open(os.path.join(tmp, pngs[0]), "rb") as a, open(os.path.join(FIX, "mito-x-verdade.png"), "rb") as b:
                self.assertEqual(a.read(), b.read())

    def test_mito_verdade_sem_apoio_igual_ao_original(self):
        """Proteção: o molde mito_verdade sem 'apoio' continua desenhando a lousa da outra sessão."""
        import lousa
        with tempfile.TemporaryDirectory() as tmp:
            lousa.main([os.path.join(FIX, "r50-1_01_abertura-mito.json"), "-o", tmp])
            with open(os.path.join(tmp, "r50-1_01_abertura-mito.png"), "rb") as a, \
                    open(os.path.join(FIX, "r50-1_01_abertura-mito.png"), "rb") as b:
                self.assertEqual(a.read(), b.read())


if __name__ == "__main__":
    unittest.main()
