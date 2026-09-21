# Round 48 — a file-delivery failure we have not fixed, and step 6 rewritten under your criticism

**The author has asked for another round on step 6 before step 10.** His reason, in his own
words: *"We went fast through the sections that were generally accepted, but look — here a
'good thing we asked' situation arose. I don't want to move to the next stage while there is an
error or a problem. One more round costs nobody anything."*

---

## 0. Verify what you are reading

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`99282b2`**
(this briefing lands one commit later).

```
paper/v8/06-the-second-half.md      SHA-256 818c19517efd798cbb9fcc12fc4e041f58e97a3bd080f395e38de297fed3fd6a
paper/v8/05-the-first-half.md       SHA-256 a20ced694cba23fade532021d0fe10d1f642cd9c387206c602f2a98898ac72f3
paper/v8/04-the-independent-check.md SHA-256 023562cbb28f5afd1e546f404826322f248271d4ced22d3dfab95f124d1a500b
paper/effective-ld-finding.md       SHA-256 4c82072d8ac6ac522aa26d0a67192cf0f7f0d521bd4cbbfa190363509d9946cf
paper/roll-axis-finding.md          SHA-256 6514853e26b6a62c25a338c4d6970666c99ef2055160a944070e587be14939a2
aero/effective_ld.py                SHA-256 5323b44da3b4c754330ae0fe58cf4b445a6dec8059cc36444144585c0dc15e0f
aero/reaction_torque.py             SHA-256 cdeef249f94f0f853da831dc54e4469956514e684eda9b38b7919b2e6990ef51
```

> **You do not need to open any of these.** Everything this round asks about is reproduced in
> full below. The hashes are there so you can check a file if you have one, not so you have to
> find one.

---

## 1. A delivery failure. Ours first, then the inconsistency, then a request.

**Qwen declined to review last round, on the grounds that it held a stale file.** Declining to
review a file you cannot verify is the behaviour this project asked for, and it has been right
before. **This time the stop was caused by looking at the wrong artifact, and the root cause is
something we have never told you.**

### 1.1 The facts, all checkable

Qwen reported holding `makale-v6-535401f.md`, and ran three checks against it: `0.0216` absent,
`Three architectural claims are made and a fourth is` present, twenty-two table captions.

- **That check list is from Round 24.** The file is the build pinned in **Round 25**.
- **That path has not existed in this repository since 2026-09-16**, when the whole repository
  was renamed from Turkish to English and `makale/` became `paper/`. The snapshot itself was
  last written on 2026-09-14.
- **The filename already said so.** Round 25 introduced the commit-stamped filename for exactly
  this purpose, in these words: *"A stale copy is now visible from its filename alone."* The
  briefing pinned `ab39ba5`; the file says `535401f`. **The mismatch was visible without opening
  it.**
- **Round 47 pinned nine files by SHA-256 and not one of them was a manuscript.** Five were
  `paper/v8/` step files; the rest were finding records and scripts.

### 1.2 The inconsistency, stated plainly

**Qwen concluded "stale" from the absence, in the v6 manuscript's §4.2, of the effective-L/D
conversion — but nothing in Round 47 claimed §4.2 had changed.** The conversion lives in
`paper/v8/06-the-second-half.md`, a file Qwen was not given and which none of its three checks
looked for. **A file is not stale for lacking edits that were never claimed for it.** The checks
were valid in Round 24. Re-run in Round 47, they tested a claim nobody made.

**Then, having said it would stop rather than review, Qwen reviewed both substantive items — the
`L/De = (L/D)·η_p` identity and the roll correction — and was right about both.** So the material
was sufficient. The stop was not caused by missing content.

**And this was already known.** In Round 43 Qwen wrote: *"the knowledge base holds the
pre-restructure `makale-v6.md`, not the step files."* That is the same diagnosis, eight rounds
earlier, and it is correct. What did not follow from it was the conclusion: **if your knowledge
base holds a manuscript, and this project no longer works by editing a manuscript, then a
manuscript check can never confirm a current build — not this round and not any round.**

### 1.3 Our share, and it is the larger one

**We have never told you how this project is laid out.** Here it is:

> **v8 is not being written by editing the manuscript.** It is being written as **separate step
> files**, one per skeleton step, in `paper/v8/`. `paper-v7.md` is a frozen record we quote from
> as a source. `paper-v6.md` is two versions behind that and is not being worked on at all.
> **Nothing we report as "changed this round" will ever appear in a manuscript file.**

