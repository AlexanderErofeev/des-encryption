# Пример использования
from DES import DES

plaintext = "1010101010111100101000001010101010100000101000101010101010111010"  # 64-битный блок
key = "1010101010111100101000001010101010100000101000101010101010111010"  # 56-битный ключ

des = DES(key)

# Шифрование
ciphertext = des.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Дешифровка
decrypted_text = des.decrypt(ciphertext)
print("Decrypted text:", decrypted_text)
