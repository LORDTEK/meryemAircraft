# -*- coding: utf-8 -*-
"""Uc boyutlu kanat agi: DOGRULANMIS iki boyutlu C-agini aciklik boyunca yigar.

NEDEN BOYLE. Iki boyutlu C-agi uretecinin (ortak/cagi.py) urettigi cozumler
iki bagimsiz referans kodla profil duzeyinde eslesti: duz levhada u+ ±0,06
icinde, NACA 0012 yuzey Cf'inde 91 duvar yuzunun %91'i Overflow ile Cfl3d
arasinda kaldi. O uretecin geometri mantigini (duvar dikligi, iz kesigi,
firar kenari yumusatmasi, en-boy sinirlamasi) YENIDEN YAZMAK, dogrulanmis
olani atip yerine dogrulanmamis bir sey koymak olurdu. Bunun yerine ayni
sinif her aciklik istasyonunda cagriliyor ve duzlemler birbirine baglaniyor.

Boylece uc boyutta yeni olan tek sey, istasyonlar ARASINDAKI baglantidir --
ve dogrulanmasi gereken de yalnizca odur.

ISTASYON YERLESIMI. CAgi birim veterde calisir. Bir istasyonu yerine koymak
icin noktalar yerel vetere olceklenir ve hucum kenari x'ine otelenir. Uzak
alan ve iz uzunlugu ise MUTLAK tutulur (yerel vetere bolunerek CAgi'ye
verilir); aksi halde uzak sinir kanatla birlikte daralir ve uc istasyonunda
govdeye kok istasyonundakinden cok daha yakin gecer.

Ilk hucre yuksekligi de yerel vetere gore hesaplanir: y+ yerel Reynolds
sayisiyla belirlenir, veter kucuduginde dy de kuculmelidir.

YAMALAR
    duvar    kanat yuzeyi (j=0, profil i araligi)
    disalan  uzak sinir (j=NJ-1)
    cikis    C-agi kesiginin iki ucu (i=0 ve i=NI-1)
    kok      k=0 duzlemi
    uc       k=NK-1 duzlemi

kok ve uc'un TIPI burada belirlenmez; vakayi kuran kod karar verir. Sonsuz
kanat sinamasinda ikisi de symmetryPlane'dir ve cozum iki boyutlusuna
esitlenmelidir -- ureteci sinayan test budur.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "ortak"))
from cagi import CAgi, ilk_hucre_yuksekligi          # noqa: E402


def naca_kodu(tc):
    """t/c oranindan dort haneli simetrik NACA kodu ("0012" gibi)."""
    n = int(round(tc * 100))
    if not 1 <= n <= 99:
        raise ValueError("t/c %.4f -> %d, dort haneli koda sigmiyor" % (tc, n))
    return "00%02d" % n


class KanatAgi:
    """istasyon: (z, x_hucum, veter, t/c) dizisi -- kokten uca."""

    def __init__(self, istasyon, Re=6e6, yplus=1.0, R=20.0, Xiz=20.0,
                 n_profil=256, n_normal=96, n_iz=64, veter_ref=1.0,
                 dy_sabit=True):
        if len(istasyon) < 2:
            raise ValueError("en az iki istasyon gerekir")
        z = [s[0] for s in istasyon]
        if any(b <= a for a, b in zip(z, z[1:])):
            raise ValueError("istasyonlar z'ye gore artan olmali")
        self.istasyon = list(istasyon)
        self.Re, self.yplus = Re, yplus
        self.R, self.Xiz = R, Xiz
        self.NF, self.NJ, self.NW = n_profil, n_normal, n_iz
        self.veter_ref = veter_ref
        # dy_sabit: duvar araligi butun istasyonlarda AYNI (mutlak) tutulur.
        #
        # Neden gerekli. Ilk surumde dy yerel vetere gore olcekleniyordu
        # (y+ her istasyonda 1 olsun diye). Duz kanatta sorun yoktu -- butun
        # veterler esit. Gercek planformda veter 0,97'den 0,236'ya iniyor,
        # yani dy dort kat degisiyor; ustelik ok acisi yuzunden istasyonlar
        # arasi YANAL kayma 0,13 civarinda, ki bu duvar hucresinin
        # yuksekliginin ~15 000 kati. Radyal dagilimdaki kucuk uyumsuzluk o
        # kaldiracla buyuyup hucreyi KATLIYOR.
        #
        # Olculdu: dy olceklenince 520 704 hucrenin 6351'i negatif hacimli
        # cikti; hepsi duvara en yakin 14 katmanda (j = 0..13), profilin
        # orta bolgesinde (i = 101..250) ve aciklikta tekduze dagilmis --
        # yani tam da hucrenin ince oldugu yerde.
        #
        # Sabit dy, EN KUCUK vetere gore secilir: boylece y+ hedefi butun
        # aciklik boyunca asilmaz (kokte y+ daha da kucuk olur, ki bu
        # zararsizdir).
        self.dy_sabit = dy_sabit
        self._dy_ort = ilk_hucre_yuksekligi(
            Re, yplus, min(s[2] for s in self.istasyon))

    # ---- duzlemler
    def duzlemler(self):
        """Her istasyon icin MUTLAK koordinatta (x, y) nokta izgarasi.

        Doner: (duzlem_listesi, NI, NJ). duzlem[k][i][j] = (x, y).
        """
        # Veter dagilimi BIR KEZ, en KALIN kesitten uretilir ve butun
        # istasyonlara aynen verilir. Boylece i cizgileri her istasyonda
        # ayni x'te durur (gercek loft cizgisi). En kalin kesit secildi
        # cunku yay uzunlugu orada en buyuktur; ince kesitlerde ayni x
        # dagilimi daha da seyrek kalir, tersi olsaydi sikisirdi.
        en_kalin = max(s[3] for s in self.istasyon)
        oncu = CAgi(kod=en_kalin, Re=self.Re, yplus=self.yplus,
                    R=self.R, Xiz=self.Xiz, n_profil=self.NF,
                    n_normal=self.NJ, n_iz=self.NW)
        dagilim = oncu.veter_dagilimi()

        duzlem, NI, NJ = [], None, None
        for (z, xle, veter, tc) in self.istasyon:
            # Uzak alan ve iz MUTLAK; CAgi birim veterde calistigi icin
            # yerel vetere bolunerek veriliyor.
            # Kalinlik KESIRLI geciriliyor (naca_kodu ile yuvarlanmiyor):
            # gercek planformda t/c kokten uca surekli degisir, tam
            # yuzdeye yuvarlamak istasyonlar arasinda basamak birakirdi.
            ag = CAgi(kod=tc, Re=self.Re, yplus=self.yplus,
                      R=self.R / veter, Xiz=self.Xiz / veter,
                      n_profil=self.NF, n_normal=self.NJ, n_iz=self.NW,
                      profil_x=dagilim)
            # Duvar araligi YEREL veterle: y+ yerel Reynolds'a baglidir.
            # CAgi'nin kendi hesabi birim veter varsayar, o yuzden
            # olcekleme sonrasi dogru cikacak degerle degistiriliyor.
            # CAgi birim veterde calisir; mutlak dy'yi ona bolerek veriyoruz.
            ag.dy = (self._dy_ort if self.dy_sabit
                     else ilk_hucre_yuksekligi(self.Re, self.yplus, veter)) / veter
            P, ni, nj = ag.uret()
            if NI is None:
                NI, NJ = ni, nj
            elif (ni, nj) != (NI, NJ):
                raise RuntimeError(
                    "istasyonlar farkli izgara boyutu verdi: (%d,%d) vs "
                    "(%d,%d) -- yigilamaz" % (ni, nj, NI, NJ))
            duzlem.append([[(xle + veter * P[i][j][0], veter * P[i][j][1])
                            for j in range(nj)] for i in range(ni)])
        return duzlem, NI, NJ

    # ---- yazim
    def yaz(self, yol):
        duzlem, NI, NJ = self.duzlemler()
        z = [s[0] for s in self.istasyon]
        NK = len(z)

        dugum, sira = {}, []

        def dn(x, y, zz):
            k = (round(x, 9), round(y, 9), round(zz, 9))
            if k not in dugum:
                dugum[k] = len(sira) + 1
                sira.append(k)
            return dugum[k]

        # no[k][i][j]. Iz kesiginde ust ve alt ayni koordinattadir; koordinat
        # anahtariyla birlestirildikleri icin orada tek dugum olusur ve kesik
        # IC YUZ olur -- iki boyutlu uretecin davranisinin aynisi.
        no = [[[dn(duzlem[k][i][j][0], duzlem[k][i][j][1], z[k])
                for j in range(NJ)] for i in range(NI)] for k in range(NK)]

        hexler = []
        yuzler = {"duvar": [], "disalan": [], "cikis": [], "kok": [], "uc": []}
        prof_bas, prof_son = self.NW, self.NW + self.NF

        for k in range(NK - 1):
            for i in range(NI - 1):
                for j in range(NJ - 1):
                    a = no[k][i][j];         b = no[k][i + 1][j]
                    c = no[k][i + 1][j + 1]; d = no[k][i][j + 1]
                    e = no[k + 1][i][j];     f = no[k + 1][i + 1][j]
                    g = no[k + 1][i + 1][j + 1]; h = no[k + 1][i][j + 1]
                    hexler.append((a, b, c, d, e, f, g, h))
                    if j == 0 and prof_bas <= i < prof_son:
                        yuzler["duvar"].append((a, b, f, e))
                    if j == NJ - 2:
                        yuzler["disalan"].append((d, c, g, h))
                    if i == 0:
                        yuzler["cikis"].append((a, d, h, e))
                    if i == NI - 2:
                        yuzler["cikis"].append((b, c, g, f))
                    if k == 0:
                        yuzler["kok"].append((a, b, c, d))
                    if k == NK - 2:
                        yuzler["uc"].append((e, f, g, h))

        ad = ["duvar", "disalan", "cikis", "kok", "uc"]
        L = ["$MeshFormat", "2.2 0 8", "$EndMeshFormat",
             "$PhysicalNames", str(len(ad) + 1)]
        for i, a in enumerate(ad):
            L.append('2 %d "%s"' % (i + 1, a))
        L.append('3 %d "ic"' % (len(ad) + 1))
        L.append("$EndPhysicalNames")
        L += ["$Nodes", str(len(sira))]
        for i, (x, y, zz) in enumerate(sira):
            L.append("%d %.10g %.10g %.10g" % (i + 1, x, y, zz))
        L += ["$EndNodes", "$Elements",
              str(len(hexler) + sum(len(v) for v in yuzler.values()))]
        e = 0
        for i, a in enumerate(ad):
            for yz in yuzler[a]:
                e += 1
                L.append("%d 3 2 %d %d %s" % (e, i + 1, i + 1,
                                              " ".join(map(str, yz))))
        for hx in hexler:
            e += 1
            L.append("%d 5 2 %d %d %s" % (e, len(ad) + 1, len(ad) + 1,
                                          " ".join(map(str, hx))))
        L += ["$EndElements", ""]
        open(yol, "w").write("\n".join(L))
        return dict(dugum=len(sira), hucre=len(hexler),
                    NI=NI, NJ=NJ, NK=NK,
                    duvar=len(yuzler["duvar"]))


def duz_kanat(aciklik, nk, kod="0012", **kw):
    """Sabit kesitli, ok acisiz, sivrilmesiz kanat -- ureteci sinamak icin.

    Iki ucta da symmetryPlane ile kosuldugunda cozum IKI BOYUTLUNUN AYNISI
    olmalidir. Ureteci dogrulayan sinama budur.
    """
    tc = int(kod[2:]) / 100.0
    ist = [(aciklik * i / (nk - 1), 0.0, 1.0, tc) for i in range(nk)]
    return KanatAgi(ist, **kw)
