class ColumnarTranspositionCipher:
    def __init__(self, key, filler='X'):
        self.key = key.upper().replace(" ", "")
        self.filler = filler.upper()


def encrypt(self, plaintext):
    plaintext = ''.join(c for c in plaintext.upper() if c.isalpha())

