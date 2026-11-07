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
         "texto": "- ✗ ENTRADA: {vermelho:SEM VALE-PEDÁGIO}\n- ✓ SAÍDA: PEDÁGIO SÓ SOBRE O {verde:LUCRO DA VIAGEM} "
                  "(OS RENDIMENTOS)\n- MESMA CARGA, BASE MENOR: SÓ O QUE A CARGA GANHOU NO CAMINHO"},
        {"titulo": "RODOVIA PGBL", "desenho": "rodovia_pedagio", "rotulos": ["ENTRADA = APORTE", "SAÍDA = RESGATE"],
         "texto": "- ✓ ENTRADA: {verde:VALE-PEDÁGIO} DE ATÉ {laranja:12% DA RENDA BRUTA TRIBUTÁVEL}\n"
                  "  - SÓ NA {laranja:DECLARAÇÃO COMPLETA} E, EM REGRA, COM INSS OU REGIME PRÓPRIO\n"
                  "- ✗ SAÍDA: PEDÁGIO SOBRE A {vermelho:CARGA INTEIRA} (VALOR TOTAL)"},
    ],
    "faixas": [
        "{ciano:TARIFA DA SAÍDA, NAS DUAS:} REGRESSIVO {laranja:35% → 10%} PELO TEMPO DE CADA APORTE · "
        "PROGRESSIVO: {laranja:TABELA DO IR}",
        "{ciano:CARGA DE EXEMPLO:} APORTES DE R$ 50.000 QUE VIRARAM R$ 80.000 → BASE NO VGBL {laranja:R$ 30.000} · "
        "NO PGBL {laranja:R$ 80.000}",
    ],
    "destaque": {"texto": "✗ {vermelho:RODOVIA ERRADA:} PGBL NA DECLARAÇÃO SIMPLIFICADA NÃO USA O VALE E AINDA PAGA "
                          "PEDÁGIO SOBRE A CARGA INTEIRA", "cor": "branco", "moldura": "vermelho"},
    "referencia": ["IR DA PREVIDÊNCIA (LEI 11.053/2004)", "DEDUÇÃO DO PGBL (LEI 9.532/1997)"],
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


class TesteMoldesAntigos(unittest.TestCase):
    def test_topicos_e_colunas_valores_nao_quebram(self):
        topicos = {"molde": "topicos", "titulo": "T", "texto": "- BASE = R$ 10.000", "destaque": "SAEM R$ 40.000"}
        colunas = {"molde": "colunas", "titulo": "T", "topo": "TOPO R$ 1", "destaque": "X R$ 2",
                   "colunas": [{"titulo": "A", "texto": "- R$ 3"}, {"titulo": "B", "texto": "- R$ 4"}]}
        for spec in (topicos, colunas):
            _, _, elementos = renderizar(spec)
            for e in elementos:
                if isinstance(e.get("texto"), str):
                    self.assertNotIn("R$ ", e["texto"], (spec["molde"], e.get("id")))


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


EXERCICIO_V5 = {
    "molde": "exercicio", "semente": 588, "saida": "r58b_4_resolucao.png",
    "titulo": "MESMO DINHEIRO, MUDA SÓ A CONCENTRAÇÃO",
    "dados": "- CLIENTE COM {laranja:R$ 400.000} EM CDB, JÁ COM OS RENDIMENTOS\n"
             "- FGC: ATÉ {laranja:R$ 250.000} POR CPF E POR CONGLOMERADO\n"
             "  - TETO DE R$ 1 MILHÃO A CADA 4 ANOS",
    "premissas": "VALORES HIPOTÉTICOS · X E Y SÃO DE CONGLOMERADOS DIFERENTES",
    "cenarios": [
        {"titulo": "A: TUDO NO BANCO X",
         "passos": "- COBERTO: R$ 250.000\n- DESCOBERTO: R$ 400.000 − R$ 250.000 = R$ 150.000\n"
                   "- O EXCESSO VAI PARA A LIQUIDAÇÃO",
         "resultado": "37,5% FORA DO FGC"},
        {"titulo": "B: R$ 200.000 EM X E EM Y",
         "passos": "- CADA BANCO ABAIXO DE R$ 250.000\n- TOTAL ABAIXO DO TETO DE R$ 1 MILHÃO",
         "resultado": "100% COBERTO"},
    ],
    "conclusao": {"texto": "{ciano:POR QUÊ:} O LIMITE VALE POR CONGLOMERADO → DIVIDIR TIROU R$ 150.000 DO RISCO",
                  "cor": "branco", "moldura": "amarelo"},
    "pergunta": "E SE X E Y FOSSEM DO MESMO CONGLOMERADO?",
    "sintese": "RISCO = INCERTEZA → RÉGUA: SELIC → MAIS RISCO EXIGE MAIS RETORNO",
    "referencia": "GARANTIA DO FUNDO GARANTIDOR DE CRÉDITOS (FGC.ORG.BR, NOV./2026)",
}

