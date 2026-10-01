#!/usr/bin/env python3
"""Okuyucu paketi: guncel govde (birlesik gorunum) + dergi eki taslagi, tek dosya.

Yazar, Tur 206: "Eksik bilgiyle verimli calisma olmaz." Okuyucular depo dosyalarini acamiyor;
govdenin tamami en son Tur 188-190'da tur metnine girmisti. Bu betik, tur metnine eklenecek
tek dosyayi uretir: paper/submission/reader-packet.md. Her turda yeniden uretilir.
"""
import re, subprocess, pathlib
K = pathlib.Path(__file__).resolve().parents[2]
govde = (K / "paper/v8/ASSEMBLED.md").read_text()
govde = govde.split("\n", 1)[1]                      # uretec basligi
ek = (K / "paper/submission/supplement-src.md").read_text()
ek = ek.split("\n", 1)[1]
ek = re.sub(r"<!--(.*?)-->", lambda m: "> *Provenance and changes:* " + " ".join(x.strip() for x in m.group(1).split("\n")).strip(), ek, flags=re.S)
ek = re.sub(r"^(#+) ", lambda m: "#" + m.group(1) + " ", ek, flags=re.M)
h = subprocess.run(["git", "-C", str(K), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
n_g, n_e = len(govde.split()), len(ek.split())
out = f"""# meryemAircraft — reader packet: the current body and the journal supplement draft

> Generated from the repository at commit `{h}` (branch `claude/ecstatic-cori-6w30at`). It is a reference for reading the round texts, not a task in itself.
>
> **Part 1** is the current body ({n_g} words) in the assembled numbering the round texts use (*"Section 5.2"*). The submission generator converts this to the journal's form (Roman-numeral sections, *Sec.*, numbered citations, American spelling, one figure); the wording is the same.
>
> **Part 2** is the journal supplement as drafted so far ({n_e} words), with each passage's provenance note.

---

# Part 1. The body

{govde.strip()}

---

# Part 2. The journal supplement (draft so far)

{ek.strip()}
"""
(K / "paper/submission/reader-packet.md").write_text(out)
print("reader-packet.md:", n_g, "+", n_e, "words, commit", h)

# Parcalar (yazar, Tur 208: Qwen dosya alamiyor, tek parca metin olarak da yapistirilamiyor).
# Paket ~6 000 sozcukluk parcalara bolunur; her parca kendi basligini ve sirasini tasir.
parcalar, simdiki, n = [], [], 0
for para in out.split("\n\n"):
    w = len(para.split())
    if n + w > 6000 and simdiki:
        parcalar.append("\n\n".join(simdiki)); simdiki, n = [], 0
    simdiki.append(para); n += w
if simdiki:
    parcalar.append("\n\n".join(simdiki))
for f in (K / "paper/submission").glob("reader-packet-part*.md"):
    f.unlink()
for i, t in enumerate(parcalar, 1):
    bas = f"> **Reader packet, part {i} of {len(parcalar)}** (commit `{h}`). Read all parts before answering; the round text says what to judge.\n\n"
    (K / f"paper/submission/reader-packet-part{i}.md").write_text(bas + t + "\n")
print("parcalar:", [len(t.split()) for t in parcalar])
