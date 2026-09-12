# -*- coding: utf-8 -*-
"""GECIS, DONME DINAMIGI ILE -- nokta kutle sonucu ayakta kaliyor mu?

NEDEN VAR. 3.15'in benzetimi govde acisini KINEMATIK suruyor: ucak
donmuyor, donduruluyor, ve donmeyi ureten moment denklemde hic yok.
3.17 ayri olarak momentin YETIP yetmedigine bakiyor ama yorungeyi
hesaba katmiyor. Ikisi hic bulusmadi. Bu betik bulusturuyor: uc serbestlik
(x, z, theta), sonlu kontrol momenti, ve ODUNC ALINMIS bir C_m(alfa).

DURUST CERCEVE. Bu bir TAHMIN DEGIL, bir DUYARLILIK taramasidir. Makale
zaten uc farkli sadakatte uc yontemin ~10 derecenin uzerinde olcumle
uyusmadigini yaziyor; dorduncu bir model o bosluga sayi koymaz. Sorulan
sey su: nokta kutle sonucu -- tirmanisla girilince irtifa kaybi sifir --
MAKUL her C_m altinda ayakta kaliyor mu, yoksa bazilarinda cokuyor mu?
Ikinci durumda sonuc modelin secimine bagimlidir ve bunu bilmek gerekir.

MODELLER (hicbiri bu planform icin olculmedi)
  sifir      : C_m = 0. Donme dinamiginin TEK BASINA etkisini ayirir.
  dogrusal   : C_m = C_m0 + C_m_alfa alfa, VLM'den C_m_alfa = -0,48/rad.
  duz levha  : ince levha iliskisi, 90 dereceye kadar; 3.15'in kaldirma
               icin zaten kullandigi ayni kaba model, momente uygulanmis.
  kaydirma   : sabit +-0,05 / +-0,10 ofset. "Ne kadar moment yutulabilir"
               sorusunu dogrudan sorar.

NE ALEYHIMIZE SAYILIR
  - makul bir modelde donme 90 dereceye VARMIYORSA,
  - ya da kontrol momenti DOYUYORSA,
  - ya da irtifa kaybi referans profilde 20 m'yi asiyorsa.
"""
import math, os, sys

import numpy as np

RHO, G = 1.225, 9.81
D2R = math.pi / 180.0


def catlak_cm(model, alfa, ofset=0.0):
    """Oduncu alinan C_m(alfa) modelleri. alfa radyan."""
    if model == "sifir":
        return 0.0 * alfa
    if model == "dogrusal":
        return 0.056 - 0.48 * alfa
    if model == "levha":
        # ince levha: merkez basinc 0.25c'den 0.5c'ye kayar -> burun asagi
        return -0.25 * np.sin(2 * alfa)
    if model == "kaydirma":
        return 0.0 * alfa + ofset
    raise ValueError(model)


