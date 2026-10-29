# Zenodo v9: fields to enter (new version of the existing meryemAircraft record)

New version of the v8 record (10.5281/zenodo.23437041), draft saved by the authors on 2026-10-29.
Reserved version DOI: 10.5281/zenodo.23754355 (already in the paper's Data availability). It is registered only when the record is published.
Before publishing: remove the placeholder v9.tex uploaded to the draft and upload the files below.

- **Resource type:** Publication / Preprint
- **Title:** meryemAircraft: A Blended-Wing-Body Tail-Sitter with Body-Fixed Coaxial Propulsors
- **Creators** (each with affiliation Independent Researcher, as in v8):
  1. Gülmen, Meryem
  2. Gülmen, Berke
  3. Gülmen, Ömer, ORCID 0009-0002-8017-5400 (Ömer Gülmen's ORCID only)
- **Version:** 9
- **Publication date:** the upload date
- **Licence:** CC BY 4.0 (as in v8)
- **Keywords:** hybrid VTOL; tail-sitter; blended wing body; airframe rotation; aircraft sizing; sizing contracts
- **Related identifier:** https://github.com/LORDTEK/meryemAircraft, "Is supplemented by", Software (as in v8)

## Files (from zenodo/out/)

| File | Content |
|---|---|
| meryemAircraft-v9.pdf | Paper (preprint, without vitae) |
| meryemAircraft-v9-supplement.pdf | Supplement: claim-evidence Table S0 and Sections S1-S11 |
| meryemAircraft-v9-source.zip | LaTeX sources of both PDFs, highlights and the two figures |
| meryemAircraft-v9-code.zip | Analysis code (aero/) and licence, at the GitHub commit named in the folder |
| meryemAircraft-v9-reimplementation.zip | Blind re-implementation of this version: frozen text with SHA-256, pre-registration, list of the 58 compared values with status, prompt, generated scripts, answers, run outputs, and the diff of every change after the freeze |
| meryemAircraft-v9-additional-checks.zip | v9 checks not yet in the repository: second section source for the tip rotors, frame-drag sensitivity through the closure loop, the 20.7 N m transition point, and the roll output |
| SHA256SUMS | Checksums (optional) |

Not uploaded: meryemAircraft-v9-AST-submission.pdf (journal version with vitae and photos).

## Description

<p>Version 9 (October 2026).</p>
<p>Hybrid vertical-takeoff aircraft change between hover and cruise by carrying two propulsor sets or reorienting one. meryemAircraft, a 50 kg tail-sitting blended-wing body for a 13 kg payload, does neither: its fixed-pitch coaxial pairs keep one body-relative orientation while the whole airframe rotates, so it carries none of the mechanism classes a tilting architecture uses to change regime. It is priced in three costs of hover: carried hover mass, exposed cruise drag and continuous power sized to the hover peak. On a buffered series hybrid, the nose pair, which supplies hover and cruise thrust, incurs none of them; the attitude-control tip pairs and frames stay in the cruise flow, taking 50 to 80 percent of zero-lift drag across the drag sources examined. With the assumed frame drag the sizing loop closes at 52.3 to 57.5 kg, at an effective lift-to-drag ratio 13 to 51 percent above a published turboshaft quadrotor's; across those sources the envelope, not a confidence interval, is 50.7 to 66.1 kg and 699 to 1,401 km. The range margin of a lift-plus-cruise layout over this aircraft shifts by 67 to 77 percentage points across three sizing contracts, so the ranking depends on the contract. No store reported as built delivers the required specific power; hover heading authority, the transition and landing remain open.</p>
<p>Files: the paper; the supplement with the working behind every pointer of the paper; the LaTeX sources; the analysis code at a recorded commit of the GitHub repository; the v9 checks not yet in the repository; and the record of two blind re-implementations of the sizing closures from the frozen text by large language models (a reproducibility check, not a validation).</p>

## References

A new version copies the previous version's reference list (about 50 entries from v8). Delete all of them, then enter the 31 below, one per entry: the paper's 28 in order of citation, then the supplement's 3.

```
Bacchini, A., and Cestino, E., "Electric VTOL Configurations Comparison," Aerospace, Vol. 6, No. 3, 2019, Paper 26. https://doi.org/10.3390/aerospace6030026
Anderson, S. B., "Historical Overview of V/STOL Aircraft Technology," NASA TM-81280, March 1981.
De Wagter, C., Ruijsink, R., Smeur, E., van Hecke, K., van Tienen, F., van der Horst, E., and Remes, B., "Design, Control, and Visual Navigation of the DelftaCopter VTOL Tail-Sitter UAV," Journal of Field Robotics, Vol. 35, No. 6, 2018, pp. 937–960. https://doi.org/10.1002/rob.21789
Oosedo, A., Abiko, S., Konno, A., Koizumi, T., Furui, T., and Uchiyama, M., "Development of a Quad Rotor Tail-Sitter VTOL UAV without Control Surfaces and Experimental Verification," 2013 IEEE International Conference on Robotics and Automation (ICRA), IEEE, Karlsruhe, Germany, 2013, pp. 317–322. https://doi.org/10.1109/ICRA.2013.6630594
Escareño, J., Sanchez, A., Garcia, O., and Lozano, R., "Modeling and Global Control of the Longitudinal Dynamics of a Coaxial Convertible Mini-UAV in Hover Mode," Journal of Intelligent and Robotic Systems, Vol. 54, Nos. 1–3, 2009, pp. 261–273. https://doi.org/10.1007/s10846-008-9265-y
Wang, J., Song, B., and Wang, L., "L1 Adaptive Attitude Controller for a Tail-Sitter MAV in Hover Flight," 29th Congress of the International Council of the Aeronautical Sciences, St. Petersburg, Russia, 2014, Paper ICAS 2014-0529.
Zhang, D., Chen, Z., and Lv, J., "Lift System Design of Tail-Sitter Unmanned Aerial Vehicle," Intelligent Control and Automation, Vol. 3, No. 4, 2012, pp. 285–290. https://doi.org/10.4236/ica.2012.34033
Pathak, S., "Design of Flying Wing Tail Sitter Contra-Rotating Propeller VTOL Sky Swift V1.0 UAV," Journal of Informatics Education and Research, Vol. 5, No. 2, 2025, pp. 6268–6278. https://doi.org/10.52783/jier.v5i2.3173
Rohith, S. K., Sridharan, A., and Govindarajan, B., "Hybrid Powertrain Systems for 100 kg Multicopters and Tailsitters," Journal of Aircraft, Vol. 63, No. 2, 2026, pp. 575–591. https://doi.org/10.2514/1.C038443
Vegh, J. M., "Hybrid-Electric Design Studies for a Long-Endurance Tailsitter Concept," AIAA Paper 2025-1436, Jan. 2025. https://doi.org/10.2514/6.2025-1436; correction notice https://doi.org/10.2514/6.2025-1436.c1
Escareño, J., Stone, R. H., Sanchez, A., and Lozano, R., "Modeling and Control Strategy for the Transition of a Convertible Tail-Sitter UAV," Proceedings of the European Control Conference 2007, Kos, Greece, 2007, pp. 3385–3390. https://doi.org/10.23919/ECC.2007.7068919
Yang, Y., Zhu, J., Zhang, X., and Wang, X., "Active Disturbance Rejection Control of a Flying-Wing Tailsitter in Hover Flight," 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), IEEE, Madrid, Spain, 2018, pp. 6390–6396. https://doi.org/10.1109/IROS.2018.8594470
Liebeck, R. H., "Design of the Blended Wing Body Subsonic Transport," Journal of Aircraft, Vol. 41, No. 1, 2004, pp. 10–25. https://doi.org/10.2514/1.9084
Merical, K., Beechner, T., and Yelvington, P., "Hybrid-Electric, Heavy-Fuel Propulsion System for Small Unmanned Aircraft," SAE International Journal of Aerospace, Vol. 7, No. 1, 2014, pp. 126–134. https://doi.org/10.4271/2014-01-2222
Bacchini, A., "Electric VTOL Preliminary Design and Wind Tunnel Tests," Ph.D. Dissertation, Dept. of Mechanical and Aerospace Engineering, Politecnico di Torino, Turin, Italy, 2020.
Mathur, A., and Atkins, E., "Wind Tunnel Testing and Aerodynamic Characterization of a QuadPlane Uncrewed Aircraft System," arXiv:2301.12316v1, Jan. 2023. https://doi.org/10.48550/arXiv.2301.12316
Rheaume, J. M., and Lents, C., "Energy Storage for Commercial Hybrid Electric Aircraft," SAE Technical Paper 2016-01-2014, 2016. https://doi.org/10.4271/2016-01-2014
Johnson, W., and Silva, C., "NASA Concept Vehicles and the Engineering of Advanced Air Mobility Aircraft," The Aeronautical Journal, Vol. 126, No. 1295, 2022, pp. 59–91. https://doi.org/10.1017/aer.2021.92
Nelms, W. P., and Anderson, S. B., "V/STOL Concepts in the United States: Past, Present, and Future," NASA TM-85938, April 1984.
Donlan, C. J. (compiler), "An Interim Report on the Stability and Control of Tailless Airplanes," NACA Report 796, 1944.
Sharpe, P. D., "AeroSandbox: A Differentiable Framework for Aircraft Design Optimization," S.M. Thesis, Dept. of Aeronautics and Astronautics, Massachusetts Institute of Technology, Cambridge, MA, 2021.
Panagiotou, P., Dimopoulos, T., Dimitriou, S., and Yakinthos, K., "Quasi-3D Aerodynamic Analysis Method for Blended-Wing-Body UAV Configurations," Aerospace, Vol. 8, No. 1, 2021, Paper 13. https://doi.org/10.3390/aerospace8010013
Wang, K., and Zhou, Z., "Aerodynamic Design, Analysis and Validation of a Small Blended-Wing-Body Unmanned Aerial Vehicle," Aerospace, Vol. 9, No. 1, 2022, Paper 36. https://doi.org/10.3390/aerospace9010036
Sharpe, P. D., and Hansman, R. J., "NeuralFoil: An Airfoil Aerodynamics Analysis Tool Using Physics-Informed Machine Learning," arXiv:2503.16323, 2025. https://doi.org/10.48550/arXiv.2503.16323
Yu, S., Jung, Y.-J., Cho, B.-D., and Lee, G.-S., "Design, Fabrication, and In-Flight Demonstration of a 24S NCM Battery System for an eVTOL Aircraft," Batteries, Vol. 12, No. 9, 2026, Paper 317. https://doi.org/10.3390/batteries12090317
Barrett, S. R. H., Brown, A., and Gomez-Vega, N., "Silent, Solid-State Propulsion for Advanced Air Mobility Vehicles," NASA Innovative Advanced Concepts Phase I Final Report, Massachusetts Institute of Technology, Cambridge, MA, 2023.
Sheldahl, R. E., and Klimas, P. C., "Aerodynamic Characteristics of Seven Symmetrical Airfoil Sections Through 180-Degree Angle of Attack for Use in Aerodynamic Analysis of Vertical Axis Wind Turbines," SAND80-2114, Sandia National Laboratories, Albuquerque, NM, 1981. https://doi.org/10.2172/6548367
Hoerner, S. F., Fluid-Dynamic Drag, published by the author, Midland Park, NJ, 1965.
MacNeill, R., and Verstraete, D., "Propeller Optimisation for an Electrically-Powered Tactical UAS," 31st Congress of the International Council of the Aeronautical Sciences, ICAS 2018-0404, Belo Horizonte, 2018.
Persystems, INV-60V-120A inverter, product data sheet, https://persystems.com/en/inverters/inv-60v-120a/, accessed 29 October 2026.
Ohtake, T., Nakae, Y., and Motohashi, T., "Nonlinearity of the Aerodynamic Characteristics of NACA0012 Aerofoil at Low Reynolds Numbers," Journal of the Japan Society for Aeronautical and Space Sciences, Vol. 55, No. 644, 2007, pp. 439–445. https://doi.org/10.2322/JJSASS.55.439
```
