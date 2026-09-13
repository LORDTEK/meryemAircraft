# -*- coding: utf-8 -*-
"""3.6'YI IKI TASINMIS SAYIYLA YENIDEN BOYUTLANDIR.

NEDEN. 3.6'nin uc-sozlesme tablosu iki girdi uzerine kuruluydu ve tur 15
ile 16 ikisini de oynatti:

  (1) A'nin seyir cezasi 1/1,12 idi ve YALNIZCA uc cercevelerini
      faturaliyordu. 3.3 serbest donen uc rotorlarini hesapladi:
      dC_D0 >= 0,0153. B'nin 13/17'si ise OLCULMUS bir konfigurasyondan
      gelir ve kendi rotor suruklemesini zaten icerir. Yani tablo
      A'nin lehine egikti ve egiklik olculmemisti.

  (2) Tampon 5,63 kW/kg varsayiyordu. Olculmus tavan 1,5 kW/kg ve
      kapanma dongusu orada 68,9 kg veriyor.

BU BETIK NE YAPIYOR. Ayni tabloyu dort girdi kombinasyonunda yeniden
kosturur: eski/yeni surukleme x eski/yeni tampon. Boylece "hangi sayi
sonucu ne kadar tasidi" ayri ayri okunur -- ikisini birden degistirip
tek bir yeni tablo basmak, hangi terimin ne yaptigini gizlerdi.

DURUSTLUK NOTU. B ve C'ye de ayni tampon verilir. Onlara vermeyip yalniz
A'yi cezalandirmak, 4.4'un "B ayni pakette yeniden boyutlandirilmali"
uyarisini tersine cevirmek olurdu.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
import temel as T                                          # noqa: E402
import planform as P                                       # noqa: E402

CL, E_SPAN, CD0 = 0.45, 0.817, 0.0248


def carpan(rotor):
    """Seyir L/D carpani, surukleme kurulusundan.

    Temiz gövde = toplam eksi cerceveler eksi rotorlar. Carpan, o temize
    gore oran. rotor=0 makalenin 1/1,12'sini yeniden uretir -- zincirin
    dogrulugu once bununla sinaniyor.
    """
    AR = P.olcuier()["AR"]
    cdi = CL * CL / (math.pi * AR * E_SPAN)
    top = CD0 + cdi
    temiz = top - 0.0043
    return temiz / (top + rotor)


if __name__ == "__main__":
    eski, yeni = carpan(0.0), carpan(0.0153)
    print("SEYIR CEZASI, surukleme kurulusundan")
    print("  cerceveler yalniz      1/%.3f   (makale 1/1,12 diyor)"
          % (1 / eski))
    print("  + serbest donen rotor  1/%.3f   (3.3: dC_D0 >= 0,0153)"
          % (1 / yeni))
    if abs(1 / eski - 1.12) > 0.02:
        sys.exit("!! DUR -- taban carpan makalenin 1,12'sini uretmiyor.")
    print("  taban yeniden uretildi, zincir tutarli.")

    # Tampon kesri. 0,04 varsayilan; olculmus 1,5 kW/kg pakette kapanma
    # dongusu tamponu MTOW'un %15,6'sina cikariyor (4.4). UCUNE DE ayni
    # kesir verilir -- yalniz A'yi cezalandirmak 4.4'un kendi uyarisini
    # tersine cevirmek olurdu.
    for t_ad, t in (("tampon %4 (varsayilan)", 0.04),
                    ("tampon %15,6 (olculmus paket)", 0.156)):
        for d_ad, c in (("ESKI surukleme (yalniz cerceveler)", None),
                        ("YENI surukleme (rotorlar dahil)", yeni)):
            print("\n" + "=" * 70)
            print("%s  |  %s" % (d_ad, t_ad))
            print("=" * 70)
            T.sozlesmeler(A_LD_carpan=c, f_tampon=t)
