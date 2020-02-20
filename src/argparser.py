#!/usr/bin/env python3

import argparse


class ArgParser:

    def __init__(self):
        """ Stara se o parsovani argumentu """
        self.parser = argparse.ArgumentParser(prog='wis.py', description='WIS Command Line Interface')
        self.subparser = self.parser.add_subparsers(dest='subparser_name')
        self.create_version()
        self.create_terminy()
        self.create_mistnosti()

    def parse(self):
        return self.parser.parse_args()

    def create_version(self):
        self.parser.add_argument('-v', '--version', action='version', version='WIS-CLI v0.0.1')

    def create_terminy(self):
        """ Vytvari subparser pro terminy"""
        # sp_t = SubParser pro Terminy
        sp_t = self.subparser.add_parser('terminy')
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

    def create_mistnosti(self):
        """ Vytvari subparser pro mistnosti """
        # sp_m = SubParser pro Mistnosti
        sp_m = self.subparser.add_parser('mistnosti')
        sp_m.add_argument('-m',
                        choices=['C127.1', 'C128', 'C211', 'G104', 'S207'],
                        help="Mistnost, pro kterou ukazat rozvrh")
