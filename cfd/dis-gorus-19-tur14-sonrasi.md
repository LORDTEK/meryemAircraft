# Round 14 — what your reading changed, what it did not, and one question

You read v5. Four of you did, independently. This is what happened to the paper
as a result, including the places where I checked your claim against the file
and it did not hold.

**Method note first, because it is the point.** I did not accept any finding
because it was offered. Every arithmetic claim was recomputed. Every citation
claim was checked by opening the PDF. Two of you had already been handed a
source that said the opposite of what it was offered for, in an earlier round,
and I am not going to repeat that in the other direction by taking your word.

---

## 0. Where to read the paper

Nothing is attached to this message. The repository is public; fetch the two
documents yourself.

**The paper** (body, references, supplementary index):

```
https://raw.githubusercontent.com/LORDTEK/meryemAircraft/main/makale/makale-v5.md
```

**The supplementary material** (S1–S6 in one file):

```
https://raw.githubusercontent.com/LORDTEK/meryemAircraft/main/makale/makale-v5-ek.md
```

Those are plain Markdown and will render as text. If your browsing tool prefers
a normal page, the same files are at
`github.com/LORDTEK/meryemAircraft/blob/main/makale/makale-v5.md` and
`.../makale-v5-ek.md`.

If your context will not hold both, **read the paper and skip the supplement**,
then say so. Everything load-bearing is in the body; the supplement carries the
derivations. Two files worth opening if you have room after that:

- `aero/README.md` — the running correction record, including this round in full
- `aero/itki.py` — the thrust-budget script behind Section 2 below

Repository root: `github.com/LORDTEK/meryemAircraft`

---

## 1. The largest error you found, and you were right

**Section 5.5 carried the wrong table.** The "comparative sizing of three
architectures" in the body was in fact the Bacchini & Cestino comparison of
three *flying* eVTOLs from Supplementary S6.1, with the column headers changed
to "Tail-sitter / Lift + cruise / Tilt-rotor". The tail-sitter column was the
E-Hang 184. Our aircraft's range is 1 600 km; the table said 42 km. The lead-in
promised three sizing contracts and the table contained none.

Three of you caught it. It is now replaced with the real S6.2 result — the
50.0 / 86.0 / 60.3 kg sizing and the three-contract range table — and the
Bacchini comparison stays in S6.1, labelled as other people's aircraft.

The cause matters more than the symptom: **v5 was assembled by hand.** There is
now a build script that regenerates both documents from the section files,
counts the word totals rather than carrying them, generates the supplementary
index once for both documents, and checks for citation gaps and phantoms. A
drift of that kind cannot live silently in it.

---

## 2. The finding that changed the most, and only one of you saw it

Section 6.1 sizes hover at **thrust equal to weight**. With the figure of merit
of 0.599 and the single 1.20 m disc, 490.5 N needs 10 895 W. So the 10.9 kW of
Section 6.2 *is* T/W = 1.00, exactly.

But Supplementary S2's buffer table wrote "T/W 1.20" against that same 10.9 kW —
the whole column was a factor 1.2 high — and Section 7.4 used T/W = 1.2 to claim
0.2 g of climb, which is what the paper's headline result rests on: *entering
the rotation while still climbing removes the altitude penalty entirely.*

I did not close this with an assumption. The only other source of vertical
thrust on the aircraft is the tip pairs, and during the rotation they are busy
producing the rotation. On a bang-bang profile the upper pairs run at full
thrust and the lower at zero — which is the M = 2TL of Section 4.3 — and the
two upper pairs still push upward. That gives a trade:

| pitch authority retained | vertical from tips | T/W |
|---|---:|---:|
| 100 % (23.0 N·m) | 32.4 N | **1.066** |
| 50 % | 48.6 N | 1.099 |
| 0 % | 64.8 N | **1.132** |

1.200 is not reachable at any setting.

**The headline survives.** Re-running the transition at every achievable ratio,
the altitude loss at both reference rotation times — 2 s light, 5.1 s heavy —
is still zero with a 5 m s⁻¹ entry climb, and stays zero down to T/W = 1.00.
What changed is the cost of *acquiring* that climb: 0.132 g, 3.9 s and 9.6 m,
against the 0.2 g, 2.6 s and 6.4 m previously claimed. And a rotation begun from
rest is markedly worse than reported — the light design loses 14.7 m at its own
two seconds rather than 9.1 m. The climb entry is now a requirement of the
configuration rather than a refinement of it.

One thing came out of this that the paper did not have: the tip propellers carry
the take-off thrust margin as well as the attitude moments. That is a second
duty for hardware already bought — but it is a dependency, because the margin
and the authority come from the same four propellers and cannot both be had in
full. Section 8.2 now records it as an open item.

---

## 3. The battery, and why it got worse

The 4.61 kW kg⁻¹ was (10.9 − 2.6)/1.8. But 10.9 kW is at the **rotor shaft**,
2.6 kW is at the **engine shaft**, and the buffer is on the **electrical bus**.
Three stations. Running the chain link by link:

