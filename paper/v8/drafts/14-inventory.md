# Step 14 — semantic inventory (Round 91; before any draft)

Source: `14-what-does-not-close.md`, 1502 words, SHA-256 of the body `f49859d6697673cd…`. **P** = protected (9 rows). Assembled position:
Section 8, after the calculations and before the conclusion.

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

## Outbound

| Taken by | What |
|---|---|
| Step 15 | *"The loop closes; the aircraft is not shown to"*; the store as the named obstacle |
| Steps 5, 9 | the store dependency of the runway claim |
| Steps 11, 12 | the 3.6 % buffer as an input; the coupling paid here |
| Supplement S14 | what each unknown bears on |

## Inbound

Section 10 (closures, masses, payload, ranges), Section 11 (ledger), Section 12 (coupling), Section 13 (orderings with the
store held common), Section 3 (the escape from Bill 3), Section 6 (effective L/D), Sections 7–8 (the count).

## Round 92

Inventory confirmed (four + Claude). 14E numbers and 14G last two sentences removed; "The escape from Bill 3 is real…"
protected (160); 14H kept (named job: closing on the contribution). **R-2** caught before applying (14D "instead") → R to
vote. **S-19** (Barrett 2023 p. 34: lithium-polymer up to 3 kW/kg, not quoted) → added sentence to vote; 4 kW/kg now
verified (p. 16). Trace columns for the draft: debt vs scope flag (Qwen P2).

## Round 93

R-2 applied with its repair; S-19 sentence entered (four + Claude). **R-3** (the S-19 sentence leaves "three different
kinds" and the unlike-ratings list incomplete) and **S-20** (Barrett pp. 34–35: pulse limits, hover ≤ 20 s, "may be possible
… using existing technology", not quoted) to vote. Trace columns: evidence status per battery figure (Qwen P2, DeepSeek).

## Round 94

R-3 and S-20 applied (four + Claude; ChatGPT's "The study argues / the study's hover" referents); "the highest figure
obtained from a measurement"; S-19 sentence protected (161). **Trace column agreed (four + Claude):** evidence status per
battery figure — 0.724 and 0.892 verified (ratings); ~1.5 model-derived from measured current, voltage and mass; 4 verified
**as a design assumption**; 3 attributed; Barrett's "may be possible" an attributed conclusion, not a built pack. **Qwen P1
(trace note):** pulse versus continuous rating is the specific mechanism left unposed; it depends on the vertical-phase
duration, which 14G lists under the buffer's energy.