Anyone looking for our changes in a manuscript will always find them missing, will always
conclude staleness, and will always be wrong. **That is our failure to state, not your failure
to read.**

One more admission. **The first version of Round 47 linked step 6 rather than reproducing it.**
It was corrected within minutes and the corrected version inlines the full text, but both
versions briefly existed. If the linked version reached you, a request for the text was
legitimate — for step 6, though not for a v6 manuscript.

### 1.4 What we are doing about it, and what we are asking you

Our fix, from this round onward:

1. **Every briefing reproduces, in full, every text it asks about.** No attachment is ever
   required. No fetch is ever required.
2. **A standing negative instruction:** *you are not being asked to read a manuscript.* If you
   are holding a file whose name contains `v6` or `v7`, it is a historical record and it is not
   what this round is about.
3. **The layout statement above appears in every briefing**, so the structure is never assumed.
4. Hashes stay, but demoted — **for checking a file you happen to have, not for finding one.**

**What we are asking of each of you, and this is a genuine request rather than a courtesy:**

- **Is that enough?** A file-version problem has hit this project repeatedly — Qwen in Rounds 23,
  43 and 47; ChatGPT in Round 40, unable to reach GitHub; Grok answering without refetching.
  Reproducing everything inline is the obvious fix, but it makes each briefing longer every
  round, and at some point length becomes its own failure mode.
- **For those of you with a persistent knowledge base:** is there anything we can put in a
  briefing that would cause a stale stored file to be *ignored* rather than consulted? A
  filename convention? An explicit "do not read X" list? We do not know what works from your
  side and we are guessing.
- **For those of you with no fetch tool at all:** what is the most useful form for us to send?
  One long message? Text split by section? Something else?
- **And the harder question:** is there a check you can run *on the briefing itself* that tells
  you whether it is internally complete — rather than a check on an external file that may or
  may not be the right one?

**No source is needed for any of this.** It is process, and §2.1's boundary applies: PDFs are
requested only for priority claims, numbers and verbatim quotations.

---

## 2. What changed in step 6 after your last round

**Five changes accepted, one qualification rejected, two source checks run.**

### 2.1 ChatGPT was right about the η_p interval, and the fix opened something better

The section described 0.632–0.683 as *"a two-point blade-element solution of the actual nose
blade at its actual hover and cruise conditions."* **That is not what the interval is.** The
crossing search output:

| blades per rotor | target section c_l | η_p |
|---|---|---:|
| 2 | 0.55 | 0.648 |
| 2 | 0.70 | **0.683** |
| 3 | 0.55 | **0.632** |
| 3 | 0.70 | 0.643 |

The interval is the spread across **four blade families**, each of which meets the paper's hover
figure of merit. "Two-point" describes how each blade is solved — at hover and at cruise — not
where the interval comes from. The sentence conflated the two.

**And correcting it answered the bracket question all three of you raised.** The two spreads are
not the same kind of thing:

> The **zero-lift drag bracket is uncertainty** — a designer does not choose where the real
> aircraft lands in it. The **blade family is an unfixed design choice** — a designer building
> the aircraft takes the best of them. Presenting them together as one "adverse corner" dresses
> a blade nobody would choose as though it were uncertainty.

The section now gives the product matrix and names both kinds:

| L/De | η_p 0.632 | η_p 0.683 |
|---|---:|---:|
| **L/D 8.80** (adverse drag) | **5.56** | 6.01 |
| **L/D 10.82** (favourable drag) | 6.84 | **7.39** |

ChatGPT asked for "conservative interval enclosure" rather than "corners". The section now says
the two extremes are bounding corners of the product, each reachable, with the low one pairing
the worst drag outcome with the blade a designer would not choose.

### 2.2 Grok's objection about the electric row — a real question, and the answer runs our way

> *"For the turboshaft quadrotor the shaft reading is the natural one. For the all-electric 5.8
> it is the dangerous one: if that 5.8 is WV/P_battery, our 5.56–7.39 is not in the same
> currency."*

**The question is legitimate and the source settles it — in the direction opposite to the
worry.** The separation is made inside the **battery-capacity** derivation:

> `Ecap = Ecruise + Ehover + Ereserve`  (1)
>
> `Ecruise = (Pc/ηc) × time = WR/((L/De) ηc)`  (2)

**For electric aircraft, L/De is explicitly upstream of ηc.** Had L/De contained the electrical
chain, that derivation would count the chain twice in the source's own battery sizing. **The
all-electric row is where the proof is strongest, not weakest.** The proof is now inside the
section rather than only in the working notes.

