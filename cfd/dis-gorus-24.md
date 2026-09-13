# Round 20 — one of you found a wrong sentence, and it led to a wrong finding

**Nothing has been deposited.** Version 6 is built but not uploaded, and it will
not be until this round is answered. The reason is in Section 3 below: last round
all four of you identified the same submission blocker, and it turned out not to
exist. That is not a complaint about your reviews — none of you could have caught
it — but it is a reason to run one more round before anything is public.

**Read this document alone.** You do not need the manuscript. Every number below
has been cross-checked against `makale-v6.md`.

---

## 1. The paper, in two hundred words

Hybrid VTOL aircraft pay for runway independence in cruise efficiency. The paper
treats that as *architectural* and builds an accounting framework: the penalty is
charged in three coupled currencies — **Bill 1**, hover hardware carried through
cruise as dead mass; **Bill 2**, its drag when exposed; **Bill 3**, continuous
power sized by a condition holding two percent of the flight. Every remedy
surveyed reduces one by raising another. Escape requires four things at once: the
same hardware, in the same orientation, doing the same job, with the hover peak
from a buffer.

**The headline is the framework's prediction: architectural rankings belong to
sizing contracts, not to architectures.** Three contracts are reported.

The case is an uncrewed tail-sitting blended-wing body — one coaxial nose pair for
both regimes, four small counter-rotating pairs at the tips for attitude, no
elevons, no rudder, no tilt, no dedicated lift system — instantiated at 50 kg and
1000 kg and carried far enough to show what instantiating the escape condition
costs.

Not claimed: that the aircraft is flyable, or that any architecture is generally
superior. Target: *Drones* (MDPI).

---

## 2. Current numbers, after this round's corrections

| Quantity | Value |
|---|---|
| Zero-lift drag bracket, computed | 0.0285 – 0.0381 |
| Assumed C_D0 | 0.0248 — **below both ends** |
| Light design, cruise L/D | 10.82 – 8.80 |
| Light design, **range** | **1 173 – 1 442 km** |
| Heavy design, cruise L/D | **11.78** (was 12.37) |
| Heavy design, **range** | **1 571 km** (was 1 649) |
| Free-wheeling rotor drag, light | 0.0154 |
| Free-wheeling rotor drag, heavy | **0.0051** (was 0.0033) |
| Heavy tip-pair figure of merit | **0.652 – 0.660** (was 0.536 – 0.547) |
| **Mass advantage over lift-plus-cruise** | **32 – 36 %** (was quoted as 37, earlier 42) |
| Range vs B, fixed fuel fraction | B leads, +24 to +45 % across the bracket |
| Range vs B, fixed take-off mass | A leads, −29 to −43 % |
| Range vs B, fixed fuel mass | **sign changes inside the bracket** |
| RANS/VLM ratio *K_L* | 0.796, converged over three meshes |
| Loading redistribution | 2.75°, equivalent to 1.04° of trim twist and **0.8 %** on range |
| Abstract | **195 words** |

---

## 3. The blocker you all found did not exist, and here is exactly why

### 3.1 What you said

All four of you flagged the same item, and three of you called it the one thing
you would not send:

- **Grok:** *"Heavy tip pairs at FoM 0.547 against a budget written at 0.599: this
  is the one that is not merely a limitation… a referee who opens that paragraph
  and the power table together has an internal contradiction."*
- **DeepSeek:** *"That is not a limitation on a result; it is a result that says
  the heavy design's power budget is wrong."* Recommended re-size or withdraw.
- **ChatGPT:** *"Yes, in current presentation"* — a submission blocker. Recommended
  re-size, or downgrade the heavy case to an unclosed scaling diagnostic.
- **Qwen:** alone in saying keep it, quantify it, and supplied the arithmetic —
  thrust scales as FM^(2/3), so 0.547/0.599 gives a 6 % moment loss and rotation
  margins of 1.48 and 0.99.

### 3.2 What actually happened

**Qwen also made a separate objection that none of the rest of you made**, and it
is the one that mattered. Section 3.9 explained the scale behaviour of Bill 2 by
saying the tip discs are referenced to a wing area that grows faster than they do.
Qwen checked the geometry and said that is false.

It is false. Verified:

| | tip disc area | wing area | ratio |
|---|---:|---:|---:|
| 50 kg | 0.2513 m² | 1.98 m² | **0.1270** |
| 1000 kg | 2.8205 m² | 22.24 m² | **0.1268** |

**Identical to three digits.** The stated mechanism contributes nothing.

Qwen's replacement mechanism — *"the larger rotors turn slower and carry less
profile drag per unit disc area"* — is also not right. They turn slower in rpm,
but the aerodynamically relevant tip speeds are nearly equal: 262 m s⁻¹ light
against 269 m s⁻¹ heavy.

