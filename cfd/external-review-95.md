# Round 91 — E1 and the S-18 protection are applied. Step 9 has one removal applied; the second agreed removal would have broken a reference, so it comes back as a rewrite. The Step 14 inventory. A new onboarding text, and an error in the old one

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`b8dc24d`**.
>
> New or changed this round:
> - `paper/v8/drafts/14-inventory.md`
> - `cfd/reader-onboarding.md` (rewritten)
> - `paper/v8-source-defects.md`

---

## 0. The onboarding text is rewritten, and the old one had the contract results reversed

The author asked for a text that a reader can start from in a new conversation, if a conversation fills up. The old
`cfd/reader-onboarding.md` was from Round 61 and was sent to all of you in Round 64. **I rewrote it**, and in doing so I
checked every number in it against the steps. **The old text stated Step 13's contract results in the reverse direction:**

| | The old onboarding (Round 61) | Step 13, which is correct |
|---|---|---|
| The claim | *"this configuration's range is +55 to +84 %, +28 to +54 % and −13 to +7 % under the three"* | *"Against this configuration **the lift-plus-cruise layout** is 55 to 84 percent ahead under the first contract … 28 to 54 percent under the second … and between 13 percent short and 7 percent ahead under the third."* |

**This was my error, and it went to all of you in Round 64.** If any of your answers since then relied on that sentence,
the direction was wrong. The steps themselves were always correct.

**Please check the new onboarding, especially §2 and §3, against the steps.** It is a summary, and summaries are where this
project makes the most errors. From now on its §6 (*Where the work stands*) is rewritten every round.

---

## 1. Applied — please confirm

All four of you and I agreed to each change below.

- **E1 (2E).** *"They are three distinct accounting quantities, **paid in** kilograms, drag counts and installed kilowatts,
  and they are not assumed to be independent physical causes…"*
  - ChatGPT: *"my previous veto was based on having mentally substituted the proposed wording into the current draft. That
    was my reading error."*
- **S-18 is protected, as one unit** (ChatGPT). The protected list is now at **159**:
  > The same work finds the retraction's advantage elsewhere — the speed that maximises range rose by 5 m/s — which is a
  > performance this accounting does not price.
- **Step 9, item 1.** The axis-assignment sentence is removed.

| | |
|---|---|
| Now | ***1. It does not claim range against fixed-wing aircraft.** A runway-launched aircraft that never claimed vertical capability pays none of the charges of Section 2, and nothing here competes with it on distance.* |
| Removed | *The vertical axis is where the fixed-wing family is the opponent; the range axis is not.* |

The original paragraph is frozen in a new **Supplement S9**. The nothing-lost check now covers Step 9. All checks pass.

---

## 2. Step 9, item 4: the removal we agreed would break a reference

We agreed to remove *"What is offered is a **count** of mechanism classes…"* (all four of you and I). Before applying it, I
read the paragraph as it would stand afterwards:

> ***4. It does not claim mechanical simplicity.** Part count, assembly mass, failure modes and maintenance burden were not
> measured, and nothing here supports a statement about reliability. **A count is not a reliability argument**, and readers
> who convert one into the other are not quoting this paper.*

**"A count" would now point to the "Part count" of the first sentence.** The paragraph would then say that part count is not
a reliability argument, which is not what it means. This is the first defect in the whole pilot whose **origin is the
recomposition (R)**. It was caught before it was applied, and it is recorded as **R-1** in the source-defect log. **Nothing
was applied.**

**Proposed (R), replacing the two sentences:**

> *…nothing here supports a statement about reliability. **The count of mechanism classes in Section 7 is not a reliability
> argument**, and readers who convert one into the other are not quoting this paper.*

**My position: yes.** It keeps the denial, and it puts back the reference that the deleted sentence carried.

**And one symmetric item.** Item 2 ends with *"The multirotor family is the opponent on cruise efficiency only."* That
repeats the table's axis assignment in the same way item 1's removed sentence did. **I propose removing it too**, which
leaves *"That comparison runs the other way and would be absurd."*

**The 9F precedent list is kept.** ChatGPT, DeepSeek and Qwen said keep; Grok said drop; my own view was a weak "drop". The
inventory now names its job: *"it makes the precedent denial concrete at the boundary"*. **Grok**, the other three argue that
Step 9's list does a different job from Step 1's: Step 1 builds the gap, and Step 9 limits the paper's own novelty claim.
Does that persuade you? If it does not, the list stays anyway, because removing it needs all four of you.

**Additions you asked for, now written into the Step 9 inventory:**

- 9B: the fourth row is a **refusal, not a finding**. Step 13 is the home of the full contract finding, and Step 9 carries
  only the summary. Whenever Step 13 changes, Step 9 is re-read against it (DeepSeek, ChatGPT, Qwen).
- 9C: the mechanism claim and the regime-change claim stay **two sentences** (Grok).
- Evidence status is attached only where a sentence has an evidentiary origin (ChatGPT).

---

## 3. The Step 14 inventory — please confirm it, or add rows

Step 14, *What does not close*, has 1 502 words and **9 protected sentences**. Following Qwen P2, the first row keeps
**scope** (Step 9) and **debt** (Step 14) apart.

**The battery numbers are verified this round.** I opened `references/Yu-2025_24S-NCM-battery-eVTOL-IN-FLIGHT_Batteries.pdf`
and found each of the following in it:

- 10.68C;
- 55.1 °C, with a 4.9 °C margin to 60 °C;
- *"724 W/kg (110 A) · 892 W/kg (440 A)"*.

The figure *"about 1.5 kW per kilogram for about four minutes"* is **derived** from that source's current and pack mass. The
NASA design study's 4 kW/kg is **attributed** here; I did not open it this round, and I will before 14C is drafted.

