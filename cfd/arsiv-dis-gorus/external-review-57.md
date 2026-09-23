# Round 53 — four repairs to Step 10, and Step 11: the ledger as attribution

> **READ THIS FIRST.** Everything this round asks about is reproduced here. **You are not being
> asked to read a manuscript.** v8 is written as separate step files in `paper/v8/`;
> `paper-v6.md` and `paper-v7.md` are frozen historical records. **If your knowledge base holds a
> file whose name contains `makale-v` or `paper-v`, it is not what this round is about.**

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`8c799ac`**.
`paper/v8/11-the-ledger.md` SHA-256 `d71630f6c15d57e9ae4442b8bbfd2069249795aea30b3e129c762e5d41faed3e`
`paper/v8/10-the-closure.md` SHA-256 `027d0e8d3803091e12711973ac2d5f15384028bda676405118f8e55c9398da0e`

**This round had two readers.** ChatGPT was out of credit and Qwen could not complete an answer;
the author stopped it. **Grok and DeepSeek carried the round, and between them they found four
things in Step 10 and set the scope of Step 11.**

---

## 1. Grok's geometry finding — the one that would have made Sections 8 and 10 look like two aircraft

**Grok:** *"Four closures are four wing areas (1.95–2.27 m² at fixed C_L). Step 8 still describes
one planform (span 3.453 m, S = 1.979 m²). That is allowed if step 10 states the rule in one line
— wing loading and aspect ratio held, area follows mass — and states what does **not** scale
(nose diameter, tip-frame length, strip). If those stay fixed while S grows, disc loading and
control arms are no longer the inventory values. **Name the rule before a referee treats 8 and 10
as two aircraft.**"*

**Checked, and the rule turns out to cover more than Grok assumed.** The loop holds **disc
loading fixed as well**, so the nose diameter scales too:

| MTOW | Wing area | Span | Nose disc diameter |
|---:|---:|---:|---:|
| 50.1 kg | 1.98 m² | 3.45 m | 1.20 m |
| 52.3 kg | 2.07 m² | 3.53 m | 1.23 m |
| 57.5 kg | 2.27 m² | 3.70 m | 1.29 m |

So wing loading, disc loading and aspect ratio are held, and area, span and diameter follow the
mass. **What Grok was right about is what does not scale: the tip frames and the strip are not
sizing variables in this loop.** The section now says so, and says the consequence — *"the control
moment arms of Section 8 are therefore reference values that this closure does not re-derive…
These are the same configuration at four closed masses rather than four configurations."*

## 2. DeepSeek's Reynolds finding

**DeepSeek:** *"C_L is identical. The polar also depends on Re, which depends on chord, which
grows as √area… the section's current claim — 'the polar is valid at the closed mass' — is
technically only true for C_L, not for C_D0."*

**Correct, and computed here rather than taken on the quoted figure.** Chord rises about **7 %**
across the closure range. On a turbulent-flat-plate scaling, C_D0 ∝ Re^−0.2, that is **1.4 %** in
the zero-lift coefficient — against a bracket whose ends differ by **34 %**. *(DeepSeek estimated
0.75 %; the exponent matters and the figure above is what this work computes. Either way the
effect is inside the bracket by more than an order of magnitude.)* The section now carries it, and
says explicitly: **"The claim made above is that C_L is unchanged, not that C_D0 is exactly so."**

## 3. DeepSeek's seventh propagation instance, in the passage rewritten last round

**DeepSeek:** *"The parenthetical now covers the rotation times… But the passage also says the
light design loses 5.4 m. That 5.4 m was computed at 50 kg… The parenthetical does not cover this
number."*

**Right, and it is the seventh instance of the class — in the section that had just been
rewritten to fix a related problem.** The 5.4 m now carries its own clause, and Grok's related
point is handled in the same place: the thrust-to-weight figures of 1.066 down to 1.00 are
likewise reference-geometry values, not outputs of this loop.

## 4. DeepSeek on "unavailable"

*"The moment exists physically; it is not predicted by the methods used."* Taken: **"not predicted
reliably — the moment exists; what is missing is a method that predicts it."**

**On DeepSeek's point 3 (the 8.79/8.80 margins):** the envelope bounds 5.56 and 7.39 are indeed
unchanged; what moved was the interior corner B, 6.01 → 6.00, and the margin's last digit. Said
here for the record rather than added to the section, which reports the envelope and the corners
side by side already.

---

## 5. Step 11 — the ledger

**Its scope is yours.** Grok: *"Right as an anti-double-count rule. **Too narrow if it stops at a
list of absences.** A reader of a three-bill paper will expect the closed numbers **attributed**,
not increased."* DeepSeek: *"distinguish **decomposition** from **attribution**… and note that no
single 'cost of the architecture' figure is offered."*

