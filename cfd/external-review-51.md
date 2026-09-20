# Round 47 — both roll-axis findings were right, and the documents proved more than you claimed; then I found my own error and it narrowed the paper's second claim

---

## 0. Verify what you are reading

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`ab39ba5`**
(this briefing lands one commit later).

```
paper/v8/06-the-second-half.md     SHA-256 0ac312273d195d5959850497b4b48dddf5f81c58d8e7955f0b31ef3f5d47fcab
paper/v8/05-the-first-half.md      SHA-256 a20ced694cba23fade532021d0fe10d1f642cd9c387206c602f2a98898ac72f3
paper/v8/01-the-gap.md             SHA-256 33d3d477804cd97ff4f715f1c1c2d7f0a1aa1919ce101bb3ee8b8391d79ef9cd
paper/v8/07-the-combination.md     SHA-256 197eb507a5ce6e42ad0c6c7f353459e37887f391c8b175f5231fa87d2b9113ff
paper/v8/08-what-it-is-made-of.md  SHA-256 1c107c979ec0c4e18644851360f4ed9dcf719cdcb4d1371b518747ae2b183127
paper/effective-ld-finding.md      SHA-256 8affa776985f7f36921f2b5530a241f6ea0064fd582faf8d3686a9cf50a5dd3a
paper/roll-axis-finding.md         SHA-256 6514853e26b6a62c25a338c4d6970666c99ef2055160a944070e587be14939a2
aero/effective_ld.py               SHA-256 5323b44da3b4c754330ae0fe58cf4b445a6dec8059cc36444144585c0dc15e0f
aero/reaction_torque.py            SHA-256 cdeef249f94f0f853da831dc54e4469956514e684eda9b38b7919b2e6990ef51
```

**If a hash does not match what you are reading, you have a stale file. Say so rather than
reviewing it.** That has happened twice in this project and cost a round each time.

**This round has three parts, and the middle one is the important one:**

1. Your two roll-axis findings from last round — **both confirmed**, and the uploaded documents
   proved them more sharply than either of you argued.
2. **An error I found in my own work while writing step 6.** It narrows a claim this paper has
   been leaning on since v5. I am reporting it before you find it.
3. **Step 6 — the second half, first writing, never reviewed.**

---

## 1. Both roll-axis findings were right

### Qwen: the "thirty-degree bank" is a heading change

§2.10 says, in its **hover** paragraph, that the strip gives 6.0 to 12.0 N·m, *"enough for a
thirty-degree bank in 1.5 to 2.1 s."*

Qwen said this is wrong, and it is. The strip produces a moment about the body's longitudinal
axis. In the hover attitude that axis is **vertical**, so the moment produces a change of
heading, not a bank. The number may be right; the word is wrong.

**And the deeper part of Qwen's finding is the one that matters:** the axes exchange duties
between hover and cruise. The left/right tip pair gives yaw in body terms and therefore **bank**
in hover; the strip gives roll in body terms and therefore **heading** in hover. The allocation
is actually favourable — hover lateral control needs bank, and bank comes from the longest
moment arm on the aircraft, 1.726 m — but the paper described it backwards.

### ChatGPT: "roll cannot be produced by propellers at all" ignores reaction torque

§2.10 says two things, one of which is right:

> *"every thrust vector is parallel to the body axis, so no combination of settings produces a
> rolling moment."* — **correct.**
>
> *"Roll cannot be produced by propellers at all, because every pair is coaxial and
> torque-balanced by construction."* — **wrong.**

§2.9 of the same paper states that **each rotor is driven by its own electric machine**. Two
independently driven counter-rotating rotors run at different speeds leave a net torque about
the body axis. **Magnitude, computed from the selected blades rather than estimated** — my first estimate was
low by a quarter, because it paired the paper's published hover power with an angular speed taken
from a blade that was not the one selected. The blades that actually hit the paper's figure of
merit turn slower, so the torque is larger:

| | per rotor | 10 % imbalance | 30 % imbalance |
|---|---:|---:|---:|
| Nose pair in hover | **24.9 – 27.5 N·m** | 2.5 – 2.7 N·m | **7.5 – 8.2 N·m** |

