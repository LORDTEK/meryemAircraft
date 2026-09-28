# Round 140 — Your Round 139 votes were unanimous and are applied, shown for confirmation. The 2013 paper is in the repository and read. The first regime-completeness run over Step 14. Three proposals to vote.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 1. Applied — please confirm the result, word for word

All four of you and I voted the same on every item. ChatGPT withdrew *"the remainder"*, so *"the rest"* stays and that point is closed.

**Checks after applying:**
- `v8_stale`: now 163 retired phrases, including the five *"published"* forms. I tested it by putting the old Step 10 phrase back, and it
  caught it.
- `v8_caveats`: 187 protected sentences. The two protected rows are updated.
- `v8_nothing_lost`, `v8_assemble` and `v8_refs`: clean.

### 1.1 S-61 (b) — Steps 10 and 11

**Step 10** (protected):
> **The reference design's assumed zero-lift value of 0.0248 is not used**; the consistent build-up places it below both ends of the
> bracket, outside the supported range.

**Step 10:**
> Run on the reference design's assumed inputs — that drag coefficient without the rotor term, and a propeller efficiency of 0.80 — the
> same construction reproduces the 50 kg reference design within 1.5 percent (Supplement S10). That check is the only place in this
> section where the assumed value appears, so the closures report a change of inputs, not of method.

**Step 10:**
> … Every transition figure here belongs to a reference design at its reference mass and is not an output of the closure. …

**Step 11:**
> Section 10's closures run at a cruise propeller efficiency of 0.632 to 0.683: **relative to the 0.80 the reference design's sizing
> assumed, 14.6 percent lower at the better blade and 21.0 percent lower at the worse.**

**One consequence, recorded.** The frozen snapshots of Steps 10 and 11 in the supplement still say *"published"*. They are audit archive.
When the supplement is split, they do not go into the journal supplement.

### 1.2 N5 — Step 9, the protected table cell

> **Claimed against multirotors, and bounded; against helicopters the comparison with published figures is mixed and no advantage is
> claimed.**

### 1.3 N6 and §3 ii — two S14 rows

**The low-Reynolds row, its second cell:**
> | … | The rotor term in every closure — 0.0154, carried as 0.0169 at the adverse end with the build-up's ten-percent margin (Sections 10
> and 11) — and the size of Bill 2's fall with scale (Section 12) | … |

**The store row, its first sentence after the tag:**
> A supercapacitor store is tabulated in one survey at specific-power ranges that include values at the level required by the buffer —
> 500 to 10 000 W/kg from one cited source and 10 000 to 100 000 W/kg from another — at 1 to 10 Wh/kg (Rheaume and Lents 2016, Table
> 1, citing its references [8] and [14]).

### 1.4 F1 (now S-62) — Figure 2b

Only the labels changed. The boundary is still drawn.
- The label now reads *"slipstream boundary (estimate, not derived; Section 8)"*. It carries no number.
- The tip label now reads *"b/2 = 1.726 m"*.
- The figure was regenerated: `figures/output/v8-draft-f2b-strip-slipstream.png`.
- I checked the full label set against the body again:
  - nose pair *D* = 1.20 m;
  - inboard 46 %, outboard 54 %;
  - 2 cm and 6 cm;
  - 67 % of semi-span;
  - 45°;
  - *q* = 434 Pa.

  Each is in the body or the supplement.
- The label on the outboard part says *"roll in cruise"*. The label on the inboard part says *"authority at zero airspeed"*. Neither
  names a hover axis, so no axis name is crossed.

### 1.5 Rules adopted (§3 iii–vi)

1. **Regime field and regime completeness** in the debt trace.
2. **Framework versus aircraft:** framework limits are class E.
3. **S14 mapping:** every S14 row maps to a named Step 14 item or to the known obstacle.
4. **Five source layers:**
   - source fact;
   - the source's own limit or qualification;
   - source silence;
   - our classification;
   - our paper's claim.

The first run of rule 1 is §3 below.

---

## 2. The 2013 witness — read

The author uploaded the paper:
- **File:** `references/Oosedo-2013_ICRA_quad-rotor-tailsitter-without-control-surfaces.pdf`
- **Venue:** ICRA 2013, pp. 317–322, doi 10.1109/ICRA.2013.6630594.
- **Version:** the typeset IEEE Xplore version.
- **Status:** attributed → **verified primary**.

**Step 1's sentence is true as written, now at first hand:**

> *"**Attitude without aerodynamic control surfaces is established.** A quadrotor tail-sitter operated without control surfaces, with
> experimental verification, was reported in 2013."*

The source supports it three times:
- *"it does not use any control surfaces even in the level flight"* (p. 317);
- the aileron is fixed: *"we fixed the aileron to prevent it from moving"* (p. 318);
- hover, transition and level flight were flown outdoors, with 8 s of level flight and 33 s in all (pp. 321–322).

**What else it says, by the five layers.**

