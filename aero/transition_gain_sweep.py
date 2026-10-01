"""Gecis kaybi: uc referans profil, kazanc taramasi ve surukleme duyarliligi (Tur 208, Ek S10).

Ek S10'un "kontrolcunun bir yan urunu degil" cumlesinin calismasi. transition_dynamics.kos()
PD kazanclarini (Kp 25, Kd 10) sabit tutuyor; arsivdeki "17 m'ye ulasiyor" taramasinin betigi
depoda yok. Bu betik kos()'un bir kopyasini kazanclar parametre olacak bicimde kurar ve
taramayi yeniden uretir. Kosullar (cikti basinda): 50 kg tasarim, M 23,0 N m, t_r 2 s,
giris tirmanisi 5 m/s, aerodinamik moment sifir.
"""
import os, sys
BURA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURA)
src = open(os.path.join(BURA, "transition_dynamics.py")).read().split("if __name__")[0]
src = src.replace("def kos(m, S, c_ort, Iyy, AR, M_kontrol, tr, Vcr, w0=5.0,",
                  "def kos(m, S, c_ort, Iyy, AR, M_kontrol, tr, Vcr, w0=5.0, kp=25.0, kd=10.0,")
eski = "Iyy * (25.0 * (th_ref - th) + 10.0 * (q_ref - q))"
assert src.count(eski) == 1, "transition_dynamics.kos() degismis; bu betik guncellenmeli"
src = src.replace(eski, "Iyy * (kp * (th_ref - th) + kd * (q_ref - q))")
ns = {"__file__": os.path.join(BURA, "transition_dynamics.py")}
exec(src, ns)
kos, HAFIF = ns["kos"], ns["HAFIF"]

print("KOSULLAR: 50 kg (HAFIF), M = 23,0 N m, t_r = 2 s, giris tirmanisi 5 m/s, C_m = 0; CD0 0,0248, e 0,85")
print("PROFILLER (Kp 25, Kd 10)")
for p, ad in (("dogrusal", "dogrusal"), ("duz", "yumusak 3t^2-2t^3"), ("bang", "bang-bang")):
    r = kos(**HAFIF, M_kontrol=23.0, tr=2.0, profil=p)
    print("  %-20s kayip %6.2f m   doyma %.3f s" % (ad, -r["kayip"], r["doyma"]))
print("KAZANC TARAMASI (bang-bang; Kp x k, Kd x sqrt(k))")
for k in (1, 2, 4, 8, 16):
    r = kos(**HAFIF, M_kontrol=23.0, tr=2.0, profil="bang", kp=25.0 * k, kd=10.0 * k ** 0.5)
    print("  k = %2d   kayip %6.2f m   doyma %.3f s" % (k, -r["kayip"], r["doyma"]))
print("SURUKLEME (e 0,817): kayip farki, m")
for p in ("dogrusal", "duz", "bang"):
    b = kos(**HAFIF, M_kontrol=23.0, tr=2.0, profil=p)["kayip"]
    d = [kos(**HAFIF, M_kontrol=23.0, tr=2.0, profil=p, CD0=c, e=0.817)["kayip"] - b for c in (0.0285, 0.0381)]
    print("  %-9s CD0 0,0285: %+.3f   CD0 0,0381: %+.3f" % (p, d[0], d[1]))
