# Round 17 — what we did, what broke, and where we are stuck

You are one of four independent readers. You disagree with each other often, and
that is the point. This round two of you broke a headline claim and one of you
was right to overrule my own plan. What follows is the full account — what was
run, what was expected, what actually came out, and what I could not get past —
so that you are not reasoning from a summary of a summary.

---

## 0. Version check — do this before reading anything else

Open `makale-v5.md`. Confirm **all four**:

| Marker | Current value |
|---|---|
| Sections | five; §2 is *Materials and Methods* |
| §3.3 free-wheeling rotor drag | **0.0153** (not 0.0085) |
| §3.6 contract 1, B against A | **+21.1 %** (not −14.4 %) |
| Abstract mass claim | **thirty-seven to forty-two percent** |

If you see 0.0085, or −14.4 %, or nine numbered sections: you have an old copy.
**Say so and stop.** Do not review it. One of you has now described a
non-existent version three rounds running, and a wrong review costs more than no
review.

---

## 1. What happened to your last round's claims

Every claim was checked against the files. Here is the disposition of each,
including the ones that did not survive.

### Confirmed and acted on

| Claim | Who | What was done |
|---|---|---|
| Headline rotor drag taken from a propeller the aircraft cannot use (FoM 0.27 vs 0.599) | DeepSeek | Recomputed. 0.0085 → **0.0153** |
| Rotor drag absent from the zero-lift drag bound; breaks the conservatism claim | DeepSeek | Confirmed, and **larger than you said** — see §2.2 |
| Abstract/Highlights still carry unconditional 42 % | DeepSeek, Grok | Both rewritten |
| Abstract "closes only at 3.8×" contradicts §4.4 | DeepSeek, ChatGPT | Rewritten |
| Two neutral points (0.859 vs 0.867) under one label | DeepSeek | Confirmed — **cause was not what you said**, see §2.4 |
| Two roadmap paragraphs in §1; first is self-referential and false | DeepSeek | Deleted |
| §3.5 ledger says control propellers are not in the cruise airstream | DeepSeek | Rewritten; they are, and it is now the largest ledger entry |
| §2.9 "most of the aircraft's zero-lift drag" | DeepSeek | Weakened to "a substantial fraction" |
| §3.3 heading "reduced, not removed" contradicts its own result | Grok | Now "reduced, and larger than assumed" |
| Conclusion omits the rotational-dynamics result | DeepSeek | Added |
| "The resolution costs nothing" no longer defensible | ChatGPT | Rewritten; electrical cost ≈ 0, aerodynamic cost is 0.0153 |
| Title's "no dedicated lift system" needs one explicit qualification | ChatGPT | Added to §2.8 |
| S4.7 "unchanged across profiles — 5.4, 6.6, 6.3 m" | DeepSeek | Three different numbers are not "unchanged"; rewritten |
| §3.6 "leads in three" when a fourth cell is +0.2 % | DeepSeek | Now stated as three plus a tie |
| S1 table displayed sum off by 0.0001 | DeepSeek | Table rebuilt (see §2.2) |

### Not confirmed

**Qwen — the IMRaD restructure is missing, nine sections, §2 is "Background:
seventy years of attempts".** The file has five sections, §2 is *Materials and
Methods*, and that phrase appears nowhere. The other three read the same file
and saw five sections.

*But the seed was ours.* A dead sentence from the IMRaD move was still in §1:
*"The remainder of the paper is organised as follows. Section 1 reviews seventy
years of attempts…"* — self-referential and false. It is plausible that was read
and a section structure inferred around it. The sentence is deleted. The lesson
cuts both ways: our leftover invited the error, and a claim about a file's
structure still has to be checked against the file.

**Grok — the 9.2 kg payload figure does not follow from the published chain;
it should be 7.0 kg.** Your buffer arithmetic was exactly right: 11.66 kW at the
bus, 7.78 kg of pack at 1.5 kW kg⁻¹, 5.98 kg of extra mass. The step that
differs is the last one. The component build-up leaves **2.2 kg unallocated
above the 13 kg payload** — the budget returns 15.2 kg of available mass, not
13.0 — so the buffer eats that margin first and the payload second.
15.2 − 5.98 = 9.23. The number stands.

**Your objection was still worth making**, and it changed the paper: that
arithmetic was not published anywhere, and the 9.2 kg figure spends the *entire*
structural margin — the 2.2 kg into which buckling, torsion, local load
introduction, fasteners, adhesive and paint must all fit. That condition is now
stated in §4.4.

**DeepSeek — S4.7 "mixes a pitching-moment model with two rotation profiles".**
Half right. "Unchanged" was wrong and is fixed. But linear, bang-bang and smooth
are all three rotation profiles; no moment model is mixed in.

### Overruled — and you were right

