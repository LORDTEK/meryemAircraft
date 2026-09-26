# Round 94 — Step 9 closes. R-3, S-20 and the Step 1 repairs are applied. Two points are still divided in Step 1. Step 5 inventory, with two source findings

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> New in the repository: `paper/v8/drafts/05-inventory.md`. Everything you are asked to vote on is quoted below.

---

## 1. Closed

All four of you confirmed Round 93's applied text: 14D (R-2), Step 9 item 2, and the S-19 sentence.

- **Step 9 is closed** (1 388 → 1 339 words).
- **The version stamp is closed.** ChatGPT's point stands: the count itself (2 on the current file) is not the contract;
  "more than 0" is.
- ChatGPT's two onboarding notes are closed with no change.

---

## 2. Applied — all four of you and I agreed. Please confirm the text

### Step 14C (R-3, S-20, and wording (d))

> ***What has been measured is a fraction of that, and the figures available are of four different kinds.*** *A 24-series
> nickel–cobalt–manganese pack … reached 55.1 °C against the 60 °C limit its authors adopted. A NASA-funded design study
> adopts 4 kW per kilogram and describes that figure as about twice that of existing batteries. The same study notes
> lithium-polymer figures in the literature as high as 3 kW per kilogram, which it cites rather than measures; against
> that figure the take-off demand is 1.8 to 2.0 times. **The study argues that, because a battery's pulse current limit can
> exceed its continuous limit by more than a factor of two, a pack with the required specific power may be possible with
> existing technology; the study's hover lasts twenty seconds or less, and how long this aircraft's vertical phases draw
> the peak is not computed here.** **The take-off demand of Section 10's closures is 3.7 to 4.1 times the bench rate — the
> highest figure obtained from a measurement — and 6.2 to 6.8 times the flown system's continuous rating**; hover alone is
> 3.1 to 3.5 times the bench rate. The comparison is between unlike ratings: a peak demand held through the vertical
> phases, a bench average over minutes, a continuous rating, a design assumption, **and a literature figure the study cites
> without its rating.** …*

- S-20 uses ChatGPT's referents (*"The study argues"*, *"the study's hover"*); the rest of you accepted the sentence without
  them.
- On (d), ChatGPT preferred *"obtained from a measurement"*, and none of the other three objected. Grok and DeepSeek called
  it accurate but not needed; Qwen used the phrase in its own answer.

**Protected (161):** *"The same study notes lithium-polymer figures in the literature as high as 3 kW per kilogram, which it
cites rather than measures"*.

**Evidence record (Grok P55; ChatGPT on (c)).**
- Barrett's "may be possible" is recorded as an *attributed conclusion, not a built pack*.
- 4 kW/kg is recorded as *verified as a design assumption*, never collapsed to "verified".
- The Step 14 trace carries an evidence-status column for every battery figure.
- Qwen P1 is recorded as a trace note: pulse against continuous rating is the mechanism left unposed.

### Step 1

- **1B (S-23):** *"…vectored-thrust and tilt-wing aircraft in the 1960s, **tilt-rotors from the 1950s**, and a broad
  family…"*. See §3.2: the order now reads badly.
- **1D:** the paragraph now ends *"…a choice this configuration declines rather than a limit it inherits (Sections 7 and
  8)."*
  - Removed: *"Precise hovering, ground gusts and the absence of a thrust-borne rolling moment are configuration facts,
    and they are inherited."*
  - **Protected (162):** *"The reaction-torque channel that other coaxial tail-sitters use about that axis is a choice
    this configuration declines rather than a limit it inherits"*.
- **1E:** now opens directly with *"**The route itself is established.**"*
  - Removed: *"It would be easy, and wrong, to present the third route as an empty field. It is not, and the paper is
    better for saying so first."*
  - Qwen P2 checked: *"What follows is therefore"* takes its antecedent from 1F's *"And the third route is occupied."*,
    which is untouched.
- **1E (S-22):**
  > *…fixed-pitch propellers make it "theoretically impossible to be very efficient in both hovering and forward flight."
  > A long-range tail-sitter reported in 2018 **that uses a cyclic- and collective-pitch rotor still describes it** as "a
  > compromise between efficient hover and efficient forward flight" and selects its diameter on that basis; **the same
  > paper names variable pitch as the remedy for fixed-pitch propellers, at the cost of extra actuators and the weight of
  > the mechanism.***
  - The diameter clause is checked against the source: *"A diameter of 1 m was finally selected as a compromise"*.
- **1F (S-21):** *"…audited explicitly against carried hover mass, exposed cruise drag and hover-sized continuous power,
  **the last two of them at two scales,** and under three sizing contracts."*

**Standing rule, now in the project rules (all five):**
> *When a source is opened to verify a figure or a quotation, the paragraph around it and the source's own discussion or
> conclusion on the same quantity are read and recorded in the evidence file. A qualification or contrary figure found
> there is either quoted in the body or recorded as omitted, with the reason.*

The selective-quotation cluster (S-18, S-19, S-20, S-22) is now in the source-defect log with pages (DeepSeek).

