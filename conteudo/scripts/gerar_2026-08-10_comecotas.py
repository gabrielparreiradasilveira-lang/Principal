"""
Gera o carrossel de 10/08/2026 — Tradução de Jargão: Come-cotas.
Baseado no copy validado em conteudo/posts/2026-08-10/copy.md
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import (
    W, H, PRETO, VERDE_ESCURO, VERDE_CLARO, VERDE_BG, CINZA_ESCURO,
    font, F_BOLD, F_MED, F_REG, draw_text_wrapped, rounded_rect,
    content_slide_base, slide_capa, slide_cta,
)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "posts", "2026-08-10", "carrossel")
os.makedirs(OUT, exist_ok=True)

TOTAL = 10


def salvar(img, n):
    path = os.path.join(OUT, f"slide_{n:02d}.png")
    img.save(path, quality=95)
    print(f"slide_{n:02d} OK -> {path}")


def slide_conteudo(num, linhas, tag=None, tag_color=None):
    def content(img, draw):
        y = 420
        for linha in linhas:
            y = draw_text_wrapped(draw, linha, W // 2, y, font(F_BOLD, 54), PRETO, 880, "center", 1.3) + 20
        if tag:
            rounded_rect(draw, [W // 2 - 140, 140, W // 2 + 140, 200], 30, tag_color or VERDE_BG)
            draw.text((W // 2, 170), tag, font=font(F_MED, 26), fill=VERDE_ESCURO, anchor="mm")
    return content_slide_base(content, num, TOTAL)


def main():
    # Slide 1 — capa (template branco + blob verde, conforme identidade nova só pra capa)
    salvar(
        slide_capa(
            "Come-cotas não é\nimposto extra.",
            "É antecipação. Você já vai entender.",
        ),
        1,
    )

    slides_texto = [
        (2, ["Todo mês de maio e novembro,", "seu fundo \"perde\" cotas.", "Muita gente acha que é imposto a mais."], "PROBLEMA"),
        (3, ["Quem acha que é imposto a mais,", "sai do fundo assustado.", "E perde rendimento por decisão errada."], "CONSEQUÊNCIA"),
        (4, ["Come-cotas é o Leão cobrando", "uma parte do IR antes do resgate.", "Ele não cria imposto novo."], "MÉTODO 1/3"),
        (5, ["No resgate, você paga só a diferença", "entre a alíquota do come-cotas", "e a alíquota final da tabela regressiva."], "MÉTODO 2/3"),
        (6, ["O valor total de imposto", "é o mesmo com ou sem come-cotas.", "Muda só o quando você paga."], "MÉTODO 3/3"),
        (7, ["Quem entende isso não vende fundo", "no dia do come-cotas por pânico.", "Fica com a estratégia, não com o susto."], "RESULTADO"),
        (8, ["O problema nunca foi o come-cotas.", "Foi não saber o que ele é."], "GUINADA"),
        (9, ["Isso cai direto na prova.", "E na sua carteira, se você não souber."], "FECHAMENTO"),
    ]
    for num, linhas, tag in slides_texto:
        salvar(slide_conteudo(num, linhas, tag), num)

    # Slide 10 — CTA (gradiente verde escuro, padrão já documentado na skill)
    salvar(
        slide_cta(
            "Salva esse post.",
            "Quando bater o come-cotas de novembro,\nvocê vai lembrar por que não\nprecisa entrar em pânico.",
            10,
            TOTAL,
        ),
        10,
    )

    print(f"\nCarrossel completo gerado em: {OUT}")


if __name__ == "__main__":
    main()