def kos(m, S, c_ort, Iyy, AR, M_kontrol, tr, Vcr, w0=5.0,
        model="sifir", ofset=0.0, CD0=0.0248, e=0.85,
        astall=12 * D2R, dt=1e-4, profil="bang"):
    """Uc serbestlikli gecis. Govde acisi KOMUT EDILIR, surulmez.

    Kontrolcu: istenen theta(t) profiline PD ile oturur, ama urettigi
    moment M_kontrol ile SINIRLIDIR. Doyma olursa kaydedilir -- kinematik
    benzetimde gorunmeyen sey tam olarak budur.
    """
    W = m * G
    T = M_kontrol / (2 * 0.71) if False else None      # kullanilmiyor
    CLa = 2 * math.pi / (1 + 2 / AR)
    vx, vh = 0.0, w0
    th, q = 0.0, 0.0
    t, h = 0.0, 0.0
    en_dusuk, doyma, ulasti = 0.0, 0.0, False
    Tmax = 1.066 * W                                   # 3.15: ulasilabilir
    while t <= 4 * tr:
        tau = min(t / tr, 1.0)
        if profil == "bang":
            f = 2 * tau ** 2 if tau <= 0.5 else 1 - 2 * (1 - tau) ** 2
        elif profil == "dogrusal":
            f = tau                      # 3.15'in kendi profili
        else:
            f = 3 * tau ** 2 - 2 * tau ** 3
        th_ref = (math.pi / 2) * f
        q_ref = 0.0
        # PD, sonlu otorite
        M_ist = Iyy * (25.0 * (th_ref - th) + 10.0 * (q_ref - q))
        M = max(-M_kontrol, min(M_kontrol, M_ist))
        if abs(M_ist) > M_kontrol:
            doyma += dt
        V = math.hypot(vx, vh)
        bx, bh = math.sin(th), math.cos(th)
        if V > 1e-6:
            ux, uh = vx / V, vh / V
            al = -math.atan2(bx * uh - bh * ux, bx * ux + bh * uh)
        else:
            ux, uh, al = bx, bh, 0.0
        aa = abs(al)
        CL = CLa * al if aa <= astall else math.copysign(
            2 * math.sin(aa) * math.cos(aa), al)
        CD = CD0 + CL * CL / (math.pi * AR * e) + 2 * math.sin(aa) ** 3
        qd = 0.5 * RHO * V * V
        L, Dg = qd * S * CL, qd * S * CD
        Cm = float(catlak_cm(model, np.array([al]), ofset)[0]) \
            if model != "dogrusal" else float(catlak_cm(model, al, ofset))
        M_aero = qd * S * c_ort * Cm
        Th = Tmax if V < Vcr or vx < Vcr * 0.95 else min(Tmax, Dg)
        vx += ((Th * bx - L * uh - Dg * ux) / m) * dt
        vh += ((Th * bh + L * ux - Dg * uh) / m - G) * dt
        q += (M + M_aero) / Iyy * dt
        th += q * dt
        h += vh * dt
        en_dusuk = min(en_dusuk, h)
        if th >= math.pi / 2 - 1e-3:
            ulasti = True
        t += dt
        if th > math.pi:                                # kontrolden cikti
            return dict(kayip=en_dusuk, doyma=doyma, ulasti=False,
                        theta_son=th / D2R, firladi=True)
    return dict(kayip=en_dusuk, doyma=doyma, ulasti=ulasti,
                theta_son=th / D2R, firladi=False)


HAFIF = dict(m=50.0, S=1.979, c_ort=0.62, Iyy=9.81, AR=6.03, Vcr=30.0)
AGIR = dict(m=1000.0, S=22.24, c_ort=2.08, Iyy=2503.0, AR=6.0, Vcr=40.0)


def basli(s):
    print("\n" + s)
    print("-" * len(s))


if __name__ == "__main__":
    print("GECIS + DONME DINAMIGI -- oduncu C_m uzerinde DUYARLILIK")
    print("Bu bir tahmin degil. Sorulan: nokta kutle sonucu her makul")
    print("C_m altinda ayakta mi?")

    for ad, G_, tr, Mk in (("HAFIF 50 kg, t_r = 2 s, M = 23,0 N.m", HAFIF, 2.0, 23.0),
                           ("HAFIF, muhafazakar itki, M = 17,6 N.m", HAFIF, 2.0, 17.6),
                           ("AGIR 1000 kg, t_r = 5,1 s, M = 952 N.m", AGIR, 5.1, 952.0)):
        basli(ad + "   (giris tirmanisi 5 m/s)")
        print("%-22s %11s %9s %9s %9s"
              % ("C_m modeli", "irtifa m", "90 dr?", "doyma s", "theta son"))
        for model, ofset, etiket in (("sifir", 0, "sifir"),
                                     ("dogrusal", 0, "dogrusal (VLM)"),
                                     ("levha", 0, "duz levha"),
                                     ("kaydirma", +0.05, "sabit +0.05"),
                                     ("kaydirma", -0.05, "sabit -0.05"),
                                     ("kaydirma", +0.10, "sabit +0.10"),
                                     ("kaydirma", -0.10, "sabit -0.10")):
            r = kos(M_kontrol=Mk, tr=tr, model=model, ofset=ofset, **G_)
            print("%-22s %11.2f %9s %9.2f %9.1f"
                  % (etiket, r["kayip"], "evet" if r["ulasti"] else "HAYIR",
                     r["doyma"], r["theta_son"]))
