# Ön bilgi — başlık, özet, anahtar kelimeler, beyanlar

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

## Title

**The Architectural Cost of Hybrid VTOL: meryemAircraft, a
Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated
Lift System**

## Authors

Meryem Gülmen, Berke Gülmen, Ömer Gülmen

*[Kurum bağlantısı verilecekse eklenir; verilmezse dergiler "Independent
researcher" yazar. Sorumlu yazar ve e-posta, dergi seçildiğinde eklenecek.]*

---

## Abstract

Hybrid vertical take-off and landing (VTOL) aircraft combine runway independence with
wing-borne cruise and pay for it in cruise efficiency. This paper treats that cost as
architectural rather than as a defect of implementation, and develops it as an accounting
framework. The penalty is charged in three coupled currencies — the mass of hover hardware
carried through cruise, its drag when exposed in cruise, and a power system sized by a
condition holding for some two percent of the flight — and every known remedy reduces one
by raising another. The escape condition is then explicit: the penalty is charged whenever
hover and cruise are served by hardware that is not the same hardware, in the same
orientation, doing the same job. A second result is methodological: architectural
comparisons depend on the sizing contract chosen, and a fixed fuel fraction removes the
mass bill from the range column altogether, so three contracts are reported rather than
one.

meryemAircraft, an uncrewed tail-sitting blended-wing body, satisfies the escape condition
and serves as the case study: one coaxial pair at the nose gives all thrust in both
regimes, four small pairs at the tips give attitude moments only, and a deployable strip
gives the roll that body-parallel thrust cannot. Against a lift-plus-cruise layout, on
wind-tunnel drag, it closes the same mission at forty-two percent lower take-off mass and
seventeen percent greater range; against a tilting layout the comparison reverses between
contracts and no superiority is claimed. A three-dimensional solution bounds the zero-lift
drag with a measured uncertainty budget, and a component mass build-up closes the 50 kg
design conditionally and not the 1000 kg one.

The study is analytical, with no experimental validation of the configuration. The tip
propellers can turn the aircraft's rotational inertia through the transition but not, on
present evidence, its aerodynamic moment. Resolving that margin along the trajectory shows
the aircraft never reaches ninety degrees of incidence — the relative wind rotates with the
body — so the outstanding measurement is the pitching moment to some twenty-two degrees at low
dynamic pressure, together with trim at cruise. Transition controllability remains the
principal open requirement and is stated as a threshold a future measurement must meet.

*[≈270 kelime. 200 isteyen dergide kesilecek ilk yer: ikinci paragrafın
konfigürasyon tarifi, sonra üçüncü paragrafın ilk cümlesi.]*

*[⚠️ Özette **hiçbir ödünç sayı yok.** %38/%13 (Bacchini & Cestino) bilerek
dışarıda — kaynak henüz birinci elden okunmadı. Menzil sayıları da yok, çünkü
hesaplanmış değerler özette bağlamsız durur.]*

---

## Keywords

vertical take-off and landing; tail-sitter; blended wing body; uncrewed aerial vehicle;
series hybrid propulsion; cruise efficiency; aircraft configuration design

---

## Beyanlar

### Acknowledgements

> Artificial-intelligence tools were used during the preparation of this work, for
> literature searching, numerical checking and language editing. All design decisions,
> engineering judgements and claims presented in this paper are the authors' own, and
> the authors accept full responsibility for the content.

*[✅ Tasarımcının değişmez kuralı: **genel ifade, marka/model/firma adı yok**,
yazar satırında yapay zekâ yer almaz. Bu metin o kuralı karşılar ve aynı zamanda
MDPI'ın yapay zekâ beyan zorunluluğunu da karşılar.]*

### Conflicts of Interest

> The authors have filed a patent application covering the aircraft configuration
> described in this paper (Türkpatent application 2026/014570).

*Durum: başvuru **yapıldı**. Metin buna göre yazıldı — "yapılacaktır" değil,
"yapılmıştır". Dergi başvuru numarası isterse eklenir.*

### Data Availability

> All data supporting the reported results are contained within the article. The
> parametric geometry model, the figure-generation scripts and the transition
> simulation, together with the aerodynamic calculations of Section 6.6 — including the
> mesh generator, the case setup, the grid-convergence study and the wall-resolution and
> turbulence-model sensitivity runs behind the computed zero-lift drag — are openly
> available at https://github.com/LORDTEK/meryemAircraft

*Bölüm 8.12'deki "başka bir grup bunu bağımsız deneyebilir" davetinin somut
karşılığı. Depo bağlantısı yayın öncesi eklenecek.*

### Funding

*[Öneri: "This research received no external funding."]*
