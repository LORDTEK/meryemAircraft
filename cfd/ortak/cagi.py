# -*- coding: utf-8 -*-
"""Iki boyutlu C-tipi yapisal cozum agi ureteci.

Neden elle uretiliyor: surukleme, duvar kayma gerilmesinin yuzey uzerindeki
integralidir; duvara komsu hucrenin yuzeye DIK olmasi dogrudan dogruya
sonucun dogrulugudur. blockMesh'in duz kenarlari bu dikligi vermez,
snappyHexMesh ise sinir tabakasi katmanlarini yamali birakir. Yapisal bir
C-agi ikisini de cozer.

Neden C-agi, O-agi degil: iz bolgesinin cozunurlugu suruklemede belirleyici.
C-agi izi kendi blok yonunde tasir; sayisal yayilma ize dik degil paralel
olur.

Topoloji -- tek bir yapisal blok, (i, j):

    j = 0        : ic egri  = [alt iz] + [profil: FK->HK->FK] + [ust iz]
    j = NJ-1     : dis sinir = [alt cizgi] + [cember] + [ust cizgi]
    i = 0, NI-1  : cikis duzleminin iki yarisi

Iz kesigi (j = 0 uzerinde profil disinda kalan y = 0 parcasi) alttan ve
ustten AYNI noktalara denk gelir; dugumler koordinata gore birlestirildigi
icin orada ic yuz olusur ve akis surekli kalir. C-aginin "wrap" ozelligi
budur.

Disari dogru yurume, yonu duvar normali n'den dis sinir dogrultusu e'ye,
SABIT BIR FIZIKSEL UZUNLUKTA (gecis, ~0.3 veter) dondurur:

    b(f) = f (d + gecis) / (f d + gecis)        b(0) = 0 , b(1) = 1
    P(i,j) = ic(i) + d(i) * f(j) * normalize( (1-b) n(i) + b e(i) )

b(0) = 0 duvarda dikligi, b(1) = 1 noktanin dis sinira tam oturmasini
verir. f dagilimi geometriktir; ilk hucre y+ hedefinden gelir.

Firar kenarinda normal alani sureksizdir (iz kesiginin normali dikey, alt
yuzeyinkiyse kapali NACA 0012'de ~8 derece yatik). Bu sicrama, aradaki
hucre 2e-4 veter oldugu icin komsu isinsal cizgileri kesistirir. Normal
alani yalnizca firar kenari cevresindeki dar bir pencerede yumusatilir --
bastan sona yumusatmak hucum kenarinda duvar dikligini bozar (olculdu:
0,4 dereceden 10 dereceye).

Bu kurulumda 385 x 97 dugumde ters donmus hucre YOKTUR ve duvarda
diklikten sapma ortalama 0,9 / en fazla 3,5 derecedir.

Cikti: gmsh 2.2 ASCII .msh -> gmshToFoam.
"""
import math


# ------------------------------------------------------------------ profil

def naca4(kod, x, kapali=True):
    """4 haneli simetrik NACA profilinin yari kalinligi.

    kapali=True son katsayiyi -0.1036 yapar: firar kenari sifir kalinlikta
    kapanir. Ruzgar tuneli modelleri ve turbulans modeli kaynaklari bu
    surumu kullanir. -0.1015 gercek NACA tanimidir ve firar kenarini
    %0.25 veter acik birakir.
    """
    t = int(kod[-2:]) / 100.0
    c4 = -0.1036 if kapali else -0.1015
    return 5 * t * (0.2969 * math.sqrt(max(x, 0.0)) - 0.1260 * x
                    - 0.3516 * x ** 2 + 0.2843 * x ** 3 + c4 * x ** 4)


# ------------------------------------------------------- yardimci geometri

def _uzunluk(p):
    """Kumulatif yay uzunlugu, 0..1'e olceklenmis."""
    s = [0.0]
    for i in range(1, len(p)):
        s.append(s[-1] + math.hypot(p[i][0] - p[i - 1][0], p[i][1] - p[i - 1][1]))
    L = s[-1]
    return [v / L for v in s], L


def _ornekle(p, hedef):
    """p poligonunu, normalize yay uzunlugu 'hedef' olan noktalarda ornekler."""
    s, _ = _uzunluk(p)
    cikti, k = [], 0
    for h in hedef:
        while k < len(s) - 2 and s[k + 1] < h:
            k += 1
        araliq = s[k + 1] - s[k]
        w = 0.0 if araliq <= 0 else (h - s[k]) / araliq
        cikti.append((p[k][0] + w * (p[k + 1][0] - p[k][0]),
                      p[k][1] + w * (p[k + 1][1] - p[k][1])))
    return cikti