### 2.3 DeepSeek's fourth qualification — rejected, and here is why

> *"The multirotor's propulsion losses are smaller than this configuration's, because it has no
> dual-duty compromise."*

**The source says the opposite.** §6.3, *Trim of multi-rotor aircraft*:

> *"For the quadrotor, **both collective and rotor speed control were considered.** … Edgewise
> rotor flight has reduced induced power … followed by power increasing with speed as the
> parasite power increases. … With rotor speed control and fixed collective, the rotor rpm
> follows the power variation with speed, while the rotor C_T/σ increases with speed initially
> and then decreases. **The increase in C_T/σ might be limited by maximum blade loading, perhaps
> requiring a smaller design C_T/σ at hover (hence larger blade area).**"*

That last sentence is a description of a two-regime compromise. The quadrotor's rotors hover
**and** cruise. The qualification was not taken.

### 2.4 ChatGPT's fourth qualification — taken, and verified

Analysis-chain mismatch. Confirmed in the source: sizing by **NDARC**, rotor performance by
**CAMRAD II / CHARM**. Against that, this work uses a drag build-up, a drag polar at a prescribed
cruise condition, and a separate blade-element solution. The section now says the comparison is
**two independently produced figures in a common definition, not a controlled numerical
reproduction**, and that nothing in it validates either.

### 2.5 The rest

- **Both quadrotors are now presented as co-equal.** "Primary comparison because it shares our
  energy source" is gone — ChatGPT, Grok and DeepSeek all objected, and Grok's phrasing was the
  sharpest: *"it will look like evasion because the electric row is the one you miss."*
- **The adverse-corner admission moved earlier and is presented as a result**, not a caveat
  (DeepSeek).
- **"What the configuration does instead" was expanded** to mirror step 5's balance (DeepSeek's
  Q4), and now states the physical separation — a surface holds the aircraft up, a propeller
  pushes it along — before any number appears.
- **Step 4's handoff to step 5 was sharpened** (DeepSeek): the instrument is declared fixed and
  not modified again.

### 2.6 One thing found at the edge, and deliberately kept out of step 6

The tiltwing in the same table (L/De 8.6) **uses collective control and drops its tip speed from
550 ft/s in hover to 300 ft/s in cruise** — precisely the two adjustments this architecture
refuses. That is a direct measure of what refusing the variable-pitch hub costs. **It is on the
axis where this paper claims nothing against tilts**, so it belongs to the ledger and the
contracts sections, not here. Recorded, not used.

*(That sentence describes the **tiltwing**, §5.5. It is not the quadrotor. I came close to
attributing it to the quadrotor and caught it.)*

---

## 3. Step 6 in full, as revised

### The second half: cruise carried on a wing

### The opponent, and the axis

On this axis the alternative is the multirotor, and as in the previous section the comparison
runs one way only. **Nothing here is claimed against fixed-wing aircraft.** A runway-launched
aeroplane cruises more efficiently than this configuration and pays none of the charges of
Section 2; that comparison is not made, and no result in this paper rests on it. The claim is
confined to the one thing the multirotor family structurally lacks: **a surface that carries the
cruise lift.**

### What the requirement is

Section 5 established the first half: the aircraft must leave from and return to a site that
supplies nothing. **A multirotor meets that requirement completely.** It is not a deficient
machine and this section does not treat it as one; it is excellent at what it does and is
limited by the price of doing it that way.

What it does not meet is the second half of both missions. Wildfire observation and response,
and cargo delivery to places without a runway, each require the aircraft to **cover distance
after it has left the unprepared site**, and a vehicle with no wing buys every second of that
distance with installed power. The consequence has been stated independently: surveying the
field, one study concludes that multirotors are efficient in hover and suited to short-range
missions, while vectored-thrust aircraft are efficient in cruise and suited to long-range ones.

### What the configuration does instead

**Cruise lift is carried by the airframe itself.** There is no separate fuselage: the whole
planform is the wing, so every part of the body that is carried is also a part that lifts. At
the cruise condition the lift coefficient follows from `C_L = W/(qS)`, the drag from
`C_D = C_D0 + C_L²/(πARe)`, and the nose pair is left with one job — producing the thrust that
balances that drag. It supports none of the weight.

That is the whole of the difference, and it is worth stating in those plain terms because the
consequence is structural. **A rotorcraft's discs must produce the lift and the propulsive force
together, for every second of the flight.** This aircraft separates them: a surface holds the
aircraft up and a propeller pushes it along, and the surface costs no power to do its part.
Lift is carried on a surface or it is carried on rotors, and no sizing contract, no assumption
in this paper and no choice available to a designer moves a vehicle between those two states.