**Grok said: do not run RANS next, re-size §3.6 first.** Three of you recommended
RANS. Grok argued the comparison table was standing on two numbers that had both
moved, and that a loading-distribution study does not decide the claim the paper
opens with. I agreed, and did the re-sizing instead. It broke a ranking. See §2.3.
RANS is still coming, and Grok's objection to it has now been discharged.

---

## 2. What was run this round

### 2.1 Free-wheeling drag at the aircraft's own hover efficiency

**What I expected.** A modest correction. The four-design table showed drag
falling monotonically with design section lift coefficient, so I expected to
interpolate to the aircraft's figure of merit of 0.599 and land near 0.020 —
DeepSeek's own estimate was 0.013–0.024.

**What I did first, and why it was invalid.** I bisected on figure of merit to
hit 0.599. The solver returned 0.633 and 0.557 at essentially the same design
point. Bisecting a noisy function is exactly the failure mode this project has
been bitten by before, so I stopped and tested the solver instead of trusting it:
every design built **twice**, same inputs.

**What came out.** The solver is deterministic — every design reproduces exactly.
What looked like noise is a **cliff**:

| design c_l | FoM (run 1) | FoM (run 2) | ΔC_D0 |
|---|---|---|---|
| 0.55 | 0.646 | 0.646 | 0.0238 |
| 0.60 | 0.645 | 0.645 | 0.0199 |
| 0.64 | 0.641 | 0.641 | 0.0174 |
| 0.68 | 0.633 | 0.633 | **0.0153** |
| 0.70 | 0.350 | 0.350 | 0.0126 |
| 0.85 | 0.270 | 0.270 | 0.0085 |

Figure of merit is flat at 0.63–0.65 up to c_l 0.68, then collapses. **0.599
falls inside the collapse**, so no design in this family sits on it. Every design
that *meets* the hover requirement lies at c_l ≤ 0.68, and the least draggy of
those gives **0.0153**.

So the answer is not an interpolation — it is a **constraint boundary**, which is
a sharper thing, and it is 25 % below DeepSeek's upper estimate and 80 % above
the published headline.

**What I could not settle.** The 0.68 design runs at **tip Mach 0.77**. The
section data underneath the blade-element solver are incompressible. I report
0.0153 as a lower bound and say why, but I have not put a compressibility
correction in. **This is open — see §4, question 3.**

### 2.2 The drag bound, which turned out to be load-bearing

DeepSeek said the rotor term was missing from the zero-lift build-up. It was —
there was no rotor row at all.

| | lower | upper |
|---|---:|---:|
| as published | 0.0131 | 0.0210 |
| with rotors | 0.0216 | **0.0380** |

The paper assumes C_D0 = 0.0248. It used to sit **above** the bracket, and three
separate sections called it conservative on that basis. It now sits **inside**
it — optimistic by up to 53 % at the upper end.

**This is worse than DeepSeek's own estimate** (0.0281–0.0311), because the
computed rotor term is 0.0153 rather than the 0.0085 that estimate used.

### 2.3 Re-sizing the three-architecture comparison

**The asymmetry I had not seen.** Architecture A was charged 1/1.12 for exposed
hardware — tip frames only. Architecture B was charged 13/17, which comes from a
**measured** configuration and therefore already contains its lift-rotor drag.
The comparison was tilted toward A and the tilt had never been quantified.

**Chain check first.** The drag book-keeping reproduces the published 1.12 to
three digits before anything is changed. Then the rotor term goes in:
multiplier **1/1.583**, cruise L/D 12.00 → **8.49**, MTOW 50.0 → **54.5 kg**.

| Contract | as published | rotors charged |
|---|---:|---:|
| Fixed fuel fraction | −14.4 % | **+21.1 %** |
| Fixed fuel mass | −36.5 % | −5.4 % |
| Fixed MTOW and payload | −72.6 % | −44.9 % |

**Under equal fuel fractions the ranking reverses.** A's cruise efficiency is now
below B's — 0.632 of clean against 0.765. The mass advantage survives at **37 %
rather than 42 %**. The tilting layout now leads under all three.

**Why A cannot escape and B can.** B's lift discs are horizontal in cruise and
can be stopped with blades aligned fore-and-aft. A's are fixed-pitch tractors;
the blades cannot be turned out of the flow at all. The asymmetry is physical and
it runs against this configuration.

**A second correction pushes the other way and is larger.** Applying the measured
pack's buffer fraction to **all three** architectures — charging only A would
invert the very objection that motivated it — the layout that suffers is B:

| Buffer fraction | A | B | C |
|---|---:|---:|---:|
| 4 % | 54.5 kg | 86.0 kg | 60.3 kg |
| 12 % | 82.1 kg | 182.5 kg | 95.9 kg |
| 16 % | 106.2 kg | 369 kg | 130.6 kg |
| 18 % | 132.1 kg | 1 157 kg | 172.1 kg |
| 20 % | 165.8 kg | **does not close** | 234.1 kg |

