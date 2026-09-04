# -*- coding: utf-8 -*-
"""Ag yakinsama endeksi (GCI) -- Celik ve ark., ASME JFE 130(7), 2008.

Yordamin kendisi standarttir; burada iki noktaya ozellikle dikkat edilir.

BIRINCISI, MERTEBE p ITERATIF COZULUR. Uc ag tam olarak ayni oranda
inceltilemedigi icin (r21 = 1,479, r32 = 1,453) p'nin kapali formu yoktur;
denklem

    p = |ln|e32/e21| + q(p)| / ln(r21),
    q(p) = ln( (r21^p - s) / (r32^p - s) ),   s = sign(e32/e21)

sabit nokta yinelemesiyle cozulur. Oranlar esit olsaydi q = 0 olurdu.

IKINCISI, ASIMPTOTIK ARALIK DENETIMI RAPORLANIR. GCI'yi hesaplamak, uc
noktanin bir yakinsama egrisine oturdugunu KANITLAMAZ. Denetim

    GCI32 / (r21^p * GCI21)  ~  1

birden belirgin saparsa sayilar hala asimptotik aralikta degildir ve
"GCI = %x" demek yaniltici olur. Betik bu orani her zaman basar.

s = -1 cikmasi (e32 ve e21 ters isaretli) SALINIMLI yakinsama demektir;
o durumda p guvenilmezdir ve ayrica uyarilir.
"""
import math


def _mertebe(e21, e32, r21, r32, tur=200, tol=1e-12):
    s = 1.0 if (e32 / e21) > 0 else -1.0
    p = 2.0
    for _ in range(tur):
        q = math.log((r21 ** p - s) / (r32 ** p - s))
        yeni = abs(math.log(abs(e32 / e21)) + q) / math.log(r21)
        if abs(yeni - p) < tol:
            p = yeni
            break
        p = yeni
    return p, s


def gci(N1, N2, N3, f1, f2, f3, ad="phi", boyut=3):
    """1 = EN INCE, 3 = en kaba. N hucre sayisi, f cozulen buyukluk.

    boyut: temsili hucre olcusunun ussu -- h = (1/N)^(1/boyut). Uc boyutlu
    ag icin 3, iki boyutlu icin 2. Yanlis boyut MERTEBEYI bozar ama dis
    degerlemeyi ve GCI'yi gorece az etkiler; Celik 2008'in iki boyutlu
    ornegi boyut=3 ile p = 2,30 veriyor, boyut=2 ile dogru degeri (1,53).
    Bu yuzden ayri parametredir ve varsayilana guvenilmez.
    """
    if not (N1 > N2 > N3):
        raise ValueError("N1 > N2 > N3 olmali (1 en ince)")
    u = 1.0 / boyut
    h1, h2, h3 = (1.0 / N1) ** u, (1.0 / N2) ** u, (1.0 / N3) ** u
    r21, r32 = h2 / h1, h3 / h2
    e21, e32 = f2 - f1, f3 - f2
    if e21 == 0:
        raise ValueError("f1 = f2; mertebe tanimsiz")
    p, s = _mertebe(e21, e32, r21, r32)
    f_ext = (r21 ** p * f1 - f2) / (r21 ** p - 1.0)
    ea21 = abs((f1 - f2) / f1)
    eext21 = abs((f_ext - f1) / f_ext)
    gci21 = 1.25 * ea21 / (r21 ** p - 1.0)
    ea32 = abs((f2 - f3) / f2)
    gci32 = 1.25 * ea32 / (r32 ** p - 1.0)
    asim = gci32 / (r21 ** p * gci21)
    return dict(ad=ad, r21=r21, r32=r32, p=p, s=s, f_ext=f_ext,
                ea21=ea21, eext21=eext21, gci21=gci21, gci32=gci32,
                asimptotik=asim, f1=f1, f2=f2, f3=f3)


def yaz(r):
    print("  %s" % r["ad"])
    print("    ag degerleri : ince %.7f   orta %.7f   kaba %.7f"
          % (r["f1"], r["f2"], r["f3"]))
    print("    inceltme     : r21 = %.4f   r32 = %.4f" % (r["r21"], r["r32"]))
    print("    mertebe p    : %.3f%s" % (r["p"],
          "" if r["s"] > 0 else "   ** SALINIMLI yakinsama (s=-1): p guvenilmez **"))
    print("    dis deger    : %.7f" % r["f_ext"])
    print("    yaklasik hata      e_a21   = %%%.3f" % (100 * r["ea21"]))
    print("    dis degerleme hata e_ext21 = %%%.3f" % (100 * r["eext21"]))
    print("    GCI21 = %%%.3f      GCI32 = %%%.3f"
          % (100 * r["gci21"], 100 * r["gci32"]))
    print("    asimptotik aralik: GCI32/(r21^p GCI21) = %.4f  %s"
          % (r["asimptotik"],
             "(1'e yakin -- aralikta)" if 0.85 <= r["asimptotik"] <= 1.15
             else "** 1'DEN UZAK -- asimptotik aralikta DEGIL **"))