**But the size of the resulting advantage is a calculation, not a consequence of that
statement**, and the two must not be run together. The rest of this section is the calculation,
and it gives a smaller number than the structural statement invites.

### What the margin actually is, in one currency

The sizing set of Section 4 reports an **effective lift-to-drag ratio**, defined in its own
nomenclature as `L/De = WV/P`: weight times speed over power. That is a system figure of merit,
not a force ratio, and it already contains the propulsive efficiency of whatever produces the
thrust. **A force ratio cannot be placed beside it.**

Converting this configuration's aerodynamic ratio into the same quantity is one line: in level
cruise thrust equals drag and lift equals weight, so with shaft power `P = DV/η_p`,

> **L/De = WV/P = (L/D) · η_p**

**Which power `P` denotes is not assumed here**, because reading it as electrical power rather
than shaft power would make this configuration's figure incomparable with the published one. The
source settles it in its hover formulation: hover power is written `Ph = W√(W/2ρA)/FM`, with the
figure of merit already applied — shaft power — and the propulsion-system efficiency applied
separately outside it. The cruise formulation uses the same separation, writing cruise energy as
`Pc/ηc` with `Pc = WV/(L/De)`. That separation appears in the source's **battery-capacity**
derivation, so it holds for the all-electric entries as well as the shaft-driven ones: if `L/De`
already contained the electrical chain, that derivation would count it twice.

**Neither factor is a single number, and they are two different kinds of spread.**

The aerodynamic ratio is **8.80 to 10.82**, with the tip frames and the free-wheeling attitude
rotors already charged. That spread is **uncertainty**: it is the zero-lift drag bracket, and a
designer does not get to choose where in it the real aircraft lands.

The cruise propeller efficiency is **0.632 to 0.683** across the nose-blade families that meet
the hover figure of merit — two and three blades per rotor, at two target section lift
coefficients, each solved at its hover and its cruise condition. That spread is **not
uncertainty**: it is a design choice this study did not fix, and a designer building the aircraft
would take the best of them.

| L/De | η_p 0.632 | η_p 0.683 |
|---|---:|---:|
| **L/D 8.80** (adverse drag) | **5.56** | 6.01 |
| **L/D 10.82** (favourable drag) | 6.84 | **7.39** |

**5.56 and 7.39 are the bounding corners of that product, not two simulated operating points.**
Each is reachable — the drag bracket and the blade family are independent — but the low corner
pairs the worst drag outcome with the blade a designer would not choose.

### What the comparison gives, against both published quadrotors

The sizing set contains two quadrotors for the same mission, and **neither is treated here as the
primary one.**

| | L/De | Margin against 5.56 – 7.39 |
|---|---:|---|
| Quadrotor, turboshaft | 4.9 | **+14 % … +51 %** |
| Quadrotor, all-electric | 5.8 | **−4 % … +27 %** |

**Against the turboshaft quadrotor the sign holds at every corner.** Closing it would need the
propeller efficiency to fall to 0.557, against 0.632 for the least efficient blade family
examined.

**Against the all-electric quadrotor it does not hold at the low corner**, and that result is
reported as a result rather than as a caveat. That vehicle reaches 5.8 — above this
configuration's 5.56 — and it buys the difference with 1 742 lb of battery and nearly twice the
gross weight for the same mission, 7 221 lb against 3 678 lb. **The weight it pays for that
efficiency is the charge Section 2 describes and Section 4 tests**, so the entry illustrates the
framework rather than contradicting it. On cruise efficiency taken alone, it is nonetheless
ahead of this configuration's low corner.

**So the second claim is narrower than the structural statement invites.** Carrying cruise lift
on a wing is worth **14 to 51 percent against the turboshaft reference and does not uniformly
beat the all-electric one** — a measurable advantage, not a change of category. And what
compresses it is not the wing. **It is this aircraft's own refusal of the variable-pitch hub:**
at a propeller efficiency of 0.85 the same airframe reaches 7.48 to 9.20. Section 11 charges it
there.

### Four qualifications, all of which run against this configuration

They are given together because omitting any one of them would make the comparison look better
than it is.

**Scale.** The compared vehicles are 1 670 to 3 275 kg; the designs here are 50 kg and 1 000 kg.
Reynolds number favours the larger aircraft, so the smaller design is at a disadvantage in this
comparison rather than an advantage.

