# -*- coding: utf-8 -*-
"""Moldes novos: comparacao, exercicio e mito_verdade com apoio."""
import os
import tempfile
import unittest

from util_lousa import renderizar

DUAS_RODOVIAS = {
    "molde": "comparacao", "semente": 502,
    "titulo": "DUAS RODOVIAS ATÉ A APOSENTADORIA",
    "colunas": [
        {"titulo": "RODOVIA VGBL", "desenho": "rodovia_pedagio", "rotulos": ["ENTRADA = APORTE", "SAÍDA = RESGATE"],
         "texto": "- ENTRADA: {vermelho:SEM VALE-PEDÁGIO}\n- SAÍDA: PEDÁGIO SÓ SOBRE O {verde:LUCRO DA VIAGEM} "
                  "(OS RENDIMENTOS)\n- MESMA CARGA, BASE MENOR: SÓ O QUE A CARGA GANHOU NO CAMINHO"},
        {"titulo": "RODOVIA PGBL", "desenho": "rodovia_pedagio", "rotulos": ["ENTRADA = APORTE", "SAÍDA = RESGATE"],
         "texto": "- ENTRADA: {verde:VALE-PEDÁGIO} DE ATÉ {laranja:12% DA RENDA BRUTA TRIBUTÁVEL}\n- VALE SÓ NA "
                  "{laranja:DECLARAÇÃO COMPLETA} E, EM REGRA, COM INSS OU REGIME PRÓPRIO\n- SAÍDA: PEDÁGIO SOBRE A "
                  "{vermelho:CARGA INTEIRA} (VALOR TOTAL)"},
    ],
    "faixas": [
        "{ciano:TARIFA DA SAÍDA, NAS DUAS:} REGRESSIVO {laranja:35% → 10%} PELO TEMPO DE CADA APORTE · "
        "PROGRESSIVO: {laranja:TABELA DO IR}",
        "{ciano:CARGA DE EXEMPLO:} APORTES DE R$ 50.000 QUE VIRARAM R$ 80.000 → BASE NO VGBL {verde:R$ 30.000} · "
        "NO PGBL {vermelho:R$ 80.000}",
    ],
    "destaque": {"texto": "{vermelho:RODOVIA ERRADA:} PGBL NA DECLARAÇÃO SIMPLIFICADA NÃO USA O VALE E AINDA PAGA "
                          "PEDÁGIO SOBRE A CARGA INTEIRA", "cor": "branco", "moldura": "vermelho"},
}


class TesteComparacao(unittest.TestCase):
    def test_comparacao_amostra_sem_avisos(self):
        with tempfile.TemporaryDirectory() as tmp:
            png = os.path.join(tmp, "r50-1_2_duas-rodovias.png")
            avisos, img, _ = renderizar(DUAS_RODOVIAS, salvar=png)
            self.assertEqual(avisos, [])
            self.assertEqual(img.size, (1920, 1080))
            self.assertTrue(os.path.exists(png))

    @unittest.skip("Tarefa 4: conferir_lousas.ocupacao")
    def test_comparacao_amostra_ocupa_70(self):
        import conferir_lousas
        with tempfile.TemporaryDirectory() as tmp:
            png = os.path.join(tmp, "r50-1_2_duas-rodovias.png")
            renderizar(DUAS_RODOVIAS, salvar=png)
            self.assertGreaterEqual(conferir_lousas.ocupacao(png), 0.70)


if __name__ == "__main__":
    unittest.main()
