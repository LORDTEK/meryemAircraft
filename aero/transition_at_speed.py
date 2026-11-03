"""The corrected transition model with the tip pairs' moment and the thrust falling with airspeed (R-22 follow-up).

The model, kos() of transition_dynamics.py (this folder; the file of 06c46d0, its SHA-256 asserted below), holds the
control-moment limit at its hover rating and the thrust at 1.066 W at every speed. This script rebuilds kos() with
asserted single-match edits:
  the limit becomes M_kontrol * f(V), f = M(V) / M(0), from tipthrust.py (line a: the driven pairs at 335 W, rpm free;
  line b: at the hover rpm), tipthrust_mach.py (line a with the station Mach number), tipthrust_rpmcap.py (rpm caps
  c x hover rpm, idle pairs free-wheeling) or tipthrust_rpmcap_brake.py (idle pairs braked to 0.75 of their
  free-wheel speed);
  the thrust becomes 1.066 W * g(V), g from nose_thrust_lapse.py (the nose pair at its hover power, rpm free, the
  lowest of the four blade families of S5, plus two tip pairs on line a), clamped at 1;
and re-runs the approved text's set: the zero moment and the seven linear laws, on R-21's grid, 656 runs per line.
Conservative choices, stated: f and g are applied at the total speed V, not the axial component (both fall with
speed); the hover rating is scaled by f (at speed the coaxial loss matters less, R-22, so lower ratings are
understated); g's points above 1 at 2-8 m/s are not credited.
Regression: with both edits off the rebuilt function equals kos() exactly (asserted on every run of the hover-rating
line in the default mode and on 32 runs in the lapse modes).
Modes (environment variable TMV_MODE) and outputs:
  unset     hover rating held, line a, line b, line a with station Mach   -> transition-at-speed-result.txt
  caps      rpm caps 1.05-1.25, idle pairs free-wheeling                  -> transition-at-speed-caps-result.txt
  lapse     thrust lapse with the hover rating held, line a, line a Mach  -> transition-at-speed-lapse-result.txt
  lapsecap  thrust lapse with rpm caps 1.05-1.25, idle pairs free-wheeling, and 1.00-1.15, idle pairs braked
                                                                          -> transition-at-speed-lapsecap-result.txt
Each block line is followed by the time from the start (t_cr) and the height above entry (h_cr) at 95 percent of
cruise speed, over the runs of the block that reach it, and by the range of the peak incidence (alpha_max, deg) over
all the block's runs.
Usage: TMV_MODE=lapsecap python3 -B transition_at_speed.py > transition-at-speed-lapsecap-result.txt
"""
import hashlib, inspect, math, os, sys
from multiprocessing import Pool
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SHA256_TD = "36e66f2f43af19d28d983ff0486ffd167eae92f82014e8e748794f75431431ad"
with open(os.path.join(HERE, "transition_dynamics.py"), "rb") as _fh:
    assert hashlib.sha256(_fh.read()).hexdigest() == SHA256_TD, "transition_dynamics.py is not the file of 06c46d0"
sys.path.insert(0, HERE)
import transition_dynamics as td  # noqa: E402

D2R = math.pi / 180.0
H = td.HAFIF
TAB = os.path.join(HERE, "tipthrust-result.txt")        # section 3: V_ax | T_b P_b | om_fw T_fw | om_a om_a/h Mtip T_a | M_a M_b | dCm_a dCm_b
TABM = os.path.join(HERE, "tipthrust-mach-result.txt")  # section 2: V_ax | M_a NF, M_a M0, Mtip | M_a Mach, ratio | M_b M0, M_b Mach | Tfw M0, Tfw Mach


def read_table(path, cols):
    """Rows (V_ax, value at each column index) of the first table under a 'V_ax |' header, '|' read as a space."""
    rows, on = [], False
    for ln in open(path, encoding="utf-8"):
        if ln.lstrip().startswith("V_ax |"):
            on = True
            continue
        if on:
            p = ln.replace("|", " ").split()
            try:
                v = float(p[0])
            except (ValueError, IndexError):
                if rows:
                    break
                continue
            rows.append((v,) + tuple(float(p[c]) for c in cols))
    return rows


