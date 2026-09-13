# Ön bilgi — başlık, özet, anahtar kelimeler, beyanlar

*Taslak v1 — İngilizce. Türkçe notlar italik ve köşeli parantez içinde.*

---

## Title

**The Architectural Cost of Hybrid VTOL: meryemAircraft, a
Propeller-Driven Tail-Sitting Blended-Wing-Body Without a Dedicated
Lift System**

## Authors

Meryem Gülmen <sup>1,\*</sup>, Berke Gülmen <sup>1</sup>, Ömer Gülmen <sup>1</sup>

<sup>1</sup> Independent Researcher, Türkiye; meryemgulmen@outlook.com (M.G.);
berkegulmen@outlook.com (B.G.); lordtek@me.com (Ö.G.)

<sup>\*</sup> Correspondence: meryemgulmen@outlook.com

*[Kurum bağlantısı yok; MDPI'ın "Independent Researcher" kaydı kullanılacak.
ORCID varsa gönderim sırasında eklenir — dergi zorunlu tutmuyor ama tavsiye
ediyor.]*

---

## Abstract

Hybrid vertical take-off and landing (VTOL) aircraft pay for runway independence in cruise
efficiency. This paper treats that cost as architectural as an accounting framework: the
penalty is charged in three coupled currencies — hover hardware carried through cruise, its drag
when exposed, and continuous power sized by a condition holding two percent of the flight —
and each remedy surveyed reduces one by raising another. Escape requires the same hardware, in
the same orientation, doing the same job, with the hover peak drawn from a buffer.
meryemAircraft, an uncrewed tail-sitting blended-wing body, satisfies this and is sized at 50 and 1000 kg from one set of equations. Against a lift-plus-cruise layout it closes the
same mission at thirty-seven to forty-two percent lower take-off mass, depending on whether its
attitude rotors' free-wheeling drag is charged; charging it reverses the range comparison under
one of three sizing contracts. The aircraft is not shown to be flyable. Its 50 kg budget closes only at 3.8 times
the highest rate yet measured on a flown pack, and at that rate re-closes 38 percent heavier; its
attitude rotors' free-wheeling drag is computed here and is not negligible; and transition
controllability rests on a pitching moment no current method predicts reliably. The framework
does not depend on that outcome.

*[Yukarısı ~200 kelimeye indirilmiş MDPI sürümü — dergi "about 200 words maximum"
diyor ve bunu teknik ön denetimde uyguluyor. Yapı başlıksız ama Background →
Methods → Results → Conclusion sırasını izliyor, dergi öyle istiyor.
Sondan bir önceki cümle kasten aleyhimize: hakem bulmadan biz söylüyoruz.

Aşağıdaki 588 kelimelik uzun sürüm SİLİNMEDİ. Zenodo kaydında, depo tanıtım
sayfasında ve gerekirse kapak mektubunda kullanılabilir. Buradan üretilen
belgeye girmez.]*

<details>
<summary>Uzun özet (588 kelime) — gönderime girmez</summary>

Hybrid vertical take-off and landing (VTOL) aircraft combine runway independence with
wing-borne cruise and pay for it in cruise efficiency. This paper treats that cost as
architectural rather than as a defect of implementation, and develops it as an accounting
framework. The penalty is charged in three coupled currencies — the mass of hover hardware
carried through cruise, its drag when exposed in cruise, and a power system sized by a
condition holding for some two percent of the flight — and each of the remedies surveyed here
reduces one by raising another. The escape condition is then explicit, and it has four parts:
the penalty is charged unless hover and cruise are served by the same hardware, in the same
orientation, doing the same job, with the hover peak supplied from a buffer rather than from
permanently installed continuous power. A second result is methodological: architectural
comparisons depend on the sizing contract chosen, and a fixed fuel fraction removes the
mass bill from the range column altogether, so three contracts are reported rather than
one.

