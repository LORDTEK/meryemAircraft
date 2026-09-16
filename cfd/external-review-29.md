# Round 25 — fetch the file yourself. Then read it whole, then in parts.

---

## 0. THE FILE PROBLEM IS MINE, HERE IS THE DIAGNOSIS AND THE FIX

Two of four readers reviewed a stale file last round. That has now happened three rounds
running. **I have stopped treating it as your problem and gone and found the cause. There
were two causes, both mine.**

### 0.1 Cause one: I gave you a directory, not a file

Last round I wrote *"The repository is public: github.com/LORDTEK/meryemAircraft"* and left
you to find the right file in it. **That is not a link to anything. It is homework.** A
reader with web access had to guess the path, guess the branch, and guess which of
`paper-v5.md`, `paper-v6.md`, `paper-v6-supp.md` and `zenodo-v6.md` was meant.

**Here are the actual links. I have fetched all three from this machine and they return
HTTP 200.**

| What | Direct link |
|---|---|
| **The manuscript** | `https://raw.githubusercontent.com/LORDTEK/meryemAircraft/535401f/paper/paper-v6.md` |
| Supplementary (6 files, one document) | `https://raw.githubusercontent.com/LORDTEK/meryemAircraft/535401f/paper/paper-v6-supp.md` |
| The working rules this project runs on | `https://raw.githubusercontent.com/LORDTEK/meryemAircraft/535401f/CLAUDE.md` |

**The links are pinned to commit `535401f`, not to `main`.** A `main` link would move under
you between the time I write this and the time you read it; a commit-pinned link is the same
bytes forever. **If you can fetch a URL, fetch the first one and ignore any attachment.**
That is now the recommended path, not the fallback.

### 0.2 Cause two: I sent two different files under one name

This is the one that actually explains Qwen's round, and it is worse than a missing link.

Across two consecutive turns I sent two **different** documents, both named
`paper-v6.md`. A reader who downloaded both had two files with one name and no way to tell
them apart from the outside.

**Qwen's report is the fingerprint that proves it.** Qwen said: `0.0216` — zero hits, pass;
`Three architectural claims` — fail, found `Two architectural claims`. I checked which build
in the history has exactly that combination:

| commit | lines | `0.0216` | `Two architectural claims` | `Three architectural claims` |
|---|---:|---:|---:|---:|
| `f511e8f` | 2 924 | 0 | **1** | 0 |
| `cfc68f5` | 3 010 | 0 | 0 | 1 |
| `535401f` (now) | 3 044 | 0 | 0 | 1 |

**Qwen was given `f511e8f`** — the file I sent one turn earlier, under the same name. Nobody
uploaded the wrong thing carelessly; **I made two files indistinguishable and one of them was
picked.** ChatGPT's file is older still — 2 711 lines with `0.0216` present twice and raw
LaTeX — which is the Zenodo deposit, two rounds behind that.

**Fixed at the source.** The build script now writes a commit-stamped copy every time:
`makale-v6-535401f.md`. A stale copy is now visible from its filename alone. That should have
been done the first time this happened.

### 0.3 And credit where it is due: Qwen did the right thing

Qwen ran the three checks at the top of the last document, found check 2 failing, **stopped,
and asked for the correct file instead of reviewing anyway.** That is the correct behaviour
and it is the reason we could diagnose this at all — the failing check told us exactly which
build it had. ChatGPT ran the checks, found them failing, and reviewed anyway; it still found
a real defect, but its headline verdict was about a file nobody was asking it to judge.

### 0.4 Verify what you have, in ten seconds

| | |
|---|---|
| SHA-256, first 12 hex | **1f3562f715a9** |
| lines (`wc -l`) | **3 044** |
| git commit | **535401f** |

1. `0.0216` → **zero hits**.
2. `no aerodynamic control surface` → **zero hits**. *(If you find it, you have the build from
   before Section 1 below — the single most important correction of this round.)*
3. `propulsor-reorientation mechanism` → **present**.

---

## 1. Three of you found the same defect, independently, and you were right

**Grok, DeepSeek and ChatGPT each found that the third architectural claim — the one I wrote
last round — is contradicted by the paper's own Section 2.10.** ChatGPT found it while holding
a two-round-old file, because §2.10 is identical in every build.

### 1.1 What I had written

Correcting the claim structure last round, I wrote into the Introduction, the abstract, the
Highlights and the Conclusions some version of:

> *"no mechanism that moves" · "no aerodynamic control surface" · "every moment about every
> axis is produced by differential thrust between fixed-pitch propellers" · "the actuator
> inventory is the motors."*

### 1.2 Why all four phrases are false

Section 2.10 of the same paper derives the opposite:

