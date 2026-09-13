# -*- coding: utf-8 -*-
"""SIKISTIRILABILIRLIK -- 0,0153 bir SAYI mi yoksa yalnizca bir TABAN mi?

SORUN. Serbest donme direnci 0,0153, uc Mach 0,77'de SIKISTIRILAMAZ
kesit verisiyle hesaplandi. Dort dis okumanin dordu de ayni yere bastÄ±:
bu sayi artik makalenin merkezinde -- 1/1,58 seyir carpani, L/D 8,49,
54,5 kg, +%21,1 siralama donusu, hepsi ondan turuyor. Bir taban sayi
bir paragrafta yuk tasiyip digerinde taban olamaz.

ISARET BIR CIKTI, GIRDI DEGIL. "Sikistirilabilirlik direnci artirir, o
yuzden 0,0153 bir alt sinirdir" demek kolaydi ve YANLIS olabilirdi:
Prandtl-Glauert kaldirma egimini DIKLESTIRIR, yani palet ayni itkiyi
DAHA DUSUK devirde uretir; profil suruklemesi W^2 ile duserken kesit
c_d'si dalga terimiyle yukselir. Iki etki ters yonde. Hangisinin
kazandigini hesap soyler.

YONTEM (muhendislik duzeltmesi, CFD DEGIL -- oyle de yaziliyor):
  - kaldirma: Prandtl-Glauert, c_l / sqrt(1 - M^2), M < 0,95'te kirpilir
  - surukleme sapmasi: Korn bagintisi, M_dd = k - t/c - c_l/10
    (ok acisi yok; palet kesiti okusuz)
  - dalga suruklemesi: Lock'un dorduncu kuvvet yasasi, 20 (M - M_dd)^4
  - M >= 0,95 olan serit SAYILMAZ, isaretlenir: bu duzeltme orada gecerli
    degildir ve gecerliymis gibi rapor edilmez.

Duzeltilmis polar ayni sifir-tork cozumune verilir; devir YENIDEN
ARANIR, sabit tutulmaz.
"""
import math, os, sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
import numpy as np                                      # noqa: E402
import uc_pervane as U                                  # noqa: E402

A_SES = 340.0
KORN = 0.87          # klasik kesitler icin alisilmis deger
TC = 0.12            # naca0012
M_KIRP = 0.95


def kesit_sikistirilabilir(alfa_deg, Re, M):
    """NeuralFoil'in sikistirilamaz polarina Mach duzeltmesi."""
    cl, cd = U.kesit_kuvvet(alfa_deg, Re)
    M = np.asarray(M, dtype=float)
    Mk = np.clip(M, 0.0, M_KIRP)
    beta = np.sqrt(np.maximum(1.0 - Mk ** 2, 1e-3))
    cl_c = cl / beta
    m_dd = KORN - TC - np.abs(cl_c) / 10.0
    dalga = np.where(Mk > m_dd, 20.0 * (Mk - m_dd) ** 4, 0.0)
    return cl_c, cd + dalga, (M > M_KIRP)


def bemt_sik(V, omega, c, th, tur=150, sik=True):
    """bemt_sabit'in IKIZI -- tek farkla: kesit polari Mach goruyor.

    uc_pervane.bemt_sabit'i maymun-yamasi ile degistirmedim. Sebep:
    kesit_kuvvet(alfa, Re) yerel hizi GORMUYOR ve Re kirpildigi icin
    W geri cikarilamiyor. Yama, kirpilan seritlerde sessizce yanlis Mach
    kullanirdi. Ikiz cozucu ayni denklemleri kullanir ve W'yi elinde
    tutar. sik=False ile cagrilirsa ozgun sonucu YENIDEN URETMELIDIR --
    ana blokta bu sinaniyor.
    """
    r, dr = U.serit()
    v = np.full_like(r, 5.0)
    w = np.zeros_like(r)
    for _ in range(tur):
        Va, Vt = V + v, omega * r - w
        W = np.hypot(Va, Vt)
        phi = np.arctan2(Va, np.maximum(Vt, 1e-6))
        alfa = (th - phi) / U.D2R
        Re = np.clip(U.RHO * W * c / U.MU, 2e4, 2e6)
        if sik:
            cl, cd, _ = kesit_sikistirilabilir(alfa, Re, W / A_SES)
        else:
            cl, cd = U.kesit_kuvvet(alfa, Re)
        f = U.B / 2.0 * (U.R - r) / np.maximum(r * np.sin(phi), 1e-6)
        F = np.clip(2 / math.pi * np.arccos(np.clip(np.exp(-np.abs(f)), 0, 1)),
                    1e-3, 1.0)
        q = 0.5 * U.RHO * W ** 2 * c
        dT = U.B * q * (cl * np.cos(phi) - cd * np.sin(phi))
        dQt = U.B * q * (cl * np.sin(phi) + cd * np.cos(phi))
        disk = 4 * math.pi * U.RHO * r * F
        with np.errstate(divide="ignore", invalid="ignore"):
            v_yeni = -V / 2.0 + np.sqrt(np.maximum(
                (V / 2.0) ** 2 + np.maximum(dT, 0.0) / disk, 0.0))
            w_yeni = dQt / np.maximum(2 * disk * (V + v), 1e-6)
        v += 0.3 * (np.clip(np.nan_to_num(v_yeni), 0.0, 60.0) - v)
        w += 0.3 * (np.clip(np.nan_to_num(w_yeni), 0.0, 0.5 * omega * r) - w)
    Va, Vt = V + v, omega * r - w
    W = np.hypot(Va, Vt)
    phi = np.arctan2(Va, np.maximum(Vt, 1e-6))
    alfa = (th - phi) / U.D2R
    Re = np.clip(U.RHO * W * c / U.MU, 2e4, 2e6)
    if sik:
        cl, cd, asti = kesit_sikistirilabilir(alfa, Re, W / A_SES)
    else:
        cl, cd = U.kesit_kuvvet(alfa, Re)
        asti = np.zeros_like(r, dtype=bool)
    q = 0.5 * U.RHO * W ** 2 * c
    T = (U.B * q * (cl * np.cos(phi) - cd * np.sin(phi)) * dr).sum()
    Q = (U.B * q * (cl * np.sin(phi) + cd * np.cos(phi)) * r * dr).sum()
    return T, Q, float(np.max(W / A_SES)), bool(np.any(asti))


