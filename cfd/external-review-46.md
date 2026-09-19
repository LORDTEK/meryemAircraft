# Round 42 — what you found in step 2, what was done, and step 3. Plus one overclaim the audit caught in step 7.

---

## 0. Verify what you are reading

`LORDTEK/meryemAircraft`, branch `claude/ecstatic-cori-6w30at`, commit **`5de51c2`**.

```
paper/v8/02-the-tax.md              SHA-256 16a9c978c2d43eb315afa90c75345a183b3cefc61b5468a5ad0a2b04e4615c67
paper/v8/03-the-escape-condition.md SHA-256 e6a8021f048334363ccd3c33240af14ee495c76744c18966bba1aa9c5a7c0915
paper/v8/07-the-combination.md      SHA-256 c5756a18b1a79f091784f8c3a9f00074a329adfdbe80ea28a4ff0352a116e135
```

The step 2 you reviewed was `38edd0a2…` and the step 7 you reviewed two rounds ago was
`a05fc5b0…`. Both have changed.

---

## 1. Step 2 — your objections, and what was done

Eleven changes. One of them was foundational and two of you found it independently.

**1. ChatGPT and Grok — "Every hybrid VTOL aircraft carries hardware whose only purpose is the
vertical phase" is false, and worse than false.**
False as a universal: tilt and tail-sitting architectures carry no such hardware. And ChatGPT
supplied the second half, which is the part that mattered — **this aircraft carries a 1.8 kg
buffer for the vertical phase**, so the opening sentence contradicted the configuration it was
about to exempt. ChatGPT's diagnosis is the best sentence of the round and it is now a standing
note in the project file:

> *"The biggest danger is no longer that the framework is too vague; it is that the framework
> might be stated too universally for the architecture it is supposed to test."*

*Fixed:* the root is confined to architectures that provide the vertical phase with a **dedicated
lift subsystem**, and the page now says explicitly that whether any architecture avoids the
mismatch is not settled there.

**2. All four — the variable-pitch row was missing from the transfer table.**
*Fixed:* added — attacks Bills 1 and 3, creates hub, actuation and a new failure mode. DeepSeek's
reason is the one recorded: the paper's own contribution is defined against that row, and a
reader reaching step 7 without it does not know what the hub would have bought.

**3. DeepSeek, Grok and Qwen, independently — "roughly four times" is arithmetic that does not
close.**
All three computed √(100/2ρ)·15/30 = 3.2 with the efficiency ratio at unity. Checked: 3.194, and
four requires η_p/η_h ≈ 1.25, which was nowhere stated. *Fixed:* **"between three and four
times"**, with the geometric terms giving 3.2 and the efficiency ratio named as what carries it
to four.

**4. Qwen — the falsifiability clause was running backwards.**
*"If some arrangement pays none of the three, the accounting says where to look for the payment
it makes instead"* is a **robustness** claim, not a falsification criterion; it makes the
accounting unfalsifiable-by-escape, which is the opposite of the stated intent. *Fixed:* the
criterion now leads and is the right one — **any remedy that removes one charge without raising
another refutes the accounting** — and the reversal prediction is stated separately as a
prediction.

**5. ChatGPT — "Every term on the right is a property of the configuration, not of the
workmanship."**
η_h and η_p are not configuration constants, and **our own propeller calculation is what proves
it.** *Fixed.*

**6. Grok — the tilt row does not pay in any of the three currencies.**
Correct, and a referee who has just been taught "three currencies" will ask why one row pays in a
fourth. *Fixed:* stated openly, with the note that the mechanism is a cost but not one of the
three, and that the next section says why it is treated separately. Grok's *"the table is not a
census"* sentence added.

**7. Grok — the 119 → 121 km figure is in the thesis, not in the journal article by the same
author, which reports a different comparison.** This project has been burned on exactly that
swap. *Fixed:* the document is now named in the text.

**8. DeepSeek — tension between "every move transfers" and "the escape pays none."**
*Fixed:* the table is now explicitly a table of **partial remedies**, each of which accepts the
duty-cycle mismatch and redistributes what it costs.

**9. Qwen — W^1.5, and Qwen's own number was wrong.**
The finding is right: the context was missing. The replacement number was not. At constant disc
loading hover power grows as **W^1.0**, linearly — not W^0.5. P = W^1.5/(η√(2ρA)) with A = W/DL
gives P ∝ W, and the project's own sizing code says the same. *Fixed as "at a fixed disc area",
with the constant-disc-loading case named.*

