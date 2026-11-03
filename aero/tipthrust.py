# -*- coding: utf-8 -*-
"""R-22: the tip pairs' thrust and pitching moment against airspeed.

Why. The corrected transition model (transition_dynamics.py; the paper's Sec. 4.4 and Supplement S7) holds the
control-moment limit at the tip pairs' hover rating, 23.0 N m, at every speed. This script computes the pairs' thrust
and moment against airspeed with the repository's own blade-element model; transition_at_speed.py uses the result.

The model (tip_propeller.py of this folder, unchanged; the frozen c_l 0.68 blade; tip_propeller.bemt_sabit rebuilt as
tipthrust_model.bemt with the blade count, a momentum-area factor, the polar and the swirl factor as arguments) and its
assumptions (the coaxial pair as an equivalent single rotor; axial inflow; M = 2 L (T_max - T_fw) with L = 0.71 m;
line a at 335 W per pair with the rpm free, line b at the hover rpm) are described in tipthrust_model.py.

Usage: ~/.venvs/meryem-aero/bin/python -B tipthrust.py > tipthrust-result.txt
"""
import math
import time

import numpy as np
from scipy.optimize import brentq

T_START = time.time()
from tipthrust_model import (tp, SHA256_TP, D2R, R, A_SOUND, L_ARM, P_LIM, T_RATING, S_REF, MAC,  # noqa: E402
                      W_N, V_HOVER, M_DEMAND, T_MT, T_COAX, qSc, fm_one_disc, fm_two_discs, C, TH, bemt, Pair,
                      om_fw, om_power, om_thrust, hover, state, crossing, fmt_v, head, sheldahl, ohtake)

# ===============================================================================================================
print("R-22: TIP-PAIR THRUST AND PITCHING MOMENT AGAINST AIRSPEED")
print("model: tip_propeller.py of this folder, SHA-256 %s..., unchanged"
      % SHA256_TP[:16])
import aerosandbox as _asb  # noqa: E402
import neuralfoil as _nf    # noqa: E402
print("NeuralFoil %s, AeroSandbox %s, numpy %s" % (_nf.__version__, _asb.__version__, np.__version__))
print("rotor D %.2f m, hub %.2f R, %d strips, section %s; pitch arm L = %.2f m; S %.3f m2, MAC %.4f m"
      % (tp.D, tp.r_h / R, tp.N_SERIT, tp.KESIT, L_ARM, S_REF, MAC))
print("check: 2 x %.1f N x %.2f m = %.2f N m (the transition limit 23.0)" % (T_RATING, L_ARM, 2 * T_RATING * L_ARM))
print("paper's hover readings at 335 W: %.2f N (0.702 rating), %.2f N (momentum theory, FM 0.599 on one disc),"
      % (T_RATING, T_MT))
print("  %.2f N (0.85 x that, 15 %% coaxial loss); moments %.2f, %.2f, %.2f N m"
      % (T_COAX, 2 * L_ARM * T_RATING, 2 * L_ARM * T_MT, 2 * L_ARM * T_COAX))
print("check: 23.0 / qSc(30) = 23.0 / %.1f = %.4f (the text's 0.032)" % (qSc(30.0), 23.0 / qSc(30.0)))

head("Blade: tip_propeller.hover_tasarla(cl_hedef=0.68), every third station")
r_st, _ = tp.serit()
print("%8s %10s %10s %10s" % ("r/R", "chord mm", "c/R", "theta deg"))
for i in range(0, len(r_st), 3):
    print("%8.3f %10.2f %10.4f %10.2f" % (r_st[i] / R, 1e3 * C[i], C[i] / R, TH[i] / D2R))
print("(the chord is clipped at 0.40 R inboard and 0.04 R outboard by the design routine)")

# ---------------------------------------------------------------------------------------------------------------
head("0. Regression against the committed model and outputs")
for (V, om) in ((V_HOVER, 2117.0), (15.0, 2400.0), (30.0, 2623.0), (30.0, 3000.0)):
    T0, Q0, a0 = tp.bemt_sabit(V, om, C, TH)
    T1, Q1, a1, _, _ = bemt(V, om, 2)
    assert T0 == T1 and Q0 == Q1 and np.array_equal(a0, a1), (V, om)
