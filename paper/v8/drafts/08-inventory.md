# Step 8 — semantic inventory (Round 98; before any draft)

Source: `08-what-it-is-made-of.md`, 2 174 words. **P** = protected (6 rows). Assembled position: Section 5.2 (the inventory)
and Section 6.1 (what the inventory does not settle). It is the hardware behind Section 5.1's count, and Qwen P1 asks that it
show the absence of each of the five mechanism classes.

Sources opened for this inventory, with the surrounding text read (the source-opening rule):
- `references/NACA-TR-796_interim-report-stability-control-TAILLESS-airplanes.pdf` — the C_nβ criterion;
- a repository search for the XB-35 (see S-31).

| Block | Must say | Evidence (status) | Must qualify (P) | Must not say | Restatement: of what, and status |
|---|---|---|---|---|---|
| **8A Airframe** | The whole airframe is the wing; the sweep, thickness and chord distributions; the 50 kg reference geometry (3.453 m, 1.979 m², AR 6.03); sweep and longitudinal stability are one variable | the paper's geometry | — | — | 6G (Section 4) states the tailless constraint first; 8A is its second home, and its job is the inventory's reason why sweep is not free (*"one design variable seen from two directions"*) → keep, but a candidate for the draft |
| **8B Propulsion** | Five stations, ten rotors, every station a counter-rotating pair, for reaction torque; nose pair 1.20 m for all propulsive thrust; tip pairs 0.20 m on rigid frames; **fixed geometry — no cyclic, no collective, no variable-pitch hub, no mechanism that changes a rotor's orientation**; each rotor on its own machine, so no splitting gearbox; net angular momentum nominally zero, so no gyroscopic moment in the rotation | own design. *"the arrangement that repeatedly defeated the XB-35"* — **no source in the repository → S-31** | — | a claim about the shafting | *"precesses nothing"* is unqualified, while 8F says the hover residual may be absorbed by a speed trim of the pairs, which would give the pair a net angular momentum → **S-30** |
| **8C Energy path** | Series hybrid; the engine drives no rotor; it is sized by cruise; the buffer supplies the hover difference; no wattage is quoted here, and the closed values are Section 10's | — | — | superseded wattages | *"The figures published for this configuration were closed on a propeller efficiency this work has since replaced with a computed one …"* and the sentence after it are a **previous-version narrative** in the journal body (CLAUDE §4) → **S-32** |
| **8D What produces each moment** | Pitch and yaw from tip-pair differential thrust, yaw arm 1.726 m = 2.43 × pitch arm 0.71 m; the same system is assigned the rotation through transition (not demonstrated); **roll from neither: a choice, not an impossibility**; reaction torque could, and is declined; the strip's geometry; modulated; pitches the nose down; inboard 46 % in the slipstream | own geometry; Zhang 2012 via Step 1 | **P** *"What declining it costs is not counted in this work."* | that roll is physically impossible; that the transition is demonstrated | Step 7H restates the roll and strip paragraph and points here (*"Section 8"*) → this is the home, keep. The P56 variant (*"no combination of thrust settings produces a moment about it"*) is allowed here |
| **8E What meets the ground** | Five points; the fairing is the only vertical surface, sized to C_nβ > 0.001 per degree → 39 mm against the 50–70 mm a faired strut carries anyway; the flight control system is part of the mechanism; the tip frames do four jobs | NACA TR-796, **verified**: *"The value of the directional-stability parameter Cnβ, recommended for conventional airplanes, is usually greater than 0.001 per degree"*; tailless aircraft *"should be as great as required on conventional airplanes"*. **Source-conclusion: supports**, and it adds that models *"have been flown … with a value of Cnβ of only one-third this amount"* (recorded; it makes the 39 mm conservative, not optimistic) | — | that directional stability needs a fin | *"The aircraft rests on five points … It stands on its tail in its own storage attitude, with no launch equipment present."* restates Step 5C almost word for word → **candidate: keep "five points" as an inventory line, remove the storage-attitude sentence**. *"The tip frames therefore do four jobs at once …"* restates Step 5C's *"One structure serves four purposes"* and its stance/arm coupling, and ends on the cruise exposure charge (the fifth statement of that cost: 3E, 5F, 7C, 7L, here) → **candidate removable**. The named job, *"the inventory is given here in full"*, is met by 8B–8E without it |
| **8F What moves** | The propellers rotate at commanded speed and change neither orientation nor pitch; the strip is the one thing that changes configuration, in two halves; the actuator inventory is the motors plus the strip's actuation | — | **P** *"How many actuators that is, this study does not fix."* | a number of actuators | Step 7J states the inventory sentence first; this is its home → keep |
| **8G What it does not settle** (Section 6.1) | The untrimmed hover torque (body-axis naming fixed; the channel set aside; absorb by speed trim — not shown — or a fourth duty on the strip); the two cruise states of the tip pairs; the tip pairs fail the condition (partial instantiation); the stopped state is not determinate | own analysis | **P** *"Either the residual is small enough …, or a fourth duty falls on the strip."*; **P** *"The tip pairs are the parts that fail the escape condition"*; **P** *"The free-wheeling state is physically determinate … The stopped state is not."*; **P** *"should be read as the state Section 11 defines …"* | that the hover residual is solved | The partial instantiation is also protected in 7C: two protected homes, neither can go. *"a stopped … blade … requires the stop to be produced by something — motor holding torque, an electrical brake, a mechanical lock"* bears on Step 7's table → **S-33** |