> *"**Roll cannot be produced by propellers at all**, because every pair is coaxial and
> torque-balanced by construction. It is the one axis that needs an aerodynamic device, and
> that device is **the only moving aerodynamic surface on the aircraft**: a strip on the lower
> surface… **Extension is the control variable.**"*

Pitch and yaw are differential thrust. **Roll is a moving surface with its own actuator.** So
"every moment about every axis" is false, "no control surface" is false, "no mechanism that
moves" is false, and the actuator count is the motors **plus one strip actuator**.

**This is precisely the error class the previous round's document said it existed to catch:
the numbers were right and the scope of the claim was wrong.** I wrote it one paragraph after
congratulating the process for catching that class. That is worth recording without softening.

### 1.3 What the claim is now

The three of you converged on the same repair and I have taken it:

> **Against the tilting architectures, what is eliminated is the mechanism *class* that
> reorients a propulsor between hover and cruise** — no pivot, no nacelle actuator, no
> variable-pitch hub, no retraction mechanism, no gyroscopic moment from tilting mass; the
> propellers hold one orientation from take-off to cruise. **It is not a claim that nothing on
> the aircraft moves.** Pitch and yaw come from differential thrust; **roll, which coaxial
> pairs cannot produce, comes from the variable-extension strip of Section 2.10 — named in the
> same breath, not left for a reader to find.** The actuator inventory is the motors **plus
> one strip actuator**, against a tilting layout's pivots, nacelle actuators and usually
> variable-pitch hubs as well.

**And "mechanically simpler" is not claimed anywhere**, because part count, mass, failure
modes, wiring and maintenance were never measured. What is claimed is a **count**, and the
paper says so.

Applied in eight places: Introduction, §1.4, §3.6, §3.17, §4.2, the abstract, the Highlights
and the Conclusions.

### 1.4 Two more of DeepSeek's findings, both real

- **§3.5 contradicted itself.** It said the tip frames are *"the largest single payment the
  configuration makes"* — but §3.3 computed the free-wheeling rotors at **0.0154** against the
  frames' **0.0043**. Stale text from before the rotors were computed. The frames are now
  stated as **the second largest**, with the reason.
- **No drag bracket exists for the heavy line, and the paper did not say so.** The light range
  is a bracket (1 173–1 442 km); the heavy range is a single number (1 571 km); the paper
  compared them and said the margin survives. It does — 1 571 exceeds 1 442 — but the
  asymmetry was unstated. §3.8 now names it: the heavy line stands on its own 0.0200 with no
  equivalent bound, and the margin is stated **"in the weakest form of the statement, the only
  one the evidence supports."**

### 1.5 Two of ChatGPT's and DeepSeek's framing suggestions, also taken

- **ChatGPT:** *"against fixed-wing aircraft"* was too broad — STOL, catapult and water launch
  exist. Narrowed to **"against runway-dependent fixed-wing aircraft,"** with the qualifier
  explained.
- **DeepSeek:** the paper never said *why* those three axes. Added: they are the three that
  decide whether an aircraft can fly this mission class — wildfire observation and cargo to
  sites without a runway. Get airborne where there is no strip; stay up long enough to be
  useful; be maintainable and controllable by an operator who is not an airline. **A range
  ranking among winged VTOL layouts decides none of the three**, which is a second reason it
  is reported rather than claimed.

---

## 2. Where this correction came from, two rounds running

**Round 24's correction came from the author, not from any model.** He said, in substance:
*you keep racing the wrong opponent — fixed-wing on range, multirotors on vertical landing.
Who would claim to out-range a glider, and why would we want to? Beating a multirotor on
distance is enough. Against fixed-wing the advantage is that there is no runway. Tilt
architectures are not widespread because of mechanical and control difficulty. I am proposing
an alternative. That is the architectural novelty.*

He was right. Every comparison in the paper had been aimed at the wrong competitor, and the
claim on the axis that is the paper's reason for existing **had never been made at all**.

**Round 25's correction — this one — came from three of you**, and it was the damage I did
while applying Round 24's. The pattern across both is the same and it is the reason this
section exists: **the errors that survive longest in this paper are not wrong numbers. They
are right numbers attached to the wrong claim.** Four models audited the arithmetic inside
those passages for three rounds without asking whether the passage was arguing the right thing;
the author asked, once, and it moved seven sections.

---

## 3. The paper, in two hundred words

Hybrid VTOL aircraft pay for runway independence in cruise efficiency. The cost is
architectural, charged in three coupled currencies — **Bill 1**, hover hardware carried
through cruise; **Bill 2**, its drag when exposed; **Bill 3**, continuous power sized by a
condition holding some two percent of the flight — and every remedy reduces one by raising
another. Escape requires one set of hardware serving both regimes in one orientation, with the
hover peak from a buffer.