meryemAircraft, an uncrewed tail-sitting blended-wing body, satisfies the escape condition
and serves as the case study: one coaxial pair at the nose gives all thrust in both
regimes, four small pairs at the tips give attitude moments and the residual take-off thrust
margin, and a deployable strip is
assigned the roll that body-parallel thrust cannot produce. Sized against a lift-plus-cruise
layout on wind-tunnel drag, it closes the same mission at thirty-seven to forty-two percent lower
take-off mass depending on whether its attitude rotors' free-wheeling drag is charged; charging it
costs the range comparison under one of three sizing contracts. Against a tilting layout the
comparison reverses between contracts and no superiority is claimed. Those are sizing results for an aircraft that has not
been built: a three-dimensional solution bounds the zero-lift drag with a quantified sensitivity
budget, but the component mass build-up closes the 50 kg design only on a battery specific power
of 5.6 kW kg⁻¹, which is 3.8 times the highest rate yet measured on a flown pack, and it does not
close the 1000 kg design at all.

The study is analytical, with no experimental validation of the configuration. The tip
propellers can turn the aircraft's rotational inertia through the transition but not, on
present evidence, its aerodynamic moment. Resolving that margin along the trajectory shows
the aircraft never reaches ninety degrees of incidence — the relative wind rotates with the
body — so the outstanding measurement is the pitching moment to some twenty-two degrees at low
dynamic pressure, together with trim at cruise. A vortex-lattice solution establishes static
pitch stability under a stated packaging rule and closes cruise trim, though not in the way
first supposed: measured data for reflexed sections fall an order of magnitude short of the
moment required, while nine degrees of tip washout supplies it, at a cost of 4.3 percent of
cruise lift-to-drag ratio. Roll is treated the same way: the inertia and the damping are computed
for this planform, the moment needed for a twenty-degree-per-second roll follows from them,
and the strip's effectiveness in supplying it is stated as a requirement rather than
demonstrated. Yaw has the strongest authority of the three axes, because differential tip
thrust acts through the semi-span, but the planform supplies no directional stability at
all, so the tip-frame fairings must serve as the vertical surfaces as well as the drag
measure they were introduced as. Attitude control is therefore sized in every axis and
closed in none. Transition controllability remains the
principal open requirement and is stated as a threshold a future measurement must meet.

*[≈270 kelime. 200 isteyen dergide kesilecek ilk yer: ikinci paragrafın
konfigürasyon tarifi, sonra üçüncü paragrafın ilk cümlesi.]*

*[⚠️ Özette **hiçbir ödünç sayı yok.** %38/%13 (Bacchini & Cestino) bilerek
dışarıda — kaynak henüz birinci elden okunmadı. Menzil sayıları da yok, çünkü
hesaplanmış değerler özette bağlamsız durur.]*

---

</details>

## Highlights

> **What are the main findings?**
>
> - Hybrid VTOL aircraft pay for vertical flight in three coupled currencies — hover
>   hardware carried through cruise, its drag when exposed, and continuous power sized by a
>   condition holding for some two percent of the flight — and each architectural remedy
>   surveyed here reduces one by raising another.
> - A tail-sitting blended-wing body whose single coaxial nose pair serves both regimes
>   satisfies the escape condition and, sized against a lift-plus-cruise layout on
>   wind-tunnel drag, closes the same mission at thirty-seven to forty-two percent lower
>   take-off mass, though not at longer range under every sizing contract.
>
> **What are the implications of the main findings?**
>
> - Architectural comparisons change their ranking with the sizing contract chosen, so a
>   ranking quoted without its contract is not a result; three contracts are reported here.
> - The configuration is not shown to be flyable: its mass budget closes only on a battery
>   specific power 3.8 times the highest rate yet measured on a flown pack, and transition
>   controllability rests on a pitching moment no current method predicts reliably.

*[MDPI zorunlu tutuyor ve biçimi sabit: iki başlık, her biri en çok iki madde.
Özetin kopyası olmamalı — arama motorlarında ve okuyucunun ilk üç saniyesinde
çalışacak metin. Üçüncü ve dördüncü maddeler kasten aleyhimize: hakem bunu
bulmadan önce biz söylüyoruz.]*

