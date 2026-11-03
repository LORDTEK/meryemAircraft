# -*- coding: utf-8 -*-
"""R-22: the tip-pair model shared by tipthrust.py, tipthrust_mach.py, tipthrust_rpmcap.py and
tipthrust_rpmcap_brake.py.

Model, from this folder, unchanged:
  tip_propeller.py; its SHA-256 is asserted below.
  Blade: tip_propeller.hover_tasarla(cl_hedef=0.68), the frozen blade behind the paper's 0.0154 (run_b.py, run_c.py;
         Supplement S8). D 0.20 m, hub 0.15 R, 24 strips, NACA 0012 from NeuralFoil 0.3.3 ("medium").
  Equations: tip_propeller.bemt_sabit, rebuilt below as bemt() with the blade count, a momentum-area factor, the
         section polar, the swirl factor and an optional station Mach number as arguments. bemt(B=2) reproduces
         bemt_sabit bit for bit (asserted in tipthrust.py and tipthrust_mach.py).

Coaxial pair: an equivalent single rotor, one 0.20 m disc with both rotors' blades (B = 4) carrying the pair's thrust.
  This is how nose_propeller.cift_coz treats the nose pair, and how the paper defines a pair's figure of merit (one
  disc, the pair's shaft power; Table S2a). tip_propeller.py itself runs each rotor as an isolated disc of 8.1 N; that
  reading is evaluated at hover for comparison only.

Inflow: axial. Tables are in the axial speed V_ax; a flight speed V at incidence alpha gives V_ax = V cos(alpha).
  The in-plane component V sin(alpha) is neglected (advance ratio below 0.02 at the points used).

Moment: M = 2 L (T_max - T_fw), L = 0.71 m (2 x 16.2 N x 0.71 m = 23.0 N m). The two pairs on one side of the wing
  plane are driven to a limit; the two opposite pairs free-wheel at zero shaft torque, the paper's cruise state
  (T_fw = 0 at V = 0, as in the hover rating). Limits on the driven pairs:
    (a) the hover power, 335 W per pair, with the rpm free;
    (b) the hover rpm, the speed at which the pair draws 335 W at V = 0.
  A driven pair cannot give less than free-wheeling, so M >= 0.
"""
import hashlib
import math
import os
import sys

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
SHA256_TP = "25ffea25dd372d71e450b58e45473d8989d1d08823dd65860f75f1b7ce8ed637"
with open(os.path.join(HERE, "tip_propeller.py"), "rb") as fh:
    assert hashlib.sha256(fh.read()).hexdigest() == SHA256_TP, "tip_propeller.py is not the file this model was checked against"
sys.path.insert(0, HERE)
import tip_propeller as tp  # noqa: E402

RHO, MU, D2R, R = tp.RHO, tp.MU, tp.D2R, tp.R
A_DISC = math.pi * R ** 2
A_SOUND = 340.3        # m/s, as nose_propeller.py
L_ARM = 0.71           # m, pitch arm of the tip pairs (thrust.py KOL)
P_LIM = 335.0          # W per pair, the reference design's hover rating
T_RATING = 16.2        # N per pair at 335 W
FM_SIZING = 0.599      # Table S2a
S_REF, MAC = 1.979, 0.6514
W_N = 50.0 * 9.81      # N, as the transition model (m = 50 kg)
V_HOVER = 1e-3         # m/s, as tip_propeller.py
M_DEMAND = (11.7, 20.0)

T_MT = (P_LIM * FM_SIZING * math.sqrt(2 * RHO * A_DISC)) ** (2.0 / 3.0)   # 14.58 N, the paper's 0.599 reading
T_COAX = 0.85 * T_MT                                                      # 12.39 N, 15 percent coaxial loss


def qSc(V):
    return 0.5 * RHO * V * V * S_REF * MAC


def fm_one_disc(T, P):
    """The paper's definition: one disc, the pair's thrust and shaft power (Table S2a)."""
    return T ** 1.5 / math.sqrt(2 * RHO * A_DISC) / P


def fm_two_discs(T, P):
    """tip_propeller.py's definition: each rotor an isolated disc carrying T/2."""
    return 2 * (T / 2) ** 1.5 / math.sqrt(2 * RHO * A_DISC) / P


C, TH = tp.hover_tasarla(cl_hedef=0.68)          # the frozen blade (deterministic: tip_propeller_sweep.py)


