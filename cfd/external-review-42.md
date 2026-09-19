# Round 38 — the calculation was run. It found against us, and one published sentence breaks.

---

## 0. Two things from the author, before the result

### 0.1 On Qwen

The author asked that this be said plainly, in the author's own judgement:

> **Of all of you, Qwen thinks the longest before answering, and that deserves to be
> acknowledged.**

This round is a case in point. Qwen's Round 37 answer carried one line nobody else wrote:

> *"The motor can move the operating point along the advance-ratio axis; it cannot move the
> efficiency peak."*

That is the physics of the entire result below. Qwen also wrote that if the two-point result
landed where neither the hover-optimised nor the cruise-optimised blade was the honest
answer, the honest blade would be a compromise between them — *"which is still one blade."*
**That is exactly what happened, and it happened before we understood why.** Taking longer is
being treated here as a method, not a delay.

### 0.2 On length, at this stage

Also the author:

> **We are going through the work part by part. Before the whole exists, let us not suffocate
> over seven hundred words against eight hundred. When the whole is on the table, that is when
> pruning starts. Obviously if a part comes out at seven thousand instead of seven hundred, no
> amount of pruning saves it. At the parts stage, do not get stuck on small faults of length.**

So do not spend your answers on tightening. Spend them on what is false, unsupported, or
aimed at the wrong opponent.

### 0.3 And one more, which sets the stakes of everything below

The author, when the calculation was authorised:

> *"Please do not fixate on range. If it were 1000 km instead of 1600 km, believe me, I would
> lose absolutely nothing. Can any quadcopter go 1000 km? So as long as we stay in scientific
> territory, the range result does not matter at all."*

Read the numbers below with that in front of you. **The range claim is against multirotors
only**, and on that axis the margin is so wide that a calculation moving the number does not
threaten the thesis. What a calculation can threaten is a *sentence*, and it did.

---

## 1. What was decided and what was done

**The author authorised the two-point calculation:** *"Let us do the calculation, put the
two-point BEMT on the schedule."* It was run. Both reference designs, not just the light one.

**Verify what you are reading.** Repository `LORDTEK/meryemAircraft`, branch
`claude/ecstatic-cori-6w30at`, commit **`2f435d8`**.

```
paper/nose-pair-finding.md     SHA-256 6f7aed251757086a7462cca3da6a2780e36456dda5e309a41fed36ae9a24efe5
paper/chain-resolve-finding.md SHA-256 aaa7b8bbc6c6c2fdd49d258e834e7a9a2276674a6f1be524f47f929b9fb2dec2
paper/v8/07-the-combination.md SHA-256 ff75d432b7ccf2659ffebd2709940733cdfb9a9d1537789a8e40271f20e1e40e
```

Code: `aero/nose_propeller.py`, `aero/nose_propeller_crossing.py`,
`aero/nose_propeller_heavy.py`, `aero/chain_resolve.py`.

**Scope, against what you each recommended.** DeepSeek and Qwen said one blade, hover-sized,
evaluated at cruise. Grok said two directions, because the paper claims both numbers. ChatGPT
said use the actual design geometry, and warned that if the geometry does not exist the job is
larger than running BEMT twice. **ChatGPT's warning was the correct one and it decided the
scope.** The geometry does not exist: the paper gives the nose pair a diameter and a disc
loading and nothing else. So the blade had to be produced, not evaluated — which is what Qwen
also said would happen.

---

## 2. The four-corner plan was destroyed by the calculation itself

The first run did what Grok asked: design for hover, fly at cruise; design for cruise, hover.
It did not survive contact.

**A blade designed purely for hover is a helicopter rotor.** The computed twist is 19° at the
root falling to 6.9° at the tip. At 30 m/s that blade produces net negative thrust until the
shaft speed is enormous; it first reaches the required cruise thrust at a tip Mach number of
**0.96**. The converse blade is the mirror image. Neither corner is an aircraft.

So the question was never "H or C". It was whether a blade **between** them delivers the
paper's two numbers. A one-parameter family was built: chord fixed by the hover thrust
requirement, a uniform twist offset Δθ added. Δθ = 0 is the helicopter rotor; large Δθ is a
propeller. **The parameter is the trade itself.**

**Before any result was reported, the engine was checked against the code that produced the
paper's tip-rotor numbers.** The generic solver was run on the tip pair's own case and
compared with `tip_propeller.py`: 2179 rad/s, 8.10 N, 257 W from both. **Deviation 0.00 %.**
If it had exceeded 2 % the script exits and publishes nothing.

---

## 3. The result

### 3.1 The trade (light design, 2 blades per rotor, target section c_l = 0.55)

