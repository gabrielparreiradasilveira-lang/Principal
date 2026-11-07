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


class TesteFaixaVazia(unittest.TestCase):
    def test_faixa_vazia_no_meio(self):
        img = Image.new("RGB", (1920, 1080), "black")
        d = ImageDraw.Draw(img)
        d.rectangle((80, 140, 900, 300), fill="white")
        d.rectangle((80, 700, 900, 1000), fill="white")
        with tempfile.TemporaryDirectory() as tmp:
            caminho = os.path.join(tmp, "x.png")
            img.save(caminho)
            self.assertTrue(395 <= C.faixa_vazia(caminho) <= 400, C.faixa_vazia(caminho))

    def test_traco_fino_conta_como_tinta(self):
        img = Image.new("RGB", (1920, 1080), "black")
        d = ImageDraw.Draw(img)
        d.rectangle((80, 140, 900, 300), fill="white")
        d.rectangle((945, 300, 946, 700), fill="white")  # linha vertical de 2 px no "buraco"
        d.rectangle((80, 700, 900, 1000), fill="white")
        with tempfile.TemporaryDirectory() as tmp:
            caminho = os.path.join(tmp, "x.png")
            img.save(caminho)
            self.assertLessEqual(C.faixa_vazia(caminho), 40)  # sobra só a margem de baixo (y 1001 a 1039)

    def test_faixa_vazia_ignora_cantos(self):
        img = Image.new("RGB", (1920, 1080), "black")
        d = ImageDraw.Draw(img)
        for y in range(130, 1040, 60):
            d.rectangle((80, y, 900, y + 30), fill="white")
        d.rectangle((1700, 800, 1900, 1000), fill="black")
        with tempfile.TemporaryDirectory() as tmp:
            caminho = os.path.join(tmp, "x.png")
            img.save(caminho)
            self.assertLessEqual(C.faixa_vazia(caminho), 40)


class TesteRepeticao(unittest.TestCase):
    def test_repeticao_com_marcacao(self):
        lousa = "PEDÁGIO SOBRE A {vermelho:CARGA INTEIRA} DO CAMINHÃO QUE SAI DA RODOVIA"
        fala = "o pedágio sobre a carga inteira do caminhão que sai da rodovia"
        self.assertEqual(len(C.repeticoes(lousa, fala)), 1)

    def test_repeticao_sem_acento(self):
        lousa = "PGBL SO VALE A PENA PARA QUEM FAZ A DECLARACAO COMPLETA"
        fala = "o PGBL só vale a pena para quem faz a declaração completa"
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

    def test_cli_lousa_que_cita_apostila_e_pendencia(self):
        roteiro = ("# R60A · Teste (7 min)\n\n## 2. Metáfora Central de Fixação — [1 min]\n"
                   "**[Ação na Lousa - Google Slides]**\n- Slide 2\n**[Locução Direta]**\n\"Fala sem relação.\"\n")
        lousas = {"padrao": {"fundo": "preto"}, "slides": [{"saida": "r60a_2_metafora.png", "elementos": [
            {"tipo": "titulo", "texto": "METÁFORA"},
            {"tipo": "texto", "x": 80, "y": 140, "largura": 1400, "tamanho": 34, "entrelinha": 1.5,
             "texto": "A APOSTILA DIZ OUTRA COISA\n" + "\n".join(["LINHA DE CONTEÚDO"] * 15)}]}]}
        with tempfile.TemporaryDirectory() as tmp:
            r, j = os.path.join(tmp, "r.md"), os.path.join(tmp, "l.json")
            open(r, "w", encoding="utf-8").write(roteiro)
            json.dump(lousas, open(j, "w", encoding="utf-8"), ensure_ascii=False)
            out = subprocess.run([sys.executable, "-I", SCRIPT, r, j, "-o", tmp], capture_output=True, text=True)
        self.assertEqual(out.returncode, 1, out.stdout + out.stderr)
        self.assertIn("apostila", out.stdout.lower())

    def test_cli_sem_fala_do_bloco_e_pendencia(self):
        roteiro = "# Outro roteiro sem cabeçalho de vídeo\n\nTexto qualquer.\n"
        lousas = {"padrao": {"fundo": "preto"}, "slides": [{"saida": "r60a_2_metafora.png", "elementos": [
            {"tipo": "titulo", "texto": "METÁFORA"},
            {"tipo": "texto", "x": 80, "y": 140, "largura": 1400, "tamanho": 34, "entrelinha": 1.5,
             "texto": "\n".join(["LINHA DE CONTEÚDO"] * 16)}]}]}
        with tempfile.TemporaryDirectory() as tmp:
            r, j = os.path.join(tmp, "r.md"), os.path.join(tmp, "l.json")
            open(r, "w", encoding="utf-8").write(roteiro)
            json.dump(lousas, open(j, "w", encoding="utf-8"), ensure_ascii=False)
            out = subprocess.run([sys.executable, "-I", SCRIPT, r, j, "-o", tmp], capture_output=True, text=True)
        self.assertEqual(out.returncode, 1, out.stdout + out.stderr)
        self.assertIn("não achei a fala", out.stdout)

    def test_lousa_dividida_aceita(self):
        self.assertEqual(C.video_bloco("r60a_3_conteudo-1.png"), ("r60a", 3))
        self.assertEqual(C.video_bloco("r60a_3_conteudo-2.png"), ("r60a", 3))


