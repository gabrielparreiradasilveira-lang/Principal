"""
Gera o carrossel de 14/08/2026 — Comparativo CPA-10 x CPA-20.
Baseado no copy validado em conteudo/posts/2026-08-14/copy.md
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
            "CPA-10 ou CPA-20:\numa te deixa\nestagnado.",
            "Comparativo pra você decidir com base certa.",
        ),
        1,
    )

    slides_texto = [
        (2, ["Muita gente escolhe pelo nome.", "\"CPA-20 parece mais completa.\"", "Escolhe sem saber pra que serve."], "PROBLEMA"),
        (3, ["Escolha errada = prova mais difícil", "pra um mercado que você", "nem quer atuar."], "CONSEQUÊNCIA"),
        (4, ["Foco em produtos simples de varejo.", "Fundos abertos, renda fixa,", "previdência básica."], "O QUE É CPA-10"),
        (5, ["Escopo mais amplo: private,", "produtos estruturados,", "mercado de capitais."], "O QUE É CPA-20"),
        (6, ["CPA-10: quem vai atender", "varejo simples.", "CPA-20: quem mira private,", "gerência, produtos complexos."], "PRA QUEM SERVE"),
        (7, ["Quem escolhe pelo cargo que quer,", "não pelo \"nome mais bonito\",", "estuda menos e erra menos."], "RESULTADO"),
        (8, ["A pergunta não é qual é mais difícil.", "É qual abre a porta que você quer."], "GUINADA"),
        (9, ["Ainda em dúvida entre as duas?", "Isso trava carreira, não só prova."], "FECHAMENTO"),
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