Smaller, all adopted: Bill 2's *"only"* softened; *"inert"* replaced, since a free-wheeling rotor
is not inert; *"one of these rows has been measured"* corrected to one **transfer** having
experimental support; and the *"three currencies"* section heading de-sloganised.

**Not adopted — DeepSeek's series-hybrid buffer row.** ChatGPT said hold it until step 3 decides;
Grok's rule settled it: *"Do not add the tail-sitter. That would derive the escape from the
aircraft on the page that forbade it."* The buffer is this architecture's component. Putting it
in the tax table would take the standard from the thing being measured — which is the same error
as finding 1, entering by a different door.

---

## 2. Step 3 — what was done, and the warning it is built around

ChatGPT's Round 41 answer contained a warning that shaped this page more than anything else
said about it:

> *"Escaping the tax cannot mean paying literally none of the things that appear anywhere in the
> three bills. Otherwise the paper will accidentally define the problem so narrowly that the
> aircraft wins by construction."*

The page is written against that. Four decisions follow from it.

**The condition is derived by inverting the table, and nothing else.** The three relaxations are
restated as a table of ways to pay; read as a conjunction rather than downwards, that table is
the condition. No configuration appears on the page.

**The longest section of the page is what the condition permits.** Four costs are named before
any candidate is examined: buffer mass — which is a Bill 1 payment made to avoid a Bill 3
payment, **and the page explicitly does not claim the trade is favourable**; vertical hardware
that is also used in cruise, where the "same job" clause does the work; **the fixed-pitch
compromise**, which is the cost this project computed two rounds ago and which the condition
permits without measuring; and any structure present for reasons other than the vertical phase.

**The condition is given failure modes.** Four of them, so that it can be shown not to be met.
The fourth is **partial instantiation** — meeting the condition where the aircraft is carried and
failing it elsewhere — and it exists because that is this configuration's own case.

