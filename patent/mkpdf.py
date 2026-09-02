# -*- coding: utf-8 -*-
import asyncio, sys, os, base64, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from playwright.async_api import async_playwright
from mkpdf_css import CSS
from tarifname_icerik import TARIFNAME, BASLIK
OUT="/home/user/meryemAircraft/patent/pdf"; os.makedirs(OUT,exist_ok=True)
RES="/home/user/meryemAircraft/patent/resimler"
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
E=html.escape

def page(inner,title):
    return f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><title>{E(title)}</title><style>{CSS}</style></head><body><div class='gov'>{inner}</div></body></html>"


def belge(*bolumler):
    """Bolumleri TEK belgede birlestirir; her biri yeni sayfada baslar.

    Neden: TURKPATENT sekli inceleme bildirimi (2026/014570) "Tarifname,
    Istemler ve Ozet bolumlerinde birbirini takip eden sayfa
    numaralandirmasi" istiyor. Bolumler ayri ayri basildiginda numaralar
    her seferinde 1'den basliyordu (8/8, 3/3, Ozet'te hic yok). Cozum:
    uc bolum tek belge olarak dizilir, sayfa numaralari surekli akar,
    sonra page_ranges ile ayri dosyalara BOLUNUR -- numaralar bolunurken
    korunur.
    """
    ic = "<div class='bolum'>" + "</div><div class='bolum yeni'>".join(bolumler) + "</div>"
    return ("<!doctype html><html lang='tr'><head><meta charset='utf-8'>"
            "<title>Basvuru</title><style>" + CSS + "</style></head>"
            "<body><div class='gov'>" + ic + "</div></body></html>")

# ---------- TARIFNAME ----------
# Kilavuz (Patent kilavuz 2022, s.13): "Tarifnamenin en basina
# 'TARIFNAME', bunun altina da 'Bulus Basligi' yazilmalidir."
# s.18'deki sema da ayni sirayi gosteriyor: once TARIFNAME, altinda baslik.
n=0; parts=[f"<h2 class='unsur'>TARİFNAME</h2><h1>{E(BASLIK)}</h1>"]
for kind,val in TARIFNAME:
    if kind=="h2":  parts.append(f"<h2>{E(val)}</h2>")
    elif kind=="h3":parts.append(f"<h3>{E(val)}</h3>")
    elif kind=="f": parts.append(f"<div class='f'>{E(val)}</div>")
    elif kind=="tbl":
        rows="".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td></tr>" for a,b in val)
        parts.append(f"<table>{rows}</table>")
    else:
        n+=1
        parts.append(f"<p><span class='pn'>[{n:04d}]</span>{E(val)}</p>")
TARIF_IC="".join(parts)
TARIF_HTML=page(TARIF_IC,"Tarifname")

