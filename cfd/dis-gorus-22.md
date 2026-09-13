# Round 18 — the fork in the road

**Read this document alone. You do not need the manuscript.** Everything you
need to answer is below: what the paper claims, what moved, who moved it, and
the decision we are stuck on. Previous rounds asked you to fetch a file first;
two of you could not, and one of you described a version that did not exist.
That failure mode is now removed by giving you the substance directly.

---

## 1. The paper, in four hundred words

**Thesis.** Hybrid VTOL aircraft pay for runway independence in cruise
efficiency. The paper treats that cost as *architectural* rather than as an
implementation defect, and develops it as an accounting framework. The penalty
is charged in three coupled currencies:

- **Bill 1** — hover hardware carried through cruise as dead mass.
- **Bill 2** — the drag of that hardware when it is exposed to the cruise flow.
- **Bill 3** — continuous installed power sized by a condition that holds for
  roughly two percent of the flight.

Every architectural remedy surveyed reduces one bill by raising another. The
escape condition has four parts: the *same hardware*, in the *same orientation*,
doing the *same job*, with the hover peak drawn from a *buffer* rather than from
installed power.

**The case study.** meryemAircraft: an uncrewed tail-sitting blended-wing body.
One coaxial nose pair serves both hover and cruise (same hardware, same
orientation, same job). Four small counter-rotating pairs at the wing tips
produce attitude moments. No elevons, no rudder, no tilt mechanism, no dedicated
lift system. A variable-extension strip on the lower surface supplies roll. An
internal-combustion engine drives a generator; a battery buffer on the electrical
bus supplies the hover excess. Sized at 50 kg and 1000 kg from one set of
equations.

**The comparison.** Three architectures — A the tail-sitter, B lift-plus-cruise,
C tilt-rotor — sized against the same mission under three sizing contracts:
fixed fuel fraction, fixed fuel mass, and fixed take-off mass with fixed payload.
**The ranking changes with the contract.** That contract-dependence is itself a
result, and the paper reports three contracts rather than one for that reason.

**What is not claimed.** The aircraft is not shown to be flyable. There is no
wind-tunnel data and no flight test. Transition controllability rests on a
pitching moment that three methods of three fidelities fail to predict above
about ten degrees of incidence — the best of them against wind-tunnel
measurement — so it is blocked on data, not on effort.

**Target.** *Drones* (MDPI). IMRaD, five sections, abstract capped near 200
words, Highlights obligatory.

---

## 2. Where the numbers stand right now

| Quantity | Value | Status |
|---|---|---|
| Light reference design | 54.5 kg, 13 kg payload, 1 131 km | rotors charged |
| Cruise L/D (A) | 8.49 | was 12.00 before rotor drag |
| Free-wheeling tip-rotor drag, ΔC_D0 | **0.0154** | computed, compressibility-checked |
| Assumed C_D0 | 0.0248 | **inside** the computed bracket 0.0216–0.0380 |
| Buffer specific power demanded | 5.63 kW/kg hover, 6.48 take-off | at the electrical bus |
| Highest measured on a flown pack | 1.5 kW/kg | factor 3.8 short |
| Mass advantage over lift-plus-cruise | 37 % | was 42 % |
| Range vs B, fixed fuel fraction | **B leads by 21.1 %** | ranking reversed |
| Range vs B, other two contracts | A leads by 5.4 % and 44.9 % | |
| Range vs C (tilt) | C leads under all three | |
| Neutral point | 0.858–0.867 m | 1.3 % MAC of solver scatter |
| Trim twist | −9.19° at 10.24° incidence | residual 10⁻⁶ |

---

## 3. What changed since you last commented, and who caused it

### 3.1 Qwen — a version that did not exist, third round running

You reported: *"the IMRaD restructure is not present; the file still contains
nine numbered sections and the second is Background: seventy years of attempts."*

The file had five sections, the second was *Materials and Methods*, and that
phrase appeared nowhere in it. The other three read the same file and saw five
sections.

**The seed was ours, and it is now deleted.** A dead sentence left over from the
IMRaD move was still sitting in the Introduction: *"The remainder of the paper is
organised as follows. Section 1 reviews seventy years of attempts…"* —
self-referential and false, since that *is* Section 1. It is plausible that this
was read and a section structure inferred around it.

**This round you confirmed the version markers correctly and your review was
substantive.** The access problem appears to be solved by giving you content
directly, which is why this document is written the way it is.

### 3.2 DeepSeek — the most valuable finding of the round

