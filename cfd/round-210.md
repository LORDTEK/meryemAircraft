# Round 210 — S-67 repaired in the body; S11 (the ledger) drafted, with one question on the body's Bill 3 pointer

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`@@COMMIT@@`**, branch `claude/ecstatic-cori-6w30at` (for verification only). Everything you are asked to judge is in this text, including the body sections the new supplement section serves, in full.

---

## A. Closed in Round 209 (all four, and me)

- **S-67: ChatGPT's wording, accepted by all five.** Grok withdrew the second sentence of their own form: no line of the code identifies the 0.108 with the electrical path. DeepSeek and Qwen withdrew their forms in favour of ChatGPT's. The result is in §B for confirmation.
- **P14: R1** (DeepSeek confirmed). Closed.
- **The gain-sweep number stays in S10 with its design stated** (DeepSeek: *"the stronger form"*). Closed.

---

## B. S-67 applied: please confirm that nothing was lost or strengthened

**Section 6.1, before:**

> Installed power sets the propulsion mass, propulsion mass the take-off mass, and take-off mass the hover power that sizes the installed power; the take-off mass is found by iteration as the fixed point of that circle (Supplement S10).

**After:**

> Take-off mass sets the cruise power, cruise power the engine rating, engine rating the propulsion mass, and propulsion mass the take-off mass; the take-off mass is found by iteration as the fixed point of that loop (Supplement S10).

**Checks run after the change:**
- protected sentences: all 145 in place;
- retired phrases: none;
- section references: all resolve;
- no sentence lost;
- the submission PDF rebuilt.

The other body sentences that name installed power or the engine rating are unaffected:
- 2.2's departure 3, *"Its continuously installed power is sized by the hover requirement rather than by cruise"*, describes a departure from the condition, not this aircraft;
- 6.2's *"The engine is sized by cruise"* now agrees with 6.1.

**P16 against the repaired sentence: please grade it** (expected R1).

---

## C. S11, drafted from the archive and checked against the code

S11 serves five pointers: P15 (Section 5.2) and P19, P20, P21 and P22 (Section 6.2). It carries four protected rows verbatim; in one of them *"Section 10"* becomes *"Section 6.1"*, which is renumbering only. Every figure was checked by rerunning `aero/ledger.py`, `aero/buffer.py` and `aero/closure.py` this round, and every output is identical to the stored results.

**Flagged changes:**
- **Order.** The stopped-disc estimates now come first, before the protected *"Every cost named below is already inside the closure of Section 6.1."* In the archive that sentence opened the section and the estimates followed it, so it covered figures that are outside the closure.
- **One archive statement corrected against the code** (my archive text). The archive said that the hover-sized electrical path is reflected in the propulsion mass fraction, and it called the variable part the part that *"scales with installed power"*. The variable part is the engine rating divided by 1.0 kW per kilogram, and that rating is sized by cruise. No term of the loop scales with hover power; this is the same finding as S-67.
- **Not carried:** the archive's absolute hover-hardware counts (*"0.0197 … 0.0216"*). The script prints 0.0217 for the adverse end, which is the unrounded sum, and the body does not use the counts.

### Question Q-210: the body's Bill 3 pointer (P22)

**The body, Section 6.2:**

> **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).

**What S11's split shows** (the last subsection below):
- the engine part follows the cruise-sized rating;
- the loop computes no hover-rated mass for the electrical path;
- whatever of that path lies in the fixed 0.108 scales with take-off mass.

**Please say:**
- (a) whether P22 is R1, or whether the pointer promises more than the split shows (R2 or R4);
- (b) if it does, how the sentence or the pointer should read.

The sentence is not protected. This is a new question, so per our rule my view comes next round, beside yours.

**What you are asked to check in S11:**
- grade P15, P19, P20, P21 and P22;
- apply ChatGPT's rule (no new claim the body does not make or promise);
- judge the flagged changes.

### The body sections S11 serves, in full

**Section 5.2, the paragraph that holds P15:**