print("bemt(B=2) equals tip_propeller.bemt_sabit bit for bit at 4 points (V 0 to 30 m/s, 2117 to 3000 rad/s): OK")
iso = Pair("two isolated discs", esr=False)
o30 = om_fw(iso, 30.0)
T30 = iso(30.0, o30)[0] / 2
print("free-wheel, one isolated disc, V 30: omega %.0f rad/s, axial %.3f N, dCD0 (8 discs) %.5f"
      % (o30, T30, tp.dcd0(T30)))
print("   committed run-c-result.txt (Run A):  omega 2623 rad/s, axial -2.094 N, dCD0 0.01535")
assert abs(o30 - 2623) < 1.0 and abs(T30 + 2.094) < 2e-3 and abs(tp.dcd0(T30) - 0.01535) < 2e-5

# ---------------------------------------------------------------------------------------------------------------
head("1. Hover (V = 1e-3 m/s, as tip_propeller.py)")
esr = Pair("equivalent single rotor")
print("%-34s %9s %8s %8s %7s %8s %10s %10s"
      % ("reading, operating point", "om rad/s", "rpm", "tip m/s", "T N", "P W", "FM 1 disc", "FM 2 discs"))
hov = {}
for p in (iso, esr):
    o16 = om_thrust(p, V_HOVER, T_RATING, 300.0)
    T16, P16 = p(V_HOVER, o16)[:2]
    o335 = om_power(p, V_HOVER, P_LIM, 300.0)
    T335, P335, al335, Re335, _ = p(V_HOVER, o335)
    hov[p.label] = (o16, T16, P16, o335, T335, P335)
    for tag, o, T, P in (("at 16.2 N", o16, T16, P16), ("at 335 W", o335, T335, P335)):
        print("%-34s %9.1f %8.0f %8.1f %7.2f %8.1f %10.3f %10.3f"
              % ("%s, %s" % (p.label, tag), o, o * 60 / (2 * math.pi), o * R, T, P,
                 fm_one_disc(T, P), fm_two_discs(T, P)))
    print("%-34s alpha %.2f to %.2f deg, Re %.1e to %.1e at 335 W"
          % ("", al335.min(), al335.max(), Re335.min(), Re335.max()))
o16, T16, P16, OM_H, T_H, _ = hov[esr.label]
print("paper: 16.2 N at 335 W, FM 0.702 on one disc (the reference design's rating); 14.6 N at FM 0.599")
print("HOVER CHECK (equivalent single rotor): %.2f N at 335 W, %+.1f %% from 16.2 N; 16.2 N needs %.1f W, %+.1f %%;"
      % (T_H, 100 * (T_H / T_RATING - 1), P16, 100 * (P16 / P_LIM - 1)))
print("  FM %.3f against 0.702. The isolated-disc reading gives %.2f N at 335 W (%+.1f %%), FM %.3f on one disc."
      % (fm_one_disc(T_H, P_LIM), hov[iso.label][4], 100 * (hov[iso.label][4] / T_RATING - 1),
         fm_one_disc(hov[iso.label][4], P_LIM)))
print("hover rpm (the rpm limit of line b): %.1f rad/s = %.0f rpm, tip speed %.1f m/s, tip Mach %.3f"
      % (OM_H, OM_H * 60 / (2 * math.pi), OM_H * R, OM_H * R / A_SOUND))

# ---------------------------------------------------------------------------------------------------------------
head("2. Numerics: iteration count and swirl factor (equivalent single rotor)")
o25 = om_power(esr, 25.0, P_LIM, om_fw(esr, 25.0))
ofw30 = om_fw(esr, 30.0)
print("%-30s %10s %10s %10s %10s %12s" % ("point", "T(150) N", "T(600) N", "P(150) W", "P(600) W", "resid m/s"))
for tag, V, om in (("hover, 335 W", V_HOVER, OM_H), ("25 m/s, 335 W", 25.0, o25), ("30 m/s, free-wheel", 30.0, ofw30)):
    a = esr(V, om)
    b = Pair("x", tur=600)(V, om)
    print("%-30s %10.4f %10.4f %10.2f %10.2f %12.1e" % (tag, a[0], b[0], a[1], b[1], a[4]))
