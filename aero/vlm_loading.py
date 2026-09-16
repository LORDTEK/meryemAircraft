# -*- coding: utf-8 -*-
"""VLM'in aciklik boyunca yuklemesi -- RANS ile karsilastirmanin TABANI.

NE ICIN. Dort dis okuma da ayni seyi istedi: tarafsiz noktayi DEGIL,
aciklik boyunca yukleme ORANINI karsilastir.

    K(y) = c_l,RANS(y) / c_l,VLM(y)   ve   K(y) / K_L

K(y)/K_L sabitse hata saf carpansal ve makalenin iptal savunmasi ayakta;
degilse yukleme yeniden dagilmis demektir ve 3.10'un duyarlilik
katsayilari o yeniden dagilimi denge burulmasi hareketine cevirir.

GEOMETRI SECIMI. BURULMASIZ planform. Sebep: ag ureteci istasyon basina
burulma KABUL ETMIYOR (demet dort alanli: z, x_hucum, veter, t/c), yani
trimli geometri icin once ag urecine yetenek eklenmesi gerek. Burulmasiz
karsilastirma o yetenegi beklemeden K(y)'yi verir ve K(y) bir COZUCU
ciftinin ozelligidir, burulmanin degil. Trimli kosu ayri adim.
"""
import json, os, sys
import numpy as np
import aerosandbox as asb

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
import stability as K

V, CL_HEDEF = 30.0, 0.45


def coz(alfa):
    o = K.olcuier()
    ac = asb.Airplane(wings=[K.kanat_kur(None)], s_ref=o["alan"],
                      b_ref=o["aciklik"], c_ref=K.mac()[0], xyz_ref=[0, 0, 0])
    v = asb.VortexLatticeMethod(
        airplane=ac, op_point=asb.OperatingPoint(velocity=V, alpha=alfa),
        spanwise_resolution=K.SPAN_COZ, chordwise_resolution=K.VETER_COZ)
    return v, v.run()


def alfa_icin_CL(hedef=CL_HEDEF):
    """Ikiye bolme -- dogrusal aradegerleme DEGIL (proje kurali)."""
    alt, ust = -4.0, 14.0
    for _ in range(16):
        orta = 0.5 * (alt + ust)
        if coz(orta)[1]["CL"] < hedef:
            alt = orta
        else:
            ust = orta
    return 0.5 * (alt + ust)


def aciklik_yuklemesi(v, alfa, _n=None):
    """Panel kuvvetlerini GERCEK aciklik SERITLERINE topla -> c_l * c (y).

    Ilk surum tekduze kutulara topluyordu ve dagilim tirtikliydi: kutular
    panel istasyonlariyla hizali olmadigi icin kimi kutu fazla, kimi az
    panel yakaliyordu. Tirtik fizik degil, kutulama kusuruydu.

    Burada seritler panellerin KENDI aciklik istasyonlaridir: ayni y'deki
    paneller (bir seridin veter boyunca dilimleri) toplanir ve seridin
    kendi genisligine bolunur. Kutu sayisi diye bir sey YOK.
    """
    F = np.array(v.forces_geometry)
    if F.shape[0] == 3:
        F = F.T
    mrk = np.array(v.vortex_centers)
    if mrk.shape[0] == 3:
        mrk = mrk.T
    # Kanat symmetric=True: paneller ZATEN iki yarida da var. Ilk surum
    # |y|'ye katlayip bir de ikiyle carpiyordu ve C_L'yi tam iki kat
    # veriyordu; sinama yakaladi.
    y = mrk[:, 1]
    # Kaldirma RUZGAR ekseninde; forces_geometry govde ekseninde.
    ar = np.radians(alfa)
    Fz = F[:, 2] * np.cos(ar) - F[:, 0] * np.sin(ar)

    anah = np.round(y, 9)
    ist = np.unique(anah)
    guc = np.array([Fz[anah == a].sum() for a in ist])

    # Serit genisligi: komsu istasyonlarin orta noktalari arasi.
    kenar = np.empty(len(ist) + 1)
    kenar[1:-1] = 0.5 * (ist[:-1] + ist[1:])
    kenar[0] = ist[0] - (kenar[1] - ist[0])
    kenar[-1] = ist[-1] + (ist[-1] - kenar[-2])
    gen = np.diff(kenar)

    q = 0.5 * 1.225 * V * V
    clc = guc / (q * gen)
    # Iki yarim simetrik: sag yariyi dondur.
    sag = ist > 0
    return ist[sag], clc[sag], gen[sag], float(ist.max())


if __name__ == "__main__":
    a = alfa_icin_CL()
    v, r = coz(a)
    o = K.olcuier()
    print("BURULMASIZ planform, C_L = %.4f'te alfa = %.4f der" % (r["CL"], a))
    yy, clc, gen, yari = aciklik_yuklemesi(v, a)

    # SINAMA: yuklemenin integrali cozucunun kendi C_L'sini vermeli.
    CL_int = 2.0 * np.sum(clc * gen) / o["alan"]
    print("integralden C_L = %.4f, cozucunun C_L'si = %.4f, fark %.2f %%"
          % (CL_int, r["CL"], 100 * (CL_int - r["CL"]) / r["CL"]))
    if abs(CL_int - r["CL"]) > 0.02 * abs(r["CL"]):
        sys.exit("!! DUR -- aciklik toplamasi cozucunun C_L'sini uretmiyor.")

    json.dump(dict(alfa=a, CL=float(r["CL"]), Cm=float(r["Cm"]),
                   CD=float(r["CD"]), y=list(map(float, yy)),
                   clc=list(map(float, clc)), gen=list(map(float, gen)),
                   yari=float(yari),
                   S=o["alan"], b=o["aciklik"], MAC=K.mac()[0], V=V),
              open(os.path.join(BURA, "vlm_loading.json"), "w"), indent=1)
    print("\n%d aciklik seridi" % len(yy))
    print("%-8s %12s" % ("eta", "c_l*c (m)"))
    for i in range(0, len(yy), max(1, len(yy) // 12)):
        print("%-8.3f %12.4f" % (yy[i] / yari, clc[i]))
    print("\nvlm_loading.json yazildi")
