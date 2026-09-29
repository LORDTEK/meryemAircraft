# Step 7 — The combination

**v8 taslağı, birinci yazım.** İskeletin 7. adımı. Yaklaşık 700 kelime.
Grok'un tavsiyesi: *"O sayfayı önce yaz. O sayfa netse v8 tutar."*

**Kural denetimi:** "önceki sürümde" anlatısı yok · menzil iddiası yalnız çok
rotorluya karşı · üçüncü iddia dar, şerit aynı nefeste · "mekanik olarak daha basit"
geçmiyor · *"inşa gereği"* geçmiyor.

**İkinci yazım, Tur 35 sonrası.** Dört dış okuyucunun bulduğu beş kusur düzeltildi:
tiltin koşulu *sağladığı* iddiası (DeepSeek — §2.6 tam tersini söylüyor), *"single
propulsor ... design condition throughout"* (Grok ve ChatGPT — §3.15 burun çiftinin tek
başına kalkamadığını söylüyor), tablo başlığının bütün tiltlere genellenmesi (ChatGPT ve
Qwen bağımsız olarak), gyroskopik momentin mekanizma sayılması (ChatGPT — bir etki,
mekanizma değil; düzyazıya taşındı), ve kalkış marjı bağımlılığının sayfada hiç
geçmemesi (Grok).

**Tur 47 düzeltmesi — yatış ekseni.** ChatGPT *"yatış pervanelerle ÜRETİLEMEZ"* cümlesinin
tepki torkunu atladığını gösterdi; §2.9 her rotorun **kendi elektrik makinesinde** olduğunu
söylüyor, dolayısıyla diferansiyel devir gövde ekseni etrafında net tork verir. Zhang ve ark.
2012 (`references/ica20120400001_12673514.pdf`) bunu **birincil kontrol kanalı** olarak kullanıyor.
Qwen ayrıca §2.10'un askı paragrafındaki *"thirty-degree bank"* ifadesinin aslında bir **yön
değişimi** olduğunu gösterdi. İddia daraltıldı: **fiziksel imkânsızlık değil, tasarım seçimi.**
Ayrıntı ve alıntılar: `paper/roll-axis-finding.md`.

---

## The combination

None of the three elements is new. **Each can be found on its own, and some of them
together, in the literature and in hardware** — Section 1 says where. The principle behind the third element — a continuous plant sized for cruise, with the vertical or take-off peak drawn from a store — has been applied in studies of a winged tail-sitter (Section 1) and of a single-aisle airliner reported in 2016 whose turbines are *"sized for efficient operation during"* cruise and assisted by electric motors *"during takeoff and climb."*

**What this paper contributes is the architecture that brings the three elements together; the
condition shows what it satisfies, and the price shows what it costs.** The three elements, taken together, meet the escape condition
of Section 3 **in the propulsor that carries the aircraft**, and they meet it with no mechanism
that reorients a propulsor. The assembly is not offered as novel because it is an assembly. It is
offered for what it satisfies, and for what it does not need in order to satisfy it.

**The qualification "in the propulsor that carries the aircraft" is not decoration.** The single nose pair meets all four parts of
the condition. The four tip pairs do not: they are exposed in the cruise flow and cannot be feathered, so they re-open the second
charge. **The instantiation is therefore partial**, the case Section 3 lists among the ways to fail, and reporting what the failing
part costs is a substantial share of what Section 11 does.

Each element supplies one part of the condition, and none supplies it alone:

- The **blended wing body** carries the cruise lift on a surface.
- The **tail-sitting stance** aligns the thrust axis with the body axis, so one propulsor produces the thrust for vertical operation
  and for cruise, in one orientation relative to the airframe; there is no dedicated lift system, and vertical operation needs no runway.
- The **series-hybrid buffer** releases the continuous plant from the hover peak, so that it is sized by cruise; the series
  arrangement is chosen for the electrical path it gives the buffered peak, not because it is assumed to be the more efficient hybrid.

**The configuration is arranged to change regime by rotating the airframe. The propulsors hold their orientation relative to the body
from take-off to cruise; what changes is the orientation of the body relative to the flight path.** The contemporary hybrids reach the
same end otherwise. The lift-plus-cruise design of the NASA study used in Section 4 carries its lifting rotors through cruise, stopped
and aligned with the stream, and flies on a separate pusher; its tilt-wing turns eight proprotors, each on its own motor, on a tilting
wing and tail. Turning the
propulsors is the case the condition excludes; turning the thing they are attached to leaves the orientation requirement intact.
**That single move is what removes the need for the mechanism.** The table counts the mechanism classes that exist in order to change
regime, or to take a rotor out of one regime's flow; the strip of Section 8 is a control surface, of a different class, and is named
below. The configuration therefore carries:

