class ColumnarTranspositionCipher:
    def __init__(self, key, filler='X'):
        self.key = key.upper().replace(" ", "")
        self.filler = filler.upper()
        self.col_order = self._get_column_order()


    def _get_column_order(self):
        return sorted(range(len(self.key)), key=lambda i: (self.key[i], i))
    
def encrypt(self, plaintext):
    plaintext = ''.join(c for c in plaintext.upper() if c.isalpha())


    key_len = len(self.key)
    if len(plaintext) % key_len != 0:
        padding = key_len - (len(plaintext) % key_len)
        plaintext += self.filler * padding


    grid = [
        plaintext[i:i + key_len]
        for i in range(0, len(plaintext), key_len)
    ]

    ciphertext = ''

    for col in self.col_order:
        for row in grid:
            ciphertext += row[col]

    return ciphertext

def decrypt(self, ciphertext):
        ciphertext = ''.join(c for c in ciphertext.upper() if c.isalpha() or c == self.filler)
        
        if not ciphertext:
            return ""

        key_len = len(self.key)
        num_rows = len(ciphertext) // key_len

grid = [[''] * key_len for _ in range(num_rows)]
idx = 0

for col_idx in self.col_order:
            for row in range(num_rows):
                grid[row][col_idx] = ciphertext[idx]
                idx += 1

        plaintext = ''
for row in range(num_rows):
            plaintext += ''.join(grid[row])
              plaintext = plaintext.rstrip(self.filler)
        return plaintext
    if __name__ == "__main__":
    key = "Trimethoprimumsulfamethoxazolum"
    