class TesteCorComRotulo(unittest.TestCase):
    def test_vermelho_sem_rotulo_reprova(self):
        self.assertEqual(len(C.cor_sem_rotulo("- ENTRADA: {vermelho:SEM VALE-PEDÁGIO}")), 1)

    def test_vermelho_com_xis_ou_palavra_passa(self):
        self.assertEqual(C.cor_sem_rotulo("- ✗ ENTRADA: {vermelho:SEM VALE-PEDÁGIO}"), [])
        self.assertEqual(C.cor_sem_rotulo("❌ {vermelho:SEM VALE}"), [])
        self.assertEqual(C.cor_sem_rotulo("{vermelho:RODOVIA ERRADA:} PGBL NA SIMPLIFICADA"), [])
        self.assertEqual(C.cor_sem_rotulo("⚠ {vermelho:ONDE QUEBRA:} BURACO SÓ ATRASA"), [])

    def test_verde_sem_rotulo_reprova_e_com_check_passa(self):
        self.assertEqual(len(C.cor_sem_rotulo("- SAÍDA: SÓ SOBRE O {verde:LUCRO}")), 1)
        self.assertEqual(C.cor_sem_rotulo("- ✓ SAÍDA: SÓ SOBRE O {verde:LUCRO}"), [])
        self.assertEqual(C.cor_sem_rotulo("{verde:REGRA:} O IR INCIDE SÓ SOBRE O RENDIMENTO"), [])

    def test_numero_com_sinal_dispensa_rotulo(self):
        self.assertEqual(C.cor_sem_rotulo("MARÇO {vermelho:−29,90%} · NOVEMBRO {verde:+15,90%}"), [])

    def test_sinal_sem_numero_nao_dispensa(self):
        self.assertEqual(len(C.cor_sem_rotulo("{verde:+ LUCRO} · {vermelho:- SEM VALE}")), 2)

    def test_laranja_nao_precisa_de_rotulo(self):
        self.assertEqual(C.cor_sem_rotulo("BASE {laranja:R$ 30.000}"), [])

    def test_conta_cada_linha(self):
        texto = "- ✓ {verde:CERTO}\n- {vermelho:SEM VALE}\n- {verde:LUCRO}"
        self.assertEqual(len(C.cor_sem_rotulo(texto)), 2)


class TesteTopicosCurtos(unittest.TestCase):
    def test_topico_de_13_palavras_reprova(self):
        t = "- VALE SÓ NA {laranja:DECLARAÇÃO COMPLETA} E, EM REGRA, COM INSS OU REGIME PRÓPRIO NO BRASIL"
        self.assertEqual(len(C.topicos_longos(t)), 1)

    def test_topico_de_12_palavras_passa(self):
        self.assertEqual(C.topicos_longos("- O MESMO ÍNDICE, NO MESMO ANO: O RESULTADO FINAL ESCONDE A VIAGEM"), [])

    def test_numerado_e_subtopico_contam(self):
        t = ("3. LIQUIDEZ → CASAR O PRAZO DO ATIVO COM O OBJETIVO · RESERVA EM ATIVO LÍQUIDO\n"
             "  - UM SUBTÓPICO COMPRIDO DEMAIS COM MUITAS PALAVRAS PARA UMA LINHA SÓ DA LOUSA")
        self.assertEqual(len(C.topicos_longos(t)), 2)

    def test_numero_nao_conta_como_palavra(self):
        t = "- RETORNOS DE 3 ANOS: A = 6 · 10 · 14 · B = 2 · 10 · 18 · C = 4 · 12 · 20"
        self.assertEqual(C.topicos_longos(t), [])

    def test_rs_nao_conta_como_palavra(self):
        t = "- DESCOBERTO NO BANCO X: R$ 400.000 − R$ 250.000 = R$ 150.000 VÃO PARA A LIQUIDAÇÃO"
        self.assertEqual(C.topicos_longos(t), [])

    def test_titulo_numerado_nao_e_topico(self):
        els = [{"tipo": "titulo", "texto": "2. UM TÍTULO NUMERADO COM MUITAS PALAVRAS QUE PASSA DO LIMITE DE DOZE"},
               {"tipo": "texto", "texto": "- TÓPICO CURTO"}]
        self.assertEqual(C.topicos_longos(C.texto_corpo(els)), [])

    def test_linha_sem_marcador_nao_e_topico(self):
        t = "{ciano:TARIFA DA SAÍDA, NAS DUAS:} REGRESSIVO 35% → 10% PELO TEMPO DE CADA APORTE · PROGRESSIVO"
        self.assertEqual(C.topicos_longos(t), [])


