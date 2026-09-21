# Round 50 — twenty-two seam repairs, one arithmetic correction that is mine to hand back, and a standing question about relay

> **READ THIS FIRST.** Everything this round asks about is reproduced here. **You are not being
> asked to read a manuscript.** v8 is written as separate step files in `paper/v8/`;
> `paper-v6.md` and `paper-v7.md` are frozen historical records. **If your knowledge base holds a
> file whose name contains `makale-v` or `paper-v`, it is not what this round is about.**

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`d414b71`**.
`paper/v8/ALL-STEPS-1-9.md` SHA-256 `e44104e1b5144c37fc87ae81a2ecfff3fcc03fa9230ff4d73d0746490fd75995`.

**Last round was the *whole*. This round is back to the *parts*.** You have the full text of
steps 1–9 from Round 49; below are only the passages that changed, before and after. Nothing
else in the nine steps has moved.

---

## 0. The author's question about relay, and what auditing it found

The author asked something this round that is worth putting to you directly, because it concerns
how these rounds work rather than the paper:

> *"Something is bothering me — the 109-instead-of-99 business, twice in a row? Don't you share
> your findings in the next round? Repeating the same mistake may not be their fault."*

**I checked. It was once, not twice — but the concern is correct in principle and I am acting on
it, and the audit turned up a worse case of the same kind.**

**The 109/99 item.** Two of you wrote that step 4's weight arithmetic gives 716 − 146 = 570
against a stated 679, leaving 109 lb unexplained. **Both of you left out the battery row.** From
NASA Table 3, first-hand:

| | Lift+Cruise TE | Tiltwing TE | difference |
|---|---:|---:|---:|
| Structure | 2 670 | 1 954 | **+716** |
| Propulsion | 1 772 | 1 918 | **−146** |
| Battery | 254 | 244 | **+10** |
| **sum of reported categories** | | | **580** |
| Empty weight | 5 809 | 5 130 | **679** |

**The unexplained remainder is 99 lb, not 109**, and it lies in empty-weight categories the
published table does not break out. **This correction is being handed back to you in the round
immediately after it was made**, which is the point of the author's question: a finding I keep to
myself is a finding you will repeat, and that would be my fault rather than yours.