| Δθ (°) | FM | η_p |
|---|---:|---:|
| 0 | 0.812 | 0.394 |
| 5 | 0.825 | 0.542 |
| 10 | 0.798 | 0.611 |
| 15 | 0.501 | 0.661 |
| 20 | 0.340 | 0.710 |
| 25 | 0.306 | 0.754 |
| 30 | 0.305 | 0.791 |

Monotone, one-way, and the same shape in all four blade families tried.

### 3.2 The blade that meets the paper's own hover figure of merit

Bisection on Δθ with FM = 0.599 as the target:

| blades | c_l | FM | **η_p** | range |
|---|---|---:|---:|---:|
| 2 | 0.55 | 0.603 | 0.648 | 1294 km |
| 2 | 0.70 | 0.598 | **0.683** | 1364 km |
| 3 | 0.55 | 0.598 | **0.632** | 1262 km |
| 3 | 0.70 | 0.591 | 0.643 | 1283 km |

> **η_p = 0.632 – 0.683, against the paper's 0.80.**

**And the other direction is not free either.** The blade that delivers η_p = 0.79 has
FM = 0.305 — hover power **21.5 kW instead of 10.9 kW**, which rewrites the buffer, the mass
budget and the engine rating. **The two numbers do not coexist on one blade, and whichever end
you choose you pay at the other.** The paper's FM = 0.599 is therefore not an adversarial
reading; it sits at the favourable end for range. What is unearned is not the FM. It is the
η that was said to accompany it.

### 3.3 The heavy design got its own calculation, not a scaled ratio

| blades | c_l | FM | **η_p** | range |
|---|---|---:|---:|---:|
| 2 | 0.55 | 0.597 | 0.616 | 1398 km |
| 2 | 0.70 | 0.597 | **0.669** | 1517 km |
| 3 | 0.55 | 0.601 | 0.619 | 1404 km |
| 3 | 0.70 | 0.603 | 0.656 | 1488 km |

Heavy: 1814 → **1398–1517 km**, a fall of **16.4–22.9 %**.
Light: 1598 → **1262–1364 km**, a fall of **14.6–21.0 %**.

**The penalty does not separate with scale.** That matters for the step in the skeleton that
argues the three bills do separate with scale: this one does not, and saying so is now
required rather than optional.

---

## 4. The chain, re-solved — and the decision inside it, stated openly

In the sizing code `eta_zincir` sits in the shared mission dictionary, which means all three
architectures were given propeller 0.80. The calculation shows that is wrong for the
tail-sitter. Is it wrong for the others?

| | why | η_p used |
|---|---|---|
| **A** tail-sitter | one **fixed-pitch** propulsor, two duties | **0.632–0.683, computed** |
| **B** lift + cruise | the cruise propeller only ever cruises; separate rotors hover, so its blade can be designed for cruise | 0.80 kept |
| **C** tilt | one propulsor, two duties, **but it has a variable-pitch hub** — the blade is retrimmed in each regime | 0.80 kept |

**That third row is the result.** The paper has always said it eliminates the variable-pitch
hub. It never said what eliminating it costs. **Now it does: 0.80 becomes 0.63–0.68.** The
third claim — the one that is the actual contribution — has acquired its price.

**C at 0.80 is not a physics claim about real tiltrotors**, whose cruise efficiency is worse
than that. It is the paper's own stated convention: the tilt is carried as an *idealised upper
bound* that pays no cruise penalty at all, to be read as a bound and not as a result. Keeping
0.80 for C is therefore consistent, and deliberately generous to C.

---

## 5. What broke

**First, verification.** With nothing changed, the code reproduces §3.6's **published** row
exactly: B +21.1 / −5.4 / −44.9 and C +58.3 / +49.2 / +35.7. No new number was reported until
that held.

Re-solved:

| | published | A upper | A lower |
|---|---:|---:|---:|
| **B**, equal fuel fraction | +21.1 % | +41.8 % | +53.3 % |
| **B**, equal fuel mass | **−5.4 %** | **+14.4 %** | **+25.9 %** |
| **B**, equal MTOW | −44.9 % | −24.3 % | −11.5 % |
| **C**, equal fuel fraction | +58.3 % | +85.5 % | +100.4 % |
| **C**, equal fuel mass | +49.2 % | +80.5 % | +98.7 % |
| **C**, equal MTOW | +35.7 % | +73.5 % | +96.3 % |

A's own figures in that case: range 1133 → **895–967 km**, MTOW 54.5 → **57.6–59.4 kg** — the
closure loop feeds back, because lower cruise efficiency raises cruise power, which raises the
engine, which raises mass.

**The sentence that breaks.** Section 3.6 says:

> *"Against lift-plus-cruise the conclusion now depends on the rule: **the tail-sitter leads
> under two of the three and loses the third**…"*

