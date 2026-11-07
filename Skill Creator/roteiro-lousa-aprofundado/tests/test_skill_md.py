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

    def test_regra_de_nao_citar_a_apostila(self):
        self.assertIn("Nunca cite a apostila", self.texto)

    def test_esqueleto_sem_apostila_na_base(self):
        base = [l for l in self.texto.splitlines() if l.startswith("**Base:**")]
        self.assertTrue(base)
        for l in base:
            self.assertNotIn("apostila", l.lower())

    def test_sem_goodnotes(self):
        self.assertNotIn("goodnotes", self.texto.lower())

    def test_regras_novas_da_lousa(self):
        for termo in ("premissas", "PAUSE E RESPONDA", "referencia", "12 palavras", "legenda", "sintese",
                      "regra → efeito"):
            self.assertTrue(termo in self.texto, termo)


def jsons_de_exemplo(caminho):
    """Lousas em JSON dentro dos blocos ```json de um arquivo de referência."""
    import json
    texto = open(caminho, encoding="utf-8").read()
    out = []
    for bloco in re.findall(r"```json\n(.*?)```", texto, re.S):
        try:
            d = json.loads(bloco)
        except json.JSONDecodeError:  # esqueleto com "...", não é lousa
            continue
        if isinstance(d, dict) and d.get("molde"):
            out.append(d)
    return out


class TesteExemplosDaDocumentacao(unittest.TestCase):
    """As lousas de exemplo da documentação seguem as regras que o conferidor cobra."""

    def exemplos(self):
        refs = os.path.join(util_lousa.RAIZ, "references")
        ex = jsons_de_exemplo(os.path.join(refs, "lousas.md")) + jsons_de_exemplo(os.path.join(refs, "exemplo-item.md"))
        self.assertGreaterEqual(len(ex), 2)
        return ex

    def test_exemplos_sem_avisos_e_dentro_das_regras(self):
        import conferir_lousas as C
        from util_lousa import renderizar
        for spec in self.exemplos():
            avisos, _, els = renderizar(spec)
            self.assertEqual(avisos, [], spec["saida"])
            texto = C.texto_da_lousa(els)
            self.assertEqual(C.cor_sem_rotulo(texto), [], spec["saida"])
            self.assertEqual(C.topicos_longos(texto), [], spec["saida"])
            refs = spec.get("referencia")
            self.assertTrue(refs, spec["saida"])
            for r in ([refs] if isinstance(refs, str) else refs):
                self.assertTrue(C.referencia_ok(r), r)


if __name__ == "__main__":
    unittest.main()
