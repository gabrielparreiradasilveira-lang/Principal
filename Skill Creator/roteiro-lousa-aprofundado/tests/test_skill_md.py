# -*- coding: utf-8 -*-
"""SKILL.md: descrição dentro do limite (em bytes) e sem instruções que o professor descartou."""
import os
import re
import unittest

import util_lousa

SKILL = os.path.join(util_lousa.RAIZ, "SKILL.md")


class TesteSkillMd(unittest.TestCase):
    def setUp(self):
        self.texto = open(SKILL, encoding="utf-8").read()

    def test_descricao_cabe_em_1024_bytes(self):
        d = re.search(r"^description: (.*)$", self.texto, re.M).group(1)
        self.assertLessEqual(len(d.encode("utf-8")), 1024)

    def test_explica_como_dividir_lousa(self):
        self.assertIn("conteudo-1.png", self.texto)

    def test_sem_goodnotes(self):
        self.assertNotIn("goodnotes", self.texto.lower())


if __name__ == "__main__":
    unittest.main()
