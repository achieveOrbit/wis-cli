#!/usr/bin/env python3

import os

class Output:

    def __init__(self):
        # ESCAPE SEKVENCE
        # https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences
        self.CSI = '\033['         # Delka 2
        self.SGR = 'm'             # Delka 1
        self.RES = self.CSI + '0m' # Delka 2+2=4
        # BARVY
        self.colors = {
            'black'   : '30',
            'red'     : '31',
            'green'   : '32',
            'yellow'  : '33',
            'blue'    : '34',
            'magenta' : '35',
            'cyan'    : '36',
            'white'   : '37'
        }
        # POZADI
        self.background = {
            'black'   : '40',
            'red'     : '41',
            'green'   : '42',
            'yellow'  : '43',
            'blue'    : '44',
            'magenta' : '45',
            'cyan'    : '46',
            'white'   : '47'
        }
        # FORMATY
        self.format = {
            'bold'       : '01',
            'italic'     : '03',
            'underlined' : '04',
            'blink'      : '05'
        }

    ############################################################################
    # FUNKCE PRO TISK                                                          #
    ############################################################################

    def style(self, text, color=None, form=None, bkg=None):

        if (color is not None):
            text = self.CSI + self.colors[color] + self.SGR + text
        if (form is not None):
            text = self.CSI + self.format[form] + self.SGR + text
        if (bkg is not None):
            text = self.CSI + self.background[bkg] + self.SGR + text

        # Vratime se do puvodniho stavu at nemame explozi barev zejo :D
        text = self.RES + text + self.RES

        return text

    ############################################################################
    # FUNKCE PRO ZISKANI INFORMACI O TERMINALU                                 #
    ############################################################################

    def dimensions(self):
        h, w = os.popen('stty size', 'r').read().split()
        return (w, h)

    def get_width(self):
        return int((self.dimensions()[0]))

    def get_height(self):
        return int((self.dimensions()[1]))