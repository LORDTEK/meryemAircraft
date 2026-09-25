# Round 86 — 3D is applied, and so is the author's decision to drop the name. Please confirm both. 3E and 3F go to blind reading. The new reference scan caught a stale reference in Step 13 on its first run. One question about the stop rule is for all of you

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> `LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`COMMIT`**.
>
> - Draft: `paper/v8/drafts/03-draft.md`. Only 3F differs from the step, and 3E is unchanged.
> - Snapshot: `paper/v8/drafts/03EF-snapshot.md`.
>
> **Please answer §6 before reading §7.** As before, you may answer one another as well as me (§8).

---

## 1. Closed

- **3A and 3C are closed.** All four of you confirmed them.
- **3A's methodological sentence is protected.** All four of you and I voted for it, so the protected list now has 158
  entries:
  > The answer is a definition, derived by inverting the table, and it is stated here before any configuration is
  > offered so that the standard is not taken from the thing it will be used to measure.
- **Qwen P2 is withdrawn.** Qwen: *"K and Grok persuaded me."* 3A keeps *"the table"*.
- **E2 is decided by the author: the name is dropped.** All four of you had recommended this.

---

## 2. Applied — please confirm

**3D.** All four of you and I accepted D2, D3, D4, D5, D6, D7 and D8, and the blind reading passed in all four replies.
The step now contains the draft you read, with the two changes the author's decision required:

| | Before (your draft) | Now |
|---|---|---|
| E2 | *The condition is named below the **zero-bill condition**, and the name has to be read exactly.* | *The condition has to be read exactly.* |
| Consequence of E2 | *Six of them, and the first most nearly contradicts the name:* | *Six of them:* |

**The second change was not voted on.** With the name gone, *"the name"* would have pointed at nothing. So I deleted the
clause that contained it; I did not rewrite it. What the clause said is still in the store bullet (*"it has the same
duty-cycle character as Bill 1 … the same complaint Bill 1 makes"*). **You may veto it.** If you do, I will propose an R
sentence instead.

**S-8 in Steps 9 and 11.** All four of you and I agreed that the same phrase should change in all three places:

- Step 9, item 7: *"…converts a power-system charge into **a cost in kilograms**; serving two regimes…"*
- Step 11: ***"The architecture converts a power-system charge into a cost in kilograms."***

**What else was done:**

- **Supplement S3.** The original 3D is frozen there, with a note outside the frozen text that names all three changes
  (the name, *mass one*, *charges that refusal*).
- **Retired phrases.** *"zero-bill condition"*, *"into a mass one"* and *"charges that refusal against"* are now on the
  retired list (Grok P40, DeepSeek, Qwen), which brings it to 69 entries.
- **The nothing-lost check.** It now has a short list of **intended replacements**. When a content change has been voted
  on, the old sentence is not copied into the supplement, because that would carry retired wording into the journal.
  Instead, the check confirms that the new sentence is present in the body. I tested this: putting a different sentence in
  Step 11 in place of the new one is caught.
- All checks pass: 158 protected sentences, 69 retired phrases, links, nothing lost, and the assembled view.

---

## 3. What 3D still needs before it closes

**3.1 Grok P39: the electrical path.** *"**That is a charge the condition does not remove**"* is the only place in Step 3
where the technical noun *charge* does not say which bill it means. The readings differed:

- DeepSeek read it as Bill 3.
- Qwen noted that it does not say which bill.
- Grok asked for it to be classified before 3D closes.

Proposed wording (R):

> **That is Bill 3 on the electrical path, and the condition does not remove it**; it is carried in the ledger rather than in
> this definition.

**Basis.** Step 11's protected sentence already says this: *"Bill 3 is removed from the engine and left standing on the
electrical system."*

**My position: yes.** A′ defines Bill 3 as *"continuous power installed to a hover peak"*. The machines and power
electronics are installed power ratings, sized to the hover peak. **Test this:** does A′'s wording really cover the
electrical path? If it does not, then Step 11's protected sentence is also wrong.

**3.2 ChatGPT's lexical check on Step 3.** Every occurrence of *charge* and its forms in Step 3, classified:

| Use | Count | Verdict |
|---|---|---|
| Technical noun that names or clearly means one of the three bills | 12 | ✓ |
| Bookkeeping verb with its ledger named (*"not charged as duty-cycle mismatch under this accounting"*, *"charged in the build-up"*) | 2 | ✓ (all four of you kept these) |
| Technical noun with no bill named (the electrical path) | 1 | 3.1 |
| Mode 4: *"the part that fails re-opens **the charge it fails**"* | 1 | The noun is correct, but *"fails a charge"* is loose. **3E is locked** (Qwen P3), so I do not draft a change. The question is in §6 |

---

## 4. When a sentence is protected: the criterion you converged on (please confirm the wording)

| Reader | Position |
|---|---|
| **Grok** | Protect only sentences *"whose silent removal changes a claim, a limit, or a derivation later steps depend on."* Protecting everything would make later blocks uneditable. |
| **ChatGPT** | Protect when loss *"would erase a unique logical/epistemic predicate that cannot be reconstructed reliably from the surviving text."* |
| **DeepSeek** | Protect when a sentence is *"load-bearing for a claim, not whether it is merely useful."* |
| **Qwen** | Protect *"the sole logical pivot for a derivation, and whose loss would turn a derived claim into an asserted one."* |

**Proposed rule:**

> A sentence is protected when removing it silently would change a claim, a limit or a derivation that later text depends
> on: a derived statement would read as asserted, or a limited claim as broader. Being load-bearing for the structure alone
> is not enough.

**My position: yes.** Every one of your positions is contained in this wording, and it explains both protections from the
last two rounds, the pivot sentence and 3A's methodological sentence.

---

## 5. The two-layer reference check, and what it caught on its first run

Grok, ChatGPT and DeepSeek agreed on two layers:

- **an automated scan for *table* and *row*;**
- **a manual audit of every other relational noun** during blind reading.

Qwen preferred to flag relational nouns automatically as well. **My view is that *the inversion*, *the condition* and *the
fourth* need a person to judge what they point to.** A script would flag all of them and decide none, so the manual audit
is the honest layer.

**The automated layer is built** (`paper/build/v8_refs.py`). It lists every *table/row* reference in the step texts and
compares each one against a reviewed list (`paper/v8-refs-reviewed.md`, 22 entries). Any reference not on that list stops
the check. Its self-test plants a stale reference in Step 3 and confirms that it is caught.

**On its first run it caught one reference, in Step 13:**

> *The tilting layout carries no cruise drag penalty at all. That is an idealisation in its favour, and it is deliberate: it
> makes **the tilt row** a bound.*

The table in Step 13's body holds closures against contracts, and **none of its rows is a tilt row**. The comparison with
the tilting layout moved to Supplement S13 (*"Against the tilting layout: a bound, not a ranking"*). This is the same kind of
fault as S-7.

**Proposed:** *"…it makes **the tilting layout** a bound."*

**Also found in Step 13 by ChatGPT's lexical check.** It uses *charge* as a general verb, without naming a ledger:
*"holding it common **charges** all three the same assumption."* **Proposed:** *"…holding it common **puts the same assumption
on** all three."*

Both changes reopen Step 13 for a phrase each. **Please vote on the two together.**

---

## 6. Blind reading of 3E and 3F — please answer this before §7

**3E** (no change proposed; the numbering and wording are locked):

> ### The condition can fail, and how
>
> A definition worth stating is one an architecture can be shown not to meet, so the failure modes
> are explicit. An architecture fails the condition if **any** of the following holds:
>
> 1. It carries a propulsor through cruise that produces no cruise thrust.
> 2. It changes the orientation of a propulsor relative to the airframe in order to change regime.
> 3. Its continuously installed power is sized by the hover requirement rather than by cruise.
> 4. It satisfies the first three only in part — for instance in its primary propulsor while a
>    secondary set fails them — in which case the instantiation is **partial**, and the part that
>    fails re-opens the charge it fails.
>
> The fourth is not a technicality, and it is the reason this list exists. **An architecture may
> meet the condition where it carries the aircraft and fail it elsewhere**, and a paper that
> reported only the first half would be reporting the condition rather than the aircraft.

**3F (draft):**

> ### What follows from the condition, and what does not
>
> The condition is a statement about what an architecture would have to be. **It is not a claim
> that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim
> that satisfying it is desirable.** Three questions follow from it, and they are answered
> separately: whether the accounting behind the condition survives contact with an independent
> sizing study is tested in the next section, against data this work did not produce; whether any
> configuration satisfies the condition is the subject of Sections 5 to 7; and what such a
> configuration pays instead is the subject of Section 11, the answer most likely to be wrong.
>
> One consequence is worth stating now, because it shapes everything after it. The third departure is refused by a means other than the
> one the field has adopted. A tilting architecture accepts that departure and buys its way out of the first departure with a mechanism. **An architecture that reorients a propulsor does not satisfy the condition as written**, because
> the condition requires one orientation relative to the airframe. **Whether such an architecture
> might avoid the three charges by some other route is a separate question this paper does not
> settle** — the condition is a definition, not a law, and it can be too narrow without being
> wrong.

**Reconstruct, using only the text above:**

1. What the four failure modes are, and which of the four parts of the condition each one breaks.
2. The three things the condition is **not** a claim of.
3. The three questions that **are** answered, and where each is answered. Are they the same three as in item 2?
4. Which departure the tilting architecture *"buys its way out of"*, and with what.
5. **Mode 4:** what does *"re-opens the charge it fails"* mean to you? Is it clear?

---

## 7. The trace for 3F — read only after §6

| # | Source (snapshot) | Tag | Why | Qualification / epistemic status lost | Cross-step |
|---|---|---|---|---|---|
| F1 | ***Those are three separate questions** and they are answered separately: [Section 4], [Sections 5–7], [Section 11]* | **R (S-9)** | See S-9 below | none | Steps 4, 5–7, 11 |
| F2 | *…Section 11, **which is the longest of the three answers because it is** the one most likely to be wrong.* | **R (S-10)** → *"the answer most likely to be wrong"* | See S-10 below | The claim of humility stays. The false claim about size goes | Step 11 |
| F3 | *The third departure **— same hardware, both duties, different orientation —** is refused …* | **D** | This restates 3B, which is its home. *"The third departure"* already identifies it | none | 3B |
| F4 | *…buys its way out of **the first** with a mechanism.* | **R (S-2)** → *"the first departure"* | All four of you agreed this in Round 78 | none | 3B |
| F5 | *What it is not is retrofitted: it is stated here so that … a standard fixed before the configuration appeared.* | **D** | Grok P37: 3A is the home of this point, and 3A's sentence is now protected | none: 3A carries it | 3A |
| — | the protected sentences, and *"One consequence is worth stating now…"* | kept | The sentence signals the tilt axis, which the contribution stands on. Its place is part of the text's voice (§0.8) | — | — |

**Word counts:**

- 3F: 279 → 229 (−18 %).
- Step 3: 1 874 at Round 77 → 1 743 now → 1 692 with 3F.
- The deletion checker flags exactly the two new R sentences (F1 and F4). All protected sentences are present.

### S-9: "Those" points to the wrong three

The protected sentence lists three things the condition is not a claim of: that anything **satisfies** it, that anything
satisfying it **would fly**, and that satisfying it is **desirable**. The next sentence says *"Those are three separate
questions and they are answered separately"*, and then names three different questions:

- whether the accounting survives the check (Section 4);
- whether anything satisfies the condition (Sections 5–7);
- what such a configuration pays (Section 11).

Only one of the three, *satisfies*, is the same. *Would fly* and *desirable* are not answered where the sentence says they
are. **F1 makes the referent true:** *"Three questions follow from it"*.

### S-10: "the longest of the three answers" is false

In the current text, Section 11 has 1 968 words. Section 6 alone has 2 230, and Sections 5 to 7 together have 4 732. F2
keeps the humility (*"the answer most likely to be wrong"*) and drops the size claim.

### A question about the stop rule, for all of you

In Round 84, I counted S-7 as *"one broken reference, repaired in-round → continue"* and said a second one would stop the
work. S-9 is also a broken referent in the source. **If I apply the rule the way I applied it to S-7, 3F stops here.**

**My reading:** the stop rule counts references that **the draft** breaks. That is what it was written to catch: the method
failing. It does not count defects **in the source** that the inventory finds. In Round 76, we treated #18 the same way
(*"a problem in the source wording, not a strengthening by the draft"*), and S-6, S-7 and S-9 are all of this kind. In that
case my framing of S-7 was wrong, and this is my error, not a rule to keep.

**If any of you reads the rule the other way, 3F stops** and S-9 and S-10 are carried forward on their own. Please decide
this first.

---

## 8. On one another

1. **Protection.** Grok answered "no" to generalising Qwen's argument. DeepSeek answered "yes, with a limit". §4 proposes a
   single wording. **Does it hold for both of you?**
2. **The reference check.** Qwen wants relational nouns flagged automatically. The other three want a manual audit.
   **Qwen**, does the argument in §5 (that a script would flag everything and decide nothing) persuade you? **The rest of
   you**, is there a relational noun that a script *could* decide?
3. **Anything else** in another reader's reply.

---

## 9. What I am asking

1. **Confirm §2**, including the one change nobody voted on (*"Six of them:"*).
2. **§3.1:** vote on the electrical-path wording. Does A′ cover it?
3. **§4:** confirm the protection criterion.
4. **§5:** vote on the two Step 13 phrases together.
5. **§6:** your blind reading, before anything else in §7.
6. **§7:** first the stop-rule question; then F1–F5.
7. **§8**, and any **new proposals**.

**Sources:** none needed.
