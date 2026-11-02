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

REVISION (2026-11). Five corrections to kos(); the submitted version is commit b1a340e.
  1. Moment sign. theta grows from hover (0) to cruise (pi/2), so +theta is nose-down, while C_m is nose-up positive
     (stability.py, and the flat-plate comment in catlak_cm below). The aerodynamic moment therefore enters as
     q += (M - M_aero) / Iyy. The submitted q += (M + M_aero) / Iyy turned the stable linear law into a negative pitch
     stiffness, 0.48 q S c / Iyy = 33.1 1/s2 at 30 m/s, larger than the controller's 25 1/s2.
  2. Chord. The linear law is a trim line on the mean aerodynamic chord, 0.6514 m (stability.mac()), not 0.62 m.
  3. Lift slope. CL_alpha = 3.866 /rad, the vortex-lattice slope the linear law is built on (0.48 = 0.125 x 3.866),
     not the lifting-line 2 pi / (1 + 2/AR) = 4.72 /rad.
  4. End attitude. The reference profile ends at the level-cruise trim attitude, pi/2 - C_L,cruise / CL_alpha
     (83.34 deg for the 50 kg design), not with the body horizontal (90 deg), where this model's wing carries no lift.
  5. Run length. The run continues 40 s after the profile ends; the submitted run stopped at 4 t_r = 8 s, before the
     motion had settled. Pitching back past hover (theta < -90 deg) also counts as tumbling.
  New outputs: the largest fall from an earlier high point (dusus), the peak incidence, the peak demanded moment,
  the time and altitude at which 95 % of cruise speed is first reached, and whether the run has settled.
  "90 dereceye varmak" above now reads "reaching the trim attitude".
