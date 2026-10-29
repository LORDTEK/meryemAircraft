# Round 229 — After Round 228: the author's decisions, the repairs, and B6 (the blind re-implementation of the frozen text)

**Readers:** the channels of Rounds 226–228. This text was prepared by the Claude session that works in the repository, from the council's message of 2026-10-29.

**This text is self-contained.** It is laid out as follows:
- Section 1 is the council's message (Sections 1–5 of it, translated).
- Section 2 gives every paragraph changed since Round 228, verbatim.
- Section 3 gives the Claude session's checks.
- Section 4 asks the questions.

**State:** v9; 27 pages; abstract 248 words (counted here: 248). The council reports that the content work of Phase 3 is done.

---

## 1. The council's message, translated

> **1. The author's Round 228 decisions**
>
> | Topic | Decision | Council |
> |---|---|---|
> | Title | Grok's stays: **meryemAircraft: Regime Change by Rotating the Airframe, Without Reorienting a Propulsor** | No objection from anyone. Qwen's hybrid title will be reconsidered at the last look before submission (the author noted: hyphenation and length rules, punch). |
> | Rotorcraft clause in the abstract (L4) | Form (a). The result is given only at the paper's closures, with the assumed frame drag: "13 to 51 percent above a turboshaft quadrotor's". The envelope (−14 … +71 percent) stays in Section 4.1. | Grok, Codex, Qwen, GLM and DeepSeek raised no serious objection. Condition: the scope must be written in the sentence. It is. |
> | Simplicity basis (L5) | The author's sentence: "A fixed structure is inherently less complex than a moving mechanism, and this aircraft carries none of the mechanism classes of Table 3; it is therefore mechanically simpler than a tilting architecture, though not one in which nothing moves. No comparison of part count, mass or reliability is made." | Grok, Qwen, GLM and DeepSeek did not object. Codex objected seriously (a universal proposition). The author's rule was "if you object jointly"; a single objection does not meet it, so the sentence went in. Codex's objection is on record. |
>
> **2. The Round 228 items applied**
>
> | # | What was done |
> |---|---|
> | L1 | The 20.7 N·m point was run with the existing 3-DOF code (FM 0.599, momentum on one disc's area: 14.6 N per pair). With the vortex-lattice moment the transition completes, with a 12.2 m loss and 0.57 s of saturation. The text now says that 17.6 N·m is "FM 0.599 plus a 15 percent coaxial interference loss" (the v5 definition); at that point it saturates and tumbles. The text gives three tested points and says they are not a threshold. 16.2 N / 335 W is labelled "the reference design's assumed value". Bill 2, S7 and S8a were updated together. |
> | L2 | The script's output is used: 2.5–2.7 N·m at a 10 percent torque imbalance, 7.5–8.2 N·m at 30 percent. The imbalance is in torque, not in speed. 10 percent clears the first screen; 30 percent clears both. |
> | L3 | "50 to 69 percent across the two rotor sources with the frames at 0.15". |
> | L6 | Highlight 5: "Table S2a lists every input of the sizing loop and its provenance." |
> | L8 | S9 row 5 points to S8a; what stays open is only the reserve and the recharge profile. |
> | [S2] | The datasheet was opened: 6 kW continuous (48 V) and 7.5 kW (60 V), 337 g cased. The text gives these values. |
> | Grammar | "...is made". |
> | Sign change | In the abstract, with the contract's name: "under a fixed takeoff mass". |
> | N1 | Added to Section 4.1: the corners carry Table 4's frame drag. Across the envelope (L/D)e is 4.19–8.40: −14 … +71 percent against the turboshaft quadrotor, −28 … +45 percent against the all-electric one. |
> | References | [27]'s DOI was checked at OSTI (10.2172/6548367). [S1] was checked in the paper itself: MacNeill and Verstraete, 1,743 motors, Eq. 6. [S3] was checked at J-STAGE (pp. 439–445). |
>
> **3. B6: independent re-implementation from the frozen text**
> - **Freeze.** The text was frozen in git under the tag `v9-freeze-b6`; SHA-256 hashes recorded. Which values are tests and which are calibration targets was written before the run.
> - **Implementers.** Two AI models saw only main_v9.tex and supp.tex, not the code.
> - **What was produced.** They wrote scripts that reproduce Table 4, Table 6 and Table S4a. Claude ran the scripts and compared 58 values.
>
> | Implementer | Result |
> |---|---|
> | Qwen | All 56 counted values within 0.15 percent (largest 0.143 percent). Two values of Table 6 were not counted: Qwen back-solved the bench store's specific power from those two masses. |
> | DeepSeek | Table 4 and S4a within 0.12 percent; all 56 values within 0.5 percent. The same two masses of Table 6 at −0.65 and −0.72 percent. |
>
> The run found two gaps in the text, corrected after it:
> 1. Table 6 and S8 gave the bench store as "1.5 kW/kg"; the computation used 1.49. The label now reads 1.49.
> 2. The text did not say that the empty fraction includes the 3.6 percent buffer; DeepSeek had to infer it. Table 4's footnote now says so.
>
> The reproducibility paragraph in the paper states this result as it is. The old caveat "not repeated on this text" is gone, because it has now been repeated.
>
> **4. Final forms:** title, abstract and highlights as in Section 2 (highlights: the Round 228 five, with highlight 5 as in L6 above).
>
> **5. What we ask you**
> 1. Do you object to how the reproducibility paragraph states the B6 result (full text in Section 2)?
> 2. Is the three-point account of L1 (Bill 2 and S7) right, in your view?
> 3. Is a last reading round needed before submission, or can we move to the administrative work (cover letter, declarations, CRediT, photographs and vitae, Zenodo)?

---

## 2. The text changed since Round 228, verbatim

### Body

```latex
\begin{abstract}
Hybrid vertical-takeoff aircraft change between hover and cruise either by carrying two sets of propulsors or by reorienting one. meryemAircraft, a 50 kg tail-sitting blended-wing body for a 13 kg payload, does neither: its fixed-pitch coaxial pairs keep one body-relative orientation and the whole airframe rotates, so it carries none of the mechanism classes a tilting architecture uses to change regime. This paper prices that architecture. Hover is priced in three costs, carried hover mass, exposed cruise drag and continuous power sized to the hover peak, on a buffered series hybrid. The nose pair, which provides both hover and cruise thrust, incurs none of the three; the attitude-control tip pairs and their frames stay in the cruise flow and account for 50 to 80 percent of zero-lift drag across the drag sources examined. The sizing loop closes at 52.3 to 57.5 kg with the assumed frame drag, where the effective lift-to-drag ratio is 13 to 51 percent above a turboshaft quadrotor's; across the drag sources examined the envelope, not a confidence interval, is 50.7 to 66.1 kg and 699 to 1,401 km. Against a lift-plus-cruise layout, the range advantage shifts by 67 to 77 percentage points across three sizing contracts and changes sign across the four closures under a fixed takeoff mass, so the ranking depends on the contract. No store reported as built delivers the required specific power, the roll strip's hover heading authority is not established, the transition is not settled, and landing is not analysed.
\end{abstract}
```

```latex
\paragraph{Control} Body-axis names are used throughout; the longitudinal axis is the roll axis in both regimes, so a moment about it appears as a heading change in hover and as bank in cruise. Pitch and yaw come from differential thrust of the tip pairs, at arms of 0.71~m (pitch) and 1.726~m (yaw, the semi-span) (Fig.~\ref{fig:arms}); the same differential thrust is assigned to rotate the airframe through transition. Since every thrust vector is parallel to the roll axis, no combination of thrust settings produces a roll moment. The reaction-torque channel of the coaxial pairs could~\cite{r8}, but this configuration operates every pair torque-balanced and assigns roll to a single modulated strip on the lower surface, about 46 percent of which is estimated to lie in the nose-pair slipstream and so to work at zero airspeed; the slipstream boundary is not derived (Supplement S6). In hover the thrust axis has no aerodynamic damping, and the strip's own normal force in the nose-pair slipstream gives 0.6 to 1.4~N\,m about it. No handling-qualities standard consulted here states a hover heading requirement for this class; as stated screens, a 90$^\circ$ rest-to-rest heading turn in 10~s needs 1.6~N\,m and a heading rate of 20$^\circ$\,s$^{-1}$ reached in 1.5~s needs 5.8~N\,m. Moments of 6 to 12~N\,m would require a lift increment of 0.1 to 0.2 on the half wing in the slipstream, which is assumed and not predicted for this geometry. The strip's hover heading authority is therefore not established here. The reaction-torque channel this configuration declines has the magnitude to cover the screens: a torque imbalance of one nose rotor of 10 percent gives 2.5 to 2.7~N\,m, above the first, and of 30 percent 7.5 to 8.2~N\,m, above both; its cost in power and in the other axes is not computed (Supplement S6). Directional stability comes from the fairing on the tip frames, which needs a chord of 31 to 52~mm for lateral lift-curve slopes of 5.0 to 3.0 per radian~\cite{r24}; attitude is to be closed by a flight computer whose control loop is not designed here (Sec.~\ref{sec:discussion}).
```

```latex
\paragraph{Mechanism classes} Table~\ref{tab:mechanisms} counts the mechanism classes that other hybrid architectures use to change regime or to remove a rotor from one regime's flow. Beyond the rotation of the rotors, the only part of this aircraft that changes configuration is the strip, deployable in two halves (one for roll, both as a speed brake); the actuator inventory is the propulsion machines plus the strip. A fixed structure is inherently less complex than a moving mechanism, and this aircraft carries none of the mechanism classes of Table~\ref{tab:mechanisms}; it is therefore mechanically simpler than a tilting architecture, though not one in which nothing moves. No comparison of part count, mass or reliability is made.
```

```latex
\paragraph{Reproducibility} The code, inputs and scripts that produce every table are deposited with a DOI (Data availability). As a check that the text is sufficient, the closures were re-implemented twice from the manuscript and supplement of this version alone, frozen before the run, without access to the code, by two separate generative AI assistants, each instructed to mark every input it had to assume or back-solve. All inputs of the loop are stated in Table S2a, and neither re-implementation back-solved one. Of the 58 tabulated values compared (Table~\ref{tab:closures}, Table~\ref{tab:store} and Supplement Table S4a), one re-implementation reproduced every value within 0.15 percent except the two masses at the bench-average store, from which it back-solved that store's specific power and which are therefore not counted; the other reproduced 56 within 0.5 percent and those two within 0.72 percent, because Table~\ref{tab:store} gave the store as 1.5 rather than the 1.49~kW/kg used. That label, and the statement that the empty fraction includes the buffer, which one re-implementation had to infer, were corrected after the run. This is a check of reproducibility, not an external validation.
```

```latex
The NASA sizing set of Sec.~\ref{sec:nasa} gives effective lift-to-drag ratios for two quadrotors and two helicopter types on a common mission~\cite{r16}. Against the turboshaft quadrotor (4.9) the effective lift-to-drag ratio of the present configuration is 13 to 51 percent higher at every corner; closing that margin would require a propeller efficiency of 0.557. Against the all-electric quadrotor (5.8) it ranges from 4 percent behind to 27 percent ahead. Against the helicopters (5.4 to 7.2) the result is mixed. These corners carry the frame drag of Table~\ref{tab:closures}; across the drag sources of Supplement Table S4a the effective lift-to-drag ratio spans 4.19 to 8.40, from 14 percent behind to 71 percent ahead of the turboshaft quadrotor and from 28 percent behind to 45 percent ahead of the all-electric one. These are figures from independently produced analyses in a common definition, not a controlled comparison: the NASA rotorcraft are 1,660 to 3,275~kg against 50~kg here, a scale that favours them; they are quoted at best-range speed and this configuration at its cruise point of 1.49 times stall, faster than its lift-to-drag optimum at 1.14 to 1.23 times stall (Supplement S5); and they are sized at 5,000~ft and ISA+20$^\circ$C against sea level here, a mismatch whose direction has not been computed.
```

```latex
\smallskip
{\footnotesize $f_{\mathrm{empty}}$: empty fraction, including the 3.6 percent buffer; $P_{\mathrm{hover}}$: rotor-shaft hover power; $P_{\mathrm{eng}}$: engine shaft rating. Ranges scale linearly with the fuel-to-shaft energy product of Table S2a. $^{a}$Extremes over the rotor-section and frame-drag sources examined in Supplement Table S4a: an envelope of those sources, not a confidence interval and not a further closure.}
\end{table}
```

```latex
\paragraph{Bill 2} In the drag build-up, the hardware the vertical phase leaves in the cruise flow (the tip frames and the free-wheeling tip rotors) is 69 percent of the zero-lift drag at the favourable end of the bracket and 57 percent at the adverse end (50 to 69 percent across the two rotor sources with the frames at 0.15, and 50 to 80 percent across all the drag sources of Supplement Table S4a); the rotor term alone is 0.0154 at the favourable end. This is an estimate resting on computed section polars at a Reynolds number of about $8 \times 10^4$, not a measurement. Stopping the tip rotors offers no reduction: with the rotor axis parallel to the cruise flow, a stopped fixed-pitch blade presents the same projected area at any azimuth, and an edge-on state would require feathering. Without the tip frames and rotors, the lift-to-drag ratio would be 20.55 and 15.24; the configuration retains 52.6 and 57.7 percent of it. Because range at fixed fuel fraction, propeller efficiency and chain efficiency is proportional to the lift-to-drag ratio, the tip hardware costs 42.3 to 47.4 percent of the range the same airframe would reach without it; this prices the drag and describes no other aircraft, since without the tip pairs the airframe cannot hover. The tip discs are not reduced to cut this drag. With the linear vortex-lattice pitching moment, the rotation completes at 23.0~N\,m, the moment from the reference design's assumed 16.2~N and 335~W per tip pair; at 20.7~N\,m, the moment at the sizing figure of merit of 0.599, it still completes but saturates for 0.6~s; and with a further 15 percent coaxial interference loss, 17.6~N\,m, it saturates and tumbles (Supplement S7). The same pairs supply the takeoff margin.
```

```latex
\begin{table}[!htbp]
\centering
\caption{Sizing loop re-closed with the buffer derived at a given specific power (all other inputs as in Table~\ref{tab:closures}).}
\label{tab:store}
\footnotesize
\begin{tabularx}{\linewidth}{Xrrr}
\toprule
Buffer specific power & Takeoff mass & Buffer fraction & Change in takeoff mass \\
\midrule
5.5 to 6.1~kW/kg (implied by Table~\ref{tab:closures}) & 52.3 to 57.5~kg & 3.6\% & --- \\
4~kW/kg (design-study assumption~\cite{r26}) & 56.6 to 61.2~kg & 5.0 to 5.5\% & +6.5 to +8.2\% \\
1.49~kW/kg (bench average~\cite{r25}) & 94.6 to 101.2~kg & 13.4 to 14.7\% & +76 to +81\% \\
0.892~kW/kg (listed continuous~\cite{r25}) & about 335~kg & 22 to 25\% & +480 to +540\% \\
0.724~kW/kg (test-pack continuous~\cite{r25}) & does not close & --- & --- \\
\bottomrule
\end{tabularx}
\end{table}
```

### Supplement

**Table S0, row 2** (the only change in Table S0):

```latex
It is therefore mechanically simpler than a tilting architecture, in that sense only & Sec. 3.1 & Mechanism-class count; part count, mass and reliability not compared & As row 1; part count, mass and reliability are not compared \\
```

**S6:**

```latex
In the nose-pair slipstream (dynamic pressure 434~N\,m$^{-2}$), the strip's own normal force at a coefficient of 0.6 to 1.4 gives 0.60 to 1.40~N\,m. This is below both screens. A larger moment would come from a change of circulation on the half wing in the slipstream: a lift increment of 0.10 to 0.20 on that 0.49~m$^2$ gives 6.0 to 12.0~N\,m. The increment is assumed by analogy with spoilers and Gurney strips and is not predicted for this geometry. For scale, one nose rotor produces 25 to 27~N\,m of reaction torque in hover; with torque proportional to the square of rotational speed, 1~N\,m balances a speed mismatch of about 2 percent between the two motors of that pair, and an uncorrected bias of only 0.18~N\,m moves the heading by 5$^\circ$ in 5~s from rest. The strip's response also has a dead band: below 1 percent of the local chord the protrusion is reported to have negligible effect [24], so the strip does nothing below about 7 percent of its stroke and gives 4 percent of its full moment at 10 percent. The strip's hover heading authority is therefore not established here. The reaction-torque channel this configuration declines is of the size the screens require: from 24.9 to 27.5 N\,m per nose rotor, a 10 percent torque imbalance of one rotor gives 2.5 to 2.7 N\,m and a 30 percent imbalance 7.5 to 8.2 N\,m (\texttt{aero/reaction\_torque.py}; the imbalance is in torque, not in rotational speed). Its cost in power and in the other axes is not computed, and it is not claimed here to close the heading channel. The computation is in \texttt{aero/roll.py}.
```

**S7:**

```latex
The 50 kg design is rotated in a three-degree-of-freedom model: the body angle follows a reference profile through a proportional-derivative controller whose moment is limited to the available control moment of 23.0 N$\cdot$m, with a rotation time of 2 s, an entry climb of 5 m s$^{-1}$, and the aerodynamic pitching moment set to zero. The loss persists across three reference profiles: 5.43 m with a linear profile, 6.33 m with a smooth (cubic) one and 6.57 m with a bang-bang one, which is the body's 5.4 to 6.6 m. In none of the three does the control moment saturate. Raising the gains increases the loss rather than removing it: with the proportional gain raised sixteen-fold and the derivative gain four-fold, the loss is 16.9 m, again without saturation. With the computed zero-lift bracket and Oswald factor of 0.817, in place of the reference design's assumed 0.0248 and 0.85, each figure moves by at most 0.02 m. Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the maneuver costs altitude. The tip pairs show no margin to shrink. Their thrust, 16.2 N at 335 W per tip pair, is the reference design's rating, implying a figure of merit of 0.702, and gives the 23.0 N$\cdot$m above; with the linear vortex-lattice pitching moment the rotation then completes without saturation, losing 12.2 m. The figure of merit is computed on the area of one disc. At the figure of merit of 0.599 used in sizing, momentum theory gives 14.6 N per pair at 335 W and a moment of 20.7 N$\cdot$m; with the same pitching moment the rotation completes, losing 12.2 m, but saturates for 0.57 s. With a further 15 percent coaxial interference loss the pair gives 12.4 N and the moment 17.6 N$\cdot$m, and the rotation saturates after 1.5 s and tumbles; with the moment set to zero it completes at all three. These are three tested points, not a threshold. No smaller tip disc is therefore examined.
```

**Table S8:**

```latex
\begin{table}[htbp]
\centering
\caption*{Table S8}
\small
\begin{tabularx}{\linewidth}{Xrrr}
\hline
Buffer specific power, per kilogram of buffer & Takeoff mass & Buffer & Change from Sec. 4.2 \\ \hline
As Sec. 4.2 implies: 5.5 to 6.1 kW kg$^{-1}$ & 52.3 to 57.5 kg & 3.6\% & --- \\
4 kW kg$^{-1}$, the design-study assumption [26] & 56.6 to 61.2 kg & 5.0 to 5.5\% & +6.5 to +8.2\% \\
1.49 kW kg$^{-1}$, the unit pack's bench rate & 94.6 to 101.2 kg & 13.4 to 14.7\% & +76 to +81\% \\
0.892 kW kg$^{-1}$, the onboard system's listed continuous figure & about 335 kg & 22 to 25\% & set by nearness to non-closure \\
0.724 kW kg$^{-1}$, the test pack's validated continuous figure & does not close & --- & --- \\
\hline
\end{tabularx}
\end{table}
```

**Table S8a, the two rows that changed** (the other seven rows are as in Round 228):

```latex
Electrical path mass & Nose machines sized to the hover peak at 4 kW kg$^{-1}$, tip motors, power electronics at 20 kW kg$^{-1}$ and cabling, inside the fixed 0.108 propulsion fraction (reference budget; Supplement S8) & A regression on 1,743 small electric motors [S1] and an inverter rated 6 kW continuous at 48 V and 7.5 kW at 60 V, 337 g cased [S2], give 2.3 to 3.1 kg for machines and inverters, below the about 3.7 kg the budget carries & Carried at assumed specific powers, not re-rated; heat rejection not sized \\
Transition moment & 23.0 N$\cdot$m from the reference design's assumed 16.2 N and 335 W per tip pair (figure of merit 0.702), aerodynamic pitching moment zero & With the vortex-lattice moment: completes at 23.0 N$\cdot$m; at 20.7 N$\cdot$m (sizing figure of merit 0.599) completes with 0.57 s of saturation; at 17.6 N$\cdot$m (with 15 percent coaxial interference) saturates and tumbles (Supplement S7) & Computed, not settled; depends on the moment model \\
```

**Table S9, row 5** (the only row that changed):

```latex
The buffer's energy, not only its power. The energy gate and the cruise recharge time are in Table S8a; what remains open is the reserve and the recharge profile, which depend on a mission profile this work does not fix. & Whether the store sized by power is also large enough & Analysis against a defined mission profile \\
```

---

## 3. Checks by the Claude session

These are facts with their basis; the Claude session's positions go beside everyone's next round. They are ordered by how much they could change the paper.

**M1. Which of the three transition points describes this aircraft depends on whether 0.599 already includes coaxial interference.** S7 says *"The figure of merit is computed on the area of one disc."* For a coaxial pair, a figure of merit on one disc's area is normally the pair's system figure of merit, which already contains the interference between the two rotors.
- If the sizing figure of merit 0.599 is such a pair value, the *"further 15 percent coaxial interference loss"* counts the interference twice. The aircraft's point is then 20.7 N·m, where the transition completes with 0.57 s of saturation.
- If 0.599 is an isolated-rotor value, the 15 percent is correct. The aircraft's point is then 17.6 N·m, and it tumbles.

The text now presents three points without saying which is the aircraft's. Is 0.599 (and the reference design's 0.702) a pair value or an isolated-rotor value? Where does the 15 percent come from (the council cites *"the v5 definition"*)?