| Mechanism | Where it is required | Present here |
|---|---|---|
| Pivot or tilting joint | Tilting architectures | — |
| Nacelle or rotor-group actuator | Tilting architectures | — |
| Variable-pitch hub | Architectures that trim a rotor across two widely separated operating points, or feather a rotor unused in one regime | — |
| Dedicated lift rotors | Lift-plus-cruise architectures | — |
| Rotor stowing, indexing or stopping mechanism | Architectures that remove dedicated lift rotors from the cruise flow by such means | — (see note) |

*Note.* The stopping class is absent if the tip pairs free-wheel in cruise or are held stopped by motor torque; a
brake or a mechanical lock would add it. The means of stopping is not fixed by this study (Section 8, *What this inventory does not settle*).

The tip
pairs are sized from the moment requirement, but because the nose pair is sized at thrust equal to weight and no more, they also supply
the whole take-off margin; that dependency is reported in Section 5, and it does not make them a dedicated lift system.

**The claim is narrower than it may appear.** **This is not a configuration in which nothing moves.** Roll cannot come from the
propellers' thrust, since every thrust vector is parallel to the body axis; it could come from their reaction torque, and this
configuration declines that channel by design (Section 8), assigning the axis to the only moving aerodynamic surface on the aircraft: a
variable-extension strip on the lower surface, modulated rather than switched, which also pitches the nose down slightly when deployed.
It is named here because a claim about eliminated mechanisms that omitted it would be false. **Nor is this a claim of
mechanical simplicity**: what is offered is a count of the mechanism classes a tilting architecture needs to change regime and this
arrangement does not, and the actuator inventory that replaces them is the propulsion motors together with the strip.

