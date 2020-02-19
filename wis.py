#!/usr/bin/env python3

from argparser import ArgParser
from output import Output
from termin import Termin

if __name__ == "__main__":
    parser = ArgParser()
    out = Output()
    options = parser.parse()

    if (options.subparser_name=="terminy"):
        print(out.style('Staram se o terminaly', color='red', form='bold'))
    elif (options.subparser_name=="mistnosti"):
        print(out.style('Staram se o mistnosti', color='green', form='bold'))