class DES:
    initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                           60, 52, 44, 36, 28, 20, 12, 4,
                           62, 54, 46, 38, 30, 22, 14, 6,
                           64, 56, 48, 40, 32, 24, 16, 8,
                           57, 49, 41, 33, 25, 17, 9, 1,
                           59, 51, 43, 35, 27, 19, 11, 3,
                           61, 53, 45, 37, 29, 21, 13, 5,
                           63, 55, 47, 39, 31, 23, 15, 7]

    final_permutation = [40, 8, 48, 16, 56, 24, 64, 32,
                         39, 7, 47, 15, 55, 23, 63, 31,
                         38, 6, 46, 14, 54, 22, 62, 30,
                         37, 5, 45, 13, 53, 21, 61, 29,
                         36, 4, 44, 12, 52, 20, 60, 28,
                         35, 3, 43, 11, 51, 19, 59, 27,
                         34, 2, 42, 10, 50, 18, 58, 26,
                         33, 1, 41, 9, 49, 17, 57, 25]

    def __init__(self, key: str):
        self.key = key

    @staticmethod
    def permute(block, table):
        return ''.join(block[i - 1] for i in table)

    def feistel_function(self, half_block, subkey):
        # Простая Feistel-функция: XOR половины блока с ключом (упрощение)
        return ''.join(str(int(a) ^ int(b)) for a, b in zip(half_block, subkey))

    def generate_subkeys(self):
        # Простая генерация субключей (в реальном DES это сложнее)
        return [self.key[i:] + self.key[:i] for i in range(16)]

    def process_block(self, block, subkeys):
        block = self.permute(block, self.initial_permutation)
        left, right = block[:32], block[32:]

        for subkey in subkeys:
            temp = right
            right = ''.join(str(int(a) ^ int(b)) for a, b in zip(left, self.feistel_function(right, subkey)))
            left = temp

        block = self.permute(right + left, self.final_permutation)
        return block

    def encrypt(self, plaintext: str):
        subkeys = self.generate_subkeys()
        blocks = [plaintext[i:i + 64] for i in range(0, len(plaintext), 64)]
        return ''.join(self.process_block(block, subkeys) for block in blocks)

    def decrypt(self, ciphertext: str):
        subkeys = self.generate_subkeys()[::-1]  # Инвертируем порядок субключей
        blocks = [ciphertext[i:i + 64] for i in range(0, len(ciphertext), 64)]
        return ''.join(self.process_block(block, subkeys) for block in blocks)
