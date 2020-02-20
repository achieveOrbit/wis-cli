#!/usr/bin/env python3

# Python moduly
from datetime import datetime
# Nase moduly <3
from src.config import Config
from src.output import Output


class Terminy:

    def __init__(self):
        self.out = Output()
        self.dimensions = self.out.dimensions()
        self.terminy = []
        self.settings = Config().get_termin_colours()
        self.max_width = 0

    def add_termin(self, datum, predmet, nazev, typ='termin', registrace_start=None, registrace_end=None):
        self.terminy.append(
            {
                "datum"     : datum,
                "predmet"   : predmet,
                "nazev"     : nazev,
                "typ"       : typ,
                "reg_start" : registrace_start,
                "reg_end"   : registrace_end,
                "delta"     : self.time_delta(datum)
            }
        )
        if (len(nazev) > self.max_width):
            self.max_width = len(nazev)
        # self.datum            = datum
        # self.predmet          = predmet
        # self.nazev            = nazev
        # self.typ              = typ
        # self.registrace_start = registrace_start
        # self.registrace_end   = registrace_end
        # # print(self.time_delta())
        # self.pretty_print()

    def time_delta(self, datum):
        d1 = datetime.strptime(datum, "%Y-%m-%d")
        return abs((datetime.now() - d1).days)

    def pretty_print(self):
        # Objekty, ktere budeme potrebovat zejo
        out = Output()

        # Ziskani velikosti terminalu a podle toho vypocet sirky polozek
        w = out.get_width() - 40
        datum_space   = int(w*0.15)
        predmet_space = int(w*0.075)
        # nazev_space   = int(w*0.35)
        nazev_space = self.max_width+2
        typ_space     = int(w*0.1)

        # datum = out.style(self.datum, form='bold')

        for t in self.terminy:
            # Obarveni polozek
            if (t["delta"] <= self.settings[2]['days']):
                datum = out.style(t["datum"], form='bold', color=self.settings[2]['color'])
            elif (t["delta"] <= self.settings[1]['days']):
                datum = out.style(t["datum"], form='bold', color=self.settings[1]['color'])
            else:
                datum = out.style(t["datum"], form='bold', color=self.settings[0]['color']) # Only for debugging

            # Tohle je pocet escape sekvenci, ktere potrebujeme, aby vsechny data mely stejnou sirku :)
            esc = len(datum)-10-8

            zaklad = ("|{d:^{ds}}|{p:^{ps}}|{n:^{ns}}|{t:^{ts}}|".format(d=datum,        ds=datum_space+esc,
                                                                        p=t["predmet"],  ps=predmet_space,
                                                                        n=t["nazev"],    ns=nazev_space,
                                                                        t=t["typ"],      ts=typ_space))

            if (t["reg_start"] is not None):
                zaklad = zaklad + ("{d:^{ds}}|".format(d=t["reg_start"], ds=datum_space))
            else:
                zaklad = zaklad + datum_space*(" ") + "|"
            if (t["reg_end"] is not None):
                zaklad = zaklad + ("{d:^{ds}}|".format(d=t["reg_end"], ds=datum_space))
            else:
                zaklad = zaklad + datum_space*(" ") + "|"

            print(zaklad)