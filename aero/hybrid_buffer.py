"""Hybrid buffer: does a battery + capacitor store close the sizing loop?

The paper sizes the buffer by power alone (mass = bus demand / specific power) and finds that no
battery reported as built delivers the specific power its closures imply (Sec. 4.6, Table 6).
This script sizes the buffer for a vertical event of given duration instead, so that the store must
hold the event's power for the event's duration, and lets a capacitor bank (behind a DC-DC
converter) carry the takeoff increment. The loop is re-closed with that buffer mass at fixed fuel
fraction (range unchanged).

Battery model: each store is a list of measured discharges to cut-off (duration, mean specific power).
A store that holds p_i for t_i also holds it for any shorter time, and at a lower power it delivers at
least the energy p_i t_i (energy delivered falls as power rises). The specific power it holds for t is
therefore at least the largest over its points of p_i (where t_i >= t) or p_i t_i / t (where t_i < t).
Between and beyond the points the store may do better. One caveat runs the other way: the Batemo points
are CONSTANT-CURRENT discharges, while the buffer must deliver constant power, so the current rises as
the voltage sags and cut-off comes earlier. Read as constant-power capability the points are optimistic;
derating them by 10 to 15 percent adds 3 to 7 points of takeoff mass (revision notes R-1, 2026-10-31).

Usage: python hybrid_buffer.py   (from aero/; or pass the aero dir)
"""
import math
import sys

if len(sys.argv) > 1:
    sys.path.insert(0, sys.argv[1])
import baseline as BL                                     # noqa: E402
import buffer as B                                        # noqa: E402


def sustained(store, t_s):
    """Lower bound on the specific power (kW/kg) the store holds for t_s seconds, from its points."""
    return store.get("pack", 1.0) * max(p if t >= t_s else p * t / t_s for t, p in store["points"])


def battery_mass(P_kW, t_s, store):
    """Lightest battery that holds P_kW for t_s seconds."""
    if P_kW <= 0.0:
        return 0.0
    return P_kW / sustained(store, t_s)


def capacitor_mass(P_kW, t_s, cap):
    """Capacitor bank plus its DC-DC converter delivering P_kW at the bus for t_s seconds.

    The bank swings from full to its lowest voltage, so only cap["u"] of its stored energy is usable;
    converter losses are taken from the bank.
    """
    if P_kW <= 0.0:
        return 0.0
    P_bank = P_kW / cap["eta_conv"]
    m_bank = max(P_bank / cap["p"], P_bank * t_s / 3600.0 / (cap["u"] * cap["e"] / 1000.0))
    return m_bank + P_kW / cap["p_conv"]


def profile_mass(P_plateau, t_event, P_spike, t_spike, store, cap=None):
    """Lightest store for a vertical event: a plateau of P_plateau kW for t_event s, with an extra
    P_spike kW during the first t_spike s (takeoff with the tip pairs at full thrust).

    Battery alone: it must hold the peak for t_spike and the event's mean power for t_event.
    Hybrid: the battery carries the plateau and the capacitor bank the spike. Both masses are
    linear in power, so splitting a flat plateau never helps (the lightest answer there is one
    device); a capacitor can only pay for itself on the short spike. Returns (mass, layout).
    """
    P_mean = P_plateau + P_spike * t_spike / t_event
    alone = max((P_plateau + P_spike) / sustained(store, t_spike), P_mean / sustained(store, t_event))
    if cap is None or P_spike <= 0.0:
        return alone, "battery"
    split = battery_mass(P_plateau, t_event, store) + capacitor_mass(P_spike, t_spike, cap)
    return (split, "battery + capacitor") if split < alone else (alone, "battery")


def close(cd0, eta_p, t_s, store, cap=None, rounds=400, t_spike=5.0):
    """The paper's sizing loop (buffer.kapat_ozgul) with the buffer sized for a vertical event:
    the hover plateau for t_s seconds plus the takeoff increment for t_spike seconds."""
    m, ld_clean, g = B.kur(cd0, eta_p)
    LD = ld_clean * m.LD_carpan
    eta_c = g["eta_seyir"] * m.eta_carpan
    MTOW = 60.0
    for _ in range(rounds):
        A = MTOW / g["disk_yuklemesi"]
        W = MTOW * BL.G
        P_h = W ** 1.5 / (g["eta_hover"] * math.sqrt(2 * BL.RHO * A)) / 1000.0
        P_c = W * g["V"] / LD / eta_c / 1000.0
        P_e = P_c * g["motor_pay"]
        f_prop = BL.F_TAHRIK_SABIT + P_e / BL.OZGUL_GUC / MTOW
        P_bus = max(B.tampon_gucu(P_h, P_e, "aski"), 0.0)
        P_up = max(B.tampon_gucu(P_h, P_e, "kalkis"), 0.0) - P_bus
        m_buf, layout = profile_mass(P_bus, t_s, P_up, t_spike, store, cap)
        f_empty = BL.ORTAK["f_govde"] + BL.ORTAK["f_aviyonik"] + f_prop + m_buf / MTOW + m.f_ek
        denom = 1.0 - f_empty - BL.ORTAK["f_yakit"]
        if denom <= 0.0:
            return None
        new = g["m_faydali"] / denom
        if abs(new - MTOW) < 1e-10:
            break
        MTOW = 0.5 * MTOW + 0.5 * new
    else:
        return None
    if MTOW > 2000.0:
        return None
    return dict(MTOW=MTOW, m_buf=m_buf, f_buf=m_buf / MTOW, P_bus=P_bus, layout=layout)


