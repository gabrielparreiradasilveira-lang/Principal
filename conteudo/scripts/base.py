"""
Módulo compartilhado de desenho para os carrosséis @gparreiraaa.
Adaptado da skill `instagram-carrossel-financas` para rodar a partir deste repo
(sem depender de /home/claude ou /home/ubuntu).
"""
import os
from PIL import Image, ImageDraw, ImageFont

# ── Configurações globais ────────────────────────────────────────────────
W, H = 1080, 1350
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(SCRIPT_DIR, "fonts")

# Paleta de cores oficial (identidade visual @gparreiraaa)
VERDE_ESCURO = (27, 94, 32)
VERDE_MEDIO = (46, 125, 50)
VERDE_CLARO = (76, 175, 80)
VERDE_MENTA = (105, 240, 174)
VERDE_BG = (232, 245, 233)
BRANCO = (255, 255, 255)
PRETO = (33, 33, 33)
CINZA_ESCURO = (97, 97, 97)
CINZA_MEDIO = (158, 158, 158)
CINZA_CLARO = (245, 245, 240)
VERMELHO = (229, 57, 53)
LARANJA = (255, 143, 0)

# Cores específicas do template de capa (fundo branco + blob verde + pontos)
CAPA_BLOB = (76, 175, 80)
CAPA_DOT = (144, 164, 190)

HANDLE = "@gparreiraaa"

F_BLACK = os.path.join(FONT_DIR, "Poppins-Black.ttf")
F_BOLD = os.path.join(FONT_DIR, "Poppins-Bold.ttf")
F_MED = os.path.join(FONT_DIR, "Poppins-Medium.ttf")
F_REG = os.path.join(FONT_DIR, "Poppins-Regular.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


# ── Utilitários de texto ─────────────────────────────────────────────────
def wrap_text(text, font_obj, max_width, draw):
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = (current + " " + word).strip()
        bbox = draw.textbbox((0, 0), test, font=font_obj)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_text_wrapped(draw, text, x, y, font_obj, color, max_width, align="left", line_spacing=1.3):
    lines = wrap_text(text, font_obj, max_width, draw)
    cy = y
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font_obj)
        lw, lh = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if align == "center":
            draw.text((x - lw // 2, cy), line, font=font_obj, fill=color)
        else:
            draw.text((x, cy), line, font=font_obj, fill=color)
        cy += int(lh * line_spacing)
    return cy


def rounded_rect(draw, xy, radius, fill, outline=None, outline_width=0):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=outline_width)


def gradient_bg(img, color_top, color_bottom):
    draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        r = int(color_top[0] + (color_bottom[0] - color_top[0]) * t)
        g = int(color_top[1] + (color_bottom[1] - color_top[1]) * t)
        b = int(color_top[2] + (color_bottom[2] - color_top[2]) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))


# ── Elementos estruturais (slides de conteúdo) ──────────────────────────
def add_top_bar(draw):
    for x in range(W):
        t = x / W
        r = int(VERDE_ESCURO[0] + (VERDE_CLARO[0] - VERDE_ESCURO[0]) * t)
        g = int(VERDE_ESCURO[1] + (VERDE_CLARO[1] - VERDE_ESCURO[1]) * t)
        b = int(VERDE_ESCURO[2] + (VERDE_CLARO[2] - VERDE_ESCURO[2]) * t)
        draw.line([(x, 0), (x, 14)], fill=(r, g, b))


def add_handle(draw, color=CINZA_MEDIO):
    draw.text((W - 60, H - 60), HANDLE, font=font(F_REG, 28), fill=color, anchor="rs")


def add_slide_num(draw, num, total):
    draw.text((60, 40), f"{num} / {total}", font=font(F_BOLD, 30), fill=VERDE_CLARO)


def add_progress_dots(draw, active, total):
    dot_w, dot_h, gap = 12, 12, 18
    sx = 60
    y = H - 80
    for i in range(total):
        if i + 1 == active:
            rounded_rect(draw, [sx, y, sx + 36, y + dot_h], 6, VERDE_CLARO)
            sx += 36 + gap
        else:
            draw.ellipse([sx, y, sx + dot_w, y + dot_h], fill=(200, 200, 200))
            sx += dot_w + gap


def content_slide_base(draw_content, num, total):
    """Slide padrão de conteúdo: fundo cinza claro + barra + numeração + dots."""
    img = Image.new("RGB", (W, H), CINZA_CLARO)
    draw = ImageDraw.Draw(img)
    add_top_bar(draw)
    add_handle(draw)
    add_slide_num(draw, num, total)
    add_progress_dots(draw, num, total)
    draw_content(img, draw)
    return img


# ── Template de capa (fundo branco + blob verde + borda pontilhada) ────
# Aproximação do template de referência enviado pelo Gabriel: fundo branco,
# fileiras de círculos pontilhados no topo/rodapé e um "glow" verde radial
# centralizado atrás do título. Reprodução aproximada por camadas de
# elipses translúcidas — não é o asset original pixel a pixel.
def _draw_dot_rows(draw, y_positions, color=CAPA_DOT):
    spacing = 34
    radius = 4
    for y in y_positions:
        x = 20
        while x < W - 20:
            draw.ellipse([x - radius, y - radius, x + radius, y + radius], outline=color, width=2)
            x += spacing


