#!/usr/bin/env python3

class Termin:
    """ Trida reprezentujici jeden termin """
    def __init__(self, datum, predmet, nazev, typ='termin', registrace_start=None, registrace_end=None):
        self.datum            = datum
        self.predmet          = predmet
        self.nazev            = nazev
        self.typ              = typ
        self.registrace_start = registrace_start
        self.registrace_end   = registrace_end
