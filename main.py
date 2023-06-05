def XOR_cipher(msg, key):
    """Функция для зашифровки сообщения 'msg' с помощью ключа 'key'"""
    res = ""
    for i in range(len(msg)):
        res += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
    return res

def XOR_uncipher(msg, key):
    """Функция для расшифровки сообщения 'msg' с помощью ключа 'key'"""
    res = ""
    for i in range(len(msg)):
        res += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
    return res
msg = "Привет!"
key = "Секрет"


# Зашифровать сообщение
ciphered = XOR_cipher(msg, key)
print("Зашифрованное сообщение:", ciphered)

# Расшифровать сообщение
unciphered = XOR_uncipher(ciphered, key)
print("Расшифрованное сообщение:", unciphered)