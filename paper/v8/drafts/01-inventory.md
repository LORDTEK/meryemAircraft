# Step 1 — semantic inventory (Round 93; before any draft)

Source: `01-the-gap.md`, 1 679 words, SHA-256 of the body `3aecec8af0dc9e40…`. **P** = protected (8 distinct rows).
Assembled position: Section 1, the opening. Every later section's "what is new" leans on it (Steps 7, 9, 15).

Sources opened for this inventory, with the surrounding paragraph read (Qwen P1, applied before its vote):
`references/19810010574.pdf` and `references/19840014464.pdf` (NASA reviews), `references/Wagter_et_al_2018_Journal_of_Field_Robotics.pdf`,
`references/Design+of+Flying+Wing+Tail+Sitter+Contra-Rotating+Propeller+VTOL+Sky+Swift+V1.0+UAV_Final.pdf`. Novlit 2014,
Zhang 2012 and Johnson & Silva 2022 were read first-hand in Rounds 45–47 and not reopened.

| Block | Must say | Evidence (status) | Must qualify (P) | Must not say | Restatement: of what, and status |
|---|---|---|---|---|---|
| **1A Two families, two limits** (24–43) | Fixed wing is limited by infrastructure, rotorcraft by installed power; neither is deficient; the two applications sit in the corner where both are wanted; the corner is not empty; what is unsettled is the price | background, no source (conventional) | — | that either family is deficient | first |
| **1B Seventy years** (45–51) | Tail-sitters 1950s, vectored thrust and tilt-wing 1960s, tilt-rotors, hybrid VTOL UAVs since about 2010; the need is real | 1950s tail-sitter **verified** (XFY-1, Aug 1954); tilt-wing 1960s **verified** (XC-142, CL-84 in the NASA review); **tilt-rotors "from the 1980s" contradicted by the same review: XV-3 hovered August 1955, XV-15 hovered May 1977 → candidate S-23**; "since roughly 2010" attributed (De Wagter 2018 cites 2012–2014 platforms) | — | — | first. *"No field sustains that level of effort against a need that is not real"* is an argument from effort (J), not evidence |
| **1C How the contemporary answers change regime** (53–80) | Hybrids work and some are in service; lift+cruise keeps two sets and stops one in the airstream; tilting keeps one set and turns it; tilting is more elegant on paper and harder to build; **the requirements are mechanical and control, not aerodynamic, and the paper is built on that distinction** | Johnson & Silva 2022 §5.4–5.5 **verified** (Round 45); "several are in service" **unsupported in the step** (no source named) | — | that the hybrids do not work | *"This paper does not dispute that they work"* is restated in 1F (*"This paper does not claim otherwise"*) |
| **1D The third route; inherited difficulties** (82–102) | Rotating the whole aircraft is the third route, flown in 1954 and revisited since; what curtailed the XFY-1 was engine and gear-box reliability, not the pilot; three difficulties are inherited; the reaction-torque channel is declined, not impossible; three enablers exist now | XFY-1: six transitions, "curtailed because of engine and gear-box reliability problems", "very high pilot workload" — **verified in both NASA reviews**; "exploiting exactly those three for over a decade" attributed | **P** *"they are the only one of those documented obstacles an uncrewed aircraft removes"*; **P** *"Some of the difficulties were real, internal, and are inherited here."*; the declining sentence (*"a choice this configuration declines rather than a limit it inherits"*) — **not protected, but it is what stops *"no rolling moment by any combination of thrust settings"* reading as a physical impossibility** (CLAUDE §0.1) | that roll is physically impossible; that an uncrewed aircraft removes every documented obstacle | *"Precise hovering, ground gusts and the absence of a thrust-borne rolling moment are configuration facts, and they are inherited"* is the **third** statement of "inherited" in one paragraph, and it names **"precise hovering"** where the list it summarises names **"a tail-sitting vertical descent"** → candidate removable |
| **1E What is already occupied** (104–145) | Six things are established: the route (fixed-pitch rotors + flying wing, over a decade); attitude without control surfaces (2013); coaxial contra-rotation for torque (2007, 2014); a slipstream surface as the hover-control answer (2014), refused here; the reaction-torque channel as a control channel (2012); a BWB contra-rotating tail-sitter for disaster response (2025); and the fixed-pitch compromise is a known result | De Wagter 2018 **verified** (Quadshot, "typically two aerodynamic actuators"; Escareno 2007 "at the cost of an extra motor and coaxial system"; "theoretically impossible"); Oosedo 2013 **attributed** (title in De Wagter's list); Novlit 2014, Zhang 2012 **verified**; SkySwift 2025 **verified** (XFLR5 VLM, Fluent RANS, winglets, transition, disaster response). **DelftaCopter: the quote is verified but the rotor is cyclic-and-collective variable pitch, and the same page says variable pitch "theoretically makes it possible" to be efficient in both, at the cost of two extra actuators and mechanism weight → candidate S-22** | **P** *"Using it is a choice, and so is declining it."* | that the third route is empty; that the fixed-pitch compromise is this paper's discovery | The opening *"It would be easy, and wrong, to present the third route as an empty field. It is not, and the paper is better for saying so first."* is said again in 1F (*"And the third route is occupied. What follows is therefore not a claim to an empty field."*, P) and by the heading → candidate removable (1F's sentence carries the "therefore" and must stay) |
| **1F The gap, stated precisely** (147–165) | Each half and both together are served; the route is occupied; what is not established is the combination **with its price**: every propulsor a torque-balanced coaxial pair, no control surfaces beyond one device, buffered series hybrid, audited against the three charges; the giving-up is the part that is not free | model-derived (the paper's own sections) — but **"audited … at two scales" is broader than Step 12, where Bill 1 is not tested at the second scale → candidate S-21** | **P** *"What follows is therefore not a claim to an empty field."*; **P** *"What is not established is the combination taken together with its price."* | that the field is empty; that the combination is free | *"a coaxial pair can produce one the same way, by running its two rotors at different speeds"* restates 1E, **but it is the antecedent of "that channel" in the next sentence** (Grok P51) → keep |
| **1G The contribution** (167–177) | None of the elements is new; the route was not waiting to be found; **the contribution is the architecture**; the combination and its accounting are how it is presented and priced; Section 2 states the cost | the three "old" elements: attributed (Step 7) | **P** *"None of the elements is new"*; **P** *"The route is not claimed to have been waiting to be found."*; **P** *"The contribution is the architecture: …"* | a simplicity or reliability claim; a priority claim beyond "not found" | *"Tail-sitting aircraft are seventy years old and uncrewed ones are ordinary"* restates 1B/1D, but it is the list that the protected *"None of the elements is new"* stands on → keep. Step 7 restates the list; under the restatement rule the cut, if any, belongs there |

## Outbound

| Taken by | What |
|---|---|
| Step 2 | the price that any architecture in the corner pays (*"Section 2 states the cost…"*) |
| Step 7 | *"None of the elements is new"*; the contribution sentence |
| Steps 7, 8 | the declined reaction-torque channel (*"Sections 7 and 8"*) |
| Step 9 | the fixed-wing and multirotor rejections; the four axes |
| Step 15 | the contribution; the gap stated as combination-with-price |
| Supplement S1 | the 1954 programmes and the reviews of them |

## Inbound

None: Step 1 opens the paper. It points forward to Sections 2, 7 and 8.

## Candidate source defects found by opening the sources (to vote; none applied)

- **S-21 (1F).** *"audited explicitly against carried hover mass, exposed cruise drag and hover-sized continuous power, at
  two scales and under three sizing contracts"*. Step 12: *"Bill 1 is not tested"* at scale. My proposal: *"… hover-sized
  continuous power, the last two of them at two scales, and under three sizing contracts."*
- **S-22 (1E).** The DelftaCopter is cited as a second witness to the fixed-pitch compromise, but its rotor is variable-pitch
  (cyclic and collective), and its paper names variable pitch as the way out of that compromise, at a mechanism cost. My
  proposal: keep the quote, and say what the rotor is: *"A long-range tail-sitter reported in 2018 that escapes it with a
  cyclic- and collective-pitch rotor still describes that rotor as 'a compromise …' and selects its diameter on that basis;
  the same paper names variable pitch as the remedy for fixed-pitch propellers, at the cost of extra actuators and the
  weight of the mechanism."* This also documents, in someone else's words, one of the mechanism classes the paper counts.
- **S-23 (1B).** *"tilt-rotors from the 1980s"*: the NASA review gives the XV-3 first hover in August 1955 and the XV-15
  in May 1977. My proposal: *"tilt-rotors from the 1950s"*, or name the two dates.

## Round 94

Inventory confirmed (four + Claude). Applied: 1D *"Precise hovering…"* removed; 1E opener removed; S-21, S-22, S-23
repaired; the 1D declining sentence protected (162). Qwen P2 checked: the antecedent of *"What follows is therefore"* is
1F's *"And the third route is occupied."*, untouched. **Open:** *"No field sustains…"* (Grok, DeepSeek, Qwen keep as voice;
ChatGPT remove) and *"several are in service"* (four different remedies; a candidate source found in Bacchini, crewed
aircraft). Body 1 679 → 1 667.

## Round 95

1B reordered (four + Claude). **Corrected rationale for the 1D removal (ChatGPT):** removed because it duplicated a later and
more fitting home in Step 5E, not because "precise hovering" was unsupported or misnamed — the NASA sources support it.
Still open: *"No field sustains…"* and *"several are in service"*. Qwen quoted the 1D protected sentence in its older S1 form a
second time; the vote is counted for the current wording and Qwen is asked once more.

## Round 96

*"No field sustains…"* removed and *"and several are in service"* removed (four + Claude). **Own check:** the 1B heading still
reads *"The demand has been continuous for seventy years"*; ChatGPT's argument (effort is not proof of need) applies to it too.
