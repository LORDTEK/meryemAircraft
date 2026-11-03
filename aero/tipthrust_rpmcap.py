"""R-22 follow-up (2026-11-03): the tip-pair moment against axial speed with an rpm cap on the driven pairs.

Line a (335 W, rpm free) needs the driven rotors at up to 1.29 x the hover rpm at 30 m/s; line b holds them at the
hover rpm and loses all authority from 26.4 m/s. Between the two, the driven pairs run at
    omega = min(omega_335W(V), c x omega_hover),
so that both the hover power and an rpm cap c bind. Same model as tipthrust.py (tipthrust_model, hash asserted there):
equivalent single rotor, NeuralFoil, opposite pairs free-wheeling, M = 2 L (T_driven - T_fw), never negative.
Regression: c = 1 reproduces line b and a cap above line a's own ratio reproduces line a (asserted on the grid).
Writes tipthrust-rpmcap-moments.txt (V_ax and M for each cap) for transition_at_speed.py.
Usage: ~/.venvs/meryem-aero/bin/python -B -I tipthrust_rpmcap.py > tipthrust-rpmcap-result.txt
"""
import math
import os
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tipthrust_model import L_ARM, P_LIM, R, A_SOUND, Pair, hover, state  # noqa: E402

T0 = time.time()
CAPS = (1.00, 1.05, 1.10, 1.15, 1.20, 1.25)
VS = [float(v) for v in range(0, 36)]
esr = Pair("equivalent single rotor")
OM_H, T_H = hover(esr)
print("R-22 follow-up: tip-pair moment with an rpm cap on the driven pairs (equivalent single rotor, NeuralFoil)")
print("hover: %.1f rad/s, %.3f N at %.0f W per pair; M(0) = %.2f N m" % (OM_H, T_H, P_LIM, 2 * L_ARM * T_H))
rows = []
for V in VS:
    s = state(esr, V, OM_H)
    Ms = []
    for c in CAPS:
        om = min(s["op"], c * OM_H)
        T = esr(V, om)[0]
        Ms.append(2 * L_ARM * max(0.0, T - s["Tfw"]))
    rows.append((V, s, Ms))
    # regression on the grid: cap 1 = line b; a cap above line a's own ratio = line a
    assert abs(Ms[0] - s["Mr"]) < 1e-9 or s["op"] < OM_H, (V, Ms[0], s["Mr"])
    for c, M in zip(CAPS, Ms):
        if c * OM_H >= s["op"]:
            assert abs(M - s["Mp"]) < 1e-9, (V, c, M, s["Mp"])
print("regression: cap 1.00 equals line b where the hover rpm is within 335 W, and every cap at or above line a's own")
print("  rpm ratio equals line a (asserted at every grid speed)")
print()
print("%5s | %7s %7s %6s | %7s %7s | " % ("V_ax", "op/om_h", "Mtip_a", "M_a", "M_b", "T_fw") + " ".join("c=%.2f" % c for c in CAPS))
for V, s, Ms in rows:
    print("%5.1f | %7.3f %7.3f %6.2f | %7.2f %7.2f | " % (V, s["op"] / OM_H, s["mt"], s["Mp"], s["Mr"], s["Tfw"]) + " ".join("%6.2f" % M for M in Ms))
print("(M in N m; Mtip_a = helical tip Mach on line a; with a cap c the helical tip Mach at 30 m/s is %s)"
      % ", ".join("%.2f: %.3f" % (c, math.hypot(c * OM_H * R, 30.0) / A_SOUND) for c in CAPS))
with open(os.path.join(HERE, "tipthrust-rpmcap-moments.txt"), "w", encoding="utf-8") as fh:
    fh.write("# V_ax " + " ".join("cap_%.2f" % c for c in CAPS) + "  (N m; tipthrust_rpmcap.py)\n")
    for V, s, Ms in rows:
        fh.write("%.1f " % V + " ".join("%.6f" % M for M in Ms) + "\n")
print("\nwritten: tipthrust-rpmcap-moments.txt; run time %.0f s" % (time.time() - T0))
