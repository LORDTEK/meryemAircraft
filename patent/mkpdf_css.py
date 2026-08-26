CSS = """
@page { size: A4; margin: 25mm 20mm 20mm 25mm; }
body { font-family: 'DejaVu Serif','Times New Roman',serif; font-size: 11.5pt;
       line-height: 1.75; color: #000; margin:0; }
h1 { font-size: 13pt; text-align:center; margin: 0 0 14mm 0; letter-spacing:.4px; }
h2 { font-size: 11.5pt; margin: 9mm 0 3mm 0; text-transform: uppercase; letter-spacing:.6px; }
h3 { font-size: 11.5pt; margin: 6mm 0 2mm 0; font-style: italic; font-weight: normal; }
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
.fig { page-break-after: always; text-align:center; }
.fig:last-child { page-break-after: auto; }
.fig img { max-width: 165mm; max-height: 225mm; }
.fig .cap { font-size: 12pt; font-weight:bold; text-align:left; margin-bottom:6mm; }
"""
