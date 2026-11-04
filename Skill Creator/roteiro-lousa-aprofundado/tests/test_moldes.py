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
    def test_comparacao_valores_nao_quebram(self):
        _, _, elementos = renderizar(DUAS_RODOVIAS)
        for e in elementos:
            if str(e.get("id", ""))[:2] in ("ct", "cf"):
                self.assertNotIn("R$ ", e["texto"])

    def test_comparacao_amostra_sem_avisos(self):
        with tempfile.TemporaryDirectory() as tmp:
            png = os.path.join(tmp, "r50-1_2_duas-rodovias.png")
            avisos, img, _ = renderizar(DUAS_RODOVIAS, salvar=png)
            self.assertEqual(avisos, [])
            self.assertEqual(img.size, (1920, 1080))
            self.assertTrue(os.path.exists(png))

    def test_comparacao_desenho_alto_nao_sobrepoe(self):
        spec = dict(DUAS_RODOVIAS, colunas=[
            dict(DUAS_RODOVIAS["colunas"][0], desenho={"nome": "casa", "largura": 220}, rotulos=[]),
            dict(DUAS_RODOVIAS["colunas"][1], desenho={"nome": "balanca_peso", "largura": 240}, rotulos=[])])
        avisos, _, _ = renderizar(spec)
        self.assertEqual(avisos, [])

    def test_comparacao_amostra_ocupa_70(self):
        import conferir_lousas  # noqa: E402
        with tempfile.TemporaryDirectory() as tmp:
            png = os.path.join(tmp, "r50-1_2_duas-rodovias.png")
            renderizar(DUAS_RODOVIAS, salvar=png)
            self.assertGreaterEqual(conferir_lousas.ocupacao(png), 0.70)


EXERCICIO_R50_1 = {
    "molde": "exercicio", "semente": 505,
    "titulo": "MESMO RESGATE, MUDA SÓ O PRODUTO",
    "dados": "- SALDO DE R$ 150.000, COM R$ 100.000 APORTADOS HÁ MAIS DE 10 ANOS · REGRESSIVO ({laranja:10%})\n"
             "- RESGATE DE {laranja:R$ 30.000} (NÚMEROS HIPOTÉTICOS)",
    "cenarios": [
        {"titulo": "VGBL", "passos": "- R$ 30.000 = 20% DO SALDO\n- SAEM 20% DOS APORTES: R$ 20.000\n"
                                      "- RENDIMENTO = R$ 30.000 − R$ 20.000 = R$ 10.000",
         "resultado": "IR = 10% × R$ 10.000 = R$ 1.000"},
        {"titulo": "PGBL", "passos": "- BASE = VALOR TOTAL DO RESGATE\n- BASE = R$ 30.000",
         "resultado": "IR = 10% × R$ 30.000 = R$ 3.000"},
    ],
    "conclusao": {"texto": "MESMO RESGATE: O VGBL PAGA {verde:R$ 2.000 A MENOS}, PORQUE A BASE É SÓ O RENDIMENTO",
                  "cor": "branco", "moldura": "amarelo"},
}

MITO_COM_APOIO = {
    "molde": "mito_verdade", "semente": 501,
    "titulo": "VGBL · C-PRO R 3.7.4.1",
    "mitos": ["\"O VGBL É UM PGBL PIORADO, PORQUE NÃO DEDUZ NADA\""],
    "verdade": "O VGBL SERVE A OUTRO CLIENTE: O IR INCIDE SÓ SOBRE OS RENDIMENTOS",
    "desenho": {"nome": "placa", "largura": 200},
    "apoio": "- PREVIDÊNCIA ABERTA, JAN. A AGO./2026: VGBL COM {laranja:R$ 94,5 BILHÕES}, CERCA DE 90% DOS APORTES\n"
             "- QUEM USA: DECLARAÇÃO SIMPLIFICADA · SEM INSS · JÁ USOU OS 12% DO PGBL · SUCESSÃO",
}


class TesteExercicio(unittest.TestCase):
    def test_exercicio_r50_1_sem_avisos(self):
        avisos, img, elementos = renderizar(EXERCICIO_R50_1)
        self.assertEqual(avisos, [])
        texto = " ".join(str(e.get("texto", "")) for e in elementos).replace("\u00a0", " ")
        self.assertIn("R$ 1.000", texto)
        self.assertIn("R$ 3.000", texto)

    def test_exercicio_valores_nao_quebram(self):
        _, _, elementos = renderizar(EXERCICIO_R50_1)
        for e in elementos:
            if str(e.get("id", ""))[:2] in ("er", "ep", "da"):
                self.assertNotIn("R$ ", e["texto"])

    def test_exercicio_sem_buraco_no_meio(self):
        _, img, _ = renderizar(EXERCICIO_R50_1)
        self.assertLessEqual(maior_faixa_vazia(img, 200, 1000), 130)


def maior_faixa_vazia(img, y0, y1):
    """Maior sequência de linhas sem tinta entre y0 e y1 (ignora o canto da webcam, x >= 1600)."""
    g = img.convert("L").crop((0, y0, 1600, y1))
    larg, alt = g.size
    px = g.load()
    maior = atual = 0
    for y in range(alt):
        if any(px[x, y] > 40 for x in range(0, larg, 2)):
            atual = 0
        else:
            atual += 1
            maior = max(maior, atual)
    return maior


class TesteMitoComApoio(unittest.TestCase):
    def test_apoio_valores_nao_quebram(self):
        _, _, elementos = renderizar(MITO_COM_APOIO)
        self.assertNotIn("R$ ", [e for e in elementos if e.get("id") == "apoio"][0]["texto"])

    def test_mito_verdade_com_apoio_sem_avisos(self):
        avisos, img, elementos = renderizar(MITO_COM_APOIO)
        self.assertEqual(avisos, [])
        apoio = [e for e in elementos if e.get("id") == "apoio"]
        self.assertEqual(len(apoio), 1)
        self.assertGreater(apoio[0]["y"], 640)


if __name__ == "__main__":
    unittest.main()
