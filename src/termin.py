#!/usr/bin/env python3

# Python moduly
from datetime import datetime
# Nase moduly <3
from src.config import Config
from src.output import Output


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
        # Objekty, ktere budeme potrebovat zejo
        out = Output()
        con = Config()

        # Ziskani velikosti terminalu a podle toho vypocet sirky polozek
        w = out.get_width() - 40
        datum_space   = int(w*0.25)
        predmet_space = int(w*0.075)
        nazev_space   = int(w*0.35)
        typ_space     = int(w*0.1)

        # datum = out.style(self.datum, form='bold')
        td = self.time_delta()
        settings = con.get_termin_colours()

        # Obarveni polozek
        if (td <= settings[2]['days']):
            datum = out.style(self.datum, form='bold', color=settings[2]['color'])
        elif (td <= settings[1]['days']):
            datum = out.style(self.datum, form='bold', color=settings[1]['color'])
        elif (td <= settings[0]['days']):
            datum = out.style(self.datum, form='bold', color=settings[0]['color'])
        else:
            datum = out.style(self.datum, form='bold', color='white', bkg='blue') # Only for debugging

        # Tohle je pocet escape sekvenci, ktere potrebujeme, aby vsechny data mely stejnou sirku :)
        esc = len(datum)-10-8

        zaklad = ("|{d:^{ds}}|{p:^{ps}}|{n:^{ns}}|{t:^{ts}}|".format(d=datum,        ds=datum_space+esc,
                                                                     p=self.predmet, ps=predmet_space,
                                                                     n=self.nazev,   ns=nazev_space,
                                                                     t=self.typ,     ts=typ_space))

        if (self.registrace_start is not None):
            zaklad = zaklad + ("{d:^{ds}}|".format(d=self.registrace_start, ds=datum_space))
        if (self.registrace_end is not None):
            zaklad = zaklad + ("{d:^{ds}}|".format(d=self.registrace_end, ds=datum_space))

        print(zaklad)