sw = Pair("swirl 1", swirl=1.0)
oh_sw, Th_sw = hover(sw)
o25_sw = om_power(sw, 25.0, P_LIM, om_fw(sw, 25.0))
T25_sw = sw(25.0, o25_sw)[0]
ofw30_sw = om_fw(sw, 30.0)
Tfw30_sw = sw(30.0, ofw30_sw)[0]
print("swirl: the repo's momentum balance takes the swirl at the disc as dQt / (2 disk (V+v)); the textbook balance")
print("  has dQt / (disk (V+v)). With the textbook factor: hover T at 335 W %.3f N (repo %.3f), T at 25 m/s and 335 W"
      % (Th_sw, T_H, ))
print("  %.3f N (repo %.3f), free-wheel T at 30 m/s %.3f N (repo %.3f)"
      % (T25_sw, esr(25.0, o25)[0], Tfw30_sw, esr(30.0, ofw30)[0]))

# ---------------------------------------------------------------------------------------------------------------
head("3. Thrust and moment against axial speed (equivalent single rotor, NeuralFoil)")
VS = [float(v) for v in range(0, 36)]
VS[0] = V_HOVER
PRINT_V = (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 35)
rows = [state(esr, V, OM_H) for V in VS]
print("line a: driven pairs at 335 W, rpm free; line b: driven pairs at the hover rpm %.0f rad/s; opposite pairs"
      % OM_H)
print("free-wheeling. M = 2 x %.2f x (T_driven - T_fw), per side of two pairs; dCm = M / (q S MAC)." % L_ARM)
print("%5s | %7s %7s | %7s %7s | %7s %6s %6s %7s | %7s %7s | %7s %7s"
      % ("V_ax", "T_b N", "P_b W", "om_fw", "T_fw N", "om_a", "om_a/h", "Mtip", "T_a N", "M_a Nm", "M_b Nm",
         "dCm_a", "dCm_b"))
for s in rows:
    if round(s["V"]) in PRINT_V:
        dca = s["Mp"] / qSc(s["V"]) if s["V"] >= 5 else float("nan")
        dcb = s["Mr"] / qSc(s["V"]) if s["V"] >= 5 else float("nan")
        print("%5.1f | %7.2f %7.1f | %7.0f %7.3f | %7.0f %6.3f %6.3f %7.3f | %7.2f %7.2f | %7.4f %7.4f"
              % (round(s["V"]), s["Th"], s["Ph"], s["ofw"], s["Tfw"], s["op"], s["op"] / OM_H, s["mt"], s["Tp"],
                 s["Mp"], s["Mr"], dca, dcb))
print("(dCm not printed below 5 m/s; a negative P_b means the rotor would be braked below its free-wheel speed)")
print("\nstation incidence on line a and free-wheeling, deg, and the largest residual on line a:")
for s in rows:
    if round(s["V"]) in (0, 10, 20, 25, 30, 35):
        fw = "%.1f to %.1f" % (s["al_fw"].min(), s["al_fw"].max()) if s["al_fw"] is not None else "-"
        print("  V %4.0f: line a %.1f to %.1f (Re %.1e to %.1e); free-wheel %s"
              % (round(s["V"]), s["al_p"].min(), s["al_p"].max(), s["Re_p"].min(), s["Re_p"].max(), fw))
print("  largest last-step change of the axial induction on line a: %.1e m/s" % max(s["res_p"] for s in rows))
print("\nnumerics along line a: the same states (V, omega) solved with 150 (as above), 600 and 2,000 iterations")
e600, e2000 = Pair("600", tur=600), Pair("2000", tur=2000)
dTmax, dPmax, worst = 0.0, 0.0, None
for s in rows:
    a, b, c = esr(s["V"], s["op"]), e600(s["V"], s["op"]), e2000(s["V"], s["op"])
    dT = max(abs(a[0] - b[0]), abs(a[0] - c[0]))
    dP = max(abs(a[1] - b[1]), abs(a[1] - c[1]))
    if dT > dTmax:
        dTmax, worst = dT, s["V"]
    dPmax = max(dPmax, dP)
print("  largest thrust difference %.3f N (at %.0f m/s), largest power difference %.2f W"
      % (dTmax, round(worst), dPmax))
print("  (the unsettled station is the root, r/R 0.17 to 0.20, alternating between positive and negative thrust;")
print("  the model sets no induction on negative-thrust stations, so the fixed-point iteration has a two-cycle there)")

