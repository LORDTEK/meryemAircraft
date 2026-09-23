# -*- coding: utf-8 -*-
"""Askida tepki torku -- birakilan kontrol kanalinin buyuklugu.

NEDEN: ChatGPT (Tur 47) makalenin "roll cannot be produced by propellers at
all" cumlesinin TEPKI TORKUNU atladigini gosterdi. §2.9 her rotorun kendi
elektrik makinesinde oldugunu soyluyor; iki karsit rotor farkli devirlerde
dondurulurse torklari birbirini goturmez ve net tork govde ekseni (X_b)
etrafindadir. Zhang ve ark. 2012 bunu BIRINCIL kontrol kanali olarak
kullaniyor (references/ica20120400001_12673514.pdf, Tablo 2).

Soru: o kanal ne kadar buyuk? Serit askida 6,0--12,0 N.m veriyor (§2.10).
Tepki torku ayni mertebede mi, yoksa ihmal edilebilir mi?

ILK TAHMIN YANLISTI. paper/roll-axis-finding.md once soyle yazdi:
    "10,9 kW, om ~ 273 rad/s -> rotor basi ~20 N.m; %30 -> 6 N.m"
Bu iki sayiyi KARISTIRIYORDU: 10,9 kW makalenin YAYIMLANMIS askı gucu,
273 rad/s ise BEMT tablosunun d_theta = 0 satiri -- yani SECILMEYEN palet.
Secilmis paletler (FM = 0,599 tutturanlar) daha yavas doner, dolayisiyla
ayni guc icin tork DAHA BUYUKTUR.

Bu betik sayiyi secilmis paletlerin kendisinden alir.

    Q_rotor = (P_cift / 2) / om_h

CAPRAZ DENETIM: hesaplanan cift gucu makalenin yayimlanmis 10,9 kW'ini
bagimsiz olarak yeniden uretmeli. Uretmezse sayi yayimlanmaz.
"""
import os
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)

from nose_propeller import Rotor, D_BURUN                       # noqa
from nose_propeller_crossing import fm_icin_hatve               # noqa

P_MAKALE_KW = 10.9          # §2.9, satir 788-792: askı gucu, rotorda
SERIT_ASKI = (6.0, 12.0)    # N.m, §2.10 satir 866-868


def main():
    print("ASKIDA TEPKI TORKU -- birakilan kanalin buyuklugu")
    print("=" * 72)
    print()
    print("Secilmis paletler (FM = 0,599 tutturan), askı noktasinda:")
    print()
    print("%-5s %-6s %9s %9s %13s %10s %10s"
          % ("pala", "c_l", "om_h r/s", "cift kW", "rotor basi Q", "%10 net", "%30 net"))
    print("-" * 72)
    qs, ps = [], []
    for B in (2, 3):
        rot = Rotor(D_BURUN, 2 * B)
        for cl in (0.55, 0.70):
            _, k = fm_icin_hatve(rot, cl)
            om, P = k["om_h"], k["P_h"]
            Q = (P / 2.0) / om              # cift toplam guc -> rotor basi
            qs.append(Q)
            ps.append(P / 1000.0)
            print("%-5d %-6.2f %9.1f %9.2f %13.2f %10.2f %10.2f"
                  % (B, cl, om, P / 1000.0, Q, 0.10 * Q, 0.30 * Q))
    print("-" * 72)
    print()

    print("CAPRAZ DENETIM -- makalenin yayimlanmis askı gucu %.1f kW:" % P_MAKALE_KW)
    print("  hesaplanan aralik: %.2f - %.2f kW" % (min(ps), max(ps)))
    sapma = max(abs(p - P_MAKALE_KW) for p in ps) / P_MAKALE_KW
    print("  en buyuk sapma   : %.1f %%" % (100 * sapma))
    if sapma > 0.05:
        print("  >>> SAPMA %5 USTUNDE. Sayi yayimlanmaz.")
        raise SystemExit(1)
    print("  ok -- bagimsiz olarak yeniden uretiliyor.")
    print()

    print("SONUC:")
    print("  rotor basi tork      : %.1f - %.1f N.m" % (min(qs), max(qs)))
    print("  %%10 dengesizlikte net: %.1f - %.1f N.m" % (0.10 * min(qs), 0.10 * max(qs)))
    print("  %%30 dengesizlikte net: %.1f - %.1f N.m" % (0.30 * min(qs), 0.30 * max(qs)))
    print()
    print("  Serit askida (§2.10) : %.1f - %.1f N.m" % SERIT_ASKI)
    print()
    print("  Yani %30'luk bir devir dengesizligi seridin askıdaki araliginin")
    print("  ICINDE kaliyor (%.1f-%.1f, serit %.1f-%.1f). Ihmal edilebilir DEGIL:"
          % (0.30 * min(qs), 0.30 * max(qs), SERIT_ASKI[0], SERIT_ASKI[1]))
    print("  bu, bu yapilandirmanin KULLANMAMAYI SECTIGI gercek bir kanaldir.")
    print()
    print("  Seridin alt ucunu (%.1f N.m) yakalamak icin gereken dengesizlik:"
          % SERIT_ASKI[0])
    print("    %.0f %% - %.0f %%" % (100 * SERIT_ASKI[0] / max(qs),
                                     100 * SERIT_ASKI[0] / min(qs)))
    print()
    print("SAYILMAYAN: dengesizligin itki asimetrisi, verim kaybi ve rotor")
    print("ataletinden gelen gecikmesi. Acik kalem.")


if __name__ == "__main__":
    main()