**The originals are frozen in Supplements S1 and S14.**
- Six new retired phrases, 93 in all: *"tilt-rotors from the 1980s"*, *"at two scales and under three sizing contracts"*,
  *"selects its diameter on exactly that basis"*, *"configuration facts, and they are inherited"*, *"the highest of the
  measured figures"*, *"of three different kinds"*.
- The nothing-lost check now covers Step 1.
- All checks pass. Protected 162 of 162.

Word counts: Step 1 went 1 679 → 1 667 (the repairs added words), Step 14 is 1 508, and the body is 25 870.

---

## 3. My own checks on what was applied — please answer

**3.1 My reason for removing *"Precise hovering…"* was half wrong.** I wrote that it "names *precise hovering* where the
list names *vertical descent*" — as if the item were wrong. It is not.
- The XFY-1 entry in the NASA review reads *"Difficult to hover precisely over a spot"*.
- The 1984 review reads *"hovering over a given spot and touching down precisely was extremely difficult."*

The removal still stands on the other ground, the third "inherited" in one paragraph. Precise hovering is still named in
the paper, in Step 5E (*"Precise hovering, ground gusts and the descent itself are not disposed of by removing the
pilot"*).

**Question:** should 1D's list of inherited difficulties name precise hovering too? My view: no, because Step 5 carries
it where the landing is discussed. But I misstated the reason, and you voted on my wording.

**3.2 S-23 now reads out of order:** *"1950s …, 1960s, tilt-rotors from the 1950s"*. My proposal:
> *"**Tail-sitting prototypes and the first tilt-rotor flew in the 1950s**, vectored-thrust and tilt-wing aircraft in the
> 1960s, and a broad family of hybrid vertical take-off and landing uncrewed aircraft since roughly 2010."*

This drops "tilt-rotors from", which claimed continuity; the XV-15 (1977) is the next one in the review.

**3.3 S-20's "a battery's pulse current limit can exceed its continuous limit by more than a factor of two"** rests on
**one** module in Barrett: *"For example, a commercially available battery module [61] has a maximum pulse discharge
current more than twice as high as its continuous discharge current."* The general statement Barrett makes is only
*"batteries can have burst (pulse) current limits that are higher than their continuous-current limits."*

"Can … by more than a factor of two" is supported by one example, which is a slight widening that I wrote and none of
us caught. Proposal:
> *"…because pulse current limits can exceed continuous ones — by more than a factor of two in one commercial module it
> cites — …"*

**3.4 Qwen quoted the 1D sentence in a form that is not in the text** (*"…is a separate matter, and it is a choice this
configuration declines…"*). That wording is the older one, now in Supplement S1. I have counted Qwen's vote for the
sentence as it stands, quoted in §2. Qwen, please confirm against that wording.

---

## 4. Two points divided — please answer one another, not only me

**4.1 1B, *"No field sustains that level of effort against a need that is not real."***

| Reader | Vote | Reason |
|---|---|---|
| Grok | keep as voice | an argument from effort; do not tag it verified |
| DeepSeek | keep as voice | it supports the section's tone |
| Qwen | keep as voice | rhetorical framing, not a statistical claim |
| ChatGPT | **remove** | an inference from the amount of activity to the reality of the need; the history already shows the pursuit; *"no reason to spend epistemic capital on it"* |

**My view: narrow it.** The weakness is the universal form — it is a claim about every field, and it is not supported.
The narrowed form is about this record only:
> *"Seventy years of that effort is evidence that the need is real."*

Under our rule, the text stays as it is unless all five agree to a change.
- ChatGPT: do you accept the narrowed form?
- Grok, DeepSeek, Qwen: does ChatGPT's reason move you, and would you accept the narrowed form?

**4.2 1C, *"Hybrid VTOL aircraft occupy that corner today, and several are in service."***

| Reader | Remedy |
|---|---|
| Grok | *"some have entered service"* without a count, or name the type and the review |
| ChatGPT | hold for a source; otherwise remove or rewrite |
| DeepSeek | *"several have been built and flown"* without a source |
| Qwen | *"some are in service"* |

**I found a source in the repository** (Bacchini's dissertation, opened this round):
- *"After many tests and refinements, the V-22 was adopted in 2007 by the United States Air Force, the US Navy, and the US
  Marine Corps. More than 200 V-22 were in service in 2014."* (printed p. 53)
- the Harrier: *"the first operational VTOL attack aircraft"* (p. 49);
- the F-35: *"now in service"* (p. 68).

**All three are crewed.** The paragraph's next sentence turns to the NASA study, whose vehicles are urban air mobility
concepts, so crewed examples do not change what the paragraph is about.

**My proposal:**
> *"Hybrid VTOL aircraft occupy that corner today, and some are in service — the V-22 tilt-rotor among them, adopted in
> 2007."*

Is a crewed example the right witness here? Or does the uncrewed framing of Section 1's first line (*"Uncrewed powered
flight is dominated by…"*) make it the wrong one, in which case DeepSeek's *"built and flown"* is the honest fallback?

---

## 5. New proposals, to vote

| # | Proposal | Who | My vote |
|---|---|---|---|
| a | Protect the S-20 sentence (as finally worded after 3.3) | DeepSeek | yes — the same reason as S-19: removing it silently makes the gap look larger than the source supports |
| b | **Count-consistency step.** When a sentence adds or removes an item from a list, any count or list nearby (*"three kinds"*, *"four parts"*) is re-read before applying. R-3 is the example. | DeepSeek | yes — it is P51's twin: P51 reads the next sentence's pointers, this reads the paragraph's counts |
| c | **Grok P56 as a check.** *"by any combination of thrust settings"* may appear only in Step 1, beside the protected declining sentence. Anywhere else, the check fails. | Grok | yes — the phrase occurs once today, so the check is cheap and it guards the §0.1 limit |

---

## 6. Step 5 inventory — please confirm or correct

Step 5, *The first half: operation without a runway* (assembled Section 3), is 1 213 words, with 4 protected sentences.
Under the new rule, I opened the NASA 1984 review ("In retrospect" paragraph) and the 1981 XFY-1 entry, and read around
each quotation.

| Block | Must say | Restatement candidate |
|---|---|---|
| **5A** Opponent | Fixed wing is the opponent on this axis only; P *"Nothing here is claimed against fixed-wing aircraft on range or cruise efficiency."* | Step 9 item 1 is the second home; Step 9 is closed, with it kept |
| **5B** Requirement | Depart **and recover** with nothing supplied by the site; a catapult fails the recovery half | — |
| **5C** How it is met | Five-point stance, no launch equipment; tip frames serve four purposes, charged once; P *"The saving has precedent…"*; the stance base is a parameter | — |
| **5D** Sized / not demonstrated | Sized: hover power, buffer, tip frames, landing structure. Not demonstrated, five items: take-off on the control propellers; the descent (vortex ring); the landing transition, which is not the outbound reversed; closed-loop hover control, with the declined channel's cost not computed; crosswind on the ground. P ×2 | *"This is the part of the section that decides whether the rest of it can be trusted"* is a signpost → weak candidate. The crosswind item is the third statement of ground-wind exposure, but *"a parameter rather than a proof"* adds a limit → keep |
| **5E** Record | Only the pilot's orientation is removed; precise hovering, ground gusts and the descent are not | *"That disposes of the spatial-orientation objection and nothing else"* restates Step 1's protected sentence. But it is where Step 1's 1954 material landed in Round 64, and after this round 5E is the paper's only mention of precise hovering → keep |
| **5F** Costs | Tip-frame drag, unfeatherable propellers, buffer mass: all charged later | pointers only |

The 5D sentence *"What that refusal costs in authority and in response time is not computed"* is **not protected.** It is
the limit that must travel with the declined channel wherever it appears. Should it be protected, as the 1D sentence now
is?

**Two source findings (S), to vote. Neither has been applied.**

- **S-24 (5C) — the rule's first catch in a new block.** The body quotes *"dispensing with a conventional landing gear
  improved the empty weight fraction for these VATOL aircraft"* and the note that *"some form of gear was required on the
  vertical and horizontal tail surfaces."* The review's next sentence is not quoted:
  > *"Not only were these landing gears limited to relatively low allowable sink rates, but … tip-over tendencies were a
  > constant worry in gusty air and on uneven ground, particularly with the propellers turning."*
  - The section's own requirement is an **unprepared** site, and uneven ground is not in 5D's list.
  - My proposal: in 5C, *"…while noting that some form of gear was still required on the tail surfaces, **that such gear
    was limited to low sink rates, and that tip-over was 'a constant worry in gusty air and on uneven ground, particularly
    with the propellers turning.'**"* In 5D's inherited item: *"A tail-sitting aircraft on the ground is more exposed to
    crosswind **and to uneven ground** than a conventional one."*
- **S-25 (5E).** *"The XFY-1's landing difficulty was attributed to a pilot judging a backwards vertical descent by
  looking over his shoulder, to turbulence sensitivity and to reduced control power near touchdown."*
  - The review gives these three causes for *"these tail-sitter designs"*.
  - The XFY-1's own entry lists gust sensitivity and reduced control power in ground effect, but not the over-the-shoulder
    view.
  - My proposal: *"**The landing difficulty of the 1950s tail-sitters** was attributed to…"*.

---

## 7. What I am asking

1. Confirm §2's applied text.
2. §3: answer 3.1 (should precise hovering be in 1D?), 3.2 (the 1B order), 3.3 (the S-20 widening), and 3.4 (Qwen only).
3. §4: answer one another on 4.1 and 4.2.
4. §5 (a) to (c).
5. §6: confirm or correct the Step 5 inventory. Vote on the weak 5D candidate, on protecting the 5D "not computed"
   sentence, and on S-24 and S-25.
6. Your own proposals, of any kind, with reasons.

Step 6 follows, once Step 5's inventory is confirmed.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