"""
import math

import numpy as np

RHO, G = 1.225, 9.81
D2R = math.pi / 180.0


def catlak_cm(model, alfa, ofset=0.0, cm0=0.056, cma=-0.48):
    """Oduncu alinan C_m(alfa) modelleri. alfa radyan. C_m nose-up positive, on the MAC, about the CG."""
    if model == "sifir":
        return 0.0 * alfa
    if model == "dogrusal":
        return cm0 + cma * alfa          # the paper's law: 0.056 - 0.48 alpha
    if model == "levha":
        # ince levha: merkez basinc 0.25c'den 0.5c'ye kayar -> burun asagi
        return -0.25 * np.sin(2 * alfa)
    if model == "kaydirma":
        return 0.0 * alfa + ofset
    raise ValueError(model)


def trim_attitude(m, S, Vcr, CLa, **_):
    """Body angle theta (0 hover, pi/2 body horizontal) of level flight at Vcr with lift = weight."""
    return math.pi / 2 - m * G / (0.5 * RHO * Vcr ** 2 * S) / CLa


def kos(m, S, c_ort, Iyy, AR, CLa, M_kontrol, tr, Vcr, w0=5.0,
        model="sifir", ofset=0.0, CD0=0.0248, e=0.85,
        astall=12 * D2R, dt=1e-4, profil="bang", kp=25.0, kd=10.0,
        t_after=40.0, cm0=0.056, cma=-0.48):
    """Uc serbestlikli gecis. Govde acisi KOMUT EDILIR, surulmez.

    Kontrolcu: istenen theta(t) profiline PD ile oturur, ama urettigi
    moment M_kontrol ile SINIRLIDIR. Doyma olursa kaydedilir -- kinematik
    benzetimde gorunmeyen sey tam olarak budur.
    Integrator: semi-implicit Euler (velocities first, then positions with the new velocities), dt 1e-4 s.
    """
    W = m * G
    th_end = trim_attitude(m, S, Vcr, CLa)                 # REVISION 4
    vx, vh = 0.0, w0
    th, q = 0.0, 0.0
    t, h = 0.0, 0.0
    en_dusuk, doyma, ulasti = 0.0, 0.0, False
    tepe, dusus, al_max, M_ist_max = 0.0, 0.0, 0.0, 0.0
    t_cr, h_cr = None, None
    Tmax = 1.066 * W                                   # 3.15: ulasilabilir
    while t <= tr + t_after:                           # REVISION 5
        V = math.hypot(vx, vh)
        tau = min(t / tr, 1.0)
        if profil == "bang":
            f = 2 * tau ** 2 if tau <= 0.5 else 1 - 2 * (1 - tau) ** 2
        elif profil == "dogrusal":
            f = tau                      # 3.15'in kendi profili
        else:
            f = 3 * tau ** 2 - 2 * tau ** 3
        th_ref = th_end * f
        q_ref = 0.0
        # PD, sonlu otorite
        M_ist = Iyy * (kp * (th_ref - th) + kd * (q_ref - q))
        M = max(-M_kontrol, min(M_kontrol, M_ist))
        if abs(M_ist) > M_kontrol:
            doyma += dt
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
            if model != "dogrusal" else float(catlak_cm(model, al, ofset, cm0, cma))
        M_aero = qd * S * c_ort * Cm
        Th = Tmax if V < Vcr or vx < Vcr * 0.95 else min(Tmax, Dg)
        vx += ((Th * bx - L * uh - Dg * ux) / m) * dt
        vh += ((Th * bh + L * ux - Dg * uh) / m - G) * dt
        q += (M - M_aero) / Iyy * dt                    # REVISION 1: +theta nose-down, C_m nose-up positive
        th += q * dt
        h += vh * dt
        en_dusuk = min(en_dusuk, h)
        tepe = max(tepe, h)
        dusus = max(dusus, tepe - h)
        al_max = max(al_max, aa)
        M_ist_max = max(M_ist_max, abs(M_ist))
        if t_cr is None and vx >= 0.95 * Vcr:
            t_cr, h_cr = t, h
        if th >= th_end - 1e-3:
            ulasti = True
        t += dt
        if th > math.pi or th < -math.pi / 2:           # kontrolden cikti (REVISION 5: backwards too)
            return dict(kayip=en_dusuk, dusus=dusus, doyma=doyma, ulasti=False, oturdu=False,
                        theta_son=th / D2R, theta_trim=th_end / D2R, firladi=True, t_son=t, vh_son=vh, q_son=q / D2R,
                        al_max=al_max / D2R, M_ist_max=M_ist_max, t_cr=t_cr, h_cr=h_cr)
    oturdu = abs(th - th_end) < 2 * D2R and abs(q) < D2R and vh > -0.1
    return dict(kayip=en_dusuk, dusus=dusus, doyma=doyma, ulasti=ulasti, oturdu=oturdu,
                theta_son=th / D2R, theta_trim=th_end / D2R, firladi=False, t_son=t, vh_son=vh, q_son=q / D2R,
                al_max=al_max / D2R, M_ist_max=M_ist_max, t_cr=t_cr, h_cr=h_cr)


# REVISION 2 and 3: chord = MAC (stability.mac(), 0.6514 m; the heavy design's scaled by sqrt(22.24/1.979)),
# CL_alpha = the vortex-lattice 3.866 /rad (the heavy design is the same planform scaled).
HAFIF = dict(m=50.0, S=1.979, c_ort=0.65137, Iyy=9.81, AR=6.03, CLa=3.866, Vcr=30.0)
AGIR = dict(m=1000.0, S=22.24, c_ort=2.1836, Iyy=2503.0, AR=6.0, CLa=3.866, Vcr=40.0)


def basli(s):
    print("\n" + s)
    print("-" * len(s))


if __name__ == "__main__":
    print("TRANSITION WITH ROTATIONAL DYNAMICS -- sensitivity to the borrowed C_m (corrected model, see REVISION)")
    print("Not a prediction. Entry climb 5 m/s; PD Kp 25, Kd 10 with the moment limit; run 40 s after the profile.")
    print("loss = lowest altitude below entry; fall = largest fall from an earlier high point;")
    print("end = settled (within 2 deg of the trim attitude, pitch rate below 1 deg/s, not sinking) or TUMBLES.")

    for ad, G_, tr, Mk in (("light 50 kg, t_r = 2 s, M = 23.0 N m", HAFIF, 2.0, 23.0),
                           ("light 50 kg, conservative thrust, M = 17.6 N m", HAFIF, 2.0, 17.6),
                           ("heavy 1000 kg, t_r = 5.1 s, M = 952 N m", AGIR, 5.1, 952.0)):
        basli(ad + "   (trim attitude %.2f deg)" % (trim_attitude(**G_) / D2R))
        print("%-18s %8s %8s %8s %9s %8s  %s"
              % ("C_m model", "loss m", "fall m", "sat s", "alpha max", "theta", "end"))
        for model, ofset, etiket in (("sifir", 0, "zero"),
                                     ("dogrusal", 0, "linear (VLM)"),
                                     ("levha", 0, "flat plate"),
                                     ("kaydirma", +0.05, "constant +0.05"),
                                     ("kaydirma", -0.05, "constant -0.05"),
                                     ("kaydirma", +0.10, "constant +0.10"),
                                     ("kaydirma", -0.10, "constant -0.10")):
            r = kos(M_kontrol=Mk, tr=tr, model=model, ofset=ofset, **G_)
            end = ("TUMBLES at %.2f s" % r["t_son"]) if r["firladi"] else (
                "settled" if r["oturdu"] else "NOT settled (vh %+.2f m/s at the end)" % r["vh_son"])
            print("%-18s %8.2f %8.2f %8.2f %9.1f %8.1f  %s"
                  % (etiket, -r["kayip"], r["dusus"], r["doyma"], r["al_max"], r["theta_son"], end))
