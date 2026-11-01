"""Run C (revision item 3): the zero-shaft-torque blade-element solver of Run B with the section polar taken
from MEASUREMENT: Ohtake, Nakae & Motohashi 2007, JJSASS 55(644):439-445, doi 10.2322/JJSASS.55.439,
NACA 0012, chord 75 mm, span 300 mm, Re 6e4 to 1e5 (Fig. 4 lift, Fig. 7 drag; balance measurement).

The two figures were digitized at 600 dpi (cfd/sources/digitize_ohtake.py): the frame gives the axes, the
dashed grid lines check them (all within 0.01 deg and 0.0003 in C_d), and each value is the median of the
marker pixels of all five Reynolds numbers in that column, so it is a 6e4-1e5 band value, not one Re.
Symmetrized: cl = (cl(a) - cl(-a))/2, cd = (cd(a) + cd(-a))/2. Beyond 16 deg: held at the 16 deg row.
Geometry frozen as in Run B (design c_l = 0.68, the design behind the paper's 0.0154).
Usage: python run_c.py   (from aero/; or pass a directory containing tip_propeller.py)
"""
import sys, numpy as np
if len(sys.argv) > 1:
    sys.path.insert(0, sys.argv[1])
import tip_propeller as tp

A  = np.arange(0, 17, dtype=float)
CL = np.array([0.0, 0.1376, 0.2585, 0.3464, 0.4337, 0.5, 0.5628, 0.6361, 0.6872, 0.7425, 0.7842,
               0.7324, 0.7124, 0.6486, 0.6285, 0.6255, 0.6275])
CD = np.array([0.0195, 0.0200, 0.0196, 0.0204, 0.0225, 0.0248, 0.0283, 0.0317, 0.0374, 0.0443, 0.0587,
               0.0792, 0.1547, 0.1837, 0.2057, 0.2214, 0.2387])


def ohtake(alfa_deg, Re):
    a = np.abs(np.asarray(alfa_deg, dtype=float))
    s = np.sign(alfa_deg)
    return s * np.interp(a, A, CL), np.interp(a, A, CD)


c, th = tp.hover_tasarla(cl_hedef=0.68)          # geometry frozen with the baseline polar
om_a, T_a = tp.sifir_tork(c, th)
alfa_a = tp.bemt_sabit(tp.V_SEYIR, om_a, c, th)[2]
print("conditions: V %.1f m/s; frozen blade of the paper's design (c_l 0.68); 8 discs" % tp.V_SEYIR)
print("Run A (NeuralFoil):          omega %.0f rad/s  axial %.3f N  dCD0(8 discs) %.5f" % (om_a, T_a, tp.dcd0(T_a)))
print("  alpha range %.1f .. %.1f deg" % (alfa_a.min(), alfa_a.max()))
tp.kesit_kuvvet = ohtake                           # Run C: only the section source changes
om_c, T_c = tp.sifir_tork(c, th)
if om_c:
    alfa_c = tp.bemt_sabit(tp.V_SEYIR, om_c, c, th)[2]
    print("Run C (Ohtake, measured):    omega %.0f rad/s  axial %.3f N  dCD0(8 discs) %.5f" % (om_c, T_c, tp.dcd0(T_c)))
    print("  alpha range %.1f .. %.1f deg; stations beyond 16 deg: %d" % (alfa_c.min(), alfa_c.max(), int((np.abs(alfa_c) > 16).sum())))
else:
    print("Run C: no zero-torque root found")
