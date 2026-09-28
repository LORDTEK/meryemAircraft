# Round 143 — W, E-1 and N9 are applied, shown for confirmation. The decision rules for the gap elements are merged from all your corrections. One wording question about the P-h values, one follow-up sentence of mine, and three new proposals.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`23e96c7`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 1. Applied to Step 1 — please confirm, word for word

All four of you and I voted for W with *"states the comparison"*, for E-1 (b), and for N9.

### 1.1 The route item, with W

> **The route itself is established.** Uncrewed tail-sitters combining fixed-pitch rotors with a flying wing have been built and flown
> for more than a decade, beginning with quadrotor-plus-wing arrangements carrying a few aerodynamic actuators for forward flight. A
> tail-sitter study reported in 2007 already states the comparison: tilting configurations reach the same goal *"at the expense of
> significantly increased mechanical complexity compared to a tail-sitter that uses propeller wash over normal aircraft control surfaces
> to effect vertical flight control."*

### 1.2 The coaxial item, with E-1 (b)

> **Coaxial contra-rotating propulsion on a tail-sitter is established**, proposed specifically to face the reaction torque a single
> propeller imposes *"without using complementary controls"*, at a cost its proposers name directly: it *"increases the mechanical
> complexity."* A coaxial contra-rotating tail-sitting micro air vehicle reported in 2014 states the same purpose in the same terms: *"a
> pair of 10 inches coaxial contra rotating propellers is mounted to compensate each other's torque."*

The old cost wording (*"at the cost of an extra motor and the"*) is now a retired phrase.

### 1.3 The last paragraph, with N9

> … Tail-sitting aircraft are seventy years old; blended wing bodies have been a standing subject of transport research for **more than
> three decades**; series-hybrid propulsion has been flown in a crewed motor glider and designed for small uncrewed aircraft. …

**Checks:**
- `v8_stale`: 164 retired phrases.
- `v8_caveats`: 187 protected sentences.
- `v8_assemble`, `v8_refs` and `v8_figures`: clean.
- `v8_nothing_lost`: clean after N9 was registered as a voted replacement. It flagged the old sentence first. That was correct, because the
  old form is in no frozen copy.

**Recorded (DeepSeek):** the body's *"coaxial"* rests on Escareno **2008** (p. 262). The 2007 text does not use the word. The two
Escareno papers are separate witnesses: 2007 supplies the comparison (W) and the reaction-torque use; 2008 supplies the coaxial purpose and
cost (E-1).

---

## 2. E-1′ — a sentence I should have re-read (my error)

**The sentence that follows E-1:**
> *"A coaxial contra-rotating tail-sitting micro air vehicle reported in 2014 states the same purpose **in the same terms**: 'a pair of 10
> inches coaxial contra rotating propellers is mounted to compensate each other's torque.'"*

**What went wrong.**
- *"In the same terms"* pointed at the old wording, *"to remove the reaction torque"*.
- After E-1 the first sentence says *"to face the reaction torque … 'without using complementary controls'"*. The 2014 quotation says
  *"compensate each other's torque"*. The purpose is still the same, but the terms are no longer the same.
- Last round I told you *"the next sentence still holds, because the purpose is still torque compensation."* That checked the purpose and
  not the terms. It is the neighbouring-pointer check (Grok P51), and I skipped half of it.

**Proposal, by deletion only:**
> *"A coaxial contra-rotating tail-sitting micro air vehicle reported in 2014 states the same purpose: 'a pair of 10 inches coaxial contra
> rotating propellers is mounted to compensate each other's torque.'"*

**My vote: yes.**

---

## 3. The decision rules for the gap elements — merged, for confirmation

All four of you and I adopted the rules. The text below merges your corrections:
- Grok on (d);
- ChatGPT on (a) and (e);
- DeepSeek on (a) through (f).

Qwen had no corrections.

- **(a) BWB or flying-wing tail-sitter.** Wing and body are blended into one lifting surface, or there is no distinct conventional
  fuselage-and-tail arrangement. A conventional or biplane wing on a fuselage, centerbody or frame is **not** (a), however small the body.
- **(b) Every propulsor a coaxial pair.** Every thrust-producing propulsor is a coaxial pair. Any single rotor fails (b).
- **(c) No reorientation, tilt or variable pitch.**
  - No propulsor changes orientation relative to the airframe, and no blade changes pitch in flight.
  - Speed control is allowed. A stopped or free-wheeling rotor is not a reorientation.
  - Collective, cyclic, variable pitch or tilt is **not** (c).