**The strip gives 6.0 to 12.0 N·m in hover.** A 30 % imbalance sits *inside* that range, not at
its lower edge, and reaching the strip's lower bound needs only 22–24 %. **Cross-check:** the
computed pair power, 10.85–11.08 kW, independently reproduces the paper's published 10.9 kW to
within 1.7 %.

**And the paper contradicted itself.** §2.9, discussing the untrimmed hover torque residual,
says it may be absorbed *"by the **speed trim of the pairs**."* That is the same channel it
denies elsewhere.

### What the two uploaded documents did to these findings

**Both were read first-hand. The first extraction interleaved the two columns and the quotes did
not match; re-extracting with the layout preserved fixed it.** That is worth saying because a
mismatched quote nearly became a "not found in the source" verdict.

**Zhang et al. 2012** (`cfd/ica20120400001_12673514.pdf`), a coaxial contra-rotating tail-sitter.
Its Table 2, quoted exactly:

| | **Vertical Mode** | **Horizontal Mode** |
|---|---|---|
| Yaw Motion | **Differential velocity of the two motors** | Rudde[r] |
| Pitch Motion | Stabilizer | Stabilizer |
| Roll Motion | Rudde[r] | **Differential velocity of the two motors** |
| VTOL | Increase or decrease the combined thrust of the two motors | – |

**That single table proves both of your findings at once**, and neither of you claimed this much:

- **ChatGPT's finding.** A coaxial, contra-rotating, torque-balanced pair produces a moment about
  the body axis by differential motor speed — and on that aircraft it is the **primary channel in
  both modes**. The prose confirms it: *"It balances the anti-torque of the rotors by the inverse
  rotating of the two rotors"*, and then *"Roll motion is controlled by the differential velocity
  of the two motors."*
- **Qwen's finding.** The **same physical channel** is called *yaw* in the vertical mode and
  *roll* in the horizontal one. The axis does not change; its name does.

**Novlit et al. 2014** (`cfd/2014_0529_paper.pdf`), a coaxial contra-rotating tail-sitting MAV:

> *"A pair of 10 inches coaxial contra rotating propellers is mounted to compensate each other's
> torque."*
>
> *"Elevon and rudder are immersed in the propeller slip stream to provide three axis control
> moments in hover."*
>
> *"…the definition of the roll and yaw angles are **interchanged.** The roll angle now
> represents the angle between the horizontal surface and the connecting line of the right and
> left wingtips, while the yaw angle represents the rotation around the centerline of the MAV
> fuselage."*

The third quote is Qwen's finding named in the literature, ten years ago.

### What was changed

The claim is now **narrow and it is a choice rather than a limit**:

> Roll cannot be produced by the propellers' **thrust**: every thrust vector is parallel to the
> body axis. It **could** be produced by their **reaction torque** — each rotor has its own
> machine — which is a channel the tail-sitter literature uses. **This configuration declines
> it**, operating every pair torque-balanced so that no reaction torque is spent on control, and
> assigns the axis to an aerodynamic device instead. That is a design constraint, not a physical
> impossibility, and **what declining it costs is not counted in this work.**

Steps 7 and 8 carry that. Step 8's axis-naming paragraph was rewritten so hover and cruise names
are never mixed. **Step 5 needed no change — it makes no roll claim; I searched rather than
assumed.** Step 1 gained both documents in its "what is already occupied" section, and its gap
paragraph lost a sentence that the Zhang table falsifies:

> ~~*"a torque-balanced coaxial pair cannot produce a rolling moment by any setting, which the
> quadrotor tail-sitters can"*~~

**New open item, created by the correction:** declining the channel has a price — thrust
asymmetry, efficiency loss, and lag from rotor inertia. **None of it is computed.**

---

## 2. My own error this round. I am reporting it before you find it.

This is the part I most want you to check, because **it narrows the paper's second claim** and I
would rather be wrong about the narrowing than wrong about the claim. Nobody asked for this
calculation; it came out of writing step 6 and finding that the two numbers being compared were
not the same quantity.

### The error

The paper compares this configuration against multirotors in three places, always like this:

> *"the sizing set puts a turboshaft quadrotor at an **effective** lift-to-drag ratio of 4.9 …
> against this configuration's **aerodynamic** 8.8 to 10.8."*

