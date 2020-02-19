#!/usr/bin/env python3

from output import Output
from datetime import datetime

class Termin:
    """ Trida reprezentujici jeden termin """
    def __init__(self, datum, predmet, nazev, typ='termin', registrace_start=None, registrace_end=None):
        self.datum            = datum
        self.predmet          = predmet
        self.nazev            = nazev
        self.typ              = typ
        self.registrace_start = registrace_start
        self.registrace_end   = registrace_end
        # print(self.time_delta())
        self.pretty_print()

    def time_delta(self):
        d1 = datetime.strptime(self.datum, "%Y-%m-%d")
        return abs((datetime.now() - d1).days)

    def pretty_print(self):

        out = Output()

        # Ziskani velikosti terminalu a podle toho vypocet sirky polozek
        w = out.get_width()
        w = int(w) - 20
        datum_space   = int(w*0.20)
        predmet_space = int(w*0.0625)
        nazev_space   = int(w*0.4375)
        typ_space     = int(w*0.0625)

        # datum = out.style(self.datum, form='bold')
        td = self.time_delta()

        # Obarveni polozek
        if (td >= 10):
            datum = out.style(self.datum, form='bold', color='green')
        elif (td < 10 and td > 5):
            datum = out.style(self.datum, form='bold', color='yellow')
        else:
            datum = out.style(self.datum, form='bold', color='red')

        zaklad = ("|{d:^{ds}}|{p:^{ps}}|{n:^{ns}}|{t:^{ts}}|".format(d=datum,        ds=datum_space,
                                                                     p=self.predmet, ps=predmet_space,
                                                                     n=self.nazev,   ns=nazev_space,
                                                                     t=self.typ,     ts=typ_space))

        if (self.registrace_start is not None):
            zaklad = zaklad + ("{d:^{ds}}|".format(d=self.registrace_start, ds=datum_space))
        if (self.registrace_end is not None):
            zaklad = zaklad + ("{d:^{ds}}|".format(d=self.registrace_end, ds=datum_space))

        print(zaklad)