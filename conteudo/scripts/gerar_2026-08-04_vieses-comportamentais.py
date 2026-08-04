"""
Gera o carrossel avulso de 04/08/2026 — Psicologia e Finanças: Aversão à Perda e Efeito Manada.
Baseado no copy validado em conteudo/posts/2026-08-04/copy.md
Peça avulsa, sem vínculo com o calendário editorial.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import (
    W, PRETO, VERDE_ESCURO, VERDE_BG,
    font, F_BOLD, F_MED, draw_text_wrapped, rounded_rect,
    content_slide_base, slide_capa, slide_cta,
)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "posts", "2026-08-04", "carrossel")
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
            rounded_rect(draw, [W // 2 - 210, 140, W // 2 + 210, 200], 30, VERDE_BG)
            draw.text((W // 2, 170), tag, font=font(F_MED, 22), fill=VERDE_ESCURO, anchor="mm")
    return content_slide_base(content, num, TOTAL)


def main():
    salvar(
        slide_capa(
            "Perder dinheiro ativa\no mesmo alarme de perigo\nque uma ameaça real.",
            "Por que suas piores decisões de investimento não são falta de disciplina.",
        ),
        1,
    )

    slides_texto = [
        (2, ["Você segura a ação perdendo,", "vende a que tá subindo cedo demais,", "e jura que foi \"estratégia\"."], "PROBLEMA"),
        (3, ["Não foi estratégia.", "Foi o alarme de perigo", "disparando no seu cérebro."], "CONSEQUÊNCIA"),
        (4, ["Perder dinheiro dói bem mais", "do que ganhar o mesmo valor", "dá satisfação. É assimetria, não fraqueza."], "AVERSÃO À PERDA"),
        (5, ["Quando todo mundo corre pra vender,", "seu cérebro lê isso como", "\"tem perigo real aqui\"."], "EFEITO MANADA"),
        (6, ["Numa queda, o medo de perder", "mais se soma ao pânico da manada.", "Todo mundo vende ao mesmo tempo."], "OS DOIS JUNTOS"),
        (7, ["Quem reconhece o alarme", "consegue pausar antes de reagir.", "Segue o plano, não o pânico."], "RESULTADO"),
        (8, ["Não é falta de disciplina.", "É biologia. O alarme", "sempre vai disparar."], "GUINADA"),
        (9, ["A pergunta não é como", "desligar o alarme.", "É o que você faz quando ele toca."], "FECHAMENTO"),
    ]
    for num, linhas, tag in slides_texto:
        salvar(slide_conteudo(num, linhas, tag), num)

    salvar(
        slide_cta(
            "Comenta aqui.",
            "Você já vendeu no pânico\ne se arrependeu depois?\nQuero ler sua experiência.",
            10,
            TOTAL,
        ),
        10,
    )

    print(f"\nCarrossel completo gerado em: {OUT}")


if __name__ == "__main__":
    main()
