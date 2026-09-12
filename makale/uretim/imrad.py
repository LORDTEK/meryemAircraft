# -*- coding: utf-8 -*-
"""BOLUMLERI IMRaD'A TASIR -- bir kez calistirilir, sonra silinmez.

NEDEN VAR. Drones'un Instructions for Authors'i, "Free Format Submission"
altinda bile bolum listesini adiyla sayiyor: Introduction, Materials &
Methods, Results, Conclusions. Bizim dokuz bolumluk yapimiz bu degildi.

BU BIR TASIMA, YENIDEN YAZMA DEGIL. Hicbir paragraf silinmiyor. Yapilan
sey her alt bolumu yeni bir numaraya goturmek ve ~180 capraz atfi o
numaralara cevirmek.

TEHLIKE. Eski 3.3 "Bill 2 -- drag", yeni 3.3 ise "Bill 2 denetlendi"
(eski 5.2). Yani eski ve yeni numara uzaylari CAKISIYOR. Sirali bir
arama-degistirme bu yuzden felaket olur -- daha once bir kaskad regex
S7->S6->S5 zincirini S2'ye cokertmisti. Burada esleme TEK GECISTE, bir
fonksiyonla uygulaniyor: her atif bir kez okunur, bir kez yazilir,
zincirlenmez.

DOGRULAMA. Calistiktan sonra ciktidaki her "Section N.M" atfi gercekten
var olan bir baslikla eslesmeli; betik bunu kendi kontrol eder ve
eslesmeyeni sayar.
"""
import os, re, sys, collections

BURA = os.path.dirname(os.path.abspath(__file__))
MAKALE = os.path.abspath(os.path.join(BURA, ".."))
BOLUM = os.path.join(MAKALE, "bolumler")
EK = os.path.join(MAKALE, "ek")

# ---------------------------------------------------------------- esleme
# eski alt bolum -> yeni alt bolum. Her eski basligin tam olarak bir
# karsiligi var; bijection oldugu asagida denetleniyor.
HARITA = {
    # Introduction: eski 2 (Background) girisin alt bolumleri olur
    "2.1": "1.1", "2.2": "1.2", "2.3": "1.3", "2.4": "1.4", "2.5": "1.5",
    # Materials and Methods: cerceve (eski 3.1-3.6) + konfigurasyon (eski 4)
    # + boyutlandirma yontemi (eski 6.1)
    "3.1": "2.1", "3.2": "2.2", "3.3": "2.3", "3.4": "2.4",
    "3.5": "2.5", "3.6": "2.6",
    "4.1": "2.7", "4.2": "2.8", "4.3": "2.9", "4.4": "2.10", "4.5": "2.11",
    "6.1": "2.12",
    # Results: cercevenin sinanmasi (eski 3.7) + fatura denetimi (eski 5)
    # + referans tasarimlar (eski 6.2-6.4, 6.6, 6.7) + gecis (eski 7)
    "3.7": "3.1",
    "5.1": "3.2", "5.2": "3.3", "5.3": "3.4", "5.4": "3.5", "5.5": "3.6",
    "6.2": "3.7", "6.3": "3.8", "6.4": "3.9", "6.6": "3.10", "6.7": "3.11",
    "7.1": "3.12", "7.2": "3.13", "7.3": "3.14", "7.4": "3.15",
    "7.5": "3.16", "7.6": "3.17",
    # Discussion: baglam (eski 6.5) + pazar (eski 3.8) + sinirlar (eski 8)
    "6.5": "4.1", "3.8": "4.2",
    "8.1": "4.3", "8.2": "4.4", "8.3": "4.5", "8.4": "4.6", "8.5": "4.7",
}

# ciplak "Section N" atiflari
UST = {"2": "1", "3": "2", "4": "2", "5": "3", "6": "3", "7": "3",
       "8": "4", "9": "5"}

# yeni ust bolumlerin basliklari
YENI_UST = [
    ("1", "Introduction"),
    ("2", "Materials and Methods"),
    ("3", "Results"),
    ("4", "Discussion"),
    ("5", "Conclusions"),
]


