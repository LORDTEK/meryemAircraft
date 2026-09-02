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
                 dy_sabit=True, normal="kesit",
                 uc_uzanim=0.0, n_uc=0, n_kapak=16):
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
        self.gecis = 0.3
        self._dag = None
        # normal: duvardan yurumeye hangi dogrultuyla baslanacagi.
        #   "kesit" -> her istasyonun KENDI 2-B normali (ilk surum)
        #   "3b"    -> lofte edilmis yuzeyin gercek 3-B normali
        #   "ortak" -> butun istasyonlarda AYNI (ortalama) 2-B normal
        # Uc secenek de olculdu; sonuclar dogrulama.md'de.
        self.normal = normal
        # Uzak alan merkezi ve cikis duzlemi MUTLAK: kok kesitinin ceyrek
        # veterinden ve kok firar kenarindan olculuyor, butun istasyonlarda
        # ayni.
        # --- UC KAPAGI (duz kapak) ---
        #
        # Kanat ucta biter ama AKIS bitmez: uctan disarida da akiskan var
        # ve profil deligi orada KAPANMALIDIR. Tek bloklu C-agi yiginı bu
        # topoloji degisimini ifade edemez, o yuzden ikinci bir blok
        # ekleniyor:
        #
        #   - Uc duzleminden disariya n_uc istasyon daha (hepsi UC KESITI
        #     geometrisiyle; orada kanat yok, profil cizgisi artik duvar
        #     degil IC cizgidir).
        #   - Profil kesitini dolduran bir IC BLOK (H-agi): alt yuzeydeki
        #     m'inci nokta ile ust yuzeydeki NF-m'inci nokta AYNI x'te
        #     oldugu icin (olculdu: 65 indeksin 65'i) ikisi arasi duzgun
        #     bolunebiliyor.
        #   - Bu ic blogun UC DUZLEMINDEKI tabani KAPAK DUVARIDIR.
        #
        # Hucum ve firar kenarinda alt ile ust ayni noktaya dustugu icin
        # oradaki hucreler HEXA degil PRIZMA olarak yazilir; tekrar eden
        # dugumle hexa yazmak sifir alanli yuz uretirdi.
        self.n_kapak = n_kapak
        self.kw = len(self.istasyon)          # kanat istasyonu sayisi
        if uc_uzanim > 0 and n_uc > 0:
            zt, xt, ct, tt = self.istasyon[-1]
            d0 = self.istasyon[-1][0] - self.istasyon[-2][0]
            # ilk adim kanadin son adimina esit, sonra geometrik buyume
            # Buyume orani IKIYE BOLEREK cozuluyor. Onceki surum r'yi
            # 0,01'lik adimlarla ariyordu ve yakinsamiyordu: istenen 20
            # uzanim icin 7,68 uretti.
            lo, hi = 1.0, 3.0
            for _ in range(200):
                r = (lo + hi) / 2
                if sum(d0 * r ** i for i in range(n_uc)) < uc_uzanim:
                    lo = r
                else:
                    hi = r
            r = (lo + hi) / 2
            zz = zt
            for i in range(n_uc):
                zz += d0 * r ** i
                self.istasyon.append((zz, xt, ct, tt))

        z0, x0, c0, _t0 = self.istasyon[0]
        self._xc_abs = x0 + 0.25 * c0
        self._cikis_abs = x0 + c0 + Xiz
        self._dy_ort = ilk_hucre_yuksekligi(
            Re, yplus, min(s[2] for s in self.istasyon))

    # ---- duzlemler
    def duzlemler(self):
        """Her istasyon icin MUTLAK koordinatta nokta izgarasi.

        Doner: (duzlem, NI, NJ). duzlem[k][i][j] = (x, y, z) -- z ARTIK
        istasyon duzlemine bagli degil; 3-B yurume onu oynatir.

        NEDEN 3-B YURUME. Kesit duzleminde yurumek, kalinlik aciklik
        boyunca degistiginde bozuk ag veriyordu. Olculdu: yalnizca ok
        acisi ya da yalnizca sivrilme degistiginde kusur YOK; yalnizca
        kalinlik degistiginde binlerce bozuk hucre. Sebep, yuzeyin kendi
        normali dogrultusunda kaymasi: x = 0,3'te komsu istasyonlar arasi
        kayma 0,0143 iken duvar hucresi 8,9e-6, yani ~1600 kat.

        Bir bozuk hucrenin koseleri incelendiginde goruldu ki hucre
        GERCEKTE ters degil (ideal paralelyuzlu hacmi pozitif); j yonu
        vektoru komsu istasyonlar arasinda ~0,6 derece DONUYOR ve hucre
        o incelikte oldugu icin yuz CARPIK cikiyor. Hacmi negatif yapan
        bu carpiklik.

        Cozum: duvar bolgesinde yurume, kesit duzlemindeki 2-B normal
        yerine lofte edilmis yuzeyin GERCEK 3-B normali boyunca baslar.
        Boylece j cizgileri komsu istasyonlarda ayni yuzeye dik olur ve
        aralarindaki donme kaybolur.

        Iki yerde 3-B normal KULLANILMAZ ve bunun sebebi var:
          - iz kesiginde: orada ust ve alt ayni noktada; egilirse ikisi
            ayrilir ve kesik ic yuz olmaktan cikar.
          - k = 0 ve k = NK-1 duzlemlerinde: o yamalar symmetryPlane
            olacak, duz kalmalari gerekir.
        """
        pr, NI, NJ = [], None, None
        for (z, xle, veter, tc) in self.istasyon:
            ag = CAgi(kod=tc, Re=self.Re, yplus=self.yplus,
                      R=self.R / veter, Xiz=self.Xiz / veter,
                      n_profil=self.NF, n_normal=self.NJ, n_iz=self.NW,
                      profil_x=self._dagilim())
            ag.dy = (self._dy_ort if self.dy_sabit
                     else ilk_hucre_yuksekligi(self.Re, self.yplus, veter)) / veter
            # UZAK ALAN SABIT TUTULUR -- kanatla birlikte ok acisi yapmaz.
            #
            # CAgi dis cemberi birim veterde 0,25'te merkezler; olcekleyince
            # merkez xle + 0,25c'ye gider, yani uzak sinir da kanadi izler.
            # Istasyonlar arasi kayma boylece 0,13 oluyordu, aciklik adimi
            # ise 0,144 -- neredeyse esit. Uzak alandaki aciklik yuzleri o
            # yuzden 42 dereceye varan egimle duruyor ve dikey olmayanligi
            # yukari cekiyordu.
            #
            # Olculdu: siddetli dikey olmayan yuzlerin %98'i ACIKLIK yuzu ve
            # veter ortasindan ortanca uzakligi 29 veter -- yani kanadin
            # yaninda degil, uzak alanda. Merkez mutlaklastirildi.
            ag.xc = (self._xc_abs - xle) / veter
            # Cikis duzlemi de mutlak: (xle + veter) + Xiz olacak yerde
            # sabit bir x'te dursun.
            ag.Xiz = (self._cikis_abs - (xle + veter)) / veter
            p = ag.parcalar()
            if NI is None:
                NI, NJ = p["NI"], len(p["f"][0])
            elif (p["NI"], len(p["f"][0])) != (NI, NJ):
                raise RuntimeError("istasyonlar farkli izgara boyutu verdi")
            pr.append((p, z, xle, veter))

        NK = len(pr)
        # --- mutlak ic ve dis egriler
        IC = [[(xle + veter * p["ic"][i][0], veter * p["ic"][i][1], z)
               for i in range(NI)] for (p, z, xle, veter) in pr]
        DIS = [[(xle + veter * p["dis"][i][0], veter * p["dis"][i][1], z)
                for i in range(NI)] for (p, z, xle, veter) in pr]
        N2 = [[(p["n"][i][0], p["n"][i][1], 0.0) for i in range(NI)]
              for (p, z, xle, veter) in pr]

        # --- 3-B yuzey normali (yalnizca profil araliginda)
        prof = range(self.NW, self.NW + self.NF + 1)
        N3 = [[N2[k][i] for i in range(NI)] for k in range(NK)]

        if self.normal == "ortak":
            # Butun istasyonlarda AYNI dogrultu: j cizgileri birbirine tam
            # paralel olur, aralarinda donme kalmaz, dolayisiyla yuz
            # carpikligi da kalmaz. Bedeli, kesit sekli degistikce duvar
            # dikliginden sapmaktir -- ama sapma sinirlidir ve olculebilir.
            for i in range(NI):
                sx = sum(N2[k][i][0] for k in range(NK))
                sy = sum(N2[k][i][1] for k in range(NK))
                L = math.hypot(sx, sy) or 1.0
                for k in range(NK):
                    N3[k][i] = (sx / L, sy / L, 0.0)
            return self._yuru(pr, IC, DIS, N3, NI, NJ)

        if self.normal != "3b":
            return self._yuru(pr, IC, DIS, N3, NI, NJ)

        for k in range(NK):
            if k == 0 or k == NK - 1:
                continue                      # kok/uc duz kalir
            for i in prof:
                if i == 0 or i == NI - 1:
                    continue
                a = IC[k][i - 1]; b = IC[k][i + 1]
                c = IC[k - 1][i]; d = IC[k + 1][i]
                t1 = [b[m] - a[m] for m in range(3)]      # veter yonu
                t2 = [d[m] - c[m] for m in range(3)]      # aciklik yonu
                v = [t2[1]*t1[2] - t2[2]*t1[1],
                     t2[2]*t1[0] - t2[0]*t1[2],
                     t2[0]*t1[1] - t2[1]*t1[0]]
                L = math.sqrt(sum(q*q for q in v))
                if L <= 0:
                    continue
                v = [q / L for q in v]
                # Isaret 2-B normalden alinir: disari bakmali.
                if sum(v[m] * N2[k][i][m] for m in range(3)) < 0:
                    v = [-q for q in v]
                N3[k][i] = tuple(v)

        return self._yuru(pr, IC, DIS, N3, NI, NJ)

    def _yuru(self, pr, IC, DIS, N3, NI, NJ):
        NK = len(pr)
        gec = self.gecis
        duzlem = []
        for k in range(NK):
            p = pr[k][0]
            sut_i = []
            for i in range(NI):
                d = math.dist(IC[k][i], DIS[k][i])
                e = [(DIS[k][i][m] - IC[k][i][m]) / d for m in range(3)]
                n0 = N3[k][i]
                sut = []
                for ff in p["f"][i]:
                    b = ff * (d + gec) / (ff * d + gec)
                    v = [(1.0 - b) * n0[m] + b * e[m] for m in range(3)]
                    L = math.sqrt(sum(q*q for q in v)) or 1.0
                    sut.append(tuple(IC[k][i][m] + d * ff * v[m] / L
                                     for m in range(3)))
                sut_i.append(sut)
            duzlem.append(sut_i)
        return duzlem, NI, NJ

    def _dagilim(self):
        """Veter dagilimi BIR KEZ, en kalin kesitten uretilir ve butun
        istasyonlara aynen verilir; boylece i cizgileri her istasyonda ayni
        x'te durur (gercek loft cizgisi)."""
        if getattr(self, "_dag", None) is None:
            en_kalin = max(s[3] for s in self.istasyon)
            oncu = CAgi(kod=en_kalin, Re=self.Re, yplus=self.yplus,
                        R=self.R, Xiz=self.Xiz, n_profil=self.NF,
                        n_normal=self.NJ, n_iz=self.NW)
            self._dag = oncu.veter_dagilimi()
        return self._dag

    # ---- yazim
    def yaz(self, yol):
        duzlem, NI, NJ = self.duzlemler()
        NK = len(self.istasyon)

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
        no = [[[dn(*duzlem[k][i][j]) for j in range(NJ)]
               for i in range(NI)] for k in range(NK)]

        hexler, prizmalar = [], []
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
                    if (j == 0 and prof_bas <= i < prof_son
                            and k < self.kw - 1):
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

        # --- IC BLOK (uc kapagi) ---
        # k = kw-1 .. NK-1 arasinda profil kesitini doldurur; kw-1
        # duzlemindeki tabani KAPAK DUVARIDIR.
        if self.kw < NK:
            M = self.NF // 2
            NC = self.n_kapak
            kap = {}
            for k in range(self.kw - 1, NK):
                for m in range(M + 1):
                    L = duzlem[k][prof_bas + m][0]
                    U = duzlem[k][prof_son - m][0]
                    for q in range(NC + 1):
                        t = q / float(NC)
                        kap[(k, m, q)] = dn(*[L[c] + t * (U[c] - L[c])
                                              for c in range(3)])
            for k in range(self.kw - 1, NK - 1):
                for m in range(M):
                    for q in range(NC):
                        # SARIM YONU: once +q (alttan uste), sonra +m (firar
                        # kenarindan hucum kenarina). Ilk surumde tersiydi --
                        # (+m)x(+q) ekseni -z'ye bakiyordu, oysa hucrenin
                        # "ustu" +k = +z. Butun kapak hucreleri SOL ELLI
                        # cikiyor ve hacimleri negatif oluyordu (olculdu:
                        # 462 hucre, carpiklik 3,9e15).
                        a = kap[(k, m, q)];         b = kap[(k, m, q + 1)]
                        c = kap[(k, m + 1, q + 1)]; d = kap[(k, m + 1, q)]
                        e = kap[(k + 1, m, q)];     f = kap[(k + 1, m, q + 1)]
                        g = kap[(k + 1, m + 1, q + 1)]; h = kap[(k + 1, m + 1, q)]
                        if a == b:            # firar kenari ucu (m=0) capraz
                            prizmalar.append((a, c, d, e, g, h))
                            taban, ust = (a, c, d), (e, g, h)
                        elif c == d:          # hucum kenari ucu (m=M)
                            prizmalar.append((a, b, c, e, f, g))
                            taban, ust = (a, b, c), (e, f, g)
                        else:
                            hexler.append((a, b, c, d, e, f, g, h))
                            taban, ust = (a, b, c, d), (e, f, g, h)
                        if k == self.kw - 1:
                            yuzler["duvar"].append(taban)   # KAPAK DUVARI
                        if k == NK - 2:
                            yuzler["uc"].append(ust)

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
              str(len(hexler) + len(prizmalar)
                  + sum(len(v) for v in yuzler.values()))]
        e = 0
        for i, a in enumerate(ad):
            for yz in yuzler[a]:
                e += 1
                # gmsh: 3 = dortgen, 2 = ucgen
                L.append("%d %d 2 %d %d %s" % (e, 3 if len(yz) == 4 else 2,
                                               i + 1, i + 1,
                                               " ".join(map(str, yz))))
        for hx in hexler:
            e += 1
            L.append("%d 5 2 %d %d %s" % (e, len(ad) + 1, len(ad) + 1,
                                          " ".join(map(str, hx))))
        for pz in prizmalar:                       # gmsh: 6 = prizma
            e += 1
            L.append("%d 6 2 %d %d %s" % (e, len(ad) + 1, len(ad) + 1,
                                          " ".join(map(str, pz))))
        L += ["$EndElements", ""]
        open(yol, "w").write("\n".join(L))
        return dict(dugum=len(sira), hucre=len(hexler) + len(prizmalar),
                    hexa=len(hexler), prizma=len(prizmalar),
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