def bemt(V, om, B, kA=1.0, polar=None, tur=150, swirl=2.0, mach=False):
    """tip_propeller.bemt_sabit, with B, the momentum-area factor kA, the polar, the swirl factor and the station
    Mach number (mach=True: polar(alfa, Re, W / A_SOUND)) as arguments.

    kA = 1, polar = tp.kesit_kuvvet, swirl = 2, tur = 150 and mach = False are bemt_sabit itself. Returns T and Q of the
    disc, the station incidences, the station Reynolds numbers and the last relaxation step of the axial induction.
    """
    polar = polar or tp.kesit_kuvvet
    c, th = C, TH
    r, dr = tp.serit()
    v = np.full_like(r, 5.0)
    w = np.zeros_like(r)
    res = float("nan")
    for _ in range(tur):
        Va, Vt = V + v, om * r - w
        W = np.hypot(Va, Vt)
        phi = np.arctan2(Va, np.maximum(Vt, 1e-6))
        alfa = (th - phi) / D2R
        Re = np.clip(RHO * W * c / MU, 2e4, 2e6)
        cl, cd = polar(alfa, Re, W / A_SOUND) if mach else polar(alfa, Re)
        f = B / 2.0 * (R - r) / np.maximum(r * np.sin(phi), 1e-6)
        F = np.clip(2 / math.pi * np.arccos(np.clip(np.exp(-np.abs(f)), 0, 1)), 1e-3, 1.0)
        q = 0.5 * RHO * W ** 2 * c
        dT = B * q * (cl * np.cos(phi) - cd * np.sin(phi))
        dQt = B * q * (cl * np.sin(phi) + cd * np.cos(phi))
        disk = 4 * math.pi * RHO * r * F * kA
        with np.errstate(divide="ignore", invalid="ignore"):
            v_yeni = -V / 2.0 + np.sqrt(np.maximum(
                (V / 2.0) ** 2 + np.maximum(dT, 0.0) / disk, 0.0))
            w_yeni = dQt / np.maximum(swirl * disk * (V + v), 1e-6)
        dv = 0.3 * (np.clip(np.nan_to_num(v_yeni), 0.0, 60.0) - v)
        v += dv
        w += 0.3 * (np.clip(np.nan_to_num(w_yeni), 0.0, 0.5 * om * r) - w)
        res = float(np.abs(dv).max())
    Va, Vt = V + v, om * r - w
    W = np.hypot(Va, Vt)
    phi = np.arctan2(Va, np.maximum(Vt, 1e-6))
    alfa = (th - phi) / D2R
    Re = np.clip(RHO * W * c / MU, 2e4, 2e6)
    cl, cd = polar(alfa, Re, W / A_SOUND) if mach else polar(alfa, Re)
    q = 0.5 * RHO * W ** 2 * c
    T = (B * q * (cl * np.cos(phi) - cd * np.sin(phi)) * dr).sum()
    Q = (B * q * (cl * np.sin(phi) + cd * np.cos(phi)) * r * dr).sum()
    return T, Q, alfa, Re, res


class Pair(object):
    """One tip pair: the equivalent single rotor (esr=True) or two isolated discs (tip_propeller.py's reading)."""

    def __init__(self, label, esr=True, kA=1.0, polar=None, swirl=2.0, tur=150, mach=False):
        self.label, self.esr, self.kA, self.polar = label, esr, kA, polar
        self.swirl, self.tur, self.mach = swirl, tur, mach

    def __call__(self, V, om):
        """Pair thrust (N), pair shaft power (W), station incidences, Reynolds numbers, residual."""
        if self.esr:
            T, Q, al, Re, res = bemt(V, om, 4, self.kA, self.polar, self.tur, self.swirl, self.mach)
            return T, Q * om, al, Re, res
        T, Q, al, Re, res = bemt(V, om, 2, self.kA, self.polar, self.tur, self.swirl, self.mach)
        return 2 * T, 2 * Q * om, al, Re, res


def root(f, lo, hi, xtol=1e-2):
    if f(lo) * f(hi) > 0:
        raise RuntimeError("no sign change in [%g, %g]" % (lo, hi))
    return brentq(f, lo, hi, xtol=xtol)


def om_fw(pair, V):
    """Free-wheeling speed (zero shaft torque); zero at hover."""
    if V < 1.0:
        return 0.0
    return root(lambda om: pair(V, om)[1], 20.0, 8000.0)


def om_power(pair, V, P, lo):
    return root(lambda om: pair(V, om)[1] - P, lo, 8000.0)


def om_thrust(pair, V, T, lo):
    return root(lambda om: pair(V, om)[0] - T, lo, 8000.0)


def hover(pair):
    """Hover operating point at the power limit: rpm, thrust."""
    om_h = om_power(pair, V_HOVER, P_LIM, 300.0)
    return om_h, pair(V_HOVER, om_h)[0]