**The worse case the audit found is mine and is four rounds old.** In Round 45 ChatGPT was right
that *"four VTOL architectures"* is false — the source says five types. **I relayed that to you,
and I corrected it in step 1** (Round 45's briefing carries the corrected sentence). **I never
swept step 2, which already existed** — it was written the day before that briefing. It sat there
for four rounds until ChatGPT and Grok found it again in the whole reading. That is the same propagation failure as the span-efficiency
numbers below, and it is now the fourth instance of the class.

**Both lessons are written into the project's rules**, and I state them here because they change
what you can expect of me:

> A script correction does not correct the prose that quotes its output — the number was copied by
> hand and stays there. **When a script changes, every passage quoting it is re-read in the same
> round.**
>
> And: **a caveat that lives only in the Turkish audit table does not exist in the English body.**
> Grok found the stale wattage in step 8 and noted the label was gone; the label was in the
> Turkish table, and the bundle I sent you strips those. Any qualification meant for a reader now
> goes in the body.

---

## 1. The finding three of you made independently — and it was mine

Step 6 said, on one page:

> *"The span efficiency used throughout this section is the computed value, 0.817"*

and

> *"L/D_max … **11.88** against 10.82, and **10.28** against 8.80"*

**11.88 and 10.28 are the e = 0.85 values.** ChatGPT, DeepSeek and Qwen each computed 11.65 and
10.08 and each was right. **I had computed those same two numbers myself the round before**, in
`aero/effective_ld.py`, and then copied the wrong column into the prose. The script was corrected;
the prose was not.

**Now:**

> *"…exceeds the cruise ratio at both ends of the drag bracket — **11.65 against 10.82, and 10.08
> against 8.80, both at e = 0.817.**"*

The conclusion is unchanged: the reference is given its best-range speed, this configuration is
not given its best lift-to-drag point, and the margin is positive anyway.

---

## 2. Grok's two findings in step 8

### 2.1 The stale energy-path numbers — removed, not relabelled

**Before:** *"For the light design the continuous cruise requirement is 1.9 kW at the engine shaft
and the engine is rated at 2.6 kW, while the hover requirement is 10.9 kW at the rotor. The
difference is supplied for the vertical phase from a **1.8 kg battery buffer, 3.6 % of take-off
mass.**"*

**After:** *"**The separation the architecture depends on is that the continuous cruise
requirement is several times smaller than the hover peak, and that the difference is supplied from
a battery buffer for the vertical phase alone.** No wattage is quoted here. The figures published
for this configuration were closed on a propeller efficiency this work has since replaced with a
computed one, and the re-closed set belongs to Section 10 rather than to an inventory. **Quoting
the superseded numbers beside a propulsion section that no longer assumes them is precisely the
inconsistency this paper is trying not to commit.**"*

ChatGPT preferred removal over labelling; Grok offered either. Removal was taken.

### 2.2 The retired sentence had come back

**Before:** *"Five propellers, and every one of them is a coaxial counter-rotating pair."*
**After:** *"**Five propeller stations, ten rotors:** every station is a coaxial counter-rotating
pair."*

---

## 3. The rest of step 8

**"No variable mechanism of any kind" fought the commanded shaft speed two paragraphs later.**

**After:** *"…no collective, no variable-pitch hub and no mechanism that changes a rotor's
orientation relative to the airframe. **Shaft speed is commanded; blade geometry and orientation
are not.**"*

**The concentric-shaft claim had reverted to the wide form.**

**After:** *"…so **the splitting gearbox and the mechanical governors that synchronise it are not
required** — the arrangement that repeatedly defeated the XB-35. **This work makes no claim about
the shafting**: whether the two machines are stacked on the axis or arranged some other way is an
implementation question it does not settle."*

**The trim question was pointed at Section 10, which is the mass loop.** Grok is right that
Section 10 cannot be obliged to answer it.

**After:** *"…are **not settled in this paper**: the moment is a sizing input to Section 10, but
the trim through the rotation depends on the transition aerodynamics, and **Section 14** says why
those are not currently reliable … at the incidences the rotation passes through."*

**DeepSeek's row reference was right and is fixed.** Step 8 said the tip pairs fail "the second
row of Section 3's table"; that row concerns a propulsor that lifts and is then carried, and the
tip pairs do not lift.

**After:** *"…the **fourth** failure mode — meeting the condition where the aircraft is carried and
failing it elsewhere — and the charge it re-opens is the second … *(They are not the second row of
Section 3's table: that row concerns a propulsor that lifts and is then carried, and the tip pairs
do not lift.)*"*

**And the tip frames do four jobs, not three** (DeepSeek): landing gear, moment arms, attitude
rotors, **and — through the fairing — the aircraft's only vertical surface.**

---

## 4. Step 4 — the weight passage rewritten

**Two things were wrong.** ChatGPT: *"the only architectural difference between them"* is too
strong, and *"the dedicated lift group costs 687 lb"* over-attributes a net difference to one
hardware group.

**After, in part:** *"**They are not identical in every other respect** — one stops its lift rotors
in the airstream and drives a separate pusher, the other reorients its proprotors on a tilting
wing — **but the difference the comparison turns on is that one carries a dedicated lift group
through cruise and the other does not.** The comparison is the closest the published set comes to
isolating that charge; **it is not a controlled experiment.**"*

*"…the design gross weights differ by 687 lb in the tilt-wing's favour. **That figure is the net
difference between two architectures, not the measured mass of a lift group.**"*

*"**Of the empty-weight difference of 679 lb**, structure accounts for 716 lb in the
lift-plus-cruise entry's disfavour, propulsion returns 146 lb … and battery returns a further 10
lb. **Those three categories account for 580 lb of the 679**; the remaining **99 lb** lies in
empty-weight categories the published table does not break out, **and this work does not know how
it is distributed.**"*

---

## 5. Step 2 — the NASA headcount, the tilting row, and falsifiability

**"Four VTOL architectures" → "five VTOL architecture families."** Four rounds late, as in §0.

**DeepSeek's "zero-bill" finding: the premise was wrong, the ambiguity was real.**

Tilting does not pay zero of the three. It attacks Bill 1 and **does not attack Bill 3** — with no
store, the power plant is still sized by the hover peak. The NASA tiltwing confirms it: a battery
*"just to enable emergency landing after loss of turboshaft power."* **But the row's old wording,
"not one of the three," could be read as "net zero," and that reading makes the condition's name
look wrong.**

**After:** *"| Tilt-rotor, tilt-wing, tilt-nacelle | 1 — one propulsion group serves both regimes |
**Bill 3 is left standing** — with no store, the power plant is still sized by the hover peak —
together with mechanical complexity, gyroscopic coupling and a transition control problem, which
are **not among the three** |"*

The dangling *"see below"* is gone with it.

**ChatGPT's falsifiability objection follows from the same row, and is fixed.**

**After:** *"**The accounting is refuted by any remedy that reduces one charge while leaving the
others no worse and adding no cost of its own.** … **Two clarifications keep that test from being
either too easy or unfalsifiable.** A remedy that attacks one charge and simply leaves another
standing is not a counter-example — the tilting row is the case… And a remedy whose cost falls
**outside** the three charges is not a counter-example either, but the accounting only earns that
if it names such costs rather than ignoring them… **A framework that could absorb any cost by
declaring it out-of-scope would be unfalsifiable**, so the costs outside the three are listed, not
waved away."*

---

## 6. Steps 1, 3, 7 and 9

**Step 1 — the "three of the four objections" sentence is deleted.** ChatGPT is right that the
four were authorially constructed from a source reporting a longer list. **After:** *"…**But it is
not what curtailed the testing.** The reviews record a longer list of handling and control
difficulties than this section reproduces, and no attempt is made here to sort them into those
that would and would not recur — what the record settles is the cause of the curtailment, and that
cause was mechanical."*

**Step 1 — the "unoccupied corner" contradiction.** **After:** *"**The corner where both
capabilities are wanted at once is where the two applications this work is aimed at sit** … **That
corner is not empty**, as the rest of this section sets out; what is unsettled is which price an
architecture in it must pay."*

**Step 1 — the roll sentence now foreshadows step 7** (DeepSeek): *"…produces no rolling moment
**by any combination of thrust settings** … **The reaction-torque channel that other coaxial
tail-sitters use about that same axis is a separate matter, and it is a choice this configuration
declines rather than a limit it inherits.**"*

**Step 3 — "cruise thrust" is now defined** (DeepSeek): *"***Cruise thrust in this paper means the
thrust that balances cruise drag.*** Attitude devices produce thrust in cruise, but they produce no
cruise thrust in that sense … **They remain in the airstream, so the second charge reaches them**,
and an architecture that carries them is a partial instantiation rather than a full one."*

**Step 7 — "What is new" is retired** (ChatGPT). **After:** *"**What this paper contributes is that
combination, the condition it is built to satisfy, and the price it pays for satisfying it.** …
The assembly is not offered as novel because it is an assembly … **and Section 1 has already set
out how much of the ground is occupied.**"*

**Step 7 — the elevon/rudder row is out of the mechanism table** (ChatGPT), and the table now says
what it counts: *"**The table below counts mechanism classes that exist in order to change
regime**, which is why no aerodynamic control device appears in it: the strip of Section 8 is a
control surface, not a means of changing regime, and counting its absence would be counting the
wrong thing."*

**Step 7 — the transition limit is now stated in step 7 itself** (DeepSeek, Grok): *"**One thing
this section does not establish, and Section 9 holds it to that.** … **Whether this aircraft can
actually perform the change is a separate question and is not settled anywhere in this paper** …
**The mechanism claim is about hardware and survives that limit. The transition claim is not
made.**"*

**Step 7 — "same job" → "both duties"** (Grok), matching step 3's explicit refusal of "job".

**Step 9 — "Cruise efficiency and range | Multirotors" → "Cruise efficiency | Multirotors"**
(ChatGPT). Step 6 gives no range number against a multirotor, and the table should not imply one.

---

## 7. Not taken, and why

- **Qwen: "no other cross-step contradictions found; the claims are consistent."** Not taken.
  Fifteen more were found by the other three, and several are in sections Qwen said it had checked
  against every other section. **The one number Qwen did find was correct and it mattered** — but a
  clean bill after that scan was not warranted by the scan.
- **DeepSeek: cut step 1's 1954 narrative to two sentences.** A proportion judgement rather than a
  defect. **Deferred by the author**, in his words: *"Shortening is the last thing we do, not
  now."* It is recorded in `paper/deferred-decisions.md` with the rest of the shortening pass, to
  be done once steps 10–14 exist.
- **Renaming the "zero-bill condition."** With the tilting row fixed the name is defensible, but
  the tension Grok and DeepSeek both noted is real. **Deferred by the author**, same record.

---

## 8. What I am asking, and what happens next

**The author's instruction is explicit: if you have no objection to these repairs, we go to
Step 10.**

So the question is narrow:

1. **Does any repair above create a new contradiction?** That is the failure mode this project has
   hit four times, and every instance was a correction that did not propagate. Three of the
   repairs touch text you have not seen in place — step 2's tilting row, step 3's cruise-thrust
   definition, and step 7's transition paragraph. **Those are the ones to check hardest.**
2. **Is anything on the not-taken list wrongly not taken?**
3. **Step 10 will close the sizing loop on the consistent bracket 0.0285–0.0381, carrying the four
   corners of the L/De matrix as four inputs to `baseline.py`, which takes lift-to-drag as an
   input.** Four closures, four masses, four ranges; the envelope survives because the loop never
   needs four geometries inside it. **That is Grok's mechanism and the author has accepted it.**
   If it is wrong, say so now rather than after the loop is written.

**No source is needed for any of this.** The boundary stands: PDFs only for priority claims,
numbers taken from tables, and verbatim quotations.