class TesteReferencia(unittest.TestCase):
    def test_referencia_com_descricao_e_identificador(self):
        self.assertTrue(C.referencia_ok("GARANTIA DO FUNDO GARANTIDOR DE CRÉDITOS (FGC.ORG.BR, NOV./2026)"))
        self.assertTrue(C.referencia_ok("LEI DO IR DA PREVIDÊNCIA (LEI 11.053/2004)"))

    def test_referencia_so_com_codigo_reprova(self):
        self.assertFalse(C.referencia_ok("IN RFB 1.585/2015 (ART. 46)"))
        self.assertFalse(C.referencia_ok("LEI 11.053/2004"))
        self.assertFalse(C.referencia_ok("(LEI 11.053/2004)"))
        self.assertFalse(C.referencia_ok("LEI (11.053/2004)"))
        self.assertFalse(C.referencia_ok(""))


def lousa(saida, **campos):
    return dict({"saida": saida, "molde": "topicos", "referencia": "PROGRAMA DA PROVA C-PRO R (ITEM 4.5)"}, **campos)


def exercicio(saida, **campos):
    base = {"saida": saida, "molde": "exercicio", "referencia": "PROGRAMA DA PROVA C-PRO R (ITEM 4.5)",
            "premissas": "VALORES HIPOTÉTICOS", "conclusao": "REGRA: LIMITE POR CONGLOMERADO → DIVIDIR REDUZ O RISCO",
            "pergunta": "QUANTO FICA DESCOBERTO?"}
    return dict(base, **campos)


class TesteRegrasDaAula(unittest.TestCase):
    def aula(self):
        return [lousa("r60a_1_abertura.png", legenda=True), exercicio("r60a_4_resolucao.png"),
                lousa("r60b_1_abertura.png"), exercicio("r60b_4_resolucao.png", sintese="A → B")]

    def test_aula_completa_sem_pendencias(self):
        pend, _ = C.regras_da_aula(self.aula())
        self.assertEqual(pend, [])

    def test_primeira_lousa_sem_legenda(self):
        aula = self.aula()
        aula[0] = lousa("r60a_1_abertura.png")
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("legenda" in p for p in pend), pend)

    def test_bloco_4_sem_pergunta(self):
        aula = self.aula()
        aula[1] = exercicio("r60a_4_resolucao.png", pergunta="")
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("r60a_4" in p and "pergunta" in p for p in pend), pend)

    def test_pergunta_sem_interrogacao(self):
        aula = self.aula()
        aula[1] = exercicio("r60a_4_resolucao.png", pergunta="RESPONDA QUANTO FICA DESCOBERTO")
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("?" in p for p in pend), pend)

    def test_ultimo_video_sem_sintese(self):
        aula = self.aula()
        aula[3] = exercicio("r60b_4_resolucao.png")
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("síntese" in p for p in pend), pend)

    def test_sintese_so_e_exigida_no_ultimo_video(self):
        pend, _ = C.regras_da_aula(self.aula())
        self.assertFalse(any("r60a" in p and "síntese" in p for p in pend), pend)

    def test_exercicio_sem_premissas(self):
        aula = self.aula()
        aula[1] = exercicio("r60a_4_resolucao.png", premissas="")
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("premissas" in p for p in pend), pend)

    def test_conclusao_sem_mecanismo(self):
        aula = self.aula()
        aula[1] = exercicio("r60a_4_resolucao.png", conclusao={"texto": "B É MELHOR", "cor": "branco"})
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("regra" in p and "efeito" in p for p in pend), pend)

    def test_conclusao_com_porque_passa(self):
        aula = self.aula()
        aula[1] = exercicio("r60a_4_resolucao.png", conclusao="✓ B PAGA MENOS PORQUE A BASE É SÓ O RENDIMENTO")
        pend, _ = C.regras_da_aula(aula)
        self.assertEqual(pend, [])

    def test_lousa_sem_referencia_e_pendencia(self):
        aula = self.aula()
        del aula[2]["referencia"]
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("r60b_1" in p and "referência" in p for p in pend), pend)

    def test_referencia_false_vira_aviso(self):
        aula = self.aula()
        aula[2]["referencia"] = False
        pend, avis = C.regras_da_aula(aula)
        self.assertEqual(pend, [])
        self.assertTrue(any("r60b_1" in a for a in avis), avis)

    def test_referencia_true_e_pendencia_sem_quebrar(self):
        aula = self.aula()
        aula[2]["referencia"] = True
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("r60b_1" in p and "referência" in p for p in pend), pend)

    def test_resultado_vermelho_sem_xis_e_pendencia(self):
        aula = self.aula()
        aula[1] = exercicio("r60a_4_resolucao.png", cenarios=[
            {"titulo": "A", "passos": "- X", "resultado": "37,5% FORA DO FGC", "cor": "vermelho"},
            {"titulo": "B", "passos": "- Y", "resultado": "✓ 100% COBERTO", "cor": "verde"}])
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("r60a_4" in p and "cor sem rótulo" in p for p in pend), pend)

    def test_resultado_com_rotulo_e_resultado_padrao_passam(self):
        aula = self.aula()
        aula[1] = exercicio("r60a_4_resolucao.png", cenarios=[
            {"titulo": "A", "passos": "- X", "resultado": "✗ 37,5% FORA DO FGC", "cor": "vermelho"},
            {"titulo": "B", "passos": "- Y", "resultado": "100% COBERTO"}])
        pend, _ = C.regras_da_aula(aula)
        self.assertEqual(pend, [])

    def test_destaque_verde_padrao_sem_rotulo_e_pendencia(self):
        aula = self.aula()
        aula[2] = lousa("r60b_1_abertura.png", destaque="DIVIDIR ENTRE BANCOS TIRA O EXCESSO DO RISCO")
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("r60b_1" in p and "cor sem rótulo" in p for p in pend), pend)

    def test_destaque_branco_nao_precisa_de_rotulo(self):
        aula = self.aula()
        aula[2] = lousa("r60b_1_abertura.png", destaque={"texto": "DIVIDIR TIRA O EXCESSO", "cor": "branco"})
        pend, _ = C.regras_da_aula(aula)
        self.assertEqual(pend, [])

    def test_referencia_mal_escrita_e_pendencia(self):
        aula = self.aula()
        aula[2]["referencia"] = ["LEI 11.053/2004"]
        pend, _ = C.regras_da_aula(aula)
        self.assertTrue(any("r60b_1" in p and "referência" in p for p in pend), pend)