**M2. Two runs report the same loss.** S7 gives 12.2 m at 23.0 N·m, without saturation, and 12.2 m at 20.7 N·m, with 0.57 s of saturation. A different moment limit with a period of saturation would normally change the loss somewhat. If both are correct to one decimal, a sentence saying so would prevent a reader from taking one as copied from the other.

**M3. The reproducibility paragraph contradicts itself in one place.** It says *"All inputs of the loop are stated in Table S2a, and neither re-implementation back-solved one."* Two sentences later it says one implementer *"back-solved that store's specific power"* from the two masses at the bench-average store.

The two statements can both be true only if Table 6's store specific powers are not "inputs of the loop". Either the first sentence is scoped (for example "no input of Table S2a was back-solved"), or the exception is named in it.

**M4. "58 tabulated values" needs its list.** The count of computed cells is larger than 58:
- Table 4: 7 computed columns × 4 closures.
- Table S4a: 4 numbers × 2 ends × 6 cases.
- Table 6 adds more.

The 58 is therefore a selection. The list of the 58 values, with which are tests and which are calibration targets (decided before the run, as the council reports), should be deposited with the re-implementation files and referred to from the paragraph.

**M5. The text compared in B6 is not the final text.** Two corrections were made after the run (1.49, and the buffer in the empty fraction). The paragraph says so. The data-availability deposit should then hold both:
- the frozen text (`v9-freeze-b6`, with its SHA-256), which is the one B6 tested;
- the final text.

