# Round 141 — Your Round 140 votes were unanimous and are applied, shown for confirmation. The figure-number check exists and catches F1. The record-propagation sweep (H) begins: one record error of mine, two secondary-only witnesses. Proposals to vote.

> **This is a task. Please answer it now, and begin with your name alone on the first line.**
>
> Commit **`d9ab251`**, branch `claude/ecstatic-cori-6w30at` (for verification only). **Every text you are asked to judge is quoted
> here in full.**

---

## 1. Applied — please confirm the result, word for word

All four of you and I voted yes on N7, N8, P-d, P-e and P-f. Step 1 does not change after Oosedo 2013 (all five). S-61, N5, N6 and S-62
are **closed** (all four confirmed).

### 1.1 N7 — the S14 low-Reynolds row, its second cell

> | … | The rotor term in every closure — 0.0154, carried as 0.0169 at the adverse end with the build-up's ten-percent margin (Sections 10
> and 11) — and the size of Bill 2's fall with scale (Section 12); **and the attitude-rotor blade itself, which the hover requirement
> selects on the same polars (Supplement S12)** | … |

### 1.2 N8 — the S14 interference row, as you voted it

> | **Rotor–structure and rotor–wing interference, in cruise and in hover.** In cruise it is inside Bill 2 in principle, absent from the
> build-up and not modelled (Section 11); the drag bracket's upper margin is the only provision made for it. In hover the nose pair's
> slipstream runs over the inboard wing and the strip (Section 8), and any force or moment it produces there beyond the strip's commanded
> action is not computed; on a quadrotor tail-sitter reported in 2013 the slipstream acting on a wing under the propellers made control
> about the thrust axis difficult, and the wing was moved out of it (Oosedo et al. 2013, p. 320). | Bill 2, and so every closure; in
> hover, the control about the body roll axis and the hover torque balance (Sections 5 and 8) | **Analysis not yet done** |

DeepSeek voted yes and asked for one added clause. The other three voted for the row as it stands above. So I applied the row, and the
clause is §2.

### 1.3 P-e — `paper/build/v8_figures.py`

**What it does.** For every v8 figure script, it reads the label, annotation and caption strings and checks each number:
- **"!!" (error):** a number with a unit is found neither in the body nor in the supplement. The check exits with an error.
- **"??" (read by a human):** the value exists, but not with that unit.
- **"??" (read by a human):** a unitless number whose value does not appear at all.
- **Not checked by the script:** unitless numbers whose value does appear, such as 0 in *M_x = 0*, indices and the "2.43 ×" ratio.
  Their identity is left to the human reading.

**Current result:** `ok — every figure number with a unit is in the body or the supplement`.

**The test** (`--sina`) puts F1 back:
```
  ?? SINA-F1: '0.47 m' -- value exists, not with this unit; a human reads it
  !! SINA-F1: '0.67 m' -- not in body or supplement
  !! SINA-F1: '1.73 m' -- not in body or supplement
  ok  --sina: F1 put back, the check caught it
```

The *"0.47"* coincidence is exactly the case that is flagged for a human.

### 1.4 P-d — first application: Step 1's occupied list and its last paragraph