# ---------- ISTEMLER ----------
ISTEM=[
"Gövdesi (1) kanat-gövde biçiminde olan, boyuna ekseni dikey konumda yere oturan, itkisi koaksiyel karşıt dönüşlü pervane çiftleriyle üretilen ve hareketli kumanda yüzeyi bulunmayan bir insansız hava aracı olup, özelliği; aracın tüm itki gücünün, gövdenin (1) burun ucunda bulunan tek bir koaksiyel karşıt dönüşlü pervane çifti (2) tarafından üretilmesi, bu çiftin dikey uçuşta ve seyir uçuşunda gövdeye göre aynı yönelimde çalışması ve itki organının açıklık boyunca dağıtılmamış olması; gövdenin (1) alt yüzeyinde, planform düzleminde gövde eksenine göre açılı olarak arkaya ve dışa uzanan, açık ve kapalı olmak üzere iki konumu bulunan bir yuvarlanma şeridi (5) bulunması; ve söz konusu şeridin (5) iç kısmının, burun pervane çiftinin (2) izi (13) içinde, dış kısmının ise bu izin dışında kalacak biçimde konumlandırılmış olması ile karakterize edilmesidir.",
"İstem 1'e uygun hava aracı olup, özelliği; şeridin (5) gövde eksenine göre yaptığı açının yaklaşık 45 derece olmasıdır.",
"İstem 1 veya 2'ye uygun hava aracı olup, özelliği; şeridin (5) planformdaki uzunluğunun kök veterinin en az yüzde 100'ü olmasıdır.",
"Önceki istemlerden herhangi birine uygun hava aracı olup, özelliği; şeridin (5) açıldığındaki yüksekliğinin iç uçtan dış uca doğru artmasıdır.",
"Önceki istemlerden herhangi birine uygun hava aracı olup, özelliği; şeridin (5) iki yarıda simetrik olarak bulunması ve yuvarlanma momentinin bir yarının açılıp diğerinin kapalı kalmasıyla üretilmesidir.",
"Önceki istemlerden herhangi birine uygun hava aracı olup, özelliği; kanat uçlarında planform düzlemine dik olarak yukarı (3a) ve aşağı (3b) uzanan uç iskeletleri (3) ve bu iskeletlerin uçlarında dört adet koaksiyel karşıt dönüşlü pervane çifti (4) bulunmasıdır.",
"İstem 6'ya uygun hava aracı olup, özelliği; uç pervane çiftlerinin (4) kaldırmaya katkı vermeyecek, yalnızca yönelim momenti üretecek biçimde boyutlandırılmış olması ve toplam güç talebinin askı gücünün yüzde 15'inden az olmasıdır.",
"İstem 6 veya 7'ye uygun hava aracı olup, özelliği; uç iskeletlerinin (3), pervane bağlantı yapısı, kumanda momenti kolu ve yere oturma yapısı işlevlerini birlikte görmesidir.",
"İstem 6 ilâ 8'den herhangi birine uygun hava aracı olup, özelliği; uç iskeletlerinin (3) her yöndeki uzama miktarının yerel uç veterinin en az iki katı olmasıdır.",
"Önceki istemlerden herhangi birine uygun hava aracı olup, özelliği; uç iskeletlerinin (3) dört alt ucu ve gövdenin (1) firar kenarından geriye uzanan bir orta omurganın (6) arka ucu olmak üzere beş noktadan yere oturmasıdır.",
"Önceki istemlerden herhangi birine uygun hava aracı olup, özelliği; gövdenin (1) hücum kenarı ok açısının kökten uca azalması ve firar kenarı ok açısının sabit olmasıdır.",
"Önceki istemlerden herhangi birine uygun hava aracı olup, özelliği; bir yakıt deposu (11), bu depodan beslenen bir içten yanmalı motor (7), bu motor tarafından döndürülen bir jeneratör (8), bu jeneratörden beslenen ve pervane çiftlerini süren elektrik motorları (10) ve askı anındaki güç tepesini karşılayan bir pil tamponu (9) içermesidir.",
"İstem 12'ye uygun hava aracı olup, özelliği; içten yanmalı motorun (7) hiçbir pervaneye mekanik olarak bağlı olmaması ve askı gücünün üçte birinden küçük bir güce göre boyutlandırılmış olmasıdır.",
"İstem 12 veya 13'e uygun hava aracı olup, özelliği; pil tamponunun (9) kütlesinin azami kalkış kütlesinin yüzde 5'inden az olmasıdır.",
"Önceki istemlerden herhangi birine uygun hava aracı olup, özelliği; burun pervane çiftinin (2) her bir pervanesinin (2a, 2b) kendi elektrik motoruyla (10) sürülmesi ve iki pervane arasında mekanik dişli bağlantısı bulunmamasıdır.",
"Önceki istemlerden herhangi birine uygun hava aracı olup, özelliği; pervanelerin sabit geometrili olması, devirli hatve ve toplu hatve düzeneği bulunmamasıdır.",
"Önceki istemlerden herhangi birine uygun bir hava aracının çalıştırılmasına ilişkin yöntem olup, özelliği; dikey uçuştan yatay uçuşa geçişin, aracın tırmanışı kesilmeden başlatılması ve giriş anındaki tırmanış hızının dönüş süresince dikey momentum rezervi olarak kullanılmasıdır.",
]
ist="".join(f"<li>{E(t)}</li>" for t in ISTEM)
# Kilavuz (s.13): "Istem sayfasinin basina SADECE 'ISTEMLER' ifadesi
#  yazilmalidir." -> baslik tekrarlanmiyor.
ISTEM_IC=f"<h2 class='unsur'>İSTEMLER</h2><ol class='claims'>{ist}</ol>"
ISTEM_HTML=page(ISTEM_IC,"İstemler")

