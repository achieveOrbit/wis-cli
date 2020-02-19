#!/usr/bin/env python3

from argparser import ArgParser
from output import Output
from termin import Termin

if __name__ == "__main__":
    parser = ArgParser()
    out = Output()
    options = parser.parse()

    if (options.subparser_name=="terminy"):
        # print('\033[1m\033[31mStaram se o terminy')
        print(out.style('Text1'))
        print(out.style('Text2', color='red'))
        print(out.style('Text3', form='bold'))
        print(out.style('Text4', color='yellow', form='underlined'))
        print(out.style('Text5', color='white', bkg='blue'))
    elif (options.subparser_name=="mistnosti"):
        print("Staram se o mistnoti")