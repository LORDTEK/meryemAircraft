"""Supplement S7: the transition with the aerodynamic moment set to zero, across reference profiles, controller gains,
the stall break of the lift model and the drag data. Corrected model (transition_dynamics.py, REVISION).
Conditions: 50 kg design (HAFIF), M = 23.0 N m, t_r = 2 s, entry climb 5 m/s, C_m = 0, run 40 s after the profile.
loss = lowest altitude below entry; fall = largest fall from an earlier high point (every 2 s case first climbs about
10 m on the entry climb at full thrust). The lift model is linear up to the stall break and a flat plate beyond it
(transition_dynamics.kos); the break is coded at 12 deg and moved to 14 deg as a sensitivity.
Usage: python transition_gain_sweep.py
"""
import math
import os
import sys
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import transition_dynamics as td

D2R = math.pi / 180.0
BASE = dict(td.HAFIF, M_kontrol=23.0, tr=2.0)
PROFILES = (("dogrusal", "linear"), ("duz", "cubic 3t^2-2t^3"), ("bang", "bang-bang"))
GAINS = (1, 2, 4, 8, 16)


def one(job):
    kind, key, ast = job
    kw = dict(BASE, astall=ast * D2R)
    if kind == "profile":
        kw.update(profil=key)
    elif kind == "gain":
        kw.update(profil="bang", kp=25.0 * key, kd=10.0 * key ** 0.5)
    else:
        prof, CD0 = key
        kw.update(profil=prof, CD0=CD0, e=0.817)
    return job, td.kos(**kw)


def cell(r):
    return "loss %5.2f m  fall %5.2f m  sat %4.2f s  alpha %4.1f" % (-r["kayip"], r["dusus"], r["doyma"], r["al_max"]) + (
        "  TUMBLES" if r["firladi"] else "")


if __name__ == "__main__":
    jobs = [("profile", p, a) for p, _ in PROFILES for a in (12.0, 14.0)]
    jobs += [("gain", k, a) for k in GAINS for a in (12.0, 14.0)]
    jobs += [("drag", (p, c), 12.0) for p, _ in PROFILES for c in (0.0248, 0.0285, 0.0381)]
    with Pool(4) as pool:
        out = dict(pool.map(one, jobs))
    print("CONDITIONS: 50 kg (HAFIF), M = 23.0 N m, t_r = 2 s, entry climb 5 m/s, C_m = 0; CD0 0.0248, e 0.85")
    print("PROFILES (Kp 25, Kd 10)")
    for p, name in PROFILES:
        for a in (12.0, 14.0):
            print("  %-17s break %2.0f deg: %s" % (name, a, cell(out[("profile", p, a)])))
    print("GAINS (bang-bang; Kp x k, Kd x sqrt(k))")
    for k in GAINS:
        for a in (12.0, 14.0):
            print("  k = %2d  break %2.0f deg: %s" % (k, a, cell(out[("gain", k, a)])))
    print("DRAG (e 0.817 with CD0 0.0285 and 0.0381; first row of each profile: CD0 0.0248, e 0.817), break 12 deg")
    for p, name in PROFILES:
        for c in (0.0248, 0.0285, 0.0381):
            print("  %-17s CD0 %.4f: %s" % (name, c, cell(out[("drag", (p, c), 12.0)])))
