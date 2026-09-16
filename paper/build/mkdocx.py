# -*- coding: utf-8 -*-
"""MDPI SABLONUNDA .docx URETIR -- paper-<version>.md'den, elle bicimleme YOK.

NEDEN BOYLE. Sablona elle dokmek 70 sayfa, 172 tablo ve 12 sekil demek;
her biri bir kopyala-yapistir kaymasi firsatidir ve bu depoda bir surum
ELLE toparlandigi icin yanlis tablo tasimisti. Sablon da uretilir.

NE URETIR. MDPI'nin Word sablonunun yapisi: baslik, yazarlar ve ustsimge
kurum numaralari, kurum satirlari, yazisma adresi, Abstract:, Keywords:,
numarali bolumler, sekil altyazilari "Figure N.", tablo ustyazilari
"Table N.", arka madde bloklari derginin kendi sirasinda, ve numarali
kaynakca.

NE URETMEZ. Derginin logolu ust bilgisi, DOI/alinma tarihi satirlari ve
telif kutusu -- onlar kabul sonrasi dizgide dolduruluyor ve gonderimde
bos birakilmasi bekleniyor.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from captions import FIGS
from version import SURUM                  # tek dogruluk kaynagi

ROOT = "/home/user/meryemAircraft"
KAYNAK = os.path.join(ROOT, "paper", "paper-%s.md" % SURUM)
EK_KAYNAK = os.path.join(ROOT, "paper", "paper-%s-supp.md" % SURUM)
GOR = os.path.join(ROOT, "figures", "output")
CIKTI = os.path.join(ROOT, "paper", "pdf", "meryemAircraft-MDPI.docx")
EK_CIKTI = os.path.join(ROOT, "paper", "pdf", "meryemAircraft-MDPI-supp.docx")
# Bazi sekiller birden cok dosyadan olusuyor (10a/10b); liste olarak gelir.
CAP = {n: (f if isinstance(f, list) else [f], c) for n, f, c in FIGS}

GOVDE_PT, KUCUK_PT = 10, 9
YAZI = "Palatino Linotype"          # MDPI'nin govde yazi tipi


def yazitipi(calisan, boyut=GOVDE_PT, kalin=False, italik=False):
    calisan.font.name = YAZI
    calisan.font.size = Pt(boyut)
    calisan.bold = kalin
    calisan.italic = italik
    r = calisan._element.rPr.rFonts
    r.set(qn("w:eastAsia"), YAZI)


def satir_isle(p, metin, boyut=GOVDE_PT, kalin_hepsi=False):
    """**kalin**, *italik* ve <sup> isaretlerini calisanlara cevirir.

    Kaynak markdown'da yazar satirlari HTML ustsimgesi tasiyor
    (<sup>1,\*</sup>) ve beyan bloklari alinti isaretiyle (>) yazilmis.
    Ikisi de Word'de ham metin olarak gorunmemeli.
    """
    metin = re.sub(r"^\s*>\s?", "", metin)          # alinti isareti
    metin = metin.replace("\\*", "*")
    # <sup>...</sup> once ayri calisanlara bolunur
    for ust in re.split(r"(<sup>.*?</sup>)", metin):
        if not ust:
            continue
        if ust.startswith("<sup>"):
            c = p.add_run(ust[5:-6])
            yazitipi(c, boyut, kalin_hepsi)
            c.font.superscript = True
            continue
        _satir_vurgu(p, ust, boyut, kalin_hepsi)


def _satir_vurgu(p, metin, boyut, kalin_hepsi):
    for parca in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", metin):
        if not parca:
            continue
        if parca.startswith("**") and parca.endswith("**"):
            yazitipi(p.add_run(parca[2:-2]), boyut, True)
        elif parca.startswith("*") and parca.endswith("*") and len(parca) > 2:
            yazitipi(p.add_run(parca[1:-1]), boyut, kalin_hepsi, True)
        else:
            yazitipi(p.add_run(parca), boyut, kalin_hepsi)


def paragraf(d, metin, boyut=GOVDE_PT, hiza=WD_ALIGN_PARAGRAPH.JUSTIFY,
             once=0, sonra=4, kalin_hepsi=False, girinti=0):
    p = d.add_paragraph()
    p.alignment = hiza
    p.paragraph_format.space_before = Pt(once)
    p.paragraph_format.space_after = Pt(sonra)
    if girinti:
        p.paragraph_format.left_indent = Pt(girinti)
    p.paragraph_format.line_spacing = 1.0
    satir_isle(p, metin, boyut, kalin_hepsi)
    return p


def birlikte(p):
    """Paragrafi bir SONRAKI paragrafla ayni sayfada tutar (keepNext).

    Sekil ile altyazisinin, tablo ustyazisi ile tablosunun sayfa
    sonunda ayrilmasi MDPI'nin acikca yasakladigi seylerden.
    """
    pPr = p._p.get_or_add_pPr()
    pPr.append(OxmlElement("w:keepNext"))
    return p


def tablo_ekle(d, satirlar):
    """Markdown tablosu -> Word tablosu, MDPI ustyazisiyla."""
    hucreler = [[c.strip() for c in s.strip().strip("|").split("|")]
                for s in satirlar if not re.match(r"^\s*\|[\s:|-]+\|\s*$", s)]
    if not hucreler:
        return
    n = max(len(h) for h in hucreler)
    t = d.add_table(rows=len(hucreler), cols=n)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, sat in enumerate(hucreler):
        trPr = t.rows[i]._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
        if i == 0:
            trPr.append(OxmlElement("w:tblHeader"))
        for j in range(n):
            hucre = t.cell(i, j)
            hucre.text = ""
            p = hucre.paragraphs[0]
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            satir_isle(p, sat[j] if j < len(sat) else "", KUCUK_PT, i == 0)
    d.add_paragraph()


def sekil_ekle(d, no):
    dosyalar, altyazi = CAP[no]
    kondu = False
    for dosya in dosyalar:
        yol = os.path.join(GOR, dosya)
        if not os.path.exists(yol):
            print("UYARI — sekil bulunamadi: %s" % dosya)
            continue
        p = d.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        p.add_run().add_picture(yol, width=Cm(15.0 if len(dosyalar) == 1 else 12.0))
        birlikte(p)
        kondu = True
    if not kondu:
        return
    c = d.add_paragraph()
    c.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    c.paragraph_format.space_after = Pt(8)
    yazitipi(c.add_run("Figure %s. " % no), KUCUK_PT, True)
    satir_isle(c, altyazi, KUCUK_PT)


def kur():
    d = Document()
    st = d.styles["Normal"]
    st.font.name = YAZI
    st.font.size = Pt(GOVDE_PT)
    for s in d.sections:
        s.top_margin = Cm(2.4); s.bottom_margin = Cm(2.4)
        s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)
    return d


# --- kaynak belgeyi bloklara ayir ---------------------------------------
def bloklar(metin):
    """Satirlari (tur, icerik) ciftlerine ayirir."""
    cik, tampon, tablo = [], [], []
    for sat in metin.split("\n"):
        # Alinti isareti SATIR BASINDA temizlenir, birlestirmeden ONCE.
        # Sonra temizlenirse cok satirli beyan bloklarinda paragraf
        # ortasinda '>' kaliyor.
        sat = re.sub(r"^\s*>\s?", "", sat)
        if sat.strip().startswith("|") and sat.strip().endswith("|"):
            if tampon:
                cik.append(("p", " ".join(tampon))); tampon = []
            tablo.append(sat); continue
        if tablo:
            cik.append(("t", tablo)); tablo = []
        if sat.startswith("#"):
            if tampon:
                cik.append(("p", " ".join(tampon))); tampon = []
            duzey = len(sat) - len(sat.lstrip("#"))
            cik.append(("h%d" % duzey, sat.lstrip("#").strip()))
        elif sat.strip() in ("", "---"):
            if tampon:
                cik.append(("p", " ".join(tampon))); tampon = []
        else:
            tampon.append(sat.strip())
    if tampon: cik.append(("p", " ".join(tampon)))
    if tablo: cik.append(("t", tablo))
    return cik


if __name__ == "__main__":
    ham = open(KAYNAK, encoding="utf-8").read()
    bs = bloklar(ham)
    d = kur()

    # --- ON MADDE, MDPI duzeni ---------------------------------------
    def blok_metni(ad):
        al, topla = False, []
        for t, i in bs:
            if t.startswith("h") and isinstance(i, str):
                if i.strip().lower() == ad.lower(): al = True; continue
                if al: break
            elif al and t == "p":
                topla.append(i)
        return topla

    baslik = blok_metni("Title")
    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(10)
    satir_isle(p, baslik[0] if baslik else "", 16, True)

    for sat in blok_metni("Authors"):
        paragraf(d, sat, GOVDE_PT, WD_ALIGN_PARAGRAPH.LEFT, sonra=2)

    # HIGHLIGHTS PDF'DE VARDI, DOCX'TE YOKTU. ON kumesi onu atlıyordu;
    # yani ayni kusurun -- zorunlu bir on maddenin uretilen belgeye hic
    # girmemesi -- ikinci kopyasi, bu kez gonderilecek olan dosyada.
    # Sira mkrelease.py ile ayni: Title, Authors, Highlights, Abstract, Keywords.
    vurgu = blok_metni("Highlights")
    if not vurgu:
        raise SystemExit("DUR -- Highlights bulunamadi; MDPI bunu zorunlu tutuyor")
    for sat in vurgu:
        if sat.strip().startswith("- "):
            for madde in re.split(r"(?:^|\s)- ", sat.strip())[1:]:
                paragraf(d, "\u2022  " + madde.strip(), KUCUK_PT,
                         WD_ALIGN_PARAGRAPH.JUSTIFY, sonra=3, girinti=14)
        elif sat.strip():
            paragraf(d, sat.strip(), KUCUK_PT, WD_ALIGN_PARAGRAPH.LEFT,
                     once=6, sonra=3)

    ozet = blok_metni("Abstract")
    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(10)
    yazitipi(p.add_run("Abstract: "), KUCUK_PT, True)
    satir_isle(p, " ".join(ozet), KUCUK_PT)

    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(12)
    yazitipi(p.add_run("Keywords: "), KUCUK_PT, True)
    satir_isle(p, " ".join(blok_metni("Keywords")), KUCUK_PT)

    # --- GOVDE --------------------------------------------------------
    ON = {"title", "authors", "abstract", "keywords", "highlights"}
    icinde, sekil_sirasi = False, set()
    beyan_kipi, beyanlar = [False], []
    kaynak_kipi, kaynaklar = [False], []
    for t, i in bs:
        # Beyan kipindeyken h3 basliklari da toplanmali. Ilk surumde
        # baslik dali butun basliklari yakaliyordu ve beyan alt
        # basliklari (Supplementary Materials, Patents, ...) hic
        # gorunmuyordu -- govdeleri duruyor, baslıklari kayboluyordu.
        if beyan_kipi[0] and t == "h3":
            beyanlar.append((t, i)); continue
        if t.startswith("h") and isinstance(i, str):
            ad = i.strip().lower()
            # BEYANLAR MDPI'DA SONDA. Kaynak belge onlari Keywords'ten
            # hemen sonra tasiyor (tek dosyalik markdown icin dogru);
            # burada toplanip kaynakcadan SONRA basiliyorlar.
            if ad in ON:
                icinde = False
                continue
            if ad == "declarations":
                beyan_kipi[0] = True; icinde = False
                continue
            # Numarali bir govde basligi ya da References gorulunce beyan
            # toplama BITER. Kaynakta beyanlar govdeden ONCE geliyor; bu
            # satir olmadan butun govde beyan sanilir.
            if re.match(r"^\d+\.", ad):
                beyan_kipi[0] = False
                icinde = True
            if ad == "references":
                # MDPI'da arka madde bloklari kaynakcadan ONCE gelir.
                # Kaynak belge onlari en basa koyuyor (tek dosyalik
                # markdown icin dogru), burada araya giriyorlar.
                beyan_kipi[0] = False
                kaynak_kipi[0] = True
                icinde = False
                continue
            if not icinde:
                continue
            duzey = int(t[1])
            p = d.add_paragraph()
            p.paragraph_format.space_before = Pt(10 if duzey <= 2 else 8)
            p.paragraph_format.space_after = Pt(4)
            yazitipi(p.add_run(i.strip()), 13 if duzey == 1 else 11, True)
        elif kaynak_kipi[0] and t == "p":
            # Kaynakca numarali liste; satirlar girintiyle devam ediyor ve
            # bos satirla ayrilmiyor, o yuzden bloklar() hepsini TEK
            # paragrafa birlestiriyor. Numaraya gore yeniden bolunuyor.
            for parca in re.split(r"(?=(?:^|\s)\d{1,2}\.\s+[*\[]?[A-ZŞÇĞİÖÜ])", i):
                parca = parca.strip()
                # Yazarsiz kurum kaynaklari italikle basliyor (*An Interim
                # Report...*); ilk surum harf bekledigi icin uc tanesi
                # bir onceki girdiye yapismisti.
                if re.match(r"^\d{1,2}\.\s", parca):
                    kaynaklar.append(parca)
        elif beyan_kipi[0] and t in ("p", "h3"):
            beyanlar.append((t, i))
        elif icinde and t == "p":
            par = paragraf(d, i)
            # Tablo ustyazisi kendi tablosuyla ayni sayfada kalsin.
            if re.match(r"^\*\*Table \d+\.\*\*", i):
                birlikte(par)
            for m in re.finditer(r"Figure (\d+)", i):
                n = m.group(1)
                if n in CAP and n not in sekil_sirasi:
                    sekil_ekle(d, n); sekil_sirasi.add(n)
        elif icinde and t == "t":
            tablo_ekle(d, i)

    # --- BEYANLAR, MDPI sirasinda, KAYNAKCADAN ONCE --------------------
    SIRA = ["supplementary materials", "author contributions", "funding",
            "data availability", "acknowledgements", "conflicts of interest",
            "dual-use research of concern", "patents"]
    gruplar, simdiki = {}, None
    for t, i in beyanlar:
        if t == "h3":
            simdiki = i.strip().lower(); gruplar.setdefault(simdiki, [i, []])
        elif simdiki:
            gruplar[simdiki][1].append(i)
    duzenli = [gruplar[k] for k in SIRA if k in gruplar]
    duzenli += [v for k, v in gruplar.items() if k not in SIRA]
    if len(duzenli) != len(gruplar):
        sys.exit("!! DUR -- beyan bloklari siralanirken kayip var.")
    if duzenli:
        for baslik, govde in duzenli:
            q = d.add_paragraph()
            q.paragraph_format.space_before = Pt(8)
            q.paragraph_format.space_after = Pt(2)
            yazitipi(q.add_run(baslik.strip()), 10, True)
            for satir in govde:
                paragraf(d, satir, KUCUK_PT)

    if kaynaklar:
        p = d.add_paragraph(); p.paragraph_format.space_before = Pt(14)
        yazitipi(p.add_run("References"), 12, True)
        for k in kaynaklar:
            q = paragraf(d, k, KUCUK_PT, sonra=2)
            q.paragraph_format.left_indent = Cm(0.8)
            q.paragraph_format.first_line_indent = Cm(-0.8)

    eksik = [n for n, _, _ in FIGS if n not in sekil_sirasi]
    if eksik:
        print("UYARI — yerlesmeyen sekil:", eksik)
    os.makedirs(os.path.dirname(CIKTI), exist_ok=True)
    d.save(CIKTI)
    print("%s yazildi (%.1f MB)" % (CIKTI, os.path.getsize(CIKTI) / 1e6))
    print("yerlesen sekil: %d / %d" % (len(sekil_sirasi), len(FIGS)))


    # --- EK BELGE, ayni bicimde ----------------------------------------
    # Dergi ek malzemeyi ayri dosya olarak istiyor. Ayni donusturucuden
    # geciyor ki ana belgeyle ayni bicimde olsun.
    e = kur()
    p = e.add_paragraph(); p.paragraph_format.space_after = Pt(10)
    yazitipi(p.add_run("Supplementary Material"), 16, True)
    p = e.add_paragraph(); p.paragraph_format.space_after = Pt(12)
    satir_isle(p, "for *The Architectural Cost of Hybrid VTOL: meryemAircraft, "
                  "a Propeller-Driven Tail-Sitting Blended-Wing-Body Without a "
                  "Dedicated Lift System*", GOVDE_PT)
    for t, i in bloklar(open(EK_KAYNAK, encoding="utf-8").read()):
        if t.startswith("h"):
            duzey = int(t[1])
            q = e.add_paragraph()
            q.paragraph_format.space_before = Pt(10 if duzey <= 2 else 8)
            q.paragraph_format.space_after = Pt(4)
            yazitipi(q.add_run(i.strip()), 13 if duzey == 1 else 11, True)
        elif t == "p":
            paragraf(e, i)
        elif t == "t":
            tablo_ekle(e, i)
    e.save(EK_CIKTI)
    print("%s yazildi (%.1f MB)" % (EK_CIKTI, os.path.getsize(EK_CIKTI) / 1e6))