**Both are implemented.** The section adds nothing; it decomposes Section 10's own numbers, marks
which terms the study separated and which it did not, and refuses a single figure with a reason.

**One result in it was not expected, and it is the part I would most like attacked.** Bill 2 turns
out to be **heavier at the favourable drag end than at the adverse one** — 47 percent of
clean-body lift-to-drag against 38 percent — because the rotor term barely moves while the clean
surface nearly doubles, so a near-constant charge takes a larger share of a smaller total.

**3.8× does not appear in Step 11**, per Grok's instruction that it stays one paragraph in
Section 14.

---

### The ledger

Section 2 named three charges that any architecture in this corner pays. Section 10 closed a
sizing loop. **This section puts the two together: it says where each charge appears inside
the closed numbers, and how large it is there.**

#### What this section does, and the one thing it must not do

**It attributes. It does not add.** Every cost named below is already inside the closure of
Section 10 — in the drag bracket, in the propeller efficiency, in the empty-mass fraction, in
the engine rating. **Adding any of them again would be double counting**, and the numbers that
follow are decompositions of quantities already reported rather than new charges on top of them.

**Two kinds of item appear, and the difference is stated rather than smoothed over.** Some
costs were computed per source and can be split: the drag build-up has named terms, and the
mass fractions were solved separately. Others are inside a single computed quantity and **the
study did not separate them**; saying otherwise would invent a decomposition that was never
performed. Each is marked.

**And there is no single figure for what the architecture costs.** The three charges are in
three different currencies — kilograms, drag counts, installed kilowatts — and a reader who
wants one number would have to be given a weighting this work has no basis for choosing. **The
ledger reports three quantities and refuses to collapse them.**

#### Bill 2 — the drag of hover hardware, inside the bracket

The zero-lift drag coefficient of Section 10 is a build-up with named terms. Splitting it:

| | favourable end | adverse end |
|---|---:|---:|
| Clean wetted surface | 0.0073 | 0.0142 |
| Hub and small items | 0.0015 | 0.0022 |
| **Tip frames** | **0.0043** | **0.0047** |
| **Attitude rotors, free-wheeling** | **0.0154** | **0.0169** |
| Total | 0.0285 | 0.0381 |

*(The adverse end carries a ten percent margin applied to the whole build-up, which is why
every term differs between the columns.)*

**The hover hardware is 69 percent of the zero-lift drag at the favourable end and 57 percent
at the adverse one.** The frames and the rotors they carry are the majority of the aircraft's
zero-lift drag in both cases, and the rotors alone are more than half of it at the favourable
end. **That is Bill 2 on this aircraft, in the terms Section 2 defined it.**

The same statement as a lift-to-drag ratio: removing the frames and the rotors gives a
clean-body ratio of **20.55** at the favourable end and **14.29** at the adverse one, against
the aircraft's **10.82** and **8.79**. **The configuration retains 53 percent of its clean-body
lift-to-drag ratio at the favourable end and 62 percent at the adverse one.**

**That ordering is the opposite of the one intuition offers, and it is worth stating plainly.**
Bill 2 is *heavier* where the rest of the aircraft is cleaner. The rotor term barely moves
between the two ends, while the clean surface nearly doubles; so at the favourable end a
near-constant charge is levied against a smaller total, and it takes a larger share. **An
architecture that improved its clean-body drag without touching its exposed rotors would find
this charge growing as a fraction, not shrinking.**

**One term inside Bill 2 is not separated, and it is not small in principle.** The build-up
computes each item on its own. **Rotor–structure and rotor–wing interference is not modelled
and is not carried as a line.** Section 2 quotes a wind-tunnel finding that a simulation
assuming negligible rotor–structure interaction *"always predicts higher lift and lower drag than
were experimentally observed"*; this build-up is such a calculation, and the bracket's upper margin
is the only provision made for it.

#### The price of fixed pitch, inside the propeller efficiency

Section 10's closures run at a cruise propeller efficiency of 0.632 to 0.683, against the 0.80
the published chain assumed. **That gap — 14.6 percent at the better blade and 21.0 percent at
the worse — is the price of refusing the variable-pitch hub**, paid by one blade geometry
serving a hovering condition and a cruising one.

**It is not decomposed, and it should not be read as though it were.** How much of the gap is
blade twist, how much is section drag at the cruise inflow angle, and how much is the operating
point itself, this work does not say. **The statement the ledger can make is that the computed
efficiency is what a blade meeting the hover figure of merit delivers in cruise, and that the
published assumption was optimistic by that margin.** Anything finer would be a decomposition
that was never performed.

#### Bill 1 — carried mass, and what it is on this configuration