**The quadrotor is a good quadrotor.** Its disc loading is 3.5 lb ft⁻², which is unusually low
and unusually efficient. Nothing here is compared against a poor example.

**The speeds are not matched.** The published figure is quoted at the best-range speed; this
configuration's is at its chosen cruise condition, 1.49 times stall, which Section 10 states
explicitly is **not** its best lift-to-drag point. Cruising at the best point would leave too
little margin, and the ratio that the chosen condition gives is the one reported.

**The analysis chains are not matched, and this is the qualification that bounds what the
comparison can be called.** The published value is the output of an integrated conceptual-design
system with a comprehensive rotor analysis behind its rotor performance. The value here is
assembled from a drag build-up, a drag polar at a prescribed cruise condition, and a separate
blade-element propeller solution. **This is a comparison of two independently produced figures
in a common definition, not a controlled numerical reproduction**, and nothing in it should be
read as validation of either.

### What is sized, and what is not demonstrated

**Sized.** The drag build-up and its bracket; the lift-to-drag ratio at the cruise condition
from the drag polar; the propeller efficiency from blade-element momentum theory at two
operating points; and the range that follows from the chain, link by link.

**Not demonstrated.** **No part of this has been measured.** There is no wind-tunnel test and no
flight test in this work, and the drag coefficient is a build-up with a declared bracket rather
than a measurement. The planform's sweep, taper and thickness distributions were chosen rather
than optimised. The span efficiency of 0.85 is an assumption which the paper's own calculation
puts at 0.817 — optimistic by 3.9 percent. And **the aerodynamics above roughly ten degrees of
incidence are not reliable for anyone on this class of configuration**: three methods of three
fidelities depart at the same place, the highest of them against wind-tunnel measurement. That
limit does not touch the cruise numbers above, which sit at a few degrees, but it bounds what
this section may be read to support.

### What this half costs

The wing that makes cruise efficient is carried through the vertical phase, where it produces
nothing and presents the aircraft's largest surface to ground wind. The tailless planform that
follows from having no boom constrains the sweep, because with no horizontal stabiliser the
pitching moment must come from the distribution of lift along the body itself. And the
fixed-pitch propeller that serves both regimes is the reason the margin above is 14 to 51
percent rather than more. Section 11 charges all three.

**The two halves are now on the table separately. Section 7 is where they are combined**, and
the combination is what this paper is for.

---

## 4. What I am asking of you

**On the delivery problem (section 1):** the four questions in §1.4. Process only, no source
needed.

**Qwen specifically:** you were right to stop, and the substantive comments you did give were
correct. The request is narrower than a defence — **please check whether the diagnosis in §1.2
is fair**, and then tell us what would actually have prevented it from your side. You are the
reader who has hit this most often and therefore the one who knows most about it.

**On step 6 as it now reads:**

1. Does the uncertainty-versus-choice distinction hold? A designer takes the best blade family,
   so is quoting 5.56 at all over-conservative — or is it right to keep it because this study
   has not fixed the blade?
2. With both quadrotors now co-equal, does the section still read as claiming more than it has?
3. Four qualifications now, all against us. Is a **fifth** missing?
4. Is §2.2's battery-derivation argument airtight, or is there still a reading in which the
   all-electric 5.8 is not in our currency?

**And the author's question, which is the reason for this round:** is there anything still wrong
in steps 1 to 9 that would be cheaper to find now than after step 10 is written?

---

## 5. Where the work stands

**Written:** steps 1 through 9. **Not written:** 10 (analytical closure of the sizing loop),
11 (the ledger), 12 (the bills separate with scale), 13 (rankings belong to contracts), 14 (what
does not close).

**One contribution: the architecture** — a configuration that reaches the regime change with no
mechanism that reorients a propulsor. The three-bill framework is the instrument that makes that
claim checkable, not a second and equal contribution.

**Three claims, three families, three axes:** runway-independent vertical operation against
fixed-wing aircraft; wing-borne cruise against multirotors, at **+14 % to +51 % against the
turboshaft reference and −4 % to +27 % against the all-electric one**; and freedom from the
propulsor-reorientation mechanism class against tilting architectures, which is the contribution.

**Not claimed:** a range ranking against the other hybrids, which reverses with the sizing
contract and is reported as a case result.

**Nothing here has been measured.** No wind tunnel, no flight test. The pitching moment through
transition remains the largest open item; three methods of three fidelities fail at the same
incidence, so it belongs to measurement rather than computation.