def _radial_blob(img, center, max_radius, color, layers=36, max_alpha=70):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    cx, cy = center
    for i in range(layers, 0, -1):
        r = int(max_radius * i / layers)
        alpha = int(max_alpha * (1 - i / layers) ** 2)
        odraw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, alpha))
    img.paste(Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB"), (0, 0))


def slide_capa(titulo, subtitulo, num=1, total=1):
    img = Image.new("RGB", (W, H), BRANCO)
    _radial_blob(img, (W // 2, H // 2), 380, CAPA_BLOB, layers=40, max_alpha=90)
    draw = ImageDraw.Draw(img)

    _draw_dot_rows(draw, [30, 62])
    _draw_dot_rows(draw, [H - 62, H - 30])

    # Centraliza o bloco título+subtítulo dinamicamente conforme o nº de linhas,
    # para não sobrepor quando o título tem 3 linhas em vez de 2.
    titulo_font = font(F_BLACK, 72)
    subtitulo_font = font(F_MED, 34)
    titulo_lines = wrap_text(titulo, titulo_font, 860, draw)
    titulo_line_h = int((draw.textbbox((0, 0), "Ág", font=titulo_font)[3]) * 1.2)
    titulo_h = titulo_line_h * len(titulo_lines)
    subtitulo_lines = wrap_text(subtitulo, subtitulo_font, 780, draw)
    subtitulo_line_h = int((draw.textbbox((0, 0), "Ág", font=subtitulo_font)[3]) * 1.3)
    subtitulo_h = subtitulo_line_h * len(subtitulo_lines)

    gap = 30
    start_y = H // 2 - (titulo_h + gap + subtitulo_h) // 2

    end_y = draw_text_wrapped(draw, titulo, W // 2, start_y, titulo_font, PRETO, 860, "center", 1.2)
    draw_text_wrapped(draw, subtitulo, W // 2, end_y + gap, subtitulo_font, CINZA_ESCURO, 780, "center", 1.3)
    draw.text((W // 2, H - 100), "› Deslize para aprender ›", font=font(F_REG, 26), fill=CINZA_MEDIO, anchor="mm")
    draw.text((W - 40, H - 40), HANDLE, font=font(F_REG, 26), fill=CINZA_ESCURO, anchor="rs")

    return img


def slide_cta(titulo, cta_texto, num, total):
    img = Image.new("RGB", (W, H))
    gradient_bg(img, (10, 46, 10), (46, 125, 50))
    draw = ImageDraw.Draw(img)
    add_slide_num(draw, num, total)
    add_progress_dots(draw, num, total)

    draw_text_wrapped(draw, titulo, W // 2, H // 2 - 120, font(F_BLACK, 60), BRANCO, 860, "center", 1.25)
    draw_text_wrapped(draw, cta_texto, W // 2, H // 2 + 40, font(F_MED, 34), (230, 245, 230), 780, "center", 1.3)
    draw.text((W // 2, H - 100), "Salva esse post ›", font=font(F_BOLD, 32), fill=VERDE_MENTA, anchor="mm")
    draw.text((W - 40, H - 40), HANDLE, font=font(F_REG, 26), fill=(255, 255, 255, 180), anchor="rs")

    return img


# ── Story (formato vertical 1080x1920, distinto do carrossel 1080x1350) ──
SW, SH = 1080, 1920


def slide_story(tag, titulo, corpo, rodape=None):
    img = Image.new("RGB", (SW, SH), CINZA_CLARO)
    draw = ImageDraw.Draw(img)

    # Barra de progresso superior (padrão único de story, sem numeração/dots)
    for x in range(SW):
        t = x / SW
        r = int(VERDE_ESCURO[0] + (VERDE_CLARO[0] - VERDE_ESCURO[0]) * t)
        g = int(VERDE_ESCURO[1] + (VERDE_CLARO[1] - VERDE_ESCURO[1]) * t)
        b = int(VERDE_ESCURO[2] + (VERDE_CLARO[2] - VERDE_ESCURO[2]) * t)
        draw.line([(x, 0), (x, 14)], fill=(r, g, b))

    rounded_rect(draw, [SW // 2 - 170, 160, SW // 2 + 170, 216], 28, VERDE_BG)
    draw.text((SW // 2, 188), tag, font=font(F_MED, 26), fill=VERDE_ESCURO, anchor="mm")

    y = draw_text_wrapped(draw, titulo, SW // 2, 420, font(F_BLACK, 62), VERDE_ESCURO, 880, "center", 1.25)
    draw_text_wrapped(draw, corpo, SW // 2, y + 50, font(F_MED, 36), CINZA_ESCURO, 820, "center", 1.35)

    if rodape:
        draw.text((SW // 2, SH - 220), rodape, font=font(F_BOLD, 30), fill=VERDE_ESCURO, anchor="mm")

    draw.text((SW - 50, SH - 60), HANDLE, font=font(F_REG, 28), fill=CINZA_MEDIO, anchor="rs")
    return img


# ── Imagem estática (post avulso 1080x1350, sem numeração/dots de carrossel) ──
def slide_static(tag, titulo, corpo):
    img = Image.new("RGB", (W, H), CINZA_CLARO)
    draw = ImageDraw.Draw(img)
    add_top_bar(draw)

    rounded_rect(draw, [W // 2 - 150, 130, W // 2 + 150, 186], 26, VERDE_BG)
    draw.text((W // 2, 158), tag, font=font(F_MED, 24), fill=VERDE_ESCURO, anchor="mm")

    y = draw_text_wrapped(draw, titulo, W // 2, 340, font(F_BLACK, 56), VERDE_ESCURO, 880, "center", 1.25)
    draw_text_wrapped(draw, corpo, W // 2, y + 50, font(F_MED, 34), CINZA_ESCURO, 840, "center", 1.35)

    add_handle(draw)
    return img
