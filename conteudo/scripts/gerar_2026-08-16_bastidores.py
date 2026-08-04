"""
Gera a imagem estática de 16/08/2026 — Bastidores da Carreira de Gestor.
Baseado no copy validado em conteudo/posts/2026-08-16/copy.md
Ângulo institucional/geral — não usa o Gabriel como case pessoal (correção dele).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import slide_static

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "posts", "2026-08-16", "imagem")
os.makedirs(OUT, exist_ok=True)


def main():
    img = slide_static(
        "BASTIDORES",
        "O que ninguém te conta\nsobre ser gestor de fundos",
        "Não é só escolher onde investir. É comitê de investimentos, compliance verificando cada decisão, relatório pra cotista, e uma trilha de responsabilidade que não some se o fundo for bem ou mal.",
    )
    path = os.path.join(OUT, "imagem_01.png")
    img.save(path, quality=95)
    print(f"imagem_01 OK -> {path}")


if __name__ == "__main__":
    main()
