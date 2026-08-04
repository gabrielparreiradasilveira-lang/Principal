"""
Gera o story de 13/08/2026 — Economia no Dia a Dia: Selic e reserva de emergência.
Baseado no copy validado em conteudo/posts/2026-08-13/copy.md
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import slide_story

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "posts", "2026-08-13", "story")
os.makedirs(OUT, exist_ok=True)


def main():
    img = slide_story(
        "ECONOMIA DA SEMANA",
        "Selic subiu.\nIsso muda sua\nreserva de emergência.",
        "Reserva rende atrelada ao CDI. CDI segue a Selic de perto. Selic mais alta = reserva rendendo mais, sem você mexer em nada.",
        rodape="Manda uma reação se você já sabia disso",
    )
    path = os.path.join(OUT, "story_01.png")
    img.save(path, quality=95)
    print(f"story_01 OK -> {path}")


if __name__ == "__main__":
    main()
