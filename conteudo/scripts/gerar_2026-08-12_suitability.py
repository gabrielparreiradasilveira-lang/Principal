"""
Gera o carrossel de 12/08/2026 — Questão Comentada: Suitability.
Baseado no copy validado em conteudo/posts/2026-08-12/copy.md
ATENÇÃO: conteúdo pendente de revisão técnica do Gabriel antes de publicar.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import (
    W, PRETO, VERDE_ESCURO, VERDE_BG,
    font, F_BOLD, F_MED, draw_text_wrapped, rounded_rect,
    content_slide_base, slide_capa, slide_cta,
)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "posts", "2026-08-12", "carrossel")
os.makedirs(OUT, exist_ok=True)

TOTAL = 10


def salvar(img, n):
    path = os.path.join(OUT, f"slide_{n:02d}.png")
    img.save(path, quality=95)
    print(f"slide_{n:02d} OK -> {path}")


def slide_conteudo(num, linhas, tag=None, font_size=48, align="center"):
    def content(img, draw):
        x = 100 if align == "left" else W // 2
        max_width = 880 if align == "left" else 900
        y = 400
        for linha in linhas:
            y = draw_text_wrapped(draw, linha, x, y, font(F_BOLD, font_size), PRETO, max_width, align, 1.3) + 18
        if tag:
            rounded_rect(draw, [W // 2 - 160, 140, W // 2 + 160, 200], 30, VERDE_BG)
            draw.text((W // 2, 170), tag, font=font(F_MED, 24), fill=VERDE_ESCURO, anchor="mm")
    return content_slide_base(content, num, TOTAL)


def main():
    salvar(
        slide_capa(
            "Essa questão\nreprovou 6 em cada 10\nno simulado.",
            "Suitability. Você marcaria qual alternativa?",
        ),
        1,
    )

    salvar(
        slide_conteudo(
            2,
            ["Cliente varejo se recusa a", "atualizar o suitability.", "O distribuidor deve fazer o quê?"],
            "ENUNCIADO",
        ),
        2,
    )

    salvar(
        slide_conteudo(
            3,
            ["A. Bloquear tudo", "B. Só por iniciativa do cliente,", "com alerta", "C. Perfil conservador automático", "D. Dispensar suitability"],
            "ALTERNATIVAS",
            font_size=40,
            align="left",
        ),
        3,
    )

    salvar(
        slide_conteudo(
            4,
            ["Pensa antes de continuar.", "Escolhe sua alternativa."],
            "ANTES DE VER A RESPOSTA",
        ),
        4,
    )

    salvar(
        slide_conteudo(
            5,
            ["O cliente pode operar", "por conta própria.", "Mas só com alerta claro", "da falta de verificação."],
            "GABARITO: B",
        ),
        5,
    )

    salvar(
        slide_conteudo(
            6,
            ["Bloquear tudo vai longe demais.", "O direito de operar por", "conta própria continua."],
            "POR QUE A ESTÁ ERRADA",
        ),
        6,
    )

    salvar(
        slide_conteudo(
            7,
            ["Não existe \"perfil automático\"", "por omissão.", "Sem dado, não tem", "recomendação — de nenhum tipo."],
            "POR QUE C ESTÁ ERRADA",
        ),
        7,
    )

    salvar(
        slide_conteudo(
            8,
            ["Recusar preencher", "não é virar qualificado.", "Qualificado tem", "critério objetivo próprio."],
            "POR QUE D ESTÁ ERRADA",
        ),
        8,
    )

    salvar(
        slide_conteudo(
            9,
            ["Suitability não existe", "pra travar o cliente.", "Existe pra travar a", "recomendação sem base."],
            "REGRA GERAL",
        ),
        9,
    )

    salvar(
        slide_cta(
            "Salva esse post.",
            "Suitability cai em praticamente\ntoda prova ANBIMA\n(CPA, C-Pro R, C-Pro I).",
            10,
            TOTAL,
        ),
        10,
    )

    print(f"\nCarrossel completo gerado em: {OUT}")
    print("LEMBRETE: conteúdo pendente de revisão técnica antes de publicar.")


if __name__ == "__main__":
    main()