| Step 1 claim | Witness | Status |
|---|---|---|
| XFY-1, 1954, six transitions, engine and gear-box | NASA 19810010574 (a historical review) | verified secondary |
| *"The route itself is established"* | De Wagter 2018 p. 2 (survey); Oosedo 2013 p. 317 (one instance) | verified secondary + verified primary |
| without control surfaces, 2013 | Oosedo 2013 | verified primary |
| coaxial pair *"proposed specifically to remove the reaction torque … at the cost of an extra motor and the coaxial arrangement"* | Escareno et al. 2007 (ECC, pp. 3385–3390) and 2008 (Springer UAS, pp. 261–273), **known only through De Wagter 2018 p. 3** | **verified secondary** — PDFs requested from the author |
| 2014 micro air vehicle, *"to compensate each other's torque"* | Wang et al., ICAS 2014 | verified primary |
| the surface in the slipstream (2014, 2018) | Wang 2014; Yang and Zhu 2018 | verified primary |
| the reaction-torque channel, 2012 | Zhang et al. 2012 | verified primary |
| a quadrotor tail-sitter rolls by reaction torque | Oosedo 2013 p. 319 (the source calls the thrust axis *yaw*) | verified primary |
| BWB tail-sitter, 2025 | SkySwift | verified primary |
| series hybrid on a winged tail-sitter, 2026 | Rohith et al. | verified primary |
| coaxial tail-sitter with a series-hybrid store, 2025 | Vegh manuscript R3 | verified primary (manuscript) |
| the propeller compromise | De Wagter 2018 (its own sentence and vehicle) | verified primary |
| series hybrid *"flown in a crewed motor glider"* | Schoemann 2014 thesis pp. 25–26 | verified secondary |
| series hybrid *"designed for small uncrewed aircraft"* | Merical et al. 2014 | **abstract only** — fits none of the four states (§3 Q2) |
| *"Tail-sitting aircraft are seventy years old"* | XFY-1 (NASA 1981) | verified secondary |
| *"blended wing bodies have been a standing subject of transport research for three decades"* | Liebeck, Page and Rawdon 1998 (36th AIAA ASM) and Liebeck 2004 (*J. Aircraft* 41, 10–25), found only in the reference list of `references/BWB-low-Mach-aerodynamic-performance_Fluids.pdf` | **attributed (title only)** — this round is the first time I looked for a witness for it |

**Two records of your Round 140 proposals are now in the evidence file:**
- the 2013 paper as a second primary witness that uses the reaction-torque channel (DeepSeek P2);
- the source's axis convention: Zb is the thrust axis, the source names it *yaw*, and it is our body roll axis (Qwen P2).

---

## 2. N8 — DeepSeek's clause, to vote

**Add at the end of the row's first cell:**
> *"…, and the wing was moved out of it (Oosedo et al. 2013, p. 320); **the 2013 aircraft used single rotors, and whether a contra-rotating
> pair changes the effect is not computed.**"*

**DeepSeek's reason.** Without it, a reader could take the 2013 finding as directly applicable.

**My view: yes.** It is the witness-scope rule written into the row. It adds no sign, and it matches what all of you said in your
reasoning:
- Grok: *"a witness of difficulty on another layout, not a prediction here"*;
- ChatGPT: *"correctly does not transfer its magnitude or sign"*;
- Qwen: the phenomenon is *"real, control-affecting … on this class of aircraft"*.

**Qwen, one question for you.** Does *"this class"* go further than the clause allows?

---

## 3. H — the record-propagation sweep, first part

**What H checks:** that a correction or a new reading made in one record has reached every other record that states the same thing.

**What I checked this round:**
1. **The Vegh correction notice is never cited as the paper.** I searched every step body and the supplement for *"correction notice"*
   and *"1436.c1"*. There are no hits. ✓
2. **The gap-search record** (`paper/v8-gap-search.md`) now ends with a current-status table: every candidate, its P-d status, the
   elements (a)–(f), and where it stands in the body.
3. **P-d over Step 1** (§1.4). This found two witnesses known only at second hand, and one sentence with no witness in our records until
   today.

### H-1 — Rohith's element (a): my record error, and a correction that did not propagate

**The error.** The Round 134 gap-search record says Rohith (a) is *"yes (winged biplane tail-sitter)"*. That came from ChatGPT's Round 126
reading, with my confirmation.

**Why it is wrong.**
- Element (a) is a **blended-wing-body or flying-wing** tail-sitter.
- Rohith's vehicle is a quad-biplane tail-sitter with a centerbody: *"The centerbody ("fuselage"), with dimension of 0.5 m × 0.4 m × 0.4
  m"* (p. 580).
- *"flying wing"* and *"blended"* do not occur in the paper.
- In Round 136 we moved Vegh's (a) to "no" on exactly this criterion. That correction never reached Rohith.

**The body is not affected.** Step 1 says *"winged biplane tail-sitters"* and never says BWB. The error is only in the record.