def state(pair, V, om_h):
    """Free-wheel state, line b (om_h) and line a (335 W) at the axial speed V, and the two moments."""
    ofw = om_fw(pair, V)
    if ofw > 0:
        Tfw, _, al_fw, _, _ = pair(V, ofw)
    else:
        Tfw, al_fw = 0.0, None
    Th, Ph, _, _, _ = pair(V, om_h)
    op = om_power(pair, V, P_LIM, ofw if ofw > 0 else 300.0)
    Tp, Pp, al_p, Re_p, res_p = pair(V, op)
    return dict(V=V, ofw=ofw, Tfw=Tfw, al_fw=al_fw, Th=Th, Ph=Ph, op=op, Tp=Tp, al_p=al_p, Re_p=Re_p,
                res_p=res_p, mt=math.hypot(op * R, V) / A_SOUND,
                Mp=2 * L_ARM * max(0.0, Tp - Tfw), Mr=2 * L_ARM * max(0.0, Th - Tfw))


def crossing(Vs, Ms, level):
    """First speed at which M falls below level, by linear interpolation on the grid; 0.0 if already below at the
    first grid point (hover)."""
    if Ms[0] < level:
        return 0.0
    for i in range(1, len(Vs)):
        if Ms[i - 1] >= level > Ms[i]:
            return Vs[i - 1] + (Ms[i - 1] - level) * (Vs[i] - Vs[i - 1]) / (Ms[i - 1] - Ms[i])
    return None


def fmt_v(x):
    return "%5.1f" % x if x is not None else " >35"


def head(s):
    print("\n" + s)
    print("-" * len(s))


def regression():
    """bemt(B=2) against tip_propeller.bemt_sabit, bit for bit."""
    for (V, om) in ((V_HOVER, 2117.0), (15.0, 2400.0), (30.0, 2623.0), (30.0, 3000.0)):
        T0, Q0, a0 = tp.bemt_sabit(V, om, C, TH)
        T1, Q1, a1, _, _ = bemt(V, om, 2)
        assert T0 == T1 and Q0 == Q1 and np.array_equal(a0, a1), (V, om)


# ---------------------------------------------------------------------------------------------------------------
# Section polars of R-4 (run_b.py and run_c.py of this folder; tables copied, symmetrized as there; held
# at the 16 deg row beyond 16 deg). Used in the section-source check of tipthrust.py part 9.
_A16 = np.arange(0, 17, dtype=float)
_SK_CL = np.array([0, .11, .22, .33, .44, .55, .6384, .7227, .6930, -.0010, .0413,
                   .0911, .1430, .1966, .2504, .3043, .3582])
_SK_CD = np.array([.0133, .0134, .0138, .0145, .0155, .0170, .0189, .0204, .0222,
                   .0600, .0600, .1170, .1340, .1520, .1710, .1900, .2100])
_OH_CL = np.array([0.0, 0.1376, 0.2585, 0.3464, 0.4337, 0.5, 0.5628, 0.6361, 0.6872, 0.7425, 0.7842,
                   0.7324, 0.7124, 0.6486, 0.6285, 0.6255, 0.6275])
_OH_CD = np.array([0.0195, 0.0200, 0.0196, 0.0204, 0.0225, 0.0248, 0.0283, 0.0317, 0.0374, 0.0443, 0.0587,
                   0.0792, 0.1547, 0.1837, 0.2057, 0.2214, 0.2387])


def sheldahl(alfa_deg, Re):
    a = np.abs(np.asarray(alfa_deg, dtype=float))
    return np.sign(alfa_deg) * np.interp(a, _A16, _SK_CL), np.interp(a, _A16, _SK_CD)


def ohtake(alfa_deg, Re):
    a = np.abs(np.asarray(alfa_deg, dtype=float))
    return np.sign(alfa_deg) * np.interp(a, _A16, _OH_CL), np.interp(a, _A16, _OH_CD)


_AF = None


def asb_polar(alfa_deg, Re, mach=0.0):
    """NeuralFoil 0.3.3 through AeroSandbox 4.2.10's Airfoil.get_aero_from_neuralfoil ("medium"), which adds a
    compressibility model (critical Mach from the incompressible Cp_min by Laitone's rule, wave drag, buffet lift
    loss) when mach > 0. Used only in tipthrust_mach.py."""
    global _AF
    if _AF is None:
        import aerosandbox as asb
        _AF = asb.Airfoil(tp.KESIT)
    o = _AF.get_aero_from_neuralfoil(alpha=alfa_deg, Re=Re, mach=mach, model_size="medium")
    return o["CL"], o["CD"]