**There is no dedicated lift group to charge**, which is the architectural claim of Section 7
appearing as an absence in a ledger. What Bill 1 becomes here is the energy buffer: **3.6
percent of take-off mass, 1.9 to 2.1 kg across the four closures.**

**Section 3 said in advance that this would happen and refused to call it free.** The buffer is
not lift-subsystem mass, so it is not Bill 1 as Section 2 defines it — but it is mass carried
for the whole flight to serve a demand that lasts about two percent of it, which is the
complaint Bill 1 makes. **The architecture converts a power-system charge into a mass one.**
Whether that trade is favourable is what the closure tests, and the closure is where the answer
is: the engine it buys is 3.54 to 5.17 kW rather than one sized by a hover peak of 11.4 to
12.5 kW.

The rest of the empty-mass fraction, for completeness, is airframe 0.300 and avionics 0.080,
both held common across architectures by Section 10's construction, and propulsion 0.176 to
0.198.

#### Bill 3 — released from the engine, and not from the electrical path

**This is the charge the architecture attacks most directly, and it is also the one where the
release is partial.**

The engine is sized by cruise: **3.54 to 5.17 kW**. The hover requirement is **11.4 to
12.5 kW**. The buffer supplies the difference for the vertical phase, and the ratio between the
two is **2.4 to 3.2** — that is the factor by which the continuously installed power plant is
smaller than the peak the aircraft must produce.

**But the full hover power passes through the electrical path, and that path is sized by it.**
Machines, power electronics and wiring between the buffer and the rotors carry 11.4 to 12.5 kW
whatever the engine is rated at. **Bill 3 is removed from the engine and left standing on the
electrical system**, and the propulsion mass fraction reflects it: of the 0.176 to 0.198 that
propulsion occupies, **0.108 is fixed and 0.068 to 0.090 scales with installed power.**

#### What the closure does not contain at all

The items above are inside Section 10's numbers. **These are not**, and a reader should not
take the closure's convergence as covering them.

| Item | Status |
|---|---|
| **The cost of declining the reaction-torque channel** | Not computed. Thrust asymmetry, propulsive efficiency and the lag set by rotor inertia; quantifying it requires a control-allocation study rather than a torque figure. |
| **The transition altitude result** | 5.4 m in the finite-moment model at the reference geometry — **a result, not a charge**, and not a term in any sizing loop here. |
| **The strip's actuation** | Carried in the systems budget without sizing the mechanism. The number of actuators is not fixed by this study. |
| **The take-off margin** | Drawn from the tip pairs, because the nose pair is sized at thrust equal to weight. It competes with attitude authority and neither is closed against the other. |
| **Landing transition, vortex ring state, closed-loop hover control** | Not analysed. |
| **Engine installation — bay, intake, exhaust, cooling** | Absent from this work entirely. |
| **Rotor–structure and rotor–wing interference** | Inside Bill 2 in principle, absent from the build-up in practice. |

**The first and the last are the two that would most change the numbers above if they were
computed**, and neither is a small correction to a known quantity: one is a control problem the
study has not posed, and the other is a term the study's method is known to under-predict.

#### What the ledger amounts to

**Three charges, three currencies, no total.** Bill 2 takes 38 to 47 percent of the clean-body
lift-to-drag ratio and is the majority of the zero-lift drag. Bill 1 appears as a 3.6 percent
buffer rather than a lift group. Bill 3 is divided by 2.4 to 3.2 at the engine and is not
divided at all on the electrical path. **Refusing the variable-pitch hub costs 14.6 to 21.0
percent of cruise propeller efficiency.**

**None of those numbers is new here.** Every one was already inside a quantity Section 10
reported, and this section's only work has been to say which part of which quantity it was.
Section 12 asks whether the three separate with scale, and Section 13 asks what happens to the
comparison when the sizing contract changes.

---

## 6. What I am asking

1. **Does the ledger add anything?** That is the one thing its scope forbids. Every figure should
   be traceable to a quantity Section 10 already reported. **If any of them is a new charge, it is
   the trap in prose form and I have walked into it.**
2. **Is the Bill 2 ordering right?** That Bill 2 is heavier where the aircraft is cleaner follows
   from the build-up arithmetically, but it is counter-intuitive enough that I would rather have it
   checked than admired.
3. **Is "three currencies, no total" a refusal a referee will accept**, or does it read as avoiding
   the question a cost section exists to answer?
4. **Does Step 11 hand off to Section 12?** 12 asks whether the three bills separate with scale —
   that they are separate quantities rather than three names for one. **Has Step 11 spent anything
   12 needs**, or left the separation harder to demonstrate than it was?

**No source is needed for any of this.** PDFs only for priority claims, numbers taken from tables,
and verbatim quotations.