You wrote: *"The headline rotor drag is 0.0085, taken from the design with hover
figure of merit 0.27, but the aircraft's figure of merit is 0.599 everywhere
else. The paper understates its own cost by using a propeller it has already said
it cannot use."* You estimated the correct value at 0.013–0.024 by interpolation.

**Confirmed, and the computed answer is sharper than an interpolation.** My first
attempt was invalid: I bisected on figure of merit to hit 0.599 and the solver
returned 0.633 and 0.557 at essentially the same design point. Rather than trust
it, I tested the solver — every design built twice:

| design c_l | FoM run 1 | FoM run 2 | ΔC_D0 |
|---|---|---|---|
| 0.55 | 0.646 | 0.646 | 0.0238 |
| 0.60 | 0.645 | 0.645 | 0.0199 |
| 0.64 | 0.641 | 0.641 | 0.0174 |
| 0.68 | 0.633 | 0.633 | **0.0153** |
| 0.70 | 0.350 | 0.350 | 0.0126 |
| 0.85 | 0.270 | 0.270 | 0.0085 |

The solver is deterministic. What looked like noise is a **cliff**: figure of
merit is flat at 0.63–0.65 up to c_l 0.68, then collapses. **0.599 falls inside
the collapse**, so no blade in this family sits on it. Every design that *meets*
the hover requirement lies at c_l ≤ 0.68, and the least draggy of those gives
0.0153. It is a **constraint boundary**, not an interpolation.

### 3.3 The drag bound broke, and it was load-bearing

DeepSeek also wrote: *"the rotor drag is not integrated into the zero-lift-drag
bound, and it breaks the conservatism claim."*

There was no rotor row in the build-up at all.

| | lower | upper |
|---|---:|---:|
| as published | 0.0131 | 0.0210 |
| with rotors | 0.0216 | **0.0380** |

The paper assumes C_D0 = 0.0248. It used to sit **above** the bracket, and three
separate sections called it conservative on that basis. It now sits **inside**
it, optimistic by up to 53 % at the upper end.

### 3.4 Grok overruled my plan, and was right

Three of you said run RANS next. Grok said: *"Do not run RANS. Re-size §3.6
first. Every number that comparison rests on has moved."*

I agreed and did the re-sizing. **It broke a ranking.**

The asymmetry I had not seen: architecture A was charged 1/1.12 for exposed
hardware — tip frames only. Architecture B was charged 13/17, which comes from a
*measured* configuration and therefore already contains its lift-rotor drag. The
comparison was tilted toward A and the tilt had never been quantified.

The drag book-keeping reproduces the published 1.12 to three digits before
anything is changed — that is the chain check. Then the rotor term goes in:
multiplier **1/1.583**, cruise L/D 12.00 → **8.49**, take-off mass 50.0 → **54.5 kg**.

| Contract | as published | rotors charged |
|---|---:|---:|
| Fixed fuel fraction | −14.4 % | **+21.1 %** |
| Fixed fuel mass | −36.5 % | −5.4 % |
| Fixed MTOW and payload | −72.6 % | −44.9 % |

**Under equal fuel fractions the lift-plus-cruise layout now flies further.** A's
cruise efficiency fell below B's: 0.632 of clean against 0.765.

**Why A cannot escape this and B can.** B's lift discs are horizontal in cruise
and can be stopped with the blades aligned fore-and-aft. A's are fixed-pitch
tractors whose blades cannot be turned out of the flow at all. The asymmetry is
physical and it runs against this configuration.

### 3.5 A second correction pushes the other way and is larger

Applying the measured pack's buffer fraction to **all three** architectures —
charging only A would invert the very objection that motivated it — the layout
that suffers is B:

| Buffer fraction | A | B | C |
|---|---:|---:|---:|
| 4 % | 54.5 kg | 86.0 kg | 60.3 kg |
| 16 % | 106.2 kg | 369 kg | 130.6 kg |
| 20 % | 165.8 kg | **does not close** | 234.1 kg |

B's hover power per unit mass is the highest of the three and the buffer feeds
back through hover power. **B's entries past 12 % are not masses** — they lie on
a curve going vertical, and B stops closing between 18 and 20 %. I scanned for
that limit specifically so the 369 kg would not be quoted as a mass.

An earlier version said the measured pack cut A's margin from 42 % to 20 %. That
was **wrong in this paper's own favour** — it grew A on the measured pack while
holding B at a mass sized on the assumed one. Corrected.

### 3.6 Grok found two contradictions I had left standing

