# Round 29 — v8 begins. We are asking each of you for a table of contents.

---

## 0. How this round works, and one change

**The frame stays lifted.** Round 28 removed it and that was right. Answer what you
think matters, not only what is numbered below. `TO THE AUTHOR:` still gets relayed
verbatim, unsummarised, including where it contradicts me.

**One change, and it is deliberate: everything is shared.** Next round, **every
reply to this briefing will be given to all four of you in full** — not my summary
of it, the reply itself. You will see what the others wrote, and they will see what
you wrote. Write accordingly: disagreement is useful and will be visible.

**I have prepared my own answer to this round's question and it is deliberately not
in this document.** Putting it here would anchor you, which is the steering problem
the author caught in Round 28. Mine will be shared alongside yours next round, on
the same terms, and you are free to take it apart.

---

## 1. Verifying anything here

Repository: `https://github.com/LORDTEK/meryemAircraft`

The submitted manuscript — unchanged, and byte-identical to the Zenodo deposit
(DOI `10.5281/zenodo.22745666`), SHA-256 begins `c5b0cd898d20`:
`https://raw.githubusercontent.com/LORDTEK/meryemAircraft/e45d43c/makale/makale-v7.md`

*(That URL is pinned to an old commit, so it still uses the old Turkish path. The
repository's directories and filenames were translated to English on 16 September;
published version files were not touched, only renamed. Today the same file is
`paper/paper-v7.md`.)*

New since Round 28, all on the current branch: `paper/joa-compliance.md`,
`paper/v8-budget.md`, `paper/bacchini-reading-record.md`,
`paper/bacchini-draft-text.md`.

---

## 2. What I did since Round 28, and what came of it

You asked in Round 27 for the missing wind-tunnel reference to be dealt with. It has
been. Here is the whole of it, including the part that embarrasses me.

**The paper we were missing turned out to be a chapter of a thesis we had already
read.** Bacchini's doctoral dissertation (Politecnico di Torino, March 2020, open
access) lists under "research publications": *"Impact of takeoff propeller drag on
the performance of lift+cruise eVTOL aircraft. (Under submission)"* — the paper that
became Aerospace Science and Technology 109:106429 (2021). Chapter 5 of the thesis
**is** that work. We now hold the measurements first-hand.

**A number we were carrying was wrong, and it was wrong in the way this project is
supposed to catch.** Our revision list said, citing the 2021 paper, that retraction
reduces parasite drag by 38 % and increases range by 13 %. Those figures came from a
search-engine summary — mine, taken from a Round 26 report and never checked. **The
thesis says 34 % and 1.7 %.** The paper's own front matter had deliberately excluded
those numbers on the grounds that the source had not been read first-hand, and it was
right to. They are now flagged and will not enter the manuscript.

**What the measurement actually says.** University of Sydney 7 ft × 5 ft tunnel,
chord Reynolds number 280 000, four models: a clean airframe, a standard quadplane
conversion, an airframe that retracts its lift propellers, and a second retracting
airframe from a commercial manufacturer. At a cruise lift coefficient of 0.4 the
standard quadplane measures C_D = 0.044 against 0.029 retracted, the retracted
airframe being indistinguishable from the clean one. Maximum lift-to-drag ratios run
about 17 with the motors removed, about 13 with propellers aligned to the flow, and
about 9 with propellers perpendicular. The author explicitly warns that the 63 %
figure obtained by comparing the aircraft with itself is **not** the right comparison
and that 34 % against the standard quadplane is.

**What we can and cannot compare.** Disc-to-wing area ratio is 64.5 % in their model
and 12.7 % in ours — a factor of five. Absolute coefficients are not comparable and
we will not present them as though they were. What is comparable is the penalty as a
fraction of clean-airframe zero-lift drag: **62 % computed for our free-wheeling tip
rotors, 65 % measured for their quadplane hardware.** Different aircraft, different
scale, different Reynolds number. The agreement is of magnitude, not of coefficient,
and the text says so.

**And reading it produced something of our own, which is the part I did not expect.**
The thesis concludes from its measurement that takeoff propellers *"must be free to
rotate and to align to the airflow."* But it measured **locked** propellers, at two
fixed orientations. A propeller that is genuinely free to rotate does not align — it
turns. Our blade-element calculation puts it at 25 000 rpm at zero shaft torque,
costing twenty times the same blade held edge-on. **Freedom and alignment are
different states, and the first does not produce the second.** Holding a blade
aligned needs a mechanism to hold it — mass, and a failure mode. Their measurement
supports the comparison it makes; the recommendation generalises it to a state that
was not tested, and our calculation bounds that generalisation. This is now the
sharpest thing in that section and it exists only because the source was read rather
than cited.

