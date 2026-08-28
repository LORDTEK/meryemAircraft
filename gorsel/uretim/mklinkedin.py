# -*- coding: utf-8 -*-
"""LinkedIn paylasim karti — 1200 x 1200.

Akista kayan birinin iki saniyede gormesi gereken sey: ayni arac, iki duruş.
Kuyruğu uzerinde dikilirken ve kanadiyla seyrederken. Arada donen tek sey
aracin kendisi; uzerinde hicbir parca donmuyor. Karti bu anlatir.

Yan gorunus dik izdusumdur; yunuslama ekseni bu duzleme dik oldugu icin
siluetin 90 derece dondurulmesi araci gercekten dondurmekle ayni sonucu verir
(makale Sekil 9 ile ayni yontem notu).

Kaynak siluet: figlib ile modelden uretilir, yoksa Sekil 4'ten alinmaz —
uretim betigi calistirilmadan kart uretilmez, boylece kart hep modelle uyumlu.
"""
import os, sys, math, asyncio
from PIL import Image, ImageDraw, ImageFont
import matplotlib

BURA = os.path.dirname(os.path.abspath(__file__))
GOR = os.path.abspath(os.path.join(BURA, "..", "cikti"))
FD = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")


def F(sz, b=False):
    return ImageFont.truetype(
        os.path.join(FD, "DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf"), sz)


INK, MUT, ACC = (28, 32, 36), (110, 120, 128), (47, 111, 143)
W = H = 1200
KENAR = 76


def siluet():
    """Modelden temiz bir yan gorunus uretir."""
    sys.path.insert(0, BURA)
    from figlib import render, autocrop
    res, _ = asyncio.run(render({"side": (math.pi / 2, 0.0)}, "hafif",
                                w=1600, h=1200, scale=2, rmul=1.25))
    im, _ = autocrop(res["side"], pad=8)
    return im.convert("RGB")


def sar(d, metin, font, en):
    satir, cikti = "", []
    for k in metin.split():
        dn = (satir + " " + k).strip()
        if d.textlength(dn, font=font) > en and satir:
            cikti.append(satir); satir = k
        else:
            satir = dn
    if satir:
        cikti.append(satir)
    return cikti


def kart(dosya, ust, alt, etiketler, yan):
    tuval = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(tuval)

    fb = F(46, True)
    y = KENAR
    for s in sar(d, ust, fb, W - 2 * KENAR):
        d.text((KENAR, y), s, font=fb, fill=INK); y += 60
    y += 14
    d.line([(KENAR, y), (W - KENAR, y)], fill=(214, 220, 225), width=2)
    ust_bitis = y

    fa = F(30)
    alt_satirlar = sar(d, alt, fa, W - 2 * KENAR)
    alt_h = len(alt_satirlar) * 43 + 30 + 32
    alt_bas = H - KENAR - alt_h

    # --- iki duruş, AYNI olcekte ---
    dik = yan.rotate(-90, expand=True)      # burun yukari: kuyruguna oturmus
    yat = yan                                # seyir

    ETIKET_H = 46                            # etiketlere ayrilan serit
    kutu_ust = ust_bitis + 34
    kutu_alt = alt_bas - 26 - ETIKET_H
    kutu_h = kutu_alt - kutu_ust
    ARA = 64
    kutu_w = W - 2 * KENAR

    olcek = min(kutu_h / dik.height, (kutu_w - ARA) / (dik.width + yat.width))
    dw, dh = int(dik.width * olcek), int(dik.height * olcek)
    yw, yh = int(yat.width * olcek), int(yat.height * olcek)

    orta = kutu_ust + kutu_h // 2            # ikisi de dikeyde ayni eksende
    x = KENAR + (kutu_w - dw - ARA - yw) // 2
    tuval.paste(dik.resize((dw, dh), Image.LANCZOS), (x, orta - dh // 2))
    xy = x + dw + ARA
    tuval.paste(yat.resize((yw, yh), Image.LANCZOS), (xy, orta - yh // 2))

    fe = F(25, True)
    ey = kutu_alt + 12
    for merkez, et in ((x + dw // 2, etiketler[0]), (xy + yw // 2, etiketler[1])):
        d.text((merkez - d.textlength(et, font=fe) / 2, ey), et, font=fe, fill=ACC)

    y = alt_bas
    for s in alt_satirlar:
        d.text((KENAR, y), s, font=fa, fill=(51, 57, 63)); y += 43
    d.text((KENAR, y + 12),
           "Gülmen · Gülmen · Gülmen   ·   zenodo.org/records/22144195",
           font=F(23), fill=MUT)

    tuval.save(os.path.join(GOR, dosya))
    print("yazildi:", dosya)


if __name__ == "__main__":
    yan = siluet()
    kart("linkedin-kart-tr.png",
         "Aynı uçak, iki duruş. Arada dönen tek şey uçağın kendisi.",
         "Dikey kalkan uçaklar pistten kurtulur ama bunu seyir verimliliğinden "
         "öderler. Bu bedelin bir tasarım kusuru değil, mimarinin kendisi "
         "olduğunu savunduk — ve onu ödemeyen bir konfigürasyon önerdik.",
         ("askıda", "seyirde"), yan)

    kart("linkedin-kart-en.png",
         "One aircraft, two attitudes. The only thing that rotates is the aircraft.",
         "Aircraft that take off vertically escape the runway but pay for it in "
         "cruise efficiency. We argue the cost is architectural rather than a "
         "design defect — and propose a configuration that does not pay it.",
         ("hover", "cruise"), yan)