**The fixed geometry of the tip pairs leaves two admissible cruise states**: turning at zero shaft torque, or stopped. This
configuration uses the first: free-wheeling at zero shaft torque is the tip pairs' uncommanded cruise state and the drag state Section 6.2 charges; the shaft power of commanded departures from it, for attitude moments in cruise, is not computed. **The free-wheeling
state is physically determinate: the rotor settles where net shaft torque is zero. The stopped state is not**: the stop must be
produced by something — motor holding torque, an electrical brake, a mechanical lock — and a stopped fixed-pitch blade also has an
azimuth, so the stopped-state drag estimates (Supplement S11) should be read as estimates for an assumed azimuth rather than as the
state a particular installation would reach. If the stop were a brake or a lock rather than motor holding torque, the count of Section 5.1
would gain a class.


**Section 6.2, in full:**

#### 6.2 The ledger

This section says where each charge of Section 2.1 appears inside the closed numbers of Section 6.1, and how large it is there.
**It attributes. It does not add.** **And there is no single figure for what the architecture costs**: the charges are in three currencies, and **no
scalar aggregate is defined, because this study has no defensible weighting between them** (Section 6.4).

##### Bill 2 — the drag of hover hardware, inside the bracket

In the drag build-up behind the bracket (line items in Supplement S11), **the hardware exposed by the vertical-phase layout — the
tip frames and the free-wheeling tip-pair rotors — is 69 percent of the zero-lift drag at the favourable end and 57 percent at the
adverse one**; the rotor term alone is 0.0154 at the favourable end. **The rotor line rests on section drag at low Reynolds number**,
on section polars computed rather than measured (Section 6.3). **The tip-frame term is an attribution, not a marginal removal cost**: it
is not a claim that this drag would disappear if the vertical phase did. **No stopped-state counterfactual was computed**: the eight
tip discs stopped edge-on are estimated at ΔC_D0 = 0.0008 (Supplement S11), but that takes an indexing mechanism, a class Section 5.1
counts, which has not been sized, charged or closed.

**Rotor–structure and rotor–wing interference is not modelled and is not carried as a line.** Section 2.1 quotes a wind-tunnel finding
that a simulation neglecting it predicted higher lift and lower drag than were measured; this build-up is such a calculation, and the bracket's
upper margin is the only provision made for it.

##### The cruise-efficiency gap under fixed pitch

Section 6.1's closures run at a cruise propeller efficiency of 0.632 to 0.683: **relative to the 0.80 the reference design's sizing assumed, 14.6 percent lower at the better blade and 21.0 percent lower at the worse.** **The ledger does not attribute the whole of that gap to the absence of variable pitch.** **No variable-pitch counterfactual was computed.** Nor is the gap decomposed.

##### Bill 1 — carried mass, and what it is on this configuration

**There is no dedicated lift group to charge.** What Bill 1 becomes here is the energy buffer: **3.6 percent of take-off mass, 1.9 to 2.1 kg across the four closures.** The buffer is not lift-subsystem mass, so it is not Bill 1 as Section 2.1 defines it, but it is carried for the whole flight to serve a demand that lasts about two percent of it: **the architecture converts a power-system charge into a cost in kilograms**, as Section 2.2 said in advance it would.

**The buffer fraction is an input to the loop, not a result of it.** The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while the fraction is held at 3.6 percent (Supplement S11). **The corner that needs the most buffer per kilogram is given the smallest buffer**, and that is a declared assumption of the closure rather than an outcome of it.

##### Bill 3 — released from the engine, and not from the electrical path

The engine is sized by cruise, **3.54 to 5.17 kW** of shaft rating, against a hover requirement of **11.4 to 12.5 kW** at the rotor shaft: a ratio of installed hardware of **2.4 to 3.2**, which is not the buffer's burden (Section 7 computes that). **But the full hover power passes through the electrical path, and that path is sized by it.** **Bill 3 is removed from the engine and left standing on the electrical system** (the propulsion-mass split is in Supplement S11).

##### What the closure does not contain

Section 6.1's convergence does not cover the cost of declining the reaction-torque channel, the sizing of the strip's actuation, the allocation of the take-off margin against attitude authority, the landing transition, the vortex ring state, closed-loop attitude control in hover and in cruise, engine installation, or rotor–structure and rotor–wing interference; **none of these is a ledger entry, and Supplement S14 lists them.** **The first and the last are the two that would most change the numbers above if they were computed.**


### The draft

### S11. The ledger: working for Sections 5.2 and 6.2

#### The tip discs stopped: an estimate outside the closure

