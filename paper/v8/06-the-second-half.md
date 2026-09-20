# Step 6 — The second half: cruise carried on a wing

**v8 taslağı, birinci yazım.** İskeletin 6. adımı. Rakip **çok rotorlu**, ve **yalnız bu
eksende.** Adım 5'in simetriği.

**Kural denetimi:** sabit kanatlıya karşı **hiçbir menzil ya da verim karşılaştırması yok**
(§0, birinci yasak hata) · *"inşa gereği"* geçmiyor · **boyutlandırıldı / gösterilmedi**
ayrımı Adım 5'teki gibi ortada · karşılaştırma **tek bir birimde** yapılıyor.

**Bu sayfa yazılırken bir hesap yapıldı ve bir iddia daraldı.** Makale çok rotorlu
karşılaştırmasını iki **farklı türden** sayıyla yapıyordu: NASA'nın *etkin* L/De = 4,9'u ile
bizim *aerodinamik* 8,8–10,8'imiz. İkisi aynı birime çevrilince pay **+%80…+%121'den
+%14…+%51'e** iniyor, ve bir köşede işaret dönüyor. Hesap: `aero/effective_ld.py`,
kayıt: `paper/effective-ld-finding.md`. **Sayfa düzeltilmiş sayıyla yazıldı.**

---

## The second half: cruise carried on a wing

### The opponent, and the axis

On this axis the alternative is the multirotor, and as in the previous section the comparison
runs one way only. **Nothing here is claimed against fixed-wing aircraft.** A runway-launched
aeroplane cruises more efficiently than this configuration and pays none of the charges of
Section 2; that comparison is not made, and no result in this paper rests on it. The claim is
confined to the one thing the multirotor family structurally lacks: **a surface that carries the
cruise lift.**

### What the requirement is

Section 5 established the first half: the aircraft must leave from and return to a site that
supplies nothing. **A multirotor meets that requirement completely.** It is not a deficient
machine and this section does not treat it as one; it is excellent at what it does and is
limited by the price of doing it that way.

What it does not meet is the second half of both missions. Wildfire observation and response,
and cargo delivery to places without a runway, each require the aircraft to **cover distance
after it has left the unprepared site**, and a vehicle with no wing buys every second of that
distance with installed power. The consequence has been stated independently: surveying the
field, one study concludes that multirotors are efficient in hover and suited to short-range
missions, while vectored-thrust aircraft are efficient in cruise and suited to long-range ones.

### What the configuration does instead

Cruise lift is carried by the blended wing body — the whole planform, since there is no
separate fuselage — while the nose pair produces only the thrust needed to balance drag. **This
is a structural difference rather than a margin.** Lift is carried on a surface or it is carried
on rotors, and no sizing contract, no assumption in this paper and no choice available to a
designer moves a vehicle between those two states. It is the one claim in this work that is a
property of the configuration rather than of a calculation.

### What the margin actually is, in one currency

The structural statement is worth little without a number, and the number has to be given in a
single unit or it is not a comparison at all.

The sizing set of Section 4 reports an **effective lift-to-drag ratio**, defined in its own
nomenclature as `L/De = WV/P`: weight times speed over power. That is a system figure of merit,
not a force ratio, and it already contains the propulsive efficiency of whatever produces the
thrust. **A force ratio cannot be placed beside it.** Converting this configuration's
aerodynamic lift-to-drag ratio into the same quantity is one line — in level cruise thrust
equals drag and lift equals weight, so with shaft power `P = DV/η_p`,

> **L/De = WV/P = (L/D) · η_p**

and both factors are computed rather than assumed. The aerodynamic ratio is 8.80 to 10.82 across
the zero-lift drag bracket, **with the tip frames and the free-wheeling attitude rotors already
charged**; the propeller efficiency is 0.632 to 0.683 from a two-point blade-element solution of
the actual nose blade at its actual hover and cruise conditions. The product is **5.56 to 7.39**.