**So rather than swap one guess for another, the actual mechanism was measured.**
It is blade solidity: 0.0754 light against 0.0215 heavy. Which raised the
question: *why is the heavy blade so much less solid?*

### 3.3 The answer was a hard-coded constant in our own code

The blade-element routine sizes the chord inside limits:

```python
c_yeni = np.clip(dTdr_hedef / np.maximum(pay, 1e-6), 0.004, 0.040)
```

Four to forty millimetres — **absolute**. Those bounds were chosen for the light
design's 0.20 m rotor, where they mean chord-to-radius ratios of 0.04 to 0.40 and
bind sensibly. Applied unchanged to the heavy design's 0.67 m rotor:

| | radius | mean chord | **chord / radius** |
|---|---:|---:|---:|
| light | 0.100 m | 13.9 mm | 0.139 |
| heavy | 0.335 m | 11.9 mm | **0.035** |

A 12 mm chord on a 335 mm radius. The clip was binding at **both** ends.

### 3.4 What the bug manufactured

With the limits expressed relative to the radius, as they should have been:

| | figure of merit | ΔC_D0 |
|---|---:|---:|
| with the bug | 0.536 – 0.547 | 0.0033 |
| **corrected** | **0.652 – 0.660** | **0.0051** |

**The heavy tip pairs clear the required 0.599 comfortably.** The finding all four
of you treated as the submission blocker — a heavy design that cannot hover on its
own power allocation — **was produced by our chord limits, not by the physics.**

**The light design is unchanged.** At its own radius the relative and absolute
limits are identical, and every light figure in the paper reproduces to the digit.
That is the check that the fix did not quietly repair something else.

It is **withdrawn in the text rather than silently corrected**, with the reason
stated, because a reader comparing against an earlier deposited version is
entitled to know which of the two numbers to believe and why.

### 3.5 The real mechanism, measured

$$\Delta C_{D0} \;\propto\; \frac{\sigma R^{2}}{q\,S}$$

*R²/S* is the constant disc-to-wing ratio above and contributes nothing — exactly
Qwen's point. Two terms move: **solidity** falls 0.075 → 0.044 as the larger rotor
meets its thrust with proportionally less blade, and **cruise dynamic pressure**
rises by 1.78 between 30 and 40 m s⁻¹. Their product is 3.08; the computed drag
ratio is 3.04.

Bill 2 still shrinks with scale. The reason is not the one the paper gave.

### 3.6 What this episode says about these reviews

None of you could have found this. You read the manuscript; the defect was in the
generator. **What found it was Qwen's insistence that a stated mechanism was
arithmetically wrong, followed by refusing to accept the replacement mechanism
without measuring it.** That is the useful pattern, and it is worth naming: the
external reading caught a *wrong sentence*, and chasing the wrong sentence caught
a *wrong number*.

---

## 4. Grok was right about the mass advantage, and it is worse than Grok thought

**Grok:** *"Make '37 %' point at one mass pair. 37 % of 86 kg is 54 kg. The
sweep's adverse end is 53.9 kg; the assumption is 50.1 kg (which is 42 % again).
One comparison, one sentence, no third mass for A."*

Checking it found the actual defect: the 37 % compared **this configuration with
its rotors charged (54.5 kg) against a lift-plus-cruise layout sized on the
uncharged drag (86.0 kg)**. Two different aerodynamic bases — the same
apples-to-oranges class this paper has been correcting for several rounds,
committed by us in the correction itself.

Re-solving **both** layouts on the same drag at each end of the bracket:

| | A | B | A lighter by |
|---|---:|---:|---:|
| bracket, favourable end | 51.1 kg | 75.5 kg | **32.3 %** |
| bracket, adverse end | 53.9 kg | 83.9 kg | **35.7 %** |

**32 to 36 percent.** Not 37, and not the 42 of the original assumption. Corrected
in the abstract, the highlights, §3.6, §4.4 and the mass supplement.

---

## 5. Your other points, and what was done

- **All three of you who raised it** — Grok, ChatGPT and Qwen — said the 2.6° should
  not be called a threshold, because exceeding a gate you set yourself and then
  arguing it does not matter reads badly however true it is. **Agreed and changed.**
  It is now what it is: a unit conversion. 2.75° of redistribution → 1.04° of trim
  twist → 2.1 % of span efficiency → **0.8 % of range**, against a drag bracket
  that moves the same number by 9 to 26 %.
- **Qwen:** *"'nothing is taken from the tip alone' is true but not sufficient — the
  span efficiency, roll damping and neutral point are integrals over the span."*
  Correct and now bounded in the text: the tip carries about a tenth of the load and
  disagrees by about a quarter, so those integrals carry roughly 2.5 % from this
  source.
- **DeepSeek:** flagged +21.1 % in one table against −13.7 % in another. Not an
  arithmetic error — one is the assumption plus rotor (0.0401, *above* the bracket),
  the other the assumption alone (0.0248, *below* it) — but the labelling did not
  say so. Fixed.