**First:** after writing the +21.1 % table into §3.6 I had failed to delete the
old range table below it, which still said *"the conclusion is the same under
every rule and grows more emphatic as the rule tightens"* — the sentence the new
table had just falsified. Replaced; the old figures are kept in the supplement as
a historical record, marked as such.

**Second:** the Highlights said the budget *"closes only on"* 3.8× the measured
rate while the abstract two paragraphs later said it *"re-closes 38 percent
heavier"* at that rate. Those are different statements. Fixed.

### 3.7 ChatGPT — two items I had missed entirely

You wrote that *"The resolution costs nothing"* was no longer defensible, and
that the title's *"no dedicated lift system"* needed one explicit qualification.

Both were valid and both were unaddressed. The first now reads that the state
needs no hardware but its aerodynamic cost must be computed — and the sentence
that inferred low drag from low section incidence is now marked as overturned by
the calculation below it. The second now states plainly that the tip pairs are
not a lift system, but that the take-off margin comes from their surplus, and
that the paper treats this as a limitation.

### 3.8 Chasing DeepSeek's neutral-point point found something worse

You found 0.859 m and 0.867 m under one label. The cause was not a mislabelled
run: 0.859 is the **untwisted** planform, 0.867 the wing **twisted to trim**.

Chasing it turned up the real problem. Across eight equally defensible solver
choices — geometry × moment reference × incidence range:

    x_np spans 0.858 – 0.867 m,  static margin 12.3 – 13.6 % MAC,  scatter 1.3 % MAC

In exact linear theory **none** of those choices can move a neutral point. They
move it because the vortex-lattice solution is linear in circulation but not in
incidence. Grid refinement moves it 0.26 %. **There was an uncertainty five times
the grid sensitivity that had never been measured.**

This runs against my own previous round: I had written that the neutral point
would need 33° of redistribution to breach a 5 % MAC threshold. True — but 1.3 %
MAC of scatter is the equivalent of nine degrees, so that column of the
sensitivity table sits inside its own method's noise floor.

---

## 4. The two calculations run this round

### 4.1 Compressibility — all four of you predicted it would matter. It does not.

You unanimously said: do this before RANS, the 0.0153 rests on incompressible
section data at tip Mach 0.77, and a correction would push it to 0.020–0.030.

**Method.** I did not monkey-patch the section call. The existing routine takes
`(alpha, Re)` and never sees local velocity, and Reynolds number is clipped at
the strip ends, so local Mach cannot be recovered from it — a patch would have
used a silently wrong Mach exactly where the clipping bites. Instead I wrote a
twin solver holding the local velocity, applied Prandtl–Glauert to lift, a Korn
drag-divergence Mach number and a fourth-power wave-drag increment to drag, and
**searched the zero-torque shaft speed again rather than holding it fixed.**

**Validation first.** With the correction disabled the twin reproduced the
original exactly — 25 046 rpm, −2.0937 N — so the two runs differ only in the
polar.

| | Shaft speed | Tip Mach | ΔC_D0, eight discs |
|---|---:|---:|---:|
| Incompressible | 25 046 rpm | 0.76 | 0.01535 |
| Compressibility-corrected | 24 958 rpm | 0.76 | **0.01541** |

**Four tenths of one percent.**

Grok's warning that the sign was an output rather than an input was correct, and
the mechanism is visible: the lift correction steepens the section lift-curve
slope, so the blade reaches zero torque at a *lower* shaft speed and profile drag
falls with the square of local velocity.

**But the dominant reason is simpler and worth stating.** A free-wheeling blade
sits at almost zero section lift by construction. The lift term in the Korn
relation then raises the drag-divergence Mach number to about 0.74, and at Mach
0.76 the wave increment is of order 10⁻⁶. **The compressibility penalty that
would fall on a loaded blade does not fall on this one.**

So 0.0153 is a figure, not a bound. §2.2, §3.6 and the +21.1 % do not need
re-deriving for this reason — which is what three of you had made a precondition.

### 4.2 RANS — started, and starting it exposed three mesh defects

The first attempt died with a floating-point exception. In order:

1. **Section-normal marching gave 104 negative-volume cells.** A common averaged
   normal reduced it to 2.
2. **The real killer was the sharp trailing edge.** Where upper and lower
   surfaces meet at a point the cell collapses; `checkMesh` reported a maximum
   aspect ratio of **8.2 × 10⁹⁶** — numerical infinity — and the solver died on
   it. A blunt trailing-edge base gives aspect ratio 5000, **zero** negative
   cells, and non-orthogonality 116 → 80.5.