def _taban(u, oran=0.35):
    """Monoton 0..1 dizisinin araliklarina alt sinir koyar.

    Dis sinir noktalari ic egrinin dagilimini miras alir; ama ic dagilim
    firar kenarinda veterin 1e-5'i kadar sikisir. Bu sikismayi 20 veter
    uzaktaki dis sinira oldugu gibi tasimak, komsu isinsal cizgileri ayni
    noktada bulusturur ve orada hucre ters doner. Her araliga "duzgun
    dagilimin en az 'oran' kadari" tabani konur, sonra yeniden normalize
    edilir: bicim korunur, cokme onlenir.
    """
    n = len(u) - 1
    if n < 1:
        return u
    d = [max(u[i + 1] - u[i], oran / n) for i in range(n)]
    T = sum(d)
    c, x = [0.0], 0.0
    for v in d:
        x += v / T
        c.append(x)
    return c


def _geometrik(n, ilk, toplam):
    """n araliga bolunmus [0, toplam]; ilk aralik 'ilk'. Kumulatif dizi
    doner (n+1 eleman, 0 ile toplam dahil)."""
    if n < 1:
        return [0.0, toplam]
    lo, hi = 1.0 + 1e-12, 3.0
    if ilk * n >= toplam:                     # geometrik gerekmiyor
        return [toplam * i / n for i in range(n + 1)]
    for _ in range(200):
        r = (lo + hi) / 2
        if ilk * (r ** n - 1) / (r - 1) < toplam:
            lo = r
        else:
            hi = r
    r = (lo + hi) / 2
    c, x = [0.0], 0.0
    for i in range(n):
        x += ilk * r ** i
        c.append(x)
    return [v * toplam / c[-1] for v in c]    # yuvarlama artigini kapat


