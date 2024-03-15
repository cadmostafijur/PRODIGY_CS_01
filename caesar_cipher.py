import random
def caesar_cipher(txt, st, encrypt=True):
    result = ""
    for ch in txt:
        if ch == " ":
            result += " "
        elif ch.isupper():
            if encrypt:
                result += chr((ord(ch) + st - 65) % 26 + 65)
            else:
                result += chr((ord(ch) - st - 65) % 26 + 65)
        else:
            if encrypt:
                result += chr((ord(ch) + st - 97) % 26 + 97)
            else:
                result += chr((ord(ch) - st - 97) % 26 + 97)
    return result
usertext = input("Enter the text: ")
print("Original Plain Text is : " + usertext)
# Encryption
st = random.randint(1, 25)
print("Shift pattern used for encryption: " + str(st))
print("Cipher Text is : " + caesar_cipher(usertext, st))
# Decryption
print("Decrypted Text is : " + caesar_cipher(caesar_cipher(usertext, st), st, encrypt=False))
