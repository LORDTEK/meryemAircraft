"""R-22 follow-up (2026-11-03): rpm-capped driven pairs with the opposite pairs BRAKED instead of free-wheeling.

tipthrust_rpmcap.py leaves the opposite pairs free-wheeling (R-22's scheme). The paper's cruise state is zero shaft
torque, and a commanded moment may depart from it on either side: braking the idle pairs below their free-wheel speed
makes them drag more and widens the thrust difference. The brake is taken to 0.75 of the free-wheel speed, where
the braked side's stations reach -16 deg, the edge of the polar's attached range (R-25's B4 check).
M = 2 L (T(min(omega_335W, c omega_hover)) - T(0.75 omega_fw)), never negative. Same model as tipthrust.py.
Regression: at each speed the free-wheel thrust equals tipthrust's state() value (asserted).
Writes tipthrust-rpmcap-brake-moments.txt for transition_at_speed.py (TMV_MODE=lapsecap).
Usage: ~/.venvs/meryem-aero/bin/python -B -I tipthrust_rpmcap_brake.py > tipthrust-rpmcap-brake-result.txt
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
CAPS = (1.00, 1.05, 1.10, 1.15)
KB = 0.75
VS = [float(v) for v in range(0, 36)]
esr = Pair("equivalent single rotor")
OM_H, T_H = hover(esr)
print("R-22 follow-up: rpm-capped driven pairs, opposite pairs braked to %.2f of their free-wheel speed" % KB)
print("hover: %.1f rad/s, %.3f N at %.0f W per pair; M(0) = %.2f N m" % (OM_H, T_H, P_LIM, 2 * L_ARM * T_H))
rows = []
for V in VS:
    s = state(esr, V, OM_H)
    if s["ofw"] > 0:
        Tfw_chk = esr(V, s["ofw"])[0]
        assert abs(Tfw_chk - s["Tfw"]) < 1e-12, (V, Tfw_chk, s["Tfw"])
        Tb = esr(V, KB * s["ofw"])[0]
    else:
        Tb = 0.0
    Ms = []
    for c in CAPS:
        om = min(s["op"], c * OM_H)
        T = esr(V, om)[0]
        Ms.append(2 * L_ARM * max(0.0, T - min(Tb, s["Tfw"])))
    rows.append((V, s, Tb, Ms))
print("%5s | %7s %7s %7s | " % ("V_ax", "T_fw", "T_brk", "M_a") + " ".join("c=%.2f" % c for c in CAPS) + "   (M in N m, opposite side braked)")
for V, s, Tb, Ms in rows:
    print("%5.1f | %7.2f %7.2f %7.2f | " % (V, s["Tfw"], Tb, s["Mp"]) + " ".join("%6.2f" % M for M in Ms))
with open(os.path.join(HERE, "tipthrust-rpmcap-brake-moments.txt"), "w", encoding="utf-8") as fh:
    fh.write("# V_ax " + " ".join("cap_%.2f" % c for c in CAPS) + "  (N m; opposite pairs braked to 0.75 omega_fw; tipthrust_rpmcap_brake.py)\n")
    for V, s, Tb, Ms in rows:
        fh.write("%.1f " % V + " ".join("%.6f" % M for M in Ms) + "\n")
print("\nwritten: tipthrust-rpmcap-brake-moments.txt; run time %.0f s" % (time.time() - T0))