The paper **says** these are different kinds of number and warns they are *"offered for scale
rather than as a measured margin."* **The warning is true and insufficient.** A reader who sees
4.9 against 8.8–10.8 reads a factor of two. That is not the margin.

### The conversion, and the proof that it is legitimate

Johnson & Silva's own nomenclature (p. 94):

> `L/De   aircraft effective lift-to-drag ratio, WV/P`

In level cruise thrust equals drag and lift equals weight, so with shaft power `P = DV/η_p`:

> **L/De = WV/P = (L/D) · η_p**

**I did not assume which power `P` is — I proved it from the source, because getting it wrong
would double-count η_p.** Equation (2) writes cruise energy as `E = (Pc/ηc)·t` and calls `ηc`
*"the propulsion system efficiency in cruise"*, which on its own is ambiguous. The proof is in
the hover analogue, equation (3):

> `I = (Ph/ν)/ηh`  with  `Ph = W√(W/2ρA)/FM`

`Ph` is hover power **with figure of merit already applied** — shaft power — and `ηh` sits
*outside* it. So `ηh` is the electrical chain, not the rotor's aerodynamics; **FM does the
rotor's work.** By exact symmetry `ηc` is the electrical chain in cruise and `Pc` is shaft power.
Therefore **L/De already contains the propulsor's efficiency**, and multiplying our aerodynamic
ratio by η_p is the correct conversion rather than a double count.

**Cross-check:** invert it on their own vehicles. At η_p ≈ 0.80, tiltwing 8.6 → L/D ≈ 10.8;
lift+cruise 8.5 → L/D ≈ 10.6. Both sensible for the class. The conversion does not produce
nonsense.

### The result

Our aerodynamic ratio is **8.80 to 10.82** across the zero-lift drag bracket, with tip frames and
free-wheeling rotors already charged. Our propeller efficiency is **0.632 to 0.683**, from the
two-point blade-element solution you reviewed two rounds ago.

| | L/De |
|---|---:|
| This configuration, adverse corner | **5.56** |
| This configuration, favourable corner | **7.39** |
| Quadrotor, turboshaft | 4.9 |
| Quadrotor, all-electric | 5.8 |

| Comparison | Margin |
|---|---|
| What the paper has been placing side by side (8.8–10.8 vs 4.9) | +80 % … +121 % |
| **In one currency (5.56–7.39 vs 4.9)** | **+14 % … +51 %** |
| Against the all-electric quadrotor (5.56–7.39 vs 5.8) | **−4 % … +27 %** |

### Two things follow, and I am not softening the second

**(a) Against the quadrotor that uses the same kind of energy source, the sign holds at every
corner.** Closing the margin would need η_p to fall to 0.557 against a computed worst case of
0.632 — a margin of 0.075.

**(b) "We beat rotorcraft on cruise efficiency" is false as stated.** NASA's all-electric
quadrotor reaches 5.8, **above our adverse corner of 5.56**. That vehicle buys the difference
with 1 742 lb of battery and nearly twice the gross weight for the same mission — 7 221 lb
against 3 678 lb — which is exactly the charge our own framework predicts. **But on cruise
efficiency taken alone, it is ahead of our worst case.**

### What I changed as a result

> **The phrase "different efficiency class" is retired.** v7 says *"a vehicle that carries its
> cruise lift on a wing is in a different efficiency class from one that carries it on rotors."*
> **+14 % is not a class difference.**

The structural statement survives — lift is carried on a surface or on rotors, and no sizing
contract moves a vehicle between them — but it is now separated from the quantitative one.
**And the thing compressing the margin is not the wing. It is our own refusal of the
variable-pitch hub:** at η_p = 0.85 the same airframe reaches 7.48 to 9.20.

**I want to be challenged on this.** Specifically: is the `L/De = (L/D)·η_p` identity right, is
the ηh/FM symmetry argument sound, and is pairing the adverse L/D with the adverse η_p the honest
bracket or an over-conservative one?

---

## 3. Step 6 — the second half, first writing, not yet reviewed

Three qualifications are stated in the section and **all three run against us**: scale (1 670–3 275 kg
against 50 kg, and Reynolds favours the larger); the compared quadrotor has an unusually low
3.5 lb ft⁻² disc loading, so it is a good example rather than a poor one; and the speeds are not
matched — theirs is at best-range speed, ours at 1.49 × stall, which our own sizing section says is
**not** our best lift-to-drag point.

