#!/usr/bin/env python3

from src.argparser import ArgParser
from src.output import Output
from src.terminy import Terminy

if __name__ == "__main__":
    parser  = ArgParser()
    out     = Output()
    options = parser.parse()

    if (options.subparser_name=="terminy"):
        t = Terminy()
        for x in range(1, 29):
            t.add_termin(("2020-02-{:02d}".format(x)), 'IPP', 'Pokusne odevzdani', 'termin', '2020-02-20', '2020-02-25')
        t.pretty_print()
    elif (options.subparser_name=="mistnosti"):
        print(out.style('Staram se o mistnosti', color='green', form='bold'))
