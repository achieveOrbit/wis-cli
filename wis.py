#!/usr/bin/env python3

from argparser import ArgParser
from output import Output
from termin import Termin

if __name__ == "__main__":
    parser  = ArgParser()
    out     = Output()
    options = parser.parse()

    if (options.subparser_name=="terminy"):
        for x in range(1, 29):
            t = Termin(("2020-02-{:02d}".format(x)), 'IPP', 'Pokusne odevzdani', 'termin', '2020-02-20', '2020-02-25')
    elif (options.subparser_name=="mistnosti"):
        print(out.style('Staram se o mistnosti', color='green', form='bold'))