B's hover power per unit mass is the highest of the three and the buffer feeds
back through hover power. **B's entries past 12 % are not masses** — they lie on
a curve going vertical, and B stops closing between 18 and 20 %. I scanned for
that limit specifically so that 369 kg would not be quoted as a mass.

An earlier version said the measured pack cut A's margin from 42 % to 20 %. That
was **wrong in this paper's own favour** — it grew A on the measured pack while
holding B at a mass sized on the assumed one. Corrected.

**The two corrections do not cancel and the paper does not claim they do.** They
act on different contracts: the rotor drag costs A the range comparison under
equal fuel fractions; the measured buffer costs B its ability to close at all.

### 2.4 The neutral point — chasing a reviewer's point found something worse

DeepSeek found 0.859 m and 0.867 m under one label. Confirmed, but the cause is
not a mislabelled run: 0.859 is the **untwisted** planform and 0.867 is the wing
**twisted to trim** — the geometry the aircraft actually flies.

Chasing it turned up the real problem. Across eight equally defensible solver
choices — geometry × moment reference × incidence range:

    x_np spans 0.858 – 0.867 m,  static margin 12.3 – 13.6 % MAC,  scatter 1.3 % MAC

In exact linear theory **none** of those choices can move a neutral point. They
move it because the vortex-lattice solution is linear in circulation but not in
incidence. Grid refinement moves it 0.26 %. So there was an uncertainty **five
times the grid sensitivity** that had never been measured.

**This runs against my own previous round.** I had written that the neutral point
would need 33° of spanwise redistribution to breach a 5 % MAC threshold. True —
but 1.3 % MAC of scatter is the equivalent of **nine degrees**, so that column of
the sensitivity table sits inside its own method's noise floor. It is now flagged
as showing an absence of movement rather than measuring one. The trim twist has
no such problem: residual 10⁻⁶ at every shape.

---

## 3. Where I am stuck

**Three things, stated plainly.**

1. **The rotor drag rests on incompressible section data at Mach 0.77.** Every
   number in §2.1–2.3 above descends from it. I flagged it as a lower bound; I
   did not fix it.

2. **Nothing downstream of C_D0 = 0.0248 has been re-derived.** Cruise L/D, the
   ranges of §3.8, the heavy-design results — all computed on a value that is now
   inside the bracket rather than above it. §3.6 was re-sized by hand through the
   drag multiplier; the rest was not.

3. **The transition pitching moment remains blocked on measurement**, not effort.
   Three methods of three fidelities fail above ~10° incidence, the best of them
   against wind-tunnel data. No amount of further simulation fixes this.

---

## 4. What I want comment on

Not a general review. These four, in order of how much they would change.

**Q1 — Is RANS still the right next calculation, now that §3.6 has moved?**
Three of you said run it; Grok said fix the table first, and Grok was right. The
table is fixed. The case for RANS is that §3.10 already measures the
*sensitivity* to a spanwise redistribution — 0.15 % MAC of neutral-point movement
and 0.38° of trim twist per degree — and RANS would supply the redistribution
itself. The cost is ~14 hours on 1.67 M cells plus re-meshing the twisted
geometry. **If you think something else should go first, name it and name the
result that would count against the paper.**

**Q2 — Does the 1.3 % MAC solver scatter spoil the RANS comparison before it
starts?** A RANS result would be read against a VLM baseline carrying that
scatter. Does that make the comparison worth less than it looks? If so, what
fixes it — pinning the VLM protocol first, or comparing a different quantity
(sectional loading ratio rather than neutral point)?

**Q3 — Compressibility on the blade-element run.** 0.0153 comes from a blade at
tip Mach 0.77 with incompressible section data. Is the honest move to report it
as a bound and proceed, or to redo it with a correction before anything else is
built on it? Note that a correction would push the drag **up**, not down, which
makes §2.2 and §2.3 worse rather than better.

**Q4 — Is the paper now making a claim it can defend?** With the ranking reversed
under one contract, the drag assumption no longer conservative, and the mass
advantage at 37 %, the honest summary is that this configuration has a mass
advantage and a contract-dependent range advantage, not a general one.
**Is that still a publishable claim, or has the result been corrected into
triviality?** I want a straight answer to this, including "no" if that is the
answer.

---

## 5. What I am not asking for

Do not re-run the 3-DOF or 6-DOF transition study. S4.7 already did the useful
sensitivity — with zero aerodynamic moment the light design loses 5.4 m where the
kinematic model reports zero, and the loss grows under tighter control gains.
Further simulation without measured C_m and C_m_q manufactures precision around
an unknown. Two of you said this last round and I agree.

Do not re-run the mass-closure loop. It is done and reported at four specific
powers.

If you cannot open the file, say so rather than describing it.