---

## Keywords

vertical take-off and landing; tail-sitter; blended wing body; uncrewed aerial vehicle;
series hybrid propulsion; cruise efficiency; aircraft configuration design

---

## Beyanlar

### Supplementary Materials

> The following supplementary material is available: **S1** — independent checks on the two
> assumed aerodynamic coefficients (the full version of Section 3.10); **S2** — a component
> build-up of the mass budget (Section 3.11); **S3** — the control axes in full (Section 2.10);
> **S4** — rotational authority, trim and the transition envelope (Section 3.17); **S5** — the
> limitations in full (Section 4); **S6** — the three bills stated formally and the comparative
> sizing under three contracts (Sections 3.1 and 3.6).

*[Dergi bu bölümü arka maddede zorunlu tutuyor ve her parçanın adıyla anılmasını
istiyor. Altı ek tek dosyada gönderilecek — hakem için altı ayrı dosyadan kolay.]*

### Patents

> A patent application covering the aircraft configuration described in this paper has been
> filed with the Turkish Patent and Trademark Office (application 2026/014570).

*[Dergi bu bölümü isteğe bağlı tutuyor ama "bu çalışmadan doğan patent varsa
eklenebilir" diyor. Patent hem burada hem Conflicts of Interest'te anılıyor: biri
kaydın kendisi, diğeri çıkar beyanı. İkisi farklı şeyler ve dergi ikisini de
istiyor.]*

### Author Contributions

> Conceptualization, Ö.G. and M.G.; Methodology, Ö.G. and M.G.; Software, B.G.;
> Formal Analysis, M.G. and B.G.; Investigation, M.G., B.G. and Ö.G.; Data Curation,
> B.G.; Writing — Original Draft Preparation, M.G.; Writing — Review & Editing, M.G.,
> B.G. and Ö.G.; Visualization, B.G.; Supervision, Ö.G.; Project Administration, M.G.
> All authors have read and agreed to the published version of the manuscript.

*[⚠️ BU TASLAK — yazarların onaylaması gerek. MDPI bu bölümü zorunlu tutuyor ve
CRediT sözlüğünden terim istiyor; ben kimin ne yaptığını bilemem, o yüzden sorumlu
yazarın Meryem, denetleyenin Ömer olduğu varsayımıyla makul bir dağılım yazdım.
Yanlışsa değiştirin — uydurma bir katkı beyanı yayın etiği ihlalidir.
Kullanılabilecek roller: Conceptualization, Methodology, Software, Validation,
Formal Analysis, Investigation, Resources, Data Curation, Writing — Original Draft,
Writing — Review & Editing, Visualization, Supervision, Project Administration,
Funding Acquisition. Baş harfler: M.G., B.G., Ö.G.]*

### Acknowledgements

> During the preparation of this study, the authors used large-language-model assistants for
> the purposes of literature searching and triage, numerical checking of the authors' own
> calculations, and language editing. Section 2.14 states the scope of that use and the rules
> under which it was admitted. No source was cited on a model's description of it, and no
> correction was adopted until it had been reproduced independently from the underlying model.
> All design decisions, engineering judgements and claims presented in this paper are the
> authors' own. The authors have reviewed and edited the output and take full responsibility
> for the content of this publication.

*[✅ Değişmez kural korundu: **genel ifade, marka/model/firma adı yok**, yazar
satırında yapay zekâ yer almaz.

⚠️ AMA BİR ÇATIŞMA VAR, KARAR SENİN. MDPI'ın şablonu "[tool name, version
information]" diyor — yani araç adı ve sürüm istiyor. Yukarıdaki metin şablonun
*yapısını* (ne için kullanıldı + gözden geçirildi + sorumluluk yazarlarda) karşılıyor
ama araç adını vermiyor. Editör ısrar ederse iki yol var: adı yazmak, ya da "genel
sınıf yeterlidir" diye direnmek. Şimdilik ikincisindeyiz ve bu bilinçli bir seçim.

