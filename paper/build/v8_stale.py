# -*- coding: utf-8 -*-
"""v8 ADIMLARININ INGILIZCE GOVDELERINDE EMEKLI IFADE VE SAYI DENETIMI.

NEDEN VAR (CLAUDE.md §3.1). verify.py'nin bayat deger listesi yalniz v7'nin
bolumlerini tariyor. v8'de emekli ifadeler bugune kadar elle, grep ile
araniyordu; Tur 49'da "different efficiency class" Adim 9'da canli kaldi,
Tur 50'de duzeltilen betigin eski sayisi duzyazida kaldi. Bir ifade ya da
sayi emekliye ayrildiginda BURAYA eklenir, gerekcesi ve turuyla.

Taranan: paper/v8/NN-*.md dosyalarinin Ingilizce govdesi (ilk "## " baslik
ile "## Yazarın denetimi" arasi) ve ALL-STEPS.md. Turkce denetim tablolari
eski degerleri BILEREK alintilar; taranmazlar.

--sina: onceki commit'teki Adim 12 govdesini (Tur 55 oncesi) tarar ve
en az bir emekli degeri YAKALAMASI gerekir. Yakalamazsa denetim bozuktur.
"""
import glob
import os
import re
import subprocess
import sys

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

EMEKLI = {
    "0.0051": "Tur 55: agir rotor terimi kurulum hatasiyla (30 m/s dengesi, 40 m/s q'su; "
              "703 m/s tasarim uc hizi). Dogrusu 0.0068 (c_l 0,68), aralik 0.0045-0.0100",
    "0.0035": "Tur 55: eski agir aralik alt ucu (ayni hata)",
    "0.0074": "Tur 55: eski agir aralik ust ucu (ayni hata)",
    "a quarter and a half": "Tur 55: eski oran araligi 0,23-0,48; dogrusu 0,29-0,65",
    "blade thins": "Tur 55: emekli mekanizma -- dolgunluk artiyor (0,075 -> 0,100)",
    "σ R²": "Tur 55: emekli formul dC_D0 ~ sigma R^2/(qS); q sifir torkta sadelesir",
    "1.73 × 1.78": "Tur 54/55: izlenemeyen uc haneli uyum",
    "3.08": "Tur 54/55: izlenemeyen uc haneli uyum",
    "usual expectation": "Tur 55: kaynaksiz genelleme (Grok'un isaretiyle)",
    "move independently": "Tur 55: 'kilitlenmeme' gosterildi, bagimsizlik degil (ChatGPT)",
    "any ranking must": "Tur 55: fazla evrensel; baskin mimari tartisiz siralanir (ChatGPT)",
    "16.4 to 23.0": "Tur 55: betik 22,9 veriyor",
    "variable-pitch hub costs": "Tur 53/55: acik gobege atfedilemez; karsi-olgusal hesaplanmadi (ChatGPT)",
    "where it reverses": "Tur 55: Adim 13 tersine donmeyi zarfin yalniz yarisinda buldu",
    "reverses across the three contracts": "Tur 55: ayni",
    "will reverse when the sizing rule": "Tur 55: Adim 2'nin ongorusu 'will move ... and can reverse'",
    "not behind on either count": "Tur 55: tilt %0,5-5,4 agir; takas var, dengesiz",
    "behave as one quantity in three currencies": "Tur 56: Adim 12 ile celisiyordu; 'coupled'",
    "the whole of the fall": "Tur 56: modelin icinde ayristirma; '18 percent above'",
    "differ\nby some seventy points": "Tur 56: kayma kaldirma grubuna bagli (14-134)",
    "0.128 to 0.150": "Tur 56: mil-mil cikarmasi; bara tabaninda 0.168-0.188",
    "0.166 kW": "Tur 56: mil-mil; bara tabaninda 0.202",
    "yet measured on a flown pack": "Tur 56: 'yet' kaynaksiz genelleme; 1,5 kW/kg tezgahtaki 24S1P'de",
    "3.8 times": "Tur 56: Adim 10 kapanislarinda 3,7-4,1 kati (kalkis talebi, 1,49 kW/kg)",
    "none of its orderings rests on": "Tur 56: tampon agirlasinca siralamalar kayabilir; hesaplanmadi",
    "a factor of about four": "Tur 56: 3,8x'in tek evi Adim 14'un tek paragrafi (Grok)",
    "the aircraft exists and": "Tur 57: dongu kapaniyor; ucak degil (dort okuyucu)",
    "381 kg": "Tur 57: motor istasyon karisikligi; dogru istasyonla lift+cruise kapanmiyor",
    "Until that item is settled": "Tur 57: Adim 14 sonrasi 'notr' degil; 'ayni varsayim'",
    "What the obstacle does not touch": "Tur 57: 'reaches, and what it does not'",
    "own refusal of the variable-pitch hub": "Tur 57: Adim 6'da kalmisti; asiri atif (ChatGPT, Tur 53)",
    "the battery gap, the transition": "Tur 57: pist iddiasi depoya bagli (Adim 14)",
    "for anyone": "Tur 58: evrensel; 'for the methods used here' (Grok)",
    "0.85 the same airframe would reach 7.48": "Tur 51/58: 7.47; e degil eta_p (Grok, DeepSeek)",
    "configuration that\ncombines runway-independent": "Tur 58: 'sized to combine' (ChatGPT)",
    "configuration that combines runway-independent": "Tur 58: ayni",
    "one of the measured continuous ratings": "Tur 58: 'the unit pack's continuous rating' (DeepSeek)",
    "1.98 to 2.27": "Tur 59: alt uc 50 kg referans geometrisi; kapanislar 2.07-2.27 (Grok'un 8/10 isaretiyle)",
    "3.45 to 3.70": "Tur 59: ayni; 3.53-3.70",
    "1.20 to 1.29": "Tur 59: ayni; 1.23-1.29",
    "regime change is made": "Tur 59: P1'in emekli fiili; 'arranged to change regime' (Grok)",
    "change of regime is then made": "Tur 59: ayni, Adim 7",
    "tip pairs do not lift": "Tur 59: Adim 5 ile celisiyor; kalkis payini uc ciftleri veriyor",
    "so they fail the second row": "Tur 59: ayni paragrafta 'not the second row' (DeepSeek); birinci basarisizlik kipi",
    "inventory in Section 8": "Tur 59: 'Sections 7 and 8' (Grok, DeepSeek)",
    "masses of 52 to 58 kg": "Tur 59: 52.3-57.5 (Grok)",
    "attitude hardware does not violate it": "Tur 60: Adim 8/7 ile celisiyordu; birinci basarisizlik kipi (DeepSeek)",
    "that row concerns a propulsor whose": "Tur 60: ikinci satiri dar tarif ediyordu (DeepSeek)",
    "producing moments rather than thrust": "Tur 60: 'cruise thrust' (Grok)",
    "between 52 and 58 kg": "Tur 60: 52.3-57.5 (DeepSeek)",
    "For the light design": "Tur 60: '50 kg reference design' (ChatGPT, DeepSeek)",
    "leads under every contract at every closure": "Tur 60: siralama dili; 'a size, not an order' (ChatGPT)",
    "Two things the loop does not scale": "Tur 60: uc disk capi da (Grok)",
    "different efficiency class": "Tur 49: emekliye ayrildi, Adim 9'da canli kalmisti",
    "14.29": "Tur 53: temiz govde L/D, drag_sweep.zincir pay hatasi; dogrusu 15.24",
    "10.28": "Tur 50: e = 0,85 ile L/D_max; e = 0,817 ile 10.08",
    "range of a fixed-wing": "CLAUDE.md §0.3: sabit kanatla menzilde yarisilmaz",
    "general architectural superiority": "CLAUDE.md §0: bu cumle bir daha yazilmaz",
    "does not pay in any of the three currencies": "Tur 80: pivot kilogramla odeniyor (3B, S4); 'pays part of its cost in none' (Grok P26)",
    "is not a counter-example — the tilting row": "Tur 81: kosulsuz muafiyet; taban adlandirildi (S5-1, Grok P30)",
    "Bill 3 is left standing": "Tur 81: tabansiz goreli ifade; 2E'de 'imposed or left standing', 3B'de 'incurred' (S5-3/4, Grok P30)",
    "itself mass, complexity": "Tur 81: 'complexity' Tur 65'te emekli; S3'te kalmisti (Claude'un Tur 65 kacirmasi)",
    "tilt-wing is the transfer property": "Tur 82: #18 ile ayni daraltma; 'is consistent with' (Grok P32)",
    "The charges exist because the two regimes": "Tur 84: S-6 -- uc ozellik, dort sapma; R1 dort sayar (DeepSeek: geri gelmesin)",
    "sizing point leaves Bill 3": "Tur 84: goreli kelime; 'incurs' (R6)",
    "moves* the charge": "Tur 80: mekanizma fatura degil, maliyet (Qwen; dort okuyucu)",
}