Va = [s["V"] for s in rows]
Ma = [s["Mp"] for s in rows]
Mb = [s["Mr"] for s in rows]


def refine(level, key):
    """Crossing speed refined by root-finding on the model itself, bracketed by the grid."""
    vg = crossing(Va, [s[key] for s in rows], level)
    if vg is None:
        return None, None
    lo, hi = math.floor(vg), math.floor(vg) + 1.0
    vr = brentq(lambda V: state(esr, V, OM_H)[key] - level, lo, hi, xtol=5e-3)
    return vg, vr


head("4. Speeds at which the moment falls below the demands (axial speed)")
cross_main = {}
for key, name in (("Mp", "line a, 335 W, rpm free"), ("Mr", "line b, hover rpm")):
    for level in M_DEMAND:
        vg, vr = refine(level, key)
        cross_main[(key, level)] = vr
        print("%-26s below %4.1f N m at %s m/s (grid interpolation %s)"
              % (name, level, fmt_v(vr), fmt_v(vg)))
vz = crossing(Va, [s["Th"] - s["Tfw"] for s in rows], 0.0)
vx = crossing(Va, [OM_H - s["ofw"] for s in rows], 0.0)
print("line b reaches zero at %s m/s; the free-wheel speed passes the hover rpm at %s m/s (the same point)"
      % (fmt_v(vz), fmt_v(vx)))
vm = crossing(Va, [-s["mt"] for s in rows], -0.75)
print("line a: helical tip Mach passes 0.75 at %s m/s and 0.80 at %s m/s"
      % (fmt_v(vm), fmt_v(crossing(Va, [-s["mt"] for s in rows], -0.80))))

# ---------------------------------------------------------------------------------------------------------------
head("5. At the transition's peak-demand points (R-21's peak-demand check, 23.0 N m held; points copied)")
PEAKS = (("paper law, 3 s, PD", 22.2, 9.9, 11.7),
         ("paper law, 3 s, hold ki 50", 23.7, 9.5, 12.4),
         ("raw RANS line, 3 s, PD", 23.6, 8.9, 20.7),
         ("paper law, 6 s, PD", 15.8, 9.0, 5.7),
         ("raw RANS line, 6 s, PD", 17.4, 8.2, 10.3),
         ("raw RANS line, 6 s, hold ki 50", 30.2, 6.8, 12.5))
print("%-32s %6s %6s %6s %8s %8s %8s %9s"
      % ("case", "V", "alpha", "V_ax", "demand", "M_a", "M_b", "a / b"))
for name, V, al, dem in PEAKS:
    Vax = V * math.cos(al * D2R)
    s = state(esr, Vax, OM_H)
    ok = ("yes" if s["Mp"] >= dem else "NO") + " / " + ("yes" if s["Mr"] >= dem else "NO")
    print("%-32s %6.1f %6.1f %6.2f %8.1f %8.2f %8.2f %9s" % (name, V, al, Vax, dem, s["Mp"], s["Mr"], ok))
print("(V in m/s, alpha in deg, moments in N m; 'a / b': does the line cover the demand)")

head("6. What the driven pairs need for the demands (axial speed)")
print("%5s %7s | %8s %7s %6s %8s | %8s %7s %6s %8s"
      % ("V_ax", "T_fw", "om 11.7", "om/om_h", "Mtip", "P W", "om 20", "om/om_h", "Mtip", "P W"))
for V in (20.0, 22.0, 24.0, 26.0, 30.0):
    s = state(esr, V, OM_H)
    out = []
    for level in M_DEMAND:
        Tneed = level / (2 * L_ARM) + s["Tfw"]
        o = om_thrust(esr, V, Tneed, s["ofw"])
        P = esr(V, o)[1]
        out.append((o, o / OM_H, math.hypot(o * R, V) / A_SOUND, P))
    print("%5.1f %7.3f | %8.0f %7.3f %6.3f %8.0f | %8.0f %7.3f %6.3f %8.0f"
          % ((V, s["Tfw"]) + out[0] + out[1]))
print("(power per driven pair; 335 W is the hover rating)")