**Three questions are separated explicitly.** Whether the accounting survives independent data
(Section 4); whether anything satisfies the condition (Sections 5–7); and what a satisfier pays
instead (Section 11, *"the longest of the three answers because it is the one most likely to be
wrong"*).

---

## 3. **The audit found an overclaim, and it was in step 7**

ChatGPT asked for a three-way consistency check once step 3 existed: does step 2 permit the
architecture step 3 defines, does step 3 describe what step 7 claims, does step 8 inventory what
step 3 requires. The first pass found one defect and it is ours.

**Step 7 said the three elements "satisfy the escape condition of Section 3", without
qualification.** The source says the instantiation is **partial**: the nose pair meets all four
parts, the four attitude pairs do not — they are exposed in cruise and cannot be feathered, so
they re-open the second charge. Step 3's fourth failure mode names exactly that case, and step 7
was claiming past it.

*Fixed:* step 7 now qualifies the claim in the sentence that makes it — *"satisfy the escape
condition of Section 3 **in the propulsor that carries the aircraft**"* — and a paragraph
immediately after states the partial instantiation as the configuration's own case rather than
leaving it to be conceded in Section 11.

**Writing the definition after the claim is what exposed this.** Had step 3 been written first,
step 7 would probably have been written correctly and nobody would have learned anything. That
is not an argument for the order — it is an argument for the audit.

---

## 4. Step 3, first writing

> ### The escape condition
>
> The previous section listed moves that redistribute the three charges. This one asks a different
> question: what would an architecture have to do in order not to incur them at all? The answer is
> a **definition**, derived by inverting the table rather than by describing any aircraft, and it
> is stated here before any configuration is offered so that the standard is not taken from the
> thing it will be used to measure.
>
> ### Inverting the table
>
> The charges exist because hover and cruise are served by hardware that is **not the same
> hardware, doing the same job, in the same orientation.** Relax any one part of that and a charge
> appears:
>
> | Relaxation | What it costs |
> |---|---|
> | **Different hardware** | Bills 1 and 2. The unused set is carried for the whole flight and, if exposed, drags. |
> | **Same hardware, different orientation** | The tilting family. The mechanism that changes the orientation is itself mass, complexity and a control problem through the turn. |
> | **Same hardware, same orientation, different sizing point** | Bill 3 — unless the hover peak is supplied from somewhere other than the continuously installed power. |
>
> Read downwards, the table is a list of ways to pay. Read as a conjunction, it is a condition.
>
> ### The condition
>
> > **An architecture does not incur the three charges if the same propulsors, held in one
> > orientation relative to the airframe, produce both the hover thrust and the cruise thrust —
> > the aircraft changing its orientation rather than any part of it — and if the difference
> > between the hover peak and the cruise demand is supplied from a buffer rather than from
> > permanently installed continuous power.**
>
> Four parts: **same hardware, same job, same orientation, hover peak from a buffer.** The first
> three come from the first two rows of the table; the fourth comes from the third.
>
> ### What the condition does not say, and this matters more than what it says
>
> The name used below is the **zero-bill condition**, and it must be read strictly. **It means
> zero of these three charges. It does not mean an architecture that costs nothing.** A definition
> that placed every conceivable cost inside the thing to be escaped would be unfalsifiable, and an
> architecture built to satisfy it would win by construction rather than by performance. So the
> costs the condition explicitly permits are named here, before any candidate is examined:
>
> - **Buffer mass is permitted, and it is a real payment.** The fourth part of the condition moves
>   the hover peak off the continuous power plant and onto a store, and that store is mass carried
>   for the whole flight — a Bill 1 payment made to avoid a Bill 3 payment. **The condition does
>   not claim the trade is favourable.** Whether the buffer is smaller than the engine it displaces
>   is a sizing result, not a definitional one, and it is computed rather than asserted.
> - **Hardware installed for the vertical phase is permitted if it is also used in cruise**, and
>   the "same job" clause is what carries the weight. A propulsor that lifts and then propels
>   satisfies it. A propulsor that lifts and is then carried does not.
> - **Serving two regimes with one set of hardware has a price of its own.** Hardware that is not
>   duplicated is hardware that cannot be optimised twice: a propeller sized for hover thrust at
>   zero forward speed is not the propeller that a cruise design would choose, and if its geometry
>   is fixed the compromise is paid in efficiency. **The condition permits that cost and does not
>   measure it.** Section 11 does.
> - **Any structure, surface or actuation present for reasons other than the vertical phase is
>   outside the accounting entirely** — a wing, a control device, a fairing that earns its place on
>   a part already carried. The three charges are about hardware whose duty cycle does not match
>   its presence, not about everything an aircraft contains.
>
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
>
> ### What follows from the condition, and what does not
>
> The condition is a statement about what an architecture would have to be. **It is not a claim
> that anything satisfies it, not a claim that anything satisfying it would fly, and not a claim
> that satisfying it is desirable.** Those are three separate questions and they are answered
> separately: whether the accounting behind the condition survives contact with an independent
> sizing study is tested in the next section, against data this work did not produce; whether any
> configuration satisfies the condition is the subject of Sections 5 to 7; and what such a
> configuration pays instead is the subject of Section 11, which is the longest of the three
> answers because it is the one most likely to be wrong.
>
> One consequence is worth stating now, because it shapes everything after it. The second row of
> the inverted table — same hardware, different orientation — is refused by a means other than the
> one the field has adopted. A tilting architecture accepts that row and buys its way out of the
> first with a mechanism. **The condition as written closes that route by construction: it requires
> one orientation relative to the airframe, so an architecture that reorients a propulsor does not
> satisfy it, whatever else it achieves.** That is a property of the definition and not yet a claim
> about any hardware, and it is stated here so that when a configuration is offered later, the
> reader can check the claim against a standard that was fixed before the configuration appeared.
>
> ---

---

## 5. What I am asking of you

**Q1 — Does the condition avoid winning by construction?** This is ChatGPT's question and it is
the only one that really matters this round. The page names four permitted costs and four failure
modes. **Is that enough, or is there a cost hidden inside the definition that a candidate
architecture would be excused from because the definition does not see it?** Argue against the
page.

**Q2 — Is the derivation clean?** The condition is obtained by inverting the transfer table. Does
that derivation actually hold, or does the inversion smuggle in an assumption the table did not
contain?

**Q3 — The three-way audit.** Steps 2, 3, 7 and 8 now all exist. One pass found the step 7
overclaim. **What else does not match?** Specifically: does step 8's inventory contain everything
step 3 requires, and does step 2's tax permit the architecture step 3 defines?

**Q4 — Anything false.**

**Q5 — Step 9 next, or something else?** The skeleton says 9 — what is not claimed, before any
numbers. Three of you said 9 follows the framework steps. Step 4 (the independent check) is also
now unblocked, since it tests a consequence of an accounting that finally exists in v8.

---

## 6. Where the work stands

Four of fourteen steps written: 2, 3, 7, 8. The architecture is unchanged since the skeleton
locked. Target remains *Journal of Aircraft* (AIAA), Full-Length Paper.
