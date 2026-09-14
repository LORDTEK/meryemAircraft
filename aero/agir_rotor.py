# -*- coding: utf-8 -*-
"""AGIR HATTIN uc rotorlari da serbest donme faturasi odar mi?

3.8 de tam 3.6'nin tasidigi kusuru tasiyor: LD_temiz = 13,6 x 1,12, yani
YALNIZCA uc cerceveleri faturalanmis, serbest donen rotorlar degil.
Hafif hatta o terim 0,0154 cikti; agir hatta OLCEKLEME ile tahmin etmek
yerine ayni BEMT ayni kosullarda kosturuluyor.

AGIR HATTIN KENDI SAYILARI (3.8 ve donme.py'den, uydurulmuyor):
    D = 0,67 m, 8 disk, V = 40 m/s, S_ref = 22,24 m2
    uc cifti gucu = hover gucunun %12'si / 4 = 0,12 x 216,2 kW / 4
    hover itkisi momentum kuraminden, FM = 0,599 ile

uc_pervane.py modul duzeyi sabitlerle yazilmis; burada o sabitler AGIR
hattin degerleriyle degistiriliyor ve ayni fonksiyonlar cagriliyor.
Kendi kopyasini yazmak, cikan farkin "olcek mi, yoksa ikinci bir
kurulus mu?" sorusunu acik birakirdi.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
import uc_pervane as U                                  # noqa: E402

P_HOVER_KW, D_AGIR, V_AGIR, S_AGIR = 216.2, 0.67, 40.0, 22.24
FM = 0.599


def agir_ayarla():
    U.D, U.R = D_AGIR, D_AGIR / 2.0
    U.V_SEYIR, U.S_REF = V_AGIR, S_AGIR
    p_cift = 0.12 * P_HOVER_KW * 1000.0 / 4.0
    A = math.pi * U.R ** 2
    # momentum: P = T^1.5 / (FM sqrt(2 rho A))  ->  T
    T = (p_cift / 2.0 * FM * math.sqrt(2 * U.RHO * A)) ** (2.0 / 3.0)
    return p_cift, T


if __name__ == "__main__":
    p_cift, T = agir_ayarla()
    print("AGIR HAT, UC ROTORU")
    print("  D %.2f m, 8 disk, V %.0f m/s, S_ref %.2f m2" % (U.D, U.V_SEYIR, U.S_REF))
    print("  cift gucu %.0f W, rotor basina hover itkisi %.1f N" % (p_cift, T))
    print("  (hafif hat: 335 W, 8,1 N)")
    print()
    print("%-12s %9s %10s %9s %12s" % ("tasarim c_l", "FM", "rpm", "uc Mach",
                                       "dC_D0 (8 disk)"))
    en_iyi = None
    # LISTE GENISLETILDI VE BU BIR DUZELTME DEGIL, BIR ITIRAF.
    # Eski liste (0,55 / 0,62 / 0,68 / 0,75) ile "FM >= 0,599 saglayanlar
    # arasinda en az surukleyen" kurali 0,75'i seciyor, dC_D0 = 0,00446.
    # Oysa makale 0,0051 tasiyor ve o, listede OLMAYAN c_l = 0,70'in
    # degeri. Yani tasinan sayi kuralin sectigi sayi degildi.
    # Genisletince asil sorun goruldu: HAFIF hatta FM 0,70'in ustunde
    # ucurumdan atliyor (0,633 -> 0,350) ve kural orada BAGLIYOR; agir
    # hatta atlamiyor (0,85'te hala 0,657), yani kural hic baglamiyor ve
    # secilen sayi listenin nerede bittigine bagli. Kurali oldugu gibi
    # uygulamak 0,85'i ve 0,0035'i verirdi -- bizim LEHIMIZE. Makale bu
    # yuzden tek sayi degil ARALIK rapor ediyor ve 0,0051'i tasimaya
    # devam ediyor; bkz. 3.8.
    for cl_h in (0.55, 0.62, 0.68, 0.70, 0.72, 0.75, 0.78, 0.85):
        c, th = U.hover_tasarla(cl_hedef=cl_h, T_hedef=T)
        om = U.devir_itki_icin(c, th, T_hedef=T)
        Th, Q, _ = U.bemt_sabit(1e-3, om, c, th)
        P = 2 * Q * om
        A = math.pi * U.R ** 2
        fm = 2 * (Th ** 1.5 / math.sqrt(2 * U.RHO * A)) / P if P > 0 else 0.0
        om2, T2 = U.sifir_tork(c, th)
        d = U.dcd0(T2) if om2 else float("nan")
        print("%-12.2f %9.3f %10.0f %9.2f %12.5f"
              % (cl_h, fm, (om2 * 60 / 2 / math.pi) if om2 else 0,
                 (om2 * U.R / 340.0) if om2 else 0, d))
        if fm >= FM and (en_iyi is None or d < en_iyi[1]):
            en_iyi = (cl_h, d, fm)
    print()
    if en_iyi:
        print("HOVER SARTINI (FM >= %.3f) SAGLAYAN EN AZ SURUKLEYEN TASARIM" % FM)
        print("  tasarim c_l %.2f, FM %.3f, dC_D0 = %.5f" % (en_iyi[0], en_iyi[2], en_iyi[1]))
        print("  hafif hat karsiligi: 0,01541")
        print()
        print("  !! KURAL BURADA BAGLAMIYOR. Hafif hatta FM 0,70'in ustunde")
        print("     coker ve secimi o coküs yapar; burada en yuksek c_l'de")
        print("     bile FM %.3f. Secilen tasarim listenin nerede bittigine" % en_iyi[2])
        print("     bagli, fizige degil. Makale bu yuzden ARALIK rapor eder.")
    else:
        print("!! Hicbir tasarim FM >= %.3f saglamadi -- agir uc rotoru" % FM)
        print("   hafif hattinki gibi tek bir sayiya oturmuyor; rapor edilmeli.")