head("7. Cruise, 30 m/s axial")
s30 = rows[30]
print("q S MAC = %.1f N m. Held hover rating 23.0 N m -> dCm %.4f." % (qSc(30.0), 23.0 / qSc(30.0)))
print("line a: T %.2f N driven, %.2f N free-wheeling -> M %.2f N m, dCm %.4f (%.0f %% of the held value)"
      % (s30["Tp"], s30["Tfw"], s30["Mp"], s30["Mp"] / qSc(30.0), 100 * s30["Mp"] / 23.0))
print("        at omega %.0f rad/s (%.2f x hover rpm), helical tip Mach %.3f"
      % (s30["op"], s30["op"] / OM_H, s30["mt"]))
print("line b: T %.2f N at the hover rpm, below free-wheeling -> M %.2f N m, dCm %.4f"
      % (s30["Th"], s30["Mr"], s30["Mr"] / qSc(30.0)))
print("free-wheel share of line a's moment: %.0f %%" % (100 * -s30["Tfw"] / (s30["Tp"] - s30["Tfw"])))
print("R-21's cruise moments against line a's %.4f: raw RANS -0.016 uses %.0f %%; offset removed -0.003 to +0.006"
      % (s30["Mp"] / qSc(30.0), 100 * 0.016 / (s30["Mp"] / qSc(30.0))))
print("  uses %.0f to %.0f %%; the VLM -0.0013 %.0f %%."
      % (100 * 0.003 / (s30["Mp"] / qSc(30.0)), 100 * 0.006 / (s30["Mp"] / qSc(30.0)),
         100 * 0.0013 / (s30["Mp"] / qSc(30.0))))

# ---------------------------------------------------------------------------------------------------------------
head("8. Sensitivity: the coaxial loss (the paper's own bracket, 23.0 / 20.7 / 17.6 N m)")
print("The equivalent single rotor gives each blade the pair's mean induction and no extra interference. The paper's")
print("two lower hover readings (14.58 N, FM 0.599 as the pair's value; 12.39 N, a further 15 % coaxial loss) are")
print("entered two ways:")
print("  (i) as an induced loss: the momentum area of every station multiplied by kA, tuned so that the pair gives the")
print("      reading's thrust at 335 W in hover, and the whole model rerun (its loss then varies with speed);")
print("  (ii) as a constant thrust factor on the driven pairs, f = reading / %.2f N, the free-wheel thrust unchanged."
      % T_H)


def tune_kA(target):
    def g(kA):
        p = Pair("tune", kA=kA)
        return hover(p)[1] - target
    return brentq(g, 0.2, 1.0, xtol=1e-5)


SENS = [("equivalent single rotor (main)", esr, OM_H, rows)]
for target in (T_MT, T_COAX):
    kA = tune_kA(target)
    p = Pair("induced loss, kA %.4f" % kA, kA=kA)
    om_h, T_h = hover(p)
    rws = [state(p, V, om_h) for V in VS]
    SENS.append(("(i) %.2f N: kA %.4f" % (target, kA), p, om_h, rws))
summary = []
for name, p, om_h, rws in SENS:
    summary.append((name, rws[0]["Tp"], om_h, [s["Mp"] for s in rws], [s["Mr"] for s in rws], rws))
for target in (T_MT, T_COAX):
    f = target / T_H
    Mp_c = [2 * L_ARM * max(0.0, f * s["Tp"] - s["Tfw"]) for s in rows]
    Mr_c = [2 * L_ARM * max(0.0, f * s["Th"] - s["Tfw"]) for s in rows]
    summary.append(("(ii) %.2f N: f %.3f" % (target, f), f * T_H, OM_H, Mp_c, Mr_c, None))
print("\nline a (335 W, rpm free)")
print("%-34s %7s %7s | %6s %6s %6s %6s | %7s | %7s %7s"
      % ("reading", "T0 N", "om_h", "M0", "M22", "M26", "M30", "dCm30", "<20 at", "<11.7 at"))
for name, T0, om_h, Mp_, Mr_, _ in summary:
    print("%-34s %7.2f %7.0f | %6.2f %6.2f %6.2f %6.2f | %7.4f | %7s %7s"
          % (name, T0, om_h, Mp_[0], Mp_[22], Mp_[26], Mp_[30], Mp_[30] / qSc(30.0),
             fmt_v(crossing(Va, Mp_, 20.0)), fmt_v(crossing(Va, Mp_, 11.7))))