# ---------- OZET ----------
OZ=('Buluş, dikey kalkış ve iniş yapabilen, seyir uçuşunu kanat üzerinde gerçekleştiren insansız hava araçları ile ilgilidir. Koaksiyel karşıt dönüşlü pervane çiftleriyle donatılmış, kuyruğa oturan hava araçlarında itki vektörleri gövde eksenine paralel olduğundan yuvarlanma momenti üretilemez; tepki torku da koaksiyel düzenleme nedeniyle ortadan kalktığından, bilinen diferansiyel tork çözümü de uygulanamaz. Buluşta, gövdenin (1) alt yüzeyinde arkaya ve dışa açılı uzanan, açık ve kapalı olmak üzere iki konumu bulunan bir yuvarlanma şeridi (5) yer alır. Şeridin iç kısmı, aracın tüm itkisini üreten burun koaksiyel pervane çiftinin (2) izi (13) içinde kaldığından hava hızı sıfır iken de moment üretir; dış kısmı ise izin dışında kalarak seyir uçuşunda çalışır. Böylece araç, hareketli kumanda yüzeyi taşımaksızın her uçuş rejiminde yuvarlanma kumandası elde eder. Buluş, pist gerektirmeyen gözetleme, kargo taşıma ve arama-kurtarma görevlerinde kullanılır.')
# Sekli inceleme bildirimi (2026/014570) uc sey istedi, ucu de burada:
#  - "Tarifname bolumunde bulunan bulus basligi, Ozet bolumune eklenmeli
#     ve AYNI olmalidir."  -> baslik ayni BASLIK degiskeninden geliyor,
#                             yani ayni olmasi kod tarafindan garanti.
#  - "Ozet bolumunde bulunan sekil cikartilmalidir."  -> gomulu PNG
#                                                       kaldirildi.
#  - "'Yayimlanacak sekil: Sekil 1' ibaresindeki 'Yayimlanacak sekil:'
#     kismi cikartilmalidir."  -> yalnizca "Şekil 1" kaldi.
# Kilavuz (s.15): "Ozetin en basina 'OZET', bunun altina da bulus
#  basligi yazilmalidir." -> sira OZET, sonra baslik. Ilk surumde
#  tersiydi; kilavuz okununca duzeltildi.
OZET_IC=("<h2 class='unsur'>ÖZET</h2><h1>" + E(BASLIK) + "</h1><p>" + E(OZ) +
         "</p><p class='center' style='margin-top:9mm'><b>Şekil 1</b></p>")
OZET_HTML=page(OZET_IC,"Özet")

# ---------- RESIMLER ----------
figs=[]
for i in range(1,6):
    b=base64.b64encode(open(f"{RES}/sekil-{i}.png","rb").read()).decode()
    figs.append(f"<div class='fig'><div class='cap'>Şekil {i}</div>"
                f"<div class='holder'><img src='data:image/png;base64,{b}'></div></div>")
RES_HTML=page("".join(figs),"Resimler")

# SATIR NUMARALANDIRMA -- tarayicida degil, URETILEN PDF UZERINDE.
#
# Ilk deneme satir kutularini tarayicida olcup mutlak konumlu div'lerle
# numara koyuyordu. IKI kez yanlis cikti ve ikisi de olculerek bulundu:
#
#  1) Tarayici, gorunum alani genisliginde (1280 px) diziyordu; PDF ise
#     A4 baski alaninda (165 mm). Satir sonlari farkli oluyordu.
#     Duzeltildi: govde genisligi 165 mm'ye sabitlendi (mkpdf_css).
#  2) Bu duzeltmeden sonra 1. sayfa tuttu ama 5. ve 8. sayfalar kaydi.
#     Nedeni: basliklardaki "break-after: avoid" kurallari sayfalama
#     sirasinda icerigi asagi itiyor, mutlak konumlu numaralar ise
#     belge koordinatinda kaliyor -- ikisi desenkron oluyor.
#
# Tahmin etmeyi birakip OLCULEN veriye gecildi: PDF uretilir, sonra
# pdftotext -bbox-layout ile HER SAYFADAKI GERCEK satir kutulari okunur
# ve numaralar reportlab ile o konumlara damgalanir. Boylece tarayicinin
# dizgisini tahmin etmeye gerek kalmaz.
SATIR_HER = 5          # her kacinci satir numaralanacak
SATIR_SAYFA_BASI = True  # True: her sayfada 5,10,15... (PCT Kural 11.8
                         #       "sets of five" uygulamasi)
                         # False: bolum boyunca surekli 5,10,15...


