#!/usr/bin/env python3

import sys

from argparser import ArgParser
from termin import Termin

if __name__ == "__main__":
    parser = ArgParser()
    options = parser.parse()

    if (options.subparser_name=="terminy"):
        print("Staram se o terminy")
    elif (options.subparser_name=="mistnosti"):
        print("Staram se o mistnoti")