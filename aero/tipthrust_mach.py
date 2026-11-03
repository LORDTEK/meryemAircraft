# -*- coding: utf-8 -*-
"""R-22: compressibility check on the tip-pair thrust and moment.

Why. Line a of tipthrust.py needs a helical tip Mach number near 0.8 and above from about 20 m/s, and the hover point
itself runs at a tip Mach number of 0.68; tip_propeller.py's NeuralFoil polar is incompressible. This script reruns the
hover point and lines a and b at selected axial speeds with NeuralFoil called through AeroSandbox's wrapper, once at
Mach 0 (the reference) and once at each station's Mach number W / a. The difference between the two is the
compressibility effect in AeroSandbox's model (critical Mach from the incompressible Cp_min by Laitone's rule, wave
drag, buffet lift loss). It is an estimate fitted to transonic aerofoil data at high Reynolds number, not a validation
at the blade's Reynolds numbers of 4e4 to 2e5.

Usage: ~/.venvs/meryem-aero/bin/python -B tipthrust_mach.py > tipthrust-mach-result.txt
"""
import math
import time

import numpy as np

import tipthrust_model as m

T_START = time.time()
m.regression()
print("R-22: COMPRESSIBILITY CHECK ON THE TIP-PAIR THRUST AND MOMENT")
print("bemt(B=2) equals tip_propeller.bemt_sabit bit for bit at 4 points: OK")
print("models: NeuralFoil as tip_propeller.kesit_kuvvet (the main model); NeuralFoil through AeroSandbox at Mach 0;")
print("        the same at the station Mach number. Equivalent single rotor, the frozen c_l 0.68 blade, as tipthrust.py.")

NF = m.Pair("NeuralFoil, as tip_propeller.py")
INC = m.Pair("AeroSandbox wrapper, Mach 0", polar=lambda a, Re: m.asb_polar(a, Re, 0.0))
CMP = m.Pair("AeroSandbox wrapper, station Mach", polar=m.asb_polar, mach=True)

m.head("1. Hover at 335 W per pair")
print("%-36s %9s %8s %8s %8s %7s %8s" % ("model", "om rad/s", "tip m/s", "tipMach", "T N", "FM", "M0 N m"))
HOV = {}
for p in (NF, INC, CMP):
    om_h, T_h = m.hover(p)
    HOV[p.label] = om_h
    print("%-36s %9.1f %8.1f %8.3f %8.3f %7.3f %8.2f"
          % (p.label, om_h, om_h * m.R, om_h * m.R / m.A_SOUND, T_h, m.fm_one_disc(T_h, m.P_LIM),
             2 * m.L_ARM * T_h))

# stations at the incompressible hover point: Mach, incidence and AeroSandbox's critical Mach
om_h = HOV[INC.label]
T, P, al, Re, _ = INC(m.V_HOVER, om_h)
W = Re * m.MU / (m.RHO * m.C)
import aerosandbox as asb  # noqa: E402
o = asb.Airfoil(m.tp.KESIT).get_aero_from_neuralfoil(alpha=al, Re=Re, mach=W / m.A_SOUND, model_size="medium")
r, _ = m.tp.serit()
print("\nstations at the AeroSandbox Mach-0 hover point (%.0f rad/s): Mach, incidence, critical Mach" % om_h)
print("%8s %8s %8s %8s" % ("r/R", "Mach", "alpha", "M_crit"))
for i in range(0, len(r), 3):
    print("%8.3f %8.3f %8.2f %8.3f" % (r[i] / m.R, W[i] / m.A_SOUND, al[i], o["mach_crit"][i]))
print("stations above their critical Mach: %d of %d" % (int((W / m.A_SOUND > o["mach_crit"]).sum()), len(r)))

m.head("2. Lines a (335 W, rpm free) and b (each model's own hover rpm), opposite pairs free-wheeling")
print("%5s | %8s %8s %6s | %8s %8s | %7s %7s | %7s %7s"
      % ("V_ax", "M_a NF", "M_a M0", "Mtip", "M_a Mach", "ratio", "M_b M0", "M_b Mach", "Tfw M0", "Tfw Mach"))
rows = []
for V in (m.V_HOVER, 5.0, 10.0, 15.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0):
    snf = m.state(NF, V, HOV[NF.label])
    si = m.state(INC, V, HOV[INC.label])
    sc = m.state(CMP, V, HOV[CMP.label])
    rows.append((V, snf, si, sc))
    print("%5.1f | %8.2f %8.2f %6.3f | %8.2f %8.3f | %7.2f %7.2f | %7.3f %7.3f"
          % (V, snf["Mp"], si["Mp"], si["mt"], sc["Mp"], sc["Mp"] / si["Mp"] if si["Mp"] > 0 else float("nan"),
             si["Mr"], sc["Mr"], si["Tfw"], sc["Tfw"]))
print("(M in N m; 'ratio' = line a with station Mach over line a at Mach 0; Mtip = helical tip Mach on line a)")
for V, snf, si, sc in rows:
    if V in (22.0, 26.0, 30.0):
        print("V_ax %4.1f: line a with station Mach: T %.2f N at %.0f rad/s, tip Mach %.3f; at Mach 0: T %.2f N at %.0f"
              % (V, sc["Tp"], sc["op"], sc["mt"], si["Tp"], si["op"]))
Vg = [x[0] for x in rows]
print("\ncrossings (axial speed, linear interpolation on this grid; 0.0 = already below at hover):")
for key, line in (("Mp", "line a"), ("Mr", "line b")):
    for level in m.M_DEMAND:
        print("  %s below %4.1f N m: NeuralFoil %s, Mach 0 %s, station Mach %s m/s"
              % (line, level, m.fmt_v(m.crossing(Vg, [x[1][key] for x in rows], level)),
                 m.fmt_v(m.crossing(Vg, [x[2][key] for x in rows], level)),
                 m.fmt_v(m.crossing(Vg, [x[3][key] for x in rows], level))))
V30 = [x for x in rows if x[0] == 30.0][0]
print("\ndCm at 30 m/s, line a: NeuralFoil %.4f, Mach 0 %.4f, station Mach %.4f (held hover rating 0.0324)"
      % (V30[1]["Mp"] / m.qSc(30.0), V30[2]["Mp"] / m.qSc(30.0), V30[3]["Mp"] / m.qSc(30.0)))
dc = V30[3]["Mp"] / m.qSc(30.0)
print("R-21's cruise moments against it: raw RANS -0.016 uses %.0f %%, offset removed -0.003 to +0.006 %.0f to %.0f %%,"
      % (100 * 0.016 / dc, 100 * 0.003 / dc, 100 * 0.006 / dc))
print("  the VLM -0.0013 %.0f %%" % (100 * 0.0013 / dc))
print("\nrun time %.0f s" % (time.time() - T_START))
