"""v8 Sekil 1 TASLAGI (Tur 102 oylari, dort okuyucu + Claude): v7 Sekil 5 (uc gorunus, 50 kg referans tasarim, 2 m cubuk)
uzerine (c) paneline govde eksenleri. 3B goruntu yeniden uretilmez; v7 PNG'si okunur, eksenler ustune cizilir.
Adlandirma Adim 8'in govde ekseni kurali: x_b boylamsal eksen (govde terimleriyle yatis ekseni), burun yonunde; z_b asagi.
Askida ayni eksen dikeydir (Adim 8); iki kural karistirilmaz. y_b cizilmez (yan gorunuste bakis yonu belirtilmemis).
Etiketler v8_stale.py SEKILLER listesinde taranir.
"""
import os
import matplotlib
from PIL import Image, ImageDraw, ImageFont

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FD = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")
SRC = os.path.join(KOK, "figures", "output", "fig05-three-views.png")
OUT = os.path.join(KOK, "figures", "output", "v8-draft-f1-three-views.png")
INK = (28, 32, 36)

im = Image.open(SRC).convert("RGB")
d = ImageDraw.Draw(im)
k = im.width / 1400.0                      # yerlesim 1400 px genislikteki onizlemede olculdu
O = (1060 * k, 960 * k)                    # (c) panelinin bos alt-orta bolgesi
L = 100 * k
W = int(4 * k)
F = ImageFont.truetype(os.path.join(FD, "DejaVuSans-Oblique.ttf"), int(17 * k))
Fs = ImageFont.truetype(os.path.join(FD, "DejaVuSans.ttf"), int(12 * k))


def ok(p0, p1):
    d.line([p0, p1], fill=INK, width=W)
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    n = (dx * dx + dy * dy) ** 0.5
    ux, uy = dx / n, dy / n
    h = 14 * k
    d.polygon([p1, (p1[0] - h * ux + h * 0.45 * uy, p1[1] - h * uy - h * 0.45 * ux),
               (p1[0] - h * ux - h * 0.45 * uy, p1[1] - h * uy + h * 0.45 * ux)], fill=INK)


def etiket(xy, harf):
    d.text(xy, harf, font=F, fill=INK)
    w = d.textlength(harf, font=F)
    d.text((xy[0] + w + 1 * k, xy[1] + 9 * k), "b", font=Fs, fill=INK)


ok(O, (O[0] - L, O[1]))                    # x_b: burun yonunde (goruntude sol)
ok(O, (O[0], O[1] + L))                    # z_b: asagi
d.ellipse([O[0] - 4 * k, O[1] - 4 * k, O[0] + 4 * k, O[1] + 4 * k], fill=INK)
etiket((O[0] - L - 10 * k, O[1] - 30 * k), "x")
etiket((O[0] + 10 * k, O[1] + L - 22 * k), "z")
im.save(OUT, dpi=(600, 600))
print("yazildi: figures/output/v8-draft-f1-three-views.png")
