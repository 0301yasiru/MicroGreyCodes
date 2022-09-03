# !/usr/bin/python
# this is a simple tutorial about linux terminal coloring

class COLORS:
    def __init__(self):
        self.Red     = '\u001b[31m'
        self.Green   = '\u001b[32m'
        self.Yellow  = '\u001b[33m'
        self.White   = '\u001b[37m'

        self.RESET   = '\u001b[0m'
        self.BOLD    = '\u001b[1m'
        self.ULINE   = '\u001b[4m'