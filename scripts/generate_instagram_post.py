"""Gera as imagens do post do Instagram (1080x1350, proporção 4:5) a partir das fotos da montagem.

Uso (na raiz do repositório):
    pip install -r requirements.txt
    python scripts/generate_instagram_post.py [pasta_de_saida]

Entrada: fotos em media/photos/.
Saída padrão: media/instagram/
  - sofle-v2-post.png    post principal: foto do teclado pronto e as etapas da montagem
  - sofle-v2-before.png  "Antes": o início da montagem
  - sofle-v2-after.png   "Depois": o teclado pronto

A fonte é a Bahnschrift (vem com o Windows). Em outro sistema, o script cai para uma fonte
comum do sistema (DejaVu/Arial); ajuste FONT_CANDIDATES se o resultado ficar diferente.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PHOTOS = os.path.join(ROOT, "media", "photos")
OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "media", "instagram")

W, H = 1080, 1350
MARGIN = 60

# Post principal
HERO = "07-finished-keyboard.jpg"
PHOTO_H = 950             # altura da área da foto de destaque
HERO_CROP_Y = 190         # topo do recorte, em pixels da foto já escalada para a largura W
# (arquivo, rótulo) das miniaturas, na ordem da montagem
STAGES = [
    ("03-hotswap-sockets-mounted.jpg", "Sockets"),
    ("04-continuity-test.jpg", "Teste"),
    ("05-mcu-oled-encoders-mounted.jpg", "MCU e OLED"),
    ("06-switches-in-printed-case.jpg", "Switches"),
]
SPECS = "58 teclas   •   QMK   •   ABNT2   •   case impresso em 3D"

# Antes e Depois: (arquivo de saída, foto, título, cor do título, legenda, foco vertical do recorte)
BEFORE = ("sofle-v2-before.png", "02-diodes-done-sockets-loose.jpg", "ANTES", None,
          "PCBs, diodos e sockets", 0.5)
AFTER = ("sofle-v2-after.png", "07-finished-keyboard.jpg", "DEPOIS", None,
         "Sofle v2 pronto", 0.4)

BG = (14, 16, 26)
ORANGE = (255, 154, 46)   # a cor da legenda dos keycaps
WHITE = (245, 245, 247)

FONT_CANDIDATES = [
    "C:/Windows/Fonts/bahnschrift.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]


def font(size, variation=None):
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            f = ImageFont.truetype(path, size)
            if variation:
                try:
                    f.set_variation_by_name(variation)
                except (OSError, AttributeError):
                    pass  # fonte sem eixos variáveis
            return f
    return ImageFont.load_default()


def gradient(width, height, top_alpha, bottom_alpha, color=BG):
    """Camada RGBA com degradê vertical de transparência."""
    layer = Image.new("RGBA", (width, height))
    px = layer.load()
    for y in range(height):
        a = int(top_alpha + (bottom_alpha - top_alpha) * y / max(height - 1, 1))
        for x in range(width):
            px[x, y] = (*color, a)
    return layer


def cover(img, width, height, focus_y=0.5):
    """Escala para cobrir a área e recorta, com foco vertical configurável."""
    scale = max(width / img.width, height / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    left = (img.width - width) // 2
    top = round((img.height - height) * focus_y)
    return img.crop((left, top, left + width, top + height))


def rounded(img, radius):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *img.size), radius, fill=255)
    out = img.convert("RGBA")
    out.putalpha(mask)
    return out


def photo(name):
    return ImageOps.exif_transpose(Image.open(os.path.join(PHOTOS, name))).convert("RGB")


def overlay(canvas, layer, y):
    canvas.paste(layer, (0, y), layer)


def save(canvas, name):
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, name)
    canvas.save(path, optimize=True)
    print(f"{os.path.relpath(path, ROOT)}: {canvas.size}")


def main_post():
    canvas = Image.new("RGB", (W, H), BG)

    # Foto de destaque: escala pela largura e recorta a faixa que contém o teclado.
    hero = photo(HERO)
    hero = hero.resize((W, round(hero.height * W / hero.width)), Image.LANCZOS)
    canvas.paste(hero.crop((0, HERO_CROP_Y, W, HERO_CROP_Y + PHOTO_H)), (0, 0))

    # Degradês: escurece o topo (título) e funde a base da foto com o painel.
    overlay(canvas, gradient(W, 330, 235, 0), 0)
    overlay(canvas, gradient(W, 260, 0, 255), PHOTO_H - 260)

    draw = ImageDraw.Draw(canvas)

    # Título e subtítulo.
    draw.text((MARGIN, 50), "SOFLE", font=font(150, "Bold"), fill=WHITE)
    sofle_w = draw.textlength("SOFLE ", font=font(150, "Bold"))
    draw.text((MARGIN + sofle_w, 50), "v2", font=font(150, "Bold"), fill=ORANGE)
    draw.text((MARGIN + 4, 218), "Teclado split montado do zero", font=font(46, "SemiBold"), fill=WHITE)

    # Etapas da montagem.
    gap = 20
    size = (W - 2 * MARGIN - gap * (len(STAGES) - 1)) // len(STAGES)
    y = 985
    for i, (name, label) in enumerate(STAGES):
        x = MARGIN + i * (size + gap)
        thumb = rounded(cover(photo(name), size, size, focus_y=0.55), 18)
        canvas.paste(thumb, (x, y), thumb)
        draw.text((x + 6, y + size + 8), f"{i + 1}  {label}", font=font(24, "SemiBold"), fill=WHITE)

    draw.text((MARGIN, 1275), SPECS, font=font(30, "SemiBold"), fill=WHITE)
    save(canvas, "sofle-v2-post.png")


def before_after(filename, photo_name, title, color, caption, focus_y):
    """Foto em tela cheia com o título no topo e a legenda embaixo."""
    canvas = cover(photo(photo_name), W, H, focus_y)
    overlay(canvas, gradient(W, 360, 225, 0), 0)
    overlay(canvas, gradient(W, 300, 0, 235), H - 300)
    draw = ImageDraw.Draw(canvas)
    draw.text((MARGIN, 50), title, font=font(170, "Bold"), fill=color or (ORANGE if title == "DEPOIS" else WHITE))
    draw.text((MARGIN + 4, H - 120), caption, font=font(50, "SemiBold"), fill=WHITE)
    draw.text((MARGIN + 4, H - 190), "SOFLE v2", font=font(30, "SemiBold"), fill=ORANGE)
    save(canvas, filename)


main_post()
before_after(*BEFORE)
before_after(*AFTER)