def satir_kutulari(pdf_yolu):
    """Her sayfadaki gercek satir kutulari: [[(yMin,yMax),...], ...]

    pdftotext -bbox-layout, PDF puntosu cinsinden ve sol-UST kokenli
    koordinat verir. Alt bilgi (sayfa numarasi) icerik alaninin disinda
    kaldigi icin ayiklanir -- yoksa satir sayilir.
    """
    import subprocess, re as _re, tempfile as _tf, os as _os
    g = _tf.mktemp(suffix=".xhtml")
    subprocess.run(["pdftotext", "-bbox-layout", pdf_yolu, g], check=True)
    metin = open(g, encoding="utf-8").read()
    _os.unlink(g)
    sayfalar = []
    for sayfa in _re.findall(r"<page width=\"([\d.]+)\" height=\"([\d.]+)\">(.*?)</page>",
                             metin, _re.S):
        gen, yuk, ic = float(sayfa[0]), float(sayfa[1]), sayfa[2]
        alt_sinir = yuk - 56.7          # 20 mm alt kenar boslugu
        satir = []
        for m in _re.finditer(r"<line xMin=\"([\d.]+)\" yMin=\"([\d.]+)\" "
                              r"xMax=\"([\d.]+)\" yMax=\"([\d.]+)\"", ic):
            y0, y1 = float(m.group(2)), float(m.group(4))
            if y0 >= alt_sinir:
                continue                 # alt bilgi satiri
            satir.append((y0, y1))
        satir.sort()
        # AYNI GORSEL SATIRDAKI kutulari birlestir. Tablolarda her hucre
        # ayri bir <line> olarak gelir; birlestirilmezse bir tablo satiri
        # iki-uc satir sayilir ve numaralar kayar. Olculdu: referans
        # numaralari tablosunda "10" 7. satira dusuyordu.
        birlesik = []
        for (y0, y1) in satir:
            if birlesik and y0 < birlesik[-1][1] - 2.0:
                birlesik[-1] = (birlesik[-1][0], max(birlesik[-1][1], y1))
            else:
                birlesik.append((y0, y1))
        sayfalar.append(dict(gen=gen, yuk=yuk, satir=birlesik))
    return sayfalar


def satir_numarala(giris, cikis, her=SATIR_HER, sayfa_basi=SATIR_SAYFA_BASI,
                   sol=None):
    """Uretilmis PDF'e satir numaralarini damgalar."""
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas as _cv
    import io
    sayfalar = satir_kutulari(giris)
    oku = PdfReader(giris)
    yaz = PdfWriter()
    n = 0
    for i, sf in enumerate(sayfalar):
        if sayfa_basi:
            n = 0
        tampon = io.BytesIO()
        c = _cv.Canvas(tampon, pagesize=(sf["gen"], sf["yuk"]))
        c.setFont("Helvetica", 9)
        # Numaralar SAGA yaslanir; bu x, numaranin SAG kenari.
        # 31 mm secildi: iki haneli numara ~27.8 mm'de basliyor, yani
        # kilavuzun (s.18) 2,5 cm asgari sol marjinin SAGINDA kaliyor;
        # metin ise 34 mm'de basladigi icin arada 3 mm bosluk var.
        # Ilk surumde 25 mm idi -- numaralar marjin ICINE tasiyordu
        # (olculdu: 21,5 mm). Kilavuz okununca duzeltildi.
        x = sol if sol is not None else 87.9      # 31 mm
        for (y0, y1) in sf["satir"]:
            n += 1
            if n % her:
                continue
            # reportlab kokeni sol-ALT; pdftotext sol-UST verir.
            c.drawRightString(x, sf["yuk"] - y1 + 2.0, str(n))
        c.save()
        tampon.seek(0)
        ust = PdfReader(tampon).pages[0]
        sayfa = oku.pages[i]
        sayfa.merge_page(ust)
        yaz.add_page(sayfa)
    with open(cikis, "wb") as f:
        yaz.write(f)


def pdf_bol(giris, parcalar):
    """parcalar: [(cikti_yolu, ilk, son)] -- 1 tabanli, kapali aralik."""
    from pypdf import PdfReader, PdfWriter
    oku = PdfReader(giris)
    for yol_, a, b in parcalar:
        yaz = PdfWriter()
        for k in range(a - 1, b):
            yaz.add_page(oku.pages[k])
        with open(yol_, "wb") as f:
            yaz.write(f)


def pdf_sayfa(yol):
    """Bir PDF'in sayfa sayisi (pdfinfo)."""
    import subprocess
    c = subprocess.run(["pdfinfo", yol], capture_output=True, text=True)
    for satir in c.stdout.splitlines():
        if satir.startswith("Pages:"):
            return int(satir.split()[1])
    raise RuntimeError("sayfa sayisi okunamadi: " + yol)