| | L/De |
|---|---:|
| This configuration, adverse corner | **5.56** |
| This configuration, favourable corner | **7.39** |
| Quadrotor, turboshaft | 4.9 |
| Quadrotor, all-electric | 5.8 |

**Against the quadrotor that uses the same kind of energy source, the sign holds at every
corner**, by 14 to 51 percent. The margin is not fragile: closing it would require the
propeller efficiency to fall to 0.557 against a computed worst case of 0.632.

**Against the all-electric quadrotor in the same set it does not hold at the adverse corner**,
and this is stated rather than arranged around. That vehicle reaches 5.8, above this
configuration's 5.56. It buys the difference with 1 742 lb of battery and **nearly twice the
gross weight for the same mission** — 7 221 lb against the turboshaft quadrotor's 3 678 lb —
which is precisely the charge Section 2 describes and Section 4 tests. But on cruise efficiency
taken alone, it is ahead of this configuration's worst case.

**So the honest form of the second claim is narrower than the structural statement invites.**
Wing-borne cruise is a different way of carrying lift, and it is worth 14 to 51 percent in this
comparison — not a change of category. And what compresses it is not the wing. **It is this
aircraft's own refusal of the variable-pitch hub**: at a propeller efficiency of 0.85 the same
airframe would reach 7.48 to 9.20. The margin is a property of the propeller choice as much as
of the architecture, and Section 11 charges it as such.

### Three qualifications, all of which run against this configuration

They are given together because omitting any one of them would make the comparison look better
than it is.

**Scale.** The compared vehicles are 1 670 to 3 275 kg; the designs here are 50 kg and 1 000 kg.
Reynolds number favours the larger aircraft, so the smaller design is at a disadvantage in this
comparison rather than an advantage.

**The quadrotor is a good quadrotor.** Its disc loading is 3.5 lb ft⁻², which is unusually low
and unusually efficient. Nothing here is compared against a poor example.

**The speeds are not matched.** The published figure is quoted at the best-range speed; this
configuration's is at its chosen cruise condition, 1.49 times stall, which Section 10 states
explicitly is **not** its best lift-to-drag point. Cruising at the best point would leave too
little margin, and the ratio that the chosen condition gives is the one reported.

### What is sized, and what is not demonstrated

**Sized.** The drag build-up and its bracket; the lift-to-drag ratio at the cruise condition
from the drag polar; the propeller efficiency from blade-element momentum theory at two
operating points; and the range that follows from the chain, link by link.

**Not demonstrated.** **No part of this has been measured.** There is no wind-tunnel test and no
flight test in this work, and the drag coefficient is a build-up with a declared bracket rather
than a measurement. The planform's sweep, taper and thickness distributions were chosen rather
than optimised. The span efficiency of 0.85 is an assumption which the paper's own calculation
puts at 0.817 — optimistic by 3.9 percent. And **the aerodynamics above roughly ten degrees of
incidence are not reliable for anyone on this class of configuration**: three methods of three
fidelities depart at the same place, the highest of them against wind-tunnel measurement. That
limit does not touch the cruise numbers above, which sit at a few degrees, but it bounds what
this section may be read to support.

### What this half costs

The wing that makes cruise efficient is carried through the vertical phase, where it produces
nothing and presents the aircraft's largest surface to ground wind. The tailless planform that
follows from having no boom constrains the sweep, because with no horizontal stabiliser the
pitching moment must come from the distribution of lift along the body itself. And the
fixed-pitch propeller that serves both regimes is the reason the margin above is 14 to 51
percent rather than more. Section 11 charges all three.

