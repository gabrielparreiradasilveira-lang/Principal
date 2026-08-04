"""
Gera o carrossel de 14/08/2026 — Comparativo C-Pro R x C-Pro I.
Baseado no copy validado em conteudo/posts/2026-08-14/copy.md
Reescrito em 04/08 — nomenclatura ANBIMA vigente desde jan/2026 (CPA-10/CPA-20/CEA descontinuadas).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import (
    W, PRETO, VERDE_ESCURO, VERDE_BG,
    font, F_BOLD, F_MED, draw_text_wrapped, rounded_rect,
    content_slide_base, slide_capa, slide_cta,
)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "posts", "2026-08-14", "carrossel")
os.makedirs(OUT, exist_ok=True)

TOTAL = 10


def salvar(img, n):
    path = os.path.join(OUT, f"slide_{n:02d}.png")
    img.save(path, quality=95)
    print(f"slide_{n:02d} OK -> {path}")


def slide_conteudo(num, linhas, tag=None):
    def content(img, draw):
        y = 420
        for linha in linhas:
            y = draw_text_wrapped(draw, linha, W // 2, y, font(F_BOLD, 50), PRETO, 880, "center", 1.3) + 20
        if tag:
            rounded_rect(draw, [W // 2 - 170, 140, W // 2 + 170, 200], 30, VERDE_BG)
            draw.text((W // 2, 170), tag, font=font(F_MED, 24), fill=VERDE_ESCURO, anchor="mm")
    return content_slide_base(content, num, TOTAL)


def main():
    salvar(
        slide_capa(
            "C-Pro R ou C-Pro I:\nescolher errado trava\nsua especialização.",
            "Comparativo pra você decidir com base certa.",
        ),
        1,
    )

    slides_texto = [
        (2, ["Depois da CPA, todo mundo trava", "na escolha entre as duas C-Pro.", "Escolhe pelo nome, não pelo que faz."], "PROBLEMA"),
        (3, ["Vira especialista errado", "pro público errado.", "Tempo de estudo jogado fora."], "CONSEQUÊNCIA"),
        (4, ["Foco em relacionamento com o cliente", "e recomendação de carteira.", "Pré-requisito: ter a CPA."], "O QUE É C-PRO R"),
        (5, ["Foco em produtos complexos,", "gestão de risco, investimentos", "alternativos. Também exige a CPA."], "O QUE É C-PRO I"),
        (6, ["C-Pro R: quem quer atender e", "recomendar carteira pro cliente.", "C-Pro I: quem quer ser especialista", "técnico em produto."], "PRA QUEM SERVE"),
        (7, ["Quem escolhe pelo cargo que quer,", "não pelo \"nome mais completo\",", "estuda menos e erra menos."], "RESULTADO"),
        (8, ["A pergunta não é qual é mais completa.", "É qual combina com o que você", "quer fazer no dia a dia."], "GUINADA"),
        (9, ["Ainda em dúvida entre as duas?", "Isso trava especialização, não só prova."], "FECHAMENTO"),
    ]
    for num, linhas, tag in slides_texto:
        salvar(slide_conteudo(num, linhas, tag), num)

    salvar(
        slide_cta(
            "Manda mensagem.",
            "Conta seu objetivo de carreira.\nTe ajudo a decidir qual\nfaz sentido pra você.",
            10,
            TOTAL,
        ),
        10,
    )

    print(f"\nCarrossel completo gerado em: {OUT}")


if __name__ == "__main__":
    main()
