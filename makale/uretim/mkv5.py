# -*- coding: utf-8 -*-
"""v5 GONDERIM BELGELERINI KURAR -- makale-v5.md ve makale-v5-ek.md.

NEDEN VAR. v5'in ilk surumu EL ILE toparlanmisti. Bunun bedelini odedik:
disaridan dort bagimsiz okuma, govdedeki 5.5 tablosunun aslinda S6.1'in
Bacchini & Cestino tablosu oldugunu, sutun basliklari degistirilmis halde
kendi boyutlandirmamiz gibi durdugunu buldu. El ile toplanan bir belgede
bu tur bir kayma sessizce yasar.

Bu betik ayni belgeyi bolum dosyalarindan ve 00-on-bilgi.md'den her
seferinde yeniden kurar, kelime sayilarini SAYAR (elle yazmaz), ve ek
dizinini iki yerde ayni kaynaktan uretir -- boylece iki liste birbirinden
ayrisamaz.

mkmakale.py sekilli PDF'i uretir; bu betik sekilsiz, tek dosyalik
gonderim/paylasim surumunu uretir. Ikisi ayni bolum dosyalarini okur.
"""
import os, re, sys

BURA = os.path.dirname(os.path.abspath(__file__))
MAKALE = os.path.abspath(os.path.join(BURA, ".."))
sys.path.insert(0, BURA)
from mkmakale import temizle, blok           # ayni ayiklama kurallari

BOLUM = os.path.join(MAKALE, "bolumler")
EK = os.path.join(MAKALE, "ek")

EKLER = [
    ("S1", "S1-aerodinamik-dogrulama.md",
     "Independent checks on the two assumed aerodynamic coefficients"),
    ("S2", "S2-kutle-kurulusu.md",
     "A component build-up of the mass budget"),
    ("S3", "S3-kontrol-eksenleri.md",
     "Control axes in full"),
    ("S4", "S4-donme-otoritesi-ve-denge.md",
     "Rotational authority, trim, and the transition envelope"),
    ("S5", "S5-sinirlar-tam.md",
     "The limitations in full"),
    ("S6", "S6-faturalar-ve-karsilastirma.md",
     "The three bills stated formally, and a comparative sizing"),
]

BASLIK = ("The Architectural Cost of Hybrid VTOL: meryemAircraft, a "
          "Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated "
          "Lift System")


def oku(yol):
    return open(yol, encoding="utf-8").read()


def kelime(s):
    """Baslik isaretlerini ve tablo cubuklarini saymadan kelime sayar."""
    s = re.sub(r"^#{1,6}\s", "", s, flags=re.M)
    s = s.replace("|", " ")
    return len(s.split())


def ek_dizini(sayilar):
    return "\n".join(
        "- **Supplementary %s** — %s (%d words)" % (kod, ad, sayilar[kod])
        for kod, _, ad in EKLER)


# ---------------------------------------------------------------- ekler
ek_govde, ek_sayi = [], {}
for kod, dosya, _ in EKLER:
    metin = oku(os.path.join(EK, dosya)).strip()
    ek_sayi[kod] = kelime(metin)
    ek_govde.append(metin)

dizin = ek_dizini(ek_sayi)

# ---------------------------------------------------------------- makale
on = oku(os.path.join(MAKALE, "00-on-bilgi.md"))
parcalar = ["# The Architectural Cost of Hybrid VTOL", "---", "## Title",
            "**" + BASLIK + "**"]
for ad in ("Authors", "Abstract", "Keywords"):
    govde = blok(on, ad)
    if not govde:
        print("UYARI — 00-on-bilgi.md icinde '%s' bulunamadi" % ad)
    parcalar += ["## " + ad, govde]

# Beyanlar kendi alt basliklarini tasiyor, o yuzden blok() ile degil:
# "## Beyanlar"dan dosya sonuna kadar alinip basligi ingilizcelestiriliyor.
m = re.search(r"^##\s+Beyanlar\s*$(.*)\Z", on, flags=re.M | re.S)
if m:
    parcalar += ["## Declarations", temizle(m.group(1))]
else:
    print("UYARI — 00-on-bilgi.md icinde 'Beyanlar' bulunamadi")

bolumler = sorted(f for f in os.listdir(BOLUM) if f.endswith(".md"))
gsayi = 0
for f in bolumler:
    metin = temizle(oku(os.path.join(BOLUM, f))).strip()
    gsayi += kelime(metin)
    parcalar += ["---", metin]

parcalar += ["---", oku(os.path.join(MAKALE, "kaynakca-en.md"))
             .strip().replace("# References", "# References", 1)]
parcalar += ["---", "# Supplementary Material", """Six supplementary files accompany this paper and are cited from it by number.
They carry the derivations behind the results stated here; each was a section of an earlier,
longer version and is reproduced without abridgement.""", dizin,
             """The computational setup, the scripts that produce every number here, and a running record
of the corrections made during the study are in the repository this paper cites."""]

makale = "\n\n".join(parcalar) + "\n"
open(os.path.join(MAKALE, "makale-v5.md"), "w", encoding="utf-8").write(makale)

# ------------------------------------------------------------ ek belgesi
ek_bas = "\n\n".join([
    "# Supplementary Material — meryemAircraft",
    '*Supplementary material to "%s".*' % BASLIK,
    """These six files carry the derivations behind the results stated in the paper. Each was a
section of an earlier, longer version and is reproduced without abridgement, so that every
number quoted in the main text can be traced to the calculation that produced it. The
computational setup, the scripts, and a running record of the corrections made during the
study are in the repository the paper cites.""",
    "**Contents**", dizin])

ek_belge = ek_bas + "\n\n---\n\n" + "\n\n---\n\n".join(ek_govde) + "\n"
open(os.path.join(MAKALE, "makale-v5-ek.md"), "w", encoding="utf-8").write(ek_belge)

# ------------------------------------------------------------------ rapor
print("makale-v5.md      %6d kelime  (govde %d, %d bolum)"
      % (kelime(makale), gsayi, len(bolumler)))
print("makale-v5-ek.md   %6d kelime" % kelime(ek_belge))
for kod, _, _ in EKLER:
    print("   %-3s %6d" % (kod, ek_sayi[kod]))

# atif bosluk/hayalet denetimi -- kaynakca ile govde tutuyor mu
kaynak_sayisi = len(re.findall(r"^\s*(\d+)\. ",
                               oku(os.path.join(MAKALE, "kaynakca-en.md")), re.M))
atifli = set()
for m in re.finditer(r"\[(\d+(?:\s*,\s*\d+)*)\]", makale + ek_belge):
    atifli.update(int(x) for x in m.group(1).split(","))
eksik = sorted(n for n in range(1, kaynak_sayisi + 1) if n not in atifli)
hayalet = sorted(n for n in atifli if n > kaynak_sayisi)
print("kaynak %d; atif almayan %s; listede olmayan %s"
      % (kaynak_sayisi, eksik or "yok", hayalet or "yok"))