**The two halves are now on the table separately. Section 7 is where they are combined**, and
the combination is what this paper is for.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| Çok rotorlu piste ihtiyaç duymuyor; eksik makine değil | §1, satır 160–163 |
| Kanatsız araç her saniyeyi kurulu güçle satın alıyor | §1, satır 161–163 |
| *"Multirotors are efficient in hover and suited to short-range missions…"* | §4.2, satır 2478–2481 |
| Kaldırma bir yüzeyde mi rotorda mı — yapısal, sözleşme değiştirmez | §4.2, satır 2504–2506 |
| **`L/De = WV/P` tanımı** | Johnson & Silva 2022, gösterim listesi s. 94 — **birinci elden** |
| **L/De propulsor verimini İÇERİR** (η_h/FM simetrisinden kanıtlandı) | aynı belge, denklem 2 (s. 645) ve denklem 3 (s. 658); `paper/effective-ld-finding.md` §2 |
| Aerodinamik L/D 8,80–10,82, rotorlar ve uç çerçeveleri **faturalanmış** | §3.6 Tablo 9, satır 1511; *"the tip frames and the free-wheeling rotors charged to this configuration alone"* satır 1500; braket §3.10 / Ek S1 |
| η_p = 0,632–0,683, iki noktalı BEMT | `paper/nose-pair-finding.md`, `paper/chain-resolve-finding.md` |
| **L/De = 5,56–7,39** | `aero/effective_ld.py`, `aero/effective-ld-result.txt` |
| Quadrotor turboşaft L/De 4,9; DGW 3.678 lb; disk yüklemesi 3,5 lb/ft² | NASA Tablo 3, s. 70 — **birinci elden** |
| Sayı **Vbr**'de, yani *"best-range speed"* | aynı belge s. 386: *"Cruise is flown at best-range speed (Vbr, 99% high side)"* — **birinci elden** |
| Quadrotor elektrik L/De 5,8; DGW 7.221 lb; batarya 1.742 lb | NASA Tablo 3, s. 70 — **birinci elden** |
| Payın kapanması için gereken η_p = 0,557; hesaplanan en kötü 0,632 | `aero/effective-ld-result.txt` |
| η_p = 0,85 olsaydı L/De 7,48–9,20 | aynı betik, `lde(8.80, .85)` ve `lde(10.82, .85)` |
| Karşılaştırılan araçlar 1.670–3.275 kg | NASA Tablo 3, DGW satırı |
| Seyir 1,49 × stall, **en iyi L/D noktası değil**; L/D_max 25,3 m/s'de, stall'ın 1,26 katı | §2.12, satır 971–977 |
| Hiçbir rüzgâr tüneli, hiçbir uçuş denemesi yok | §4.4, satır 2549 |
| Planform süpürme/incelme/kalınlık **seçildi, optimize edilmedi** | §4.5, satır 2656–2658 |
| Açıklık verimi 0,85 varsayım; hesabı 0,817, **%3,9 iyimser** | §4.5, satır 2658–2660 |
| On derece üstünde üç yöntem üç aslılıkta sapıyor; en yükseği ölçüme karşı | §3.17, satır 2400–2408; §4.4, satır 2647–2650 |
| Kuyruksuz planform süpürmeyi kısıtlıyor; yunuslama momenti gövdeden | §2.8, satır 741–743 |

**Bu sayfada BİLEREK olmayanlar:**

- **Çok rotorluya karşı hiçbir MENZİL sayısı.** Bu çalışmada boyutlandırılmış bir çok rotorlu
  yok; karşılaştırma yalnız seyir verimi ekseninde ve yalnız yayımlanmış boyutlandırma
  setinin sayılarıyla yapılıyor. Menzil karşılaştırması iddia edilse uydurma olurdu.
- **Sabit kanatlıya karşı hiçbir şey.** §0'ın birinci yasak hatası.
- **"Farklı verim sınıfı" (different efficiency class) ifadesi.** +%14 bir sınıf farkı
  değildir; hesap bunu gösterdi ve ifade kullanılmıyor.
- **Bizim kütle üstünlüğümüz.** Çok rotorluya karşı kütle bu sayfanın ekseni değil; Fatura 1
  Adım 2'de kuruluyor, ölçülüyor Adım 11 ve 12'de.
