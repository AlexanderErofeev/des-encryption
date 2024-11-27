from DES import DES


key = "1010101010111100101000001010101010100000101000101010101010111010"  # 56-битный ключ

des = DES(key)

message = "Привет, зашифруй меня!!!"
print("Исходное сообщение:", message)

# Шифрование
ciphertext = des.encrypt_message(message)
print("Зашифрованное сообщение:", ciphertext)

# Дешифровка
decrypted_message = des.decrypt_message(ciphertext)
print("Расшифрованное сообщение:", decrypted_message)
