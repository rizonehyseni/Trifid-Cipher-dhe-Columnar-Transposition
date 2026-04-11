import string

class TrifidCipher:
    def __init__(self, key="", period=5, extra_char="+"):
        self.period = period
        self.extra_char = extra_char
        self.alphabet = ""
        self.letter_to_coord = {}
        self.coord_to_letter = {}

    def _generate_mixed_alphabet(self, key, extra):
        key = key.upper().replace(" ", "")
        seen = set()
        alphabet = []
        
        for char in key:
            if char.isalpha() and char not in seen:
                alphabet.append(char)
                seen.add(char)
        
        for char in string.ascii_uppercase:
            if char not in seen:
                alphabet.append(char)
                seen.add(char)
        
        if extra not in seen:
            alphabet.append(extra)
        
        alphabet = alphabet[:27]
        while len(alphabet) < 27:
            alphabet.append(chr(65 + len(alphabet)))  
        
        return ''.join(alphabet)    