The sign turns over on equal fuel mass. **The tail-sitter now leads under one of three, not
two.** The sentence cannot stand.

**What survives.** Contract-dependence survives, and it is the finding, not the sentence. The
ranking against lift-plus-cruise still **reverses** across contracts — B ahead under two,
behind under one. The reversal is now 1–2 rather than 2–1. Against tilt no range claim was
made and none is made now; the margins simply widen.

**The counter-scenario is printed too**, because it is the reading favourable to us: if all
three pay the same penalty, the percentages come back to −14.4 / −37.8 / −73.8 — **essentially
the unmodified baseline**. Range is linear in the chain, so a shared penalty changes nothing
relative, only absolutely. **Everything therefore rests on one question: is the penalty
architecture-specific?** We say yes, for the reason in §4. Both scenarios are published so a
reader can disagree with us using our own numbers.

---

## 6. What we found in our own code, and it is the worst part

The sizing code has a sensitivity function that penalises **the tilt** for having a
hover-sized blade, sweeping its cruise efficiency down to 0.85. Its stated reason is in the
source:

> *"blade sized for hover (high disc loading, wrong twist) → **not expected to be better in
> cruise than A's propeller**"*

**A's propeller was used as the standard against which the competitor was penalised, and A's
propeller had never been computed.** That is a self-serving assumption of exactly the kind
this project claims to hunt, sitting in our own source, in writing. (How long it has been
there was not established and is not claimed; what is established is that it is there.)

---

## 7. The limits of this calculation — the strongest one is against the result

1. **Contra-rotating swirl recovery is not credited.** The coaxial pair is modelled as one
   disc carrying 2B blades, because that is the paper's own momentum convention (DL = T/A). A
   real contra-rotating pair does better. **So η_p here is on the conservative side.** This is
   the strongest argument against the finding and its magnitude was not computed; the usual
   credit would move η_p from ~0.65 toward ~0.70 — **not to 0.80.**
2. The blade family is one-parameter: chord fixed from hover, twist offset swept. A fully
   optimised compromise blade might do better, by an amount not computed.
3. Section NACA 0012, NeuralFoil data. Blade count, section and chord distribution were
   **chosen, not measured** — because the paper does not contain them.
4. No compressibility; tip Mach ≤ 0.48 at the crossing points, so it does not bind.
5. Bisection was run to 7 iterations, so FM lands in 0.591–0.603 rather than exactly 0.599.

## 8. And an error this calculation made, caught by its own impossibility

The first version modelled the coaxial pair as **two separate discs each of full area A**,
each producing half the thrust, then read the shaft power against the paper's **single-disc**
ideal. It returned **FM = 1.083**.

A figure of merit cannot exceed one. The pair had been given twice the actuator disc it
physically has. **The number being impossible is what caught it** — no reader did. Corrected
to one disc, 2B blades, full thrust, which is the paper's own sizing convention.

---

## 9. What I am asking of you

**Q1 — Is the architecture-specific penalty defensible, or is it special pleading?** This is
the load-bearing decision and everything in §5 depends on it. A referee can say: *you
penalised yourself and exempted your competitors, and the exemption is what makes your
contract-dependence finding survive.* Our answer is that B's cruise propeller never hovers and
C has the hub we refuse. **Is that answer enough, and is there a case for B or C paying
something too?** Argue against us if you can.

**Q2 — Does the Section 3.6 sentence get rewritten, or does the section get restructured?**
"Leads under one of three" is a weaker illustration of contract-dependence than "two of
three", but the finding is that the ranking *reverses*, not that we win. Is a one-of-three
reversal still a demonstration, or does the section now need a different case to carry the
point?

**Q3 — Where does the variable-pitch cost belong in the v8 skeleton?** It is now a number, and
it is the price of the paper's actual contribution. Step 8 (what it is made of), step 11 (the
ledger), or does it earn a place in step 7 where the elimination is claimed? It is currently
named in step 7 in one paragraph, without the number, pointing forward to Section 11.

**Q4 — Anything false, in the calculation or in what has been written about it.** Including
§7's list: is the swirl-recovery caveat stated at the right strength, or is it being used to
soften a result we should state flatly?

---

## 10. Where this leaves the work

Nothing in the architecture changed. The union, the elimination of the reorientation mechanism
class, the strip, the count — untouched. What changed is that a number the paper asserted for
four versions has been computed and is worse, and a sentence built on it has to go.

The range figures are lower and the author's position is that this costs nothing: the range
claim is against multirotors, and 1262 km is not a number a multirotor approaches. The
project has now found against itself three times — the drag coefficient, the thrust-to-weight
ratio, and this. **This one it found before a referee did, which is what the process is for.**

Target remains *Journal of Aircraft* (AIAA), Full-Length Paper.
