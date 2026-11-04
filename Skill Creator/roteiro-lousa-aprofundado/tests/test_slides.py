# -*- coding: utf-8 -*-
"""Pedidos do Google Slides: URL do GitHub, ids dos slides e ordem dos pedidos."""
import re
import unittest

import util_lousa  # noqa: F401  (põe scripts/ no caminho)
import slides as S


class TesteSlides(unittest.TestCase):
    def test_url_codifica_espaco(self):
        u = S.url_raw("dono", "Principal", "abc123", "Skill Creator/a b.png")
        self.assertEqual(u, "https://raw.githubusercontent.com/dono/Principal/abc123/Skill%20Creator/a%20b.png")

    def test_object_id_limites(self):
        i = S.object_id(3, "r50-1_2_metáfora-das-duas-rodovias-até-a-aposentadoria-longa.png")
        self.assertTrue(5 <= len(i) <= 50, i)
        self.assertRegex(i, r"^[A-Za-z0-9_-]+$")

    def test_requisicoes_dois_pngs(self):
        r = S.requisicoes(["a/r50-1_1_abertura.png", "a/r50-1_2_metafora.png"], "d", "R", "s1")
        self.assertEqual([list(x)[0] for x in r],
                         ["createSlide", "updatePageProperties", "createSlide", "updatePageProperties", "deleteObject"])
        url = r[1]["updatePageProperties"]["pageProperties"]["pageBackgroundFill"]["stretchedPictureFill"]["contentUrl"]
        self.assertEqual(url, "https://raw.githubusercontent.com/d/R/s1/a/r50-1_1_abertura.png")
        self.assertEqual(r[1]["updatePageProperties"]["fields"], "pageBackgroundFill")
        self.assertEqual(r[0]["createSlide"]["slideLayoutReference"], {"predefinedLayout": "BLANK"})
        self.assertEqual(r[0]["createSlide"]["objectId"], r[1]["updatePageProperties"]["objectId"])
        self.assertEqual(r[4], {"deleteObject": {"objectId": "p"}})

    def test_sem_slide_inicial(self):
        r = S.requisicoes(["a/x_1_y.png"], "d", "R", "s1", slide_inicial=None)
        self.assertNotIn("deleteObject", [list(x)[0] for x in r])


if __name__ == "__main__":
    unittest.main()