def _iki_uclu(n, ilk, son, toplam):
    """Iki ucu da sikistiran dagilim: tanh benzeri, ilk ve son aralik
    verilen degerlere yakin. Basit ve dayanikli: iki geometrik yarim."""
    a = _geometrik(n // 2, ilk, toplam / 2)
    b = _geometrik(n - n // 2, son, toplam / 2)
    return a[:-1] + [toplam - v for v in reversed(b)]


def ilk_hucre_yuksekligi(Re, yplus=1.0, veter=1.0):
    """Hedef y+ icin duvara komsu hucrenin YUKSEKLIGI.

    y+ = u_tau * y_merkez / nu ,  u_tau = U sqrt(Cf/2) ,  Cf = 0.026 Re^(-1/7)
    Hucre merkezi yuksekligin yarisindadir; bu yuzden 2 ile carpilir.
    """
    cf = 0.026 / Re ** (1.0 / 7.0)
    return 2.0 * yplus * (veter / Re) / math.sqrt(cf / 2.0)


# ------------------------------------------------------------------- ag

class CAgi:
    def __init__(self, kod="0012", Re=6e6, yplus=1.0,
                 R=20.0, Xiz=20.0, kalinlik=1.0, kapali=True,
                 n_profil=256, n_normal=96, n_iz=64,
                 fk_hucre=2e-4, hk_hucre=2e-4, iz_cikis=1.0, dis_hucre=1.5,
                 n_sigma=None, fk_pencere=None, gecis=0.3, en_boy=5000.0):
        self.kod, self.Re, self.kapali = kod, Re, kapali
        self.R, self.Xiz, self.kalinlik = R, Xiz, kalinlik
        self.NF, self.NJ, self.NW = n_profil, n_normal, n_iz
        self.fk, self.hk = fk_hucre, hk_hucre
        self.iz_cikis, self.dis_hucre = iz_cikis, dis_hucre
        # Firar kenarindaki normal sicramasi, yuzey egimiyle buyur: kapali
        # NACA 00xx'te firar acisi %12'de 8,3 derece, %30'da 20 derecedir.
        # Sabit bir yumusatma penceresi kalin kesitlerde yetmez -- olculdu:
        # 0030 ve 0035, pencere 0,02'de sirasiyla 38 ve 138 ters hucre
        # veriyor, 0,04'te sifir. Bu yuzden pencere firar egimiyle
        # olcekleniyor. Taban 0,02'dir ve %12'de tam o degere oturur, yani
        # daha once uretilmis 0012 aglari DEGISMEZ.
        eg = abs(naca4(kod, 1.0, kapali) - naca4(kod, 0.999, kapali)) / 0.001
        eg0 = 0.1454                      # 0012'nin firar egimi
        self.fk_pencere = fk_pencere if fk_pencere is not None else \
            0.02 * max(1.0, eg / eg0)
        self.n_sigma = n_sigma if n_sigma is not None else self.fk_pencere / 2
        self.gecis, self.en_boy = gecis, en_boy
        self.dy = ilk_hucre_yuksekligi(Re, yplus)
        self.xc = 0.25                       # dis cemberin merkezi

    # ---- j = 0 ic egrisi
    def _profil_egrisi(self):
        """FK -> (alt) -> HK -> (ust) -> FK. Her iki ucta da sikistirilmis:
        hucum kenarinda egrilik, firar kenarinda iz baslangici onemli."""
        ince = [(1 - math.cos(math.pi * i / 3000)) / 2 for i in range(3001)]
        alt = [(x, -naca4(self.kod, x, self.kapali)) for x in reversed(ince)]
        ust = [(x, naca4(self.kod, x, self.kapali)) for x in ince]
        ham = alt + ust[1:]                  # HK bir kez
        _, L = _uzunluk(ham)
        yarim = self.NF // 2
        d1 = _iki_uclu(yarim, self.fk / L, self.hk / L, 0.5)          # FK->HK
        d2 = _iki_uclu(self.NF - yarim, self.fk / L, self.hk / L, 0.5)
        hedef = d1[:-1] + [1.0 - v for v in reversed(d2)]
        return _ornekle(ham, hedef), L

    def ic_egri(self):
        """NI = 2*NW + NF + 1 nokta.

        indeks  0 .. NW-1        alt iz  (cikistan FK'ya, FK haric)
        indeks  NW .. NW+NF      profil  (FK -> HK -> FK)
        indeks  NW+NF+1 .. NI-1  ust iz  (FK haric, cikisa)
        """
        X, NW = self.Xiz, self.NW
        prof, _ = self._profil_egrisi()
        c = _geometrik(NW, self.fk, X)                 # NW+1 deger, 0 dahil
        iz_ust = [(1.0 + v, 0.0) for v in c]           # FK -> cikis
        iz_alt = [(1.0 + v, 0.0) for v in reversed(c)]  # cikis -> FK
        return iz_alt[:-1] + prof + iz_ust[1:]

    def dis_egri(self, ic):
        """Ic egriyle ayni sayida nokta.

        Dis sinir tek bir poligondur: alt cizgi + cember + ust cizgi. Ic
        egrinin uc parcasi bu poligonun uc parcasina ESLENIR, ama parca
        sinirlarinda nokta CAKISMAZ -- caksaydi iki isinsal cizgi ayni dis
        noktada bulusur, orada sifir alanli hucre olusurdu. Profil parcasi
        cemberin tamamini uctan uca kaplar; iz parcalari kalan araligi,
        kendi ic dagilimlarini koruyarak doldurur.
        """
        R, X, xc = self.R, self.Xiz, self.xc
        NW, NF = self.NW, self.NF
        cember = [(xc + R * math.cos(math.radians(-90.0 - 180.0 * i / 2000)),
                   R * math.sin(math.radians(-90.0 - 180.0 * i / 2000)))
                  for i in range(2001)]
        poli = [(1.0 + X, -R)] + cember + [(1.0 + X, R)]
        s, _ = _uzunluk(poli)
        t1, t2 = s[1], s[-2]                 # cember baslangici / bitisi

        # profil: cemberin tamami, ic yay dagilimiyla (tabanlanmis)
        s_prof, _ = _uzunluk(ic[NW:NW + NF + 1])
        s_prof = _taban(s_prof)
        prof = _ornekle(poli, [t1 + (t2 - t1) * v for v in s_prof])
        # alt iz: FK dahil olculur, sonra FK atilir -> son nokta t1'in altinda
        s_alt, _ = _uzunluk(ic[0:NW + 1])
        s_alt = _taban(s_alt)
        alt = _ornekle(poli, [t1 * v for v in s_alt[:NW]])
        # ust iz: ayni, bastaki FK atilir
        s_ust, _ = _uzunluk(ic[NW + NF:])
        s_ust = _taban(s_ust)
        ust = _ornekle(poli, [t2 + (1.0 - t2) * v for v in s_ust[1:]])

        d = alt + prof + ust
        assert len(d) == len(ic), (len(d), len(ic))
        return d

    # ---- yurume
    def uret(self):
        ic = self.ic_egri()
        NI = len(ic)
        dis = self.dis_egri(ic)

        # dis normal: teget +90 derece dondurulur
        ham = []
        for i in range(NI):
            a = ic[max(i - 1, 0)]
            b = ic[min(i + 1, NI - 1)]
            tx, ty = b[0] - a[0], b[1] - a[1]
            L = math.hypot(tx, ty) or 1.0
            ham.append((-ty / L, tx / L))

        # Firar kenarinda normal alani SUREKSIZDIR: iz kesiginin normali
        # (0, -1), alt yuzeyinkiyse yaklasik 8 derece yatiktir (kapali NACA
        # 0012'nin firar acisi). Aradaki hucre 2e-4 veter oldugu icin bu
        # sicrama, 20 veter disari yurunurken komsu isinsal cizgileri
        # kesistirir ve hucre ters doner.
        #
        # Cozum yalnizca FIRAR KENARI CEVRESINE uygulanir. Normal alanini
        # bastan sona yumusatmak hucum kenarini bozar: orada normaller
        # zaten dogru ve hizla doner, yumusatmak duvar dikligini yok eder
        # (olculdu: sapma 0.4 dereceden 10 dereceye cikiyor). Bu yuzden
        # yumusatilmis alan, firar kenarindan yay uzunlugu olarak uzaklasan
        # bir pencereyle ham alana harmanlanir.
        yay = [0.0]
        for i in range(1, NI):
            yay.append(yay[-1] + math.hypot(ic[i][0] - ic[i - 1][0],
                                            ic[i][1] - ic[i - 1][1]))
        fk_yay = (yay[self.NW], yay[self.NW + self.NF])   # iki firar kenari
        sig, tau = self.n_sigma, self.fk_pencere

        def yumusak(i):
            sx, sy = ham[i][0], ham[i][1]        # merkez bir kez
            for adim in (1, -1):
                k = i + adim
                while 0 <= k < NI:
                    u = abs(yay[k] - yay[i]) / sig
                    if u > 3.0:
                        break
                    g = math.exp(-0.5 * u * u)
                    sx += g * ham[k][0]; sy += g * ham[k][1]
                    k += adim
            L = math.hypot(sx, sy) or 1.0
            return sx / L, sy / L

        n = []
        for i in range(NI):
            uz = min(abs(yay[i] - f) for f in fk_yay)
            lam = math.exp(-0.5 * (uz / tau) ** 2)
            if lam < 1e-3:
                n.append(ham[i]); continue
            yx, yy = yumusak(i)
            nx = (1 - lam) * ham[i][0] + lam * yx
            ny = (1 - lam) * ham[i][1] + lam * yy
            L = math.hypot(nx, ny) or 1.0
            n.append((nx / L, ny / L))

        mesafe = [math.hypot(dis[i][0] - ic[i][0], dis[i][1] - ic[i][1])
                  for i in range(NI)]

        # Ilk hucre yuksekligi i'ye BAGLIDIR. Profil uzerinde y+ hedefinden
        # gelen dy kullanilir; iz kesiginde ise i adimi cikisa dogru 2.8
        # vetere kadar buyudugu halde dy sabit kalirsa en-boy orani 300 000'i
        # asar (olculdu) ve dogrusal cozucunun kosullanmasi bozulur. Iz
        # duvar degildir, orada y+ = 1 gerekmez: ilk hucre, yerel i adimini
        # en_boy'a bolen degerin altina inmeyecek sekilde gevsetilir.
        # Profil uzerinde yerel adim / dy zaten en_boy'un altinda kaldigi
        # icin bu kural orada devreye girmez.
        adim = []
        for i in range(NI):
            a = ic[max(i - 1, 0)]
            b = ic[min(i + 1, NI - 1)]
            bol = 2.0 if 0 < i < NI - 1 else 1.0
            adim.append(math.hypot(b[0] - a[0], b[1] - a[1]) / bol)

        f = []
        for i in range(NI):
            dyi = max(self.dy, adim[i] / self.en_boy)
            c = _geometrik(self.NJ, dyi, mesafe[i])
            f.append([v / mesafe[i] for v in c])

        # Yurume: yon, duvar normalinden dis sinir dogrultusuna SABIT BIR
        # FIZIKSEL UZUNLUKTA (gecis) doner.
        #
        #   b(f) = f (d + L) / (f d + L)      b(0) = 0 , b(1) = 1
        #   yon  = normalize((1-b) n + b e)
        #   P    = ic + d f yon
        #
        # b(0) = 0 duvarda dikligi, b(1) = 1 ise noktanin dis sinira TAM
        # oturmasini verir. Gecis uzunlugu L, yonun ne kadar mesafede
        # normalden dis dogrultuya dondugunu belirler.
        #
        # Onceki bicim -- ic + d [f(1-f) n + f^2 e] -- bunu yapmiyordu:
        # f(1-f) terimi d = 20 veter ile carpildigi icin alanin ortasinda
        # normal yonunde 5 vetere varan yer degistirme uretiyordu. Sonuc,
        # duvardan cok uzakta bile normal alanindaki kucuk degisimlere asiri
        # duyarliydi ve orada hucreleri ters cevirebiliyordu.
        gec = self.gecis
        P = []
        for i in range(NI):
            d = mesafe[i]
            ex = (dis[i][0] - ic[i][0]) / d
            ey = (dis[i][1] - ic[i][1]) / d
            sut = []
            for ff in f[i]:
                b = ff * (d + gec) / (ff * d + gec)
                vx = (1.0 - b) * n[i][0] + b * ex
                vy = (1.0 - b) * n[i][1] + b * ey
                L = math.hypot(vx, vy) or 1.0
                sut.append((ic[i][0] + d * ff * vx / L,
                            ic[i][1] + d * ff * vy / L))
            P.append(sut)
        return P, NI, len(f[0])

    # ---- yazim
    def yaz(self, yol):
        P, NI, NJ = self.uret()
        z0, z1 = -self.kalinlik / 2, self.kalinlik / 2

        # dugumleri koordinata gore birlestir -> iz kesigi ic yuz olur
        dugum, sira = {}, []

        def dn(x, y, z):
            k = (round(x, 9), round(y, 9), round(z, 9))
            if k not in dugum:
                dugum[k] = len(sira) + 1
                sira.append(k)
            return dugum[k]

        no = [[[dn(P[i][j][0], P[i][j][1], z) for z in (z0, z1)]
               for j in range(NJ)] for i in range(NI)]

        hexler, yuzler = [], {"duvar": [], "disalan": [], "cikis": [],
                              "on": [], "arka": []}
        NW, NF = self.NW, self.NF
        prof_bas, prof_son = NW, NW + NF              # profil i araligi

        for i in range(NI - 1):
            for j in range(NJ - 1):
                a = no[i][j][0]; b = no[i + 1][j][0]
                c_ = no[i + 1][j + 1][0]; d = no[i][j + 1][0]
                e = no[i][j][1]; f_ = no[i + 1][j][1]
                g = no[i + 1][j + 1][1]; h = no[i][j + 1][1]
                hexler.append((a, b, c_, d, e, f_, g, h))
                if j == 0 and prof_bas <= i < prof_son:
                    yuzler["duvar"].append((a, b, f_, e))
                if j == NJ - 2:
                    yuzler["disalan"].append((d, c_, g, h))
                if i == 0:
                    yuzler["cikis"].append((a, d, h, e))
                if i == NI - 2:
                    yuzler["cikis"].append((b, c_, g, f_))
                yuzler["on"].append((a, b, c_, d))
                yuzler["arka"].append((e, f_, g, h))

        ad = ["duvar", "disalan", "cikis", "on", "arka"]
        L = ["$MeshFormat", "2.2 0 8", "$EndMeshFormat",
             "$PhysicalNames", str(len(ad) + 1)]
        for i, a in enumerate(ad):
            L.append('2 %d "%s"' % (i + 1, a))
        L.append('3 %d "ic"' % (len(ad) + 1))
        L.append("$EndPhysicalNames")
        L += ["$Nodes", str(len(sira))]
        for i, (x, y, z) in enumerate(sira):
            L.append("%d %.10g %.10g %.10g" % (i + 1, x, y, z))
        L += ["$EndNodes", "$Elements", str(len(hexler) + sum(len(v) for v in yuzler.values()))]
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
        return dict(dugum=len(sira), hucre=len(hexler), NI=NI, NJ=NJ,
                    dy=self.dy)