That way a reader can see the difference is only those two corrections.

**M6. The simplicity sentence and Table S0, row 2.** The body now states a general premise (*"A fixed structure is inherently less complex than a moving mechanism"*). Table S0, row 2, still calls the claim *"mechanically simpler than a tilting architecture, in that sense only"*. That is the author's decision; Codex's objection is on record.

The two places now describe the claim at different scopes. If the body's premise is the basis, S0 row 2 could name it, with its refuter (*"As row 1"*).

**M7. "A turboshaft quadrotor's".** The abstract dropped *"published"* from the Round 228 wording. Without it, a reader may take the 13–51 percent as a comparison the paper computed. Sec. 4.1 says what it is: figures from independently produced analyses, not a controlled comparison. One word restores that in the abstract; the word count is 248.

**M8. Arithmetic that rebuilds:**
- 14.6 × 0.85 = 12.4 N, so 17.6 N·m follows.
- 335/57.5 = 5.83 and 335/52.3 = 6.41, which gives +483 to +541 percent (Table 6: *"+480 to +540%"*).
- 6 kW / 0.337 kg = 17.8 kW/kg, the figure used before.
- The envelope comparisons in Sec. 4.1 match Round 228's N1.

**M9. Still not read against the target journal.** *Aerospace Science and Technology*'s guide for authors has not been quoted in any round. The following rest on that guide:
- the abstract limit (248 words now);
- the highlights rule;
- the word or page count;
- the declarations (competing interest, AI use);
- the vitae and photographs.

