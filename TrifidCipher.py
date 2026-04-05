import string

class TrifidCipher:
    def __init__(self, key="", period=5, extra_char="+"):
        self.period = period
        self.extra_char = extra_char
        self.alphabet = ""
        self.letter_to_coord = {}
        self.coord_to_letter = {}