Dergi ayrıca GenAI'ın analiz/yorumda kullanıldığı durumda Methods İÇİNDE de beyan
istiyor; onu 2.14 karşılıyor. Buradaki blok Acknowledgements tarafı.]*

### Conflicts of Interest

> The authors have filed a patent application covering the aircraft configuration
> described in this paper (Türkpatent application 2026/014570).

*Durum: başvuru **yapıldı**. Metin buna göre yazıldı — "yapılacaktır" değil,
"yapılmıştır". Dergi başvuru numarası isterse eklenir.*

### Data Availability

> All data supporting the reported results are contained within the article. The
> parametric geometry model, the figure-generation scripts and the transition
> simulation, together with the aerodynamic calculations of Section 3.10 — including the
> mesh generator, the case setup, the grid-convergence study and the wall-resolution and
> turbulence-model sensitivity runs behind the computed zero-lift drag — are openly
> available at https://github.com/LORDTEK/meryemAircraft

*Bölüm 8.12'deki "başka bir grup bunu bağımsız deneyebilir" davetinin somut
karşılığı. Depo bağlantısı yayın öncesi eklenecek.*

### Dual-Use Research of Concern

> This paper is a civil aircraft configuration study. The applications the configuration was
> conceived for are civil ones — wildfire observation and response, and cargo carriage to places
> without a runway — and no military organization, mission, weapon or payload is named or
> analysed anywhere in this work. It reports no experimental hardware and no controlled
> technical data.
>
> **The authors acknowledge the dual-use potential inherent in the subject matter.** A
> long-endurance unmanned aircraft is dual-use in principle, as most aircraft configurations
> are, and the authors note for completeness that the heavier of the two analytical scale cases
> — a 1000 kg vehicle with a computed range near 1800 km — falls within the range band by which
> unmanned aerial vehicles are listed under international export-control arrangements. What is
> published here is an open configuration study and its equations, offered so that others may
> check or refute it; the authors neither direct it at, nor undertake to police, any particular
> downstream use, and they remain available to provide whatever further declaration the editors
> require.

*[⚠️ KARAR SENİN, ama önceki taslağımı düzelttim ve sebebini yazayım.

Önce "no part of this work was conducted for, or is directed at, a military application"
yazmıştım. Bunun ikinci yarısı gelecek hakkında bir **taahhüt**ti ve kimse onu
veremez. Senin itirazın doğru: birisi yarın askeri amaçla kullanırsa biz yanlış
beyan vermiş oluruz.

Şimdiki metin üç şeyi ayırıyor: (1) bu çalışmanın NE OLDUĞU — sivil, askeri hiçbir
şey adlandırılmıyor, bu bir olgu; (2) NİYETİMİZ — orman yangını ve yük, bu da olgu;
(3) ÇİFT KULLANIM POTANSİYELİ — inkâr edilmiyor, kabul ediliyor.

Üçüncüsü ayrıca daha GÜÇLÜ bir DURC beyanı. MDPI'ın kendi rehberi yazarlardan
"bulgularının nasıl kötüye kullanılabileceğini tahmin etmesini" istiyor. "Çift
kullanım yoktur" demek bu rehbere uymaz; "vardır, farkındayız" demek uyar. Drones'ta
2026'da yayımlanan İHA sürü makaleleri de tam bunu yapıyor.

Derginin kapsam sayfası şablonu yalnızca askeri kuruluş/görev adı geçen makaleler
için zorunlu tutuyor; bizde geçmiyor, yani bu blok gönüllü. Ama gönüllü olması onu
zayıflatmıyor, tersine.

NOT: Orman yangını ve yük amacını ilk kez burada yazdım. Makalenin GÖVDESİNDE hiçbir
görev tanımı yok — hakem "bu ne için?" diye sorar. 13 kg faydalı yük / 1600 km bir
misyonun sayısı; hangi misyon olduğunu söylemek makaleyi güçlendirir. Girişe bir
cümle eklememi istersen söyle, kendiliğimden eklemedim.]*

### Funding

> This research received no external funding.