**The bill transfer has also been priced from outside.** Their retraction mechanism
weighed 200 g of a 2 456 g aircraft. Applied to a published passenger design at 30 %
drag reduction and a 5 % mass fraction — with that mass taken out of the battery —
maximum range rose from 119 km to 121 km, **under two percent**, while the
best-range speed rose 5 m s⁻¹. The drag bill was really reduced and really paid for,
and the range column barely moved. That is what our framework predicts, measured and
costed by someone else.

**One apparent conflict, checked and dissolved.** The thesis argues the retraction
benefit grows with scale, because holding hover performance forces disc area to grow
faster than geometric scaling. Our Section 3.9 finds our own charge *falling* with
scale. They are not in conflict: our disc-to-wing ratio is constant to three digits
at both scales (0.127), and our charge falls because blade solidity drops and cruise
dynamic pressure rises. The two studies hold different things fixed — hover time
there, disc loading here.

**Still open:** the published author list. The thesis lists *"Verstraete, and
Benjamin Van Magill"*; our note said *"Magill, Verstraete"*. The journal version's
byline is not yet confirmed, and AIAA requires every author in full with no "et al."

---

## 3. Where we are sending it, and what that journal demands

**Target: *Journal of Aircraft* (AIAA).** Three of you named it in Round 27 and our
own reading of the scope agreed. The scope names **UAV and V/STOL** explicitly, and
it seeks *"discipline-level studies most applicable to the conceptual and preliminary
design process."*

**The clause that killed us at *Drones* does not exist here.** *Drones* publishes a
requirement that general theoretical aircraft-design work be validated with
experimental data from an unmanned platform, at least at laboratory scale. We failed
a written, checkable requirement we had never opened. **AIAA has no such clause.**
What it has instead is a policy on *Numerical and Experimental Accuracy* asking for
credibility and reproducibility of numerical results and enough information for
readers to assess them independently — which is the strongest part of this work, not
the weakest.

**The constraints are hard and several of them we currently violate.** From AIAA's
own author pages, read first-hand:

| Requirement | Our position |
|---|---|
| Full-Length Paper: **10 000–12 000 words** | body is **35 969** |
| That count **includes equivalent space for figures and tables**: 200 words per single-column object, 450 per two-column, 700 per large two-column table | we have **12 figures and 22 tables** = 34 objects. At 200 each that is 6 800 words — over half the budget before a sentence is written |
| Title **maximum 12 words, no acronyms** | ours is **16 words and contains "VTOL"** |
| Abstract **100–200 words, no acronyms, no numerical references** | ours is **214** and contains "VTOL" |
| Figure captions **20–25 words** | **11 of 12 exceed it**; the worst is 82 |
| Line art at **600 dpi** — 1 950 px at single column, 4 200 px at two | all but one pass single-column; almost none pass two-column |
| Conclusions **must not cite other work** | ours cites |
| References: AIAA numbered style, all authors, no "et al.", DOI where available | ours is MDPI style |
| Sites **with no archiving commitment** may not be cited | our data statement cites a bare GitHub link; it must become a DOI |
| Supplementary material allowed, but **the article must stand alone and is judged solely on its own content** | matches the author's own instruction exactly |

**Our working budget: about 7 500 words of text, 6 figures, 8 tables.** That is the
paper we are trying to write.

**One decision is the author's and is still open.** *Journal of Aircraft* has a
category found in no other AIAA journal: **Design Forum**, for *"design case studies
of actual or notional air vehicles… new design methodologies"*, same length, same
abstract — but *"Design Forum papers do not undergo routine peer review."* It fits us
almost too well, and it costs the peer-reviewed label. Comment if you have a view.

---

## 4. What v8 is, and the one thing that must sit at its centre

**v8 is a rebuild, not a cut.** Every one of you said in Round 28 that shortening by
moving paragraphs into the supplement would not work, and the author agrees. The
manuscript is being rewritten around its argument.

**Two rules the author has set, and they are not open:**

1. **No "in the earlier version we said" anywhere in the journal body.** In his
   words: *what you present must stand on its own; if someone is curious they can
   open the repository and see everything.* The correction history stays in the
   repository. Where a number currently carries its justification inside that
   history — the heavy-rotor interval is one — the justification gets rewritten in
   the present tense. It is not deleted.
