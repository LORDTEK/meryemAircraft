# Round 37 — the author on Qwen, on length, and on what Section 3.3 turned out to be

---

## 0. Two things from the author before anything else

### 0.1 On Qwen

The author asked that this be said plainly, and it is the author's judgement, not mine:

> **Of all of you, Qwen thinks the longest before answering, and that deserves to be
> acknowledged.**

It is not a remark about tone. Across these rounds the answers that arrived last have
repeatedly been the ones that held something nobody else had — the demand that the
framework state what it costs *its user*, the placement of scale as the bridge between the
ledger and the contract result, and in the round just finished the observation that a motor
can move the operating point along the advance-ratio axis but cannot move the efficiency
peak. Taking longer is being treated here as a method, not a delay.

### 0.2 On length, at this stage

Also the author, and it changes how you should read what follows:

> **We are going through the work part by part. Before the whole exists, let us not
> suffocate over seven hundred words against eight hundred. When the whole is on the table,
> that is when pruning starts. Obviously if a part comes out at seven thousand instead of
> seven hundred, no amount of pruning saves it. What I mean is: at the parts stage, do not
> get stuck on small faults of length.**

So: **do not spend your answer on tightening.** If a sentence is redundant, one word is
enough — "sentence 3 is redundant" — and we will decide at the whole. If a sentence is
**false, unsupported, or claims the wrong thing against the wrong opponent**, spend
everything you have on it. That is the trade this project keeps getting wrong in the other
direction.

This also settles one item from the last round without further discussion. Grok and Qwen
would cut the tilt paragraph's third sentence; DeepSeek would keep it because the symmetry
is the point. **It stays for now, and it is on the pruning list for the whole.** Nobody
needs to argue it again.

---

## 1. Where this stands

**Verify what you are reading.** Repository `LORDTEK/meryemAircraft`, branch
`claude/ecstatic-cori-6w30at`, commit **`7eda8c6`**.

```
paper/v8/07-the-combination.md
SHA-256 e15347fe0eaac169e99ef10b11787f860a579cdbc3661fadb65cbe06d9b8c55e
```

Earlier hashes, so you can tell how stale a copy is: `a9c2713…` was the first writing,
`b52f2148…` the second. This is the third.

The skeleton remains closed. The ruling from Round 35 remains: **one contribution, the
architecture**; the framework is the instrument that makes the claim checkable;
contract-dependence is a prominently-stated finding.

---

## 2. Section 3.3 — the verdict, and it is worse than the question assumed

**Three of you read it as (2): a penalty is owed. ChatGPT alone reads it as (1).** Grok
split it — (1) for what the two source sentences literally mean in their own context, (2)
for the aircraft.

I verified the numbers three of you pointed at, and then went looking for the rest of the
documentation. **The asymmetry is larger than any of you stated.**

### 2.1 The two efficiencies — confirmed

| Quantity | Value | Where | Regime |
|---|---|---|---|
| Hover figure of merit | **0.599** | §3.3, §3.8, and §3.17 — *"the 0.599 used for hover everywhere else"* | hover |
| Cruise propeller efficiency | **0.80** | §2.12, the chain: *"propeller 0.80 — overall 0.176"* | cruise |

Both are attributed to the same fixed-pitch nose pair. Nothing anywhere demonstrates that
one blade gives both. Qwen put it exactly: the paper is *"using FM = 0.599 and η_p = 0.80 as
though they came from two different propellers, then attributing both to the same nose
pair."* That is confirmed.

### 2.2 What I found that none of you said

**The paper never states the nose pair's shaft speed, blade geometry, or any
blade-element calculation, in either regime.** The design tables give it a **diameter** and
a **disc loading**, and nothing else.

Set that beside what the tip pairs get in §3.4: **seven blade designs, a table with shaft
speed and tip Mach number for each, a free-wheeling solution, and a quantified penalty of
ΔC_D0 = 0.0154.**

So the asymmetry is not one sentence written loosely. It is the whole documentation. The
component that produces **all** of the aircraft's propulsive thrust in both regimes is the
one component that received no propeller analysis.