| Layer | Content (page) | Where it bears |
|---|---|---|
| **source fact** | four fixed-pitch rotors plus a fixed wing; mass 1.18 and 1.39 kg (pp. 318, 320) | classification below |
| **source fact** | *"The PID controller generates the desired differential thrusts for Xb, Yb axis control, the desired torque for Zb axis control"*; the distributor sets each motor's speed (p. 319). Zb is the thrust axis. The source calls it **yaw**, and its *"coordinate system … is consistent in every flight modes"* (p. 318) | It uses the reaction-torque channel about the thrust axis as a control channel. That supports Step 1's *"A quadrotor tail-sitter produces a rolling moment from the reaction torque of four independently driven rotors"*. The source calls the axis *yaw*, and our paper calls the same axis *roll*: the axis names are exchanged, not the physics |
| **source fact** | a wing under the propellers: the slipstream acting on it produces a moment about Zb opposite to the propellers' anti-torque, and *"the effect of the slipstream leads to the difficulty of the attitude control"*. The fix was to move the main wing out of the slipstream (p. 320, Fig. 4) | **§3, N8** |
| **source fact** | *"the altitude significantly fell in transition flight … The cause of altitude loss in transition flight is a lack of wing lift. The transition flight was performed quickly"* (pp. 321–322) | qualitatively consistent with Step 10's finite-moment result. But the aircraft, the controller and the manoeuvre are different (witness scope), so it is **recorded only** |
| **source fact** | *"a tail-sitter aircraft is the simplest way to achieve the VTOL maneuver since it does not require extra actuators for the VTOL maneuver"*; Quadshot *"requires six actuators for flying"* (p. 317) | supports *"The route itself is established"*; recorded |
| **source limit** | *"three times longer distance compared with … the conventional quad rotor helicopter"* comes from the authors' **earlier simulation**, and *"In the future, we will verify the improvement of energy efficiency"* (pp. 317, 322) | not measured here, so **not used** |
| **source silence** | no occurrence of *battery, hybrid, coaxial, contra-, counter-rotat-, blended, flying wing, variable pitch, collective, cyclic, swirl, fuel* | the evidence record keeps this list |

**Classification:**
- tail-sitter: yes;
- **(a): no** (a wing on a quadrotor frame, not a blended wing body);
- **(b): no** (four single rotors);
- **(c): yes** (fixed pitch, nothing reoriented);
- **(d): yes** (no moving surface at all);
- (e): not stated;
- (f): no.

**No obstacle.** It confirms an item Step 1 already lists. It also flies what this paper only sizes: a transition without control
surfaces, on a different and much smaller aircraft.

**My view:** Step 1 does not change. **Do you see anything in it that should?**

**My error, found here.** Step 1's audit table cited *"Oosedo 2013 (via De Wagter 2018)"* as the source of the reaction-torque sentence.
But De Wagter only says *"Oosedo et al. (2013) tried several structural variations with good results"* (p. 2), and the title says nothing
about reaction torque. Until today, that body sentence had no opened source. It has one now (p. 319).

---

## 3. Regime completeness — the first run over Step 14's eighteen items

| # | Step 14 item | Regime(s) the quantity acts in | S14 row covers | Finding |
|---|---|---|---|---|
| 1 | pitching moment through the transition | transition | yes | — (my view: closed-loop control through the rotation is carried here, because the row asks whether the moment suffices and whether the aircraft trims) |
| 2 | section drag at low Reynolds number | cruise (free-wheeling drag) **and hover** (the attitude-rotor blade is selected by its hover requirement on the same polars, S12) | cruise only | **N7** |
| 3 | stopped cruise state | cruise | yes | — |
| 4 | shaft power off free-wheeling | cruise | yes | — |
| 5 | buffer energy | vertical phases; recharge in cruise | yes | — |
| 6 | electrical path at peak | take-off and hover | yes | — |
| 7 | airframe mass | none | — | — |
| 8 | strip and fairing | strip: both regimes; fairing: cruise | yes | — |
| 9 | closed-loop attitude control | hover and cruise | yes (S-60) | — |
| 10 | vertical descent and landing transition | descent, transition | yes | — |
| 11 | ground handling | ground | yes | — |
| 12 | competitor's lift-group mass | none | — | — |
| 13 | competitor's cruise propeller efficiency | cruise | yes | — |
| 14 | rotor–structure and rotor–wing interference | cruise (Bill 2) **and hover** (the nose-pair slipstream on the inboard wing and strip) | cruise only | **N8** |
| 15 | engine installation | none | — | — |
| 16 | blade-family selection | hover and cruise | yes | — |
| 17 | variable-pitch counterfactual | both, closed through one loop | yes | — |
| 18 | atmosphere | hover and cruise | yes | — |

### N7 — the low-Reynolds row carries only the cruise side

**The row as it stands:**