def govde(metin):
    m = re.search(r"^## (?!Yazar)", metin, re.M)
    t = re.search(r"^## Yazarın denetimi", metin, re.M)
    if not m:
        return ""
    return metin[m.start():t.start() if t else len(metin)]


def tara(adlar_metinler):
    bulunan = []
    for ad, metin in adlar_metinler:
        duz = re.sub(r"\s+", " ", metin)   # Tur 59: satir kirilmasi aramayi kacirmasin
        for k, neden in EMEKLI.items():
            if re.sub(r"\s+", " ", k) in duz:
                bulunan.append((ad, k, neden))
    return bulunan


def dosyalar():
    out = []
    for f in sorted(glob.glob(os.path.join(KOK, "paper", "v8", "[0-9][0-9]-*.md"))):
        out.append((os.path.basename(f), govde(open(f, encoding="utf-8").read())))
    hepsi = os.path.join(KOK, "paper", "v8", "ALL-STEPS.md")
    if os.path.exists(hepsi):
        out.append(("ALL-STEPS.md", open(hepsi, encoding="utf-8").read()))
    return out


if __name__ == "__main__":
    if "--sina" in sys.argv:
        eski = subprocess.run(
            ["git", "-C", KOK, "show", "d64d4ea:paper/v8/12-the-bills-separate.md"],
            capture_output=True, text=True, check=True).stdout
        b = tara([("12 (d64d4ea, Tur 55 oncesi)", govde(eski))])
        print("SINAMA: eski Adim 12 govdesinde %d emekli deger yakalandi" % len(b))
        for ad, k, _ in b:
            print("   yakalandi: %r" % k)
        if not b:
            sys.exit("!! Denetim eski hatayi YAKALAMADI -- denetim bozuk.")
    b = tara(dosyalar())
    print("=== v8 EMEKLI IFADE/SAYI DENETIMI ===")
    if b:
        for ad, k, n in b:
            print("  !! %s icinde %r -- %s" % (ad, k, n))
        sys.exit("Emekli deger bulundu.")
    print("  ok  %d emekli degerin hicbiri %d govdede gecmiyor."
          % (len(EMEKLI), len(dosyalar())))