| station | light design, hover |
|---|---:|
| nose propeller shaft | 10.90 kW |
| ÷ electric machine 0.92 | 11.85 kW |
| ÷ power electronics 0.95 | **12.47 kW demanded at the bus** |
| engine 2.60 kW × generator 0.90 | **2.34 kW supplied at the bus** |
| **buffer** | **10.13 kW → 5.63 kW kg⁻¹** |

Counting the tip pairs, which the aircraft needs to leave the ground at all,
**6.48 kW kg⁻¹**. Against the flown pack of [47] that is a factor of **3.8 on
its measured thermal ceiling and 6.3 on its measured continuous rate**. The most
exposed number in the paper is more exposed than it was.

---

## 4. A source request answered — from a source we already had

One of you said the assumed fin lift-curve slope of 4 rad⁻¹ is the wrong part of
the curve at Re ≈ 10⁵, and pointed at Selig — but cited a volume we do not hold.
I found the statement in the volume we do hold, reference [36]:

> "past work on **symmetrical** airfoils has shown that a **deadband often
> appears in the lift curve near zero degrees**. This nonlinearity can lead to
> undesirable longitudinal handling characteristics. Interestingly, cambered
> airfoils do not appear to have a similar, intrinsic deadband region."

and, of a section where one was not expected, a deadband present at Re of 60 000
and 100 000 and absent higher, "usually only seen on symmetrical airfoils at low
Re's".

Our fairing is a **symmetric section at Re ≈ 80 000, toed one to two degrees**.
That is inside the band. So 4 rad⁻¹ is an upper bound and not a conservative
choice — what the measurements remove is the *linearity* of the curve, not
merely the size of its slope, and a stability margin taken from a linear
derivative through zero is taken from the one part of the curve the data say is
not there.

The same source names the remedy and it costs us nothing structurally: camber
the fairing outboard, keep the toe-out. The paper does not size that fairing,
because choosing a slope from a curve we have not measured is the error we just
finished recording. **Source request 1 is closed, and it closed against us.**

---

## 5. Where I checked your claim and it did not hold

I am reporting these because a review that is never wrong was never a review.

| claim | what the file says |
|---|---|
| "The fixed-fuel-mass column is numerically wrong: −50.2 %, not −36.5 %" | **The paper is right.** Resizing properly under that contract gives −36.6 % and +0.3 %; the paper says −36.5 and +0.2. The claim held MTOW fixed at the fixed-fuel-*fraction* values while changing the fuel rule. That is not a contract — the aircraft re-closes, and B goes from 86.0 to 67.5 kg. |
| "The coaxial pair should use 2A; the figure of merit is 0.495, not 0.702" | The standard treatment of a coaxial pair is **one disc area plus an interference penalty**, not two discs — the lower rotor works in the upper's wake. The paper does exactly that. |
| "The endurance arithmetic does not close" | It closes. D = 490.5/12 = 40.875 N → 1 226 W of thrust power → /0.80 propeller → /0.92 machine = 1 666 W. 103.2 kWh × 0.28 × 0.90 × 0.95 = 24.71 kWh ÷ 1.666 kW = 14.83 h → 1 602 km. The objection used 1.7 kW, which is the rounded figure. |
| "The NASA numbers are wrong; they should be 4.9/3 735 and 9.3/7 517" | I opened the Johnson & Silva PDF. Quadrotor/turboshaft: L/D_e **4.9**, DGW **3 678 lb**. Lift+cruise/turbo-electric: **8.5**, **7 271 lb**. Our numbers are verbatim correct. **Only the citation number was wrong** ([7] → [22]). The claim was "three things are wrong at once"; one was. |

That last row is the one I would ask you to sit with. The instruction in the
previous round was *give me the sentence you are relying on, not just the
citation* — and it applies to a correction exactly as much as to a claim.

---

## 6. What none of you caught, which was the real defect in Section 3.7

You were right that the citation was wrong. But the logic was worse. The
sentence claimed that a configuration carrying a dedicated lift system should
show *lower cruise efficiency and* higher gross weight — and offered the
quadrotor (4.9 / 3 678) → lift+cruise (8.5 / 7 271) pair as showing "exactly
that ordering". It does not. The quadrotor has **no** dedicated lift system and
the *lower* efficiency; the lift+cruise has one and the *higher* efficiency.

The correct prediction is sharper, and the table does support it: the weight
charge is **not recovered** by the cruise efficiency the arrangement buys.
Seventy percent better in cruise, nearly twice as heavy. Sections 3.2 and 9 had
this right all along; only 3.7 misread its own source.

---

## 7. Everything else that was fixed

- S1's drag build-up table was missing its **10 % excrescence row**; the totals
  in the script were right, the printed table did not sum to them. Row added,
  substituted range put on one convention: **0.0201 – 0.0231**.
- S4's conservative rotation margin is **1.14, not 1.59** (17.6 / 15.4), and
  **0.76** on a smooth profile. "Still comfortable" is gone.
- Section 7.4 said control **power** scales as 1/t_r². Moment does; **power goes
  as 1/t_r³**, and Table 4 already did — its entries are constant to 0.3 % when
  multiplied by t_r³.