**The full text is in `paper/v8/06-the-second-half.md` at the hash above.** Its structure mirrors
step 5: the opponent and the axis · what the requirement is · what the configuration does instead ·
what the margin actually is, in one currency · three qualifications · what is sized and what is not
demonstrated · what this half costs.

**Deliberately absent from it, and I want to know if any of these is a mistake:**

- **No range number against a multirotor.** No multirotor is sized in this work; inventing a range
  comparison would be fabrication. The comparison is confined to cruise efficiency and to the
  published sizing set.
- **Nothing at all against fixed-wing aircraft.** A runway-launched aeroplane cruises better than
  this configuration and pays none of our charges. This project has twice written a fixed-wing
  range comparison by accident and twice had it caught; it is now a standing prohibition.
- **No mass advantage.** Bill 1 is built in step 2 and measured in steps 11 and 12.

---

## 4. The source rule, and its boundary — unchanged from last round

You asked, correctly, that this be workable rather than heroic.

> **A downloadable PDF is requested only for things that could FALSIFY a claim:**
> **(a) priority and novelty claims** — any sentence saying "this has not been done";
> **(b) numbers** — any value taken from a table;
> **(c) verbatim quotations.**
>
> **No source is requested for opinion, judgement, structural proposals or criticism of style.**
> Most of the value of these rounds comes from exactly those, and they need no citation.

**And the reciprocal holds: a number whose document you did not open THIS round is not used.**
If you cannot open it, please say so and give no number. A hedged number is worse than no number,
because it enters the record as data.

**It worked three times now, in three directions.** Round 45 it confirmed our numbers. Round 46 it
falsified our gap claim. Round 47 it proved your roll findings more sharply than you argued them.

---

## 5. What I am asking of you

**On step 6 (fresh, never reviewed):**

1. Is the margin stated honestly, or does the section still read as if it were claiming more than
   +14 %?
2. Is it right to make the turboshaft quadrotor the primary comparison because it shares our energy
   source — or is that the evasion it could look like, given that the all-electric quadrotor is the
   one we do not clear at the adverse corner?
3. Three qualifications are given and all three run against us. Is any **fourth** missing?
4. Does the section still earn the word "half"? Step 5 and step 6 are supposed to be the two halves
   that step 7 combines.

**On the conversion (section 2 above):** attack the identity and the ηh/FM proof. If it is wrong,
the number moves and I would rather it moved now.

**On the roll correction (section 1):** the new open item — the unpriced cost of declining the
reaction-torque channel — is real. Is it small enough to name and defer, or does it need a number
before the paper can claim the channel is declined "cheaply"? **The paper does not currently claim
it is cheap. Should it have to?**

**Structural, and no source needed:** steps 1, 2, 3, 4, 5, 6, 7, 8 and 9 now exist. **Does the
argument run in that order?** The remaining steps are 10 (analytical closure of the sizing loop),
11 (the ledger), 12 (the bills separate with scale), 13 (rankings belong to contracts) and 14 (what
does not close).

---

## 6. Where the work stands

**Written:** steps 1–9 except step 6's review. **Not written:** 10, 11, 12, 13, 14.

**One contribution: the architecture** — a configuration that reaches the regime change with no
mechanism that reorients a propulsor. The three-bill framework is the instrument that makes that
claim checkable, not a second and equal contribution.

**What is claimed, on three axes against three different families:** runway-independent vertical
operation against fixed-wing aircraft; wing-borne cruise efficiency against multirotors, now at
**+14 % to +51 %** rather than the factor of two the old pairing implied; and freedom from the
propulsor-reorientation mechanism class against tilting architectures, which is the contribution.

**What is not claimed:** a range ranking against the other hybrids. That ranking reverses with the
sizing contract, and it is reported as a case result rather than defended as a thesis.

**Target: *Journal of Aircraft* (AIAA).** Two desk rejections, never to peer review.

**Nothing here has been measured.** No wind tunnel, no flight test. The pitching moment through
transition remains the largest open item, and three methods of three fidelities fail at the same
incidence — so it belongs to measurement rather than to computation.
