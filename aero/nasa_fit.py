"""Supplement S3: does the paper's power-ratio scaling, Eq. (2), explain NASA's independently sized designs?

Source: Johnson & Silva 2022, The Aeronautical Journal 126(1295), Table 3 (p. 70), read first-hand.
Eq. (2): P_hover/P_cruise = sqrt(DL/(2 rho)) * (L/D)_e / V / FM, with (L/D)_e = (L/D) * eta_p.
NASA UAM mission (Sec. 5.0 of the source): takeoff at 6,000 ft ISA, cruise 4,000 ft above ground level.
Hover sets the regressor, so rho is taken at the takeoff altitude.  (An earlier version used 5,000 ft
ISA+20 C, the atmosphere of the source's earlier air-taxi mission of Table 2; since rho is common to all
nine vehicles it scales x uniformly, so R^2 and the percentage errors are unchanged and k and FM_eff
scale by sqrt(rho_new/rho_old).)  Installed power includes NASA's margins
(sizing conditions, OEI), so one effective constant k = 1/FM_eff is fitted, not assumed.
"""
import math

LB, FT, HP, KT = 4.44822, 0.3048, 745.7, 0.514444
p = 101325 * (1 - 2.25577e-5 * 6000 * FT) ** 5.25588          # 6,000 ft pressure
T = 288.15 - 0.0065 * 6000 * FT                                 # ISA
rho = p / (287.05 * T)

# name, DL lb/ft2, L/De, Vbr kt, hover-sized installed power hp, DGW lb   (Table 3)
rows = [("QSMR turboshaft", 4, 5.4, 100, 2 * 241, 3951),
        ("QSMR electric", 3.5, 6.0, 84, 2 * 272, 5980),
        ("Side-by-side turboshaft", 5, 5.9, 103, 2 * 234, 3665),
        ("Side-by-side electric", 4, 7.2, 89, 2 * 234, 5547),
        ("Quadrotor turboshaft", 3.5, 4.9, 112, 2 * 294, 3678),
        ("Quadrotor electric", 3, 5.8, 91, 4 * 181, 7221),
        ("Lift+cruise turbo-electric", 11.6, 8.5, 81, 8 * 126, 7271),   # lift motors only
        ("Lift+cruise electric", 15.1, 7.9, 83, 8 * 189, 9482),        # lift motors only
        ("Tiltwing turbo-electric", 20, 8.6, 148, 8 * 244, 6584)]

xs, ys = [], []
print(f"rho(6000 ft, ISA) = {rho:.4f} kg/m3")
print(f"{'design':28s} {'x=sqrt(DL/2rho)LDe/V':>20s} {'NASA P_inst/P_cr':>17s}")
for name, dl, lde, v, php, dgw in rows:
    W = dgw * LB; V = v * KT; DL = dl * LB / FT ** 2
    p_cr = W * V / lde
    x = math.sqrt(DL / (2 * rho)) * lde / V
    y = php * HP / p_cr
    xs.append(x); ys.append(y)
    print(f"{name:28s} {x:20.3f} {y:17.3f}")

# one-constant fit through the origin: y = k x
k = sum(a * b for a, b in zip(xs, ys)) / sum(a * a for a in xs)
res = [b - k * a for a, b in zip(xs, ys)]
my = sum(ys) / len(ys)
r2 = 1 - sum(r * r for r in res) / sum((b - my) ** 2 for b in ys)
print(f"\nfit y = k x : k = {k:.3f} (effective 1/FM incl. margins -> FM_eff = {1/k:.3f}), R^2 = {r2:.3f}")
for (name, *_), a, b in zip(rows, xs, ys):
    print(f"  {name:28s} predicted {k*a:6.2f}  NASA {b:6.2f}  error {100*(k*a-b)/b:+6.1f}%")

# Decomposition: is NASA's installed power hover-governed?  FM_eff = ideal hover power / installed power.
print("\nhover-only check: FM_eff = W*sqrt(DL/2rho) / P_installed  (0.6-0.8 would mean hover-governed)")
for name, dl, lde, v, php, dgw in rows:
    W = dgw * LB; DL = dl * LB / FT ** 2
    print(f"  {name:28s} FM_eff {W * math.sqrt(DL / (2 * rho)) / (php * HP):.3f}")
