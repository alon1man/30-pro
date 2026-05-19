def encrypt_vigenere(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    key = key.lower()
    ki = 0

    for char in text:
        if char.lower() in alpha:
            # Shift = position of text char + position of key char
            placement = alpha.find(char.lower())
            shiftlike_ofchar = alpha.find(key[ki % len(key)])
            new_char = alpha[(placement + shiftlike_ofchar) % 26]

            result += new_char.upper() if char.isupper() else new_char
            ki += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    key = key.lower()
    ki = 0

    for char in text:
        if char.lower() in alpha:
            placement = alpha.find(char.lower())
            shiftlike_ofchar = alpha.find(key[ki % len(key)])

            # כל השורות האלו חייבות להיות בתוך ה-if
            new_char = alpha[(placement - shiftlike_ofchar) % 26]
            result += new_char.upper() if char.isupper() else new_char
            ki += 1
        else:
            # כאן מטפלים בתווים שהם לא אותיות (כמו רווחים)
            result += char
            
    return result