print("\nline b (the reading's own hover rpm)")
print("%-34s %7s %7s | %6s %6s %6s %6s | %7s | %7s %7s"
      % ("reading", "T0 N", "om_h", "M0", "M22", "M26", "M30", "dCm30", "<20 at", "<11.7 at"))
for name, T0, om_h, Mp_, Mr_, _ in summary:
    print("%-34s %7.2f %7.0f | %6.2f %6.2f %6.2f %6.2f | %7.4f | %7s %7s"
          % (name, T0, om_h, Mr_[0], Mr_[22], Mr_[26], Mr_[30], Mr_[30] / qSc(30.0),
             fmt_v(crossing(Va, Mr_, 20.0)), fmt_v(crossing(Va, Mr_, 11.7))))
print("(M in N m at 0, 22, 26 and 30 m/s axial; crossings by grid interpolation, 0.0 = already below at hover;")
print(" om_h in rad/s)")
for name, p, om_h, rws in SENS[1:]:
    print("%s: line a at 30 m/s needs omega %.0f rad/s (%.2f x its hover rpm), tip Mach %.3f"
          % (name, rws[30]["op"], rws[30]["op"] / om_h, rws[30]["mt"]))

# ---------------------------------------------------------------------------------------------------------------
head("9. Check: the section source (R-4's polars, the same blade, the main model otherwise)")
print("Not the paper's moment bracket; run because at speed the free-wheel drag is part of the moment.")
print("(each polar with its own hover rpm at 335 W; crossings by grid interpolation, 0.0 = already below at hover)")
print("%-34s %7s %7s | %6s %6s %6s | %6s %6s %6s | %6s %6s %6s %6s"
      % ("polar", "T0 N", "om_h", "Ma22", "Ma26", "Ma30", "Mb22", "Mb26", "Mb30", "a<20", "a<11.7", "b<20",
         "b<11.7"))
print("%-34s %7.2f %7.0f | %6.2f %6.2f %6.2f | %6.2f %6.2f %6.2f | %6s %6s %6s %6s"
      % ("NeuralFoil (main)", T_H, OM_H, Ma[22], Ma[26], Ma[30], Mb[22], Mb[26], Mb[30],
         fmt_v(crossing(Va, Ma, 20.0)), fmt_v(crossing(Va, Ma, 11.7)), fmt_v(crossing(Va, Mb, 20.0)),
         fmt_v(crossing(Va, Mb, 11.7))))
for name, pol in (("Sheldahl-Klimas 8e4 (run_b.py)", sheldahl), ("Ohtake, measured (run_c.py)", ohtake)):
    p = Pair(name, polar=pol)
    om_h, T_h = hover(p)
    rws = [state(p, V, om_h) for V in VS]
    mp, mr = [s["Mp"] for s in rws], [s["Mr"] for s in rws]
    print("%-34s %7.2f %7.0f | %6.2f %6.2f %6.2f | %6.2f %6.2f %6.2f | %6s %6s %6s %6s"
          % (name, T_h, om_h, mp[22], mp[26], mp[30], mr[22], mr[26], mr[30],
             fmt_v(crossing(Va, mp, 20.0)), fmt_v(crossing(Va, mp, 11.7)), fmt_v(crossing(Va, mr, 20.0)),
             fmt_v(crossing(Va, mr, 11.7))))
    print("%-34s T_fw at 30 m/s %.3f N per pair (NeuralFoil %.3f); line a T at 30 m/s %.3f N (NeuralFoil %.3f)"
          % ("", rws[30]["Tfw"], rows[30]["Tfw"], rws[30]["Tp"], rows[30]["Tp"]))

# ---------------------------------------------------------------------------------------------------------------
head("10. Side reading: the transition model's thrust")
print("The model's thrust of 1.066 W (%.1f N) counts 2 x 16.2 = 32.4 N from two tip pairs at the hover rating." %
      (1.066 * W_N))
for V in (15, 20, 22, 24, 26, 30):
    s = rows[V]
    print("  V_ax %2d m/s: two pairs at 335 W give %.1f N, %.1f N (%.1f %% of W) less than 32.4 N"
          % (V, 2 * s["Tp"], 32.4 - 2 * s["Tp"], 100 * (32.4 - 2 * s["Tp"]) / W_N))

print("\nrun time %.0f s" % (time.time() - T_START))
