# Step 15 — Four axes, and where the paper stops

**v8 taslağı, birinci yazım (Tur 57).** İskeletin son satırı: *"Dört eksende dur — yeni hesap yok, atıf
yok."* Grok, Tur 57: *"The last section … should repeat Section 9's four axes and stop. No new number."*
Yazar, Tur 57: *"Adım 9 için dört ekseni tekrarla."*

**Kural denetimi:** hiç sayı yok (3,8×'in tek evi Adım 14 — burada tekrarlanmıyor) · hiç atıf yok · sabit
kanatla menzil yarışı yok (§0) · çok rotorluyla dikey yarış yok (§0) · tilt'e karşı iddia **mekanizma**,
dar hâliyle: yeniden yönlendiren mekanizma sınıfı yok, hareketli parça yok değil; yatış şeritten (§0.1)
· *"mekanik olarak daha basit"* yok · *"inşa gereği"* yok · öteki hibritlere karşı menzil iddiası yok ·
*"the range of a fixed-wing aircraft"* yok (§0.3) · katkı merkezde (oran incelemesi P2).

**Bu sayfa yazılırken bulunan:** Adım 9'un bağımlılık tablosu pist iddiasının *"the battery gap"*e bağlı
olmadığını söylüyordu; Adım 14 dikey evrenin bu depoyla boyutlandığını gösterdi. **Adım 9 düzeltildi.**
Ve **Adım 6 hâlâ *"It is this aircraft's own refusal of the variable-pitch hub"* diyordu** — ChatGPT'nin Tur
53'te Adım 11'de yakaladığı aşırı atıf Adım 6'ya hiç yayılmamıştı; bu sayfanın ilk yazımı onu tekrarladı.
İkisi de düzeltildi, emekli listesine girdi.

---

## Four axes, and where the paper stops

The paper makes its claims on four axes, against four opponents (Section 9), and on each it stops where
its evidence stops.

**Cruise efficiency, against multirotors — claimed, and bounded.** Cruise lift is carried on a surface
rather than on rotors. The size of the advantage is a calculation, not a consequence of that statement:
positive throughout against one published quadrotor, and from slightly behind to comfortably ahead against
the other (Section 6). Nothing is claimed against multirotors on vertical capability.

**Operation without a runway, against fixed-wing aircraft — claimed as sized, not demonstrated.** The
vertical phase was sized with an energy store whose required performance the sources consulted here do not
report as built (Section 14). Nothing is claimed against fixed-wing aircraft on range or cruise efficiency.

**The mechanism required to change regime, against tilting architectures — the contribution.** The
configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so
carries none of the mechanism classes Section 7 counts: no pivot, no nacelle or rotor-group actuator, no
variable-pitch hub, no dedicated lift rotors, and no rotor stowing, indexing or stopping mechanism. Roll
comes from the strip; the reaction-torque channel the coaxial pairs could provide is declined, and what
declining it costs is not computed. **This is a count of mechanism classes, not a claim that nothing moves, and not a
claim of mechanical simplicity or reliability.** Whether this aircraft completes the rotation is a separate
question, and it is not settled here.

**Range, against the other hybrids — not claimed, in either direction.** The ordering belongs to the sizing
contract (Section 13).

**The loop closes; the aircraft is not shown to.** Section 14 lists what would settle the rest; nothing in
this work addresses certification. What the paper offers is **a configuration sized to combine
runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so with no mechanism
that reorients a propulsor, and an account of what the combination costs.**

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 61 — kısa kapanış** (dört okuyucu + Claude hemfikir, A3): 1 023 → ~330 kelime. Kalan her yüklem aşağıdaki satırlarda kaynağıyla; çıkarılanlar kendi evlerinde: çerçeve özeti Adım 2–3, kısmi gerçekleşme Adım 3/7/8, *"by construction"* Adım 9, bağımsız üretilmiş rakamlar Adım 6 | `paper/v8-shortening-consensus.md` A3, A4 |
| **Tur 60:** *"rather than cruise thrust"* | Grok |
| **Tur 59:** *"The configuration is arranged to change regime by rotating the airframe"* — Grok Adım 14'ü yakaladı; aynı fiil burada da vardı | Adım 1 (P1) |
| Dört eksen, dört rakip, sıralama | Adım 9 tablosu |
| Seyir kaldırması yüzeyde; hiçbir sözleşme bunu değiştirmez | Adım 6 (*"no sizing contract … moves a vehicle between those two states"*) |
| Üstünlük hesap; iki yayımlanmış quadrotor; turboşafta karşı pozitif, tam elektriğe karşı *"slightly behind to comfortably ahead"* | Adım 6, *"What the margin actually is"* |
| Sıkıştıran şey sabit hatveli paletin seyir verimi | Adım 6 (**Tur 57'de düzeltildi**: *"own refusal of the variable-pitch hub"* ChatGPT'nin Tur 53'te Adım 11'de yakaladığı aşırı atıftı ve Adım 6'ya yayılmamıştı) |
| Karşılaştırma kontrollü yeniden üretim değil | Adım 6, beşinci nitelendirme |
| Kuyruğunun üstünde duruyor; saha yalnız zemin veriyor; duruş yapısı = kontrol pervanelerinin yapısı | Adım 5 |
| Dikey evre bu depoyla boyutlandı; ölçülmüş depoda yalnız daha ağır, sürekli anmada kapanmıyor | Adım 14 (ikinci yazım) |
| *"By construction … by the sizing, never by demonstration"* | Adım 9, madde 8 |
| Gövde döner, propulsor dönmez; beş mekanizma sınıfı | Adım 7 tablosu ve metni |
| Yunuslama/sapma diferansiyel itkiden; yatış şeritten; tepki torku kanalı reddedildi, bedeli hesaplanmadı | Adım 7, Adım 8, Adım 9; CLAUDE.md §0.1 |
| Eyleyici envanteri: motorlar ve şerit | Adım 7 (*"the propulsion motors together with the strip"*) |
| Sayım, basitlik/güvenilirlik değil | Adım 7, Adım 9 madde 3–4 |
| Mekanizma iddiası sürükleme, η_p, sözleşme, depo, geçiş aerodinamiğine bağlı değil | Adım 9 bağımlılık tablosu; Adım 14 *"It does not reach the mechanism claim"* |
| Geçişin tamamlanması iddia edilmiyor | Adım 7 son paragrafı; Adım 10 |
| Kısmi gerçekleşme: burun çifti sağlıyor, uç çiftleri değil | Adım 7, Adım 8, Adım 9 madde 5 |
| Lift+cruise sıralaması sözleşmeye bağlı; bir sözleşmede işaret değişiyor ve ölçülmemiş bir kesre bağlı; tilt bir sınır | Adım 13 |
| Üç para birimi, bağlaşık; her çare aktarır | Adım 2 (Tur 56 başlığı) |
| En az ikisi kilitli değil → sıralama bir ağırlıklandırma | Adım 12, Adım 13 |
| Döngü kapanıyor, uçak gösterilmedi; ilk engel depo; ötekiler | Adım 10, Adım 14 |
| Son cümle | Adım 9 *"What the claims that remain amount to"*; CLAUDE.md §0.3 |

**Bu sayfada BİLEREK olmayanlar:** hiçbir sayı; hiçbir atıf; ağır tasarım; öteki hibritlere karşı menzil
sıralaması; *"validation"*; *"no moving parts"*; *"simpler"*.
