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
