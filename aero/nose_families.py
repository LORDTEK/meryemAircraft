# -*- coding: utf-8 -*-
"""R-25: the four nose-blade families of Supplement S5, re-derived with this folder's own code; nose_thrust_lapse.py
reads them.

For each family (2 and 3 blades per rotor, design section c_l 0.55 and 0.70) nose_propeller_crossing.fm_icin_hatve
finds the uniform pitch shift d_theta at which the hover figure of merit is 0.599 (the fixed-pitch blade of the paper)
and reads the cruise efficiency on the same blade. reaction_torque.py's per-rotor hover torque (P_pair / 2) / omega_h
is recomputed from the same points. Regression targets (committed outputs of this folder):
  nose-propeller-crossing.txt: d_th 13.7 / 10.5 / 11.6 / 8.7, FM 0.603 / 0.598 / 0.598 / 0.591,
                               eta 0.648 / 0.683 / 0.632 / 0.643
  reaction-torque-result.txt:  omega_h 197.3 / 219.3 / 201.8 / 220.3 rad/s, pair 10.85 / 10.94 / 10.95 / 11.08 kW,
                               torque per rotor 27.49 / 24.95 / 27.15 / 25.15 N m
Writes nose-families.json (read by nose_thrust_lapse.py) and prints nose-families-result.txt.

Usage: ~/.venvs/meryem-aero/bin/python -B nose_families.py > nose-families-result.txt
"""
import hashlib
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SHA256 = {"tip_propeller.py": "25ffea25dd372d71e450b58e45473d8989d1d08823dd65860f75f1b7ce8ed637",
          "nose_propeller.py": "31905aab24f62dd72ae0bd9464a800ab972985e93d5e310a67102a30190f2d18",
          "nose_propeller_crossing.py": "887a425ca65ec3cdf6bcfeca539060f744200b0b17a9cb4123bb0cd6a07b3f6b"}
for _name, _h in SHA256.items():
    with open(os.path.join(HERE, _name), "rb") as _fh:
        assert hashlib.sha256(_fh.read()).hexdigest() == _h, "hash mismatch: %s" % _name
sys.path.insert(0, HERE)
FAMILIES_JSON = os.path.join(HERE, "nose-families.json")


def head(s):
    print("\n" + s)
    print("-" * len(s))
    sys.stdout.flush()


import nose_propeller as NP  # noqa: E402
import nose_propeller_crossing as NC  # noqa: E402

T0 = time.time()
print("R-25: THE FOUR NOSE-BLADE FAMILIES (Supplement S5), RE-DERIVED")
print("modules: tip_propeller.py, nose_propeller.py and nose_propeller_crossing.py of this folder (SHA-256 asserted)")
print("nose: D %.2f m, hover thrust W %.1f N (MTOW %.1f kg), cruise %.0f m/s at T %.2f N (L/D %.1f)"
      % (NP.D_BURUN, NP.W_N, NP.MTOW, NP.V_SEYIR, NP.T_SEYIR, NP.LD_SEYIR))

head("0. Cross-check of the general engine against tip_propeller.py (nose_propeller.capraz_denetim)")
a, b = NP.capraz_denetim()
print("nose_propeller engine: omega %.0f rad/s, T %.2f N, pair %.0f W" % a)
print("tip_propeller.py:      omega %.0f rad/s, T %.2f N, pair %.0f W" % b)
dev = abs(a[2] - b[2]) / b[2]
print("power deviation %.2f %%" % (100 * dev))
assert dev < 0.02

head("1. The fixed-pitch blade of each family (FM 0.599 in hover), and its cruise efficiency")
TARGET = {(2, 0.55): (13.7, 0.603, 0.648, 197.3, 10.85, 27.49),
          (2, 0.70): (10.5, 0.598, 0.683, 219.3, 10.94, 24.95),
          (3, 0.55): (11.6, 0.598, 0.632, 201.8, 10.95, 27.15),
          (3, 0.70): (8.7, 0.591, 0.643, 220.3, 11.08, 25.15)}
print("%-5s %-5s %7s %7s %7s %7s %9s %9s %9s %9s %10s"
      % ("B", "c_l", "d_th", "FM", "eta", "J", "om_h r/s", "P_h kW", "om_c r/s", "P_c W", "Q_rotor Nm"))
out = {}
for B in (2, 3):
    rot = NP.Rotor(NP.D_BURUN, 2 * B)
    for cl in (0.55, 0.70):
        dth, k = NC.fm_icin_hatve(rot, cl)
        Q = (k["P_h"] / 2.0) / k["om_h"]
        print("%-5d %-5.2f %7.2f %7.3f %7.3f %7.2f %9.1f %9.2f %9.1f %9.1f %10.2f"
              % (B, cl, dth, k["FM"], k["eta"], k["J"], k["om_h"], k["P_h"] / 1000.0, k["om_c"], k["P_c"], Q))
        t = TARGET[(B, cl)]
        assert abs(dth - t[0]) < 0.06 and abs(k["FM"] - t[1]) < 6e-4 and abs(k["eta"] - t[2]) < 6e-4
        assert abs(k["om_h"] - t[3]) < 0.06 and abs(k["P_h"] / 1000.0 - t[4]) < 6e-3 and abs(Q - t[5]) < 6e-3
        out["%d-%.2f" % (B, cl)] = dict(B=B, cl=cl, dth=dth, FM=k["FM"], eta=k["eta"], J=k["J"], om_h=k["om_h"],
                                       P_h=k["P_h"], om_c=k["om_c"], P_c=k["P_c"], Q_rotor=Q)
print("regression against nose-propeller-crossing.txt and reaction-torque-result.txt: OK (to their printed digits)")

with open(FAMILIES_JSON, "w") as fh:
    json.dump(out, fh, indent=1, sort_keys=True)
print("\nwritten: nose-families.json")
print("hover check: W^1.5/sqrt(2 rho A) / 0.599 = %.0f W (the paper's 10.9 kW)"
      % (NP.W_N ** 1.5 / math.sqrt(2 * NP.RHO * math.pi * (NP.D_BURUN / 2) ** 2) / 0.599))
print("\nrun time %.0f s" % (time.time() - T0))