def bijection_denetle():
    hedefler = list(HARITA.values())
    tekrar = [k for k, v in collections.Counter(hedefler).items() if v > 1]
    if tekrar:
        sys.exit("HATA: iki eski bolum ayni yeni numaraya gidiyor: %s" % tekrar)
    print("esleme: %d alt bolum, cakisma yok" % len(HARITA))


# ---------------------------------------------------------- atif cevirici
# "Section 6.2", "Sections 6.2 and 6.3", "Sections 4 to 7", "Section 8.2"
ATIF = re.compile(
    r"\bSections?\s+\d+(?:\.\d+)?"
    r"(?:\s*(?:,|and|to|–|-)\s*\d+(?:\.\d+)?)*")
SAYI = re.compile(r"\d+(?:\.\d+)?")


def cevir_sayi(s):
    if s in HARITA:
        return HARITA[s]
    if "." not in s and s in UST:
        return UST[s]
    return s                      # 1, ya da tanimadigimiz bir sey


def cevir_atif(m):
    """Bir atif obegindeki HER sayiyi tek seferde cevirir."""
    return SAYI.sub(lambda x: cevir_sayi(x.group(0)), m.group(0))


def cevir(metin):
    return ATIF.sub(cevir_atif, metin)


def oku(y):
    return open(y, encoding="utf-8").read()


def yaz(y, s):
    open(y, "w", encoding="utf-8").write(s)


# ------------------------------------------------------ alt bolum cikar
def parcala(metin):
    """'## N.M Baslik' bloklarina ayirir. Ilk basliktan onceki kisim ''."""
    parcalar, ad, tampon = [], None, []
    for satir in metin.split("\n"):
        m = re.match(r"^##\s+(\d+\.\d+)\s+(.*)$", satir)
        if m:
            parcalar.append((ad, "\n".join(tampon)))
            ad, tampon = (m.group(1), m.group(2)), []
        else:
            tampon.append(satir)
    parcalar.append((ad, "\n".join(tampon)))
    return parcalar