# The columns are pinned by value against R-22 before anything runs (an earlier run read p[10] and p[11], M_b and
# dCm_a, as lines a and b).
ROWS = read_table(TAB, (9, 10))            # M_a (line a), M_b (line b)
ROWSM = read_table(TABM, (1, 4))           # M_a NeuralFoil (= M_a above), M_a with the station Mach number
_r = {r[0]: r for r in ROWS}
_m = {r[0]: r for r in ROWSM}
assert ROWS[0][0] == 0.0 and len(ROWS) >= 20, ROWS[:3]
assert abs(_r[0.0][1] - 22.83) < 0.01 and abs(_r[0.0][2] - 22.83) < 0.01, _r[0.0]
assert abs(_r[22.0][1] - 14.87) < 0.01 and abs(_r[22.0][2] - 8.17) < 0.01, _r[22.0]
assert abs(_r[30.0][1] - 12.79) < 0.01 and _r[30.0][2] == 0.0, _r[30.0]
assert abs(_m[0.0][2] - 20.96) < 0.01 and abs(_m[22.0][2] - 14.30) < 0.01 and abs(_m[30.0][2] - 8.72) < 0.01, ROWSM
_common = [v for v in _m if v in _r]       # the Mach table's NeuralFoil column is the same line a where both have the speed
assert len(_common) >= 8, _common
for v in _common:
    assert abs(_m[v][1] - _r[v][1]) < 0.011, (v, _m[v], _r[v])
M0_INC = _r[0.0][1]                        # hover moment of the incompressible model, 22.83 N m


def frac(rows, col, m0=None):
    """f(V) = M(V) / m0, linear between grid points, held at the last point, never negative.
    m0 defaults to the line's own hover value (f(0) = 1)."""
    vs = [r[0] for r in rows]
    ms = [r[col] for r in rows]
    m0 = ms[0] if m0 is None else m0

    def f(V):
        if V != V:
            return 0.0
        if V <= vs[0]:
            return max(ms[0], 0.0) / m0
        if V >= vs[-1]:
            return max(ms[-1], 0.0) / m0
        for i in range(1, len(vs)):
            if V <= vs[i]:
                w = (V - vs[i - 1]) / (vs[i] - vs[i - 1])
                return max(ms[i - 1] + w * (ms[i] - ms[i - 1]), 0.0) / m0
    return f


# The station-Mach line is scaled by the incompressible hover value, so its hover authority is 20.96/22.83 = 0.918 of the
# rating, as the compressible model says (R-22 checks); the other two lines have f(0) = 1.
FUNCS = {"a": frac(ROWS, 1), "b": frac(ROWS, 2), "am": frac(ROWSM, 2, M0_INC)}
LINES = {"hover rating held (as the text)": None, "line a (335 W, rpm free)": "a", "line b (hover rpm)": "b",
         "line a with station Mach (AeroSandbox)": "am"}

# rpm-capped lines (tipthrust_rpmcap.py -> tipthrust-rpmcap-moments.txt): the driven pairs at min(335 W speed, c x hover rpm).
# TMV_MODE=caps runs only these (the edits are those regressed in the default run, so no regression block there).
CAPFILE = os.path.join(HERE, "tipthrust-rpmcap-moments.txt")
if os.path.exists(CAPFILE):
    with open(CAPFILE, encoding="utf-8") as fh:
        _hdr = fh.readline().split()[2:]
        _caps = [float(h.split("_")[1]) for h in _hdr if h.startswith("cap_")]
        _rows = [tuple(float(x) for x in ln.split()) for ln in fh if ln.strip()]
    assert _rows[0][0] == 0.0 and all(abs(m - M0_INC) < 0.01 for m in _rows[0][1:]), _rows[0]
    assert all(abs(r[1 + _caps.index(1.0)] - _r[r[0]][2]) < 0.01 for r in _rows if r[0] in _r), "cap 1.00 is not line b"
    for i, c in enumerate(_caps):
        FUNCS["c%.2f" % c] = frac(_rows, 1 + i)
if os.environ.get("TMV_MODE") == "caps":
    LINES = {"rpm cap %.2f x hover rpm, 335 W" % c: "c%.2f" % c for c in _caps if c > 1.0}

# thrust lapse (nose_thrust_lapse.py -> nose-thrust-lapse.txt): T_avail(V) / (1.066 W) for each nose family
# (nose at its hover power, rpm free, plus two tip pairs on line a). The envelope (lowest family) is used, and it is
# clamped at 1: the BEMT's 2-8 m/s points above the static value are not credited.
GFUNCS = {}
TLFILE = os.path.join(HERE, "nose-thrust-lapse.txt")
if os.path.exists(TLFILE):
    _tl = [ln.split() for ln in open(TLFILE, encoding="utf-8") if ln.strip() and not ln.startswith("#")]
    _tlrows = [(float(r[0]), min(1.0, min(float(x) for x in r[1:]))) for r in _tl]
    assert _tlrows[0][0] == 0.0 and abs(_tlrows[0][1] - 1.0) < 2e-3, _tlrows[0]
    GFUNCS["min"] = frac(_tlrows, 1, 1.0)
