"""
This program will be able to create and
decipher caesar cipher code encryption
"""
"""
This program will be able to create and decipher a caesar cipher code encryption
"""

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result


text = input('Write a secret message: ')

shift = 3
encrypted_text = caesar_cipher(text, shift)
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)