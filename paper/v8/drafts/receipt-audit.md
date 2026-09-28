# Receipt audit (P-Claude-1; Round 130)

**Scope.** Every body sentence that names another section or a supplement section (`Section N`, `Sections N and M`, `Supplement SN`, *the next / previous / last section*): **149 sentences.** Each was read against the receiving section's body and its supplement: does the receiver carry what the sender promises, and does the sender overstate it (ChatGPT's fourth category)?

**Not covered:** pointers without a section number (*above*, *below*, *the table*) — table references are `v8_refs.py`'s job.

**Categories (ChatGPT, Round 130):** R1 carried faithfully · R2 carried but qualified differently · R3 reference resolves, promised content absent · R4 sender overstates what the receiver establishes. S-53 = R3 + R4; S-54 = R4; S-55 = R3; S-56 = R3 + R4 (the promised content absent, and the sender's *"all three"* overstated; DeepSeek, Round 132 — the categories are not exclusive).

**Result: 144 hold; 5 sentences fail, in four defects — S-53 (known), S-54, S-55, S-56 (new).**

| # | Step | Sentence (start) | Verdict |
|---|---|---|---|
| 0 | 1 | The NASA sizing study used in Section 4 describes the two relevant routes in its own terms. | holds |
| 1 | 1 | The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice this configuration declines rather than a limit it inherit… | holds |
| 2 | 1 | None of the elements is new, and Section 7 says so. | holds |
| 3 | 1 | Section 2 states the cost that any architecture in this corner pays, in terms that do not presume an escape. --- | holds |
| 4 | 2 | Whether any architecture avoids the mismatch — and what it pays instead — is the subject of the next section, and it is not settled here. | holds |
| 5 | 2 | (The exponent is a property of the scaling rule chosen: holding disc loading constant instead makes hover power grow linearly with weight, and Section… | holds |
| 6 | 2 | The NASA sizing study of Section 4 found the lift-plus-cruise concepts the heaviest of the vehicles examined, and named the cause: not the cruise powe… | **S-54** — the quotation is from Silva et al. 2018 (`references/20180006683.pdf`), not the Section 4 study (Johnson & Silva 2022); cut before *"(wing and propeller)"*, which names cruise hardware carried in hover, not lift hardware carried in cruise |
| 7 | 2 | The ratio between the two demands follows from the governing equations rather than from any design choice (Supplement S2): P_hover / P_cruise = √(DL /… | holds |
| 8 | 2 | Whether a change of size moves them together, which would make them one quantity under three names, is tested in Section 12. | holds |
| 9 | 2 | Section 13 tests both the movement and the reversal on this configuration, and Section 4 tests a different consequence against a sizing study this wor… | holds |
| 10 | 2 | Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question, and the next section stat… | holds |
| 11 | 3 | What each departure costs is in Supplement S3. | holds |
| 12 | 3 | It means zero of the three charges as Section 2 defines them. | holds |
| 13 | 3 | It is not Bill 1 as Section 2 defines it — it is not lift-subsystem mass — but it is mass carried for a duty that is briefly needed, which is the same… | holds |
| 14 | 3 | Section 11 does. | holds |
| 15 | 3 | Three questions follow from it, and they are answered separately: whether the accounting behind the condition survives contact with an independent siz… | holds |
| 16 | 4 | The prediction has two halves, and only the first is a derivation. > First half, derived from Section 2. | holds |
| 17 | 4 | Section 2 predicts the charge and the amplification; it does not prove that the credit must lose. | holds |
| 18 | 4 | The check uses a NASA study, conducted for its own purposes and with no relationship to the present work, that sizes five VTOL architecture families —… | holds |
| 19 | 4 | The published weight breakdown is consistent with the transfer property of Section 2 — the mechanism giving part of the structural saving back — insid… | holds |
| 20 | 4 | The quadrotor is reported for scale, and the isolation test above is what carries the prediction: against it the lift-plus-cruise design changes three… | holds |
| 21 | 4 | The tilt-wing is consistent with the transfer property of Section 2, in someone else's data. | holds |
| 22 | 4 | It does not escape the accounting by avoiding the mass charge; it moves the cost — to the mechanism that reorients its propulsors, with the actuation,… | holds |
| 23 | 4 | A reader who wants to know whether the accounting flatters that configuration will have to wait for Section 11, where it is applied to it and where th… | holds |
| 24 | 5 | Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency, where a runway-launched aeroplane that never bought vertical capabi… | holds |
| 25 | 5 | One structure serves four purposes and is charged to the mass budget once — Section 8 gives the fairing's sizing. | holds |
| 26 | 5 | The vertical phase is sized: hover power from momentum theory at thrust equal to weight, the buffer that supplies what the engine cannot deliver of th… | holds |
| 27 | 5 | Those numbers exist and Section 10 reports whether they close, and with what margin. | holds |
| 28 | 5 | Whether this configuration's descent profile enters that region, and at what rate of descent, is an open question in Section 14 rather than an answere… | holds |
| 29 | 5 | That gap is wider than it looks, because this configuration declines the reaction-torque channel that comparable aircraft use about the body's longitu… | holds |
| 30 | 5 | What that refusal costs in authority and in response time is not computed, and Section 14 carries it. | holds |
| 31 | 5 | The tip frames that make the aircraft self-supporting are structure standing in the cruise airstream, and Section 11 charges their drag. | holds |
| 32 | 5 | The attitude propellers they carry are exposed for the whole cruise and cannot be feathered, and Section 11 charges that too. | holds |
| 33 | 5 | The second half — cruise carried on a wing rather than on rotors — is the subject of the next section, and the two are combined in Section 7. --- | holds |
| 34 | 6 | On this axis the alternative is the rotorcraft, multirotor and helicopter alike, and as in the previous section the comparison runs one way only. | holds |
| 35 | 6 | Section 5 established the first half: the aircraft must leave from and return to a site that supplies nothing. | holds |
| 36 | 6 | The sizing set of Section 4 reports an effective lift-to-drag ratio, defined in its own nomenclature as `L/De = WV/P`: weight times speed over power. | holds |
| 37 | 6 | Section 10 is where one blade is carried into a closed sizing loop; until then this section stays at envelope level and does not present any corner as… | holds |
| 38 | 6 | That higher gross weight is consistent with the mass charge Section 2 describes, and Section 4 is where the independent sizing evidence for it is set … | holds |
| 39 | 6 | Whether a variable-pitch hub would recover that difference is not computed; Section 11 reports the gap and declines to attribute all of it to the hub. | holds |
| 40 | 6 | The compared vehicles are 1 660 to 3 275 kg; the designs here are of order 50 kg and 1 000 kg — Section 10 closes the light one between 52.3 and 57.5 … | holds |
| 41 | 6 | The published figure is quoted at the best-range speed; this configuration's is at its chosen cruise condition, 1.49 times stall, which Section 10 sta… | **S-55** — Section 10 never states it (no version in the repository); the fact is in Section 6 itself and S6 |
| 42 | 6 | There is a second difference inside that one: the published value is the effective ratio of a fully sized vehicle, while the value here is a converted… | holds |
| 43 | 6 | Section 11 charges all three. | **S-56** — Section 11 charges only the third (the fixed-pitch gap); the wing carried through the vertical phase and the sweep constraint are charged nowhere |
| 44 | 6 | Section 7 is where they are combined, and the combination is what this paper is for. --- | holds |
| 45 | 7 | Each can be found on its own, and some of them together, in the literature and in hardware — Section 1 says where. | holds |
| 46 | 7 | The three elements, taken together, meet the escape condition of Section 3 in the propulsor that carries the aircraft, and they meet it with no mechan… | holds |
| 47 | 7 | It is offered for what it satisfies, and for what it does not need in order to satisfy it — and Section 1 has already set out how much of the ground i… | holds |
| 48 | 7 | Section 3 lists partial instantiation among the ways an architecture can fail the condition: meeting it where the aircraft is carried and failing it e… | holds |
| 49 | 7 | The instantiation is therefore partial, and reporting what the failing part costs is a substantial share of what Section 11 does. | holds |
| 50 | 7 | The strip of Section 8 is a control surface, of a different class, and is named below and in Section 8 rather than in the table. | holds |
| 51 | 7 | The means of stopping is not fixed by this study (Section 8). | holds |
| 52 | 7 | It could be produced by their reaction torque, and this configuration declines that channel by design (Section 8), assigning the axis to an aerodynami… | holds |
| 53 | 7 | That is a price of refusing the variable-pitch hub rather than an argument against refusing it, and it is charged in Section 11 with the other costs o… | holds |
| 54 | 7 | One thing this section does not establish, and Section 9 holds it to that. | holds |
| 55 | 7 | The combination carries costs: the attitude rotors that make the union controllable are themselves exposed in cruise, and Section 11 charges them. --- | holds |
| 56 | 8 | Section 7 claimed that a class of mechanism is absent. | holds |
| 57 | 8 | For the 50 kg reference design — the design this inventory describes; Section 10 re-closes it at four masses, and Section 12 sets it beside a 1 000 kg… | holds |
| 58 | 8 | No wattage is quoted here; the closed powers are Section 10's. | holds |
| 59 | 8 | That is a design assignment, not a demonstrated result (Section 7): the moment it produces is a sizing input to Section 10, and whether it suffices an… | holds |
| 60 | 8 | Both ends are computed rather than assumed and the charge appears in Section 11. | **S-53** — only the free-wheeling state is in Section 11 / S11; the stopped end was an estimate (sentence deleted, Round 130) |
| 61 | 8 | The nose pair meets all four parts of Section 3. | holds |
| 62 | 8 | The tip pairs do not: they hold one orientation, but they are carried through cruise producing moments rather than cruise thrust, which is the first o… | holds |
| 63 | 8 | This is the partial instantiation Section 3 lists as its fourth failure mode — meeting the condition where the aircraft is carried and failing it else… | holds |
| 64 | 8 | (They are sized for moments and used for them in both regimes; they add the take-off margin (Section 5) but were not sized for weight support. | holds |
| 65 | 8 | Section 3's permitted-cost clause therefore places them outside the first charge while leaving them in the airstream.) The free-wheeling state is phys… | holds |
| 66 | 8 | Neither the means nor the azimuth is fixed by this study, and the drag figure quoted for the stopped condition should be read as the state Section 11 … | **S-53** — no stopped figure is quoted and no state defined in Section 11 (protected clause; repair to vote) |
| 67 | 8 | The free-wheeling state needs no stopping means; the stopped state does, and if it were a brake or a lock rather than motor holding torque, the count … | holds |
| 68 | 9 | Those are in Section 14, and the difference matters: the boundary below is about claims the paper declines to make, most of which it could not make on… | holds |
| 69 | 9 | The fourth row is the important one, and the reason it is a refusal rather than a result is the paper's own finding in Section 13. | holds |
| 70 | 9 | Operation without a runway does not depend on the drag bracket, the propeller efficiency or the transition aerodynamics — but it does depend on the en… | holds |
| 71 | 9 | The size of the cruise-efficiency margin depends on both the drag bracket and the blade family, and Section 6 reports it as a range rather than a numb… | holds |
| 72 | 9 | The mechanism claim is a statement about what hardware is present, and it is settled by the inventory of Sections 7 and 8. | holds |
| 73 | 9 | The separate claim that this aircraft can actually perform the regime change is not settled (Section 7). | holds |
| 74 | 9 | This configuration declines the reaction-torque channel that comparable aircraft use for roll (Section 8). | holds |
| 75 | 9 | The count of mechanism classes in Section 7 is not a reliability argument. 5. | holds |
| 76 | 9 | Section 3 names that case as partial instantiation, and the charge it re-opens is reported rather than absorbed. 6. | holds |
| 77 | 9 | Nor is the configuration claimed to be without precedent: Section 1 sets out what is already established, including uncrewed tail-sitters, tail-sitter… | holds |
| 78 | 9 | The contribution is the architecture, and the paper presents it as the combination, the consequences of the choices inside it, and the accounting — wh… | holds |
| 79 | 10 | This section prices the arrangement of Sections 7 and 8 on a declared package; it does not bear on the count of mechanism classes, which rests on the … | holds |
| 80 | 10 | Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the tak… | holds |
| 81 | 10 | The zero-lift drag coefficient is uncertainty: a consistent build-up places it between 0.0285 and 0.0381 (Section 11), and a designer does not choose … | holds |
| 82 | 10 | The loop holds wing loading, disc loading and aspect ratio fixed, so the cruise lift coefficient is unchanged at 0.450 in every closure (geometry in S… | holds |
| 83 | 10 | The tip frames, the tip discs and the strip are not sizing variables; they were set on the 50 kg reference design of Section 8, and the control moment… | holds |
| 84 | 10 | Run on the published drag coefficient without the rotor term and the published propeller efficiency, the same construction reproduces the published ai… | holds |
| 85 | 10 | The loss is not an artefact of the controller: it is unchanged across three reference profiles, appears without the control moment saturating, and gro… | holds |
| 86 | 10 | What replaces it is not a prediction: the pitching moment that would make it one exists, but for the methods used here the predictions diverge above r… | holds |
| 87 | 10 | The energy store this closure assumes is the item Section 14 examines, and the examination does not end well. | holds |
| 88 | 10 | These ranges are carried forward as closed-loop values, not as a ranking: no rotorcraft is sized in this work, so no range comparison is made against … | holds |
| 89 | 11 | Section 2 named three charges that any architecture in this corner pays; this section says where each charge appears inside the closed numbers of Sect… | holds |
| 90 | 11 | Every cost named below is already inside the closure of Section 10. | holds |
| 91 | 11 | The total is the contract, not a property of the aircraft (Section 13). | holds |
| 92 | 11 | In the zero-lift drag build-up behind Section 10's bracket (line items in Supplement S11), the hardware exposed by the vertical-phase layout — the tip… | holds |
| 93 | 11 | It is a blade-element result for sections near a Reynolds number of 8 × 10⁴ in the free-wheeling state, on section polars that are computed rather tha… | holds |
| 94 | 11 | Bill 2 therefore occupies a larger share where the clean-body drag is lower, because a near-constant charge is set against a smaller total — a stateme… | holds |
| 95 | 11 | Section 2 quotes a wind-tunnel finding that a simulation assuming negligible rotor–structure interaction "always predicts higher lift and lower drag t… | holds |
| 96 | 11 | Section 10's closures run at a cruise propeller efficiency of 0.632 to 0.683: relative to the 0.80 the published chain assumed, 14.6 percent lower at … | holds |
| 97 | 11 | The buffer is not lift-subsystem mass, so it is not Bill 1 as Section 2 defines it, but it is carried for the whole flight to serve a demand that last… | holds |
| 98 | 11 | The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while th… | holds |
| 99 | 11 | The engine is sized by cruise, 3.54 to 5.17 kW of shaft rating, against a hover requirement of 11.4 to 12.5 kW at the rotor shaft: a ratio of installe… | holds |
| 100 | 11 | Bill 3 is removed from the engine and left standing on the electrical system (the propulsion-mass split is in Supplement S11). | holds |
| 101 | 11 | Section 10's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the … | holds |
| 102 | 11 | Every one of the charges above belongs to one scale: the four closures do not establish how the three charges behave as the aircraft changes size, whi… | holds |
| 103 | 12 | Section 11 decomposed the three charges on one aircraft, at one size; this section asks whether they are three quantities or one quantity under three … | holds |
| 104 | 12 | Either answer leaves the mechanism claim where it was; that claim rests on the inventory of Sections 7 and 8. | holds |
| 105 | 12 | The test is the 50 kg and 1 000 kg reference designs, sized by one method, not Section 10's closures: no closure was run at 1 000 kg, the heavy design… | holds |
| 106 | 12 | Section 11's measure of Bill 3, rotor-shaft hover power over engine shaft rating, is 4.19 at the light design and 3.98 at the heavy, and with the engi… | holds |
| 107 | 12 | (Section 11's 2.4 to 3.2 is the same ratio at the four closures. | holds |
| 108 | 12 | Within the blade-element and section-polar model, the section Reynolds number accounts for the fall, rising from about 8 × 10⁴ to 5.6 × 10⁵; three oth… | holds |
| 109 | 12 | Of the two rotor terms, the light one is therefore the less certain — and it is the one Sections 10 and 11 carry. | holds |
| 110 | 12 | Whether the two are separable here is not established; what is established is that they are coupled here, which is Section 3's claim rather than a def… | holds |
| 111 | 12 | It is consistent with the separability Section 2 asserts; it is not a verification of separability as a general property, which a single instantiation… | holds |
| 112 | 12 | The fixed-pitch gap also widens slightly with size, to 16.4 to 22.9 percent at the heavy design (Supplement S12); as in Section 11, no variable-pitch … | holds |
| 113 | 12 | Section 13 examines what the choice of sizing contract does to a ranking, on the light closures of Section 10 only. --- | holds |
| 114 | 13 | Section 12 showed that at least two of the charges are not locked together; where one architecture pays less of one charge and more of another, the ra… | holds |
| 115 | 13 | This section applies three contracts to three architectures at each of the four closures of Section 10. | holds |
| 116 | 13 | Range in the sizing loop is proportional to L/D, to the energy chain, propeller included, and to the fuel fraction, and the three contracts differ onl… | holds |
| 117 | 13 | The basis is not symmetric: the lift-plus-cruise layout carries a lift-to-drag ratio transferred from a different airframe's wind-tunnel campaign (Sec… | holds |
| 118 | 13 | Section 2 predicted that such a ranking will move when the sizing rule changes, and can reverse. | holds |
| 119 | 13 | Where the reversal falls is decided by quantities this study has not measured or not fixed: the blade family in the base case, and across the sensitiv… | holds |
| 120 | 13 | This paper meets that for its own column (Section 11) and not for the competitors', whose kilograms and drag counts here are parameters and transferre… | holds |
| 121 | 13 | Comparing computed figures against assumed ones favours whichever is assumed more optimistically — in propeller efficiency both competitors, and with … | holds |
| 122 | 13 | The comparison is at one size: Section 12's 1 000 kg reference design has no closure, and none of its figures is used here. | holds |
| 123 | 14 | Section 10 closed the sizing loop on a declared package and said that whether an aircraft can be built to it is a different question. | holds |
| 124 | 14 | Section 9 called this section a debt: questions the paper does not answer and that better evidence would. | holds |
| 125 | 14 | Every closure in Section 10 carries a buffer of 3.6 percent of take-off mass, an input rather than a result (Sections 11 and 12). | holds |
| 126 | 14 | Taken at the electrical bus, where the buffer sits, the four closures ask the buffer for 4.7 to 5.2 kW per kilogram of buffer to hover, and 5.5 to 6.1… | holds |
| 127 | 14 | A 24-series nickel–cobalt–manganese pack designed, bench-tested and flown in a 210 kg-class electric VTOL aircraft is rated, as a flown system, at 0.8… | holds |
| 128 | 14 | The study argues that, because pulse current limits can exceed continuous ones — by more than a factor of two in one commercial module it cites — a pa… | holds |
| 129 | 14 | The take-off demand of Section 10's closures is 3.7 to 4.1 times the bench rate — the highest figure obtained from a measurement — and 6.2 to 6.8 time… | holds |
| 130 | 14 | The package Section 10 closes on does not exist with any store the sources consulted here report as built. | holds |
| 131 | 14 | Closing the loop on a measured store is a sensitivity of that package, not a second aircraft: the buffer is derived inside the loop from the take-off … | holds |
| 132 | 14 | At the bench rate of about 1.5 kW per kilogram the loop closes at 94.6 to 101.2 kg, 76 to 81 percent heavier, with a buffer of 13.4 to 14.7 percent; a… | holds |
| 133 | 14 | These masses are the Section 10 package with one input changed. | holds |
| 134 | 14 | If Section 10's take-off masses are retained instead of re-closing at the bench rate, the payload falls to about 7 kg rather than 13; at the flown sys… | holds |
| 135 | 14 | This is where the coupling Section 12 found is paid: the buffer is the conversion the escape condition permits — kilowatts of hover peak paid in kilog… | holds |
| 136 | 14 | The escape from Bill 3 is real in the sense Section 3 defined it, and its price depends on a component whose required performance has not been demonst… | holds |
| 137 | 14 | It reaches every number that describes this aircraft at Section 10's masses: the closed masses of 52.3 to 57.5 kg and the 13 kg payload assume the sto… | holds |
| 138 | 14 | The vertical phase that Section 5 reports as sized was sized with this store in it, and Section 13's orderings were computed with the store held commo… | holds |
| 139 | 14 | Nor does it reach the cruise-efficiency comparison of Section 6 as a ratio: effective lift-to-drag ratio has no mass in it. | holds |
| 140 | 14 | As a comparison of aircraft, that section describes the configuration at Section 10's masses, which the store does reach. | holds |
| 141 | 14 | The remaining items are not known obstacles; they are questions this work has not answered, and each is listed with what would settle it in Supplement… | holds |
| 142 | 14 | The last section returns to the four axes of Section 9 and states what is claimed on each. --- | holds |
| 143 | 15 | The paper makes its claims on four axes, against four opponents (Section 9), and on each it stops where its evidence stops. | holds |
| 144 | 15 | The size of the advantage is a calculation, not a consequence of that statement: positive throughout against one published quadrotor, and from slightl… | holds |
| 145 | 15 | The vertical phase was sized with an energy store whose required performance the sources consulted here do not report as built (Section 14). | holds |
| 146 | 15 | The configuration is arranged to change regime by rotating the airframe rather than the propulsors, and so carries none of the mechanism classes Secti… | holds |
| 147 | 15 | The ordering belongs to the sizing contract (Section 13). | holds |
| 148 | 15 | Section 14 lists what would settle the rest. | holds |

## Re-run on the repaired text (Round 132; ChatGPT's item F)

149 sentences again. **Five are new or changed** (the S-53 to S-57 repairs); all five were read against their receivers and **hold (R1)**:

| Step | Sentence | Receiver | Verdict |
|---|---|---|---|
| 6 | *Section 11 charges the third.* | Step 11, the fixed-pitch gap | R1 |
| 6 | *The first two are inside Section 10's closed numbers — the wing's mass in the empty fraction, the constrained planform in the computed span efficiency — …* | S10 empty fraction (`aero/baseline.py`, f_govde 0.30); e = 0.817 trimmed VLM (S6) used in the bracket (`aero/drag_sweep.py`) | R1 |
| 8 | *… it is the drag state Section 11 charges.* | Step 11 Bill 2, free-wheeling rotors | R1 |
| 8 | *… the drag figures estimated for the stopped condition (Supplement S11) …* | S11, the two estimate rows | R1 (row 66 repaired) |
| 11 | *… (the estimate is an area-and-coefficient calculation, Supplement S11) … a class Section 7 counts …* | S11 estimate rows; Step 7 table (indexing) | R1 |

**Gone:** the five failing sentences of the first run (S-53 ×2, S-54, S-55, S-56). **Failures now: 0.**

## Kapanış kapısı, birleşik görünümde (Tur 150)

`paper/build/v8_receipt_diff.py`: bugünkü gövdede 152 işaretçi cümlesi; 135'i Tur 130 tablosundakiyle aynı (hüküm geçerli; S-53…S-56 onarıldı,
Tur 132 yeniden koşusu 0). **17 yeni ya da değişmiş cümle birleşik görünümdeki alıcıya karşı okundu: 17'si de R1** (liste Tur 150 metni §2.1).
Bölünmüş adım işaretçileri (Q-P1, `v8_assemble.py`): 13, hepsi R1. Kapsam dışı: numarasız işaretçiler (park listesinde). **Sonuç: başarısız alındı yok.**

## Tur 155 — 7.3 eke taşımasından sonra (birleştirme aşaması, B evresi)

Yeni işaretçi: *"The working is in Supplement S12."* → Ek S12, *"Section 12 as it stood before the supplement move (complete)"* — **R1**.
7.3'e işaret eden sekiz cümle yeni 7.3'e karşı okundu (2.1 ×2, 5.2, 7.2 ×3, 7.4 ×2, 8): hepsi **R1**. En hassası Bölüm 8'in *"This is where the
coupling Section 7.3 found is paid"*i — alıcı cümle (*"what is established is that they are coupled here … Coupling is not identity"*) gövdede
kaldı; Grok'un geri koyma isteği bu alındıyı korudu. 7.2'nin *"Section 7.3 shows how strongly the term depends on it"*i: Reynolds sayıları eke
gitti, ama bulgu (düşüşü Re açıklar, 0,29–0,65) gövdede — R1.

## Tur 157 — toplu kesimden sonra

Yeni işaretçiler: 5.2 *"The tip pairs are the parts that fail the escape condition (Section 5.1)"* → 5.1'in *"The single nose pair meets all four parts …
The four tip pairs do not: … The instantiation is therefore partial"* — **R1**. 7.4 *"… does not close under a fixed fuel fraction or a fixed take-off mass
(Supplement S13)"* → S13'ün tamponsuz paragrafı (38–47 %, 520 kg) — **R1**. ChatGPT'nin şartı (Tur 157): D evresinde 5.1 değişirse bu alındı yeniden okunur.