# rpm caps with the opposite pairs braked to 0.75 omega_fw (tipthrust_rpmcap_brake.py -> tipthrust-rpmcap-brake-moments.txt)
BRFILE = os.path.join(HERE, "tipthrust-rpmcap-brake-moments.txt")
_bcaps = []
if os.path.exists(BRFILE):
    with open(BRFILE, encoding="utf-8") as fh:
        _bcaps = [float(h.split("_")[1]) for h in fh.readline().split()[2:] if h.startswith("cap_")]
        _brows = [tuple(float(x) for x in ln.split()) for ln in fh if ln.strip()]
    assert _brows[0][0] == 0.0 and all(abs(m - M0_INC) < 0.01 for m in _brows[0][1:]), _brows[0]
    for i, c in enumerate(_bcaps):
        FUNCS["b%.2f" % c] = frac(_brows, 1 + i)
if os.environ.get("TMV_MODE") == "lapsecap":
    LINES = {}
    for c in (1.05, 1.10, 1.15, 1.20, 1.25):
        LINES["thrust lapse + rpm cap %.2f, idle pairs free-wheeling" % c] = ("lc%.2f" % c, "c%.2f" % c, "min")
    for c in _bcaps:
        LINES["thrust lapse + rpm cap %.2f, idle pairs braked" % c] = ("lb%.2f" % c, "b%.2f" % c, "min")
if os.environ.get("TMV_MODE") == "lapse":
    LINES = {"thrust lapse, hover rating held": ("lapse-hold", None, "min"),
             "thrust lapse + line a (335 W, rpm free)": ("lapse-a", "a", "min"),
             "thrust lapse + line a with station Mach": ("lapse-am", "am", "min")}


def build():
    src = inspect.getsource(td.kos)
    edits = (("def kos(", "def kos_mv("),
             ("t_after=40.0, cm0=0.056, cma=-0.48):", "t_after=40.0, cm0=0.056, cma=-0.48, mvcol=None, tlcol=None):"),
             ("        Th = Tmax if V < Vcr or vx < Vcr * 0.95 else min(Tmax, Dg)\n",
              "        Tav = Tmax if tlcol is None else Tmax * _G[tlcol](V)\n"
              "        Th = Tav if V < Vcr or vx < Vcr * 0.95 else min(Tav, Dg)\n"),
             ("        V = math.hypot(vx, vh)\n",
              "        V = math.hypot(vx, vh)\n"
              "        if not V < 1e3:  # numerically diverged (NaN or runaway): counted as a tumble\n"
              "            return dict(kayip=en_dusuk, dusus=dusus, doyma=doyma, ulasti=False, oturdu=False, theta_son=float('nan'),\n"
              "                        theta_trim=th_end / D2R, firladi=True, t_son=t, vh_son=float('nan'), q_son=float('nan'),\n"
              "                        al_max=al_max / D2R, M_ist_max=M_ist_max, t_cr=t_cr, h_cr=h_cr, diverged=True)\n"),
             ("        M = max(-M_kontrol, min(M_kontrol, M_ist))\n        if abs(M_ist) > M_kontrol:\n",
              "        Mlim = M_kontrol if mvcol is None else M_kontrol * _F[mvcol](V)\n"
              "        M = max(-Mlim, min(Mlim, M_ist))\n        if abs(M_ist) > Mlim:\n"))
    for o, n in edits:
        assert src.count(o) == 1, o
        src = src.replace(o, n)
    ns = dict(vars(td))
    ns["_F"] = FUNCS
    ns["_G"] = GFUNCS
    exec(compile(src, "kos_mv", "exec"), ns)
    return ns["kos_mv"]


KMV = build()
LAWS = (("C_m = 0", 0.0, 0.0), ("paper law", 0.056, -0.48), ("untwisted VLM fit", 0.0578, -0.4953),
        ("-9 deg washout VLM line", 0.0621, -0.5512), ("NP 0.869 m line", 0.063, -0.538),
        ("NP 0.888 m line", 0.076, -0.687), ("NP 0.855 m line", 0.053, -0.472), ("NP 0.831 m line", 0.037, -0.316))
MS, LTRS, BREAKS = (17.6, 19.0, 20.7, 23.0), (2.0, 3.0, 4.0, 6.0), (12.0, 14.0)
MGRID = tuple(sorted(set([round(17.6 + 0.2 * i, 1) for i in range(28)] + [20.7])))


def moments(tr):
    return MGRID if tr == 2.0 else MS


