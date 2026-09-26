# Step 6 — semantic inventory (Round 95; before any draft)

Source: `06-the-second-half.md`, 2 206 words. **P** = protected (22 rows). Assembled position: Section 4, the second half of
the combination, after Section 3 (the first half) and before Section 5.1 (the combination).

Sources opened for this inventory, with the surrounding text read (the source-opening rule):
- `references/1521_Johnson & Silva_122721.pdf` — Table 3 in full (PDF p. 70), the mission paragraph (Vbr, 5 000 ft ISA+20),
  and the paragraph after Table 3;
- `references/Bacchini-Cestino-2019_electric-VTOL-configurations-comparison_Aerospace.pdf` — abstract and conclusions.

**Qualification direction column (Qwen P2).** Every qualification is given the direction the text claims for it and the
direction the text actually supports.

| Block | Must say | Evidence (status) | Must qualify (P) | Must not say | Restatement: of what, and status |
|---|---|---|---|---|---|
| **6A The opponent** (33–38) | The opponent on this axis is the multirotor; the claim is confined to what the multirotor lacks, a surface that carries cruise lift | — | **P** *"Nothing here is claimed against fixed-wing aircraft."* | any fixed-wing comparison | *"A runway-launched aeroplane cruises more efficiently than this configuration and pays none of the charges of Section 2; that comparison is not made, and no result in this paper rests on it."* restates 5A (first home, protected) and Step 9 item 1 → **candidate removable** |
| **6B The requirement** (42–52) | A multirotor meets the first half completely; it does not meet the second, covering distance; one study concludes the same | Bacchini & Cestino 2019 — **verified**: abstract *"The multirotor is more efficient in hover. The vectored thrust jet is more efficient in cruise and has a higher range. The lift + cruise is a compromise."*; conclusions: *"Short-range missions are best performed by multirotors … Long-range missions cannot be accomplished by multirotors"*. Its "vectored thrust" example is the Lilium jet (tilting ducted fans) — recorded, not a defect: the witness is for the wing, not for the mechanism | — | that the multirotor is deficient | *"It is not a deficient machine and this section does not treat it as one; it is excellent at what it does and is limited by the price of doing it that way."* restates Step 1A almost word for word (*"Neither family is deficient. Each is excellent at what it does and is limited by the price of doing it that way."*) → **candidate removable**. *"buys every second of that distance with installed power"* echoes 1A → weak |
| **6C What the configuration does** (56–73) | The whole planform is the wing; the nose pair only balances drag; the wing lifts without a continuous power supply of its own; lift is on a surface or on rotors, and no contract moves a vehicle between the two; **the size of the advantage is a calculation** | the paper's own polar | **P** *"The size of the resulting advantage is a calculation, not a consequence of that statement."* | that the structural statement fixes the margin | first. **Bears on S-27**: *"Lift is carried on a surface or it is carried on rotors"* is the structural statement; a wingless helicopter in the same source reaches the upper part of this configuration's envelope |
| **6D The margin in one currency** (77–158) | L/De = WV/P is a system figure; L/De = (L/D)·η_p; P is shaft power (proved from the source's battery-capacity derivation); two spreads of two kinds; the 2×2 corners; two readings; 0.683 not settled; against the two quadrotors: turboshaft holds at every corner (break-even η_p 0.557), all-electric not at the low corner; the claim is narrower than the structural statement; the fixed-pitch blade compresses it (0.85 → 7.47–9.20) | J&S 2022 **verified** (L/De definition p. 94 nomenclature; Table 3: quadrotor TS 4.9 / 3 678 lb / 3.5 lb ft⁻², electric 5.8 / 7 221 lb / 3 lb ft⁻² / battery 1 742 lb; Vbr); corners and 0.557 **model-derived** (`aero/effective_ld.py`) | **P** *"These are the bounding corners of a product, not four simulated aircraft."*; **P** *"Whether 0.683 is the blade a designer would actually choose is not settled here."*; **P** *"Against the all-electric quadrotor it does not hold at the low corner, and that result is reported as a result rather than as a caveat."*; **P** *"variable-pitch hub would recover that difference is not computed; Section 11 reports the gap and declines to attribute all of it to the hub"* | a single performance number; that the corners are aircraft states; that the gross-weight difference is caused by the mass charge (only *"consistent with"*) | *"These are the bounding combinations permitted by two independent model inputs."* restates the protected corner sentence → weak candidate (the rest of that bullet adds a limit). **Table 3 has seven more L/De entries than the two quoted → S-27** |
| **6E Five qualifications** (160–198) | They are given together; each is stated with its direction | see direction table below | **P** ×10 (scale; Reynolds; good quadrotor; poor example; speeds; best point; direction-not-magnitude; best speed; atmospheres + "not claimed here, because it has not been computed"; analysis chains; independently produced figures) | that the comparison is a validation or a controlled reproduction | **the heading overclaims → S-26** |
| **6F Sized / not demonstrated** (202–217) | Sized: drag build-up, L/D at cruise, η_p by BEMT, range by the chain. Not demonstrated: nothing measured; planform chosen, not optimised; e = 0.817 computed, not 0.85 assumed; methods diverge above about ten degrees | the paper's own sections | **P** *"No part of this has been measured."*; **P** the 0.817 sentence; **P** the ten-degree clause | that the ten-degree divergence touches cruise | first |
| **6G What this half costs** (221–229) | The wing is carried through the vertical phase and faces ground wind; the tailless planform constrains sweep; the fixed-pitch propeller sets the margin; Section 11 charges all three; Section 7 combines the halves | — | **P** *"The two halves are now on the table separately. Section 7 is where they are combined, and the combination is what this paper is for."* | — | *"— at a propeller efficiency η_p = 0.85 the same airframe would reach 7.47 to 9.20"* is the **second** statement of 6D's number → **candidate removable** |

### Qualification direction (Qwen P2)

| Qualification | Direction the heading claims | Direction the text supports |
|---|---|---|
| Scale (with Reynolds number) | against this configuration | **against** — *"the smaller design is at a disadvantage in this comparison"* |
| The quadrotor is a good quadrotor | against | **against** — the reference is strong. Note: the disc loading quoted, 3.5 lb ft⁻², is the turboshaft's; the all-electric one's is 3 (Table 3). Both are low |
| Speeds not matched | against | **against, calculable** — the reference at best-range speed, this configuration not at its best L/D point |
| Atmospheres not matched | against | **none claimed** — *"The direction of that mismatch is not claimed here, because it has not been computed"* (P) |
| Analysis chains not matched | against | **no direction** — it bounds what the comparison can be called |

## Outbound

| Taken by | What |
|---|---|
| Step 7 | the second half of the combination |
| Step 9 | the multirotor claim as narrowed; no fixed-wing comparison |
| Step 10 | one blade carried into the closure; e = 0.817 |
| Step 11 | the three costs of 6G; the η_p gap and the hub |
| Step 15 | the cruise axis: 5.56–7.39 against 4.9 and 5.8 |

## Inbound

Section 2 (charges), Section 2.3 = Step 4 (the NASA study, the L+C and tilt-wing figures 8.5 and 8.6 already in the body),
Section 3 = Step 5 (the first half), Section 10 (closure masses; the cruise point is not the best-L/D point), Section 11.

## Candidate source findings (to vote; none applied)

- **S-26 (6E heading).** *"Five qualifications, and every one of them runs against this configuration"*. The text supports
  "against" for three of the five. For the atmospheres it says the direction **is not claimed**; the analysis chains bound
  what the comparison can be called and have no direction.
  - Proposal: *"Five qualifications: three run against this configuration, one has no computed direction, and one bounds
    what the comparison can be called"*.
  - The sentence under it, *"omitting any one of them would make the comparison look better than it is"*, still holds.
    Omitting an uncomputed direction makes the comparison look more certain.
- **S-27 (6D) — Table 3 read in full.** Two of its nine L/De entries are quoted in 6D. Of the other seven:
  - The lift-plus-cruise and tilt-wing designs (7.9 to 8.6) are already in the body at Step 4, on the axis where nothing
    is claimed. **Record them as omitted here, with that reason.**
  - The **two helicopter types** — the multirotor's nearest relatives, also without a wing — reach **5.4 to 7.2**. The
    all-electric side-by-side is 7.2, which is above this configuration's 6.84 corner and just below its 7.39 corner.
    These appear nowhere in the paper, and they bear directly on 6C's *"Lift is carried on a surface or it is carried on
    rotors"*.
  - Proposal, after the quadrotor table: *"The same table gives the study's two helicopter types 5.4 to 7.2; the
    all-electric side-by-side helicopter, which has no wing either, reaches the upper part of this configuration's
    envelope. The claim here is against the multirotor, and it is not extended to the helicopter."*
- **S-28 (6E, good quadrotor).** *"Its disc loading is 3.5 lb ft⁻²"* describes the turboshaft quadrotor only, directly
  after a paragraph that treats both as equal. The all-electric one is at 3 lb ft⁻² (Table 3).
  - Proposal: *"Their disc loadings are 3.5 and 3 lb ft⁻², which are unusually low and unusually efficient."* The
    protected *"The quadrotor is a good quadrotor."* would need its own vote if it becomes plural.

## Round 96

Inventory and direction column confirmed (four + Claude). Applied: 6A, 6B, 6G removals; S-26 heading. **Not applied:** S-27
(agreed, but the voted wording's *"The same table"* would have pointed at this paper's comparison table — R-4, caught by
`v8_refs.py`, reverted); the weak 6D removal (agreed, but it would leave *"They are not four demonstrated aircraft states"*
pointing at a label — R-5); S-28 (divided). Grok P60: 6C's *"Lift is carried on a surface or it is carried on rotors"* stays
a description of this paper's split, not a claim that rotor-borne cruise cannot reach 7.2; S-27 is the lock (Qwen P1 asks the
same trace link). Qwen P2: all nine Table 3 values are in `paper/v8-evidence.md`.