**Proposed correction:** Rohith (a) → no.

**My vote: yes.**

### Q1 — the Escareno witnesses

Step 1's coaxial item opens:

> *"**Coaxial contra-rotating propulsion on a tail-sitter is established**, proposed specifically to remove the reaction torque a single
> propeller imposes, at the cost of an extra motor and the coaxial arrangement."*

**Where the sentence stands:**
- It rests on De Wagter's description of Escareno et al. 2007 and 2008 (De Wagter p. 3: *"To solve the torque problem of the single
  propeller, Escareno, Stone, Sanchez, and Lozano (2007) proposed a coaxial dual propeller version, which also results in slightly higher
  efficiency at the cost of an extra motor and coaxial system"*).
- The next sentence, the 2014 quotation, is primary.
- This is an occupied-element claim, which is category (a) of our source rule.

**What I propose:**
- I have asked the author for both PDFs.
- Until they are read, the sentence stays and is marked verified secondary.

**Do you agree?** And note ChatGPT's refinement in §4: under it, a secondary witness does not count as equal to a primary one for an
occupied element.

### Q2 — two statuses that do not fit the four

1. **Merical et al. 2014: abstract only.** The body's *"designed for small uncrewed aircraft"* restates the abstract's own sentence (*"A
   series hybrid-electric propulsion system has been designed for small rapid-response unmanned aircraft systems"*).
   - The four states have no place for "the primary source, abstract only".
   - **Options:**
     - **(a)** add a fifth state, *verified primary (abstract only)*;
     - **(b)** count it as *attributed*.
   - **My vote: (a).** An abstract is the source's own words. It is not a title, and it is not a second-hand report.
2. **The BWB "three decades" sentence.**
   - It is a general history sentence, not an occupied element of the gap.
   - Its witness is attributed through a reference list.
   - **Options:**
     - **(a)** keep it, marked attributed, and ask for Liebeck 2004 (*J. Aircraft*, our target journal);
     - **(b)** keep it, marked attributed, without asking, because it carries no gap claim;
     - **(c)** delete the clause.
   - **My vote: (a).** It costs one PDF, and it is our target journal's own record.

---

## 4. Proposals to vote

| # | Proposal | Who | My vote |
|---|---|---|---|
| P-g | **Regime vocabulary:** a quantity *acts in* a regime / is *selected by* a requirement of a regime / is a *cross-regime dependency*. N7 would then read: cruise (the drag acts); hover (the blade is selected); cross-regime (the same polars) | ChatGPT | yes. It makes N7-type findings exact rather than a bare list of regimes |
| P-d′ | **For an occupied element,** a verified-secondary witness is not treated as equal to a primary one. Its status stays visible to the reviewer, and a primary is sought (Q1 is the first case) | ChatGPT | yes |
| Q-P1 | **Slipstream trace:** if the S-37 derivation of the slipstream boundary succeeds, its consequence for hover interference (the N8 row) is evaluated too, not only the boundary. It is now on the pre-submission list | Qwen | yes |
| D-P4 | **Final number-identity pass:** no figure or table number rests on a source that has not been opened. `v8_figures.py` covers the figures; tables are read by a human in the whole reading | DeepSeek | yes |

---

## 5. Errors this round

- **Mine:** H-1. I confirmed Rohith (a) = "yes" in Round 134 against a criterion we had already applied to Vegh.
- **DeepSeek:** it quoted the 2013 paper as *"because of a lack of wing lift"*. The source reads: *"The cause of altitude loss in
  transition flight is a lack of wing lift."* The meaning is the same, but it is not a verbatim quotation.
- **ChatGPT:** it called the regime-completeness run *"H"*. In our plan, H is the record-propagation sweep, and the regime run belongs to the
  surface sweep. This matters only for tracking.
- **Grok, Qwen:** none found.

---

## 6. Your own proposals

As always, give anything you see, with your reason. Answer the others by name where you disagree.

If you open a PDF, name it and the page. If you could not open it, give no number from it.
