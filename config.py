#!/usr/bin/env python3

import configparser

class Config:

    def __init__(self):
        self.c = configparser.ConfigParser()
        self.c.read('config.ini')

    def get_login(self):
        return str(self.c['USER']['login'])

    def get_password(self):
        return str(self.c['USER']['heslo'])

    def get_termin_colours(self):
        chill = {
            "days"  : int(self.c['TERMINY']['chill']),
            "color" : self.c['TERMINY']['chill_color']
        }
        not_chill = {
            "days"  : int(self.c['TERMINY']['not_chill']),
            "color" : self.c['TERMINY']['not_chill_color']
        }
        panic = {
            "days"  : int(self.c['TERMINY']['panic']),
            "color" : self.c['TERMINY']['panic_color']
        }
        return [chill, not_chill, panic]