> | **Section drag at low Reynolds number.** The attitude rotors' free-wheeling charge rests on section polars below a Reynolds number of
> 10⁵, and the uncertainty runs both ways. | The rotor term in every closure — 0.0154, carried as 0.0169 at the adverse end with the
> build-up's ten-percent margin (Sections 10 and 11) — and the size of Bill 2's fall with scale (Section 12) | **Validated data**: the drag
> of a free-wheeling attitude rotor, or of its sections, at about 8 × 10⁴, or a method validated there |

**The gap.** The same polars select the attitude-rotor blade that meets its hover requirement (S12: *"At 50 kg the hover requirement
selects the …"*). So the uncertainty reaches the hover side too.

**Proposed addition, at the end of the second cell:**
> *"…; and the attitude-rotor blade itself, which the hover requirement selects on the same polars (Supplement S12)"*

**My vote: yes.** It is supplement-only, adds no new unknown, and widens the scope to the true one.

### N8 — the interference row carries only cruise drag; Oosedo 2013 is the witness for hover

**The row as it stands:**

> | **Rotor–structure and rotor–wing interference.** Inside Bill 2 in principle, absent from the build-up and not modelled (Section 11); the
> drag bracket's upper margin is the only provision made for it. | Bill 2, and so every closure | **Analysis not yet done** |

**Why it is incomplete.**
- In hover, the nose pair's slipstream runs over the inboard wing and the strip. Section 8 uses exactly that: *"Its inboard 46 % lies
  inside the nose propeller's slipstream"*.
- Whatever force or moment that slipstream produces on the wing and the strip, beyond the strip's commanded action, is not computed. I
  searched the body and the supplement for *download*, *blockage* and *slipstream*; nothing treats it.
- The 2013 paper shows that on a quadrotor tail-sitter this effect was large enough to make control about the thrust axis difficult.
- Our nose pair is contra-rotating, which differs from their single rotors. Whether that makes the effect small is **not computed**, and
  I give no sign.

**Proposed row (R):**

> | **Rotor–structure and rotor–wing interference, in cruise and in hover.** In cruise it is inside Bill 2 in principle, absent from the
> build-up and not modelled (Section 11); the drag bracket's upper margin is the only provision made for it. In hover the nose pair's
> slipstream runs over the inboard wing and the strip (Section 8), and any force or moment it produces there beyond the strip's commanded
> action is not computed; on a quadrotor tail-sitter reported in 2013 the slipstream acting on a wing under the propellers made control
> about the thrust axis difficult, and the wing was moved out of it (Oosedo et al. 2013, p. 320). | Bill 2, and so every closure; in
> hover, the control about the body roll axis and the hover torque balance (Sections 5 and 8) | **Analysis not yet done** |

**Why the hover consequence names *"the body roll axis"*.** In hover that axis gives a change of heading (Section 8). The row therefore
uses the axis name, not a regime-dependent motion name.

**My vote: yes.** The body list item (*"rotor–structure and rotor–wing interference"*) names no regime, so the list and its count stay
unchanged.

---

## 4. Proposals to vote

| # | Proposal | Who | My vote |
|---|---|---|---|
| P-d | **Provenance status on every occupied-literature claim:** verified primary / verified secondary / attributed (title only) / unverified. It goes in the evidence record, and it is checked before submission. | ChatGPT | yes. The 2013 witness sat at *"attributed"* for fifty rounds while the body read as verified. |
| P-e | **A figure-number check script:** every number in a v8 figure's labels, annotations and caption must appear in the body or the supplement with the same identity. A value-only match is flagged for a human to read (the 0.47 case). | DeepSeek P3 + Qwen P1 | yes. I will write it after your vote, and test it by putting F1 back. |
| P-f | **An attributed-witness search protocol:** for every attributed witness, the evidence record holds, ahead of time, the search terms to run when the PDF arrives (the gap elements (a)–(f)), plus the date and the secondary source it came through. | DeepSeek P4 + Qwen P2 | yes. It ran for the first time this round, in §2's source-silence row. |

**DeepSeek R139-P2 (a coincidence record)** already exists: `paper/v8-coincidences-reviewed.md`. The 0.80 and 5.4 rows went in last
round.

---

## 5. What comes next in this stage

1. Your votes on §2–§4.
2. **H:** the record-propagation sweep, using the five source layers and P-d if it is adopted.
3. **I:** the Step 1 and Step 8 denial maps.
4. The whole reading in two halves (1–8, 9–15), then a short reconciliation.

---

## 6. Errors this round

- **Mine.** Step 1's audit row cited the 2013 paper, known only by its title, as the source for a reaction-torque sentence that the title
  does not support (§2).
- **Readers.** DeepSeek and Qwen acknowledged their Round 138 slips plainly. ChatGPT withdrew *"the remainder"*. I found no new reader
  errors this round.

---

## 7. Your own proposals

As always, give anything you see, with your reason. Answer the others by name where you disagree.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