def self_test():
    """A store that holds its power for any duration must reproduce buffer.kapat_ozgul (takeoff demand),
    and the lower bound must return each measured point at its own duration."""
    for k, dk, ek in B.KAPANISLAR:
        for sp in (1.49, 4.0):
            a = B.kapat_ozgul(B.CD0[dk], B.ETA_P[ek], sp, "kalkis")
            b = close(B.CD0[dk], B.ETA_P[ek], 30.0, {"points": [(math.inf, sp)]})
            assert (a is None) == (b is None)
            if a is not None:
                assert abs(a["MTOW"] - b["MTOW"]) < 1e-6, (k, sp, a["MTOW"], b["MTOW"])
    for name, st in STORES:
        for t, p in st["points"]:
            if math.isfinite(t):
                assert abs(sustained(st, t) - p * st.get("pack", 1.0)) < 1e-12 or sustained(st, t) > p * st.get("pack", 1.0), name
    print("self-test: power-only sizing reproduces buffer.kapat_ozgul; the bound returns every measured point")


def negative_test():
    """The event sizing must not be inert: a duration limit and a capacitor must change the answer."""
    k, dk, ek = B.KAPANISLAR[0]
    any_time = close(B.CD0[dk], B.ETA_P[ek], 60.0, {"points": [(math.inf, 4.0)]})
    ten_s = close(B.CD0[dk], B.ETA_P[ek], 60.0, {"points": [(10.0, 4.0)]})
    assert ten_s is None or ten_s["m_buf"] > any_time["m_buf"] + 1e-6, "duration limit ignored"
    weak = {"points": [(math.inf, 1.0)]}
    strong_cap = {"p": 10.0, "e": 5.0, "u": 0.75, "eta_conv": 0.97, "p_conv": 10.0}
    alone = close(B.CD0[dk], B.ETA_P[ek], 10.0, weak)
    mixed = close(B.CD0[dk], B.ETA_P[ek], 10.0, weak, strong_cap)
    assert alone is None or (mixed is not None and mixed["m_buf"] < alone["m_buf"]), "capacitor ignored"
    print("negative test: a duration limit and a capacitor both change the buffer mass")


# Stores. points: measured constant-power discharges to cut-off, (seconds, kW/kg); pack: cell-to-pack
# mass factor applied to cell data (0.61-0.65 X-57 battery and modules, NTRS 20180005737; 0.60-0.61
# Formula E; 0.64-0.67 Rolls-Royce ACCEL). Cell points are Batemo measurements (constant current from
# full charge, 25 C, free convection, stop at 2.5 V or the cell's surface-temperature limit); Batemo is
# a commercial laboratory and its data are not peer reviewed.
PACK = 0.65
STORES = [
    ("Yu et al. 2026 pack, bench average, as in the paper", dict(points=[(249.0, 1.49)])),
    ("Bare hobby LiPo pack (Bardwell 2018, RDQ 4S 1300)", dict(points=[(44.0, 4.9)])),
    ("Amprius 50Q cell x 0.65 (Batemo, two points)", dict(points=[(28.8, 5.81), (44.9, 4.86)], pack=PACK)),
    ("V4Smart UHP-3X A-sample cell x 0.65 (Batemo)", dict(points=[(120.0, 5.22)], pack=PACK)),
    ("EVE 30PL production cell x 0.65 (Batemo)", dict(points=[(125.0, 4.72)], pack=PACK)),
    ("Design-study assumption 4 kW/kg, any duration (Barrett et al. 2023)", dict(points=[(math.inf, 4.0)])),
]
# Lithium-ion capacitor module for the takeoff increment: Musashi MPA45G342P, 316.7 F, 45.6-26.4 V,
# 16 mOhm, 5.9 kg (datasheet). Stored 15.5 Wh/kg; usable fraction 1-(26.4/45.6)^2 = 0.665. Power per kg
# bracketed: 0.35 kW/kg (95 % efficiency at 26.4 V) to 2.0 kW/kg (the >500 A, <5 s current limit).
# Converter: 15 kW/kg at 97 % (low-voltage assumption; 44 kW/kg reported for 15 kW SiC at 450-800 V).
CAPS = [("LIC module, 95 % efficiency", dict(p=0.35, e=15.5, u=0.665, eta_conv=0.97, p_conv=15.0)),
        ("LIC module, current limit", dict(p=2.0, e=15.5, u=0.665, eta_conv=0.97, p_conv=15.0))]
