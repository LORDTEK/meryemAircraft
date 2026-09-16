# -*- coding: utf-8 -*-
"""Ayni calisma dizininde iki kosunun ayni anda baslamasini onler.

Gerekcesi olculdu, varsayilmadi: model calismasi iki kez baslatildi (biri
dusmus sanilan bir zincirden, biri elle) ve ikisi de ayni vaka dizinine
girdi. Ikinci kosunun kur() cagrisi birincinin dizinini SILIP yeniden
kurdu; birinci cozucu silinmis bir dizine yazmaya devam etti. Ustelik
sekiz MPI sureci dort cekirdekte yaristi. Sonuc sessizce cop olurdu --
hicbir hata mesaji yok, yalnizca yanlis sayilar.

Kilit, surec kimligini yazar. Bayat kilit (surec artik yok) sessizce
devralinir; canli kilit varsa cikilir.
"""
import os, sys


class Kilitli(Exception):
    pass


def _yasiyor(pid):
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ProcessLookupError):
        return False


class Kilit:
    def __init__(self, dizin, ad="kilit"):
        os.makedirs(dizin, exist_ok=True)
        self.yol = os.path.join(dizin, "." + ad)

    def __enter__(self):
        if os.path.exists(self.yol):
            try:
                pid = int(open(self.yol).read().strip())
            except (ValueError, OSError):
                pid = -1
            if pid == os.getpid():
                pass                       # ayni surec: yeniden girilebilir
            elif pid > 0 and _yasiyor(pid):
                raise Kilitli(
                    "bu dizinde zaten bir kosu var (pid %d): %s\n"
                    "Ayni dizine iki kosu girerse ikincisi birincinin\n"
                    "vakalarini siler ve iki cozucu dort cekirdekte yarisir."
                    % (pid, self.yol))
            else:
                sys.stderr.write("bayat kilit devralindi: %s\n" % self.yol)
        with open(self.yol, "w") as fh:
            fh.write(str(os.getpid()))
        return self

    def __exit__(self, *a):
        try:
            if os.path.exists(self.yol) and \
                    int(open(self.yol).read().strip()) == os.getpid():
                os.remove(self.yol)
        except (ValueError, OSError):
            pass
        return False