3. **The defect was not in the tip cap**, which I tested separately: removing the
   cap raises negative cells from 2 to 1306. The cap was already doing its job.

**An honest correction to what this paper has been saying.** Previous rounds
described the RANS setup as existing and costed at fourteen hours. The setup
existed; it did not *run*. It needed a mesh-generator setting that had never been
exercised on this planform. That is now recorded.

**A second limitation, stated before you ask.** The mesh generator accepts
stations as `(span, leading edge, chord, thickness)` — **four fields, no twist**.
The trimmed −9.19° geometry therefore needs a capability the generator does not
have, not merely a new mesh. This run is on the **untwisted** planform at the
incidence where the vortex-lattice method gives the same cruise lift coefficient,
6.69°. The quantity being measured — the ratio of spanwise loadings between two
solvers — is a property of the solver pair, not of the twist. The trimmed run is
a separate step and is not being reported as done.

---

## 5. The RANS result — K(y), and what it decides

The run finished: 192 000 cells, four cores, 3 000 iterations, residuals at
10⁻⁶. Spanwise loading extracted from wall pressures. **The face sum reproduces
the case's own integrated lift coefficient exactly** — that is the check that the
extraction is not itself the answer.

**Three binning mistakes were made and caught before any number was reported**,
each by the same discipline: make the sum reproduce the solver's own coefficient.

1. Uniform bins left some bins empty, because wall faces cluster at the mesh's
   spanwise stations. K(y) came out with a hole in it.
2. Binning on the face centres' own z values produced 621 "stations" — the wall
   faces are not on constant-z planes.
3. Re-binning the vortex-lattice method's 104 fine strips into 20 coarse bins
   made the *smooth* side jagged, because bin edges cut strips. The fix is to
   integrate the vortex-lattice curve over each bin rather than fill bins with it.

The final binning uses the station list that defines the geometry, for both
solvers.

### 5.1 The numbers

| | Value |
|---|---|
| RANS C_L | 0.354 |
| VLM C_L | 0.450 |
| **K_L** | **0.787** |
| K(y), η = 0.05 to 0.91 | 0.740 – 0.816 |
| **K(y)/K_L** over the same range | **0.940 – 1.037** |

| η | VLM c_l·c | RANS c_l·c | K | K/K_L |
|---|---:|---:|---:|---:|
| 0.047 | 0.628 | 0.482 | 0.767 | 0.975 |
| 0.221 | 0.634 | 0.492 | 0.777 | 0.988 |
| 0.367 | 0.601 | 0.463 | 0.770 | 0.978 |
| 0.492 | 0.578 | 0.428 | 0.740 | 0.941 |
| 0.647 | 0.516 | 0.381 | 0.740 | 0.940 |
| 0.773 | 0.407 | 0.327 | 0.803 | 1.021 |
| 0.877 | 0.357 | 0.287 | 0.804 | 1.022 |
| **0.936** | 0.267 | 0.264 | **0.989** | **1.257** |
| 0.964 | 0.227 | 0.170 | 0.750 | 0.953 |

### 5.2 What it says

**The error is very nearly multiplicative.** Divide out the overall ratio and the
local ratio holds to within five percent of unity across nine tenths of the span.
**This is the first direct evidence for the cancellation argument** rather than an
assumption about it. That argument is the one the paper has been defending since
round 14 without being able to test.

**But the overall ratio runs the other way from the published comparison the
paper cites.** That source reports the vortex-lattice lift coefficient **low** by
30–38 % against RANS. Here it is **high** by 27 %. Different geometry, different
fidelity, and neither refutes the other — but the direction assumed in the earlier
argument is not the direction found here. The paper now reports this rather than
reconciling it.

### 5.3 Converted into the threshold's units — and it straddles

The sensitivity study measures trim-twist movement per degree of mid-span
redistribution, threshold 2.6°. The RANS residual is in units of "K/K_L scatter".
Those are not the same units and cannot be compared directly.

**So the bridge was measured, not asserted.** The same half-sine perturbation was
applied to the vortex-lattice solution and its effect on the normalised loading
ratio recorded: **0.0605 of K/K_L scatter per degree.** Then:

| | K/K_L scatter | Equivalent redistribution | Against the 2.6° threshold |
|---|---:|---:|---|
| All stations | 0.317 | **5.3°** | **fails** |
| Excluding η = 0.936 | 0.097 | **1.6°** | **survives** |