2. **`meryemAircraft` stays in the title.** Settled. Plan around it. The title must
   still reach 12 words with no acronym.

### And now the thing I keep getting wrong

I am writing this paragraph as much to myself as to you, because I have lost it
before and the author has had to put it back three times.

**The centre of this work is a configuration that unites the tactical freedom of a
rotorcraft with the range of a fixed-wing aircraft — and reaches that union with no
mechanism that reorients a propulsor.** That is the thesis. Everything else in the
paper is either the accounting that shows why the union is hard, or the price the
configuration pays for it.

The two families each hold one half. Rotorcraft need no runway and cruise badly.
Fixed-wing aircraft cruise well and need a runway. Seventy years of hybrids have
tried to hold both halves and have paid an architectural price for it in three
coupled currencies. This configuration holds both halves, and the part that is new is
**how**: the airframe rotates and the propulsors do not, so there is no pivot, no
nacelle actuator, no variable-pitch hub, and no gyroscopic moment from a rotating
mass.

**The claims, and the one that is declined — mixing these up is the failure mode:**

| Axis | Opponent | Status |
|---|---|---|
| Range and cruise efficiency | **Multirotors** | Claimed. Sufficient. |
| Runway independence, vertical take-off and landing | **Fixed-wing** | Claimed, by construction. |
| **Absence of a propulsor-reorientation mechanism** | **Tilting architectures** | **The contribution.** |
| Range against the other hybrids | Lift-plus-cruise, tilt | **Not claimed.** |

Racing fixed-wing on range is absurd — nothing outruns a glider, and beating a
multirotor on distance is enough. Racing a multirotor on vertical take-off is equally
absurd — on that axis the opponent is fixed-wing and the advantage is by
construction. I have made both errors.

**The third claim is narrow and must stay narrow.** What is eliminated is the *class
of mechanism that reorients a propulsor*. It is **not** a claim that nothing on the
aircraft moves: roll cannot be produced by coaxial torque-balanced pairs at all and
comes from a variable-extension strip, which the paper calls the only moving
aerodynamic surface on the aircraft and which also pitches the nose down by ΔC_m
0.005–0.032. Pitch and yaw come from differential thrust. Nor is it a claim of
mechanical simplicity: part count, mass, failure modes and maintenance were never
measured. It is a **count of eliminated mechanism classes**.

**And the declined claim is declined on purpose, because it is a result.** Across the
computed drag bracket, lift-plus-cruise leads on range under equal fuel fractions by
24 to 45 percent; the tail-sitter leads under equal take-off mass by 29 to 43; under
equal fuel mass the sign changes inside the bracket. **A ranking quoted without its
contract is not a result.** That is the methodological finding, and it is why no
general range superiority is asserted.

---

## 5. What we are asking you for

**A table of contents for v8.**

Section by section, in order, with a word budget for each and the figures and tables
you would put in each. Where you feel you must, say what belongs inside a section —
but the contents list itself is the deliverable, not an outline of prose.

Work to these:

- **~7 500 words of text, 6 figures, 8 tables.** If you want a different split
  between text and objects, propose it and say what it buys.
- **Architecture leads; calculations are evidence.** If a section does not change
  what a reader believes about one of the four axes, say why it survives.
- **The union of runway independence and wing-borne range is the centre**, and the
  mechanism claim is how it is reached.
- **The body stands alone.** Six supplementary documents exist (S1–S6: aerodynamic
  validation, mass build-up, control axes, rotation authority and trim, full limits,
  bills and comparison) and can take detail — but a referee reads only the body.
- **Nothing is hidden.** The battery gap, the unmeasured free-wheeling drag, the
  borrowed roll coefficient and the unpredictable transition moment all appear in the
  body. The author's rule on weighting: results that survive get explained where
  there is room; unwanted data is stated briefly with a pointer to where the detail
  lives. Briefly is not silently.

Also tell us, if you have a view:

- **Which of the 22 tables and 12 figures earn a place**, and which merge.
- **Full-Length Paper or Design Forum.**
- **Anything in Section 4 above that you think is wrong.** Especially if you think
  the centre I have just described is not the strongest reading of this work. That is
  the question I am least able to judge for myself.

---

## 6. What does not change

- v7 is published and fingerprinted; corrections become v8.
- No range superiority is claimed against the other hybrids.
- The open items stay open and stay in the body.
- No brand, model or company name appears in the AI-use declaration, and no AI
  appears in the author line.
