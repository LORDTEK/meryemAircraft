# -*- coding: utf-8 -*-
"""Uc boyutlu vakayi kurar -- iki boyutlusundan YALNIZCA agiyla ayrilarak.

Tasarim karari. Alan dosyalarini, ayrik sema secimlerini, cozucu ayarlarini
ve turbulans kurulumunu YENIDEN YAZMIYORUZ; naca/kur.py cagriliyor ve
ciktisinin yalnizca iki parcasi degistiriliyor:

  1. ag.msh -> uc boyutlu ag
  2. 0/* icindeki "(on|arka) empty" -> "(kok|uc) <tip>"

Sebep: iki boyutlu ile uc boyutlu arasindaki farkin AGDAN geldigini iddia
edebilmek icin, geri kalan her seyin bit bit ayni olmasi gerekir. Ayri bir
kurucu yazilsaydi, cikan fark "uc boyutluluk mu, yoksa fark gozden kacan bir
sema ayari mi?" sorusunu acik birakirdi.

Degistirmenin sessizce basarisiz olmamasi icin her dosyada ESLESME SAYISI
denetleniyor.
"""
import os
import re
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "..", "naca"))
sys.path.insert(0, BURA)
from kur import kur as kur2b                          # noqa: E402


def kur3b(dizin, ag, kok="symmetryPlane", uc="symmetryPlane", **kw):
    """ag: KanatAgi ornegi. kw, naca/kur.py'nin kur()'una gecer."""
    kw.setdefault("kod", "0012")
    bilgi2 = kur2b(dizin, **kw)

    # 1) agi degistir
    yeni = ag.yaz(os.path.join(dizin, "ag.msh"))

    # 2) yamalari degistir
    eski = ('    "(on|arka)"\n    {\n        type            empty;\n    }\n')
    yerine = ('    kok\n    {\n        type            %s;\n    }\n'
              '    uc\n    {\n        type            %s;\n    }\n' % (kok, uc))
    n = 0
    for ad in sorted(os.listdir(os.path.join(dizin, "0"))):
        p = os.path.join(dizin, "0", ad)
        s = open(p).read()
        adet = s.count(eski)
        if adet != 1:
            raise RuntimeError("0/%s icinde on|arka blogu %d kez gecti, "
                               "1 bekleniyordu" % (ad, adet))
        open(p, "w").write(s.replace(eski, yerine))
        n += 1
    if n == 0:
        raise RuntimeError("0/ bos -- kur2b calismamis olabilir")

    # 3) 2B'ye ozgu sema kalintisi kalmadigini dogrula
    for ad in ("fvSchemes", "fvSolution", "controlDict"):
        s = open(os.path.join(dizin, "system", ad)).read()
        if "empty" in s:
            raise RuntimeError("system/%s icinde 'empty' gecıyor" % ad)

    bilgi = dict(bilgi2 or {})
    bilgi.update(yeni)
    bilgi["alan_dosyasi"] = n
    return bilgi


# kos3b.sh ELDEN yazilan ayri bir dosyadir; buradan URETILMEZ. Onceki
# surumde bir dizge olarak burada tutuluyordu ve gomulu Python'un duzenli
# ifadelerindeki kacislar dizge cozumlemesinde yenerek betigi bozuyordu.
# Kaba agda yapilan hizli deneme yakaladi.
