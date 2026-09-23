# Step 9 — What is not claimed

**v8 taslağı, birinci yazım.** İskeletin 9. adımı. **Hiçbir sayıdan önce.**

**Kural denetimi:** sayfada **tek bir sayı yok** · bu bir **sınır tanımı**dır, ikinci bir
kısıtlar bölümü değil (ChatGPT'nin şartı) — kapanmayanlar Adım 14'te · retler, dört eksenin
**sonucu** olarak sunuluyor, savunma listesi olarak değil (DeepSeek) · §0'ın dört ekseni ve
§0.1'in sınırı burada yazılı hâle geliyor.

---

## What is not claimed

This section states the boundary of the paper's claims. It is placed before the configuration's
own numbers because a boundary drawn after the results would be a retreat, and one drawn before
them is a commitment.

**It is not a list of the study's open questions.** Those are in Section 14, and the difference
matters: the boundary below is about claims the paper **declines to make**, most of which it
could not make on any evidence; Section 14 is about questions the paper **does not answer**, and
which better evidence would answer. One is a scope; the other is a debt.

### The claims are made on four axes, against four different opponents

The boundary is easiest to state as a consequence of the claim structure rather than as a list
of denials, so the structure comes first. Comparison is only meaningful against a named
alternative, and this paper's alternatives differ from axis to axis.

| Axis | Opponent | Status |
|---|---|---|
| Cruise efficiency | Multirotors | **Claimed, and bounded.** Cruise lift is carried on a surface rather than on rotors, which no sizing contract changes. The *size* of the resulting advantage is a calculation, not a consequence of that fact, and Section 6 measures it against two published quadrotors in one common definition. |
| Operation without a runway | Fixed-wing aircraft | **Claimed**, in the sense stated below. |
| The mechanism required to change regime | Tilting architectures | **Claimed.** This is the paper's contribution. |
| Cruise efficiency and range | Other hybrids — lift-plus-cruise, tilt | **Not claimed, in either direction.** |

**The fourth row is the important one**, and the reason it is a refusal rather than a result is
the paper's own finding in Section 13. Against lift-plus-cruise the ordering depends on the sizing
contract: across the three contracts it moves substantially, and under one of them its sign changes
inside the envelope and turns on a mass fraction of the competitor that is not measured. A paper that quoted one of those orderings as a result would be reporting its own choice of
contract. Against the tilting family the competitor can be modelled here only as a bound that pays no
cruise penalty, and an ordering against a bound is not a result. **No
range claim is made against the tilting or lift-plus-cruise families in either direction**, and
a reader who finds one implied anywhere in this paper should treat it as an error rather than
as a claim.

### What each claim does not depend on

A reader who rejects one of these claims should be able to see immediately which of the others
survive, and the dependencies are short enough to list.

| Claim | Does not depend on |
|---|---|
| Operation without a runway | the drag bracket, the propeller efficiency, the transition aerodynamics — **but it does depend on the energy store**: the vertical phase is sized with one, and Section 14 examines whether it exists |
| Cruise lift carried on a surface | the sizing contract, the transition aerodynamics |
| The **size** of the cruise-efficiency margin | — it depends on both the drag bracket and the blade family, and Section 6 reports it as a range rather than a number |
| Elimination of the propulsor-reorientation mechanism class | the drag bracket, the propeller efficiency, the sizing contract, the range result, the energy store, **and the transition aerodynamics** |

**The last row carries a distinction that matters more than the others.** The mechanism claim is
a statement about what hardware is present, and it is settled by the inventory of Sections 7 and 8. **The
separate claim that this aircraft can actually perform the regime change is not settled**, and it
depends on exactly the aerodynamics that Sections 6 and 14 describe as unreliable above roughly
ten degrees of incidence — the band the rotation passes through. **Section 7 should be read under
that limit**: it describes an arrangement that requires no reorienting mechanism, not a
demonstration that the arrangement transitions.

### One cost of the contribution that is named and not priced

The mechanism claim has a price this work does not compute, and it belongs here rather than only
in Section 1.

**This configuration declines a control channel that comparable aircraft use.** The two rotors of
a coaxial pair have independent machines and could be run at different speeds, producing a moment
about the body's longitudinal axis; the tail-sitter literature uses exactly that. Here every pair
is operated torque-balanced instead, and the axis is assigned to the strip. **What that refusal
costs — in thrust asymmetry, in propulsive efficiency, and in response time set by rotor inertia —
is not computed anywhere in this paper.** The claim is that the mechanism class is eliminated.
**Whether eliminating it is favourable on balance is a question this work does not settle**, and
quantifying it would require a control-allocation study rather than a single torque figure.

### Eight things this paper does not claim

**1. It does not claim range against fixed-wing aircraft.** The vertical axis is where the
fixed-wing family is the opponent; the range axis is not. A runway-launched aircraft that never
claimed vertical capability pays none of the charges of Section 2, and nothing here competes
with it on distance.

**2. It does not claim vertical capability against multirotors.** That comparison runs the other
way and would be absurd. The multirotor family is the opponent on cruise efficiency only.

**3. It does not claim that the aircraft has no moving parts.** What is eliminated is a *class
of mechanism* — the one that reorients a propulsor. The aircraft has a moving aerodynamic
surface, it is named where the elimination is claimed rather than later, and it also pitches the
nose down when deployed.

**4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and
maintenance burden were not measured, and nothing here supports a statement about reliability.
What is offered is a **count** of mechanism classes that a tilting architecture requires to
change regime and that this arrangement does not. A count is not a reliability argument, and
readers who convert one into the other are not quoting this paper.

**5. It does not claim that the escape condition is fully instantiated.** The condition is met
in the propulsor that carries the aircraft and is not met in the attitude system, which is
carried through cruise producing moments rather than cruise thrust. Section 3 names that case as
partial instantiation, and the charge it re-opens is reported rather than absorbed.

**6. It does not claim that satisfying the condition makes an aircraft better.** The condition
concerns three specific charges. A configuration may avoid all three and still be unbuildable,
uncontrollable, or unsuited to its mission, and the accounting says nothing against that
possibility.

**7. It does not claim that the trades inside the escape are favourable.** Moving the hover
peak onto a store converts a power-system charge into a mass one; serving two regimes with one
set of fixed-geometry propellers costs efficiency in at least one of them. Both are computed,
neither is asserted to be worth paying, and the ledger reports them whichever way they fall.

**8. It does not claim that the aircraft flies.** The design *sizes* vertical operation and the
transition; it does not demonstrate either. No aircraft has been built, no wind tunnel has been
run on this geometry, and the transition analysis is a calculation whose assumptions are stated
where it appears. **"By construction" throughout this paper means "by the sizing", never "by
demonstration."**

### What the claims that remain amount to

Removing those eight leaves something narrower than a first reading of the abstract might
suggest, and the narrower statement is the one the paper defends: **a configuration sized to
combine runway-independent vertical operation with wing-borne cruise efficiency, arranged to do so
with no mechanism that reorients a propulsor, and an account of what the combination costs.**

Each half of that has a named opponent and neither half is a record. **Nor is the configuration
claimed to be without precedent**: Section 1 sets out what is already established, including
uncrewed tail-sitters, tail-sitters without control surfaces, coaxial contra-rotating
tail-sitter propulsion, and blended-wing-body tail-sitters. **The contribution is the
architecture, and the paper presents it as the combination, the consequences of the choices inside
it, and the accounting** — which is what Sections 7 and 8 describe and what Section 11 prices.

### One consequence for how the numbers that follow should be read

Because the comparative result depends on the sizing contract, **no comparison in this paper
should be quoted without the contract it was computed under.** That is not a caveat attached for
safety; it is the paper's own finding applied to the paper's own numbers, and Section 13 states
what it demands of anyone who uses the framework afterwards.

---

## Yazarın denetimi için — bu sayfadaki her olgusal yüklem ve kaynağı

| İddia | Kaynak |
|---|---|
| **Tur 60:** *"rather than cruise thrust"* | Grok; Adım 3 (*"no cruise thrust in that sense"*) |
| **Tur 59:** *"the inventory of Sections 7 and 8"* — Adım 10, 12, 15 ile aynı ifade | Grok, DeepSeek |
| **Tur 58:** *"The contribution is the architecture, and the paper presents it as …"* — P1 ile tutarlılık için | Adım 1 (P1); CLAUDE.md §0.6 |
| Dört eksen, dört ayrı rakip | `CLAUDE.md` §0 tablosu |
| Kanatla taşıma ile rotorla taşıma ayrı verim sınıfı; sözleşme sınıf değiştirmez | §4.2, satır 2498–2502 |
| Öteki hibritlere karşı menzil iddiası **yok**, iki yönde de | §4.2, satır 2513–2517; §3.6, satır 1563–1566 |
| Lift+cruise'a karşı sıralama sözleşmeyle ~70 puan oynuyor; sabit MTOW'da işaret zarfın içinde değişiyor ve B'nin ölçülmemiş kaldırma grubu kesrine bağlı; tilt yalnız bir sınır olarak modellenebiliyor | Adım 13; `aero/contracts-result.txt` (**Tur 55'da güncellendi** — önceki hâli *"tersine dönüyor"* idi, v7 §3.6'ya dayanıyordu) |
| Sabit kanatlı menzilde rakip değil; hibrit bandın iki kenarı | §4.2, satır 2482–2489 |
| Elenen şey bir **mekanizma sınıfı**, "hiç hareketli parça yok" değil | `CLAUDE.md` §0.1; §1, satır 289–293 |
| Şerit tek hareketli aerodinamik yüzey ve burnu aşağı yunuslatıyor | §2.10, satır 815–818; §3.17 |
| "Mekanik olarak daha basit" denmez; denen şey bir **sayım** | `CLAUDE.md` §0.1 |
| Kısmî örnekleme: burun çifti sağlar, tutum sistemi sağlamaz | §2.7, satır 692–700; Adım 3, 4. başarısızlık kipi |
| Koşulu sağlamak uçağı **daha iyi** yapmaz | §3.1, satır 1126–1130 |
| Tampon: güç sistemi faturasını kütle faturasına çevirir | Adım 3, izin verilen bedel 1 |
| Sabit hatve iki rejimde birden en iyi olamaz | `paper/nose-pair-finding.md` |
| Uçuş gösterilmedi; *"inşa gereği"* = boyutlandırma | `CLAUDE.md` §0.3; §4.3 |
| Sözleşmesiz sıralama verilmez | §3.6, satır 1563–1564 |

**Bu sayfada BİLEREK olmayanlar: tek bir sayı yok.** İskelet bu adımı *"hiçbir sayıdan önce"*
diye konumlandırıyor ve gerekçesi sayfanın ilk paragrafında: sonuçlardan **sonra** çizilen
sınır bir geri çekilmedir, **önce** çizilen bir taahhüttür.

**Adım 14 ile farkı** ChatGPT'nin Tur 43 şartıdır ve sayfa bunu kendisi söylüyor: burası
**iddia etmeyi reddettiklerimiz**, orası **cevaplamadığımız sorular**. Biri kapsam, öteki borç.

**Yapı DeepSeek'in önerisi.** Retler bir savunma listesi olarak değil, dört eksenin **sonucu**
olarak sunuluyor: makale üçünde iddia ediyor, dördüncüsünde reddediyor, ve reddin gerekçesi
makalenin kendi merkezi bulgusu.