RODAPE = ("sintese", "pergunta", "legenda", "referencia")


def por_id(elementos):
    return {e.get("id"): e for e in elementos if e.get("id")}


class TesteMarcaDoBloco(unittest.TestCase):
    def test_marca_do_video_e_do_bloco_no_topo(self):
        avisos, _, elementos = renderizar(dict(DUAS_RODOVIAS, saida="r50-1_2_duas-rodovias.png"))
        self.assertEqual(avisos, [])
        marca = por_id(elementos)["marca"]
        self.assertEqual(marca["texto"], "R50-1 · 2/4")
        self.assertLess(marca["y"], 120)

    def test_sem_marca_quando_o_nome_foge_do_padrao(self):
        _, _, elementos = renderizar(DUAS_RODOVIAS)
        self.assertNotIn("marca", por_id(elementos))


class TesteRodape(unittest.TestCase):
    def test_rodape_em_ordem_e_abaixo_do_conteudo(self):
        avisos, _, elementos = renderizar(EXERCICIO_V5)
        self.assertEqual(avisos, [])
        ids = por_id(elementos)
        self.assertLess(ids["sintese"]["y"], ids["pergunta"]["y"])
        self.assertLess(ids["pergunta"]["y"], ids["referencia"]["y"])
        conteudo = [e["y"] for e in elementos if e.get("tipo") == "texto" and e.get("id") not in RODAPE]
        self.assertLess(max(conteudo), ids["sintese"]["y"])

    def test_rotulos_do_rodape(self):
        _, _, elementos = renderizar(EXERCICIO_V5)
        ids = por_id(elementos)
        self.assertIn("PAUSE E RESPONDA", ids["pergunta"]["texto"])
        self.assertIn("SÍNTESE:", ids["sintese"]["texto"])
        self.assertIn("FONTE", ids["referencia"]["texto"])
        self.assertIn("FGC.ORG.BR", ids["referencia"]["texto"])

    def test_legenda_de_cores_com_simbolos(self):
        _, _, elementos = renderizar(dict(MITO_COM_APOIO, legenda=True, referencia="X Y (Z)"))
        legenda = por_id(elementos)["legenda"]["texto"]
        self.assertIn("✓", legenda)
        self.assertIn("✗", legenda)

    def test_linha_longa_no_rodape_gera_aviso(self):
        avisos, _, _ = renderizar(dict(EXERCICIO_V5, pergunta="E SE X E Y FOSSEM DO MESMO CONGLOMERADO FINANCEIRO, "
                                                         "QUANTO DO DINHEIRO DO CLIENTE FICARIA FORA DA GARANTIA?"))
        self.assertTrue(any("rodapé" in a and "pergunta" in a for a in avisos), avisos)

    def test_exercicio_v5_cheio_e_sem_avisos(self):
        import conferir_lousas  # noqa: E402
        with tempfile.TemporaryDirectory() as tmp:
            png = os.path.join(tmp, "r58b_4_resolucao.png")
            avisos, _, _ = renderizar(EXERCICIO_V5, salvar=png)
            self.assertEqual(avisos, [])
            self.assertGreaterEqual(conferir_lousas.ocupacao(png), 0.70)
            self.assertLessEqual(conferir_lousas.faixa_vazia(png), 120)

    def test_premissas_logo_abaixo_dos_dados(self):
        _, _, elementos = renderizar(EXERCICIO_V5)
        ids = por_id(elementos)
        self.assertIn("PREMISSAS", ids["premissas"]["texto"])
        self.assertGreater(ids["premissas"]["y"], ids["dados"]["y"])
        self.assertLess(ids["premissas"]["y"], ids["ec1"]["y"])

    def test_lousa_sem_molde_tambem_ganha_rodape(self):
        spec = {"saida": "r58c_2_grafico.png", "referencia": "TEORIA DE CARTEIRAS DE MARKOWITZ (ARTIGO DE 1952)",
                "elementos": [{"tipo": "titulo", "texto": "GRÁFICO", "largura": 1000}]}
        _, _, elementos = renderizar(spec)
        self.assertIn("referencia", por_id(elementos))

    def test_comparacao_com_referencia_sem_avisos(self):
        avisos, _, _ = renderizar(dict(DUAS_RODOVIAS, saida="r50-1_2_duas-rodovias.png"))
        self.assertEqual(avisos, [])


if __name__ == "__main__":
    unittest.main()