## Five mechanism classes against this inventory (Qwen P1)

| Class (Step 7 table) | Where Step 8 shows it absent | Status |
|---|---|---|
| Pivot or tilting joint | 8B: *"no mechanism that changes a rotor's orientation relative to the airframe"* | absent |
| Nacelle or rotor-group actuator | 8B, same sentence; 8F: *"none of them changes its orientation"* | absent |
| Variable-pitch hub | 8B: *"no cyclic pitch, no collective, no variable-pitch hub"* | absent |
| Dedicated lift rotors | 8G: the tip pairs *"were not sized for weight support"*; the nose pair serves both regimes | absent |
| Rotor stowing, indexing or stopping mechanism | 8G: the free-wheeling state needs no means; the **stopped** state *"requires the stop to be produced by something — motor holding torque, an electrical brake, a mechanical lock"*, and *"neither the means nor the azimuth is fixed by this study"* | **absent only in the free-wheeling state; open in the stopped state → S-33** |

## Outbound

Steps 7 (the count; the strip; the declined channel), 9 (non-claims), 10 (the reference geometry), 11 (the two cruise states; the
tip-frame drag; the strip's actuation), 14 (the untrimmed torque; the strip; the fairing), 15.

## Inbound

Section 3 (the condition, the failure modes, the permitted-cost clause), Section 5 (the take-off margin), Section 7 (the claim
it backs).

## Candidate source findings (to vote; none applied)

- **S-30 (8B).** *"the net angular momentum of the propulsion system is nominally zero: rotating the airframe through ninety
  degrees precesses nothing, and no gyroscopic moment appears for the control system to cancel."* 8G offers a speed trim of
  the pairs as one way to absorb the hover residual. Two rotors of one pair at different speeds carry unequal angular
  momentum. Proposal: *"…precesses **nominally** nothing, and no gyroscopic moment appears **unless the pairs are
  speed-trimmed (below)**"*. Or simply *"precesses nominally nothing"*.
- **S-31 (8B).** *"the arrangement that repeatedly defeated the XB-35"* has no source in the body or in the repository. It is
  a historical claim a referee can check, and *"repeatedly defeated"* is strong. Proposal: remove the clause unless a reader
  supplies a downloadable source. The sentence stands without it.
- **S-32 (8C).** *"The figures published for this configuration were closed on a propeller efficiency this work has since
  replaced with a computed one, and the re-closed set belongs to Section 10 rather than to an inventory. Quoting the
  superseded numbers beside a propulsion section that no longer assumes them is precisely the inconsistency this paper is
  trying not to commit."* This is the previous-version narrative that the project rules keep out of the journal body.
  Proposal: *"No wattage is quoted here; the closed powers are Section 10's."*
- **S-33 (8G against Step 7's table).** Step 7 counts *"Rotor stowing, indexing or stopping mechanism"* as absent. Step 8 says
  the stopped state needs a means of stopping, possibly an electrical brake or a mechanical lock, and does not fix it. In the
  free-wheeling state the count holds. In the stopped state it may not, unless the stop is motor holding torque.
  - The table's class is defined for dedicated lift rotors, and the tip pairs are not dedicated lift rotors. But a reader
    who sees a lock on a rotor will not read that as a definitional nicety.
  - Proposal, one sentence in 8G: *"The free-wheeling state needs no stopping means; the stopped state does, and if it were a
    brake or a lock rather than motor holding torque, the count of Section 7 would gain a class."*
