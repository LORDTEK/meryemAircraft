CSS = """
@page { size: A4; margin: 25mm 20mm 20mm 25mm; }
/* Govde genisligi BASKI alaniyla ayni olacak sekilde SABITLENDI.
   Neden: satir numaralari, satir kutulari tarayicida olculerek
   konuluyor. Genislik sabitlenmezse tarayici gorunum alanina (1280 px)
   gore dizer, PDF ise A4 baski alanina (210 - 25 - 20 = 165 mm) gore --
   yani satir sonlari FARKLI olur ve numaralar kayar. Olculdu: numaralar
   ilerledikce 1-2 satir asagi kayiyordu. Genislik sabitlenince iki
   dizgi ayni olur. */
body { font-family: 'DejaVu Serif','Times New Roman',serif; font-size: 11.5pt;
       line-height: 1.75; color: #000; margin:0; width: 165mm; }
h1 { font-size: 13pt; text-align:center; margin: 0 0 14mm 0; letter-spacing:.4px; }
h2 { font-size: 11.5pt; margin: 9mm 0 3mm 0; text-transform: uppercase; letter-spacing:.6px; }
h3 { font-size: 11.5pt; margin: 6mm 0 2mm 0; font-style: italic; font-weight: normal;
     page-break-after: avoid; break-after: avoid; }
h2 { page-break-after: avoid; break-after: avoid; }
table { page-break-inside: avoid; break-inside: avoid; }
p  { margin: 0 0 2.6mm 0; text-align: justify; }
.pn { display:inline-block; width:16mm; color:#000; }
.f  { font-family:'DejaVu Sans Mono',monospace; font-size:10.5pt; text-align:center;
      margin:3mm 0 3.4mm 0; }
table { border-collapse: collapse; margin: 3mm 0 4mm 0; font-size: 10.5pt; }
td { border: 0.6pt solid #000; padding: 1.2mm 3mm; }
ol.claims { list-style:none; padding:0; margin:0; counter-reset: c; }
ol.claims > li { counter-increment: c; margin: 0 0 5mm 0; text-align: justify; }
ol.claims > li::before { content: counter(c) ". "; font-weight: bold; }
ul { margin: 2mm 0 3mm 8mm; padding:0; }
li.sub { margin-bottom: 2mm; text-align: justify; }
.center { text-align:center; }

/* --- Sekli inceleme bildirimi (2026/014570) uzerine eklendi --- */

/* Bolumler tek belgede dizilir ama her biri yeni sayfada baslar; boylece
   sayfa numaralari surekli akar ve bolum sinirlari sayfa sinirina denk
   gelir (bkz. mkpdf.belge). */
.bolum.yeni { break-before: page; page-break-before: always; }

/* Satir numarasi olugu. PCT Kural 11.8 satir numaralarinin "sol tarafta,
   kenar boslugunun SAGINDA" olmasini soyler -- yani metin alaninin
   icinde. Bu yuzden sayfa kenar boslugu (25 mm) DEGISTIRILMEDI; metin
   9 mm iceri alindi ve numaralar o oluga kondu. */
.gov { position: relative; padding-left: 9mm; }

/* Unsur basligi: TARIFNAME / ISTEMLER / OZET. Kilavuz (s.13 ve s.15)
   bu ifadenin sayfanin EN BASINA, bulus basliginin ise ONUN ALTINA
   yazilmasini istiyor; s.18'deki sema da ayni sirayi gosteriyor.
   Ilk surumde baslik ustte, unsur adi altta idi -- ters cevrildi. */
.unsur { text-align: center; font-size: 12pt; font-weight: bold;
         letter-spacing: 1.2px; margin: 0 0 7mm 0; break-after: avoid; }
.unsur + h1 { margin-top: 0; }
.satirno { position: absolute; left: 0; width: 6mm; text-align: right;
           font-size: 9pt; line-height: 1; color: #000; }
.fig { page-break-after: always; text-align:center; }
.fig:last-child { page-break-after: auto; }
.fig .holder { height: 222mm; display:flex; align-items:center; justify-content:center; }
.fig img { max-width: 172mm; max-height: 218mm; }
.fig .cap { font-size: 12pt; font-weight:bold; text-align:left; margin-bottom:6mm; }
"""