- **Grok:** *"Do not advertise 'forty internal consistency checks, zero deviations'
  in correspondence."* Taken. It will not appear in the cover letter.
- **Abstract** cut from 214 to **195 words**.
- **ChatGPT:** *"don't let 'converged' spill over into the spanwise disagreement."*
  The text now separates them: the integrated ratio converges, the near-tip
  discrepancy does not.

---

## 6. The question this round exists to ask

**ChatGPT proposed a distinction last round that the bug has not made obsolete, and
we want all four of you on it.**

The proposal was: the 1000 kg case should not be called a *reference design* unless
it closes; if it does not, it should be labelled an **unclosed scaling diagnostic**
and stripped of language that treats it as a demonstrated design.

The efficiency objection that prompted it has dissolved. **But the heavy design
still does not close, for a different and older reason**, which the paper states
plainly in the mass supplement:

> *"The heavy design is not closed by this exercise, and no claim is made that it
> closes… the component build-up does not demonstrate closure of the heavy design.
> That, and not any of the light-design assumptions, is the largest open question
> in the mass budget of this study."*

The reason is structural, not propulsive: shell mass scales as wetted area while
take-off mass scales as volume, so the shell fraction depends on how areal density
grows with size, and that exponent has not been measured. At an exponent of 0.467
the 1000 kg design's 260 kg payload is exactly break-even — closing below, failing
above — and the paper declines to argue for either side because any such argument
would be a structural model standing in for a measurement.

Meanwhile §3.8 is titled **"Heavy reference design — 1000 kg"** and reports its
mass, power, endurance and range in a table like the light one.

**Q1 — Is that label defensible?** Three readings are available:

- **(a) Keep it as a reference design.** The sizing is complete and internally
  consistent; "not closed" is a stated condition on the structure, exactly as the
  light design's 1.78 kg m⁻² condition is. The two designs are then treated alike.
- **(b) Relabel it an unclosed scaling case** — ChatGPT's proposal. Keep the
  numbers, remove "reference design", and do not let it carry the scale-behaviour
  argument as a *computed* result.
- **(c) Something else** — for instance, keep the label but move the closure
  condition from the supplement into §3.8 itself, so the qualification travels with
  the table rather than sitting sixty pages away.

**Q2 — If (b), what does §3.9 become?** The scale-behaviour section currently rests
on two computed designs. If the heavy one is a diagnostic rather than a design, is
the Bill 2 scaling result still a result, or does it become an analytical
projection? Note that the Bill 2 numbers themselves do not depend on the structural
closure at all — they come from the rotor calculation — so there is an argument that
the scaling result survives regardless of what the label says.

**Q3 — Does the light design need the same treatment?** It closes only on an areal
density of 1.78 kg m⁻² that is also not demonstrated, with 2.2 kg in hand. If the
heavy design is relabelled for not closing, consistency may demand the light one be
labelled for closing only conditionally. Or the distinction is real — one has a
margin and the other does not — and the labels should differ.

---

## 7. Our own view, stated so you can disagree with it

We lean to **(c)**, and think **(b)** is very close behind.

The argument for (c): the heavy design's numbers are not in doubt. Its sizing loop
is the same loop as the light one, its rotor calculation now clears its own
efficiency requirement, and its range of 1 571 km is as well-founded as the light
design's 1 173–1 442 km. What is in doubt is a *structural* condition that is also
in doubt for the light design, differing in degree rather than kind — the light one
has 2.2 kg of margin, the heavy one has none. Relabelling only the heavy design
implies a categorical difference that the analysis does not support.

The argument against our own position, which we find uncomfortable: the light
design has a margin and the heavy one is at break-even. A referee may reasonably
say that break-even *is* a categorical difference, and that reporting a range for
a design whose payload closes only below an unmeasured exponent is reporting the
range of an aircraft that may not exist.

**We are not confident enough in (c) to act on it without this round.** If two or
more of you prefer (b), we will take (b).

---

## 8. Also worth your time

**Q4 — Is the mass advantage now stated correctly?** It is 32–36 % across the
bracket, with both layouts re-solved on the same drag. The abstract says "32 to 36
percent." Is a two-ended figure the right thing to put in an abstract, or should it
be the adverse end alone?

**Q5 — Is the withdrawal of the FoM finding handled right?** The text states the
error, names the cause, gives both the wrong and the corrected numbers, and says
why it is recorded rather than repaired. Is that the correct disposition for a
finding that appeared in a deposited version, or does it draw attention to a defect
better handled by a quiet correction and a version note?

**Q6 — Anything else before deposit.** This is the round to say it. Nothing is
public yet.

Answer from this document. If you want a number that is not here, say which one
rather than inferring it.
