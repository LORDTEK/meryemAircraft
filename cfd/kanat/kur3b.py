# -*- coding: utf-8 -*-
"""Uc boyutlu vakayi kurar -- iki boyutlusundan YALNIZCA agiyla ayrilarak.

Tasarim karari. Alan dosyalarini, ayrik sema secimlerini, cozucu ayarlarini
ve turbulans kurulumunu YENIDEN YAZMIYORUZ; naca/kur.py cagriliyor ve
ciktisinin yalnizca iki parcasi degistiriliyor:

  1. ag.msh -> uc boyutlu ag
  2. 0/* icindeki "(on|arka) empty" -> "(kok|uc) <tip>"

Sebep: iki boyutlu ile uc boyutlu arasindaki farkin AGDAN geldigini iddia
edebilmek icin, geri kalan her seyin bit bit ayni olmasi gerekir. Ayri bir
kurucu yazilsaydi, cikan fark "uc boyutluluk mu, yoksa fark gozden kacan bir
sema ayari mi?" sorusunu acik birakirdi.

Degistirmenin sessizce basarisiz olmamasi icin her dosyada ESLESME SAYISI
denetleniyor.
"""
import os
import re
import sys

BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BURA, "..", "naca"))
sys.path.insert(0, BURA)
from kur import kur as kur2b                          # noqa: E402


P_GAMG_DICGS = ("    p\n    {\n"
                "        solver          GAMG;\n"
                "        smoother        DICGaussSeidel;\n"
                "        tolerance       1e-9;\n"
                "        relTol          0.01;\n"
                "    }\n")