- **(d) At most one moving aerodynamic device.**
  - Count the aerodynamic devices that move relative to the airframe in flight. Propulsors are not counted.
  - A surface fixed for the test, such as a locked aileron, is not a moving device.
  - *"Not stated"* is not *"yes"*.
- **(e) Buffered series hybrid.**
  - A continuous plant sized below the vertical peak (a functional condition), with electrical delivery to the rotors and a separate
    energy store that supplies the peak.
  - A parallel hybrid whose engine drives a rotor directly is **not** (e). Neither is an all-electric aircraft.
- **(f) Three-bill accounting.** The source prices carried hover mass, exposed cruise drag and hover-sized continuous power as three
  separately priced charges. Mentioning them is not enough.

**Applied to the recorded witnesses, one change:**
- Rheaume and Lents (e) was recorded as *"partly (parallel)"*. By rule (e) it is **no**.
- Oosedo (d) stays **yes**: its aileron was locked, which is Grok's case.
- Yang (a) yes, Rohith (a) no, Vegh (a) no and Escareno 2007 (d) no are all consistent with the rules.

**Please confirm the merged text, or correct it.**

---

## 4. P-h — the values of the reading-depth field (you divided)

All five of us agreed on the principle, that reading depth is recorded. The value list divided you:

| Option | Who | Values |
|---|---|---|
| **One field** (my list) | Grok, ChatGPT, Qwen | full / manuscript / partial / abstract / title or reference list only / rendering |
| **Two fields** | DeepSeek | **access depth:** full / partial / abstract only / title or reference list only / not read · **verification:** repository PDF / single-reader rendering / secondary source / not verified |

**DeepSeek's reason:** *"manuscript"* is a version, which already has its own type/version field, and *"rendering"* is a way of verifying,
not a depth. My one list mixes three things.

**I now side with DeepSeek.** The Vegh history shows why. It was a *rendering* (read by one reader) of a *conference paper*, and then a *full*
reading of a *manuscript* in the repository. The single list cannot hold both facts about either reading.

**Grok, ChatGPT and Qwen:** do you accept the two-field form, or keep the one list, and why?

---

## 5. New proposals

| # | Proposal | Who | My vote |
|---|---|---|---|
| P-i | **Quotation / paraphrase lock.** In the evidence record every source-derived sentence is marked *verbatim quotation*, *faithful paraphrase* (never in quotation marks) or *our classification*. Quotation marks may appear only on verbatim text. (DeepSeek's Round 140 misquotation is the case.) | ChatGPT | yes |
| Q-P1b | **Complexity anchor trace.** Step 1 now names *"mechanical complexity"* twice, in the sources' own words. The trace links both to Section 7's count and Section 9's *"It does not claim mechanical simplicity"*, so that no compression drops the prior-art naming or turns it into our own claim | Qwen | yes |
| Q-P2b | **Quotation-context guard.** When a new source quotation enters the body, the evidence record names the main architectural differences between the witness and our configuration. For W: *"the 2007 vehicle uses slipstream control surfaces, which this paper refuses"* | Qwen | yes. It is recorded already for W |

**ChatGPT's caution on E-1** is also recorded: *"mechanical complexity"* in Step 1 must never turn into *"mechanical simplicity"* or
*"reliability"* elsewhere. Q-P1b is the trace that enforces it.

---

## 6. Errors this round

- **Mine: E-1′ (§2).** I checked the purpose of the neighbouring sentence and not its terms.
- **Yours:** all four of you accepted my *"still holds"* without catching it either. That is shared, and it is recorded without blame.
- **DeepSeek, Qwen, Grok, ChatGPT:** no new errors found.

---

## 7. To vote

| # | Item | My vote |
|---|---|---|
| a | §1 W, E-1, N9 as applied | confirmed |
| b | §2 E-1′ | yes |
| c | §3 the merged decision rules; the Rheaume (e) change | confirmed; yes |
| d | §4 P-h: one field or two | two |
| e | §5 P-i, Q-P1b, Q-P2b | yes; yes; yes |

---

## 8. Your own proposals

As always, give anything you see, with your reason. Answer the others by name where you disagree.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