class TesteAbsolutas(unittest.TestCase):
    def test_lista_frase_absoluta_da_lousa(self):
        self.assertEqual(len(C.absolutas("- LCI É ISENTA DE IR\n- O RISCO CAI COM PRAZO")), 1)


class TesteCLIRegrasNovas(unittest.TestCase):
    ROTEIRO = ("# R60A · Teste (7 min)\n\n## 4. Resolução Rápida de Fixação — [1,3 min]\n"
               "**[Ação na Lousa - Google Slides]**\n- Slide 4\n**[Locução Direta]**\n\"Fala sem relação.\"\n")

    def rodar(self, spec):
        with tempfile.TemporaryDirectory() as tmp:
            r, j = os.path.join(tmp, "r.md"), os.path.join(tmp, "l.json")
            open(r, "w", encoding="utf-8").write(self.ROTEIRO)
            json.dump({"padrao": {"fundo": "preto"}, "slides": [spec]}, open(j, "w", encoding="utf-8"),
                      ensure_ascii=False)
            return subprocess.run([sys.executable, "-I", SCRIPT, r, j, "-o", tmp], capture_output=True, text=True)

    def test_exercicio_completo_passa(self):
        import test_moldes
        spec = dict(test_moldes.EXERCICIO_V5, saida="r60a_4_resolucao.png", legenda=True)
        out = self.rodar(spec)
        self.assertEqual(out.returncode, 0, out.stdout + out.stderr)
        self.assertNotIn("GARANTIDOR", out.stdout)  # a linha da fonte não é afirmação

    def test_exercicio_sem_pergunta_reprova(self):
        import test_moldes
        spec = dict(test_moldes.EXERCICIO_V5, saida="r60a_4_resolucao.png", legenda=True)
        del spec["pergunta"]
        out = self.rodar(spec)
        self.assertEqual(out.returncode, 1, out.stdout + out.stderr)
        self.assertIn("pergunta", out.stdout)

    def test_cor_sem_rotulo_reprova_na_cli(self):
        import test_moldes
        spec = dict(test_moldes.EXERCICIO_V5, saida="r60a_4_resolucao.png", legenda=True,
                    conclusao={"texto": "{vermelho:B PERDE} PORQUE O LIMITE VALE POR CONGLOMERADO",
                               "cor": "branco", "moldura": "amarelo"})
        out = self.rodar(spec)
        self.assertEqual(out.returncode, 1, out.stdout + out.stderr)
        self.assertIn("cor sem rótulo", out.stdout)


if __name__ == "__main__":
    unittest.main()