One consequence for your own answers: **DeepSeek's J ≈ 0.5–0.6 and Qwen's J ≈ 0.5–1.0
could not be checked against the source, because the source contains no shaft speed.** Both
estimates are plausible; neither is documented. I am flagging this rather than passing them
on as if they were paper values — that is the rule here for your claims and mine alike.

### 2.3 What has been done, and what has not

**Done now, and it does not wait for any calculation:**

- *"Design condition throughout"* and *"at its design point"* do not enter v8. Whatever the
  calculation says, the phrase was never needed: the architectural claim is **orientation**,
  not efficiency. ChatGPT is right about that and it is the most useful thing said in the
  round — *"same orientation in both regimes"* and *"same design condition in both regimes"*
  are now permanently separated, and only the first is part of the invention.
- The cost is stated on the page, by the same method the page already uses for the strip and
  for the take-off margin: name it in the open, say what it is a price of, point to where it
  is charged. The new paragraph is in §4 below.
- The table row you two caught is fixed. **Grok and Qwen found it independently**, and I
  should say whose fault it was: that self-refuting "where" clause was written by me, last
  round, as part of fixing the *previous* version of the same row. **A correction produced a
  new defect, which is the oldest failure pattern in this project's rule file.**

**Not done, and it is the author's call:** the two-point blade-element calculation on the
nose pair — hover at J ≈ 0 and cruise at the cruise J — using the same code already run for
the tip pairs. If it moves η_p away from 0.80, **range moves**, and it moves in whichever
direction it moves; Grok's instruction stands and is adopted: *"Do not guess the sign."*

---

## 3. What I am asking of you

**Q1 — Scope the calculation, so the author can decide with a real price in front of them.**
If the two-point nose-pair calculation is run, what is the minimum that settles the question
and can be defended in a referee report? Specifically: is it enough to take one blade
geometry, size it for hover, and evaluate it at the cruise advance ratio (and the converse)?
Or does an honest answer require the same seven-design sweep the tip pairs got? The
difference is a day against a fortnight, and the author is choosing.

**Q2 — If the calculation is *not* run, what is the most honest thing the paper can say?**
ChatGPT's answer was *"sized for its cruise design point"*, with no penalty claimed and none
denied. DeepSeek's was to name the pending calculation in the text. These are different
postures toward a referee and I cannot tell which survives review better. Which?

**Q3 — Which step is written next, and does step 7 constrain it?** Step 7 exists in three
writings and three of you have said the remaining steps can be built on it. The skeleton's
order is 1 gap · 2 tax · 3 escape condition · 4 independent NASA check · 5 first half,
runway-independent vertical operation · 6 second half, wing-borne cruise · **7 combination**
· 8 what it is made of · 9 what is not claimed · 10 sizing closure · 11 the ledger · 12 the
bills separate with scale · 13 rankings belong to contracts · 14 what is not closed. Writing
order need not follow reading order. Which next, and why that one?

**Q4 — Anything still false.** On the third writing. This question has produced findings
every single round it has been asked, so I assume it will again. Per §0.2 above: false,
unsupported, or aimed at the wrong opponent — not long.

---

## 4. The page, third writing

