# Yang, Zhu, Zhang & Wang 2018 — the relevant parts (for the round file)

**Source:** Y. Yang, J. Zhu, X. Zhang and X. Wang, *Active Disturbance Rejection Control of a Flying-Wing Tailsitter in Hover
Flight*, 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Madrid, pp. 6390–6396. File:
`references/Yang-Zhu-2018_IROS_ADRC-flying-wing-tailsitter-hover.pdf` (7 pages).

**What is quoted and why.** The paper is mainly a control-law paper (ADRC: extended state observer, tracking differentiator,
nonlinear state-error feedback). That part does not bear on our paper and is not quoted. Quoted verbatim below are the parts that do:
- the vehicle;
- how each attitude axis is actuated;
- how the propellers' counter-moment is treated;
- what was flown;
- what is left to future work.

The equations are garbled in the text extraction. Where one matters, it is described in words in square brackets, and **the brackets
are mine, not the paper's**.

**Abstract (in full).** *"This paper presents the development and hovering control of a tailsitter unmanned aerial vehicle (UAV) that
merges long endurance and vertical takeoff and landing (VTOL) abilities. The designed tailsitter contains one flying-wing with two
motors and two elevons. Vehicle aerodynamics and a six-degrees-of-freedom (6-DOF) model are especially developed for the tailsitter. To
achieve a good performance in outdoor stationary hovering and accurate vertical flying, the active disturbance rejection control
(ADRC) for attitude controller is proposed. … Experimental results are presented to corroborate the effectiveness of the controller in
disturbance rejection."*

**Introduction.** *"As shown in Fig. 1, we designed and manufactured a dual-rotor tailsitter UAV based on a kind of fixed-wing
aircraft. The UAV can achieve VTOL abilities without adding other mechanical complexity."* It also cites, among the tail-sitter
literature, *"A. Oosedo, … 'Development of a quad rotor tailsitter VTOL UAV without control surfaces and experimental verification,'
… ICRA, pp. 317-322, 2013"* (its reference [3]); that is the 2013 vehicle in Step 1's occupied list.

**II-A, Aircraft Design.** *"Two CW/CCW carbon propellers with the diameter of 16" driven by 600W brushless electrical motors are
chosen as the system propulsion. Two 6s LIPO batteries are used to supply power. The airframe consists of one flying-wing with two
elevons. The profile of the wing is the MH91 whose wing area is 0.478m², span is 1.2m and chord length is 0.438m. … The all-up-weight
of the tailsitter is 2.23kg."*

**II-B, Coordinate systems.** *"… vertical body frame is adopted to avoid singularity in the controller design: the original point
coincides with the center of gravity (C.G.), xb points to the belly of the vehicle, zb points to the tail of the vehicle and yb is
determined by the right-hand principle."* [So zb is the fuselage axis, which is the thrust axis; it is vertical in hover.]

**II-C, Actuation Principle.** *"The tailsitter uses a minimum combination of motors and elevons to control its attitude during the
whole flight envelope. As shown in Fig. 4(a), differential thrust of two propellers is used to control the axis xb of the vehicle. The
vehicle axis yb is controlled by equal elevons deflections (Fig. 4(b)) and the axis zb is similarly steered by differential elevons
deflections (Fig. 4(c)). The elevons have a range of ±30°, and the down deflection is defined as positive. The moments of pitch and yaw
are determined by both propeller slipstream and air flow diverted by the elevons."*

**III-B, the moment equations.** *"… the resultant thrust of left propeller and right propeller coincides with the negative zb axis
but it does not pass through the center of gravity."* [In the equation for the axis zb, the propellers enter only as a moment
M_l + M_r, and not as a control.] *"Ml and Mr are the moments generated due to the rotation of motors and propellers."*

**IV-B, how that moment is handled.** *"For the pitch and yaw channels, ESOs reflect their unknown dynamics and external disturbances
respectively, including the counter-moment due to rotation of propellers, undesired pitch moment due to the displacement between
resultant thrust axis and center of gravity and so on."* [The propellers' counter-moment about the thrust axis is estimated as a
disturbance and cancelled; it is not used as a control channel.]

**IV-C, Control Allocation.** *"… uM̄ is the pitch control moment, which is produced by equal elevons deflections. And uN̄ is the yaw
control moment, which is produced by differential elevons deflections."* [The roll moment is (T_r − T_l)·l_y, from differential
thrust.]

**V, Experiments.** *"The experiments are conducted at a windy day … The wind blows from north to south at the speed of 3 ∼ 4m/s,
which is measured by a handheld anemometer in ground."* Two tests: a hover of about 30 s, and *"fly 15 meters forward and then back
with its belly facing the wind"* in the vertical attitude.

**VI, Conclusions (in full).** *"The design and hovering control laws of the flying-wing tailsitter with two motors and two elevons
are discussed in this paper. … Experiments are presented to corroborate effectiveness of the controller in disturbance rejection.
The on-going transition and horizontal flight of the tailsitter, as well as the ability to resist stronger winds, are the main future
works."*
