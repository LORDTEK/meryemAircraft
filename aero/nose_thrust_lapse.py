"""Thrust available from the nose pair against axial speed at its hover power (2026-11-03).

kos() holds the thrust at 1.066 W "until cruise speed is reached" (aero/transition_dynamics.py: Tmax = 1.066 * W,
from aero/README.md's T/W table: the nose pair gives W at its hover power and the tip pairs add 32.4 N while making the
full pitch moment). Both parts are static values. This computes the nose part at speed: each fixed-pitch family of
S5 (nose-families.json, written by nose_families.py), at its own hover power P_h, rotor speed solved for P = P_h
(rpm free), with nose_propeller.Rotor.coz (hashes asserted below). The tip part is R-22's line a (two pairs at
335 W): T_tips(V) = 2 T_a(V) from tipthrust-result.txt. Prints T_avail(V) / (1.066 W) and writes
nose-thrust-lapse.txt for transition_at_speed.py.
Usage: ~/.venvs/meryem-aero/bin/python -B nose_thrust_lapse.py > nose-thrust-lapse-result.txt
"""
import hashlib
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SHA256 = {"tip_propeller.py": "25ffea25dd372d71e450b58e45473d8989d1d08823dd65860f75f1b7ce8ed637",
          "nose_propeller.py": "31905aab24f62dd72ae0bd9464a800ab972985e93d5e310a67102a30190f2d18"}
for _name, _h in SHA256.items():
    with open(os.path.join(HERE, _name), "rb") as _fh:
        assert hashlib.sha256(_fh.read()).hexdigest() == _h, "hash mismatch: %s" % _name
sys.path.insert(0, HERE)
FAMILIES_JSON = os.path.join(HERE, "nose-families.json")
import numpy as np  # noqa: E402
from scipy.optimize import brentq  # noqa: E402
import nose_propeller as NP  # noqa: E402

W = NP.W_N
fams = json.load(open(FAMILIES_JSON, encoding="utf-8"))
VS = [0.0, 2, 5, 8, 10, 12, 15, 18, 20, 22, 24, 26, 28, 30]

# tip pairs, line a: T_a column of tipthrust-result.txt section 3
TT = {}
on = False
for ln in open(os.path.join(HERE, "tipthrust-result.txt"), encoding="utf-8"):
    if ln.lstrip().startswith("V_ax |"):
        on = True
        continue
    if on:
        p = ln.replace("|", " ").split()
        try:
            v = float(p[0])
        except (ValueError, IndexError):
            break
        TT[v] = float(p[8])
assert abs(TT[0.0] - 16.079) < 1e-3 and abs(TT[22.0] - 7.971) < 1e-3 and abs(TT[30.0] - 4.766) < 1e-3


def tip2(V):
    ks = sorted(TT)
    for i in range(1, len(ks)):
        if V <= ks[i]:
            w = (V - ks[i - 1]) / (ks[i] - ks[i - 1])
            return 2 * (TT[ks[i - 1]] + w * (TT[ks[i]] - TT[ks[i - 1]]))
    return 2 * TT[ks[-1]]


print("Nose-pair thrust at its hover power against axial speed (rpm free), plus R-22's line a for two tip pairs")
print("W = %.1f N; the model's T_max = 1.066 W = %.1f N; tip pairs at hover 2 x %.2f N" % (W, 1.066 * W, TT[0.0]))
out = {}
for key, fam in fams.items():
    rot = NP.Rotor(NP.D_BURUN, 2 * fam["B"])
    c, th = NP.aile(rot, fam["cl"], 250.0, fam["dth"])
    Ph = fam["P_h"]
    # regression: the hover point of nose-families.json
    Th0, Qh0, _ = rot.coz(1e-3, fam["om_h"], c, th)
    assert abs(Th0 - W) / W < 2e-3 and abs(Qh0 * fam["om_h"] - Ph) / Ph < 2e-3, (key, Th0, Qh0 * fam["om_h"])
    rows = []
    for V in VS:
        Vq = max(V, 1e-3)
        f = lambda o: rot.coz(Vq, o, c, th)[1] * o - Ph
        om = brentq(f, 0.8 * fam["om_h"], 4.0 * fam["om_h"], xtol=1e-4)
        T, Q, a = rot.coz(Vq, om, c, th)
        rows.append((V, om, T, a))
    out[key] = rows
    print("\nfamily %s (B %d per rotor, c_l %.2f, d_theta %.2f deg), hover power %.0f W" % (key, fam["B"], fam["cl"], fam["dth"], Ph))
    print("%6s %9s %8s %9s %8s %8s %10s %12s" % ("V_ax", "om rad/s", "om/om_h", "T_nose N", "T/W", "T_tips N", "T_tot/W", "T_tot/1.066W"))
    for V, om, T, a in rows:
        tt = tip2(V)
        print("%6.1f %9.1f %8.3f %9.1f %8.3f %8.1f %10.3f %12.3f" % (V, om, om / fam["om_h"], T, T / W, tt, (T + tt) / W, (T + tt) / (1.066 * W)))
with open(os.path.join(HERE, "nose-thrust-lapse.txt"), "w", encoding="utf-8") as fh:
    fh.write("# V_ax and T_avail/(1.066 W) per family (nose at P_h rpm free + two tip pairs on line a)\n")
    fh.write("# V " + " ".join(fams) + "\n")
    for i, V in enumerate(VS):
        fh.write("%.1f " % V + " ".join("%.6f" % ((out[k][i][2] + tip2(V)) / (1.066 * W)) for k in fams) + "\n")
print("\nwritten: nose-thrust-lapse.txt")
