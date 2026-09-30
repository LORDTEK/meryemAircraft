# -*- coding: utf-8 -*-
"""Tur 180: 2. asama (korunan cumlelerin korunma durumu) -- yazarin karari E18 ("Hepsi onayli").
U 13 satir: kayittan cikar, "U" tablosuna yazilir (govdede aynen kalir, kisaltmayi bloklamaz).
C 1 satir: 2.3 "What follows is not a test of the whole framework." -- tasiyici ayni paragrafta; govdeden silinir.
Kayit kopyasi 3 satir silinir. 8.5 madde 1-4 kayda (K).  Kullanim: python3 v8_round180_apply.py KOK"""
import re, sys, os, glob
root = sys.argv[1] if len(sys.argv) > 1 else "."
cp = os.path.join(root, 'paper/v8-caveats.md'); C = open(cp, encoding='utf-8').read()
L = C.split('\n')
def take(step, text, who=None):
    hits = [i for i, l in enumerate(L) if l.startswith('| %d | %s |' % (step, text)) and (who is None or l.endswith('| %s |' % who))]
    assert len(hits) == 1, (step, text[:50], len(hits))
    return L.pop(hits[0])
U = [(2, "A claim that one architecture escapes a cost shared by the others is only meaningful if the cost is stated first, in terms that do not presume the escape.", "2.1"),
     (2, "Whether an architecture can decline the mismatch itself, rather than redistribute its consequences, is a different question", "2.1.7"),
     (3, "Read one at a time, these are ways to pay. Read as a conjunction, they are a condition.", "2.2.2"),
     (4, "The prediction is also mission-dependent, and the page would be weaker for hiding it.", "2.3"),
     (4, "Everything that follows is measured with it rather than added to it.", "2.3"),
     (5, "This section does not assert the outcome of a calculation it does not contain.", "3.4"),
     (6, "Nothing here is compared against a poor example.", "4.6"),
     (6, "The analysis chains are not matched, and this is the qualification that bounds what the comparison can be called.", "4.6"),
     (6, "The two halves are now on the table separately. Section 7 is where they are combined, and the combination is what this paper is for.", "4.8"),
     (7, 'The qualification "in the propulsor that carries the aircraft" is not decoration', "5.1"),
     (10, "That spread is itself the finding.", "6.1.4"),
     (12, "The evidence is one pair of design points, computed by one method, with the Bill 2 result resting on a section-drag model at low Reynolds number.", "6.3"),
     (15, "It is not a list of the study's open questions.", "8.1")]
urows = []
for st, t, sec in U:
    take(st, t)
    urows.append('| U | %d | %s | %s | E18 |' % (st, sec, t))
# kayit kopyalari
take(1, "The contribution is the architecture: a configuration arranged to change regime by rotating the airframe rather than its propulsors, and so carrying no mechanism that reorients a propulsor.", "K")
take(3, "It does not claim the trade is favourable.", "G")
dup = [i for i, l in enumerate(L) if l.startswith('| 7 | What this paper contributes is the architecture that brings')]
assert len(dup) == 2; L.pop(dup[1])
# C -> U (Tur 180 uygulamasinda bulundu): korunan tasiyici "It checks one falsifiable consequence ..." "It" ile basliyor ve oznesi
# kesilecek cumle ("What follows ..."). Kesilince "It" onceki cumlenin "a particular aircraft"ina baglaniyor. Cumle govdede kalir, U olur.
take(4, "What follows is not a test of the whole framework.")
urows.append('| U | 4 | 2.3 | What follows is not a test of the whole framework. | E18 (C yerine U; bkz. not) |')
# 8.5 madde 1-4 kayda
i = max(k for k, l in enumerate(L) if re.match(r'^\| 15 \| ', l))
L[i+1:i+1] = ['| 15 | It does not claim range against fixed-wing aircraft. | E18 |'.replace('| E18 |', '| G+C+D+Q+K |'),
              '| 15 | It does not claim vertical capability against rotorcraft. | G+C+D+Q+K |',
              '| 15 | It does not claim that the aircraft has no moving parts. | G+D+Q+K |',
              '| 15 | It does not claim mechanical simplicity. | G+D+Q+K |']
C = '\n'.join(L).rstrip('\n') + '\n\n' + '''## U — korumadan çıkarılan cümleler (Tur 180, yazar kararı E18)

Bu cümleler **gövdede aynen durur**; yalnız kısaltmayı bloklamaz. Sonraki bir kısaltma olağan oylamayla (dört okuyucu + Claude) yapılır.
Uyarı (Grok, Tur 179): 6.3 satırı kesilirse, arkasındaki korunan cümlenin *"It"* öznesi onarılmalıdır. Adım 4'ün iki satırı Tur 114'ün P71 birimidir
(*"The instrument is now fixed …"* korunur); ikincisi kesilecekse birim kuralı yeniden okunur.

| İşaret | Adım | Yer | Cümle | Karar |
|---|---:|---|---|---|
''' + '\n'.join(urows) + '\n\n**C yerine U (Tur 180):** yazar C işaretini onayladı (E18), ama uygulamada korunan taşıyıcının *"It checks one falsifiable consequence …"* *"It"* öznesinin kesilecek cümleye dayandığı görüldü; kesilince *"It"* önceki cümlenin *"a particular aircraft"*ına bağlanıyordu. Cümle gövdede kaldı, U oldu; ileride kesilirse taşıyıcının öznesi onarılmalı. Kayıt kopyaları (1 K, 3 G, 7 G ikinci) silindi.\n'
open(cp, 'w', encoding='utf-8').write(C)
# govde: C cumlesi
print('ok: U', len(urows), '(C U oldu); kopya 3; 8.5 kayit 4')
