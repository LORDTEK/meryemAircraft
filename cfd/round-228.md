# Round 228 — After Phase 1: the Round 227 repairs, Phase 2 closed without additions, and the Phase 3 draft (title, abstract, highlights, conclusions)

**Readers:** the channels of Rounds 226–227. This text was prepared by the Claude session that works in the repository, from the council's message of 2026-10-29. The council's work (Grok and Codex as members; Qwen, DeepSeek and GLM as API guests) is in its own commits and agora rounds.

**This text is self-contained.** Section 1 is the council's message (Sections 1–5 of it, translated). Section 2 gives every paragraph changed since the Phase 1 report, verbatim. Section 3 gives the Claude session's checks of that text. Section 4 asks the questions.

**State reported by the council:** v9; 26 pages; about 8,900 words in the PDF; abstract 245 words.

**The author's decisions since Round 227:**
- Table 4 option (c).
- Section 3.1: *"The strip's hover heading authority is not established here,"* followed by one sentence on the declined reaction-torque channel.
- The simplicity sentence in the bounded form (Section 2, *Mechanism classes*).

---

## 1. The council's message, translated

> **1. What you asked for in Round 227 was applied**
>
> | Item | What was done |
> |---|---|
> | Q1(c) | Table 4 keeps its four closures. An "Envelope" row is added below them: 50.7–66.1 kg and 699–1,401 km. Its label: "envelope of the sources in Supplement Table S4a; not a confidence interval, not a further closure". The abstract gives both. |
> | Q2 | The tip hardware's share is written with its scope everywhere: 50–69 percent with the 0.15 frame, 50–80 percent across all of S4a. Places: abstract, 4.3, 5.1, conclusions, S0. |
> | (b) Hover heading (author's decision) | "The strip's hover heading authority is not established here." Then one sentence: the declined reaction-torque channel is large enough to meet the screens (a 10 percent imbalance of one nose rotor gives 2.5–2.8 N·m); its cost is not computed, and it is not written as a solution. Five of five AI channels chose this option. |
> | (c) Simplicity (author's decision) | Bounded form: "In the sense of these mechanism classes ... no general claim about the complexity of moving parts." |
> | K1 | Written in the Bill 2 paragraph (4.3) as two tested points. At 23.0 N·m (16.2 N and 335 W per pair, FM 0.702), the transition completes with a 12.2 m loss. At 17.6 N·m (the sizing FM 0.599), it saturates and tumbles. It is not presented as a threshold. Also in S7 and S8a. |
> | K2 (Claude's error) | The electrical path's mass lies inside the fixed 0.108 fraction (v7 S2.1 budget). S8, S8a, S9, Bill 3 and the Limitations were corrected. An unexplained difference of 0.40 kg is stated. Heat rejection is not sized. |
> | K3 | The reaction-torque magnitude stays in S6 as scale information only: 2.5–2.8 N·m at 10 percent and 7.5–8.3 N·m at 30 percent. |
> | K5 | The S4a caption now says "mass and range sensitivity". Control margins were computed only for 50 kg and 0.20 m, and the caption says so. |
> | K6 | Added to the references: [27] Sheldahl–Klimas, [28] Hoerner. The supplement's own references: [S1] MacNeill and Verstraete, ICAS 2018 (1,743 motors, checked against the paper); [S2] the 6 kW inverter datasheet; [S3] Ohtake et al. 2007. |
> | L4H19 | NACA ACR L4H19, cited for the dead band, turned out to be NACA Report 796 itself, already [24]. No separate source was added; the citation points to [24]. |
> | [r7] | The axis is written in the source's naming: "the source's $x_b$ axis". |
> | K8 | The hover screen is 5.8 N·m everywhere. 8.79 in S4a. The S7 sentence on 0.0248 / 0.85 is corrected. The store mass ratio stays as the 5.8–6.4 band. |
> | K9 | "Not refutable" is gone from S0 row 2; it points to row 1's refuter. |
>
> Repository note: the comment at `aero/baseline.py:66` and the new scripts will be corrected when repository access is open.
>
> **2. Phase 2: nothing was added to the text**
>
> Every Phase 2 item depended on a Phase 1 result:
> - **Fairing and diameter sensitivity (B2):** cut. 8b shows no room to shrink the tip discs.
> - **Feasibility map:** not drawn. S8a carries the same information; a map would only redraw it.
> - **2-D RANS for the frame:** no. The 40 percent threshold held. At Re ≈ 8×10⁴ the result would depend on the transition model; without a validated transition model it cannot decide between 0.15 and 0.42–0.68.
> - **Transition envelope, gyroscopic number, "how to audit" box:** no. All four of you were against the transition envelope.
>
> Grok and Codex did not object to this resolution.
>
> **3. Phase 3 draft**
>
> Title candidates (the author leans to 1; do you have a major objection?):
> 1. **meryemAircraft: Regime Change by Rotating the Airframe, Without Reorienting a Propulsor** (Grok). This is in the paper now.
> 2. meryemAircraft: A Tail-Sitting Blended-Wing Body That Changes Regime by Airframe Rotation (Grok)
> 3. meryemAircraft: A Blended-Wing-Body Tail-Sitter with Body-Fixed Coaxial Propulsors (Codex)
> 4. meryemAircraft: A Series-Hybrid Tail-Sitter with a Rotating Blended-Wing Body (Codex)
>
> Abstract: 245 words (in Section 2). Removed from the previous abstract: the NASA comparison's 9.4 percent, (L/D)e 5.56–7.39, and the store's 3.7–4.1 times. Grok and Codex proposed the same list. The store, hover heading, transition and landing stand in the last sentence without numbers.
>
> Keywords: hybrid VTOL · tail-sitter · blended wing body · airframe rotation · aircraft sizing · sizing contracts ("cost accounting" removed).
>
> Highlights (each under 85 characters):
> ```
> A tail-sitting blended-wing body changes regime with no propulsor reorientation.
> Hover priced as carried mass, exposed drag and power sized to the hover peak.
> Attitude tip pairs and frames take 50-80% of zero-lift drag across drag sources.
> Range rankings vs lift-plus-cruise shift 67-77 points across sizing contracts.
> Every input needed to reproduce each sizing closure is stated.
> ```
>
> The conclusion paragraph opens with the architecture (full text in Section 2).
>
> **4. Next step: B6.** Once the title and abstract are frozen, the text is frozen and hashed. One AI then re-implements the closures from the text alone, without the code. Calibration targets (back-solved inputs) and tests are separated before the run; back-solved values are not counted as "reproduced". The final reproducibility sentence is written after B6.
>
> **5. What we ask you**
> 1. Do you have a major objection to title 1?
> 2. Is there anything you would not let drop from the abstract, or a wording you find wrong?
> 3. Do you object to Phase 2's "no additions" resolution?
> 4. Is any item in Section 6 applied wrongly, in your view?

---

## 2. The text changed since the Phase 1 report, verbatim

### Body

```latex
\title{meryemAircraft: Regime Change by Rotating the Airframe, Without Reorienting a Propulsor}
```

```latex
\begin{abstract}
Hybrid vertical-takeoff aircraft change between hover and cruise either by carrying two sets of propulsors or by reorienting one. meryemAircraft, a 50 kg tail-sitting blended-wing body for a 13 kg payload, does neither: its fixed-pitch coaxial pairs keep one body-relative orientation and the whole airframe rotates, so it carries none of the mechanism classes a tilting architecture uses to change regime. This paper prices that architecture. The price of hover is divided into three costs, carried hover mass, exposed cruise drag and continuous power sized to the hover peak, and the aircraft is closed on a buffered series hybrid. The nose pair, which provides both hover and cruise thrust, incurs none of the three; the attitude-control tip pairs and their frames stay in the cruise flow and account for 50 to 80 percent of zero-lift drag across the drag sources examined. The sizing loop closes at 52.3 to 57.5 kg; across the rotor-section and frame-drag sources examined, the envelope, not a confidence interval, is 50.7 to 66.1 kg and 699 to 1,401 km. Against a lift-plus-cruise layout, the range advantage shifts by 67 to 77 percentage points across three sizing contracts and changes sign at two of four closures under one, so the ranking depends on what the comparison holds equal. No energy store reported as built delivers the specific power the closures require, the roll strip's hover heading authority is not established, the transition is computed but not settled, and landing is not analysed.
\end{abstract}
```

```latex
\begin{keyword}
hybrid VTOL \sep tail-sitter \sep blended wing body \sep airframe rotation \sep aircraft sizing \sep sizing contracts
\end{keyword}
```

```latex
\begin{table}[!htbp]
\centering
\caption{Closest prior work. Entries restate what each reference reports; ``not stated'' means the reference, as cited here, does not report it.}
\label{tab:lit}
\scriptsize
\begin{tabularx}{\linewidth}{@{}l>{\raggedright\arraybackslash\hsize=.8\hsize}X>{\raggedright\arraybackslash\hsize=.8\hsize}X>{\raggedright\arraybackslash\hsize=1.6\hsize}X>{\raggedright\arraybackslash\hsize=.8\hsize}X@{}}
\toprule
Ref. & Airframe & Propulsors & Reported conversion and hover-control mechanisms & Power / evidence \\
\midrule
\cite{r1} & Crewed tail-sitter, 1954 & One turboprop & Not stated & Flown; six transitions \\
\cite{r2} & Delta biplane tail-sitter & Main rotor; wingtip rotors & Airframe rotates about 90$^\circ$; main-rotor cyclic and collective pitch; wingtip rotors and ailerons balance main-rotor torque & Flown \\
\cite{r3} & Quadrotor tail-sitter & Four rotors & Differential rotor thrust and torque; no control surfaces & Hover, transition and level flight, experimentally verified \\
\cite{r4} & Tail-sitter & Not stated & Differential rotor speed; elevator and ailerons in propeller wash & Transition control study \\
\cite{r5} & Convertible mini-UAV & Coaxial contra-rotating & Counter-rotation cancels reaction torque; other channels not stated & Hover control model \\
\cite{r6} & Tail-sitter MAV & Coaxial pair & Elevon and rudder in slipstream & Hover attitude control \\
\cite{r7} & Flying-wing tail-sitter & Two counter-rotating propellers & Differential thrust about the source's $x_b$ axis; elevons for the other two axes & Hover and vertical flight \\
\cite{r8} & Tail-sitter (several layouts) & Coaxial contra-rotating & Coaxial layout: differential motor speed; stabilizer and rudder & Lift-system design \\
\cite{r9} & Blended-wing-body tail-sitter & Contra-rotating pusher & Control surfaces and propeller effectiveness discussed; control allocation and blade pitch not stated & VLM and RANS analysis \\
\cite{r10} & 100 kg winged biplane tail-sitter & Four, six or eight rotors; fixed-pitch rotor model & Not stated & Sized: engine for cruise, boost battery for VTOL \\
\cite{r11} & Coaxial tail-sitter with fuselage and tails & Coaxial & Not stated & Sized: fuel cell charging a battery \\
This work & Blended-wing-body tail-sitter & Five coaxial pairs, fixed pitch and fixed mounting & Airframe rotation; differential thrust of coaxial pairs, torque-balanced in cruise; one lower-surface strip & Sized; accounting and contracts \\
\bottomrule
\end{tabularx}
\end{table}
```

```latex
\paragraph{Control} Body-axis names are used throughout; the longitudinal axis is the roll axis in both regimes, so a moment about it appears as a heading change in hover and as bank in cruise. Pitch and yaw come from differential thrust of the tip pairs, at arms of 0.71~m (pitch) and 1.726~m (yaw, the semi-span) (Fig.~\ref{fig:arms}); the same differential thrust is assigned to rotate the airframe through transition. Since every thrust vector is parallel to the roll axis, no combination of thrust settings produces a roll moment. The reaction-torque channel of the coaxial pairs could~\cite{r8}, but this configuration operates every pair torque-balanced and assigns roll to a single modulated strip on the lower surface, about 46 percent of which is estimated to lie in the nose-pair slipstream and so to work at zero airspeed; the slipstream boundary is not derived (Supplement S6). In hover the thrust axis has no aerodynamic damping, and the strip's own normal force in the nose-pair slipstream gives 0.6 to 1.4~N\,m about it. No handling-qualities standard consulted here states a hover heading requirement for this class; as stated screens, a 90$^\circ$ rest-to-rest heading turn in 10~s needs 1.6~N\,m and a heading rate of 20$^\circ$\,s$^{-1}$ reached in 1.5~s needs 5.8~N\,m. Moments of 6 to 12~N\,m would require a lift increment of 0.1 to 0.2 on the half wing in the slipstream, which is assumed and not predicted for this geometry. The strip's hover heading authority is therefore not established here. The reaction-torque channel this configuration declines has the magnitude to cover both screens, 2.5 to 2.8~N\,m at a 10 percent torque imbalance of one nose rotor; its cost in power and in the other axes is not computed (Supplement S6). Directional stability comes from the fairing on the tip frames, which needs a chord of 31 to 52~mm for lateral lift-curve slopes of 5.0 to 3.0 per radian~\cite{r24}; attitude is to be closed by a flight computer whose control loop is not designed here (Sec.~\ref{sec:discussion}).
```

```latex
\paragraph{Mechanism classes} Table~\ref{tab:mechanisms} counts the mechanism classes that other hybrid architectures use to change regime or to remove a rotor from one regime's flow. Beyond the rotation of the rotors, the only part of this aircraft that changes configuration is the strip, deployable in two halves (one for roll, both as a speed brake); the actuator inventory is the propulsion machines plus the strip. In the sense of these mechanism classes, the aircraft is therefore mechanically simpler than a tilting architecture, though not one in which nothing moves; no comparison of part count, mass or reliability is made, and no general claim about the complexity of moving parts.
```

```latex
All four closures converge (Table~\ref{tab:closures}); takeoff mass is the output and the 13~kg payload is fixed. The blade family that is best before the loop remains best after it. Run on the reference design's own assumed inputs, the same loop reproduces that design within 1.5 percent in mass and exactly in lift-to-drag ratio (Supplement S7). Closing the loop establishes that the configuration is arithmetically self-consistent on the declared package; it does not establish that the package exists (Sec.~\ref{sec:store}). Across the rotor-section and frame-drag sources examined (Supplement Table S4a), the closures span 50.7 to 66.1~kg and 699 to 1,401~km, the envelope row of Table~\ref{tab:closures}. Read as a mission, the four closures carry the 13~kg payload for 927 to 1,233~km at 30~m\,s$^{-1}$, which is 8.6 to 11.4~h of flight on the 0.16 fuel fraction with no reserve; at a radius of 50~km, 7.7 to 10.5~h of that is on station, as an observation mission such as wildfire monitoring would use it. These are sea-level values of the model. At 2,000~m the computed nose-propeller efficiency falls by about 2 percent and the hover power at the rotor shaft rises by about 10 percent (Supplement S7); the altitude penalty falls on the fixed-pitch propeller and on the store, not on the airframe.
```

```latex
\begin{table}[!htbp]
\centering
\caption{Effective lift-to-drag ratio and the four closures of the sizing loop (50~kg design, 13~kg payload, fuel fraction 0.16). Masses and ranges hold only for a buffer delivering the specific power these closures imply (Sec.~\ref{sec:store}, Table~\ref{tab:store}); ranges are modelled at sea level, not demonstrated.}
\label{tab:closures}
\scriptsize
\setlength{\tabcolsep}{3.5pt}
\begin{tabular}{lrrrrrrrrr}
\toprule
 & $C_{D0}$ & $\eta_p$ & $L/D$ & $(L/D)_e$ & MTOW & $f_{\mathrm{empty}}$ & $P_{\mathrm{hover}}$ & $P_{\mathrm{eng}}$ & Range \\
 & & & & & kg & & kW & kW & km \\
\midrule
A & 0.0381 & 0.632 & 8.79 & 5.56 & 57.5 & 0.614 & 12.53 & 5.17 & 927 \\
B & 0.0381 & 0.683 & 8.79 & 6.00 & 55.8 & 0.607 & 12.17 & 4.65 & 1002 \\
C & 0.0285 & 0.632 & 10.82 & 6.84 & 53.5 & 0.597 & 11.66 & 3.91 & 1141 \\
D & 0.0285 & 0.683 & 10.82 & 7.39 & 52.3 & 0.592 & 11.40 & 3.54 & 1233 \\
\midrule
Envelope$^{a}$ & 0.0235--0.0548 & 0.632--0.683 & 6.63--12.30 & 4.19--8.40 & 50.7--66.1 & --- & --- & --- & 699--1401 \\
\bottomrule
\end{tabular}
```

```latex
\smallskip
{\footnotesize $P_{\mathrm{hover}}$: rotor-shaft hover power; $P_{\mathrm{eng}}$: engine shaft rating. Ranges scale linearly with the fuel-to-shaft energy product of Table S2a. $^{a}$Extremes over the rotor-section and frame-drag sources examined in Supplement Table S4a: an envelope of those sources, not a confidence interval and not a further closure.}
\end{table}
```

```latex
\paragraph{Bill 2} In the drag build-up, the hardware the vertical phase leaves in the cruise flow (the tip frames and the free-wheeling tip rotors) is 69 percent of the zero-lift drag at the favourable end of the bracket and 57 percent at the adverse end (50 to 69 percent with the second rotor source, and 50 to 80 percent across all the drag sources of Supplement Table S4a); the rotor term alone is 0.0154 at the favourable end. This is an estimate resting on computed section polars at a Reynolds number of about $8 \times 10^4$, not a measurement. Stopping the tip rotors offers no reduction: with the rotor axis parallel to the cruise flow, a stopped fixed-pitch blade presents the same projected area at any azimuth, and an edge-on state would require feathering. Without the tip frames and rotors, the lift-to-drag ratio would be 20.55 and 15.24; the configuration retains 52.6 and 57.7 percent of it. Because range at fixed fuel fraction, propeller efficiency and chain efficiency is proportional to the lift-to-drag ratio, the tip hardware costs 42.3 to 47.4 percent of the range the same airframe would reach without it; this prices the drag and describes no other aircraft, since without the tip pairs the airframe cannot hover. The tip discs are not reduced to cut this drag. With the linear vortex-lattice pitching moment, the rotation completes at 23.0~N\,m, the moment given by 16.2~N and 335~W per tip pair, and saturates and tumbles at 17.6~N\,m, the moment at the sizing figure of merit of 0.599 (Supplement S7); the same pairs supply the takeoff margin.
```

```latex
\paragraph{Bill 3} The engine is sized by cruise, 3.54 to 5.17~kW of shaft rating against a hover demand of 11.4 to 12.5~kW at the rotor shaft. Bill 3, as defined in Sec.~\ref{sec:bills}, is therefore not incurred on the power plant. The electrical path (machines, power electronics, wiring) still carries the full hover power and must be rated to it; its mass is carried in the fixed propulsion fraction at the reference design's specific powers rather than re-rated in the loop, and its heat rejection is not sized (Supplement S8).
```

```latex
The configuration result is narrower. meryemAircraft meets the escape condition in the propulsor that carries it and fails it in the attitude system: the tip rotors that provide pitch and yaw, and the frames that carry them, stay in the cruise flow without producing cruise thrust and together account for 50 to 69 percent of the zero-lift drag with the frame drag assumed here and 50 to 80 percent across the drag sources examined (Supplement Table S4a). The accounting thus shows where the configuration should be improved next, in the drag of the attitude system, rather than certifying it.
```

```latex
\begin{itemize}[nosep]
\item \textit{Energy store.} The required buffer specific power is 3.7 to 4.1 times the bench average of the cited battery; re-closed at that bench average the package becomes 76 to 81 percent heavier, and at the listed continuous figure 5.8 to 6.4 times as heavy (Table~\ref{tab:store}). Sized by power, the store holds about a minute of vertical flight only if it keeps, at four times the bench rate, the specific energy the cited pack delivered at the bench rate; no reserve is included.
\item \textit{Transition and landing.} The rotation into cruise is computed with the aerodynamic pitching moment set to zero and is not settled; the landing transition is not the takeoff run backwards and has not been analysed (Supplement S4), and the vortex ring state in the vertical descent has not been assessed.
\item \textit{Control.} Attitude control is sized but not closed as a loop. Declining the reaction-torque channel has a cost in authority and response that is not computed; each pair is torque-balanced in cruise, leaving a small hover residual whose absorption is not shown; the tip pairs supply both the takeoff margin and the attitude authority; rejection of wind gusts in hover, where the vertical wing presents its full area, is not analysed; and the strip's computed hover authority about the thrust axis falls below both stated heading screens, so hover heading control is not established (Sec.~\ref{sec:configuration}).
\item \textit{Drag.} The tip-rotor term rests on computed section polars near a Reynolds number of $8 \times 10^4$ and falls from 0.0154 to 0.0104 with a second section source~\cite{r27}; the frames are charged at a frontal drag coefficient of 0.15 where a subcritical estimate gives 0.42 to 0.68~\cite{r28}. Across these sources the closures span 699 to 1,401~km (Table~\ref{tab:closures}, envelope row). Rotor--structure and rotor--wing interference are not modelled.
\item \textit{Mass and power.} The airframe fraction of 0.30 is a construction constant, not a structural sizing; the hover-rated electrical path is carried in a fixed fraction at assumed specific powers and its heat rejection is not sized; engine installation is absent; and the engine thermal efficiency of 0.28 inside the range figures is optimistic for an engine of 3.5 to 5.2~kW.
\item \textit{Scope.} All numbers are at sea level; only the 50~kg design is closed, and the 1,000~kg reference design is used only for the scale comparison. With a 13~kg payload, the missions the design serves are observation and small cargo; it is not sized for fire suppression.
\end{itemize}
```

```latex
meryemAircraft changes between hover and cruise by rotating the whole airframe, with fixed-pitch coaxial pairs that keep one body-relative orientation, and so carries none of the mechanism classes a tilting architecture uses to change regime; in that sense it is mechanically simpler, though not an aircraft in which nothing moves. Priced in three costs of hover, carried hover mass, exposed cruise drag and power sized to the hover peak, the architecture meets the escape condition in the nose pair that carries it and pays in the attitude system: the tip rotors and the frames that carry them, kept in the cruise flow, account for 50 to 80 percent of the zero-lift drag across the drag sources examined, which is where the configuration should be improved. A 50~kg design closes consistently at 52.3 to 57.5~kg, with an envelope of 50.7 to 66.1~kg and 699 to 1,401~km across those sources, and its range ranking against a lift-plus-cruise layout shifts by 67 to 77 percentage points across three sizing contracts, changing sign under one of them for the competitor assumptions used. The package depends on an energy store whose required specific power has not been demonstrated; the strip's hover heading authority is not established; and the transition and landing remain to be shown.
```

```latex
\bibitem{r27} Sheldahl, R. E., and Klimas, P. C., ``Aerodynamic Characteristics of Seven Symmetrical Airfoil Sections Through 180-Degree Angle of Attack for Use in Aerodynamic Analysis of Vertical Axis Wind Turbines,'' SAND80-2114, Sandia National Laboratories, Albuquerque, NM, 1981. \url{https://doi.org/10.2172/6548367}
```

```latex
\bibitem{r28} Hoerner, S. F., \textit{Fluid-Dynamic Drag}, published by the author, Midland Park, NJ, 1965.
```

### Supplement

```latex
\title{Supplemental Material for ``meryemAircraft: Regime Change by Rotating the Airframe, Without Reorienting a Propulsor''}
```

```latex
\begin{table}[htbp]
\centering
\caption*{Table S0. Claims, evidence and what would refute them. The thresholds of the fourth and last rows were stated before the computations that test them.}
\small
\begin{tabularx}{\linewidth}{>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}p{0.11\linewidth}>{\raggedright\arraybackslash}p{0.2\linewidth}>{\raggedright\arraybackslash}X}
\hline
Claim & Where & Evidence & What would refute it \\ \hline
The aircraft changes regime with none of the mechanism classes tilting architectures use & Sec. 3.1, Table 3 & Inventory of the design & A mechanism of one of those classes found necessary, e.g. a rotor brake or lock \\
It is therefore mechanically simpler than a tilting architecture, in that sense only & Sec. 3.1 & Mechanism-class count; part count, mass and reliability not compared & As row 1; part count, mass, reliability and the complexity of moving parts in general are not claimed \\
The loop closes at 52.3 to 57.5 kg for a 13 kg payload & Sec. 4.2 & Computed & A required input outside its stated range; the store gates of Table S8a \\
The tip hardware is the largest drag item: 50 to 69 percent of the zero-lift drag with the frames at a frontal drag coefficient of 0.15, 50 to 80 percent across Table S4a & Sec. 4.3, S8 & Two computed section sources in one solver; threshold 40 percent set before the second run & A measured rotor or frame drag that brings the share below 40 percent \\
Bill 3 is not incurred on the engine & Sec. 4.3 & Computed: engine sized by cruise & An engine rating set by a vertical phase \\
The range ranking against a lift-plus-cruise layout depends on the sizing contract & Sec. 4.5, S10 & Closed form and loop, under stated competitor assumptions & One sign under all three contracts at the same inputs \\
The rotation costs altitude, 5.4 to 6.6 m, with the pitching moment set to zero & Sec. 4.4, S7 & Computed; not a prediction & A measured pitching moment through 18 to 22 degrees that removes the loss \\
Hover heading authority is not established & Sec. 3.1, S6 & Computed strip force against stated screens & A shown circulation increment of 0.1 or more on the half wing in the slipstream \\
\hline
\end{tabularx}
\end{table}
```

```latex
In the nose-pair slipstream (dynamic pressure 434~N\,m$^{-2}$), the strip's own normal force at a coefficient of 0.6 to 1.4 gives 0.60 to 1.40~N\,m. This is below both screens. A larger moment would come from a change of circulation on the half wing in the slipstream: a lift increment of 0.10 to 0.20 on that 0.49~m$^2$ gives 6.0 to 12.0~N\,m. The increment is assumed by analogy with spoilers and Gurney strips and is not predicted for this geometry. For scale, one nose rotor produces 25 to 27~N\,m of reaction torque in hover; with torque proportional to the square of rotational speed, 1~N\,m balances a speed mismatch of about 2 percent between the two motors of that pair, and an uncorrected bias of only 0.18~N\,m moves the heading by 5$^\circ$ in 5~s from rest. The strip's response also has a dead band: below 1 percent of the local chord the protrusion is reported to have negligible effect [24], so the strip does nothing below about 7 percent of its stroke and gives 4 percent of its full moment at 10 percent. The strip's hover heading authority is therefore not established here. The reaction-torque channel this configuration declines is of the size the screens require: from 24.9 to 27.5 N\,m per nose rotor, a 10 percent torque imbalance of one rotor gives 2.5 to 2.8 N\,m and a 30 percent imbalance 7.5 to 8.3 N\,m. Its cost in power and in the other axes is not computed, and it is not claimed here to close the heading channel. The computation is in \texttt{aero/roll.py}.
```

```latex
The 50 kg design is rotated in a three-degree-of-freedom model: the body angle follows a reference profile through a proportional-derivative controller whose moment is limited to the available control moment of 23.0 N$\cdot$m, with a rotation time of 2 s, an entry climb of 5 m s$^{-1}$, and the aerodynamic pitching moment set to zero. The loss persists across three reference profiles: 5.43 m with a linear profile, 6.33 m with a smooth (cubic) one and 6.57 m with a bang-bang one, which is the body's 5.4 to 6.6 m. In none of the three does the control moment saturate. Raising the gains increases the loss rather than removing it: with the proportional gain raised sixteen-fold and the derivative gain four-fold, the loss is 16.9 m, again without saturation. With the computed zero-lift bracket and Oswald factor of 0.817, in place of the reference design's assumed 0.0248 and 0.85, each figure moves by at most 0.02 m. Within the finite-moment dynamic model, with the aerodynamic moment set to zero, the maneuver costs altitude. The tip pairs show no margin to shrink. Their thrust, 16.2 N at 335 W per tip pair, is the reference design's rating, implying a figure of merit of 0.702, and gives the 23.0 N$\cdot$m above; with the linear vortex-lattice pitching moment the rotation then completes without saturation, losing 12.2 m. At the figure of merit of 0.599 used in sizing, the pair gives 12.4 N and the moment 17.6 N$\cdot$m, and with the same pitching moment the rotation saturates after 1.5 s and tumbles; with the moment set to zero it still completes. These are two tested points, not a threshold. No smaller tip disc is therefore examined.
```

```latex
The rotor term rests on NeuralFoil polars, and NeuralFoil is trained on XFOIL, so an XFOIL run is a check of the same family rather than a second estimate. The same zero-shaft-torque blade-element solver was therefore run on the same frozen blade (design lift coefficient 0.68, the blade behind 0.0154) with the section polar replaced by the NACA 0012 table of Sheldahl and Klimas at a Reynolds number of $8\times10^4$ [27] (Table 2, report p. 16). That table is an Eppler-code synthesis, not a measurement; no measured two-dimensional NACA 0012 polar was found at this Reynolds number, and the nearest measurements, on wings of aspect ratio 2 and 4 [S3], report finite-span drag in figures only. The free-wheeling rotor then runs at 2,549 rather than 2,623 rad s$^{-1}$ with an axial drag of 1.41 rather than 2.09 N per disc, and the rotor term falls from 0.0154 to 0.0104. With the frames unchanged, the tip hardware is then 63 percent of the zero-lift drag at the favorable end and 50 percent at the adverse end, against 69 and 57 percent, and the aircraft's lift-to-drag ratio is 12.30 and 9.86 rather than 10.82 and 8.79. The closures keep the higher rotor term, which is the less favourable value for this configuration; the two computed sources span the uncertainty but do not measure it.
```

```latex
The tip frames are charged at a frontal-area drag coefficient of 0.15. The faired frame is 20 mm thick on a chord of 31 to 52 mm, a thickness ratio of 0.38 to 0.65, and runs at a chord Reynolds number of about $4\times10^4$ to $10^5$. For subcritical sections Hoerner gives $C_{D} = 2C_f(1+t/c)+(t/c)^2$ on chord area [28] (Ch.~VI, p.~6-5, Eq.~2), which with the laminar $C_f = 1.328/\sqrt{Re}$ (p.~2-4) is 0.42 to 0.68 on frontal area. The critical drop in drag spans roughly $Re_c = 5\times10^4$ to $5\times10^5$ and depends on the section (Fig.~2, p.~6-3), so no single value is established for an unspecified fairing; the book does not support 0.15 for this one. Closed through the same loop, Table S4a shows what the frame and rotor terms do to the closures.
```

```latex
\begin{table}[htbp]
\centering
\caption*{Table S4a. Mass and range sensitivity of the closures to the rotor-section source and the frame drag (favorable end at $\eta_p = 0.683$, adverse end at 0.632). Control and authority margins are computed only for the 50 kg reference design with 0.20 m tip discs, not for these cases.}
\small
\begin{tabularx}{\linewidth}{Xrrrrr}
\hline
Frame $C_D$ (frontal), rotor source & End & $C_{D0}$ & $L/D$ & Takeoff mass, kg & Range, km \\ \hline
0.15, NeuralFoil (the closures of Sec. 4.2) & fav. / adv. & 0.0285 / 0.0381 & 10.82 / 8.79 & 52.3 / 57.5 & 1233 / 927 \\
0.42, NeuralFoil & fav. / adv. & 0.0363 / 0.0466 & 9.12 / 7.54 & 55.1 / 61.6 & 1039 / 795 \\
0.68, NeuralFoil & fav. / adv. & 0.0437 / 0.0548 & 7.92 / 6.63 & 58.1 / 66.1 & 902 / 699 \\
0.15, Sheldahl--Klimas & fav. / adv. & 0.0235 / 0.0326 & 12.30 / 9.86 & 50.7 / 55.1 & 1401 / 1039 \\
0.42, Sheldahl--Klimas & fav. / adv. & 0.0313 / 0.0411 & 10.15 / 8.30 & 53.3 / 58.9 & 1156 / 876 \\
0.68, Sheldahl--Klimas & fav. / adv. & 0.0387 / 0.0493 & 8.68 / 7.21 & 56.1 / 63.0 & 990 / 760 \\
\hline
\end{tabularx}
\end{table}
```

```latex
The propulsion fraction of the empty mass is 0.176 to 0.198 across the four closures, in two parts. A fixed 0.108 is back-solved from the reference design's own budget, which itemizes 7.60 kg of propulsion at 50 kg: the nose machines sized to the hover peak at 4 kW kg$^{-1}$ (2.73 kg), the tip motors at twelve percent of nose power, the power electronics at 20 kW kg$^{-1}$, the propellers, coaxial hubs, engine mounting and cabling, and 2.60 kg of engine and generator. At 50 kg the back-solved fixed part is 5.40 kg against the 5.00 kg itemized outside the engine and generator, a difference of 0.40 kg that the budget does not explain. The engine term is the engine rating divided by an assumed specific power of 1.0 kW per kilogram: 0.068 at closure D to 0.090 at closure A, following the cruise-sized rating of 3.54 to 5.17 kW. The hover power, 11.4 to 12.5 kW at the rotor shaft, passes through the electrical path whatever the engine is rated at; that path's mass lies in the fixed 0.108 at the reference design's specific powers and scales with takeoff mass, which at fixed disc loading is how hover power scales. It is not re-rated in the loop, and its heat rejection is not sized. The airframe (0.300) and avionics (0.080) fractions are construction constants held common across the three architectures of Sec. 4.5; they are not results of the ledger.
```

```latex
\begin{table}[htbp]
\centering
\caption*{Table S8a. Closure gates: the conditions the closures of Sec. 4.2 assume, against what this work computes or cites.}
\small
\begin{tabularx}{\linewidth}{>{\raggedright\arraybackslash}p{0.17\linewidth}>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}p{0.2\linewidth}}
\hline
Gate & Condition assumed & Computed or cited & Status \\ \hline
Store power & Buffer delivers 4.7 to 5.2 kW kg$^{-1}$ in hover, 5.5 to 6.1 at takeoff & Cited pack: 1.49 kW kg$^{-1}$ bench average, 0.724 and 0.892 continuous [25] & Not met by any store reported as built \\
Store energy & Specific energy at least specific power times event duration: 39 to 51 Wh kg$^{-1}$ per 30 s, 78 to 102 per 60 s & Cited pack: 103 Wh kg$^{-1}$ delivered at 1.49 kW kg$^{-1}$ [25] & Met only if kept at four times the bench rate; no reserve. Recharge from the engine's margin over cruise power, $0.90\,P_{\mathrm{eng}} - P_{\mathrm{el,c}} = 0.25\,P_{\mathrm{eng}}$, takes about 4 to 6 min per 30 s event \\
Electrical path mass & Nose machines sized to the hover peak at 4 kW kg$^{-1}$, tip motors, power electronics at 20 kW kg$^{-1}$ and cabling, inside the fixed 0.108 propulsion fraction (reference budget; Supplement S8) & A regression on 1,743 small electric motors [S1] and a 6 kW inverter [S2] give 2.3 to 3.1 kg for machines and inverters, below the about 3.7 kg the budget carries & Carried at assumed specific powers, not re-rated; heat rejection not sized \\
Tip-rotor drag & Rotor term 0.0154 & 0.0104 with a second section source in the same solver (Supplement S8) & Bracketed; closures keep the higher value \\
Frame drag & Frontal $C_D$ 0.15, $\Delta C_{D0}$ 0.0043 & Hoerner's subcritical relation gives 0.42 to 0.68; ranges 699 to 1039 km at the adverse end (Table S4a) & Not settled; not in the closures \\
Transition moment & 23.0 N$\cdot$m from 16.2 N and 335 W per tip pair (figure of merit 0.702), aerodynamic pitching moment zero & With the vortex-lattice moment: completes at 23.0 N$\cdot$m, saturates and tumbles at 17.6 N$\cdot$m, the moment at the sizing figure of merit 0.599 (Supplement S7) & Computed, not settled; depends on the moment model \\
Hover heading & At least 1.6 to 5.8 N$\cdot$m (stated screens) & Strip force 0.6 to 1.4 N$\cdot$m; more only under an assumed circulation increment (Supplement S6) & Not met \\
Landing & Not assumed & Not analysed (Supplement S4) & Open \\
Ranking sign & Competitor lift-group mass and propeller efficiency as stated & Break-even values (Sec. 4.5; Supplement S10) & Contract-dependent \\
\hline
\end{tabularx}
\end{table}
```

**Table S9** (the open-items table, with each item's bearing and what would settle it). Its rows, verbatim in content, in the order they appear:
1. The pitching moment through the transition (three methods diverge above about ten degrees; the rotation peaks near 18–22°).
2. Section drag at low Reynolds number (the rotor term 0.0154, carried as 0.0169 at the adverse end).
3. The tip pairs' other cruise state (*"in axial flow none of them is lower-drag without feathering"*).
4. The tip pairs' shaft power off the free-wheeling state in cruise.
5. The buffer's energy, not only its power (*"depends on a hover duration this work does not fix; at the bench rate the unit pack emptied in about four minutes"*).
6. *Other store types (part of the known obstacle; not one of the eighteen):* supercapacitors at 500–10,000 and 10,000–100,000 W/kg and 1–10 Wh/kg [23], with the survey's own qualification quoted.
7. The electrical path at peak (*"their mass is carried in the fixed propulsion fraction at the reference design's specific powers, not re-rated in the loop, and their heat rejection is not sized"*).
8. The airframe's mass (areal density ≤ 1.78 kg m⁻² against 1.50 assumed; not rerun at the closed masses).
9. The strip and the fairing.
10. Closed-loop attitude control, in hover and in cruise.
11. Vertical descent and the landing transition.
12. Ground handling and landing loads.
13. The competitor's lift-group mass.
14. The competitor's cruise propeller efficiency (assumed 0.80).
15. Rotor–structure and rotor–wing interference, in cruise and in hover (with [3], p. 320).
16. Engine installation.
17. Blade-family selection.
18. The variable-pitch counterfactual.
19. Atmosphere.

```latex
\begin{enumerate}[label={[S\arabic*]}, leftmargin=*]
\item MacNeill, R., and Verstraete, D., ``Propeller Optimisation for an Electrically-Powered Tactical UAS,'' 31st Congress of the International Council of the Aeronautical Sciences, ICAS 2018-0404, Belo Horizonte, 2018.
\item Persystems, INV-60V-120A inverter, product data sheet, \url{https://persystems.com/en/inverters/inv-60v-120a/}, accessed 29 October 2026.
\item Ohtake, T., Nakae, Y., and Motohashi, T., ``Nonlinearity of the Aerodynamic Characteristics of NACA0012 Aerofoil at Low Reynolds Numbers,'' \textit{Journal of the Japan Society for Aeronautical and Space Sciences}, Vol. 55, No. 644, 2007, pp. 439--445. \url{https://doi.org/10.2322/JJSASS.55.439}
\end{enumerate}
```

---

## 3. Checks by the Claude session

These are facts with their basis; the Claude session's positions go beside everyone's next round. They are ordered by how much they could change the paper.

**L1. The 12.4 N at the sizing figure of merit does not follow from the stated inputs.** S7: *"At the figure of merit of 0.599 used in sizing, the pair gives 12.4 N and the moment 17.6 N·m."* Momentum theory, with the same 0.20 m disc and the same 335 W that give 16.2 N at FM 0.702 (T = (FM · P · √(2ρA))^(2/3)), gives:
- at FM 0.702: 16.2 N, which matches;
- at FM 0.599: **14.6 N**, so 23.0 × 14.6/16.2 = **20.7 N·m**, not 17.6.

12.4 N at FM 0.599 would need about 263 W, not 335 W. How was 12.4 N obtained?

If the power is held at 335 W, the point at the sizing figure of merit is about 20.7 N·m, which lies between the two tested points (17.6 tumbles, 23.0 completes) and has not been run. Then Bill 2's sentence (*"saturates and tumbles at 17.6 N·m, the moment at the sizing figure of merit of 0.599"*) and Table S8a's transition row describe a case that is not the sizing figure of merit.

Two further points:
- The 16.2 N at 335 W is called *"the reference design's rating"*. Table S8a should say whether that is an assumed rating, as the reference design is.
- FM 0.702 is computed on one disc's area for a coaxial pair.

**L2. The body's reaction-torque sentence quotes a number that covers only one screen.** Sec. 3.1: *"has the magnitude to cover both screens, 2.5 to 2.8 N·m at a 10 percent torque imbalance of one nose rotor."* The second screen is 5.8 N·m, and 2.8 < 5.8. S6 carries the figure that covers it (7.5–8.3 N·m at 30 percent); the body does not. Either the body quotes the 30 percent figure, or it says "the first screen at about 6 percent and the second at about 23 percent of one rotor's torque".

The script (`aero/reaction_torque.py`, commit `b3c1bd4`) prints 2.5–2.7 and 7.5–8.2; the text has 2.5–2.8 and 7.5–8.3. That is a rounding of 2.75 and 8.25, but under the number-identity rule the text should match the output it cites.

**L3. "50 to 69 percent with the second rotor source" is not what Table S4a gives.**
- The second rotor source (Sheldahl–Klimas) alone gives 63 (favourable) and 50 (adverse).
- 50–69 is the span over both rotor sources with the frame at 0.15.

Bill 2's parenthesis should read "50 to 69 percent across the two rotor sources", as Table S0 row 4 and the discussion paragraph already put it.

**L4. Neither the abstract nor the conclusions now says what the architecture gains against rotorcraft.**
- The removed (L/D)e 5.56–7.39 was the abstract's only comparison against rotorcraft. The cruise-efficiency comparison with the published quadrotors and helicopters is still in Sec. 4.1, but it has left the abstract.
- The abstract now gives the architecture, three costs, where it pays, the mass and range envelope, the contract dependence, and four unresolved items. It never says what wing-borne cruise buys against a rotorcraft.
- The highlights likewise give one architecture line, then accounting, cost, contracts and reproducibility.

The abstract and the conclusions also end on four open items in a row. The author's direction of 16 October was that the paper says what the work does. The cost and the open items are in the text, but the paper's advantage on the cruise-efficiency axis is not in the abstract at all. Question Q2 asks for a view; the decision is the author's.

**L5. The bounded simplicity sentence now disclaims the basis the author stated.** Sec. 3.1 ends *"…no comparison of part count, mass or reliability is made, and no general claim about the complexity of moving parts."* This is the author's decision, taken after Round 227. It explicitly withdraws the premise the author gave on 16 October (*"a moving element is always more complex than a fixed system"*).

The Claude session records this only so that the author sees the two together: one is the decision, the other is the reasoning it now disclaims. The clause is also elliptical: *"and no general claim … [is made]"*.

**L6. Highlight 5 is a claim that B6 will test.** *"Every input needed to reproduce each sizing closure is stated"* is exactly what the blind re-implementation (B6) tests, and B6 runs after the freeze. Should the highlight wait for B6, or be worded as a description of what the supplement contains (for example "Table S2a lists every input of the sizing loop")?

**L7. The abstract's length against the journal.** The abstract is 245 words. *Aerospace Science and Technology*'s guide for authors has not been quoted in any round; its abstract limit (and its rule for highlights) should be checked against the guide itself before the freeze.

The five highlights are 80, 77, 80, 78 and 62 characters (counted here), all under 85.

**L8. Table S9 row 5 predates the S8a energy gate.** It says the store's energy *"depends on a hover duration this work does not fix"*, while Table S8a now computes 30 s and 60 s events (39–51 and 78–102 Wh/kg). Should row 5 point to S8a and keep only the reserve and recharge profile as open?

**L9. Arithmetic that rebuilds.**
- The envelope row: (L/D)e 6.63 × 0.632 = 4.19 and 12.30 × 0.683 = 8.40.
- The electrical-path budget: 0.108 × 50 = 5.40 kg against 7.60 − 2.60 = 5.00 kg, a 0.40 kg difference. The machines and power electronics come to about 3.7 kg: 2.73 kg, plus 0.33 kg for tip motors at 12 percent, plus about 0.6 kg at 20 kW/kg.
- The tip share: 50–69 percent with the frame at 0.15 and 50–80 percent across S4a, as stated.
- NACA ACR L4H19 being NACA Report 796 (Donlan, 1944) is consistent with the NACA series' renumbering of wartime reports. The council's identification stands unless a reader finds otherwise.

**L10. References.** Under the standing rule (two or more readers cross-check each field), please check against the source:
- [27]'s DOI (`10.2172/6548367`);
- [S1]'s title and whether that paper contains the 1,743-motor regression (Eq. 6);
- [S2]'s rating: the model name reads 60 V / 120 A (7.2 kW), while the text says *"a 6 kW unit"*;
- [S3]'s pages and DOI.

---

## 4. Questions

**Q1. Title.** Do you have a major objection to title 1? One point to weigh: title 1 carries the architecture but none of "tail-sitter", "blended-wing body" or "VTOL". The keywords carry them; title 2 carries two of them.

**Q2. Abstract.**
- (i) Is there anything you would not let drop?
- (ii) Should a cruise-efficiency result against rotorcraft (L4) return to the abstract and the conclusions?
- (iii) Is any wording wrong?

**Q3. Phase 2, "no additions".** Do you object?

**Q4. Section 2.** Is any item applied wrongly? In particular L1, L2, L3, L6 and L8: accept, amend or reject, with a reason.

**Q5. L10.** Answer from the source document you opened, or say that you did not open it.

**Q6. Open proposals,** each with its reason.

---

## 5. Errors (one list, all sources)

| # | Source | Statement | Finding |
|---|---|---|---|
| 1 | Claude (Round 227, K2) | The fixed 0.108 omits the electric machines and inverters | Wrong. The reference budget (v7 S2.1) itemizes them inside the 0.16 that 0.108 is back-solved from. The code comment was incomplete; Qwen was right. |
| 2 | Claude (Round 227, K3) | *"speed imbalance"* of 10 and 30 percent | The script's arithmetic is a torque fraction (10 percent of 25–27 N·m), so these are torque imbalances. With torque ∝ ω², a 10 percent torque imbalance is about 5 percent in speed. The council's text says *"torque imbalance"* correctly. |
| 3 | DeepSeek (Round 226) | The AI paragraph twice; Sec. 4.1 cut short | Withdrawn by DeepSeek in Round 227: text-extraction artefacts. Closed. |

## 6. Answer format

Give your channel name first, then Q1–Q6 by number. Where you disagree with another channel, name it and answer its reason.

## 7. What goes to the author after this round

- **Title:** whether title 1 stands.
- **Abstract and conclusions:** whether a result for what the architecture gains (cruise efficiency against rotorcraft) returns (L4), and how the last sentence ends.
- **L1, if confirmed:** the sizing-figure-of-merit transition point is untested and lies between the tested ones. Whether it is run before the freeze is a decision on a stated result.
- **L5:** the bounded simplicity clause and the premise of 16 October, side by side.
- **L6:** highlight 5 before B6.
