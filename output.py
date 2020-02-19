#!/usr/bin/env python3

class Output:

    def __init__(self):
        # ESCAPE SEKVENCE
        # https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences
        self.CSI = '\033['
        self.SGR = 'm'
        self.RES = '\033[0m'
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
            'bold'       : '1',
            'italic'     : '3',
            'underlined' : '4',
            'blink'      : '5'
        }

    def style(self, text, color=None, form=None, font=None, bkg=None):

        if (color is not None):
            text = self.CSI + self.colors[color] + self.SGR + text
        if (form is not None):
            text = self.CSI + self.format[form] + self.SGR + text
        if (bkg is not None):
            text = self.CSI + self.background[bkg] + self.SGR + text

        # Make sure we don't mess up the users terminal :)
        text = self.RES + text + self.RES

        return text