def one(job):
    ln, li, M, tr, a = job
    _, c0, s = LAWS[li]
    col = LINES[ln]
    if isinstance(col, tuple):                      # lapse mode: (tag, moment line, thrust line)
        r = KMV(M_kontrol=M, tr=tr, model="dogrusal", cm0=c0, cma=s, astall=a * D2R, mvcol=col[1], tlcol=col[2], **H)
        return job, r
    r = KMV(M_kontrol=M, tr=tr, model="dogrusal", cm0=c0, cma=s, astall=a * D2R, mvcol=col, **H)
    if col is None:
        ref = td.kos(M_kontrol=M, tr=tr, model="dogrusal", cm0=c0, cma=s, astall=a * D2R, **H)
        assert ref == r, job
    return job, r


if __name__ == "__main__":
    if os.environ.get("TMV_MODE") in ("lapse", "lapsecap"):  # the thrust edit is inert at tlcol=None: regress a subset
        for li in range(len(LAWS)):
            for tr_ in (2.0, 6.0):
                for M_ in (17.6, 23.0):
                    _, c0_, s_ = LAWS[li]
                    kw_ = dict(M_kontrol=M_, tr=tr_, model="dogrusal", cm0=c0_, cma=s_, astall=12.0 * D2R, **H)
                    assert KMV(mvcol=None, tlcol=None, **kw_) == td.kos(**kw_), (li, tr_, M_)
        print("Regression (lapse mode): with both edits off the rebuilt function equals kos() on 32 cases (asserted).")
        print("g(V) = T_avail/(1.066 W), envelope of the four nose families, clamped at 1:",
              " ".join("%g:%.3f" % (v, GFUNCS["min"](v)) for v in (0, 5, 10, 15, 20, 22, 24, 26, 28, 30)))
    grid = [(ln, li, M, tr, a) for ln in LINES for li in range(len(LAWS)) for tr in LTRS for M in moments(tr) for a in BREAKS]
    with Pool(4) as p:
        out = dict(p.map(one, grid, chunksize=4))
    print("Transition with the tip pairs' moment against airspeed (R-22 follow-up). Model kos() 06c46d0 + M_limit(V).")
    print("Regression: with the hover rating held, the rebuilt function equals kos() on every run of that block (asserted).")
    print("f(V) = M(V)/M(0):", " ".join("%g:%.2f/%.2f/%.2f" % (v, FUNCS["a"](v), FUNCS["b"](v), FUNCS["am"](v)) for v in (0, 5, 10, 15, 20, 22, 24, 26, 30)), "(line a / line b / line a station Mach)")
    print("columns: dip = lowest altitude below entry (m); fall = largest fall from an earlier high point (m); sat = time over the limit (s); Mdem = largest demand (N m)")
    tot = {ln: [0, 0, 0] for ln in LINES}
    for ln in LINES:
        print("\n=== %s" % ln)
        for li, (name, c0, s) in enumerate(LAWS):
            print("  %s (%.4f, %.4f)" % (name, c0, s))
            for tr in LTRS:
                for a in BREAKS:
                    rs = [out[(ln, li, M, tr, a)] for M in moments(tr)]
                    t = sum(r["firladi"] for r in rs)
                    u = sum((not r["firladi"]) and (not r["oturdu"]) for r in rs)
                    tot[ln][0] += len(rs); tot[ln][1] += t; tot[ln][2] += u
                    print("    t_r %3.1f break %2.0f | dip %5.2f  fall %5.2f-%5.2f  sat %5.2f  Mdem %5.1f | %d tumble, %d not settled"
                          % (tr, a, max(-r["kayip"] for r in rs), min(r["dusus"] for r in rs), max(r["dusus"] for r in rs),
                             max(r["doyma"] for r in rs), max(r["M_ist_max"] for r in rs), t, u))
                    ok = [r for r in rs if r["t_cr"] is not None]
                    am = " | alpha_max %5.2f-%5.2f deg" % (min(r["al_max"] for r in rs), max(r["al_max"] for r in rs))
                    if ok:
                        print("      95 %% of cruise speed in %d of %d runs | t_cr %5.2f-%5.2f s | h_cr %6.2f-%6.2f m"
                              % (len(ok), len(rs), min(r["t_cr"] for r in ok), max(r["t_cr"] for r in ok),
                                 min(r["h_cr"] for r in ok), max(r["h_cr"] for r in ok)) + am)
                    else:
                        print("      95 %% of cruise speed in 0 of %d runs" % len(rs) + am)
    print()
    for ln in LINES:
        dv = [k for k, r in out.items() if k[0] == ln and r.get("diverged")]
        print("%-34s numerically diverged (counted as tumbles): %d%s" % (ln, len(dv), (" e.g. " + str(dv[:3])) if dv else ""))
    for ln, (n, t, u) in tot.items():
        print("%-34s runs %d; tumbling %d; not settled %d" % (ln, n, t, u))
