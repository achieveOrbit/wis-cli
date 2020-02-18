#!/usr/bin/env python3

import argparse

parser    = argparse.ArgumentParser(description='WIS Command Line Interface')
subparser = parser.add_subparsers(dest='subparser_name')

# sp_t = SubParser pro Terminy
sp_t = subparser.add_parser('terminy')

# Pridavani exkluzivnich argumentu
sp_t_predmety = sp_t.add_mutually_exclusive_group()
sp_t_predmety.add_argument('-a',
                           action='store_true',
                           dest='show_all',
                           help="Ukazat vsechny terminy, vcetne tymovych a zapoctu")
sp_t_predmety.add_argument('-p',
                           dest='predmet',
                           help="Ukazat terminy jen pro urcity predmet")
sp_t_predmety.add_argument('-z',
                           action='store_true',
                           dest='show_zapocty',
                           help="Ukazat pouze terminy zapoctu")
sp_t.add_argument('-g',
                  action='store_true',
                  dest='group_by_subject',
                  help='Rozdelit terminy podle dat')

# sp_m = SubParser pro Mistnosti
sp_m = subparser.add_parser('mistnosti')
sp_m.add_argument('-m',
                  choices=['C127.1', 'C128', 'C211', 'G104', 'S207'],
                  help="Mistnost, pro kterou ukazat rozvrh")

args = parser.parse_args()
print(args)