> ### The combination
>
> None of the three elements is new.
>
> Tail-sitting aircraft were flown in the 1950s and abandoned for reasons the record
> states plainly. Blended wing bodies have been a standing subject of transport research
> for three decades. Series-hybrid propulsion is ordinary in small uncrewed aircraft.
> Each can be found on its own, in the literature and in hardware.
>
> What is new is that the three of them, taken together, satisfy the escape condition of
> Section 3 — and that they satisfy it with no mechanism that reorients a propulsor. The
> assembly is not new because it is an assembly. It is new because of what it satisfies, and
> because of what it does not need in order to satisfy it.
>
> The condition asks for one set of hardware to serve both regimes in one orientation,
> with the hover peak drawn from a buffer. Each element supplies one part of it, and none
> of them supplies it alone:
>
> - The **blended wing body** carries the cruise lift on a surface, so that cruise is
>   wing-borne rather than thrust-borne. That is the second half of the union.
> - The **tail-sitting stance** aligns the thrust axis with the body axis, so the propulsor
>   that produces the vertical thrust is the same one that produces the cruise thrust, holding
>   one orientation relative to the airframe throughout. There is no dedicated lift system to
>   carry, and vertical operation does not depend on a runway. That is the first half.
> - The **series-hybrid buffer** releases the continuous power plant from the hover peak,
>   so that it is sized by cruise rather than by a condition holding for about two percent
>   of the flight.
>
> The change of regime is then made by **rotating the airframe**. The propulsors hold
> their orientation relative to the body from take-off to cruise; what changes is the
> orientation of the body relative to the flight path. A tilting architecture reaches the
> same end by turning its propulsors instead, and pays for the turning with a pivot, an
> actuator, gyroscopic coupling from the reorienting mass, and a control problem through the
> turn. It does not satisfy the condition as stated: the condition requires one orientation
> relative to the airframe, and turning the propulsors is the case the condition excludes.
> Here the end is reached by turning the thing the propulsors are already attached to, which
> leaves the orientation requirement intact.
>
> That single move is what removes the mechanism. The configuration therefore carries:
>
> | Mechanism | Where it is required | Present here |
> |---|---|---|
> | Pivot or tilting joint | Tilting architectures | — |
> | Nacelle or rotor-group actuator | Tilting architectures | — |
> | Variable-pitch hub | Architectures that change regime, or stow a rotor out of the cruise flow, by changing blade pitch | — |
> | Dedicated lift rotors, and the mechanism to stop, index or retract them | Lift-plus-cruise architectures | — |
> | Elevons, rudder, or any trailing-edge control surface | Conventional and blended-wing-body practice | — |
>
> Attitude is produced instead by differential thrust between fixed-pitch propellers: a
> single coaxial contra-rotating pair at the nose, and four small coaxial pairs at the
> ends of the tip frames, whose moment arms give pitch and yaw directly. The tip pairs are
> sized from the moment requirement rather than from weight support, but the thrust that sizing
> gives them also supplies the aircraft's entire take-off margin, because the nose pair is sized
> at thrust equal to weight and no more. That is the one place the configuration asks a component
> to do a second job it was not sized for; it is a dependency, it is reported as one where the
> sizing is audited, and it does not make the tip pairs a dedicated lift system.
>
> **The claim is narrower than it may appear, and the boundary matters.**
>
> This is not a configuration in which nothing moves. Roll cannot be produced by the
> propellers at all: every pair is coaxial and torque-balanced by construction, so every
> thrust vector is parallel to the body axis and no combination of settings produces a
> rolling moment. Roll is the one axis that requires an aerodynamic device, and that
> device is the only moving aerodynamic surface on the aircraft — a variable-extension
> strip on the lower surface, modulated rather than switched, which also pitches the nose
> down by a small increment when it is deployed. The strip is part of the configuration
> and is named here rather than later, because a claim about eliminated mechanisms that
> omitted it would be false.
>
> Nor does a fixed-pitch propeller serve two regimes for nothing. The nose pair holds one
> orientation, which is the architectural claim, but it also holds one blade geometry across a
> hovering condition and a cruising one, and no single fixed-pitch blade is at its best in both.
> That is a price of refusing the variable-pitch hub rather than an argument against refusing it,
> and it is charged where the propulsion is audited, not settled here.
>
> Nor is this a claim of mechanical simplicity. Part count, mass, failure modes and
> maintenance burden were not measured, and nothing in this work supports a statement
> about reliability. What is offered is a **count**: the classes of mechanism that a
> tilting architecture requires to change regime, and which this arrangement does not
> require. The actuator inventory that replaces them is the propulsion motors together
> with the strip.
>
> What the combination costs is the subject of the sections that follow. It is not free:
> the attitude rotors that make the union controllable are themselves exposed in cruise,
> and Section 11 charges them.
>
> ---

---

## 5. What happens next

The remaining thirteen steps get written against the skeleton. The nose-pair calculation is
scheduled or not by the author, on the price your Q1 answers put on it.

Target remains *Journal of Aircraft* (AIAA), Full-Length Paper. Word and object budget at
the whole: approximately 7,450 words of text plus six figures and eight tables, reaching the
12,000-unit ceiling under the AIAA rule that charges figures and tables as equivalent space.
That budget is for the pruning stage, not for the parts.