def main():
    # BIR KEZ calisir. Ikinci kez calistirilirsa eski numaralar artik yok
    # ve bijection denetimi zaten durdurur, ama acik bir kilit daha iyi:
    if os.path.exists(os.path.join(BOLUM, "02-methods.md")):
        sys.exit("Bolumler zaten IMRaD'a tasinmis (02-methods.md var). "
                 "Bu betik bir kez calisir; tekrar calistirmak icin once "
                 "git ile eski yapiyi geri alin.")
    bijection_denetle()

    # 1) butun eski bolum dosyalarini oku, alt bolumlere ayir
    bloklar = {}          # eski numara -> (baslik, govde)
    onsoz = {}            # dosya -> ilk basliktan onceki metin
    for f in sorted(os.listdir(BOLUM)):
        if not f.endswith(".md"):
            continue
        for ad, govde in parcala(oku(os.path.join(BOLUM, f))):
            if ad is None:
                onsoz[f] = govde
            else:
                bloklar[ad[0]] = (ad[1], govde)

    eksik = set(HARITA) - set(bloklar)
    fazla = set(bloklar) - set(HARITA)
    if eksik or fazla:
        sys.exit("HATA: haritada olmayan/bulunamayan bolum. eksik=%s fazla=%s"
                 % (sorted(eksik), sorted(fazla)))
    print("bulunan alt bolum: %d, hepsi haritada" % len(bloklar))

    # 2) yeni numaraya gore sirala
    ters = {v: k for k, v in HARITA.items()}

    def anahtar(n):
        a, b = n.split(".")
        return (int(a), int(b))

    yeni_sirali = sorted(ters, key=anahtar)

    # 3) yeni dosyalari kur
    cikti = {n: [] for n, _ in YENI_UST}
    for yeni in yeni_sirali:
        eski = ters[yeni]
        baslik, govde = bloklar[eski]
        ust = yeni.split(".")[0]
        cikti[ust].append("## %s %s\n%s" % (yeni, cevir(baslik), cevir(govde)))

    # HER dosyanin onsozu tasinmali. Ilk surumde yalniz 01 ve 09'unki
    # aliniyordu ve alti dosyanin onsozu (479 kelime, Sekil 2'nin atfi
    # dahil) sessizce dusuyordu. Kaybi kendi sekil denetleyicim yakaladi.
    giris_onsoz = cevir(onsoz.get("01-introduction.md", "").strip())
    sonuc = cevir(onsoz.get("09-conclusion.md", "").strip())
    # kalan onsozler, gittikleri bolumun ilgili basliginin onune:
    ARA = [("02-background.md", "1", "1.1"), ("03-architectural-tax.md", "2", "2.1"),
           ("05-tax-avoided.md", "3", "3.2"), ("06-reference-designs.md", "3", "3.7"),
           ("07-transition.md", "3", "3.12"), ("08-limitations.md", "4", "4.3")]

    dosyalar = {
        "01-introduction.md": "# 1. Introduction\n\n" + giris_onsoz + "\n\n"
                              + "\n".join(cikti["1"]),
        "02-methods.md": "# 2. Materials and Methods\n\n" + ONSOZ_YONTEM
                         + "\n".join(cikti["2"]),
        "03-results.md": "# 3. Results\n\n" + ONSOZ_SONUC
                         + "\n".join(cikti["3"]),
        "04-discussion.md": "# 4. Discussion\n\n" + ONSOZ_TARTISMA
                            + "\n".join(cikti["4"]),
        "05-conclusions.md": "# 5. Conclusions\n\n" + sonuc,
    }

    # eski dosyalari sil, yenileri yaz
    for f in os.listdir(BOLUM):
        if f.endswith(".md"):
            os.remove(os.path.join(BOLUM, f))
    for ad, govde in dosyalar.items():
        yaz(os.path.join(BOLUM, ad), govde.rstrip() + "\n")
    print("yazilan dosya: %d" % len(dosyalar))

    # 4) ekleri de cevir
    for f in sorted(os.listdir(EK)):
        if f.endswith(".md"):
            p = os.path.join(EK, f)
            yaz(p, cevir(oku(p)))
    # on bilgi de govde bolumlerine atif veriyor
    p = os.path.join(MAKALE, "00-on-bilgi.md")
    yaz(p, cevir(oku(p)))
    print("cevrilen ek + on bilgi: %d" % (len(os.listdir(EK)) + 1))

    # 5) DOGRULAMA -- her atif var olan bir baslikla eslesiyor mu
    var = set()
    for f in os.listdir(BOLUM):
        if f.endswith(".md"):
            for m in re.finditer(r"^##\s+(\d+\.\d+)", oku(os.path.join(BOLUM, f)), re.M):
                var.add(m.group(1))
    for f in os.listdir(EK):
        if f.endswith(".md"):
            for m in re.finditer(r"^##\s+(S\d+\.\d+)", oku(os.path.join(EK, f)), re.M):
                var.add(m.group(1))
    kirik = collections.Counter()
    for d in (BOLUM, EK):
        for f in os.listdir(d):
            if not f.endswith(".md"):
                continue
            for m in re.finditer(r"Section (\d+\.\d+)", oku(os.path.join(d, f))):
                if m.group(1) not in var:
                    kirik[m.group(1)] += 1
    if kirik:
        print("!! var olmayan alt bolume atif:", dict(kirik))
    else:
        print("dogrulama: her alt bolum atfi var olan bir baslikla eslesiyor")


ONSOZ_YONTEM = """This section states the analytical framework the paper is built on, defines the
configuration it is applied to, and gives the methods by which every number in Section 3 was
produced. Sections 2.1 to 2.6 develop the framework; Sections 2.7 to 2.11 define the aircraft;
Sections 2.12 and 2.13 give the sizing and computational methods; Section 2.14 records the use
of artificial-intelligence tools.

"""

ONSOZ_SONUC = """Results are given in four groups: the framework tested against published sizing
studies (Section 3.1), the three charges audited against the proposed configuration
(Sections 3.2 to 3.6), two reference designs with the bounds on their assumed coefficients and a
component build-up of their mass (Sections 3.7 to 3.11), and the flight profile with the
transition analysis (Sections 3.12 to 3.17). Every number is calculated rather than measured;
Section 4 states what that means.

"""

ONSOZ_TARTISMA = """This section places the results against existing aircraft and existing
literature, then states what is not shown. Sections 4.1 and 4.2 are interpretation;
Sections 4.3 to 4.7 are limitations, ordered by whether they could change a conclusion.

"""

if __name__ == "__main__":
    main()