def kur3b(dizin, ag, kok="symmetryPlane", uc="serbest", duvar_fonk=True,
          p_cozucu=P_GAMG_DICGS, sinirli_duzeltme="0.33",
          klasik_simple=True, **kw):
    """ag: KanatAgi ornegi. kw, naca/kur.py'nin kur()'una gecer."""
    kw.setdefault("kod", "0012")
    bilgi2 = kur2b(dizin, **kw)

    # 1) agi degistir
    yeni = ag.yaz(os.path.join(dizin, "ag.msh"))

    # 2) yamalari degistir
    eski = ('    "(on|arka)"\n    {\n        type            empty;\n    }\n')
    n = 0
    for ad in sorted(os.listdir(os.path.join(dizin, "0"))):
        p = os.path.join(dizin, "0", ad)
        s = open(p).read()
        adet = s.count(eski)
        if adet != 1:
            raise RuntimeError("0/%s icinde on|arka blogu %d kez gecti, "
                               "1 bekleniyordu" % (ad, adet))
        # kok: simetri duzlemi (govde orta duzlemi)
        s = s.replace(eski, '    kok\n    {\n        type            %s;\n'
                            '    }\n' % kok)
        if uc == "serbest":
            # uc: UZAK SINIR. Kanat orada bitmiyor -- uctan disariya akis
            # var ve o duzlem serbest akisa aciliyor. Bu yuzden disalan ile
            # AYNI kosulu alir; ayri bir tip yazmak freestreamValue'yu
            # eksik birakirdi.
            if s.count("    disalan\n") != 1:
                raise RuntimeError("0/%s icinde disalan blogu tek degil" % ad)
            s = s.replace("    disalan\n", '    "(disalan|uc)"\n')
        else:
            s = s.replace("    cikis\n", '    uc\n    {\n'
                          '        type            %s;\n    }\n'
                          '    cikis\n' % uc, 1)
        if duvar_fonk:
            # y+ ~ 60 icin DUVAR FONKSIYONU.
            #
            # Ag y+ = 60'ta kuruldu (y+ = 1'de gercek planform agi
            # bozuluyor, bkz. dogrulama.md). Dusuk-Re duvar islemi o y+'ta
            # gecersizdir. nutUSpaldingWallFunction, Spalding yasasina
            # dayandigi icin y+ ~ 1'den ~300'e kadar SUREKLIDIR; y+ aciklik
            # boyunca degistigi icin dogru secim budur.
            n0 = s.count("        type            nutLowReWallFunction;\n")
            s = s.replace("        type            nutLowReWallFunction;\n",
                          "        type            nutUSpaldingWallFunction;\n")
            # k'nin duvar kosulu da DEGISMEK ZORUNDA. Dusuk-Re kurulumunda
            # duvarda k = 1e-14 cakiliyor; bu, ilk hucre merkezi viskoz alt
            # tabakadayken dogrudur. y+ = 60'ta ilk hucre merkezi LOG
            # TABAKASINDA ve orada k ~ u_tau^2/sqrt(beta*) mertebesindedir.
            # Sifira cakmak turbulans uretimini bastirir ve duvar kayma
            # gerilmesini -- yani surukleme ve sinir tabakasi davranisini --
            # yanlis verir. Duvar fonksiyonunun esi kqRWallFunction'dir
            # (sifir gradyan + deger).
            if ad == "k":
                k0 = s.count("        type            fixedValue;\n"
                             "        value           uniform 1e-14;\n")
                if k0 != 1:
                    raise RuntimeError("0/k icinde dusuk-Re duvar kosulu "
                                       "%d kez gecti, 1 bekleniyordu" % k0)
                s = s.replace("        type            fixedValue;\n"
                              "        value           uniform 1e-14;\n",
                              "        type            kqRWallFunction;\n"
                              "        value           uniform 1e-14;\n")
            if ad == "nut" and n0 != 1:
                raise RuntimeError("0/nut icinde dusuk-Re duvar kosulu "
                                   "%d kez gecti, 1 bekleniyordu" % n0)
        open(p, "w").write(s)
        n += 1
    if n == 0:
        raise RuntimeError("0/ bos -- kur2b calismamis olabilir")

    # 3) BASINC COZUCUSU -- uc boyutta olculerek secildi
    #
    # Iki boyutlu vaka GAMG + GaussSeidel kullaniyor ve orada sorun yok.
    # Uc boyutlu agda ayni ayar COKUYOR: basinc cozumu adim basina 206
    # iterasyon yapiyor (saglikli agda 5-20). Sebep, agin azami en-boy
    # oraninin 145 825 olmasi -- GAMG'nin yuz alanina dayali topaklamasi
    # (agglomeration) bu anizotropide ise yaramiyor.
    #
    # Ince agda (1,67 M hucre, 4 cekirdek) olculdu:
    #
    #   GAMG GaussSeidel      38,3 s/adim   p-iter 206
    #   GAMG DICGaussSeidel   17,6 s/adim   p-iter  38
    #   PCG  + DIC            12,3 s/adim   p-iter 185
    #
    # Bu degisiklik YALNIZCA uc boyutlu vakaya uygulanir; naca/kur.py'ye
    # dokunulmaz, boylece dogrulanmis iki boyutlu zincir bit bit korunur.
    if p_cozucu:
        yol = os.path.join(dizin, "system", "fvSolution")
        s = open(yol).read()
        blok = re.search(r"    p\n    \{.*?\n    \}\n", s, re.S)
        if not blok:
            raise RuntimeError("fvSolution icinde p blogu bulunamadi")
        s = s[:blok.start()] + p_cozucu + s[blok.end():]
        open(yol, "w").write(s)

    # 4) DIKEY OLMAYANLIK DUZELTMESI SINIRLANIR
    #
    # Iki boyutlu vaka "corrected" kullaniyor ve orada dogru: o agin azami
    # dikey olmayanligi 74,97 derece, ortalamasi 12,94. Uc boyutlu agda
    # azami 89,69 ve AGIR DIKEY OLMAYAN (>70) yuz sayisi 389 137. Aci
    # 90'a yaklastikca acik (explicit) duzeltme terimi buyuyor ve cozum
    # iraksiyor.
    #
    # Olculdu: "corrected" ile kosu 8. adima kadar duzgun gidiyor, 9.
    # adimda basinc cozumu 1000 iterasyona vuruyor, 10. adimda baslangic
    # artigi 0,99998 (basinc alani cokuyor), 11. adimda kayan nokta
    # hatasiyla patliyor. "limited 0.33" ile 40 adim kararli ve Ux artigi
    # 6,0e-5'e kadar duzenli iniyor.
    #
    # Bu da yalnizca uc boyutlu vakaya uygulanir.
    if sinirli_duzeltme:
        yol = os.path.join(dizin, "system", "fvSchemes")
        s = open(yol).read()
        for eski_s, yeni_s in (
                ("laplacianSchemes { default Gauss linear corrected; }",
                 "laplacianSchemes { default Gauss linear limited %s; }"
                 % sinirli_duzeltme),
                ("snGradSchemes   { default corrected; }",
                 "snGradSchemes   { default limited %s; }" % sinirli_duzeltme)):
            if s.count(eski_s) != 1:
                raise RuntimeError("fvSchemes icinde %r %d kez gecti, 1 "
                                   "bekleniyordu" % (eski_s, s.count(eski_s)))
            s = s.replace(eski_s, yeni_s)
        open(yol, "w").write(s)

    # 5) GEVSEME -- klasik SIMPLE'a gecilir
    #
    # naca/kur.py "consistent yes" (SIMPLEC) + U 0,9 kullaniyor ve iki
    # boyutta dogru calisiyor. Uc boyutlu agda IRAKSIYOR: kosu 8. adima
    # kadar duzgun gidiyor, 9. adimda basinc cozumu 1000 iterasyona
    # vuruyor, 10. adimda baslangic artigi 0,99998 (basinc alani cokuyor),
    # 11. adimda kayan nokta hatasi.
    #
    # Olculdu -- klasik SIMPLE (consistent no) + p 0,3 / U 0,7 ile ayni ag
    # 1500 adim kararli, Ux artigi 2e-6'ya iniyor.
    #
    # BU DUZELTME ONCE YALNIZCA ELLE YAPILMISTI ve kodda degildi; yeni
    # kurulan uc GCI vakasi eski ayarla kuruldugu icin ucu de patladi
    # (110/66/75 adim, SIGFPE). Kodlanmasinin sebebi budur.
    if klasik_simple:
        yol = os.path.join(dizin, "system", "fvSolution")
        s = open(yol).read()
        if s.count("    consistent      yes;") != 1:
            raise RuntimeError("fvSolution icinde 'consistent yes' tek degil")
        s = s.replace("    consistent      yes;", "    consistent      no;")
        blok = re.search(r"relaxationFactors\n\{.*?\n\}\n", s, re.S)
        if not blok:
            raise RuntimeError("relaxationFactors blogu bulunamadi")
        s = s[:blok.start()] + ("relaxationFactors\n{\n    fields\n    {\n"
                                "        p               0.3;\n    }\n"
                                "    equations\n    {\n"
                                "        U               0.7;\n"
                                '        "(k|omega|nuTilda)" 0.7;\n'
                                "    }\n}\n") + s[blok.end():]
        open(yol, "w").write(s)

    # 6) 2B'ye ozgu sema kalintisi kalmadigini dogrula
    for ad in ("fvSchemes", "fvSolution", "controlDict"):
        s = open(os.path.join(dizin, "system", ad)).read()
        if "empty" in s:
            raise RuntimeError("system/%s icinde 'empty' gecıyor" % ad)

    bilgi = dict(bilgi2 or {})
    bilgi.update(yeni)
    bilgi["alan_dosyasi"] = n
    return bilgi


# kos3b.sh ELDEN yazilan ayri bir dosyadir; buradan URETILMEZ. Onceki
# surumde bir dizge olarak burada tutuluyordu ve gomulu Python'un duzenli
# ifadelerindeki kacislar dizge cozumlemesinde yenerek betigi bozuyordu.
# Kaba agda yapilan hizli deneme yakaladi.
