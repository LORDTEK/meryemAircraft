# Step 7 — denial-dependency map and hardware-realization map (Round 125)

These maps are built from the four readers' Round 124 tables: Grok, ChatGPT, DeepSeek and Qwen, with Qwen R122-P2 and Qwen R124-P1
("absence mapping"). **Each target was checked by searching the step bodies**; a row says so where a reader's target did not hold.

## Denial-dependency map

| Step 7 denial or limit | Later text that depends on it |
|---|---|
| *"None of the three elements is new. Each can be found on its own, and some of them together … — Section 1 says where."* | Section 1 (the occupied list; P103, S-45) |
| *"The assembly is not offered as novel because it is an assembly."* (protected) | Section 1 (*"not a claim to an empty field"*); Section 9 |
| *"The instantiation is therefore partial."* (protected) | Section 3 (failure mode 4); Section 9 item 5 (*"It does not claim that the escape condition is fully instantiated"*); Section 11 |
| *"It does not satisfy the condition as stated"* (tilting) | Section 3 (the orientation requirement) |
| *"The stopping class is absent if … a brake or a mechanical lock would add it."* (protected) | Section 8 (*"motor holding torque, an electrical brake, a mechanical lock"*); Section 15 (the conditional count) |
| *"This dual role is a dependency … and it does not make the tip pairs a dedicated lift system."* | Section 5 (the take-off coupling, protected); Section 8; Section 14 (the allocation) |
| *"This is not a configuration in which nothing moves."* (protected) | Section 9 item 3; Section 15 (*"not a claim that nothing moves"*) |
| *"… this configuration declines that channel by design (Section 8)"* | Sections 5, 8, 9 (*"not computed anywhere in this paper"*), 14, 15 |
| *"a claim about eliminated mechanisms that omitted it would be false"* (the strip) | Section 8; Section 9 item 3 |
| *"That is a price of refusing the variable-pitch hub rather than an argument against refusing it … charged in Section 11"* | the table's variable-pitch row (P71); Sections 6 and 11 |
| *"Nor is this a claim of mechanical simplicity."* (protected) | Section 9 item 4; Section 15 |
| *"Whether this aircraft can actually perform the change is … not settled anywhere in this paper"* (protected) | Sections 9, 10, 14, 15 |
| *"The mechanism claim is about hardware and survives that limit. The transition claim is not made."* (protected) | Section 9; Section 15 |
| *"The combination carries costs … Section 11 charges them."* | Section 11 (the tip frames and the free-wheeling attitude rotors in the drag ledger; Qwen R124-P2 checks the receipt when Step 11 is re-read) |

## Hardware-realization map (with absences)

| Claim in Step 7 | Hardware (Section 8) | Kind |
|---|---|---|
| Cruise lift on a surface | the blended-wing-body planform | present |
| One propulsor serves both regimes in one orientation | the single coaxial contra-rotating nose pair, fixed to the body | present |
| Hover peak from a buffer | the series-hybrid buffer | present |
| Attitude: pitch and yaw by differential thrust | the nose pair and the four coaxial tip pairs; the tip frames set the moment arms | present |
| Roll | the variable-extension strip on the lower surface, in two halves; modulated, not switched | present |
| Reaction-torque channel declined | the coaxial pairs run torque-balanced | a choice |
| No pivot, tilting joint or nacelle actuator | none present; the whole body rotates | **absent** |
| No variable-pitch hub | fixed-pitch nose pair and tip pairs | **absent** |
| No dedicated lift rotors | the nose pair serves both regimes; the tip pairs are sized for moments | **absent** |
| No stowing, indexing or stopping mechanism | free-wheel or motor torque; a brake or a lock would add it | **conditionally absent** |
| Actuator inventory | the propulsion motors together with the strip | present |
| Transition not settled | no hardware; a scope statement | — |

**Found while building it — S-50 candidate (from ChatGPT's terminology check).**
- *"Primary propulsor"* is used in Section 3 (generically), Section 5 (*"the primary propulsor supplies a thrust-to-weight ratio of
  exactly one"*) and Section 7 (*"the condition its primary propulsor is designed to satisfy"*).
- It is nowhere identified as the nose pair.
- The nose pair itself is first named in Section 6 (*"the nose pair is left with one job"*) and first described in Section 7.
- So in reading order, Section 5 uses *"the primary propulsor"* and *"the four tip pairs"* before the propulsion has been introduced.