T_SPIKE = 5.0
EVENTS = (30.0, 60.0)                       # the durations the paper names (Sec. 4.6)
SWEEP = (15.0, 30.0, 45.0, 60.0, 90.0, 120.0)


def span(rows):
    """'lo-hi kg (+a to +b %)' across the four closures, or the count that do not close."""
    ok = [r for r in rows if r[1] is not None]
    if len(ok) < len(rows):
        return "%d of %d do not close" % (len(rows) - len(ok), len(rows))
    m = [r[1]["MTOW"] for r in ok]
    d = [100.0 * (r[1]["MTOW"] / r[2] - 1.0) for r in ok]
    return "%.1f-%.1f kg (%+.0f to %+.0f %%)" % (min(m), max(m), min(d), max(d))


def report():
    base = {k: B.kapat(B.CD0[dk], B.ETA_P[ek])["MTOW"] for k, dk, ek in B.KAPANISLAR}
    print("\nconditions: the paper's four closures (buffer.KAPANISLAR), fuel fraction %.2f fixed (range unchanged),"
          % BL.ORTAK["f_yakit"])
    print("  sea level (rho %.4f kg/m3); vertical event = hover plateau for t s plus the takeoff increment"
          % BL.RHO)
    print("  (tip pairs at full thrust, %.4f x hover) for the first %g s; the buffer mass replaces the paper's"
          % (B.UC_PAYI, T_SPIKE))
    print("  3.6 percent buffer. Paper closures: " + ", ".join("%s %.1f kg" % (k, base[k]) for k in base))
    print("  battery: lower bound from measured points (module docstring); pack factor %.2f on cell data" % PACK)
    for name, st in STORES:
        pts = ", ".join("%s s at %.2f" % ("any" if math.isinf(t) else "%g" % t, p) for t, p in st["points"])
        print("    %-70s %s kW/kg%s" % (name, pts, " (cell)" if "pack" in st else ""))
    for name, cap in CAPS:
        print("  capacitor %s: %.2f kW/kg at the bank, %.1f Wh/kg stored, usable %.3f, converter %.0f kW/kg at %.2f"
              % (name, cap["p"], cap["e"], cap["u"], cap["p_conv"], cap["eta_conv"]))

    print("\nheld specific power (pack level, kW/kg) for %g, 30 and 60 s:" % T_SPIKE)
    for name, st in STORES:
        print("  %-70s %5.2f %5.2f %5.2f" % (name, sustained(st, T_SPIKE), sustained(st, 30.0), sustained(st, 60.0)))

    for t in EVENTS:
        print("\n== event %g s (battery alone)" % t)
        for name, st in STORES:
            rows = []
            for k, dk, ek in B.KAPANISLAR:
                r = close(B.CD0[dk], B.ETA_P[ek], t, st)
                rows.append("%s: does not close" % k if r is None else
                            "%s %.1f kg (buffer %.2f kg, %+.0f%%)" % (k, r["MTOW"], r["m_buf"], 100 * (r["MTOW"] / base[k] - 1)))
            print("  " + name + "\n      " + " | ".join(rows))
        for cname, cap in CAPS:
            lighter = []
            for name, st in STORES:
                gain = []
                for k, dk, ek in B.KAPANISLAR:
                    a, h = close(B.CD0[dk], B.ETA_P[ek], t, st), close(B.CD0[dk], B.ETA_P[ek], t, st, cap)
                    if h is not None and h["layout"] != "battery":
                        gain.append(a["MTOW"] - h["MTOW"] if a is not None else math.inf)
                if gain:
                    lighter.append("%s (%.1f-%.1f kg lighter)" % (name.split(" (")[0], min(gain), max(gain)))
            print("  + %s carrying the takeoff increment: %s"
                  % (cname, "; ".join(lighter) if lighter else "never lighter than the battery alone"))

    print("\n== takeoff mass against event duration (battery alone; range across the four closures)")
    for name, st in STORES:
        print("  " + name)
        for t in SWEEP:
            rows = [(k, close(B.CD0[dk], B.ETA_P[ek], t, st), base[k]) for k, dk, ek in B.KAPANISLAR]
            print("      %5g s: %s" % (t, span(rows)))

    print("\n== cell-to-pack factor 0.60 / 0.65 / 0.70 (battery alone)")
    for name, st in STORES:
        if "pack" not in st:
            continue
        for t in EVENTS:
            cells = []
            for f in (0.60, 0.65, 0.70):
                s = dict(st, pack=f)
                cells.append(span([(k, close(B.CD0[dk], B.ETA_P[ek], t, s), base[k]) for k, dk, ek in B.KAPANISLAR]))
            print("  %-48s %3g s: %s" % (name.split(" (")[0], t, " / ".join(cells)))


if __name__ == "__main__":
    self_test()
    negative_test()
    report()