async def main():
    import tempfile
    MARJ = {"top": "25mm", "bottom": "20mm", "left": "25mm", "right": "20mm"}
    # Sayfa numarasi bicimi -- kilavuz s.15 ve s.18:
    #
    #   "Resim sayfalarinin numaralandirilmasi, DIGERLERINDEN FARKLI
    #    olmalidir. Bu numaralandirma, 'ilgili sayfanin numarasi / toplam
    #    resim sayfasi sayisi' seklinde olmalidir."
    #
    # Yani "n / toplam" bicimi RESIM sayfalarina ait; tarifname/istem/ozet
    # sayfalari ondan farkli, yani DUZ ARDISIK numara tasimali. s.18'deki
    # sema da bunu gosteriyor: metin sayfasinda altta ortada yalniz "1",
    # resim sayfasinda ustte "1/3".
    #
    # Ilk surumde metin sayfalari da "1 / 12" bicimindeydi -- ikisi ayni
    # oluyordu; kilavuz okununca duzeltildi.
    ALT = ("<div style='width:100%;font-size:9pt;font-family:serif;"
           "text-align:center;color:#000;padding-top:4mm'>"
           "<span class='pageNumber'></span></div>")
    # Resim sayfalari: "n/toplam", sema uyarinca sayfanin USTUNDE.
    RES_UST = ("<div style='width:100%;font-size:9pt;font-family:serif;"
               "text-align:right;color:#000;padding:6mm 20mm 0 0'>"
               "<span class='pageNumber'></span>/"
               "<span class='totalPages'></span></div>")
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = await b.new_page()

        async def bas(htm, cikti, araliklar=None, altbilgi=True):
            await pg.set_content(htm, wait_until="load")
            await pg.emulate_media(media="print")
            o = dict(path=cikti, format="A4", print_background=True, margin=MARJ)
            if araliklar:
                o["page_ranges"] = araliklar
            if altbilgi:
                o.update(display_header_footer=True,
                         header_template="<div></div>", footer_template=ALT)
            await pg.pdf(**o)

        # 1) Her bolumun KENDI sayfa sayisi olculur. Bolumler birlesik
        #    belgede yeni sayfada basladigi icin toplam, bolum bolum
        #    sayilarin toplamina esittir; sinirlar buradan cikar.
        gec = tempfile.mkdtemp()
        say = []
        for ad, htm in (("t", TARIF_HTML), ("i", ISTEM_HTML), ("o", OZET_HTML)):
            p = os.path.join(gec, ad + ".pdf")
            await bas(htm, p, altbilgi=False)
            say.append(pdf_sayfa(p))
        n1, n2, n3 = say
        print("  sayfa: tarifname %d, istemler %d, ozet %d  (toplam %d)"
              % (n1, n2, n3, n1 + n2 + n3))

        # 2) Uc bolum TEK belge olarak basilir -> sayfa numaralari
        #    surekli akar. Once satir numarasiz basilir, sonra gercek
        #    satir kutulari olculup numaralar damgalanir, en son
        #    parcalara bolunur.
        BIRLESIK = belge(TARIF_IC, ISTEM_IC, OZET_IC)
        ham = os.path.join(gec, "birlesik-ham.pdf")
        await bas(BIRLESIK, ham)
        num = os.path.join(gec, "birlesik.pdf")
        satir_numarala(ham, num)
        pdf_bol(num, [("%s/01-tarifname.pdf" % OUT, 1, n1),
                      ("%s/02-istemler.pdf" % OUT, n1 + 1, n1 + n2),
                      ("%s/03-ozet.pdf" % OUT, n1 + n2 + 1, n1 + n2 + n3)])
        print("  -> 01-tarifname.pdf (1-%d), 02-istemler.pdf (%d-%d), "
              "03-ozet.pdf (%d-%d)"
              % (n1, n1 + 1, n1 + n2, n1 + n2 + 1, n1 + n2 + n3))

        # 3) Resimler ayri: bildirimde adi gecmiyor, satir numarasi da
        #    istenmiyor; kendi numaralandirmasiyla basiliyor.
        await pg.set_content(RES_HTML, wait_until="load")
        await pg.emulate_media(media="print")
        await pg.pdf(path=OUT + "/04-resimler.pdf", format="A4",
                     print_background=True, margin=MARJ,
                     display_header_footer=True,
                     header_template=RES_UST, footer_template="<div></div>")
        print("  -> 04-resimler.pdf")
        await b.close()


asyncio.run(main())