**Whether this aircraft can actually perform the change is a separate question and is not settled anywhere in this paper**: the aerodynamics of the rotation are not predicted reliably here (Sections 6 and 10). **The mechanism claim is about hardware and survives that
limit. The transition claim is not made.** Section 15 holds the paper to that.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 170 — yazarın notları üzerine kısaltma uygulandı** (Tur 168–169: işlemlerde dört okuyucu + Claude; korunan cümle taşımaları yazar kararı E13). Değişen her paragrafın eski hâli ekin bu adıma ait bölümünde aynen (*"… before the Round 170 shortening"*). Yeni (R) cümleler Tur 170 §2'de okuyucu vetosuna açık; sonuç teyide | `paper/build/v8_round170_texts.py`, `v8_round170_apply.py` |
| **Tur 175 — 5.1 (yazar: "5.1 olsun"; Grok, ChatGPT, Qwen önerisi; yazarın Tur 168 notu):** yalnız tekrar kesildi — tilt-wing bedel listesi, tutum ilk cümlesi (5.2.5), sabit hatve bedeli (2.2.4, 6.2.3); R9 geçiş paragrafı. Korunan cümleye dokunulmadı. Eski paragraflar ekte aynen; okuyucu teyidine | — |
| **Tur 151 — W-2 uygulandı (yazarın cümlesi ve kararı; dört okuyucu yeni yüklem bulmadı):** korunan *"What this paper contributes is that combination, the condition its primary propulsor is designed to satisfy, and the price the configuration pays for pursuing it."* → *"What this paper contributes is the architecture that brings the three elements together; the condition shows what it satisfies, and the price shows what it costs."* Tanımlık ve fiil yazarın seçimi (Grok'un biçimi). Tek katkı: mimari (Tur 35); Bölüm 1, 5.1, 6.2, 9 artık aynı katkıyı adlandırıyor. Q3, L-3 satır 1 kapandı | Tur 150 §0; Tur 151 §1 |
| **Tur 150 — W-2 Q3 uygulandı** (dört okuyucu + Claude; korunan, D): *"The qualification in that sentence is not decoration."* → *"The qualification "in the propulsor that carries the aircraft" is not decoration."* (gösterici iki cümle gerideydi; tırnak, çünkü italik Qwen'in ekranına ulaşmadı). **W-2 Q2 yazarın kararında:** (ii) Grok, ChatGPT (çekinceli), Qwen, Claude; (iii) DeepSeek, (iv) DeepSeek'in inceltmesi | Tur 149 §2 |
| **Tur 149 — L-3 satır 5, 6 uygulandı:** *"The four attitude pairs"* → *"The four tip pairs"*; *"the attitude rotors that make the union controllable"* → *"the tip pairs that…"* (ChatGPT'nin çekincesi: tek kontrol aracı değil). W-2 (katkı cümlesi) Tur 149'da ikinci tartışma turunda, sonra yazara | Tur 148 §2–3 |
| **Tur 147 — W-1 (1) ve L-7 uygulandı** (bütün okuma; dört okuyucu + Claude): not *"(Section 8)"* → *"(Section 8, *What this inventory does not settle*)"* (birleşik görünümde 6.1); L-7 *"reported as one where the sizing is audited"* → *"reported as one in Section 5"* (işaretçi eklemek Bölüm 3'ü boyutlandırma denetçisi gibi gösterecekti; teyide). W-2 katkı cümlesi yazarın kararında | Tur 146 §5; Tur 147 §1 |
| **Tur 137 — *"reported in 2016"* eklendi** (DeepSeek; dört okuyucu + Claude): *"and of a single-aisle airliner reported in 2016 whose turbines are …"* | Rheaume 2016 |
| **Tur 136 — tanık cümlesi KAPANDI** (dört okuyucu teyit etti). DeepSeek önerisi (*"reported in 2016"*) oyda | Rohith 2026; Rheaume 2016 |
| **Tur 135 — tanık cümlesi (B; dört okuyucu + Claude; Tur 124'ten beri bekliyordu):** *"— Section 1 says where."*den sonra *"The principle behind the third element — a continuous plant sized for cruise, with the vertical or take-off peak drawn from a store — has been applied in studies of a winged tail-sitter (Section 1) and of a single-aisle airliner whose turbines are 'sized for efficient operation during' cruise and assisted by electric motors 'during takeoff and climb.'"* Rheaume özet; Rohith Adım 1. Grok P127: *"some of them together"*in örneği Rohith'in kuyruk üstü + seri hibrit tampon birlikteliği (Adım 7'nin ikinci ve üçüncü öğesi), kolektif hatve değil — denetlendi | Rohith 2026; Rheaume 2016 |
| **Tur 126** (dört okuyucu + Claude): [6]'nın iki etiketi (*"That is the second half of the union."*, *"That is the first half."*) ve [12]'nin *"and the boundary matters"* yan cümlesi çıktı (ses kuralı); [3]'ün karşılama cümlesi *"The instantiation is therefore partial."* ile çift olarak korunan (ChatGPT §13); [4]'ün ilk yarısı korunan kalır (ChatGPT görüş değiştirdi); [13] temiz silme yok, kalır | Tur 125 metni §3 |
| **Tur 125 — ses (yöntem Tur 124'te kapandı; yazar: "ton seçimleri tamam, geri koyma")**: [4]'ün *"and it is made here rather than conceded later"* yan cümlesi çıktı (dört okuyucu + Claude saf ses; ChatGPT bütün cümleyi silmek istiyor, ilk yarı korunan — ayrışık). Özgün adım Ek S7'de tam | Tur 124 metni §3 |
| **Tur 124 — S-45 uygulandı** (Tur 119'da dört okuyucu + Claude; Adım 7 açılınca uygulanacaktı): *"and in combination"* → *"and some of them together"*; Adım 1 ile aynı nesne (Grok P103): öğeler, bazıları bir arada, ve bedeliyle birlikte kurulmamış birleşim | Tur 119 metni §2 |
| **Tur 99 (dört okuyucu + Claude):** S-33 — tablonun durdurma satırı "— (see note)" ve altına not: "The stopping class is absent if the tip pairs free-wheel in cruise or are held stopped by motor torque; a brake or a mechanical lock would add it. The means of stopping is not fixed by this study (Section 8)." (dördü de Adım 7'de nitelemeyi istedi; sözcükler Grok + Qwen birleşimi — teyide). 7D seri hibrit cümlesi (ChatGPT'nin sözcükleri). Özgün tablo Ek S7'de | Adım 8G |
| **Tur 98 (dört okuyucu + Claude):** 7G — Adım 5D'nin birebir cümlesi çıktı; "This dual role is a dependency, reported as one where the sizing is audited, and it does not make the tip pairs a dedicated lift system." (Qwen'in göndergesi). 7L kalıyor (dört okuyucu + Claude; iz: köprü/kapanış, yineleme değil). Özgün Ek S7'de | Tur 97 metni §5 |
| **Tur 97 (yeniden kurma; dört okuyucu + Claude):** envanter teyit edildi; 7A ortadaki üç cümle çıktı (Adım 1G'nin yinelemesi; ev 1G). **Uygulanmadı:** 7G (onarım biçimi ayrışık: "It" / "That" / "This dual role"); 7L (Grok ve Qwen çıkar, ChatGPT ve DeepSeek tut — köprü/kapanış). Özgün paragraflar Ek S7'de | Tur 96 metni §7 |
| **Tur 67 — V2, Grok'un ifadesi** (dört okuyucu + Claude): *"pays in efficiency in at least one of them"* — bedelin birimini adlandırıyor, sayı eklemiyor; Adım 3'ün *"the compromise is paid in efficiency"* cümlesiyle aynı güçte (Qwen) | Adım 3 |
| **Tur 66 — B4 (3.2) ve ses geçişi V1, V2, V6** (dört okuyucu + Claude): tepki torku tek cümle (*"could"* + *"by design"* = tasarım kısıtı, fiziksel imkânsızlık değil); şerit dışlaması kural olarak; *"pays for it"*; *"carries costs"*. **V3 ve V5 kaldı** (herkes korudu), **V4 kaldı** (Grok: olumlu hâli koşulun karşılandığını ima ediyordu — uç çiftleri karşılamıyor) | Adım 8; ChatGPT'nin A–D kuralı |
| **Tur 64:** *"removes the mechanism"* → *"removes the need for the mechanism"* (ChatGPT önerdi; beşimiz hemfikir) — bir şey sökülmüş gibi okunmasın; korunan liste aynı commit'te güncellendi | `v8-caveats.md` ruh listesi |
| **Tur 59:** *"The configuration is arranged to change regime by rotating the airframe"* — P1 fiili | Adım 1 (P1); Grok'un Adım 14 işaretinin yayılması |
| Kaçış koşulu: tek donanım, tek yönelim, tampondan tepe | v7 özeti, satır 55 |
| Her itki vektörü gövde eksenine paralel; itkiden yatış momenti yok | §2.10, satır 810–812 |
| Tepki torku bir yatış kanalıdır; her rotor kendi elektrik makinesinde | §2.9, satır 784–785 |
| Kuyruk üstü literatürü bu kanalı kullanıyor | Zhang ve ark. 2012, `references/ica20120400001_12673514.pdf`: *"Roll motion is controlled by the differential velocity of the two motors"* |
| Kaynağın *"roll cannot be produced by propellers at all"* cümlesi **daraltıldı** | §2.10, satır 813–814 aşırı iddia; `paper/roll-axis-finding.md` |
| Şerit "uçaktaki tek hareketli aerodinamik yüzey" | §2.10, satır 815–816 |
| Şerit **modüle ediliyor**, açılıp kapanmıyor | §2.10, satır 818 |
| Şerit burnu aşağı yunuslatıyor | §2.10, ΔC_m 0,005–0,032 |
| Burunda tek eşeksenli karşıt dönüşlü çift, uçlarda dört küçük çift | §2, Şekil 6 ve 8 |
| Askı koşulu uçuşun ~%2'si | v7 özeti |
| Tiltler koşulu **sağlamaz**; "aynı donanım, farklı yönelim" bir fatura doğurur | §2.6, satır 672–674 |
| Tilt bedeli: pivot, aktüatör, gyroskopik moment, geçiş kontrol problemi | §2.6 tablosu satır 659; ayrıca satır 463 |
| Burun çifti T/W = 1,00 tam, fazlası yok; kalkış marjı uçlardan | §3.15, satır 2624–2626 |
| Uç çiftleri moment gereğinden boyutlandırıldı, ağırlık taşımaktan değil | §3.2, satır 1150–1151 |
| "Sızdırılmadığı için sorulmayan bir ikinci iş" — tek yer | §2.7, satır 706–708 |
| Şerit alt yüzeyde, planformda 45°, kök veterinin %120'si — firar kenarı aygıtı DEĞİL | §2.10, satır 816–818 |

**Sayı vermediğim yerler bilerek boş:** şeridin boyutları, ΔC_m aralığı ve moment
kolları bu sayfaya girmiyor — 8. adımın (neyden yapıldığı) işi. Bu sayfa **hamleyi**
anlatıyor, envanteri değil.