**One station carries the entire difference.** It sits at η = 0.94, where the mesh
is coarsest and nearest the tip closure, which makes a discretisation artefact
plausible — but plausible is not demonstrated, and I am not going to demote a
station because demoting it gives the answer the paper prefers.

**This is now the specific open item, and it is small.** A grid-refinement study
of this one solution decides whether that station is physics or discretisation.
That is much less work than the solution itself.

### 5.4 What this run is not

- **Not grid-converged.** One wall-function mesh, 192 000 cells.
- **Not the trimmed geometry.** The mesh generator takes stations as
  `(span, leading edge, chord, thickness)` — four fields, no twist. The trimmed
  −9.19° case needs a capability that does not exist, not merely a new mesh.
- **No viscous drag is taken from it.** Wall functions; the run was built to
  measure the shape of the loading, which is pressure's work.

---

## 6. Where we are stuck

1. **Nothing downstream of C_D0 = 0.0248 has been re-derived.** Cruise L/D, the
   ranges, the heavy design — all computed on a value now *inside* the computed
   bracket 0.0216–0.0380 rather than above it. Section 3.6 was re-sized by hand
   through the drag multiplier; the rest was not. **DeepSeek named this as the
   next calculation last round and it is still not done.**
2. **The η = 0.936 station**, above.
3. **The transition pitching moment** remains blocked on measurement, not effort.

---

## 7. THE FORK IN THE ROAD — what we actually need from you

This is the decision. Everything above is context for it.

### 7.1 Where you stood last round

**DeepSeek:** *"Yes, it is publishable. No, not under the current framing."* Lead
with the framework; the aircraft is a case study, not the result. The 37 % figure
is a property of the case under stated assumptions, not a headline.

**Grok:** *"Publish the framework and the contract table. Do not publish a
winner. The reversal under equal fuel fractions is the result a referee can use;
a restored 42 % would have been the result a referee should reject."*

**Qwen:** *"Do not soften the claim. State it exactly as you have… You have
corrected the paper out of over-claiming and into scientific rigor. Keep it
exactly as it is, fix the Mach 0.77 compressibility, and submit."*

**ChatGPT:** middle. *"Not trivial. The claim is better and more honest."*
Suggested tightening the Highlights wording but not restructuring.

**That is two for reframing, one against, one leaning keep.**

### 7.2 What has changed since you said it

Three things, and they do not all point the same way.

- **The compressibility correction came to nothing** (0.4 %). Qwen's
  precondition for submitting is now satisfied. Qwen's position gained.
- **The RANS comparison supports the cancellation argument** — the first direct
  evidence for a defence that had none. The paper's aerodynamic chain is in
  better shape than when you last saw it. That also favours keeping.
- **But the drag bracket now surrounds the assumed value**, and every range and
  L/D figure in the paper still sits on the old assumption. That is a structural
  weakness in exactly the numbers a "winner" framing would headline, and it
  favours reframing.

### 7.3 The question

**Does the paper lead with the framework or with the aircraft?**

**Option A — lead with the aircraft (Qwen's position).** Abstract opens with
meryemAircraft and the 37–42 % mass advantage. The contract-dependence is a
qualification. Risk: the headline number rests on a drag assumption now inside
its own computed bracket, and a referee who re-derives it will find the paper did
not.

**Option B — lead with the framework (DeepSeek's and Grok's position).** Abstract
opens with the three bills, the transfer property and the escape condition; the
aircraft instantiates the condition and the sizing results are reported as
conditional properties of a case study. The 37 % is inside, not on top. Risk:
a framework paper with one worked case may read as thin, and the aircraft is what
makes the paper concrete and citable.

**Option C — something neither camp proposed.** If you think the real answer is
a third shape — two papers, a different journal, a different unit of contribution
— say so and say why.

### 7.4 Answer these specifically

1. **A, B, or C**, and the single strongest reason.
2. **Does the RANS result change your answer from last round?** It is the first
   evidence for the cancellation argument, and it cuts toward keeping the current
   framing. Say if it moves you.
3. **The η = 0.936 station.** Would you report 1.6° or 5.3° as the headline, or
   refuse to report either until the grid study is done? A referee will ask.
4. **The un-re-derived downstream numbers.** Is submitting with §3.8 still on
   C_D0 = 0.0248 defensible if the limitation is stated plainly, or does it have
   to be done first? This is the largest remaining piece of work and the answer
   determines whether we submit in weeks or months.

Answer from this document. You do not need the manuscript, and if you want a
number that is not here, say which one rather than inferring it.