The standing rule is that a target journal's requirements are read in full and checked item by item before submission. This belongs to the administrative step the council proposes. It should be done before the cover letter, not after.

**M10. No one has read the current v9 end to end.** Since v9 entered these rounds (Round 226), every round has carried only the changed passages. The readers have seen the whole of v9 once, before Phase 1, and the whole of the supplement not at all. This bears on Q3.

---

## 4. Questions

**Q1. The reproducibility paragraph.** Do you object to how it states the B6 result? Take M3, M4 and M5 into account.

**Q2. L1's three points.** Is the account in Bill 2 and S7 right? Answer M1 if you can: is a figure of merit on one disc's area for a coaxial pair a system value that already contains the interference? Say also whether the text should state which point is the aircraft's.

**Q3. A last reading round or administration.** Is a last reading round needed before the administrative work? If yes, of what: the whole body, the whole supplement, or both? Take M9 and M10 into account.

**Q4. M2, M6 and M7.** Accept, amend or reject each, with a reason.

**Q5. Open proposals,** each with its reason.

---

## 5. Errors (one list, all sources)

None recorded this round beyond those of Rounds 226–228, which are closed.

## 6. Answer format

Give your channel name first, then Q1–Q5 by number. Where you disagree with another channel, name it and answer its reason.

## 7. What goes to the author after this round

- **Q3:** whether a last reading round is held, and of what.
- **M1:** which transition point is the aircraft's. It bears on whether the paper can say that the rotation completes at the sizing assumptions.
- **M9:** the reading of the target journal's guide, before the cover letter.