- S6 said "range does not contain propulsive efficiency". It does — the
  propeller is 0.80 of the 0.176 η_chain. The correction turns the tilting
  layout's fixed-fraction advantage from +12 % to about **−5 %**, i.e. against
  that architecture, not for it.
- Section 8.5 and S5.17 said no remaining analysis needs an experiment; the
  Conclusion said that was no longer true. Both now say which two need a tunnel.
- The Introduction's zero-bill sentence did not carry Section 5.3's
  qualification that the electrical path is still hover-sized.
- **S5 kept the old 8.1–8.17 numbering**, colliding with the shortened body's
  8.1–8.5; six cross-references in five supplementaries pointed nowhere. Now
  S5.1–S5.17, each reference checked individually against its context.
- Figures 7 and 8 had lost their callouts in the shortening. Restored.
- "measured uncertainty budget" → "quantified sensitivity budget"; "exactly
  three of them" → three recurring charges, with the statement that control
  authority, thermal management, transition hardware, reliability and
  certification are real costs and none of them is one of these three; the
  escape condition given in **four** parts, the fourth being the buffer; the
  vortex-lattice cancellation argument made explicitly conditional on the moment
  scaling with the lift, which the source does not let us check; aspect ratio
  6.00 → 6.03; [47] dated 2026; the funding declaration filled in.

**No shortening was done.** The body is about 19 700 words. Cutting a document
while it still contained the errors above would have hidden them rather than
removed them, and the length question is deliberately deferred.

---

## 8. What I am asking for

**First: read the current version and tell me where it is wrong.** Not weak —
wrong. Same standard as before: give me the sentence you are relying on, not
just the citation, and if you are correcting a number, show the arithmetic so I
can reproduce it. If you are not sure, say so; that is a better answer than a
confident one I have to spend an hour refuting.

**Second, and this is the new question: is there a calculation you would have us
run?** Not a measurement — we have no tunnel and we say so. A calculation, with
the tools a small team has: a vortex-lattice or panel solution, a RANS case, a
strip method, a sizing loop, a point-mass or six-degree-of-freedom simulation, a
sensitivity sweep, a Monte-Carlo over the mass budget. Something that would
either close an open item or show that a standing result is wrong.

Be specific about three things: **what** to compute, **what the answer would
decide**, and **what result would count against us**. A calculation whose every
possible outcome supports the paper is not worth running.

Two things I already know need a tunnel and am not asking you to route around:
the transition pitching moment above roughly ten degrees of incidence, where
three methods of three fidelities disagree with measurement; and the side force
on the faired tip frame at Re ≈ 80 000, for the reason in §4 above.

**Third:** if you still think the paper is the wrong length or the wrong shape
for the journal, say so — but say it after the two questions above, not instead
of them, and say it against the rules below rather than against a guess.

---

## 9. The journal's rules, now read rather than assumed

Last round produced two confident and **mutually contradictory** claims about
*Drones* — one that IMRaD is mandatory, one that there is no length limit. The
authors have since pulled the Instructions for Authors. Both claims were half
right, and the half that matters was missed by three of you. Advise within
this, not around it.

**Structure is mandatory, and we do not have it.** Even under the journal's
"Free Format Submission" allowance, which waives layout but not content:

> "all manuscripts must contain the required sections: Author Information,
> Abstract, Keywords, **Introduction, Materials & Methods, Results,
> Conclusions**, Figures and Tables with Captions, Funding Information, Author
> Contributions, Conflict of Interest and other Ethics Statements."

Our nine sections are Introduction / Background / Architectural tax /
Configuration / Bills audited / Reference designs / Transition / Limitations /
Conclusion. That is not IMRaD. **This is a restructure, not a rewrite** — the
content maps onto Methods and Results without deletion — but it is real work
and it has to happen before submission.

**Highlights are obligatory and we have none.** The required shape is exact:

> "What are the main findings?" — up to 2 bullets
> "What are the implications of the main findings?" — up to 2 bullets

**The abstract cap is confirmed at "about 200 words maximum".** Ours is ~270.

**There is no maximum manuscript length anywhere in the Instructions.** So
19 700 words is not a formal problem. Whether it is a *rhetorical* problem is a
fair question — but argue it as a reader, not as a rule.

**Two mandatory back-matter items are missing**: Author Contributions in CRediT
form, and a GenAI disclosure placed in **Materials and Methods** — the journal
requires that where GenAI assisted "study design or data collection, analysis or
interpretation", not merely language editing, and this work used it for
literature searching and numerical checking. There is also a prescribed
acknowledgement wording. A Patents section is permitted and we have a patent to
declare.

**One thing to check that nobody has raised.** The journal requires authors of
work "related to military purposes or applications" to determine whether the
research involves dual-use items, and supplies a DURC statement template. This
is a civil configuration study and claims no military application — but the
heavy reference design is a 1000 kg unmanned aircraft with a computed range near
1800 km, which is inside the band where export-control regimes list unmanned
vehicles by range. If you know this territory, say what a *Drones* editor would
expect here. If you do not, say that instead of improvising.

**What I am not asking you to re-litigate:** whether the abstract should quote
the 42 % / 17 % sizing result. It now does so with the mass-budget condition in
the same sentence, and that is the authors' call.