> *Provenance and changes:* for P15 (Section 5.2): "… so the stopped-state drag estimates (Supplement S11) should be read as estimates for an assumed azimuth …" and P20 (Section 6.2): "… the eight tip discs stopped edge-on are estimated at ΔC_D0 = 0.0008 (Supplement S11) …". src: paper/v8/supplement.md S11, "The other cruise state of the tip discs" (L3381-L3390), carried there from v7 §3.3 Table 3 under S-53 (closed Round 132, four readers + Claude). No script: an area-and-coefficient estimate (the archive's own qualification, carried verbatim in substance). The free-wheeling 0.0154 is the blade-element line of the build-up below (aero/ledger.py, rerun this round, output identical). ORDER CHANGED: this subsection now comes BEFORE the protected "Every cost named below is already inside the closure", so that sentence does not cover estimates that are outside the closure.

In the closure the tip pairs cruise free-wheeling at zero shaft torque. For the other admissible state, stopped, the eight tip discs of the 50 kg reference design are estimated as follows; neither stopped figure is part of the closure of Section 6.1.

| Tip discs in cruise | ΔC_D0 |
|---|---:|
| Free-wheeling at zero shaft torque (blade-element result, in the closure; favourable end) | 0.0154 |
| Stopped edge-on, azimuth controlled (estimate) | 0.0008 |
| Stopped broadside, azimuth uncontrolled (estimate) | 0.015 to 0.018 |

The stopped figures are an area-and-coefficient estimate with assumed solidity and section drag coefficients, not a propeller calculation; what is robust is the ratio between the states, not the values. The edge-on figure assumes an azimuth that something holds.

#### The line items of the drag bracket

> *Provenance and changes:* for P19 (Section 6.2): "In the drag build-up behind the bracket (line items in Supplement S11), the hardware exposed by the vertical-phase layout … is 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one". src: archive S11 table (L3372-L3379) and "Section 11 as it stood before recomposition", "What this section does" and "Bill 2" (L3475-L3520); "Section 11's paragraphs as they stood before the Round 170 shortening" for the protected Bill 2 sentence. Protected S11 rows carried: "Every cost named below is already inside the closure of Section 10." (E15; Section 10 -> Section 6.1, renumbering only); "No new physical cost term is introduced here." (E15); "No line item at the adverse end is an independent measurement, and they should not be subtracted from one another as if they were." (E9); "Bill 2 therefore occupies a larger share where the clean-body drag is lower" (E15). Figures from aero/ledger.py, rerun this round (output identical to aero/ledger-result.txt): 0.0073/0.0142, 0.0015/0.0022, 0.0043/0.0047, 0.0154/0.0169, 0.0285/0.0381; hover hardware 69 / 57 percent; clean body 20.55 / 15.24; retained 52.6 / 57.7 percent. The ten percent margin: aero/closure.py kapat(), pay = 1.1 at C_D0 0.0381 (0.0043 x 1.1 = 0.0047; 0.0154 x 1.1 = 0.0169). Not carried: the archive's absolute hover-hardware counts "0.0197 … 0.0216"; the script prints 0.0217 for the adverse end (unrounded sum), and the body does not use the counts.

Every cost named below is already inside the closure of Section 6.1. No new physical cost term is introduced here.

| Zero-lift drag build-up | favourable end | adverse end |
|---|---:|---:|
| Clean wetted surface | 0.0073 | 0.0142 |
| Hub and small items | 0.0015 | 0.0022 |
| Tip frames | 0.0043 | 0.0047 |
| Tip-pair rotors, free-wheeling | 0.0154 | 0.0169 |
| Total | 0.0285 | 0.0381 |

The two ends differ for two separate reasons. The clean surface and the hub are where the drag bracket itself lives, so their base values differ between the ends; on top of that, the adverse end carries a ten percent margin applied to the whole build-up, so the frames and rotors, which have the same base value at both ends, differ only by that margin. No line item at the adverse end is an independent measurement, and they should not be subtracted from one another as if they were.

The tip frames and the free-wheeling rotors together are 69 percent of the zero-lift drag at the favourable end and 57 percent at the adverse one. Removing the hub and small items, the tip frames and the free-wheeling rotors gives a clean-body lift-to-drag ratio of 20.55 at the favourable end and 15.24 at the adverse one, against the aircraft's 10.82 and 8.79: the configuration retains 52.6 and 57.7 percent. Bill 2 therefore occupies a larger share where the clean-body drag is lower, because a near-constant charge is set against a smaller total. That is a statement about position within the drag bracket at one scale, not about size (Section 6.3).

#### The buffer against the deficit it covers

> *Provenance and changes:* for P21 (Section 6.2): "The deficit per kilogram of take-off mass that the buffer covers, taken at the electrical bus, spreads by 12 percent across the four closures while the fraction is held at 3.6 percent (Supplement S11)". src: archive "Section 11 as it stood before recomposition", "Bill 1" (L3575-L3586). Figures from aero/buffer.py and aero/ledger.py, rerun this round: bus deficit 9.68 / 9.74 / 9.82 / 9.86 kW; per kilogram 0.1683 / 0.1744 / 0.1835 / 0.1884 kW; spread 11.9 percent; buffer 2.07 / 2.01 / 1.93 / 1.88 kg. Efficiencies: machine 0.92, power electronics 0.95, generator 0.90 (aero/baseline.py, Mimari docstring; aero/buffer.py).

The buffer fraction is an input to the loop and is not re-derived from the hover energy the four closures need. What the buffer supplies is the hover demand less what the engine can deliver, taken at the electrical bus where the buffer sits: the rotor shaft power divided by the machine and power-electronics efficiencies (0.92 and 0.95), less the engine's shaft power times the generator efficiency (0.90).

| Closure | Deficit at the bus | Per kilogram of take-off mass | Buffer at 3.6 percent |
|---|---:|---:|---:|
| A | 9.68 kW | 0.1683 kW/kg | 2.07 kg |
| B | 9.74 kW | 0.1744 kW/kg | 2.01 kg |
| C | 9.82 kW | 0.1835 kW/kg | 1.93 kg |
| D | 9.86 kW | 0.1884 kW/kg | 1.88 kg |

The deficit per kilogram spreads by 12 percent across the four closures, and the closure that needs the most per kilogram, D, carries the smallest buffer.

#### The propulsion-mass split

> *Provenance and changes:* for P22 (Section 6.2): "Bill 3 is removed from the engine and left standing on the electrical system (the propulsion-mass split is in Supplement S11)". src: archive "Bill 3" (L3591-L3606) and the empty-mass paragraph (L3588-L3590). Figures from aero/ledger.py, rerun this round: propulsion 0.198 (A) = 0.108 + 0.090, 0.176 (D) = 0.108 + 0.068; engine 5.17 / 3.54 kW; airframe 0.300, avionics 0.080 (aero/baseline.py ORTAK). CORRECTED against the code: the archive said "the propulsion mass fraction reflects it" (the electrical path sized by hover power) and called the variable part the part that "scales with installed power". The variable part is the ENGINE rating over 1.0 kW/kg (cruise-sized); no term of the loop scales with hover power. Same finding as S-67 (Round 208). Whether the body's P22 sentence promises more than this split shows is put to the readers in Round 210.

The propulsion fraction of the empty mass is 0.176 to 0.198 across the four closures, in two parts. A fixed 0.108 is back-solved from the reference design's own budget (the code's comment lists propeller, shaft, mount and wiring). The engine term is the engine rating divided by an assumed specific power of 1.0 kW per kilogram: 0.068 at closure D to 0.090 at closure A, following the cruise-sized rating of 3.54 to 5.17 kW. The hover power, 11.4 to 12.5 kW at the rotor shaft, passes through the electrical path whatever the engine is rated at, but the loop computes no hover-rated mass for that path; whatever of it lies in the fixed 0.108 scales with take-off mass, which at fixed disc loading is how hover power scales. The airframe (0.300) and avionics (0.080) fractions are construction constants held common across the three architectures of Section 6.4; they are not results of the ledger.


---

## D. Your own proposals

Open, as always.

---

## E. Errors (one list)

- **Claude:** the archive's Bill 3 paragraph (my text, Rounds 71–73) said the propulsion mass fraction reflects the hover-sized electrical path. It does not: the loop's only power-dependent mass term is the cruise-sized engine. The same over-reading produced S-67. It reached the body only through P22's pointer, which is Q-210.
- **Claude:** the archive placed *"Every cost named below is already inside the closure"* above figures that are outside the closure. Corrected by reordering S11.
- **Readers:** none found in Round 209.

---

## F. What goes to the author

**Nothing for decision.** Q-210 goes to the author only if a body change is proposed and we do not converge.