| Block | Must say | Evidence (status) | Must qualify (P) | Must not say | Restatement: of what, and status |
|---|---|---|---|---|---|
| **14A Scope vs debt** (Qwen P2: first row) | This section is the **debt** — questions not answered that better evidence would answer; Step 9 is the **scope**. Known obstacle first, then the unknown | — | **P** *"for the first item the answer is no"* | that the list is a list of claims declined (that is Step 9) | first |
| **14B The store: demand** | Closures ask 4.7–5.2 kW/kg (hover) and 5.5–6.1 (take-off) of the buffer at the bus | model-derived (Section 10 closures) | the buffer's 3.6 % is an **input** | — | first |
| **14C The store: what is measured** | Three kinds of figure: flown system 0.892 kW/kg continuous; unit pack at 10.68C ≈ 1.5 kW/kg for ~4 min, 55.1 °C vs 60 °C; design-study 4 kW/kg; take-off demand 3.7–4.1 × bench rate, 6.2–6.8 × flown continuous | **verified** in `references/Yu-2025_24S-NCM-battery-eVTOL-IN-FLIGHT_Batteries.pdf` (10.68C; 55.1 °C with a 4.9 °C margin; 892 and 724 W/kg); ≈1.5 kW/kg **model-derived** from that source's current and pack mass; 4 kW/kg study **attributed, not reopened** | **P** *"The comparison is between unlike ratings"*; **P** *"The gap is real on every one of them; the factor quoted is peak demand against bench average."*; **P** *"The package Section 10 closes on does not exist with any store the sources consulted here report as built."* | that a store is impossible | first |
| **14D Re-closure on a measured store** | The table; a sensitivity of the package, not a second aircraft | model-derived | **P** *"These masses are the Section 10 package with one input changed."*; **P** *"They are not a structural closure at 100 kg"* | a 100 kg design | The prose after the table (*"At the bench rate the loop closes about three-quarters heavier, with a buffer of about fourteen percent…"*) **restates the table's third row** → candidate removable in part (keep the 7 kg payload alternative and the two continuous-rating readings, which the table does not say) |
| **14E Where the coupling is paid** | The buffer is the conversion the condition permits (kW of hover peak paid in kg of store); the escape from Bill 3 is real in Section 3's sense and its price depends on an undemonstrated component | — | *"The escape from Bill 3 is real in the sense Section 3 defined it, and its price depends on a component whose required performance has not been demonstrated"* — **not yet protected**; proposed for protection (Round 91) | that Bill 3 is escaped for free | *"at a measured specific power it costs thirteen to fifteen percent of take-off mass instead of 3.6"* is the **third** statement of the 13.4–14.7 % → candidate removable |
| **14F What it reaches** | It reaches every number at Section 10's masses (masses, payload, ranges, the vertical phase, Section 13's orderings); it does not reach the mechanism claim, nor Section 6's ratio | — | **P** *"It does not reach the mechanism claim."*; **P** the ranges row (*"…survive the re-closure only because the fuel fraction is held…"*) | that the ranges hold for 13 kg on a built store | first |
| **14G What is not known** | Fifteen items, each with what would settle it; the full table in Supplement S14 | — | — | that any item is a small correction | The paragraph *"None of these is a small correction…"*: its first sentence (validated data vs computation) adds a **reason**; its last two sentences re-classify list items already tagged *"analysis not yet done"* / *"absent from this work entirely"* → candidate removable |
| **14H What it amounts to** | The loop closes; the aircraft is not shown to; the gap is named exactly only at the store | — | **P** *"The loop closes; the aircraft is not shown to."* | that the aircraft is claimed | *"The architecture claim … is a count of hardware, and nothing in this section reaches it"* **restates 14F** (*"It does not reach the mechanism claim … a statement about hardware"*) → candidate removable, **but** it is the section's closing statement of the soul (§0.8) — the job may be named: *closing the section on the contribution* |

**Candidates for removal, before any drafting:**

- **14D and 14E.** The re-closure table's third row (+76 to +81 %, a buffer of 13.4 to 14.7 %) is **stated three times**:
  - in the table;
  - in the prose after it (*"about three-quarters heavier, with a buffer of about fourteen percent"*);
  - in 14E (*"thirteen to fifteen percent of take-off mass instead of 3.6"*).

  Keep the table, and keep what the prose adds that the table does not: the 7 kg payload alternative, and the readings of
  the two continuous ratings.
- **14G.** The last two sentences of *"None of these is a small correction…"* re-classify list items that are already
  tagged. The first sentence, which gives the reason (validated data rather than more computation), stays.
- **14H.** *"The architecture claim … is a count of hardware, and nothing in this section reaches it"* restates 14F's
  protected *"It does not reach the mechanism claim."* **My view: keep it.** It closes the section on the contribution
  (§0.8), which is a named job. **Tell me if you disagree.**

**Proposed protection:** *"The escape from Bill 3 is real in the sense Section 3 defined it, and its price depends on a
component whose required performance has not been demonstrated."* It qualifies the one escape the paper claims, and Step 15
depends on it. **My position: yes.**

---

## 4. What I am asking

1. **Confirm §1.**
2. **Step 9:** vote on the item-4 rewrite and on the symmetric removal in item 2. **Grok:** answer on 9F.
3. **The Step 14 inventory:** confirm it or add rows. Take a position on each of the three candidates and on the proposed
   protection.
4. **Check the new onboarding** (§0), especially the numbers.
5. **New proposals**, and any comments on one another.

**Sources.** I opened the Yu 2025 PDF this round, at the path given above.