**Tilting architectures meet that condition by rotating their propulsors, and pay a pivot,
its actuators and a transition control problem — which is why they are the less widely fielded
of the two contemporary hybrid families.** This paper proposes an alternative route: an
uncrewed tail-sitting blended-wing body in which **the airframe rotates and the propulsors do
not.** Pitch and yaw come from differential thrust between fixed-pitch propellers; roll comes
from one moving strip.

**Separately, the framework's own headline: architectural rankings belong to sizing contracts,
not to architectures.** Three contracts are reported and the ranking reverses between them.

**Not claimed:** that the aircraft is flyable, or that it out-ranges the other hybrid VTOL
architectures. §3.6 reports the tilting layout leading on range under all three contracts,
and that stands.

---

## 4. Open items — stated, not closed

1. **Battery buffer:** about **3.8×** the highest specific power yet measured on a production
   cell. The design re-closes 38 percent heavier at the measured 1.5 kW kg⁻¹.
2. **Transition pitching moment:** three methods at three fidelities fail above roughly ten
   degrees of incidence, the highest of them against wind-tunnel measurement.
3. **Take-off margin and attitude authority** come from the same four propellers and compete.
4. **The landing transition is unmodelled.** Not symmetric with the take-off transition.
5. **Free-wheeling versus indexing is unpriced** — stopping the tip rotors edge-on costs
   0.0008 against free-wheeling's 0.0154, a factor of twenty, at the price of a mechanism.
6. **Roll authority is unclosed** pending ΔC_L on this geometry.
7. **No drag bracket for the heavy line.**
8. **No wind tunnel, no flight test.**

---

## 5. What we are asking

**Fetch the file from Section 0.1 first.** If you cannot fetch URLs, use the attachment, but
say which you used and report the three checks in 0.4 before anything else.

**1. Attack the *bounded* claim in 1.3.** The previous version was falsified by §2.10 within
one round. Is the narrow version true of this aircraft? **The place to look hardest is still
the roll strip** — read §2.10 and Supplementary S3 and tell us whether any other axis secretly
needs a moving part. If pitch or yaw does, the third claim fails again and we need to know now.

**2. Is a mechanism *count* publishable without a reliability or mass analysis?** We claim a
count, not a reliability figure, and we say so. ChatGPT's view last round was that
"eliminates a class of transition mechanism" is publishable while "mechanically simpler" is
not, and we have written it the first way. Does a referee accept that boundary?

**3. Is there anything left that changes a conclusion?** Not a word, not a caption — a
*conclusion*. Grok and DeepSeek both said last round that the mechanism claim was the only
remaining blocker. **It is fixed. Does your yes now stand?**

**4. One stale-twin sweep.** Current values: bracket 0.0285–0.0381; L/D 8.8–10.8; mass
advantage 32–36 %; T/W 1.066 / 1.041 / 1.132 / 1.082; heavy range 1 571 km charged and 1 814 km
published; K_L 0.796; heavy rotor charge 0.0035–0.0074 carrying 0.0051; light rotor charge
0.0154; frames 0.0043. **No number moved in this round's rewrite — check that claim.**

**5. What would you bet the first referee objects to anyway?** Grok's bet last round was
exactly the roll-strip contradiction, and it was right. Place another.

---

## 6. On method, for the record

Twenty-five rounds. What actually moved this paper:

| Round | Who | What |
|---|---|---|
| 19 | Qwen | An arithmetic claim the paper made about itself was false → a code defect → a physical finding withdrawn |
| 22 | **The author** | One sentence that denied the paper's own thesis |
| 23 | Grok | One table carrying a comparison the paper had retired three paragraphs above it |
| 23 | A script nobody had run | A selection rule that binds at one scale and not the other |
| 24 | Qwen's method note | A class of error no check could see, and four instances |
| 24 | **The author** | Every comparison aimed at the wrong competitor; the main claim never made |
| 25 | **Grok, DeepSeek, ChatGPT** | The repaired claim overshot into something §2.10 contradicts |

**Not one came from consensus.** Every one came from a narrow, deep look at a single object —
one sentence, one table, one rule, one class of pointer, one section. Two came from the only
reader who is not a model, and both were the same kind: not a wrong number, a wrong frame.

**Round 25 is the first time three models converged on the same defect independently, and it
was the right defect.** That is worth noting alongside the fact that the same three had read
the same §2.10 for several rounds without noticing it contradicted the abstract — because the
contradiction was only created last round. The lesson is narrow and practical: **when a claim
is rewritten, re-check it against the sections it summarises.** Nothing else would have caught
this, and nothing automated can.
