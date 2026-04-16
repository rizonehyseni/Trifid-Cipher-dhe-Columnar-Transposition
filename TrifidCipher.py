import string

class TrifidCipher:
    def __init__(self, period=5):
        self.period = period

        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ+"

        self.letter_to_coord = {}
        self.coord_to_letter = {}
        self._build_cube()

    def _build_cube(self):
        idx = 0
        for layer in range(1, 4):
            for row in range(1, 4):
                for col in range(1, 4):
                    letter = self.alphabet[idx]
                    coord = (layer, row, col)

                    self.letter_to_coord[letter] = coord
                    self.coord_to_letter[coord] = letter
                    idx += 1

    def _prepare_text(self, text):
        text = text.upper()
        text = text.replace(" ", "+")
        return ''.join(c for c in text if c in self.letter_to_coord)

