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

    def encrypt(self, plaintext):
        text = self._prepare_text(plaintext)
        if not text:
            return ""

        coords = [self.letter_to_coord[c] for c in text]
        result = []

        for i in range(0, len(coords), self.period):
            group = coords[i:i + self.period]
            n = len(group)

            layers = [c[0] for c in group]
            rows   = [c[1] for c in group]
            cols   = [c[2] for c in group]

            combined = layers + rows + cols

            for j in range(0, 3 * n, 3):
                triplet = (combined[j], combined[j+1], combined[j+2])
                result.append(self.coord_to_letter[triplet])

        return ''.join(result)

    def decrypt(self, ciphertext):
        text = self._prepare_text(ciphertext)
        if not text:
            return ""

        coords = [self.letter_to_coord[c] for c in text]
        result = []

        for i in range(0, len(coords), self.period):
            group = coords[i:i + self.period]
            n = len(group)

            flat = []
            for c in group:
                flat.extend(c)

            pos = 0
            for _ in range(n):
                layer = flat[pos]
                row   = flat[pos + n]
                col   = flat[pos + 2 * n]

                triplet = (layer, row, col)
                result.append(self.coord_to_letter[triplet])
                pos += 1

        return ''.join(result).replace("+", " ")


if __name__ == "__main__":
    cipher = TrifidCipher(period=5)

    plaintext = "HELLO WORLD"

    encrypted = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(encrypted)

    print("Plaintext :", plaintext)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
    print("Alphabet  :", cipher.alphabet)