# -*- coding: utf-8 -*-
import asyncio, sys, os, base64, html
sys.path.insert(0,"/tmp/claude-0/-home-user-meryemAircraft/dec69a2c-0837-54ea-ab5a-1b131a81b67f/scratchpad")
from playwright.async_api import async_playwright
from mkpdf_css import CSS
from tarifname_icerik import TARIFNAME, BASLIK
S="/tmp/claude-0/-home-user-meryemAircraft/dec69a2c-0837-54ea-ab5a-1b131a81b67f/scratchpad"
OUT="/home/user/meryemAircraft/patent/pdf"; os.makedirs(OUT,exist_ok=True)
RES="/home/user/meryemAircraft/patent/resimler"
CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
E=html.escape

def page(inner,title):
    return f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><title>{E(title)}</title><style>{CSS}</style></head><body>{inner}</body></html>"

# ---------- TARIFNAME ----------
n=0; parts=[f"<h1>{E(BASLIK)}</h1>"]
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
TARIF_HTML=page("".join(parts),"Tarifname")

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
ISTEM_HTML=page(f"<h1>İSTEMLER</h1><ol class='claims'>{ist}</ol>","İstemler")

# ---------- OZET ----------
OZ=("Buluş, gövdesi (1) kanat-gövde biçiminde olan, boyuna ekseni dikey konumda yere oturan bir "
"insansız hava aracı ile ilgilidir. Aracın tüm itki gücü, gövdenin (1) burun ucundaki tek bir "
"koaksiyel karşıt dönüşlü pervane çifti (2) tarafından üretilir; bu çift dikey uçuşta ve seyirde "
"gövdeye göre aynı yönelimde çalışır ve itki organı açıklığa dağıtılmamıştır. Kanat uçlarındaki "
"iskeletlerin (3) uçlarına yerleştirilen dört koaksiyel çift (4) yalnızca yönelim momenti üretir. "
"Gövdenin (1) alt yüzeyinde, arkaya ve dışa açılı uzanan, açık ve kapalı iki konumu bulunan bir "
"yuvarlanma şeridi (5) yer alır; şeridin iç kısmı burun pervanesinin izi (13) içinde kaldığından "
"hava hızı sıfır iken de moment üretir, dış kısmı ise izin dışında kalarak seyirde çalışır. Böylece "
"araç, hareketli kumanda yüzeyi taşımaksızın her uçuş rejiminde yuvarlanma kumandası elde eder.")
_b1=base64.b64encode(open(f"{RES}/sekil-1.png","rb").read()).decode()
OZET_HTML=page(f"<h1>ÖZET</h1><p>{E(OZ)}</p>"
  f"<p class='center' style='margin-top:9mm;margin-bottom:3mm'><b>Yayımlanacak şekil: Şekil 1</b></p>"
  f"<div class='center'><img src='data:image/png;base64,{_b1}' style='max-width:132mm'></div>","Özet")

# ---------- RESIMLER ----------
figs=[]
for i in range(1,6):
    b=base64.b64encode(open(f"{RES}/sekil-{i}.png","rb").read()).decode()
    figs.append(f"<div class='fig'><div class='cap'>Şekil {i}</div>"
                f"<div class='holder'><img src='data:image/png;base64,{b}'></div></div>")
RES_HTML=page("".join(figs),"Resimler")

async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path=CHROME,args=["--no-sandbox"])
        pg=await b.new_page()
        for name,htm,ft in (("01-tarifname",TARIF_HTML,True),("02-istemler",ISTEM_HTML,True),
                            ("03-ozet",OZET_HTML,False),("04-resimler",RES_HTML,True)):
            await pg.set_content(htm,wait_until="load")
            await pg.emulate_media(media="print")
            opts=dict(path=f"{OUT}/{name}.pdf",format="A4",print_background=True,
                      margin={"top":"25mm","bottom":"20mm","left":"25mm","right":"20mm"})
            if ft:
                opts.update(display_header_footer=True,
                    header_template="<div></div>",
                    footer_template="<div style='width:100%;font-size:9pt;font-family:serif;"
                                    "text-align:center;color:#000;padding-top:4mm'>"
                                    "<span class='pageNumber'></span> / <span class='totalPages'></span></div>")
            await pg.pdf(**opts)
            print("  ->",name+".pdf")
        await b.close()
asyncio.run(main())
