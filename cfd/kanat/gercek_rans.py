# -*- coding: utf-8 -*-
"""GERCEK PLANFORMUN RANS COZUMU -- VLM ile aciklik yuklemesi karsilastirmasi.

AMAC. Dort dis okumanin da istedigi sey: tarafsiz noktayi DEGIL, aciklik
boyunca yukleme ORANINI olcmek.

    K(y) = c_l,RANS(y) / c_l,VLM(y)     ve     K(y) / K_L

K(y)/K_L sabitse hata saf carpansaldir ve makalenin iptal savunmasi
ayakta kalir. Degilse yukleme yeniden dagilmistir; 3.10'un katsayilari
(derece basina %0,15 MAC ve 0,38 derece) onu denge burulmasi hareketine
cevirir ve esik 2,6 derecedir.

NEDEN TARAFSIZ NOKTA DEGIL. Kendi olcumumuz, tarafsiz noktanin savunulabilir
cozucu secimleri arasinda %1,34 MAC sacildigini gosterdi -- agin hareketinin
bes kati. RANS-VLM tarafsiz nokta farki o sacilmanin icinde kalir ve
okunamaz. Dordu de bagimsiz olarak ayni seyi soyledi.

NEDEN BURULMASIZ. Ag ureteci istasyon basina burulma KABUL ETMIYOR: demet
dort alanli (z, x_hucum, veter, t/c). Trimli geometri once ag urecine
yetenek eklenmesini gerektirir. K(y) bir COZUCU CIFTININ ozelligidir,
burulmanin degil; burulmasiz kosu onu o yetenegi beklemeden verir.
Trimli kosu ayri adimdir ve yapilmadan yapilmis sayilmaz.

NEDEN DUVAR FONKSIYONU. Aranan sey yuklemenin SEKLI; bu, sinir tabakasinin
cozunurlugune degil basinc dagilimina baglidir. y+ = 1 agi (1,67 M hucre,
12,3 s/adim, ~14 saat) gecis modeli icin gerekliydi; burada gerekli degil
ve bu konteynerde 4,7 GB bos disk var. 184 bin hucre, duvar fonksiyonu.
Bu bir taviz ve oyle yaziliyor: viskoz surukleme bu kosudan ALINMAZ.
"""
import json, os, subprocess, sys, time

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
from gercek import gercek_istasyonlar                   # noqa: E402
from kanatagi import KanatAgi                           # noqa: E402
from kur3b import kur3b                                 # noqa: E402

V = 30.0
KOK = os.path.join(BURA, "veri", "gercek3b")


# --- AG AYARLARI, HEPSI OLCULDU ------------------------------------
# normal="ortak": kesit normali 104 negatif hucre veriyordu, ortak normal 2.
# firar_taban=4 : SIVRI firar kenari oldurucuydu. Ust ve alt yuzey tek
#   cizgide bulusunca hucre COKUYOR; checkMesh azami en-boy oranini
#   8,2e96 gosteriyordu (sayisal sonsuz) ve simpleFoam kayan nokta
#   istisnasiyla oluyordu. Kut tabanli firar kenariyla en-boy orani 5000,
#   negatif hucre SIFIR, dikey olmayanlik 116 -> 80,5.
#   Kusur uc kapaginda DEGILDI: kapak kapatilinca negatif hucre 2'den
#   1306'ya cikiyor, yani kapak zaten isini yapiyordu.
def kur(alfa, n_ist=20, nf=128, nn=48, ni=32, yplus=60.0, firar_taban=4):
    ist, yari = gercek_istasyonlar(n=n_ist, sikistir=True)
    ag = KanatAgi(ist, Re=1.3e6, yplus=yplus, normal="ortak",
                  firar_taban=firar_taban,
                  n_profil=nf, n_normal=nn, n_iz=ni)
    v = os.path.join(KOK, "alfa%.1f" % alfa)
    os.makedirs(KOK, exist_ok=True)
    b = kur3b(v, ag, kok="symmetryPlane", uc="serbest",
              alfa=alfa, Re=1.3e6, kod="0012")
    return v, b, yari


if __name__ == "__main__":
    alfa = float(sys.argv[1]) if len(sys.argv) > 1 else 6.69
    cek = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    t = time.time()
    v, b, yari = kur(alfa)
    print("vaka: %s" % v)
    print("hucre %d  (%dx%dx%d), duvar yuzu %d, yari aciklik %.4f"
          % (b["hucre"], b["NI"], b["NJ"], b["NK"], b["duvar"], yari))
    print("kurulum %.1f s" % (time.time() - t))
    print("alfa %.2f der, U %.1f m/s" % (alfa, V))