def sifir_tork_sik(c, th, V=U.V_SEYIR, sik=True):
    """Net saft torkunun sifir oldugu omega -- YENIDEN ARANIR, sabitlenmez."""
    def Q(om):
        return bemt_sik(V, om, c, th, sik=sik)[1]
    alt, ust = 100.0, 8000.0
    if Q(alt) * Q(ust) > 0:
        return None, None, None, None
    for _ in range(34):
        om = 0.5 * (alt + ust)
        if Q(alt) * Q(om) <= 0:
            ust = om
        else:
            alt = om
    om = 0.5 * (alt + ust)
    T, _, M, asti = bemt_sik(V, om, c, th, sik=sik)
    return om, T, M, asti


if __name__ == "__main__":
    print("SIKISTIRILABILIRLIK -- 0,0153 sayi mi, taban mi?")
    print("Korn k = %.2f, t/c = %.2f, Mach kirpma %.2f" % (KORN, TC, M_KIRP))
    print()
    c, th = U.hover_tasarla(cl_hedef=0.68)

    # --- 1) IKIZ COZUCU SINAMASI ---------------------------------------
    om0, T0, M0, _ = sifir_tork_sik(c, th, sik=False)
    om_ref, T_ref = U.sifir_tork(c, th)
    print("IKIZ COZUCU SINAMASI (sikistirilamaz kipte ozgunu uretmeli)")
    print("  ozgun   : %.0f rpm, eksenel %.4f N, dC_D0 %.5f"
          % (om_ref * 60 / 2 / math.pi, T_ref, U.dcd0(T_ref)))
    print("  ikiz    : %.0f rpm, eksenel %.4f N, dC_D0 %.5f"
          % (om0 * 60 / 2 / math.pi, T0, U.dcd0(T0)))
    if abs(T0 - T_ref) > 1e-3 * max(1.0, abs(T_ref)):
        sys.exit("!! DUR -- ikiz cozucu ozgunu uretmiyor, karsilastirma gecersiz.")
    print("  ikiz dogrulandi.")

    # --- 2) SIKISTIRILABILIR KOSU --------------------------------------
    om1, T1, M1, asti = sifir_tork_sik(c, th, sik=True)
    d0, d1 = U.dcd0(T0), U.dcd0(T1)
    print()
    print("SEYIR, NET SAFT TORKU SIFIR")
    print("  %-22s %10s %10s %10s" % ("", "rpm", "uc Mach", "dC_D0 (8)"))
    print("  %-22s %10.0f %10.2f %10.5f"
          % ("sikistirilamaz", om0 * 60 / 2 / math.pi, M0, d0))
    print("  %-22s %10.0f %10.2f %10.5f"
          % ("sikistirilabilir", om1 * 60 / 2 / math.pi, M1, d1))
    print()
    print("  oran  dC_D0_sik / dC_D0_siksiz = %.3f" % (d1 / d0))
    print("  isaret: %s" % ("ARTTI" if d1 > d0 else "AZALDI"))
    if asti:
        print("  !! bazi seritler M > %.2f -- duzeltme orada GECERSIZ." % M_KIRP)
    print()
    print("KARAR ESIGI")
    print("  0,0153'e yakin ise      -> sayi saglam, RANS'a gec")
    print("  0,020 - 0,030 bandi     -> 2.2 ve 3.6 yeniden sayisallastirilmali")
    print("  cok daha buyuk          -> +%21,1 guvenilmez, karsilastirma yeniden")
